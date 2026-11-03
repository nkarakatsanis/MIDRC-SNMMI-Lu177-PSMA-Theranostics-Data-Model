"""Generate tables, inventory, graph sources and workbook content from schemas."""
from build_module import OUT,OLD,ROOT,read,write,flat
import json,csv,collections,re,html
S={p.stem:read(p) for p in (OUT/'schemas').glob('*.json')}
fields=read(OUT/'source_field_catalog.json');meta={x['id']:x for x in read(OUT/'node_catalog.json')}
graph=read(OUT/'graph/model_graph.json');edges=graph['edges'];module=read(OUT/'integration/radiopharmaceutical_module.json')
authors=read(OUT/'AUTHORS.json');stats=read(OLD/'inventory_summary.json');records=read(OUT/'examples/full_patient_journey.json')
stats.update(version='0.4.0-proposal',as_of='2026-11-02',source_field_rows=len(fields),node_count=len(S),edge_count=len(edges),domain_count=len(read(OUT/'domain_catalog.json')),unique_node_properties=sum(len(s['properties']) for s in S.values()),new_extension_nodes=len(S)-29,synthetic_record_count=len(records),synthetic_node_types=len({r['type'] for r in records}),use_cases=8,radiopharmaceutical_new_nodes=23,radiopharmaceutical_source_occurrences=450,radiopharmaceutical_revision_themes=18)
stats['source_fields_by_sheet']=dict(collections.Counter(f['source_sheet'] for f in fields));write(OUT/'inventory_summary.json',stats)
propertyrows=[]
for n,s in sorted(S.items()):
    for p,definition in s['properties'].items():
        origin='MIDRC unchanged' if n in read(OLD/'sources/midrc_dictionary_1.4.3-2-g7505333.json') and p in read(OLD/'sources/midrc_dictionary_1.4.3-2-g7505333.json')[n].get('properties',{}) else 'Theranostics extension'
        if n=='radiopharmaceutical_test' and p in ['test_result_number','test_result_percent','test_result_ratio']:origin='Exact MIDRC measurement property definition reused for nonpatient context'
        row=dict(node=n,property=p,required=p in s['required'],system=p in s.get('systemProperties',[]),origin=origin,type=definition.get('type','enum' if 'enum' in definition else 'compound'),definition=definition.get('description',definition.get('term',{}).get('description','')),schema=definition,source_occurrence_ids=[f['source_element_id'] for f in fields if {'node':n,'property':p} in f['destination_options']])
        propertyrows.append(row)
    with (OUT/'tables'/f'{n}.csv').open('w',newline='') as f:
        keys=['node','property','required','system','origin','type','definition','source_occurrence_ids'];w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:('; '.join(r[k]) if isinstance(r[k],list) else r[k]) for k in keys} for r in propertyrows if r['node']==n)
write(OUT/'tables/node_property_catalog.json',propertyrows)
write(OUT/'tables/all_node_properties.json',propertyrows)
def aggregate_csv(path,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        writer.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()} for row in rows)
aggregate_csv(OUT/'tables/all_node_properties.csv',propertyrows)
aggregate_csv(OUT/'tables/node_catalog.csv',list(meta.values()))

