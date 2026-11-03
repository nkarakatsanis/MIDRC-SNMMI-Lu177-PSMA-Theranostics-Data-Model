"""Revise supplied architecture and manuscript artifacts without inventing author approvals."""
from pathlib import Path
import json,copy,re,os
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'extensions/lu177_psma/v0.4.0';OLD=ROOT/'extensions/lu177_psma/v0.3.0'
SOURCES=Path(os.environ.get('LU177_DOCUMENT_SOURCES', str(OUT/'sources/manuscript_inputs')));DELIVER=Path(os.environ.get('LU177_ARTIFACT_OUTPUT', str(ROOT/'dist_work')));DELIVER.mkdir(parents=True,exist_ok=True)
authors=', '.join(json.loads((OUT/'AUTHORS.json').read_text())['authors'])
stats=json.loads((OUT/'inventory_summary.json').read_text());report=json.loads((OUT/'validation/validation_report.json').read_text())
def paras(doc):
    yield from doc.paragraphs
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:yield from c.paragraphs
    for sec in doc.sections:
        yield from sec.header.paragraphs;yield from sec.footer.paragraphs
def replace(doc,mapping):
    for p in paras(doc):
        for a,b in mapping.items():
            if a in p.text:
                # Preserve formatting when the text lies inside a run.
                if any(a in r.text for r in p.runs):
                    for r in p.runs:r.text=r.text.replace(a,b)
                else:p.text=p.text.replace(a,b)
def setmatch(doc,prefix,text):
    p=next(p for p in doc.paragraphs if p.text.startswith(prefix));p.text=text;return p
def block_before(doc,prefix,items):
    anchor=next(p for p in doc.paragraphs if p.text.startswith(prefix))
    for style,text in items:
        p=doc.add_paragraph(text,style);anchor._p.addprevious(p._p)
def addtable(doc,headers,rows,widths=None):
    t=doc.add_table(rows=1,cols=len(headers));t.autofit=False
    for c,v in zip(t.rows[0].cells,headers):c.text=v
    for vals in rows:
        for c,v in zip(t.add_row().cells,vals):c.text=str(v)
    if widths:
        for row in t.rows:
            for c,w in zip(row.cells,widths):c.width=Inches(w)
    return t
def format_tables(doc):
    for t in doc.tables:
        for i,row in enumerate(t.rows):
            trPr=row._tr.get_or_add_trPr();nr=OxmlElement('w:cantSplit');trPr.append(nr)
            if i==0:
                rep=OxmlElement('w:tblHeader');trPr.append(rep)
            for cell in row.cells:
                pr=cell._tc.get_or_add_tcPr();shd=pr.find(qn('w:shd'))
                if shd is None:shd=OxmlElement('w:shd');pr.append(shd)
                shd.set(qn('w:fill'),'173F57' if i==0 else 'F1F5F7' if i%2 else 'FFFFFF')
                borders=OxmlElement('w:tcBorders')
                for e in ['top','left','bottom','right']:
                    z=OxmlElement('w:'+e);z.set(qn('w:val'),'single');z.set(qn('w:sz'),'4');z.set(qn('w:color'),'D3DDE3');borders.append(z)
                pr.append(borders)
                for p in cell.paragraphs:
                    p.paragraph_format.space_after=Pt(5);p.paragraph_format.space_before=Pt(4)
                    for r in p.runs:
                        r.font.size=Pt(9);r.font.color.rgb=RGBColor.from_string('FFFFFF' if i==0 else '172E3C');r.bold=i==0
def author_update(doc):
    for p in doc.paragraphs:
        if 'Nicolas A Karakatsanis' in p.text and 'Tyler J Bradshaw' in p.text:p.text=authors
        if p.text.lower() in ['tentative author list','tentative authors list']:p.text='tentative authors list'
    if not any('Nicolas A Karakatsanis' in p.text for p in doc.paragraphs):
        anchor=doc.paragraphs[1]
        for text in ['tentative authors list',authors]:
            p=doc.add_paragraph(text);anchor._p.addprevious(p._p)
def save(doc,path):
    author_update(doc);format_tables(doc)
    doc.core_properties.version='0.4.0';doc.core_properties.subject='Lu177-PSMA theranostics data model 0.4.0 development proposal'
    for st in ['Title','Heading 1','Heading 2','Heading 3']:
        if st in doc.styles:doc.styles[st].font.color.rgb=RGBColor(0,0,0)
    doc.save(path)

