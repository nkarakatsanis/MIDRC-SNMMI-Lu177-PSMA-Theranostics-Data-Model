"""Reproduce the additive v0.4.0 radiopharmaceutical dictionary from v0.3.0.

No patient data, external terminology release, or clinical default is embedded.
"""
from pathlib import Path
import copy, json, collections, csv, hashlib, subprocess, re
import yaml

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT/'extensions/lu177_psma/v0.3.0'
OUT = ROOT/'extensions/lu177_psma/v0.4.0'
VERSION = '0.4.0'
def read(p): return json.loads(p.read_text())
def write(p,d): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
S = {p.stem:read(p) for p in (OLD/'schemas').glob('*.json')}
PRIOR = copy.deepcopy(S)
SPEC = {}
def fields(text):
    result={}
    for line in text.strip().splitlines():
        if not line.strip():continue
        name,kind,desc=line.strip().split('|',2)
        required=name.endswith('!');name=name.rstrip('!')
        p={'description':desc}
        if kind.startswith('enum:'):p['enum']=kind[5:].split(',')
        elif kind=='strings':p.update(type='array',items={'type':'string'},uniqueItems=True)
        else:
            types={'str':'string','num':'number','pos':'number','int':'integer','sint':'integer','bool':'boolean','date':'string','time':'string','fraction':'number'}
            p['type']=types[kind]
            if kind in ['str','date','time']:p['minLength']=1
            if kind in ['pos','int','fraction']:p['minimum']=0
            if kind=='fraction':p['maximum']=1
            if kind in ['date','time']:p['format']='date' if kind=='date' else 'date-time'
        result[name]=(p,required)
    return result

def node(name,grain,text,group='Radiopharmaceutical reference'):
    base=copy.deepcopy(PRIOR['radiopharmaceutical'])
    common=['type','submitter_id',*base['systemProperties'],'model_version','record_status','source_record_id','source_system','missing_properties','missing_reasons']
    base.update(id=name,title=name.replace('_',' ').title(),description=grain,links=[],required=['type','submitter_id'],properties={k:v for k,v in base['properties'].items() if k in common})
    base['properties']['type']={'enum':[name]}
    base['category']='administrative' if name in ['external_identifier','reference_evidence','computational_model','model_run','model_parameter','model_prediction'] else 'clinical'
    S[name]=base;SPEC[name]={'group':group,'record_grain':grain,'new':True}
    addfields(name,text);link(name,'projects','project',True,False,'member_of');link(name,'provenance_records','provenance',False,True,'documented_by')

def addfields(name,text):
    for k,(p,req) in fields(text).items():
        assert k not in S[name]['properties'],(name,k)
        S[name]['properties'][k]=p
        if req:S[name]['required'].append(k)

def link(n,name,target,required=False,many=True,label='related_to'):
    assert name not in S[n]['properties'],(n,name)
    p=copy.deepcopy(PRIOR['radiopharmaceutical']['properties']['projects' if target=='project' else 'provenance_records'])
    p['description']=f'Link to {target} records by '+('code' if target=='project' else 'submitter_id')+' or UUID.'
    p.pop('minItems',None);p.pop('maxItems',None)
    if required:p['minItems']=1
    if not many:p['maxItems']=1
    S[n]['properties'][name]=p
    S[n]['links'].append(dict(name=name,backref=f'nmmi_{n}_{name}',label=label,target_type=target,multiplicity='many_to_many' if many else 'many_to_one',required=required))
    if required:S[n]['required'].append(name)