profile={
 'version':'0.4.0','status':'Proposed collection profiles; working-group and Gen3 deployment review required',
 'profiles':[
  {'name':'human_clinical','scope':'Human diagnosis, treatment and follow-up with optional product-to-administration traceability.','requirements':'Keep existing MIDRC case and typed imaging parents; prescriptions and dispensing identify the same case and cycle; units identify their batch and expiry.','not_required':'No preclinical or digital-twin record is mandatory for a clinical patient.'},
  {'name':'radiopharmacy','scope':'Manufacturing, package specifications, material lots, preparation, unit inventory and timed QC.','requirements':'Use nonpatient radiopharmaceutical_test subjects; retain method, units, result status, specification and reference times. Authorized batch disposition is separate.','not_required':'No fabricated patient is created for batch QC; passing a test is not an automated release decision.'},
  {'name':'reference_research','scope':'Published, preclinical, in-vitro and cohort evidence.','requirements':'Identify setting, species/population, statistic, method, matrix/anatomy, time and source. Separate one result per quantity.','not_required':'No automatic transfer of a cohort result to an individual human record.'},
  {'name':'digital_twin_research','scope':'Versioned model specifications, runs, parameters and predictions.','requirements':'Identify exact model release, input provenance, information cutoff, parameter units and scenario. Predictions remain separate from measured dose/outcomes.','not_required':'No model execution, readiness score, clinical decision policy or safety approval is supplied.'}],
 'validation_module':'scripts/radiopharmaceutical_profile.py','unit_policy':'Numeric results carry units. Fractions use 1, percentages use %, mass and molar activity use distinct denominator units. Other units require reviewed conversion; missing values are not zeros.',
 'legacy_policy':'Read legacy product-like radiopharmaceutical records and ambiguous batch activity fields unchanged. Curate an explicit agent/product split and timed QC result before using the new normalized profile; never infer a molar/mass denominator.'}
write(OUT/'profiles/radiopharmaceutical_v040.json',profile)

# Recompute every old scoped view from the same edge source; add focused radiopharmaceutical views.
views={}
for v in read(OLD/'graph/view_manifest.json'):
    dot=(OLD/'graph'/(v['view']+'.dot')).read_text()
    nodes=re.findall(r'^([a-z_0-9]+) \[label=',dot,re.M)
    views[v['view']]=(v['title'],list(S) if v['view']=='complete' else nodes)
views.update({
 'radiopharmaceutical_identity':('Agent, product, ingredients and identifiers',['radiopharmaceutical','radionuclide','decay_emission','molecular_entity','biological_target','medicinal_product','product_ingredient','product_package','external_identifier','regulatory_authorization','theranostic_pair']),
 'radiopharmaceutical_trace':('Preparation, quality and the actual administration',['medicinal_product','product_package','material_lot','radiopharmaceutical_batch','preparation_event','radiopharmaceutical_unit','radiopharmaceutical_test','radiopharmaceutical_order','dispense_event','administration','therapy_cycle','case']),
 'radiopharmaceutical_research':('Reference evidence and computational predictions',['radiopharmaceutical','reference_evidence','radiopharmaceutical_test','computational_model','model_run','model_parameter','model_prediction','administration','anatomic_target','absorbed_dose','treatment_plan','case'])})
manifest=[]
for key,(title,nodes) in views.items():
    es=[e for e in edges if e['source'] in nodes and e['target'] in nodes]
    lines=['digraph model {','graph [rankdir=BT,bgcolor="white",pad=0.3,nodesep=0.4,ranksep=0.7,splines=polyline,fontname="Arial",fontsize=16,label='+json.dumps(title+'\nLu177-PSMA | v0.4.0 proposal')+',labelloc=t];','node [shape=box,style="rounded,filled",fontname="Arial",fontsize=11,margin="0.14,0.09",penwidth=1.5];','edge [fontname="Arial",fontsize=9,arrowsize=0.65];']
    for n in nodes:
        base=n in read(OLD/'sources/midrc_dictionary_1.4.3-2-g7505333.json')
        lines.append(f'{n} [label={json.dumps(n.replace("_"," "))},fillcolor="'+('#e5eff7' if base else '#f5ead8')+'",color="'+('#265b85' if base else '#a66723')+'",tooltip='+json.dumps(meta[n]['record_grain'])+',URL="#node='+n+'"];')
    for e in es:
        req=e.get('required',False);group=e.get('group_required',False);tip=f"{e['source']}.{e['name']} → {e['target']} | {e['multiplicity']} | "+('required' if req else 'alternative group' if group else 'optional')
        lines.append(f"{e['source']} -> {e['target']} [tooltip={json.dumps(tip)},style=\""+('solid' if req else 'dashed')+'\",color=\"'+('#345674' if req else '#a66e29' if group else '#a0aeb8')+'\"];')
    lines.append('}');(OUT/'graph'/(key+'.dot')).write_text('\n'.join(lines)+'\n')
    manifest.append(dict(view=key,title=title,nodes=len(nodes),edges=len(es),direction='child to referenced parent/evidence',warnings=[]))