base_map={'67 individual schemas':'90 individual schemas','67 JSON schemas':'90 JSON schemas','67 template structures':'90 template structures','921 source destinations':'1,371 source destinations','122-record invented patient journey covers 55':'153-record invented patient journey covers 78','Twenty-seven intentionally invalid':'Forty-nine intentionally invalid','67 schemas and 67 templates':'90 schemas and 90 templates','67 YAML–JSON and 67 individual–merged':'90 YAML–JSON and 90 individual–merged','122 linked records across 55 node types':'153 linked records across 78 node types','27 of 27 predefined mutations':'49 of 49 predefined mutations','921 occurrences; 94':'1,371 occurrences; 94','426 checksum matches; 67 documentation pages matched':'Checksum manifest verified; 90 documentation pages matched','67 nodes':'90 nodes','293 relationships':'412 relationships','2,519 node–property':'3,212 node–property','38 proposed nodes; 67 total node types':'61 proposed nodes; 90 total node types','Five use cases, a nine-stage patient journey and 122':'Eight use cases, a nine-stage patient journey and 153','921 source-field occurrences':'1,371 source-field occurrences','Canonical version 0 3 structure':'Canonical version 0 4 structure','Representation in version 0 3':'Representation in version 0 4'}

arch=Document(OLD/'NMMI_Lu177_PSMA_Architecture_and_Status.docx');replace(arch,base_map)
replace(arch,{'NMMI documentation 0.3.2':'NMMI model 0.4.0'})
for section in arch.sections:
 for p in section.footer.paragraphs:
  if 'NMMI model 0.4.0' in p.text:
   p.clear();p.add_run('NMMI model 0.4.0 | ')
   field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');p._p.append(field)
replace(arch,{'Lu177-PSMA theranostics data model release 0.3.0 extends':'Lu177-PSMA theranostics data model release 0.4.0 extends'})
setmatch(arch,'Documentation release','Development release 0.4.0    2 November 2026\nModel schema revision 0.4.0-proposal')
setmatch(arch,'The 24 navigation domains','The original multimodality domains remain. Additional navigation groups expose radiopharmaceutical reference identity, product, supply, manufacturing, research evidence and computational modeling.') if any(p.text.startswith('The 24 navigation domains') for p in arch.paragraphs) else None
setmatch(arch,'Domains organize navigation','Domains organize navigation; nodes define record types. One domain can span several nodes, and one node can serve multiple domains. The four laboratory families share one measurement structure. The original 24 navigation domains are retained, with additional views for the radiopharmaceutical expansion.')
setmatch(arch,'The merged _settings','The merged _settings retains the MIDRC baseline provenance. Model schema revision 0.4.0-proposal is recorded in release_manifest.json; repository and document release 0.4.0 are recorded separately in root release.json. The receiving Gen3 build assigns its own dictionary version and commit; the baseline commit is not the commit of a new deployed dictionary.')
setmatch(arch,'This document accompanies repository release','This document accompanies repository release 0.4.0 and model schema revision 0.4.0-proposal under extensions/lu177_psma/v0.4.0/. It adds 23 nodes and optional extensions to six earlier nodes. Releases 0.3.1 and 0.3.2 were documentation patches over schema 0.3.0-proposal; their original tags and assets remain unchanged.')
setmatch(arch,'The HTML has passed','The HTML contains 90 node definitions, 12 schema-derived graph views, searchable source mappings, the patient journey and eight use cases. Local DOM navigation, filtering, record inspection and JSON download controls are checked as part of this release. Graph SVGs are rendered for visual inspection. A browser runtime was unavailable; no MIDRC portal deployment, real patient data extraction or clinical criteria engine is validated.')
replace(arch,{'does not claim 921 approved concepts':'does not claim 1,371 approved concepts','Documentation release 0.3.2 accompanies this document':'Development release 0.4.0 accompanies this document'})
for t in arch.tables:
 for row in t.rows:
  if row.cells[0].text=='Radiopharmaceutical':row.cells[1].text='radiopharmaceutical, medicinal_product, product_package, radiopharmaceutical_batch, preparation_event, radiopharmaceutical_unit, radiopharmaceutical_test, radiopharmaceutical_order, dispense_event and administration\nSeparate reference agent, product specification, manufacturing evidence, physical unit and actual patient delivery.'
