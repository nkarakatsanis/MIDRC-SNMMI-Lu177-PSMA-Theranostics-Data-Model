"""Version 0.4.0 context and lineage checks; not a clinical or batch-release engine."""
import datetime as dt, math

def validate_radiopharmaceutical_profile(records):
    errors=[];ix={(r['type'],r.get('submitter_id')):r for r in records}
    def linked(r,k,t):return [ix[(t,v['submitter_id'])] for v in r.get(k,[]) if (t,v.get('submitter_id')) in ix]
    def time(v):
        try:return dt.datetime.fromisoformat(v.replace('Z','+00:00'))
        except (ValueError,TypeError,AttributeError):return None
    def require(r,*props):
        for p in props:
            if p not in r or r[p] in [None,'',[]]:errors.append(r.get('submitter_id','')+' requires '+p)
    def earlier(r,a,b):
        x,y=time(r.get(a)),time(r.get(b))
        if x and y and x>y:errors.append(r['submitter_id']+' reversed '+a+'/'+b)
    containment={}
    for r in records:
        n=r['type'];key=r.get('submitter_id',n)
        if n=='radionuclide':
            if r['mass_number']<r['atomic_number'] or r['atomic_number']<1:errors.append(key+' invalid nuclear integers')
            if not r['is_stable'] and r.get('physical_half_life_seconds',0)<=0:errors.append(key+' radioactive nuclide requires positive half-life')
            if r['is_stable'] and ('physical_half_life_seconds' in r or 'decay_constant_per_second' in r):errors.append(key+' stable nuclide cannot have finite decay parameters')
            if r.get('decay_constant_per_second') is not None and r.get('physical_half_life_seconds',0)>0 and not math.isclose(r['decay_constant_per_second'],math.log(2)/r['physical_half_life_seconds'],rel_tol=.01):errors.append(key+' half-life/decay-constant mismatch')
        if n=='decay_emission':
            if r['record_kind']=='decay_branch':
                require(r,'decay_mode','branch_fraction')
                if 'yield_per_decay' in r:errors.append(key+' branch and emission yield must be distinct records')
            else:
                require(r,'radiation_type','yield_per_decay')
                if r['record_kind']=='emission_line':require(r,'energy_kev','energy_kind')
                if 'branch_fraction' in r:errors.append(key+' emission record cannot substitute a branch probability')
        if n=='molecular_entity' and 'formal_charge' in r and r['formal_charge']!=int(r['formal_charge']):errors.append(key+' formal charge must be integer-valued')
        if n=='product_ingredient' and 'quantity_value' in r:require(r,'quantity_unit','quantity_basis')
        if n=='product_package' and r.get('storage_temperature_min_c',-math.inf)>r.get('storage_temperature_max_c',math.inf):errors.append(key+' reversed storage temperature interval')
        if n=='package_component':
            if r.get('component_count',0)<=0:errors.append(key+' nonpositive package count')
            for a in r.get('outer_packages',[]):
                for b in r.get('inner_packages',[]):
                    containment.setdefault(a.get('submitter_id'),set()).add(b.get('submitter_id'))
        if n=='supply_offer' and 'price_amount' in r:require(r,'price_currency','price_basis')
        if n=='material_lot':
            if r['material_kind']=='radionuclide_stock':require(r,'radionuclides')
            elif r['material_kind'] in ['precursor','excipient']:require(r,'molecular_entities')
        if n=='preparation_event':
            earlier(r,'started_datetime','completed_datetime')
            if not r.get('input_material_lots') and not r.get('input_batches'):errors.append(key+' preparation requires inputs')
            if {v.get('submitter_id') for v in r.get('input_batches',[])} & {v.get('submitter_id') for v in r.get('output_batches',[])}:errors.append(key+' preparation output cannot be its own input')
        if n=='radiopharmaceutical_batch' and r.get('release_status') in ['released','rejected']:
            require(r,'release_datetime','release_specification_version','release_authority_reference')
        if n=='radiopharmaceutical_unit':
            earlier(r,'activity_reference_datetime','expiry_datetime')
            for prep in linked(r,'preparation_events','preparation_event'):
                if prep.get('output_batches')!=r.get('radiopharmaceutical_batches'):errors.append(key+' unit batch differs from preparation output')
        if n=='radiopharmaceutical_order':
            if r['order_kind']=='patient_prescription':require(r,'cases')
            elif r.get('cases') or r.get('therapy_cycles'):errors.append(key+' procurement must not be a patient-specific prescription')
            if 'requested_activity_mbq' in r:require(r,'requested_reference_datetime')
            if 'requested_quantity' in r:require(r,'requested_quantity_unit')
        if n=='dispense_event':
            for order in linked(r,'radiopharmaceutical_orders','radiopharmaceutical_order'):
                if order['order_kind']!='patient_prescription':errors.append(key+' dispensing must fulfill a patient prescription')
                for unit in linked(r,'radiopharmaceutical_units','radiopharmaceutical_unit'):
                    for batch in linked(unit,'radiopharmaceutical_batches','radiopharmaceutical_batch'):
                        if batch.get('medicinal_products') and batch['medicinal_products']!=order['medicinal_products']:errors.append(key+' dispensed product differs from prescribed product')
        if n=='administration' and r.get('radiopharmaceutical_units'):
            for unit in linked(r,'radiopharmaceutical_units','radiopharmaceutical_unit'):
                if r.get('radiopharmaceutical_batches') and unit['radiopharmaceutical_batches']!=r['radiopharmaceutical_batches']:errors.append(key+' administered unit batch mismatch')
                for batch in linked(unit,'radiopharmaceutical_batches','radiopharmaceutical_batch'):
                    if batch['radiopharmaceuticals']!=r['radiopharmaceuticals']:errors.append(key+' administered agent differs from unit batch agent')
                a,b=time(r.get('administration_datetime')),time(unit.get('expiry_datetime'))
                if a and b and a>b:errors.append(key+' administration after recorded unit expiry')
            for disp in linked(r,'dispense_events','dispense_event'):
                if disp['radiopharmaceutical_units']!=r['radiopharmaceutical_units']:errors.append(key+' administration and dispensing units differ')
                for order in linked(disp,'radiopharmaceutical_orders','radiopharmaceutical_order'):
                    if order.get('therapy_cycles') and order['therapy_cycles']!=r.get('therapy_cycles'):errors.append(key+' prescription and administration cycle mismatch')
        if n=='radiopharmaceutical_test':
            context=r['test_context'];subject={'batch_qc':'radiopharmaceutical_batches','material_qc':'material_lots','unit_qc':'radiopharmaceutical_units','reference_result':'reference_evidence','model_evaluation':'computational_models'}[context]
            require(r,subject)
            subject_names=['radiopharmaceutical_batches','material_lots','radiopharmaceutical_units','reference_evidence','computational_models']
            if sum(bool(r.get(k)) for k in subject_names)!=1:errors.append(key+' test must have exactly one context-appropriate subject')
            numeric=[k for k in ['test_result_number','test_result_percent','test_result_ratio'] if k in r]
            if len(numeric)>1:errors.append(key+' test has conflicting numerical result representations')
            if numeric:require(r,'unit')
            if r['result_status'] in ['pending','not_performed'] and (numeric or 'result_text' in r):errors.append(key+' pending/not-performed test cannot carry a result')
            if r['result_status']=='final' and not numeric and not r.get('result_text'):errors.append(key+' final test needs a result')
            if 'test_result_percent' in r and (r.get('unit')!='%' or not 0<=r['test_result_percent']<=100):errors.append(key+' percent result/unit inconsistent')
            if 'test_result_ratio' in r and r.get('unit')!='1':errors.append(key+' ratio requires dimensionless unit 1')
            q=r['quantity_name'].lower()
            if 'purity' in q and numeric and r.get('unit')=='1' and not 0<=r[numeric[0]]<=1:errors.append(key+' purity fraction outside 0..1')
            if context.endswith('_qc'):require(r,'assay_datetime')
            if q in ['molar activity','specific activity']:
                require(r,'analyte_basis','activity_reference_datetime')
                allowed=['GBq/umol','MBq/nmol','Bq/mol'] if q=='molar activity' else ['MBq/mg','GBq/g','Bq/g']
                if r.get('unit') not in allowed:errors.append(key+' unsupported activity-denominator unit for '+q)
            if r.get('acceptance_decision') in ['pass','fail']:
                require(r,'specification_version')
                if r['result_status']!='final':errors.append(key+' QC judgment requires final result')
            if 'uncertainty_value' in r:require(r,'uncertainty_unit','uncertainty_kind')
            if any(w in q for w in ['readiness','sufficiency score','completeness score']):require(r,'rubric_name','rubric_version')
            if q in ['rbe','rbe descriptor','relative biological effectiveness']:require(r,'reference_radiation')
        if n=='reference_evidence' and r['setting'] in ['human_clinical','preclinical','in_vitro']:require(r,'species','population_description')
        if n=='model_run':
            earlier(r,'information_cutoff_datetime','run_datetime');cut=time(r.get('information_cutoff_datetime'))
            for k,t in [('input_administrations','administration'),('input_measurements','measurement'),('input_acquisitions','acquisition')]:
                for v in linked(r,k,t):
                    ts=time(v.get('administration_datetime') or v.get('measurement_datetime') or v.get('acquisition_datetime'))
                    if cut and ts and ts>cut:errors.append(key+' input recorded after information cutoff')
        if n=='model_parameter':
            if 'value' not in r and not r.get('distribution_description'):errors.append(key+' parameter needs value or distribution')
            if 'uncertainty_value' in r:require(r,'uncertainty_unit','uncertainty_kind')
            for run in linked(r,'model_runs','model_run'):
                if run['computational_models']!=r['computational_models']:errors.append(key+' parameter/run model mismatch')
        if n=='model_prediction':
            if ('uncertainty_lower' in r)!=('uncertainty_upper' in r):errors.append(key+' incomplete prediction interval')
            if 'uncertainty_lower' in r:
                require(r,'uncertainty_definition')
                if not r['uncertainty_lower']<=r['predicted_value']<=r.get('uncertainty_upper',-math.inf):errors.append(key+' prediction outside interval')
        if n=='external_identifier' and r['identifier_system']=='NDC':
            level=r['identifier_level'].lower()
            if 'package' in level and not r.get('product_packages'):errors.append(key+' package NDC requires package identity')
            if 'product' in level and not r.get('medicinal_products'):errors.append(key+' product NDC requires product identity')
        if n=='toxicity_event' and r.get('dose_limiting_toxicity'):require(r,'dlt_definition_reference')
        if n=='provenance' and 'confidence_value' in r:require(r,'confidence_rubric')
    def walk(n,path):
        if n in path:return True
        return any(walk(c,path|{n}) for c in containment.get(n,set()))
    if any(walk(n,set()) for n in containment):errors.append('Package containment cycle')
    return errors