write(OUT/'graph/view_manifest.json',manifest)

# Workbook matrices are consumed only by the supported artifact-tool authoring API.
def tab(name,headers,rows,widths):return dict(name=name,headers=headers,rows=rows,widths=widths)
new=set(module['new_nodes']);rp=new|{'radiopharmaceutical','radiopharmaceutical_batch','administration','provenance','toxicity_event','treatment_plan'}
common={'type','submitter_id','id','project_id','state','created_datetime','updated_datetime','projects','provenance_records','model_version','record_status','source_record_id','source_system','missing_properties','missing_reasons'}
er=[]
for r in propertyrows:
    n,p=r['node'],r['property'];s=S[n]
    if n not in rp or p in common or p in {l['name'] for l in flat(s)}:continue
    if n not in new|{'radiopharmaceutical','radiopharmaceutical_batch'} and p in read(OLD/'schemas'/f'{n}.json')['properties']:continue
    d=r['schema'];constraint=json.dumps({k:v for k,v in d.items() if k not in ['description','term']},ensure_ascii=False)
    status='New node property' if n in new else 'Optional extension' if p not in read(OLD/'schemas'/f'{n}.json')['properties'] else 'Retained legacy field'
    note=''
    if n=='radiopharmaceutical_batch' and p in ['specific_activity','specific_activity_unit','radiochemical_purity_percent','assay_datetime']:note='Legacy compatibility only. Prefer separate timed QC tests with explicit quantity, units and chemical denominator; no automatic conversion.'
    if n=='radiopharmaceutical' and p in ['product_code','code_system','non_active_ingredients','physical_half_life_seconds','radionuclide','molecular_target','production_type']:note='Legacy field retained. Prefer typed identity, product/ingredient, radionuclide or manufacturing records; reconcile rather than duplicate assertions.'
    er.append([n,p,r['type'],'Required' if r['required'] else 'Optional',r['definition'],constraint,status,'; '.join(r['source_occurrence_ids']),note])
linkrows=[]
for n in sorted(rp):
 for l in flat(S[n]):
    if n not in new|{'radiopharmaceutical','radiopharmaceutical_batch','administration'} and l['name'] in {x['name'] for x in flat(read(OLD/'schemas'/f'{n}.json'))}:continue
    group=next((g for g in S[n]['links'] if 'subgroup' in g and l in g['subgroup']),{})
    linkrows.append([n,l['name'],l['target_type'],l['multiplicity'],'Required' if l['required'] else 'One required alternative' if group.get('required') else 'Optional',l['label'],l['backref']])