node('radionuclide','One nuclide identity and versioned physical reference description, including stable daughters.', '''
name!|str|Nuclide name, with element, mass number and nuclear state resolved.
atomic_symbol!|str|Chemical element symbol.
atomic_number!|int|Integer proton number Z; not an identifier code.
mass_number!|int|Integer nucleon number A.
nuclear_state!|str|Ground or specified metastable nuclear state.
is_stable!|bool|Whether the referenced nuclide is stable; a stable daughter has no finite physical half-life.
physical_half_life_seconds|pos|Physical decay half-life in seconds, excluding biological elimination; positive for a radioactive nuclide.
half_life_uncertainty_seconds|pos|Standard uncertainty of the physical half-life in seconds, if reported.
decay_constant_per_second|pos|Decay constant in s^-1; derived as ln(2)/physical_half_life_seconds when that model applies.
reference_citation!|str|Nuclear data source, release and locator supporting the physical properties.
reference_version|str|Version or evaluation date of the nuclear data source.
''')
node('decay_emission','One decay branch or one emission component with a specified energy definition and yield.', '''
record_kind!|enum:decay_branch,emission_line,continuous_spectrum|Select a branch probability record or an emitted-radiation record; their denominators differ.
decay_mode|str|Decay pathway as stated by the evaluated source.
branch_fraction|fraction|Probability of this mutually identified decay branch per parent decay; dimensionless fraction from 0 to 1.
radiation_type|str|Emitted radiation, such as beta-minus, gamma, positron, alpha or Auger electron.
energy_kev|pos|Energy in keV; interpretation is specified by energy_kind.
energy_kind|enum:discrete,mean,maximum|Whether energy is a discrete line, spectral mean or endpoint.
yield_per_decay|pos|Mean emitted particles or photons per parent decay; not automatically a branching probability and may exceed one.
spectrum_uri|str|Persistent reference to an evaluated spectrum; no binary spectrum is stored here.
reference_citation!|str|Evaluation source and locator for the branch or radiation data.
''')
link('decay_emission','parent_nuclides','radionuclide',True,False,'emitted_by')
link('decay_emission','daughter_nuclides','radionuclide',False,False,'decays_to')
node('molecular_entity','One chemically specified substance or molecular component, independent of commercial packaging.', '''
preferred_name!|str|Preferred name of this exact substance or molecular form; distinguish precursor, radiolabeled product and salt.
ingredient_name|str|Ingredient-level name such as an INN, with the naming source retained in provenance.
precise_ingredient_name|str|Name of the precise chemically specified ingredient, including isotope or salt where applicable.
synonyms|strings|Alternative labels for this same identity; these are not validated equivalence mappings.
molecular_formula|str|Formula specifying the chemical species, including relevant isotope and charge conventions.
molecular_weight_g_per_mol|pos|Molar mass in g/mol for the stated exact chemical species and isotope convention.
canonical_smiles|str|Canonical SMILES with software/version supplied in provenance.
isomeric_smiles|str|SMILES preserving stereochemistry and isotope specification.
inchi|str|Full InChI structure identifier, with standard/version context.
inchi_key|str|InChIKey for the exact substance; never a numeric quantity.
stereochemistry|str|Specified stereochemical form or explicitly unresolved stereochemistry.
formal_charge|sint|Formal integer charge of the defined molecular species, not a pH-dependent averaged net charge.
''')
node('biological_target','One biological target identity; expression, binding and internalization are contextual evidence records.', '''
preferred_name!|str|Preferred biological target label.
target_type!|str|Target class such as enzyme, receptor or antigen.
gene_symbol|str|Approved gene symbol with species and naming authority identified separately.
species!|str|Organism associated with the target identity.
cellular_localization|str|Reference subcellular localization; context-specific variation belongs in evidence records.
''')
node('medicinal_product','One versioned commercial or investigational medicinal-product formulation, distinct from agent, authorization and batch.', '''
product_name!|str|Name of the commercial or investigational medicinal product.
brand_name|str|Brand label for this product and jurisdiction; not an ingredient identifier.
investigational_name|str|Sponsor-assigned investigational product name.
product_kind!|enum:ready_to_use,kit,generator,precursor,other|Presentation category; kit contents are not assumed to be a ready-to-administer radiolabeled dose.
manufactured_dose_form|str|Dose form before required preparation or transformation.
administrable_dose_form|str|Dose form after preparation for administration.
intended_routes|strings|Permitted or investigated routes according to the linked label or protocol; actual route belongs to administration.
strength_description|str|Labeled strength or concentration convention, including numerator, denominator and activity reference basis.
appearance_specification|str|Labeled appearance requirement; measured appearance belongs to a test record.
transformation_instruction|str|Source-referenced preparation instruction such as reconstitution or dilution; not an executed preparation event.
administration_device_specification|str|Device or delivery-system specification from the source label or protocol.
label_version|str|Product-label or formulation specification version.
''','Radiopharmaceutical product')
link('medicinal_product','radiopharmaceuticals','radiopharmaceutical',True,False,'formulation_of')
node('product_ingredient','One ingredient role and quantity specification in a medicinal-product formulation.', '''
ingredient_role!|enum:active,excipient,precursor,radionuclide_source,other|Role of this chemically specified component in the linked formulation.
quantity_value|pos|Ingredient quantity or concentration according to quantity_unit and quantity_basis.
quantity_unit|str|Unit, preferably a reviewed UCUM expression, for quantity_value.
quantity_basis|str|Denominator and basis, such as per mL, per vial or total compound mass, needed to interpret the quantity.
function|str|Formulation function such as stabilizer, buffer or targeting ingredient.
''','Radiopharmaceutical product')
link('product_ingredient','medicinal_products','medicinal_product',True,False,'ingredient_of')
link('product_ingredient','molecular_entities','molecular_entity',True,False,'has_identity')
node('product_package','One versioned package specification for a medicinal product, not a physical vial.', '''
package_name!|str|Human-readable package presentation label.
container_type!|str|Immediate container type, such as vial or syringe.
container_material|str|Material of the immediate container.
closure_system|str|Closure specification.
shielding_configuration|str|Shielding specification and reference; not evidence that a specific unit was handled correctly.
nominal_fill_volume_ml|pos|Nominal volume per immediate container in mL; actual fill is recorded on the unit.
headspace_description|str|Nominal headspace composition or specification.
secondary_packaging|str|Outer packaging specification.
base_quantity|pos|Number or amount to which the package specification refers.
base_unit|str|Unit for base_quantity, separate from activity and concentration units.
storage_temperature_min_c|num|Lower labeled storage temperature in degrees Celsius.
storage_temperature_max_c|num|Upper labeled storage temperature in degrees Celsius.
storage_conditions|str|Versioned storage conditions, including at-rest and in-transit distinctions when supplied.
light_protection|str|Protection from light required by the source specification.
transport_classification|str|Transport class and governing source/version; not an inferred legal classification.
radiation_safety_label|str|Label specification or referenced instruction.
expiry_reference_basis|str|Time origin used for labeled shelf life, such as calibration or end of synthesis.
shelf_life_hours|pos|Specified shelf life in hours under the stated conditions; not a universal product constant.
''','Radiopharmaceutical product')
link('product_package','medicinal_products','medicinal_product',True,False,'package_of')
node('package_component','One containment relationship between two package specifications.', '''
component_count!|int|Number of contained package units; must be positive.
''','Radiopharmaceutical product')
link('package_component','outer_packages','product_package',True,False,'contained_in')
link('package_component','inner_packages','product_package',True,False,'contains_specification')
node('regulatory_authorization','One product-specific regulatory application or authorization state in one jurisdiction at a stated date.', '''
application_identifier|str|NDA, ANDA, IND, marketing-authorization or other identifier; preserve leading zeros and identifier scheme.
application_type!|str|Application type under the named authority; do not infer approval from an NDC or application number.
regulatory_pathway|str|Legal pathway with authority and source citation; section references require regulatory review.
authority!|str|Regulatory authority responsible for the application or authorization.
jurisdiction!|str|Jurisdiction to which this state applies.
authorization_holder|str|Marketing authorization holder, distinct from manufacturer, supplier and labeler.
status!|str|Source-reported regulatory state, not inferred from availability or marketing codes.
status_date!|date|Date to which the recorded regulatory status applies.
approval_date|date|Actual approval date when supported by the source.
approved_indication|str|Source wording or reviewed representation of the indication for this authorization and label version.
label_version|str|Approved or investigational label/protocol version associated with the assertion.
reference_application_identifier|str|Identifier of the reference application with its scheme/authority in the source.
reference_relationship|str|Relationship to a reference product, such as RLD or comparator; equivalence is an evidence assertion, not automatic identity.
submission_strategy|str|Administrative filing context such as a grouped supplement, if relevant.
source_citation!|str|Authoritative source and locator supporting the regulatory assertion.
''','Radiopharmaceutical product')
link('regulatory_authorization','medicinal_products','medicinal_product',True,False,'authorizes')
link('regulatory_authorization','reference_products','medicinal_product',False,True,'references')
node('supply_offer','One dated commercial supply presentation or catalog offer; not a clinical prescription.', '''
seller!|str|Organization offering the product.
supplier|str|Organization fulfilling supply, if different from seller.
manufacturer|str|Organization manufacturing the offered product.
labeler|str|Organization named as labeler; do not equate it automatically with manufacturer.
catalog_identifier!|str|Seller-specific catalog number or SKU, kept as a string.
valid_from!|date|Date from which this offer description is known to apply.
valid_to|date|End date when supplied; absence does not assert current availability.
unit_of_sale|str|Commercial unit, distinct from physical activity and administered dose.
price_amount|pos|Optional source-reported dated price; no current price or reimbursement is inferred.
price_currency|str|Currency code associated with price_amount.
price_basis|str|Price basis and included or excluded services, such as transport or dispensing.
source_citation!|str|Catalog or contract source and retrieval context.
''','Radiopharmaceutical supply')
link('supply_offer','product_packages','product_package',True,False,'offers')
node('material_lot','One physical lot of a precursor, radionuclide stock or other manufacturing material.', '''
lot_identifier!|str|Supplier or local lot identifier, scoped to the named material and supplier.
material_kind!|enum:precursor,radionuclide_stock,excipient,other|Role of this material lot in manufacturing.
supplier|str|Supplier of this physical material lot.
production_route|str|Manufacturing route for this lot, such as reactor or cyclotron production.
expiry_datetime|time|Material expiry timestamp with explicit UTC offset.
certificate_reference|str|Certificate of analysis reference, with file hash in provenance if available.
''','Radiopharmaceutical manufacture')
link('material_lot','molecular_entities','molecular_entity',False,False,'has_identity')
link('material_lot','radionuclides','radionuclide',False,False,'contains_nuclide')
node('preparation_event','One actual production, compounding, reconstitution or dilution event with specified inputs and output batch.', '''
event_kind!|enum:production,compounding,reconstitution,dilution,other|Executed preparation activity; dispensing and administration have separate records.
recipe_name!|str|Executed recipe or SOP name.
recipe_version!|str|Version of the executed recipe or SOP.
started_datetime|time|Start timestamp with UTC offset.
completed_datetime!|time|Completion timestamp with UTC offset, including end-of-synthesis when applicable.
site_name|str|Manufacturing or preparation site identity without patient identifiers.
gmp_status|str|Source-reported GMP status with governing evidence in provenance; not an inferred certification.
execution_mode|enum:automated,manual,hybrid,unknown|Mode of execution.
instrument_name|str|Synthesis module or preparation instrument.
reaction_conditions|str|Executed temperature, time, pH and other conditions with units or an SOP reference.
purification_method|str|Executed purification method and version.
deviation_description|str|Recorded deviation and its disposition; no deviation is inferred from missing data.
''','Radiopharmaceutical manufacture')
link('preparation_event','input_material_lots','material_lot',False,True,'uses_input')
link('preparation_event','input_batches','radiopharmaceutical_batch',False,True,'uses_input')
link('preparation_event','output_batches','radiopharmaceutical_batch',True,False,'produces')
node('radiopharmaceutical_unit','One physical vial, syringe or other traceable unit from a batch at a stated calibration time.', '''
unit_identifier!|str|Local barcode or identifier for this physical unit, separate from a package NDC.
unit_kind!|str|Physical presentation such as vial or syringe.
activity_at_reference_mbq!|pos|Measured or declared total activity of this unit in MBq at activity_reference_datetime, not administered activity.
activity_reference_datetime!|time|UTC-offset timestamp to which unit activity is referenced.
activity_basis!|enum:measured,manufacturer_declared,decay_calculated|Origin of the unit activity value.
actual_fill_volume_ml|pos|Actual content volume in mL at the stated reference context.
compound_mass_ug|pos|Total mass in micrograms of the chemically specified compound; distinguish compound from radionuclide mass.
compound_amount_nmol|pos|Total amount in nmol of the specified compound, with molar-mass assumptions in provenance.
expiry_datetime!|time|Expiry of this physical unit with UTC offset.
storage_history_reference|str|Reference to documented storage and transport history.
''','Radiopharmaceutical supply')
link('radiopharmaceutical_unit','radiopharmaceutical_batches','radiopharmaceutical_batch',True,False,'unit_of_batch')
link('radiopharmaceutical_unit','product_packages','product_package',False,False,'conforms_to')
link('radiopharmaceutical_unit','preparation_events','preparation_event',False,False,'prepared_by')
node('radiopharmaceutical_order','One procurement request or patient-specific prescription, explicitly distinguished by order_kind.', '''
order_kind!|enum:procurement,patient_prescription|A procurement order is not a patient prescription.
ordered_datetime!|time|Timestamp when the request was recorded, with UTC offset.
order_status!|str|Workflow state such as requested, authorized, cancelled or fulfilled; controlled locally with a versioned policy.
requested_activity_mbq|pos|Requested activity in MBq at requested_reference_datetime, not delivered activity.
requested_reference_datetime|time|Reference timestamp for requested activity.
requested_quantity|pos|Number or amount of requested units according to requested_quantity_unit.
requested_quantity_unit|str|Unit of requested_quantity, separate from activity units.
instruction_reference|str|Authorized protocol or order instruction reference; no regimen is encoded as a model default.
''','Radiopharmaceutical supply')
link('radiopharmaceutical_order','medicinal_products','medicinal_product',True,False,'requests')
link('radiopharmaceutical_order','product_packages','product_package',False,False,'requests_package')
link('radiopharmaceutical_order','supply_offers','supply_offer',False,False,'uses_offer')
link('radiopharmaceutical_order','cases','case',False,False,'for_patient')
link('radiopharmaceutical_order','therapy_cycles','therapy_cycle',False,False,'for_cycle')
node('dispense_event','One patient-specific dispensing event allocating a traceable physical unit to a prescription.', '''
dispensed_datetime!|time|Timestamp when the unit was dispensed, with UTC offset.
dispense_status!|str|Recorded dispensing status, such as dispensed, returned or cancelled.
dispenser_reference|str|Authorized dispenser identity or pseudonym under the receiving governance policy.
custody_reference|str|Reference to custody or delivery documentation.
''','Radiopharmaceutical supply')
link('dispense_event','cases','case',True,False,'for_patient')
link('dispense_event','radiopharmaceutical_orders','radiopharmaceutical_order',True,False,'fulfills')
link('dispense_event','radiopharmaceutical_units','radiopharmaceutical_unit',True,False,'dispenses')
node('reference_evidence','One citable evidence context, population or experimental dataset; not an individual patient observation.', '''
title!|str|Title or descriptive name of the evidence item.
evidence_kind!|enum:publication,trial,regulatory_label,experimental_dataset,technical_report,other|Kind of evidence source.
setting!|enum:human_clinical,preclinical,in_vitro,computational,reference|Experimental or reference setting; never silently pool species or settings.
source_citation!|str|Citation or source location; exact identifiers can also be assigned through external_identifier.
source_version|str|Document, label, dataset or registry version.
source_locator|str|Page, section, table, figure or record locator supporting the assertion.
evidence_date|date|Date of the evidence version or observation period as defined by the source.
species|str|Organism represented in the evidence; required for biological experimental results.
population_description|str|Population, cell system, species strain or cohort context.
disease_context|str|Disease and subtype described in the source; not an anatomical target.
treatment_setting|str|Treatment line, prior therapy and other setting constraints.
study_design|str|Source-described study design.
trial_phase|str|Source-described trial phase; not a permanent agent property.
sponsor|str|Study sponsor as reported.
comparator|str|Comparator or reference condition.
sample_size|int|Number of experimental units or subjects, interpreted with sample_unit.
sample_unit|str|Unit counted by sample_size, such as participants, specimens or animals.
inclusion_criteria|str|Population inclusion and exclusion summary.
biomarker_selection_criteria|str|Biomarker selection rule and source version.
primary_endpoint|str|Prespecified primary endpoint and its definition reference.
secondary_endpoints|strings|Secondary endpoints and their definition references.
generalizability_limits|str|Known limitations on applying the evidence to another context.
evidence_level|str|Assessment under a named evidence-grading rubric supplied in provenance.
''','Research evidence')
link('reference_evidence','radiopharmaceuticals','radiopharmaceutical',False,True,'describes')
link('reference_evidence','medicinal_products','medicinal_product',False,True,'describes_product')
link('reference_evidence','biological_targets','biological_target',False,True,'describes_target')
node('computational_model','One versioned computational model specification, independent of any execution or prediction.', '''
model_name!|str|Name of the computational model.
model_release!|str|Exact model/software release; independent of the data-model version.
model_kind!|enum:compartmental,PBPK,voxel_dosimetry,tumor_control,toxicity,AI,other|Computational model family; does not assert clinical validation.
artifact_uri|str|Location of model code or weights.
artifact_sha256|str|SHA-256 digest of the exact code or weight artifact, if available.
scope!|str|Intended subject, population, organ or molecular scope.
input_requirements!|str|Required imaging, clinical, treatment-history and other inputs with units and timing conventions.
output_definition!|str|Predicted quantities and their definitions and units.
applicability_limits|str|Disease, population and acquisition settings in which use is justified by evidence.
known_failure_modes|str|Known failure modes, including domain shift and missing inputs.
identifiability_assessment|str|Parameter identifiability assessment and method.
human_oversight!|str|Required human review and intended research or clinical use constraints.
validation_status!|enum:unvalidated,internal_evaluation,external_evaluation,reviewed_for_specified_use|Evidence status; not a certification or universal claim of safety.
''','Digital twin research')
link('computational_model','reference_evidence','reference_evidence',False,True,'supported_by')
node('model_run','One recorded execution of a computational model with explicit inputs and information cutoff.', '''
run_datetime!|time|Execution timestamp with UTC offset.
information_cutoff_datetime!|time|Latest time at which input information was available for this run; prevents silent use of future evidence.
purpose!|enum:retrospective_research,prospective_research,technical_validation|Purpose of this execution; no treatment is ordered by a run record.
software_environment!|str|Runtime, dependency and hardware versions or reproducible environment reference.
random_seed|str|Random seed or explicit deterministic setting; represented as a string to preserve generator conventions.
scenario_description!|str|Scenario assumptions, including any simulated treatment activity or schedule.
input_manifest!|str|Input identifiers, hashes, availability timestamps and transformations; detailed provenance may be stored as a referenced artifact.
''','Digital twin research')
link('model_run','computational_models','computational_model',True,False,'executes')
for name,target in [('cases','case'),('therapy_courses','therapy_course'),('therapy_cycles','therapy_cycle')]:link('model_run',name,target,False,False,'for_subject')
for name,target in [('input_measurements','measurement'),('input_acquisitions','acquisition'),('input_curves','time_activity_curve'),('input_doses','absorbed_dose'),('input_administrations','administration')]:link('model_run',name,target,False,True,'uses_input')
node('model_parameter','One parameter value or distribution for a model specification or execution, with units and provenance.', '''
parameter_name!|str|Parameter identity within the referenced model.
parameter_role!|enum:prior,fixed,fitted,posterior|Role of the parameter estimate.
value|num|Point estimate in unit; omit when only a distribution is available.
unit!|str|Unit or explicit dimensionless designation.
distribution_description|str|Distribution family and parameters, with parameter units and dependence assumptions.
uncertainty_value|pos|Magnitude of reported uncertainty in uncertainty_unit.
uncertainty_unit|str|Unit of uncertainty_value, or explicit dimensionless designation.
uncertainty_kind|str|Standard deviation, confidence interval width or another explicitly defined uncertainty statistic.
anatomic_context|str|Region or compartment to which this parameter applies.
''','Digital twin research')
link('model_parameter','computational_models','computational_model',True,False,'parameter_of')
link('model_parameter','model_runs','model_run',False,False,'estimated_in')
link('model_parameter','reference_evidence','reference_evidence',False,True,'supported_by')
node('model_prediction','One simulated or predicted result from a model execution; separate from a measured dose or outcome.', '''
quantity_name!|str|Predicted quantity, with explicit endpoint or physical quantity definition.
predicted_value!|num|Predicted numerical value; never a measured administered activity or delivered dose.
unit!|str|Unit of predicted_value or explicit dimensionless designation.
prediction_time_hours|num|Prediction horizon relative to the run scenario anchor, in hours.
scenario_activity_mbq|pos|Hypothetical activity in the simulated scenario, not an administered dose.
uncertainty_lower|num|Lower uncertainty bound in the same unit as the prediction.
uncertainty_upper|num|Upper uncertainty bound in the same unit as the prediction.
uncertainty_definition|str|Interval type, probability level and derivation method.
review_status!|enum:unreviewed,reviewed,accepted_for_research,rejected|Review state for this prediction; no automatic clinical approval.
''','Digital twin research')
link('model_prediction','model_runs','model_run',True,False,'generated_by')
link('model_prediction','anatomic_targets','anatomic_target',False,False,'predicts_for')
node('radiopharmaceutical_test','One nonpatient QC, biological-reference or computational-evaluation result with an explicit subject and method.', '''
test_context!|enum:batch_qc,material_qc,unit_qc,reference_result,model_evaluation|Nonpatient context. Individual patient laboratory and ROI results remain MIDRC measurement records.
quantity_name!|str|Quantity or finding assessed, such as radiochemical purity, binding affinity or cohort median PFS.
quantity_code|str|Reviewed identifier for the test quantity, if available.
quantity_code_system|str|Code system for quantity_code.
quantity_code_version|str|Release of the coding system.
method_name!|str|Assay, calculation or assessment method.
method_version|str|Assay/SOP/software version.
result_status!|enum:final,preliminary,pending,not_performed,invalid|Result availability; pending is not negative or failed.
result_text|str|Qualitative result or narrative interpretation; no inherited MIDRC patient-result enum is broadened.
unit|str|Unit of numerical result, preferably reviewed UCUM; fraction and percent must be distinguished.
result_operator|enum:eq,lt,le,gt,ge,approx|Relation between result and reported numerical bound.
statistic|str|Statistic such as mean, median, fraction or standard deviation; cohort summaries require a population context.
assay_datetime|time|When the assay was performed, with UTC offset.
activity_reference_datetime|time|Timestamp to which any activity-dependent quantity was decay-referenced.
analyte_basis|str|Chemical species and denominator, such as total compound mass or total compound molar amount.
anatomic_context|str|Organ, tissue, lesion class, source region or reference region in the evidence; not a patient lesion identifier.
matrix|str|Assay matrix such as serum, plasma, solvent or cell system.
time_after_administration_hours|num|Elapsed time in the referenced experimental context; not the date of a patient event.
temperature_c|num|Assay temperature in degrees Celsius.
ph|num|Assay pH, with measurement method in the evidence.
uncertainty_value|pos|Uncertainty magnitude for the numerical result.
uncertainty_unit|str|Unit or explicit dimensionless designation for uncertainty_value.
uncertainty_kind|str|Uncertainty statistic and confidence level where applicable.
specification_version|str|Version of the acceptance specification used for a QC judgment.
acceptance_lower|num|Lower numerical acceptance limit, in unit, when appropriate.
acceptance_upper|num|Upper numerical acceptance limit, in unit, when appropriate.
acceptance_decision|enum:pass,fail,not_evaluated|Recorded evaluation against the named specification; not a clinical release authorization.
decay_correction_basis|str|Decay correction method, nuclide and time reference for yield, activity or purity results.
reference_radiation|str|Reference radiation and endpoint required to interpret RBE or other relative radiobiological quantities.
rubric_name|str|Named assessment rubric required for readiness, evidence or quality scores.
rubric_version|str|Version of the scoring rubric.
''','Radiopharmaceutical evidence')
# Reuse exact applicable primitive property definitions, without weakening MIDRC's patient-parent groups.
for name in ['test_result_number','test_result_percent','test_result_ratio']:
    S['radiopharmaceutical_test']['properties'][name]=copy.deepcopy(PRIOR['measurement']['properties'][name])
