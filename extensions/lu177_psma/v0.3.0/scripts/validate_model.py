"""Validate local model structure and records. Requires Python 3 and jsonschema >=4.
No network, patient submission, file upload or clinical recommendation is performed.
"""
import json, sys, copy, collections, datetime, math
from pathlib import Path
try:
    import jsonschema
except ImportError:
    print('Install the validation dependency: python -m pip install jsonschema');raise

ROOT=Path(__file__).resolve().parents[1]
S={p.stem:json.loads(p.read_text()) for p in (ROOT/'schemas').glob('*.json')}
def flatlinks(schema):
    return [c for l in schema.get('links',[]) for c in l.get('subgroup',[l])]
def ref_list(value):
    return value if isinstance(value,list) else [value] if isinstance(value,dict) else []
def refs(record,schema):
    for l in flatlinks(schema):
        for ref in ref_list(record.get(l['name'])):yield l,ref
def record_key(r):return (r['type'],r.get('submitter_id',r.get('id',r.get('code',r.get('name','ROOT')))))
def validate_records(records):
    errors=[];index={};by_uuid={};by_code={}
    for r in records:
        n=r.get('type');key=record_key(r)
        if n not in S:errors.append('Unknown node '+str(n));continue
        if key in index:errors.append('Duplicate record key '+str(key))
        index[key]=r
        if r.get('id'):by_uuid[(n,r['id'])]=r
        if r.get('code'):by_code[(n,r['code'])]=r
        for e in jsonschema.Draft4Validator(S[n],format_checker=jsonschema.FormatChecker()).iter_errors(r):errors.append(str(key)+' '+str(list(e.path))+': '+e.message)
        for k,p in S[n]['properties'].items():
            if k not in r or r[k] is None:continue
            if p.get('format')=='date-time':
                try:
                    d=datetime.datetime.fromisoformat(r[k].replace('Z','+00:00'))
                    if d.tzinfo is None:raise ValueError('timezone absent')
                except Exception:errors.append(str(key)+' invalid ISO datetime '+k)
            if p.get('format')=='date':
                try:datetime.date.fromisoformat(r[k])
                except Exception:errors.append(str(key)+' invalid ISO date '+k)
        if len(r.get('missing_properties',[]))!=len(r.get('missing_reasons',[])):errors.append(str(key)+' mismatched missing-data arrays')
        if r.get('time_window_start_day',0)>r.get('time_window_end_day',float('inf')):errors.append(str(key)+' reversed assessment window')
        if n=='acquisition':
            arrays=[r.get(k) for k in ['energy_window_names','energy_window_lower_kev','energy_window_upper_kev']]
            present=[a for a in arrays if a is not None]
            if present and (len(present)!=3 or len({len(a) for a in present})!=1 or r.get('number_of_energy_windows')!=len(present[0])):errors.append(str(key)+' inconsistent energy windows')
            if arrays[1] and arrays[2] and any(a>=b for a,b in zip(arrays[1],arrays[2])):errors.append(str(key)+' invalid energy bounds')
        if n=='time_activity_curve':
            times=r.get('time_hours',[]);acts=r.get('activity_mbq',[])
            if len(times)!=len(acts):errors.append(str(key)+' mismatched TAC arrays')
            if times!=sorted(times) or len(set(times))!=len(times):errors.append(str(key)+' TAC times must be strictly increasing')
        if n=='administration' and r.get('administration_purpose')=='therapy' and len(r.get('therapy_cycles',[]))!=1:errors.append(str(key)+' therapeutic administration requires exactly one cycle')
        if n=='survival_outcome':
            date_key='event_date' if r.get('event_observed') else 'censor_date'
            if not r.get(date_key) or not r.get('origin_date'):errors.append(str(key)+' incomplete endpoint event/censor dates')
            else:
                dur=(datetime.date.fromisoformat(r[date_key])-datetime.date.fromisoformat(r['origin_date'])).days
                if dur<0:errors.append(str(key)+' endpoint before origin')
                if 'duration_days' in r and not math.isclose(dur,r['duration_days'],abs_tol=0.0001):errors.append(str(key)+' duration inconsistent with dates')
    def resolve(n,ref):
        if 'submitter_id' in ref:return index.get((n,ref['submitter_id']))
        if 'id' in ref:return by_uuid.get((n,ref['id']))
        if 'code' in ref:return by_code.get((n,ref['code']))
    for r in records:
        for l,ref in refs(r,S[r['type']]):
            if not resolve(l['target_type'],ref):errors.append(str(record_key(r))+' dangling '+l['name']+' '+str(ref))
    # Compute inherited patient identity and reject evidence linked across patients.
    memo={}
    def cases(r,path=()):
        key=record_key(r)
        if key in memo:return memo[key]
        if key in path:errors.append('Record-level cycle '+str(key));return set()
        if r['type']=='case':return {key}
        found=set()
        for l,ref in refs(r,S[r['type']]):
            parent=resolve(l['target_type'],ref)
            if parent:found|=cases(parent,path+(key,))
        memo[key]=found;return found
    seen_cycle=set()
    for r in records:
        if len(cases(r))>1:errors.append(str(record_key(r))+' evidence crosses case identity')
        if r['type']=='therapy_cycle':
            k=(json.dumps(r['therapy_courses'],sort_keys=True),r['cycle_number'])
            if k in seen_cycle:errors.append('Duplicate course and cycle number')
            seen_cycle.add(k)
        if r['type']=='dose_summary':
            components=[resolve('absorbed_dose',f) for f in r['component_doses']]
            if any(x is None for x in components):continue
            if any(x['anatomic_targets']!=r['anatomic_targets'] for x in components):errors.append(str(record_key(r))+' cumulative dose includes different target')
            if len({x['statistic'] for x in components})>1:errors.append(str(record_key(r))+' cumulative dose mixes statistics')
            if r.get('aggregation_method','').lower().startswith('sum') and not math.isclose(sum(x['absorbed_dose_gy'] for x in components),r['cumulative_dose_gy'],rel_tol=1e-6):errors.append(str(record_key(r))+' cumulative dose sum mismatch')
        if r['type']=='timepoint' and 'hours_from_administration' in r and r.get('anchor_administrations') and r.get('assessment_datetime'):
            ar=resolve('administration',r['anchor_administrations'][0])
            if ar and ar.get('administration_datetime'):
                h=(datetime.datetime.fromisoformat(r['assessment_datetime'].replace('Z','+00:00'))-datetime.datetime.fromisoformat(ar['administration_datetime'].replace('Z','+00:00'))).total_seconds()/3600
                if not math.isclose(h,r['hours_from_administration'],abs_tol=1e-4):errors.append(str(record_key(r))+' elapsed time disagrees with anchor')
    return errors