overview=[['Release','0.4.0 development proposal; 2 November 2026'],['Purpose','Revised radiopharmaceutical model integrating the Nouran Zaid draft, Nicolas Karakatsanis blueprint and the supplied IDRP document.'],['How to read','Nodes defines record identity; Elements defines node properties; Links defines relationships; Profiles defines conditional context; Common metadata applies to all new nodes.'],['Scope','23 new nodes and optional additions to six existing nodes; all 29 MIDRC baseline nodes remain. The complete model has '+str(len(S))+' nodes.'],['Baseline','MIDRC 1.4.3-2-g7505333; commit 7505333d56c87a289463a814131e38d0f2be6674; retrieved 16 October 2026.'],['Definitions','Proposed operational definitions. LOINC/RadLex/NucLex and regulatory mappings require separate release-specific review.'],['Units','See each quantity definition and profile. Identifiers are strings. Missing values are not zero. No source example is a clinical default.'],['Review companion','Radiopharmaceutical_Revisions_and_Rationale_v0.4.0.xlsx maps each source entry and explains the change.'],['tentative authors list',', '.join(authors['authors'])],['Status','No institutional adoption, live Gen3 deployment or clinical validation is claimed. All patient examples are invented.']]
book1=[tab('Read me',['Item','Description'],overview,[28,120]),tab('Nodes',['Node','Group','One record represents','Origin'],[[n,meta[n]['group'],meta[n]['record_grain'],'New v0.4 node' if n in new else 'Existing node extended'] for n in sorted(rp)],[32,32,110,25]),tab('Elements',['Node','Property','Type','Requiredness','Definition and units','Exact constraints','Change status','Source occurrences','Migration note'],er,[30,36,16,18,100,65,26,42,85]),tab('Links',['Child node','Link property','Referenced node','Multiplicity','Requiredness','Relationship','Reverse name'],linkrows,[30,34,30,24,28,26,48]),tab('Profiles',['Profile','Scope','Requirements','Boundary'],[[p['name'],p['scope'],p['requirements'],p['not_required']] for p in profile['profiles']],[28,75,110,100]),tab('Common metadata',['Property','Type','Requiredness','Definition'],[[r['property'],r['type'],'Required' if r['required'] else 'System' if r['system'] else 'Optional',r['definition']] for r in propertyrows if r['node']=='medicinal_product' and r['property'] in common],[35,18,20,115])]
write(OUT/'documentation/radiopharmaceutical_workbook_content.json',book1)
rpfields=read(OUT/'mappings/radiopharmaceutical_source_crosswalk.json');revs=read(OUT/'mappings/radiopharmaceutical_revision_log.json');decisions=read(OUT/'mappings/radiopharmaceutical_review_decisions.json')
def cross(source):
 return [[f['source_element_id'],f['source_name'],f['source_definition'] or 'Not defined in source',f['source_data_type'],'; '.join(d['node']+'.'+d['property'] for d in f['destination_options']),f['revision_id'],f['transformation'],json.dumps(f['fixed_values'],ensure_ascii=False),f['mapping_status']] for f in rpfields if f['source_element_id'].startswith(source+':')]
headers=['Source location','Source element','Original definition','Source type','Proposed destination','Revision','Rationale and transformation','Qualifier assignments','Review status']
book2=[tab('Read me',['Item','Description'],overview[:2]+[['Coverage','102 Nouran source entries, 325 blueprint fields and 23 IDRP conceptual passages are accounted for. Source occurrence counts include duplicate relations, one placeholder and an empty pharmacodynamics section.'],['Review method','Every proposed destination is checked against the actual v0.4 dictionary. R01–R18 summarize reasons. No source code or dosage example is accepted as validated.']]+overview[8:],[28,120]),tab('Revision themes',['ID','Revision','Source issue','Proposed revision','Rationale','Status'],[[r[k] for k in ['revision_id','title','source_issue','proposed_revision','rationale','status']] for r in revs],[12,42,85,95,100,36]),tab('Nouran row review',headers,cross('nz_model'),[26,64,90,24,75,16,115,65,25]),tab('Blueprint crosswalk',headers,cross('nk_blueprint'),[26,56,90,24,75,16,115,65,25]),tab('IDRP passages',headers,cross('idrp_ontology'),[26,55,90,24,75,16,115,65,25]),tab('Open decisions',['Item','Status','Review question'],[[x['item'],x['status'],x['question']] for x in decisions],[40,40,120]),tab('Sources',['Source','SHA256 or URL','Use'],[[v['filename'],v['sha256'],'Supplied draft; source coordinates preserved in crosswalk.'] for v in read(OUT/'sources/radiopharmaceutical_inputs/source_manifest.json')]+[['FDA NDC directory','https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory','Identifier listing does not establish approval.'],['FDA IDMP','https://www.fda.gov/industry/fda-data-standards-advisory-board/identification-medicinal-products-idmp','Product/substance/package identification levels and PhPID expansion.'],['EANM molar and specific activity','https://pmc.ncbi.nlm.nih.gov/articles/PMC8502193/','Distinct activity denominators and measurement context.'],['Gen3 dictionary guide','https://gen3.org/resources/user/dictionary/','Nodes, links, property definitions and parallel graph/table views.']],[65,110,90])]
write(OUT/'documentation/radiopharmaceutical_revision_workbook_content.json',book2)
print(json.dumps({'properties':len(propertyrows),'edges':len(edges),'workbook_elements':len(er),'links':len(linkrows),'views':len(views)}))