for name,target in [('radiopharmaceutical_batches','radiopharmaceutical_batch'),('material_lots','material_lot'),('radiopharmaceutical_units','radiopharmaceutical_unit'),('reference_evidence','reference_evidence'),('computational_models','computational_model')]:link('radiopharmaceutical_test',name,target,False,False,'assesses')
node('theranostic_pair','One evidence-supported proposed pairing of diagnostic and therapeutic agents; not an assertion of interchangeable kinetics.', '''
pair_name!|str|Label for this diagnostic and therapeutic pairing.
pair_basis!|str|Biological or chemical rationale for pairing, with limitations in pair_limitations.
pair_limitations!|str|Differences in structure, radionuclide, mass, timing and kinetics relevant to transfer of evidence.
''')
link('theranostic_pair','diagnostic_agents','radiopharmaceutical',True,False,'diagnostic_component')
link('theranostic_pair','therapeutic_agents','radiopharmaceutical',True,False,'therapeutic_component')
link('theranostic_pair','reference_evidence','reference_evidence',False,True,'supported_by')
node('external_identifier','One reviewed external identifier assignment to one explicitly typed entity; schema-level ontology mappings remain semantic_mapping records.', '''
identifier!|str|Exact external code as a string, preserving leading zeros, hyphens and case where significant.
identifier_system!|str|Identifier authority or scheme, such as RxNorm, UNII, CAS, NDC, MPID, PhPID, PubChem, DOI or PMID.
identifier_system_version|str|Release or version of the identifier system.
identifier_level!|str|Semantic level, such as RxNorm IN/PIN/SCD/SBD, NDC product/package, substance, medicinal product or publication.
preferred_label|str|Label from the identifier authority at the stated version.
jurisdiction|str|Jurisdiction where relevant to the identifier assignment.
issuer|str|Issuing authority where not inherent in identifier_system.
mapping_relation!|enum:exact,narrower,broader,related,candidate|Reviewed relationship between the linked entity and external concept; candidate is not validated equivalence.
review_status!|enum:unreviewed,reviewed,approved,rejected|Review state of this assignment.
source_citation!|str|Source supporting the identifier assignment and its semantic level.
''','Semantics and governance')
for target in ['radiopharmaceutical','radionuclide','molecular_entity','biological_target','medicinal_product','product_package','regulatory_authorization','reference_evidence']:
    link('external_identifier',{'molecular_entity':'molecular_entities','reference_evidence':'reference_evidence'}.get(target,target+'s'),target,False,False,'identifies')