def validate_midrc_profile(records):
    """Link-group/cardinality checks plus explicitly selected theranostics profiles.
    Original MIDRC dictionary remains permissive where it was permissive;
    additional evidence constraints belong to the declared collection profile.
    """
    errors=[]
    for r in records:
        s=S[r['type']];key=str(record_key(r))
        for l in flatlinks(s):
            count=len(ref_list(r.get(l['name'])))
            if l.get('required') and count==0:errors.append(key+' missing required link '+l['name'])
            if l['multiplicity'] in ['many_to_one','one_to_one'] and count>1:errors.append(key+' link cardinality '+l['name'])
        for g in s['links']:
            if 'subgroup' not in g:continue
            count=sum(bool(ref_list(r.get(l['name']))) for l in g['subgroup'])
            if g.get('required') and count==0:errors.append(key+' missing required link subgroup')
            if g.get('exclusive') and count>1:errors.append(key+' exclusive subgroup has multiple alternatives')
        n=r['type']
        if n in ['pt_series_file','nm_series_file','ct_series_file','mr_series_file']:
            expected={'pt_series_file':'PT','nm_series_file':'NM','ct_series_file':'CT','mr_series_file':'MR'}[n]
            if r.get('modality')!=expected:errors.append(key+' incorrect modality for file node')
            if not r.get('imaging_studies'):errors.append(key+' imaging study required by theranostics file profile')
            if n=='nm_series_file' and r.get('nm_acquisition_kind') not in ['SPECT','planar','other','unknown']:errors.append(key+' NM subtype required by theranostics profile')
            if (r.get('data_format'),r.get('data_type')) not in [('DCM','DICOM'),('nii.gz','NIfTI')]:errors.append(key+' inconsistent file format/data type')
        if n=='measurement' and r.get('measurement_profile') in ['laboratory','roi','anthropometric']:
            if not r.get('test_name_source_value') and not r.get('test_code') and not r.get('test_name'):errors.append(key+' measurement identity missing')
            if 'test_result_number' not in r:errors.append(key+' numeric profile missing result')
            if not r.get('unit'):errors.append(key+' quantitative result missing unit')
            if not r.get('cases'):errors.append(key+' patient link required by measurement profile')
            if r['measurement_profile']=='laboratory' and not r.get('laboratory_panels'):errors.append(key+' lab panel context missing')
            if r['measurement_profile']=='roi' and not r.get('annotations'):errors.append(key+' ROI contour evidence missing')
            if r.get('test_code')=='2857-1' and r.get('test_code_system')=='LOINC' and r.get('specimen_type') not in ['Serum','Plasma','Serum or Plasma']:errors.append(key+' PSA example code/specimen mismatch')
        if n=='annotation' and r.get('annotation_profile')=='segmentation':
            if not r.get('anatomic_targets') or not r.get('segmentation_method'):errors.append(key+' segmentation target/method missing')
            if not any(r.get(x+'_series_files') for x in ['pt','nm','ct','mr']):errors.append(key+' segmentation source image missing')
        if n=='dosimetry':
            if r.get('evidence_completeness')=='complete' and (not r.get('acquisitions') or not r.get('annotations')):errors.append(key+' dosimetry acquisition/contour provenance missing')
            if r.get('evidence_completeness') in ['partial','unavailable'] and not r.get('missing_evidence_reason'):errors.append(key+' incomplete dosimetry evidence needs a reason')
    return errors