block_before(arch,'The model dictionary and semantic layer',[
 ('Heading 1','Radiopharmaceutical expansion in version 0 4'),
 ('Normal','Version 0.4.0 reconciles Nouran Zaid’s initial radiopharmaceutical model with the supplied IDRP document and Nicolas Karakatsanis’s digital-twin ontology blueprint. The model adds 23 node types and optional fields or links on radiopharmaceutical, radiopharmaceutical_batch, administration, treatment_plan, toxicity_event and provenance. It retains all existing clinical outcome structures and the pinned MIDRC foundation.'),
 ('Normal','The revised radiopharmaceutical workbook provides 289 domain-property rows, 129 module link rows and a shared metadata sheet. Its companion revision workbook accounts for 102 entries from Nouran’s source, all 325 blueprint fields and 23 conceptual passages from IDRP. These counts include repeated source labels, proposed relations, a work-allocation placeholder and an empty pharmacodynamics heading. Eighteen revision themes explain the structural and semantic changes; mapping approval remains pending.'),
 ('Heading 2','Identity and product structure'),
 ('Normal','A radiopharmaceutical reference agent identifies the radiolabeled construct and its target. A molecular_entity identifies an exact substance, chelator, linker or targeting component. medicinal_product describes a formulation; product_ingredient assigns ingredient roles; product_package describes a package specification. A physical radiopharmaceutical_unit is a particular vial or syringe from a batch. These identities must not be merged because their identifiers and life cycles differ.'),
 ('Normal','external_identifier assigns one code to one typed entity with a system, version, semantic level and review status. RxNorm ingredient and precise-ingredient identifiers, NDC product and package identifiers, and chemical identifiers are not interchangeable. Codes remain strings. Regulatory status is a dated regulatory_authorization in a specified jurisdiction; an NDC listing does not establish FDA approval. PhPID means Pharmaceutical Product Identifier. [12, 13]'),
 ('Heading 2','Manufacturing quality and actual delivery'),
 ('Normal','material_lot identifies precursor and radionuclide stock. preparation_event records production, compounding or transformation, including input lots and output batch. radiopharmaceutical_test records one timed QC result; batch disposition remains an authorized, separately recorded action. Specific activity and molar activity are distinct quantities with mass and molar denominators and explicit activity-reference times. Neither is an invariant nuclide property. [14]'),
 ('Normal','A supply_offer describes a dated catalog presentation. radiopharmaceutical_order distinguishes procurement from a patient prescription; dispense_event connects a patient prescription with a physical unit. administration retains the authoritative delivered activity and its reference time and may link the dispensed unit. Requested, calibrated, pre-injection, residual and administered activities must be compared only after reconciling their time bases and measurement methods.'),
 ('Heading 2','Reference evidence and computational research'),
 ('Normal','The IDRP source prioritizes human clinical use, whereas the blueprint includes preclinical and computational research. Version 0.4.0 makes these scopes explicit. reference_evidence identifies setting, species, population, source and version. A nonpatient radiopharmaceutical_test records a contextual result such as binding affinity or a cohort PK estimate. Human laboratory and ROI observations continue to use MIDRC measurement records and their required patient-related parents.'),
 ('Normal','computational_model identifies the exact model release; model_run records an execution, its inputs and information cutoff; model_parameter carries a value or distribution with units; model_prediction carries a scenario result. Predictions do not overwrite absorbed_dose or administration records. A treatment plan may cite a prediction as evidence, but no prescribing algorithm is supplied. Readiness and confidence scores require declared rubrics rather than unexplained numbers.'),
 ('Heading 2','Definitions requiring careful reconciliation'),
 ('Normal','Physical decay and biological metabolism are different processes. The source example describing Lu-177 decay to Hf-177 is not imported as a metabolite. Branch probability and emission yield have distinct denominators. Biological, physical and effective half-lives require separate context. Absorbed dose, BED and EQD2 are different quantities; RBE needs a reference radiation, endpoint and model. Source numerical examples, product codes, dose ranges and billing codes remain unverified and are not defaults.'),
 ('Heading 2','Upgrade from the earlier proposal'),
 ('Normal','The new dictionary is additive relative to schema 0.3.0-proposal. Existing records remain readable. Legacy product-like radiopharmaceutical records and the ambiguous batch specific_activity field are retained for compatibility. Curators should create an explicit agent/product distinction and timed QC records, preserve the old identifiers and source provenance, and document the migration. No mass-to-molar conversion or identity reassignment is inferred automatically.')])