# An explicit exclusive parent group establishes entity identity without attaching nonpatient data to a fake case.
targets=S['external_identifier']['links'][2:]
S['external_identifier']['links']=S['external_identifier']['links'][:2]+[{'subgroup':targets,'required':True,'exclusive':True}]

# Additions to existing nodes are optional and preserve previous serialized records.
for name,target in [('radionuclide_records','radionuclide'),('molecular_entities','molecular_entity'),('biological_targets','biological_target'),('chelators','molecular_entity'),('linkers','molecular_entity'),('targeting_vectors','molecular_entity'),('precursors','molecular_entity')]:link('radiopharmaceutical',name,target,False,True,'has_component' if target=='molecular_entity' else 'has_identity')
addfields('radiopharmaceutical','''
identity_scope|enum:reference_agent,legacy_product|Identity level of this record. New v0.4 reference-agent records are distinct from legacy product-like records; migration must preserve old identifiers.
agent_class|str|Functional class of the reference agent; product, lot and administration are separate identities in the v0.4 profile.
intended_use|strings|Intended diagnostic, therapeutic or investigational uses, supported by versioned evidence.
valency|int|Number of targeting motifs per construct.
multimerization_state|str|Monomeric or multimeric structural specification.
albumin_binding_moiety|bool|Presence of a structurally specified albumin-binding moiety; not a measured plasma binding fraction.
conjugation_site|str|Site of conjugation in the specified molecular construct.
''')
for name,target in [('medicinal_products','medicinal_product'),('input_material_lots','material_lot')]:link('radiopharmaceutical_batch',name,target,False,name=='input_material_lots','related_to')
addfields('radiopharmaceutical_batch','''
release_specification_version|str|Version of the specification used for this batch disposition.
release_status|enum:quarantined,released,rejected,pending|Recorded authorized batch disposition; this data model does not determine release.
release_datetime|time|Timestamp of the recorded batch disposition with UTC offset.
release_authority_reference|str|Authorized role or pseudonym responsible for disposition, under the receiving governance policy.
deviation_reference|str|Reference to manufacturing or QC deviations and their review.
''')
for name,target in [('radiopharmaceutical_units','radiopharmaceutical_unit'),('dispense_events','dispense_event')]:link('administration',name,target,False,False,'traceable_to')
addfields('administration','''
administered_compound_mass_ug|pos|Actual administered mass of the specified compound in micrograms, distinct from radionuclide mass.
administered_compound_amount_nmol|pos|Actual administered compound amount in nmol, with chemical identity and conversion assumptions in provenance.
administered_volume_ml|pos|Actual administered volume in mL.
infusion_duration_minutes|pos|Actual delivery duration in minutes, distinct from a protocol recommendation.
mass_analyte_basis|str|Chemical identity and total/labeled/unlabeled basis of the administered compound quantity.
''')
link('treatment_plan','model_predictions','model_prediction',False,True,'considers_prediction')
addfields('toxicity_event','''
dose_limiting_toxicity|bool|Whether the event met a named protocol's dose-limiting toxicity definition; not implied by grade alone.
dlt_definition_reference|str|Protocol, version and rule used for the dose-limiting toxicity determination.
''')
addfields('provenance','''
extraction_method|str|Manual abstraction, automated extraction or other source-processing method.
curator_reference|str|Reviewer or curator identity/pseudonym under the governance policy.
source_locator|str|Source sheet and row, or document section/page/paragraph.
curation_datetime|time|Time of curation with UTC offset.
confidence_value|num|Confidence under a named rubric; not an uncalibrated probability of truth.
confidence_rubric|str|Definition and version of the confidence scale.
conflict_status|enum:none_reported,unresolved,resolved|Status of conflicts among source assertions; missing is not evidence of agreement.
conflict_resolution|str|Documented adjudication and supporting evidence.
''')