def validate_revision_profile(records):
    """Selected structural/evidence consistency rules, not a complete clinical criteria engine."""
    errors=[];index={record_key(r):r for r in records}
    def parents(r,name,target):return [index[(target,x['submitter_id'])] for x in r.get(name,[]) if (target,x.get('submitter_id')) in index]
    for r in records:
        n=r['type'];key=record_key(r)[1]
        if n=='absorbed_dose':
            for s in parents(r,'annotations','annotation'):
                if s['anatomic_targets']!=r['anatomic_targets']:errors.append(key+' dose/segmentation target mismatch')
            if 'uncertainty_value' in r and not r.get('uncertainty_unit'):errors.append(key+' uncertainty unit missing')
        if n=='time_activity_curve':
            for q in parents(r,'roi_measurements','measurement'):
                for s in parents(q,'annotations','annotation'):
                    if s['anatomic_targets']!=r['anatomic_targets']:errors.append(key+' curve source belongs to different target')
        if n=='response_assessment':
            if 'recip' in str(r.get('psa_progression_criteria_used','')).lower():errors.append(key+' RECIP cannot be a PSA progression criterion')
            if r.get('criteria_name')=='RECIP' and r.get('criteria_version')=='1.0' and r.get('recip_category') not in [None,'NE','RECIP-CR']:
                b=parents(r,'baseline_burdens','disease_burden');f=parents(r,'followup_burdens','disease_burden')
                if len(b)!=1 or len(f)!=1:errors.append(key+' RECIP needs baseline and follow-up burden evidence');continue
                if any(x['scope']!='whole_body' for x in b+f):errors.append(key+' RECIP volume must be whole-body')
                bv=b[0]['total_psma_positive_tumor_volume_ml'];fv=f[0]['total_psma_positive_tumor_volume_ml']
                if bv<=0:errors.append(key+' quantitative percent change undefined at zero baseline');continue
                delta=100*(fv-bv)/bv;new=r.get('new_psma_avid_lesions_posttreatment')
                if new is None:errors.append(key+' new-lesion observation missing');continue
                expected='RECIP-PD' if delta>=20 and new>0 else 'RECIP-PR' if delta<=-30 and new==0 else 'RECIP-SD'
                if r['recip_category']!=expected:errors.append(key+' RECIP category inconsistent with volume AND new-lesion evidence')
                if 'ptlv_change_percent' in r and not math.isclose(delta,r['ptlv_change_percent'],abs_tol=.001):errors.append(key+' tumor-volume percent change mismatch')
            if r.get('psa_response_50_confirmed'):
                baseline=parents(r,'baseline_psa_results','measurement');confirmation=parents(r,'confirmatory_psa_results','measurement')
                if len(baseline)!=1 or len(confirmation)!=1 or not r.get('psa_response_50_date') or not r.get('confirmation_date'):errors.append(key+' confirmed PSA50 lacks dated baseline/confirmation evidence')
                elif baseline[0]['test_result_number']<=0 or confirmation[0]['test_result_number']>0.5*baseline[0]['test_result_number'] or (datetime.date.fromisoformat(r['confirmation_date'])-datetime.date.fromisoformat(r['psa_response_50_date'])).days<21:errors.append(key+' PSA50 confirmation inconsistent with recorded values or interval')
            if r.get('pain_response')=='yes':
                b=parents(r,'baseline_pros','patient_reported_outcome');f=parents(r,'followup_pros','patient_reported_outcome');c=parents(r,'confirmation_pros','patient_reported_outcome')
                if not b or not f or not c:errors.append(key+' pain response lacks baseline/follow-up/confirmation');continue
                allpro=b+f+c
                if any(x.get('instrument_name')!='NRS' or x.get('score_domain')!='pain' for x in allpro):errors.append(key+' pain response evidence uses incompatible instrument/domain')
                baseline=b[0].get('score',0)
                if baseline<4:errors.append(key+' pain palliation not evaluable at this baseline')
                for x in f+c:
                    improvement=baseline-x.get('score',baseline)
                    if not (improvement>=2 or (baseline>0 and improvement/baseline>=.3)):errors.append(key+' pain improvement insufficient for illustrative profile')
                    if 'opioid_daily_ome_mg' not in x or 'opioid_daily_ome_mg' not in b[0] or x.get('opioid_daily_ome_mg',0)>b[0].get('opioid_daily_ome_mg',0):errors.append(key+' opioid escalation/unknown dose prevents confirmed pain-response example')
                if (datetime.datetime.fromisoformat(c[0]['assessment_datetime'].replace('Z','+00:00'))-datetime.datetime.fromisoformat(f[0]['assessment_datetime'].replace('Z','+00:00'))).days<14:errors.append(key+' pain-response confirmation too early')
        if n=='treatment_decision':
            if r.get('decision_type')=='complete_planned_course' and ('nlcb_date' in r or 'nlcb_reason' in r):errors.append(key+' completion must not imply NLCB')
            if r.get('decision_type')=='nlcb' and (not r.get('nlcb_date') or not r.get('nlcb_reason')):errors.append(key+' NLCB requires explicit date and reason')
        if n=='treatment_transition':
            if set(x['submitter_id'] for x in r.get('prior_courses',[])) & set(x['submitter_id'] for x in r.get('subsequent_courses',[])):errors.append(key+' retreatment must be a different course')
            if r.get('transition_type')=='psma_rpt_retreatment' and r.get('transition_status')=='occurred' and not r.get('subsequent_courses'):errors.append(key+' actual retreatment requires subsequent course')
        if n=='patient_reported_outcome' and r.get('instrument_name')=='NRS' and 'score' in r and not 0<=r['score']<=10:errors.append(key+' NRS score outside range')
    return errors