block_before(arch,'JSON templates tables and relationship rules',[
 ('Heading 1','Radiopharmaceutical use cases'),
 ('Heading 2','Trace a delivered unit back to its quality evidence'),
 ('Normal','In the invented patient journey, SYN-ADMINISTRATION links RP-UNIT and RP-DISPENSE. Dispensing fulfills RP-ORDER for the same patient and cycle. The unit identifies SYN-RADIOPHARMACEUTICAL_BATCH; RP-PREP identifies its input lots and output batch. RP-QC-RCP, RP-QC-MOLAR and RP-QC-STERILITY point to the batch. The sterility result is pending, while disposition is separately documented. This illustrates traceability and status separation, without claiming a clinically adequate release protocol.'),
 ('Heading 2','Use research evidence without changing its subject'),
 ('Normal','RP-PK contains an invented cohort mean biological half-life linked to explicitly preclinical RP-EVIDENCE. It is not a patient measurement. A human lesion’s time_activity_curve instead references its anatomical target, actual administration and ROI evidence. Translating the preclinical result to that person would require a justified computational model and a separately recorded prediction.'),
 ('Heading 2','Compare a hypothetical prediction with an observed estimate'),
 ('Normal','RP-PREDICTION is an invented 4 Gy scenario value tied to RP-RUN and model release DEMO-1. The run records its information cutoff and inputs. SYN-DOSE-LESION-C1 remains a separate 5 Gy dose estimate linked to its imaging and dosimetry evidence. No numerical prediction model was executed; the values demonstrate distinct record types and auditable relationships.')])
block_before(arch,'References and source materials',[
 ('Heading 2','Radiopharmaceutical validation and remaining review'),
 ('Normal','The combined local validator accepts 153 records across 78 node types, preserves acceptance of all 122 prior records and all 29 MIDRC baseline fixtures, and rejects 49 predefined invalid cases. The 22 added mutations exercise identifier type and entity level, decay/emission confusion, QC subject and status, activity units/reference time, patient prescriptions, expiry, preparation inputs, package cycles, evidence setting, prediction intervals and information cutoff. Both baseline-to-current and v0.3-to-v0.4 additive patches reproduce the merged dictionary.'),
 ('Normal','These checks do not validate every regulatory rule, nuclear-data evaluation, radiopharmacy release policy, NucLex binding or clinical criterion. The receiving team should approve collection profiles and run a real Gen3 build, migration, submission and export round trip. The field definitions and source crosswalk remain proposals for expert review.')])
arch.add_paragraph('Release 0.4.0 | 2 November 2026. Additive radiopharmaceutical and research expansion, revised workbooks, architecture, explorer, manuscript and supplementary documentation.')
for txt in ['[12] FDA National Drug Code Directory. https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory (accessed 2 November 2026).','[13] FDA Identification of Medicinal Products. https://www.fda.gov/industry/fda-data-standards-advisory-board/identification-medicinal-products-idmp (accessed 2 November 2026).','[14] EANM guidance on molar activity and specific activity. https://pmc.ncbi.nlm.nih.gov/articles/PMC8502193/ (accessed 2 November 2026).','New supplied sources: Radiopharmaceutical Digital Twin Ontology Blueprint_NK.xlsx; Radiopharmaceutical data model_Nov2026_NZ.xlsx; NucLex_ RadioPharmaceutical Ontology (IDRP).docx. Source hashes and row/paragraph crosswalks are distributed with v0.4.0.']:
 block_before(arch,'Release history',[('Normal',txt)])
for p in arch.paragraphs:
 if p.text.startswith(('The model dictionary and semantic layer','References and source materials','JSON templates tables and relationship rules')):
  p.paragraph_format.page_break_before=False