# Canonical grain of legacy nodes is documented without breaking old schema definitions.
SPEC['radiopharmaceutical']={'new':False,'group':'Radiopharmaceutical reference','record_grain':'One reference agent in the v0.4 profile. Existing product-like records remain readable; migrate them explicitly rather than silently reinterpreting their identifiers.'}
SPEC['radiopharmaceutical_batch']={'new':False,'group':'Radiopharmaceutical manufacture','record_grain':'One physical manufacturing batch; one or more timed QC results are linked through radiopharmaceutical_test.'}

def flat(s):return [v for g in s['links'] for v in g.get('subgroup',[g])]
def finish():
    for n,s in S.items():write(OUT/'schemas'/f'{n}.json',s)
    write(OUT/'integration/radiopharmaceutical_module.json',{'version':VERSION,'new_nodes':[n for n,v in SPEC.items() if v['new']],'node_metadata':SPEC,'extended_nodes':[n for n in PRIOR if S[n]!=PRIOR[n]],'profile':'profiles/radiopharmaceutical_v040.json'})
    merged=read(OLD/'gen3_dictionary.json');merged.update(S);write(OUT/'gen3_dictionary.json',merged)
    baseline=read(OUT/'sources/midrc_dictionary_1.4.3-2-g7505333.json')
    patches=[];delta=[]
    for n,s in S.items():
        if n not in baseline:patches.append({'op':'add','path':'/'+n,'value':s});status='new';ap=list(s['properties']);al=[x['name'] for x in flat(s)]
        else:
            b=baseline[n];ap=[k for k in s['properties'] if k not in b['properties']];al=[x['name'] for x in flat(s) if x['name'] not in {v['name'] for v in flat(b)}];status='extended' if ap or al else 'unchanged'
            for k in ap:patches.append({'op':'add','path':f'/{n}/properties/{k}','value':s['properties'][k]})
            for k,p in b['properties'].items():
                if p!=s['properties'][k]:
                    assert {a:v for a,v in p.items() if a!='enum'}=={a:v for a,v in s['properties'][k].items() if a!='enum'}
                    for v in s['properties'][k]['enum'][len(p['enum']):]:patches.append({'op':'add','path':f'/{n}/properties/{k}/enum/-','value':v})
            for l in s['links'][len(b['links']):]:patches.append({'op':'add','path':f'/{n}/links/-','value':l})
        delta.append({'node':n,'status':status,'added_properties':ap,'added_links':al})
    write(OUT/'integration/midrc_additive_patch.json',patches);write(OUT/'integration/node_delta.json',sorted(delta,key=lambda x:x['node']))
    # A separate add-only patch upgrades the former merged proposal without dropping properties.
    prior_patch=[]
    for n,s in S.items():
        if n not in PRIOR:prior_patch.append({'op':'add','path':'/'+n,'value':s});continue
        for k,p in s['properties'].items():
            if k not in PRIOR[n]['properties']:prior_patch.append({'op':'add','path':f'/{n}/properties/{k}','value':p})
        for l in s['links'][len(PRIOR[n]['links']):]:prior_patch.append({'op':'add','path':f'/{n}/links/-','value':l})
    write(OUT/'integration/v030_to_v040_additive_patch.json',prior_patch)
    parents={n:{x['target_type'] for x in flat(s)} for n,s in S.items()};order=[]
    while len(order)<len(S):
        ready=sorted(n for n in S if n not in order and parents[n]<=set(order))
        assert ready,'Cyclic node dependencies: '+str({n:parents[n]-set(order) for n in S if n not in order})
        order.extend(ready)
    write(OUT/'submission_order.json',{'note':'Parent-before-child order. Administrative roots require receiving-environment provisioning; no live ingestion is implied.','node_types':order})
    for old_template in (OUT/'templates').glob('*.json'):old_template.unlink()
    for n,s in S.items():
        t={('*' if k in s['required'] else '')+k:(n if k=='type' else None) for k in s['properties'] if k not in s.get('systemProperties',[])}
        # All required properties must be represented even when an upstream root lists a system field.
        for k in s['required']:t.setdefault('*'+k,n if k=='type' else None)
        write(OUT/'templates'/f'submission_{n}_template.json',t)
        (OUT/'integration/yaml'/f'{n}.yaml').write_text(yaml.safe_dump(s,sort_keys=False,allow_unicode=True))
    author=read(OLD/'AUTHORS.json');author['authors'].insert(author['authors'].index('Tahir I Yusufaly'),'Nouran Zaid');author['order_source']='User-specified first two and final two authors retained; intervening authors ordered by surname.'
    write(OUT/'AUTHORS.json',author)
    for relative,key in [('outcomes_framework.json','model_version'),('profiles/theranostics_profiles.json','version'),('documentation/semantic_layer_examples.json','version')]:
        retained=read(OLD/relative)
        retained.update({key:'0.4.0-proposal','authorship':author,'content_unchanged_from_model_version':'0.3.0-proposal'})
        write(OUT/relative,retained)
    manifest=read(OLD/'release_manifest.json');manifest.update(version='0.4.0-proposal',release_version=VERSION,as_of='2026-11-02',authorship=author,previous_release='0.3.2',previous_schema_revision='0.3.0-proposal');write(OUT/'release_manifest.json',manifest)
    meta={x['id']:x for x in read(OLD/'node_catalog.json')}
    for n,s in S.items():
        b=next(d for d in delta if d['node']==n)
        m=meta.setdefault(n,dict(id=n,status='Proposed extension',midrc_relation='new_extension',midrc_pattern='Gen3 clinical/administrative node pattern; existing MIDRC fields reused where their context applies.',omop_candidates='Requires an explicit reviewed ETL; no new OMOP table is asserted.'))
        m.update(model_version='0.4.0-proposal',property_count=len(s['properties']))
        if n in SPEC:m.update({k:v for k,v in SPEC[n].items() if k!='new'})
    write(OUT/'node_catalog.json',list(meta.values()))
    domains=read(OLD/'domain_catalog.json')
    for group in sorted({v['group'] for v in SPEC.values()}):
        members=[n for n,v in SPEC.items() if v['group']==group]
        domains.append({'domain':group,'nodes':members})
    write(OUT/'domain_catalog.json',domains)
    edges=[]
    for n,s in S.items():
        for i,g in enumerate(s['links']):
            for l in g.get('subgroup',[g]):
                e={'source':n,'target':l['target_type'],**l};e.pop('target_type')
                if 'subgroup' in g:e.update(group_id=f'{n}:group:{i}',group_required=g.get('required',False),group_exclusive=g.get('exclusive',False))
                edges.append(e)
    graph={'model':'SNMMI-MIDRC Lu177-PSMA Theranostics','version':'0.4.0-proposal','authorship':author,'direction':'Child record to referenced parent or evidence','nodes':[{'label':S[n]['title'],**m} for n,m in meta.items()],'edges':edges}
    write(OUT/'graph/model_graph.json',graph)
    return meta,edges

if __name__=='__main__':
    finish();print(json.dumps({'schemas':len(S),'new_nodes':len(S)-len(PRIOR),'extended_nodes':[n for n in PRIOR if S[n]!=PRIOR[n]]}))