def apply_patch(document,patch):
    result=copy.deepcopy(document)
    for op in patch:
        assert op['op']=='add'
        parts=op['path'].lstrip('/').split('/');parent=result
        for p in parts[:-1]:parent=parent[int(p)] if isinstance(parent,list) else parent[p]
        if isinstance(parent,list):parent.append(copy.deepcopy(op['value'])) if parts[-1]=='-' else parent.insert(int(parts[-1]),copy.deepcopy(op['value']))
        else:parent[parts[-1]]=copy.deepcopy(op['value'])
    return result

def clean_template(template):
    """Remove portal required-field markers and empty placeholders.
    This does not fill required values or make an incomplete record submittable.
    """
    def clean(x):
        if isinstance(x,dict):return {k.lstrip('*'):v for k,xv in x.items() if (v:=clean(xv)) is not None}
        if isinstance(x,list):return [v for xv in x if (v:=clean(xv)) is not None]
        return x
    result=clean(template)
    for k,v in list(result.items()):
        if v=={} or v==[]:result.pop(k)
    return result

def main():
    checks={};errors=[]
    B=json.loads((ROOT/'sources/midrc_dictionary_1.4.3-2-g7505333.json').read_text())
    baseline={n:s for n,s in B.items() if isinstance(s,dict) and 'links' in s and 'properties' in s}
    enum_changes=json.loads((ROOT/'integration/proposed_enum_additions.json').read_text())
    for n,b in baseline.items():
        for k,v in b.items():
            if k in ['properties','links']:continue
            if S[n].get(k)!=v:errors.append(n+' baseline node metadata changed: '+k)
        if S[n]['links'][:len(b['links'])]!=b['links']:errors.append(n+' baseline link groups changed')
        for k,p in b['properties'].items():
            expected=copy.deepcopy(p)
            for e in enum_changes:
                if (e['node'],e['property'])==(n,k):expected['enum'].append(e['added_value'])
            if S[n]['properties'].get(k)!=expected:errors.append(n+'.'+k+' baseline definition changed unexpectedly')
        if S[n]['required']!=b['required']:errors.append(n+' pre-existing data given new required fields')
    checks['midrc_nodes_preserved']=len(baseline)
    checks['baseline_properties_preserved_or_explicit_enum_append']=sum(len(s['properties']) for s in baseline.values())
    patch=json.loads((ROOT/'integration/midrc_additive_patch.json').read_text())
    if apply_patch(B,patch)!=json.loads((ROOT/'gen3_dictionary.json').read_text()):errors.append('Patch does not recreate merged dictionary')
    checks['additive_patch_round_trip']=True;checks['proposed_enum_additions']=len(enum_changes)
    for n,s in S.items():
        try:jsonschema.Draft4Validator.check_schema(s)
        except Exception as e:errors.append(n+' invalid JSON Schema '+str(e))
        for e in jsonschema.Draft4Validator(B['metaschema']).iter_errors(s):errors.append(n+' invalid Gen3 metaschema '+e.message)
        for l in flatlinks(s):
            if l['target_type'] not in S or l['name'] not in s['properties']:errors.append(n+' unresolved relationship '+str(l))
    checks['json_schemas_and_gen3_metaschema_checked']=len(S)
    backrefs=collections.Counter((l['target_type'],l['backref']) for s in S.values() for l in flatlinks(s))
    errors+=['Duplicate backref '+str(k) for k,v in backrefs.items() if v>1]
    order=json.loads((ROOT/'submission_order.json').read_text())['node_types']
    for n,s in S.items():
        for l in flatlinks(s):
            if order.index(l['target_type'])>=order.index(n):errors.append('Cyclic or incorrect submission order '+n+'.'+l['name'])
    checks['graph_acyclic_with_baseline_admin_roots_preserved']=True
    catalog=json.loads((ROOT/'source_field_catalog.json').read_text())
    for f in catalog:
        for d in f['destination_options']:
            if d['node'] not in S or d['property'] not in S[d['node']]['properties']:errors.append(f['source_element_id']+' unresolved destination')
        for k in f.get('fixed_values',{}):
            if k not in S[f['node']]['properties']:errors.append(f['source_element_id']+' unknown fixed-value property '+k)
    checks['source_occurrences_traced']=len(catalog);checks['revised_outcome_fields_traced']=sum(f['source_element_id'].startswith('outcome_revision:') for f in catalog)
    for p in (ROOT/'templates').glob('*.json'):
        t=json.loads(p.read_text());n=t.get('*type',t.get('type'))
        if n not in S:errors.append('Template unknown node '+str(p));continue
        if not {k.lstrip('*') for k in t}<=set(S[n]['properties']):errors.append('Unknown template property '+p.name)
        if {k[1:] for k in t if k.startswith('*')}!=set(S[n]['required']):errors.append('Required markers mismatch '+p.name)
        if any(k.startswith('*') for k in clean_template(t)):errors.append('Template marker cleanup failed')
    checks['portal_templates_checked']=len(S)
    records=json.loads((ROOT/'examples/full_patient_journey.json').read_text())
    def allchecks(rr):return validate_records(rr)+validate_midrc_profile(rr)+validate_revision_profile(rr)
    errors+=allchecks(records);checks['synthetic_records_checked']=len(records);checks['synthetic_node_types_covered']=len({r['type'] for r in records})
    # Existing MIDRC fixtures are derived from schema constraints and are not linked patient data.
    def sample(p):
        if 'enum' in p:return p['enum'][0]
        if 'anyOf' in p:return sample(p['anyOf'][-1])
        if p.get('type')=='object':return {k:sample(p.get('properties',{}).get(k,{'type':'string'})) for k in p.get('required',[])}
        if p.get('type')=='array':return [sample(p.get('items',{})) for _ in range(p.get('minItems',0))]
        if p.get('type') in ['number','integer']:return p.get('minimum',0)
        if p.get('type')=='boolean':return False
        if 'pattern' in p:return '0'*32 if '32' in p['pattern'] else '11111111-1111-4111-8111-111111111111'
        return 'SYNTHETIC'
    fixtures=[]
    for n,s in baseline.items():
        r={k:sample(s['properties'][k]) for k in s['required']};r['type']=n
        for l in flatlinks(s):
            if l['name'] in r:r[l['name']]={'code':'SYNTHETIC'} if l['target_type']=='project' else {'id':'11111111-1111-4111-8111-111111111111'} if l['target_type']=='program' else {'submitter_id':'SYNTHETIC'}
        for g in s['links']:
            if 'subgroup' in g and g.get('required'):
                l=g['subgroup'][0];r[l['name']]={'submitter_id':'SYNTHETIC'}
        baseerrs=list(jsonschema.Draft4Validator(s).iter_errors(r));newerrs=list(jsonschema.Draft4Validator(S[n]).iter_errors(r))
        if baseerrs or newerrs:errors.append('Baseline fixture validation '+n+': '+str([e.message for e in baseerrs+newerrs]))
        fixtures.append(r)
    (ROOT/'examples/midrc_baseline_regression_fixtures.json').write_text(json.dumps({'note':'Independent schema regression fixtures; not a connected submission bundle or real data.','records':fixtures},indent=2)+'\n')
    checks['baseline_regression_fixtures']=len(fixtures)
    negative={}
    def get(rr,n):return next(r for r in rr if r['type']==n)
    def mutant(name,change):
        rr=copy.deepcopy(records);change(rr)
        result=allchecks(rr);negative[name]=bool(result)
        if not result:errors.append('Negative test not rejected '+name)
    def specific(id,change):return lambda rr:change(next(r for r in rr if r.get('submitter_id')==id))
    mutant('unknown_property',lambda r:get(r,'case').update(unexpected_phi='example'))
    mutant('wrong_numeric_type',lambda r:get(r,'measurement').update(test_result_number='text'))
    mutant('urls_rejected_as_node_property',lambda r:get(r,'pt_series_file').update(urls=['https://example.invalid/file']))
    mutant('portal_asterisk_rejected_as_payload_key',lambda r:get(r,'pt_series_file').update({'*submitter_id':'wrong'}))
    mutant('nm_does_not_accept_pet_modality',lambda r:get(r,'nm_series_file').update(modality='PT'))
    mutant('slice_thickness_remains_array',lambda r:get(r,'pt_series_file').update(slice_thickness=4.0))
    mutant('legacy_midrc_enum_preserved',lambda r:get(r,'measurement').update(test_name='PSA'))
    mutant('file_group_requires_parent',lambda r:get(r,'pt_series_file').pop('imaging_studies'))
    mutant('dangling_measurement_panel',lambda r:next(x for x in r if x.get('measurement_profile')=='laboratory').update(laboratory_panels=[{'submitter_id':'MISSING'}]))
    mutant('annotation_source_many_to_one_preserved',lambda r:get(r,'annotation').update(nm_series_files=[{'submitter_id':'SYN-IMAGE_FILE'},{'submitter_id':'JOURNEY-C1-IMAGE-48H'}]))
    mutant('missing_measurement_unit',lambda r:get(r,'measurement').pop('unit'))
    mutant('energy_window_array_mismatch',lambda r:get(r,'acquisition').update(energy_window_upper_kev=[220,250]))
    mutant('negative_activity',lambda r:get(r,'administration').update(administered_activity_mbq=-1))
    mutant('invalid_ctcae_grade',lambda r:get(r,'toxicity_event').update(grade=6))
    mutant('cumulative_dose_mismatch',lambda r:get(r,'dose_summary').update(cumulative_dose_gy=999))
    mutant('time_anchor_mismatch',lambda r:get(r,'timepoint').update(hours_from_administration=999))
    def cross_case(rr):
        other=copy.deepcopy(get(rr,'case'));other['submitter_id']='SYN-OTHER-CASE';rr.append(other);get(rr,'anatomic_target')['cases']=[{'submitter_id':'SYN-OTHER-CASE'}]
    mutant('cross_patient_evidence',cross_case)
    mutant('dose_contour_wrong_target',specific('SYN-DOSE-LESION-C1',lambda r:r.update(annotations=[{'submitter_id':'SYN-SEGMENTATION'}])))
    mutant('uncertainty_unit_missing',specific('SYN-DOSE-LESION-C1',lambda r:r.pop('uncertainty_unit')))
    mutant('missing_dosimetry_not_complete',specific('SYN-DOSIMETRY-2',lambda r:r.update(evidence_completeness='complete')))
    mutant('recip_or_rule_rejected',specific('JOURNEY-RECIP',lambda r:r.update(recip_category='RECIP-PD',new_psma_avid_lesions_posttreatment=1)))
    mutant('recip_wrong_volume_scope',specific('JOURNEY-BURDEN-FU',lambda r:r.update(scope='selected_lesions')))
    mutant('recip_used_for_psa',specific('JOURNEY-EARLY-PSA-ASSESSMENT',lambda r:r.update(psa_progression_criteria_used='RECIP 1.0')))
    mutant('psa_confirmation_too_early',specific('SYN-RESPONSE_ASSESSMENT',lambda r:r.update(confirmation_date='2026-04-02')))
    mutant('pain_opioid_escalation',specific('JOURNEY-PAIN-FU',lambda r:r.update(opioid_daily_ome_mg=20)))
    mutant('completion_not_nlcb',specific('JOURNEY-COMPLETION',lambda r:r.update(nlcb_date='2026-02-01')))
    mutant('retreatment_distinct_course',specific('JOURNEY-TRANSITION-RETREATMENT',lambda r:r.update(subsequent_courses=r['prior_courses'])))
    checks['negative_tests']=negative
    guide=json.loads((ROOT/'examples/patient_journey_guide.json').read_text());ids={r.get('submitter_id') for r in records}
    for item in guide['steps']+guide['use_cases']:
        if any(i not in ids for i in item['record_ids']):errors.append('Unresolved journey record reference')
    checks['journey_stages']=len(guide['steps']);checks['use_cases']=len(guide['use_cases'])
    report={'status':'PASS' if not errors else 'FAIL','checks':checks,'errors':errors,'not_validated':['Live Gen3 dictionaryutils/data-model build, migration, submission API ingestion, authorization and portal rendering','Clinical completeness and treatment-decision safety; local profile checks are not a clinical criteria engine','NucLex/RadLex binding approval, full LOINC assay mapping, term-specific CTCAE grades, PCWG release-specific algorithms','SOP-class-specific DICOM extraction, actual file bytes/checksums, Indexd registration, object-store access','Real patient data or extraction interfaces']}
    (ROOT/'validation/validation_report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())