# Replace the old schema-version-labelled diagram with the freshly generated graph.
for shape in list(arch.inline_shapes):
    run=shape._inline.getparent().getparent();para=run.getparent();para.remove(run)
    from docx.text.paragraph import Paragraph
    Paragraph(para,arch).add_run().add_picture(str(OUT/'graph/lesion_dose.png'),width=Inches(6.4))
save(arch,OUT/'NMMI_Lu177_PSMA_Architecture_and_Status.docx')

man=Document(SOURCES/'Lu177_PSMA_v0.3.0_Scientific_Data_Manuscript.docx');replace(man,base_map)
replace(man,{'38 new node types':'61 new node types','describes five reuse tasks':'describes eight reuse tasks'})
replace(man,{'version 0.3.0':'version 0.4.0','Version 0.3.0':'Version 0.4.0','v0.3.0':'v0.4.0','67 schemas':'90 schemas','all 67':'all 90','all 122 linked':'all 153 linked','27 predefined':'49 predefined','Twenty-seven predefined':'Forty-nine predefined','122 entirely invented records spanning 55':'153 entirely invented records spanning 78','67 node types, 293 declared schema links, 24 domain-navigation groups and 2,519':'90 node types, 412 declared schema links, '+str(stats['domain_count'])+' domain-navigation groups and 3,212','55 node types':'78 node types'})
setmatch(man,'Longitudinal radiopharmaceutical therapy research','Longitudinal radiopharmaceutical research requires connections between product identity, preparation, treatment delivery, imaging, dosimetry, safety and outcomes. We describe version 0.4.0 of a proposed extension to the Medical Imaging and Data Resource Center Gen3 dictionary. It preserves 29 baseline node types and adds 61, including 23 radiopharmaceutical and research nodes introduced in this revision. The resource contains 412 declared relationships and 3,212 node–property entries. It separates agent, substance, medicinal product, package, batch, physical unit, dispensing and administration. Contextual evidence and computational predictions remain distinct from individual patient measurements. Machine-readable schemas, human-readable definitions, source crosswalks and synthetic examples support inspection and reuse. The revised radiopharmaceutical crosswalk accounts for 450 source entries, alongside the earlier clinical and outcome catalog. Local validation accepts 153 connected records, 29 baseline fixtures and all 122 earlier example records, and rejects 49 predefined invalid cases. Comprehensive terminology review, production Gen3 ingestion and clinical validation remain to be established.')
setmatch(man,'The manuscript characterizes','We revised the published 0.3.2 repository release, which retained model schema revision 0.3.0-proposal, to produce 0.4.0-proposal on 2 November 2026. The implementation preserves the deployed MIDRC dictionary 1.4.3-2-g7505333, commit 7505333d56c87a289463a814131e38d0f2be6674, retrieved on 16 October 2026. Its preserved SHA-256 is 578e57dc45f719b07f1ac31482fed9129675c133aaafc3004dc346e5e4928e21. The source snapshot, additive patches, current schemas and generation scripts identify the release boundary.6')
for p in man.paragraphs:
 if 'cc3f5fa2b7e7c5e8c81c5ad9bd1c8a710324fedc' in p.text:
  p.text=p.text.replace('The exact source commit is cc3f5fa2b7e7c5e8c81c5ad9bd1c8a710324fedc.','The exact release commit is resolved by the immutable v0.4.0 tag; the package checksum manifest identifies its files.').replace('commit cc3f5fa2b7e7c5e8c81c5ad9bd1c8a710324fedc','the immutable v0.4.0 release tag')
setmatch(man,'Version 0.4.0 contains',f'Version 0.4.0 contains 90 node types, 412 declared schema links, {stats["domain_count"]} domain-navigation groups and 3,212 node–property entries. Counts include administrative and link properties and are not counts of distinct clinical concepts. The package preserves 824 baseline property definitions apart from seven declared enum appends inherited from v0.3.0. The synthetic collection contains 153 records across 78 node types, including one invented human journey and separately identified reference and computational examples. No clinical population coverage is inferred.')
setmatch(man,'We reran scripts/validate_model.py','We executed scripts/validate_model.py for version 0.4.0 using Python 3.12 and jsonschema 4.26.0. It returned PASS with no reported errors. All 90 schemas and templates passed the implemented checks, all 153 linked example records were accepted, and all 29 baseline fixtures remained accepted. The 122 earlier example records also remained accepted. Each of 49 predefined invalid cases produced a rejection. The baseline-to-current and prior-proposal-to-current additive patches reproduced the merged dictionary. Table 3 separates these results from deployment and semantic claims.')
setmatch(man,'Additional deterministic inspection','Additional deterministic inspection compares each parsed YAML schema with its JSON counterpart and each individual schema with the merged dictionary. All 90 pairs in each comparison agree. Release packaging verifies every entry in SHA256SUMS.txt, and the documentation generator checks all 90 node pages against the schemas. These checks address representation agreement and file integrity; they cannot exclude a design error shared across representations. Commands are supplied in Supplementary Information.')
block_before(man,'Synthetic fixtures and validation design',[
 ('Heading 2','Radiopharmaceutical source reconciliation'),
 ('Normal','Three supplied development drafts motivated the v0.4.0 expansion: Nouran Zaid’s radiopharmaceutical data-model workbook, Nicolas Karakatsanis’s radiopharmaceutical digital-twin blueprint and the IDRP radiopharmaceutical ontology document. We retained row or paragraph locations and source hashes. The crosswalk accounts for 102 entries in the initial model, 325 blueprint fields and 23 selected conceptual passages from IDRP. Source occurrences include duplicates, an unfilled section and a work-allocation placeholder; they are not all distinct data elements. Each proposed destination is checked against the actual dictionary. Eighteen revision themes document the issue, change and rationale. Definitions and source-suggested codes remain subject to expert review.'),
 ('Normal','The sources differ in scope. IDRP emphasizes human clinical development and care, whereas the blueprint also covers preclinical evidence and digital twins. We retained a human clinical profile and added explicit radiopharmacy, reference-research and computational-research profiles. Patient-level laboratory, imaging, dose, safety and response data continue to use existing model nodes. Nonpatient QC and aggregate research findings use radiopharmaceutical_test with context-appropriate parent links; the mandatory patient-related parents of MIDRC measurement were not weakened.'),
 ('Heading 2','Product identity and the medication process'),
 ('Normal','Reference agent, chemically specified substance, medicinal-product formulation, package specification, physical batch and physical unit have separate record identities. product_ingredient assigns a substance’s role in a formulation. external_identifier assigns a string code to exactly one typed entity, with scheme, release, semantic level and review state. regulatory_authorization records jurisdiction, application, date and source. An NDC listing does not establish approval, and PhPID denotes Pharmaceutical Product Identifier.23,24'),
 ('Normal','material_lot and preparation_event preserve precursor and radionuclide inputs, recipe and execution history. Timed QC results retain method, result status, units and specification; batch disposition remains separate. Molar activity and specific activity have different denominators and require chemical and time context.25 supply_offer, radiopharmaceutical_order and dispense_event distinguish catalog supply, procurement or prescription, and patient-specific dispensing. The existing administration record remains authoritative for actual delivered activity and may reference its physical unit and dispensing event.'),
 ('Heading 2','Evidence and computational provenance'),
 ('Normal','reference_evidence identifies a source, experimental setting, species and population. Context-dependent binding, pharmacokinetic, radiobiological and aggregate outcome results are separate test records. A source example describing radioactive decay was excluded from the metabolism representation. Physical, biological and effective half-life; emission yield and decay-branch probability; and absorbed dose, BED and EQD2 require distinct quantity definitions and contextual assumptions.'),
 ('Normal','computational_model, model_run, model_parameter and model_prediction separate model specification, execution, parameterization and hypothetical output. A run identifies its release, inputs and information cutoff. Predictions retain units, scenario and uncertainty and do not overwrite observed dose or response. A treatment plan can cite a prediction as evidence without converting it into an automated prescription. The supplied computational records are invented structural fixtures; no predictive algorithm, calibration study or clinical performance result is reported.')])
man.tables[0].add_row().cells[0].text='Radiopharmaceutical process'
man.tables[0].rows[-1].cells[1].text='medicinal_product; product_package; radiopharmaceutical_batch; preparation_event; radiopharmaceutical_unit; dispense_event'
man.tables[0].rows[-1].cells[2].text='Product and package specifications, lot evidence and patient delivery have separate identities.'
man.tables[0].add_row().cells[0].text='Research and computation'
man.tables[0].rows[-1].cells[1].text='reference_evidence; radiopharmaceutical_test; computational_model; model_run; model_parameter; model_prediction'
man.tables[0].rows[-1].cells[2].text='Population evidence, model specifications, executions and predictions remain distinct from patient observations.'
block_before(man,'Semantic and deployment limits',[
 ('Normal','Twenty-two additional negative mutations test radiopharmaceutical identifiers and entity levels, nuclear-data distinctions, QC subject/status/unit constraints, activity-reference times, prescription patient links, expiry, preparation inputs, package-containment cycles, preclinical context and computational intervals/cutoffs. The tests are specified in the distributed validator. They demonstrate selected consistency checks, not compliance with all regulatory, radiopharmacy or prediction-model requirements.')])
for p in man.paragraphs:
 if p.text.startswith('6. '):p.text='6. Karakatsanis, N. A. et al. Lu177-PSMA theranostics data model, development release 0.4.0. GitHub https://github.com/nkarakatsanis/MIDRC-SNMMI-Lu177-PSMA-Theranostics-Data-Model/releases/tag/v0.4.0 (2026).'
anchor=next(p for p in man.paragraphs if p._p.xpath('.//w:drawing'))
for txt in ['23. U.S. Food and Drug Administration. National Drug Code Directory. https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory (accessed 2 November 2026).','24. U.S. Food and Drug Administration. Identification of Medicinal Products. https://www.fda.gov/industry/fda-data-standards-advisory-board/identification-medicinal-products-idmp (accessed 2 November 2026).','25. EANM guidance on molar activity and specific activity. https://pmc.ncbi.nlm.nih.gov/articles/PMC8502193/ (2021).']:
 p=man.add_paragraph(txt);anchor._p.addprevious(p._p)
# Preserve the supplied illustrative figure, with its caption and clinical scope; it has no version-specific schema additions.
save(man,DELIVER/'Lu177_PSMA_v0.4.0_Scientific_Data_Manuscript.docx')

supp=Document(SOURCES/'Lu177_PSMA_v0.3.0_Supplementary_Information.docx');replace(supp,base_map)
setmatch(supp,'The source is Git tag','The source is the immutable release tag v0.4.0 in the repository cited in the main manuscript. Resolve that tag to obtain the exact release commit. The local audit uses Python 3.12, jsonschema 4.26.0 and PyYAML for representation comparison. These versions identify the audit environment; they do not assert that every dependency is pinned.')
setmatch(supp,'The first command should return','The first command returns the exact release commit. The validator reports PASS with zero errors: 90 schemas/templates, 153 linked synthetic records, 29 baseline fixtures, acceptance of all 122 earlier records and 49 rejected negative-test mutations. The documentation check compares all 90 node pages with their schemas. The validator regenerates its report and baseline fixtures and makes no network submission of records.')
setmatch(supp,'Observed output was','The expected representation result is 90 matched nodes. Checksum verification must match every entry in the release manifest; the exact number depends on the packaged artifacts. These tests establish representation agreement and integrity, not clinical realism, source-image processing or production service behavior.')
replace(supp,{'v0.3.0':'v0.4.0','version 0.3.0':'version 0.4.0','122 records':'153 records','67 schemas':'90 schemas','27 negative':'49 negative','all 67':'all 90','all 426':'all listed','Five registry reuse tasks':'Eight registry reuse tasks','five reuse tasks':'eight reuse tasks'})
for p in supp.paragraphs:
 if 'cc3f5fa2b7e7c5e8c81c5ad9bd1c8a710324fedc' in p.text:p.text=p.text.replace('cc3f5fa2b7e7c5e8c81c5ad9bd1c8a710324fedc','v0.4.0 (resolve the tag to its exact release commit)')
block_before(supp,'Supplementary Table S2',[
 ('Heading 2','Trace preparation and quality for a delivered unit'),
 ('Normal','Start with SYN-ADMINISTRATION and follow radiopharmaceutical_units to RP-UNIT and dispense_events to RP-DISPENSE. Dispensing identifies RP-ORDER and the same patient. The unit references SYN-RADIOPHARMACEUTICAL_BATCH and RP-PREP; the preparation names precursor and radionuclide material lots. Reverse-query radiopharmaceutical_test by that batch to retrieve RCP, molar-activity and pending-sterility evidence. No synthetic QC specification is a clinically approved release rule.'),
 ('Heading 2','Retain the subject of a research result'),
 ('Normal','RP-EVIDENCE is explicitly preclinical and describes an invented cohort. RP-PK stores its kidney biological-half-life result with units and a cohort-mean statistic. No case link is introduced. Individual human activity curves still identify the persistent target and actual administration. This tests separation of subject and evidence context, without claiming translational validity.'),
 ('Heading 2','Inspect a prediction and its information cutoff'),
 ('Normal','RP-PREDICTION records an invented 4 Gy scenario result. RP-RUN identifies model release DEMO-1, an input administration and a cutoff on 4 January 2026. RP-PARAMETER supplies a unit-bearing parameter. The separate recorded lesion estimate remains SYN-DOSE-LESION-C1 at 5 Gy. No actual prediction algorithm was executed and the difference is not an evaluation of prediction accuracy.')])
supp.add_heading('Supplementary Note 3 Radiopharmaceutical revision audit',level=1)
supp.add_paragraph('The 0.4.0 source crosswalk contains 450 new entries: 102 from Nouran’s model, 325 from the blueprint and 23 IDRP passages. The original 921 source occurrences and all 94 revised outcome entries remain. Each row identifies its original location, proposed destination, qualifiers, transformation and revision theme. Compound source fields are split by quantity; duplicate labels can map to the same canonical element while retaining their source occurrences.')
supp.add_paragraph('scripts/radiopharmaceutical_profile.py implements the additional checks. The main validator runs 49 negative mutations in total and verifies acceptance of the prior 122-record fixture. Source-code membership in NucLex, RadLex, RxNorm or a current regulatory registry is not verified. No clinical dosing values or current vendor prices are derived from the supplied examples.')
supp.add_paragraph('For local reproduction, run python extensions/lu177_psma/v0.4.0/scripts/validate_model.py; then python scripts/build_dictionary_docs.py --check. Compare each YAML node in integration/yaml with schemas, compare schemas with gen3_dictionary.json and verify SHA256SUMS.txt. The prior model directory is retained to support regression and migration checks.')
save(supp,DELIVER/'Lu177_PSMA_v0.4.0_Supplementary_Information.docx')

notes=Document(SOURCES/'Lu177_PSMA_v0.3.0_Submission_Notes.docx');replace(notes,base_map)
replace(notes,{'v0.3.0':'v0.4.0','version 0.3.0':'version 0.4.0','67 node types, 293 declared relationships':'90 node types, 412 declared relationships','adding 38 nodes':'adding 61 nodes','67 schemas/templates, 122 synthetic records':'90 schemas/templates, 153 synthetic records','all 27 predefined negative cases':'all 49 predefined negative cases','All 67 YAML–JSON':'All 90 YAML–JSON','all 426 checksums matched':'the release checksum manifest is verified'})
notes.paragraphs[1].text='The manuscript now describes development release 0.4.0, including the radiopharmaceutical product, manufacturing, delivery and research-evidence expansion. It retains the requested Data Descriptor structure, with worked patient and radiopharmaceutical use cases in the supplement. The revised artifacts remain a scientific manuscript draft for author review, not a submitted or accepted publication.'
block_before(notes,'What the repository supports',[
 ('Heading 2','New material in version 0 4'),
 ('Normal','The revision adds 23 nodes and optional additions to six prior nodes. The source audit accounts for 450 radiopharmaceutical entries and 18 revision themes. A second workbook documents the revised model; the review workbook pinpoints each proposed mapping and rationale. Nouran Zaid is added after Jazmin Schwartz and before Tahir I Yusufaly, preserving the requested fixed first two and final two author positions. The author list remains tentative.'),
 ('Normal','Review the new definitions and profile requiredness with radiopharmacy, clinical, regulatory and ontology experts. In particular, verify exact ingredient/product/package identity, release-specification evidence, timing and unit conventions, and the boundary between cohort evidence and patient observations. The computational fixtures demonstrate structure only; no predictive-performance claim belongs in the manuscript.')])
save(notes,DELIVER/'Lu177_PSMA_v0.4.0_Submission_Notes.docx')
print(json.dumps({'documents':['architecture','manuscript','supplement','submission_notes'],'version':'0.4.0'}))
