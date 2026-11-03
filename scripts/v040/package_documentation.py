from build_module import ROOT,OUT,OLD,read,write
from pathlib import Path
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
import json,csv,shutil,xml.etree.ElementTree as ET,hashlib,os

DELIVER=Path(os.environ.get('LU177_ARTIFACT_OUTPUT',str(ROOT/'dist_work')))
authors=read(OUT/'AUTHORS.json');author_text=', '.join(authors['authors'])
meta=read(ROOT/'release.json');meta.update(release_version='0.4.0',git_tag='v0.4.0',release_title='0.4.0',release_date='2026-11-02',model_directory='extensions/lu177_psma/v0.4.0',model_artifact_revision='0.4.0-proposal',version_policy='Minor development release with additive schema extensions; previous tags and v0.3.0 directory remain unchanged. Model, baseline and terminology versions are independent.',authorship=authors,release_kind='Additive radiopharmaceutical and research expansion',previous_release='0.3.2',standalone_document_version='0.4.0',model_schema_changed=True)
write(ROOT/'release.json',meta);(ROOT/'VERSION').write_text('0.4.0\n')
for folder in ['review','publication']:(OUT/folder).mkdir(exist_ok=True)
for p in DELIVER.glob('*.xlsx'):shutil.copy2(p,OUT/'review'/p.name)
for p in DELIVER.glob('Lu177_PSMA*.docx'):shutil.copy2(p,OUT/'publication'/p.name)
shutil.copy2(OUT/'NMMI_Model_Explorer.html',DELIVER/'NMMI_Model_Explorer_v0.4.0.html')
shutil.copy2(OUT/'NMMI_Lu177_PSMA_Architecture_and_Status.docx',DELIVER/'NMMI_Lu177_PSMA_Architecture_and_Status_v0.4.0.docx')

def markdown(docx):
    doc=Document(docx);out=[]
    for child in doc.element.body:
        tag=child.tag.rsplit('}',1)[-1]
        if tag=='p':
            p=Paragraph(child,doc);txt=p.text.strip()
            if not txt:continue
            if p.style.name=='Title':out.append('# '+txt)
            elif p.style.name.startswith('Heading '):out.append('#'*(int(p.style.name.split()[-1])+1)+' '+txt)
            else:out.append(txt)
        elif tag=='tbl':
            t=Table(child,doc);rows=[[c.text.replace('\n','<br>').replace('|','\\|') for c in r.cells] for r in t.rows]
            out+=['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*len(rows[0]))+' |']+['| '+' | '.join(r)+' |' for r in rows[1:]]
        out.append('')
    return '\n'.join(out)
model_markdown=markdown(OUT/'NMMI_Lu177_PSMA_Architecture_and_Status.docx')
model_markdown=model_markdown.replace('Figure 1.', '![Lesion dose evidence graph](../extensions/lu177_psma/v0.4.0/graph/lesion_dose.svg)\n\nFigure 1.',1)
(ROOT/'docs/DATA_MODEL.md').write_text(model_markdown.rstrip()+'\n')
prefix='../extensions/lu177_psma/v0.4.0'
catalog=['# Node catalog — release 0.4.0','', '**tentative authors list**','',author_text,'',
         '90 node types. The schema is authoritative for property and link constraints.','',
         '| Node | Group | One record represents | MIDRC relationship | Properties | Representations |',
         '| --- | --- | --- | --- | --- | --- |']
for n in read(OUT/'node_catalog.json'):
 name=n['id'];links=f'[JSON]({prefix}/schemas/{name}.json) · [YAML]({prefix}/integration/yaml/{name}.yaml) · [template]({prefix}/templates/submission_{name}_template.json)'
 catalog.append(f"| [{name}](dictionary/{name}.md) | {n['group']} | {n['record_grain']} | {n['midrc_relation']} | {n['property_count']} | {links} |")
(ROOT/'docs/NODE_CATALOG.md').write_text('\n'.join(catalog)+'\n')
domains=['# Domain index — release 0.4.0','', '**tentative authors list**','',author_text,'',
         '32 navigation groups. Nodes may serve more than one domain; these groups do not create duplicate records.','',
         '| Domain | Reused node types |','| --- | --- |']
for domain in read(OUT/'domain_catalog.json'):
 domains.append('| '+domain['domain']+' | '+', '.join(f'[`{n}`]({prefix}/schemas/{n}.json)' for n in domain['nodes'])+' |')
(ROOT/'docs/DOMAINS.md').write_text('\n'.join(domains)+'\n')
notice=(OUT/'NOTICE.md').read_text().replace('Version 0.3 adds','Version 0.4 adds').replace('Jazmin Schwartz, Tahir','Jazmin Schwartz, Nouran Zaid, Tahir')
(OUT/'NOTICE.md').write_text(notice)

baseline='Lu177-PSMA theranostics data model release 0.4.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.'
release=f'''# Release 0.4.0

2 November 2026 · Development proposal for technical and scientific review.

{baseline}

Baseline SHA-256: `578e57dc45f719b07f1ac31482fed9129675c133aaafc3004dc346e5e4928e21`.

## Additive model changes

- Add 23 nodes separating reference agent/substance/target identity, product and packaging, manufacturing, physical units, supply, prescription, dispensing, reference evidence and computational research.
- Add optional fields or links to six earlier nodes: `radiopharmaceutical`, `radiopharmaceutical_batch`, `administration`, `provenance`, `toxicity_event` and `treatment_plan`.
- Retain all 29 MIDRC baseline nodes and all earlier clinical outcome structures. The seven enum appends were already proposed in v0.3.0; this release introduces no additional baseline enum changes.
- Distinguish molar and specific activity, physical decay and biological metabolism, reference/cohort evidence and human observations, and predicted and measured quantities.
- Add an explicit v0.3-to-v0.4 additive patch and context validation. Legacy fields remain readable; curating the new normalized profiles requires an explicit, provenance-preserving migration.

## Review materials

The model now contains 90 nodes, 412 declared links and 3,212 node–property entries. The 1,371 source occurrences include 450 radiopharmaceutical entries: 102 from Nouran's initial model, 325 from the blueprint and 23 IDRP passages. Eighteen revision themes and source-by-source crosswalks identify proposed changes and reasons.

The release includes revised model and rationale workbooks, an offline HTML explorer with 12 graph views, the architecture/status document, a scientific manuscript draft, supplementary information and submission notes. Nouran Zaid is added after Jazmin Schwartz and before Tahir I Yusufaly in the tentative authors list.

## Validation and limits

Local validation accepts all 153 connected example records, all 122 prior records and 29 baseline fixtures. All 49 predefined invalid cases are rejected. Both additive patches reproduce the merged dictionary; JSON/YAML and generated documentation agree. The examples are synthetic and no prediction algorithm was executed.

This release does not establish production Gen3 deployment, clinical validity, regulatory compliance, ontology-owner approval or institutional adoption. It does not submit the manuscript to a journal. NucLex alignment and context-specific terminology review remain pending.

## Version identity

Repository/document release: **0.4.0**; Git tag: **v0.4.0**; schema revision: **0.4.0-proposal**; model directory: `extensions/lu177_psma/v0.4.0/`. The old `v0.3.0/` directory, earlier tags and release assets remain unchanged. This is an additive minor release, following documentation-only releases 0.3.1 and 0.3.2.

**tentative authors list**

{author_text}
'''
(ROOT/'releases/0.4.0.md').write_text(release)
old=(ROOT/'CHANGELOG_LU177_PSMA.md').read_text()
old=old[old.index('## 0.3.2'):]
entry=release.replace('# Release 0.4.0','## 0.4.0',1)
entry=entry.replace('\n## Additive','\n### Additive').replace('\n## Review','\n### Review').replace('\n## Validation','\n### Validation').replace('\n## Version','\n### Version')
(ROOT/'CHANGELOG_LU177_PSMA.md').write_text('# Lu177-PSMA changelog\n\n'+entry+'\n'+old)

readme=(ROOT/'README.md').read_text()
if '### Radiopharmaceutical review and manuscript' in readme:
 start=readme.index('### Radiopharmaceutical review and manuscript');end=readme.index('## Data Dictionary',start)
 readme=readme[:start]+readme[end:]
# Current links/counts move forward; historical prose below is replaced explicitly.
for a,b in {'0.3.2':'0.4.0','extensions/lu177_psma/v0.3.0':'extensions/lu177_psma/v0.4.0','67 nodes':'90 nodes','2,519':'3,212','24 domain navigation':'32 domain navigation','67 node types and 293 relationships':'90 node types and 412 relationships','plus 38 proposed':'plus 61 proposed','adds 38 theranostics nodes':'adds 61 extension nodes','67 schemas and templates':'90 schemas and templates','921 source occurrences':'1,371 source occurrences','122 synthetic linked records':'153 synthetic linked records','27 deliberately invalid':'49 deliberately invalid','Jazmin Schwartz, Tahir':'Jazmin Schwartz, Nouran Zaid, Tahir'}.items():readme=readme.replace(a,b)
start=readme.index('Release **0.4.0**');end=readme.index('\n## Start here',start)
readme=readme[:start]+'Release **0.4.0** adds a radiopharmaceutical module covering agent, substance, product, package, batch, preparation, physical unit, QC, prescription and dispensing. Separate reference-evidence and computational nodes preserve the distinction between cohort findings, patient observations and predictions. Model schema revision **0.4.0-proposal** adds 23 nodes and optional additions to six existing nodes.\n'+readme[end:]
readme=readme.replace('The complete v0.3.0 proposal','The complete v0.4.0 proposal').replace('revised from the author-supplied file for documentation release 0.4.0','updated for the radiopharmaceutical expansion in release 0.4.0')
pos=readme.index('\n## Data Dictionary')
readme=readme[:pos]+'''
### Radiopharmaceutical review and manuscript

| Resource | Purpose |
| --- | --- |
| [Revised radiopharmaceutical model](extensions/lu177_psma/v0.4.0/review/Radiopharmaceutical_Data_Model_v0.4.0.xlsx) | Nodes, definitions, constraints, typed links and profiles. |
| [Revisions and rationale](extensions/lu177_psma/v0.4.0/review/Radiopharmaceutical_Revisions_and_Rationale_v0.4.0.xlsx) | Every source entry, proposed destination and revision rationale. |
| [Scientific manuscript draft](extensions/lu177_psma/v0.4.0/publication/Lu177_PSMA_v0.4.0_Scientific_Data_Manuscript.docx) | Updated architecture and executed validation, for author review. |
| [Supplementary information and submission notes](extensions/lu177_psma/v0.4.0/publication/) | Worked use cases, audit procedure and remaining publication decisions. |

'''+readme[pos:]
start=readme.index('## Versioning');end=readme.index('## Authorship',start)
readme=readme[:start]+f'''## Versioning and baseline

{baseline}

The repository and document release is **0.4.0**, tagged **v0.4.0**. Schema revision **0.4.0-proposal** is under `extensions/lu177_psma/v0.4.0/`. Releases 0.3.1 and 0.3.2 were documentation patches over schema 0.3.0-proposal. Historical tags, original assets and the old model directory remain unchanged.

The preserved baseline SHA-256 is `578e57dc45f719b07f1ac31482fed9129675c133aaafc3004dc346e5e4928e21`. Imported source parent `bee947238381704486ccd12beeb8f4689fb22843` is a different revision; the receiving Gen3 build must reconcile it. `pyproject.toml` describes that imported package, not this extension release.

'''+readme[end:]
(ROOT/'README.md').write_text(readme)

guide=f'''# Repository guide for 0.4.0

**tentative authors list**

{author_text}

The current model lives under `extensions/lu177_psma/v0.4.0/`. The previous `v0.3.0/` directory is preserved for comparison and regression checks. The inherited `gdcdictionary/` and its Python packaging remain unchanged and are not the merged proposal.

{baseline}

The imported source parent is `bee947238381704486ccd12beeb8f4689fb22843`, a different revision. Its custom PT `mr_images` field and other differences need receiving-team reconciliation before integration.

## Current artifacts

- `schemas`, `integration/yaml`, `templates`, `tables` and `graph` are representations of the same 90-node dictionary.
- `review` contains the two radiopharmaceutical workbooks; `publication` contains the manuscript draft, supplement and submission notes.
- `mappings/radiopharmaceutical_source_crosswalk.json` and the revision log trace the new inputs. Source hashes and field extracts are under `sources/radiopharmaceutical_inputs`.
- `integration/v030_to_v040_additive_patch.json` upgrades the prior merged proposal. The baseline patch still starts from the exact deployed MIDRC snapshot.
- `scripts/validate_model.py` validates structure, profile rules, fixtures and both patches. Root `scripts/build_dictionary_docs.py --check` detects documentation drift.
- `scripts/v040/` records the schema and source-crosswalk generation procedure. Artifact authoring also requires the source Word drafts and the supported spreadsheet renderer; generated artifacts are distributed for direct review.

## Publication workflow

The GitHub Actions release workflow runs on the authorized `cdis` branch when VERSION changes. It validates the model and documentation, verifies checksums, builds downloads and publishes a development release. The title is `0.4.0` and the tag is `v0.4.0`. Existing tags are never moved. This workflow publishes files only; it does not deploy MIDRC, migrate a database or submit a manuscript to a journal.

Model, baseline dictionary, terminology/ontology, clinical criteria and dataset versions remain independent. A receiving deployment still needs a Gen3 build, ingestion/export round trip, vocabulary review and clinical/radiopharmacy review.
'''
(ROOT/'docs/REPOSITORY_GUIDE.md').write_text(guide)
(OUT/'README.md').write_text('# Lu177 PSMA model 0.4.0\n\n'+release[release.index('2 November'):]+ '\nSee the root README, review workbooks, publication drafts and integration guide. Templates mark required fields with `*`; remove markers and blank optionals before validation. Profile requirements remain additional to JSON Schema.\n')
integration=(OLD/'integration/MIDRC_Integration_Guide.md').read_text()
integration=integration.replace('Jazmin Schwartz, Tahir','Jazmin Schwartz, Nouran Zaid, Tahir')
(OUT/'integration/MIDRC_Integration_Guide.md').write_text('''# MIDRC integration guide for model 0.4.0

'''+baseline+'''

The dictionary has 90 nodes and 412 declared links. It preserves the 29-node deployed baseline and seven previously proposed enum appends. This revision adds 23 radiopharmaceutical/research nodes and optional extensions to six earlier nodes. No additional baseline required field or enum is changed.

## Integrating the radiopharmaceutical module

1. Confirm the receiving baseline. Do not apply a compiled patch blindly to a different source revision.
2. Review `radiopharmaceutical_module.json` for node grains and `../profiles/radiopharmaceutical_v040.json` for context requirements. Batch QC uses a nonpatient node; existing MIDRC measurement parent groups remain intact.
3. Apply `midrc_additive_patch.json` to the preserved baseline, or `v030_to_v040_additive_patch.json` to the exact previous merged proposal. Both patches are tested add-only transformations.
4. Retain legacy data without silently reclassifying a product-like record as an agent. Create explicit agent, product, ingredient, package and identifier records and document the mapping. Migrate ambiguous specific_activity only when denominator, chemical species, unit and time are known.
5. Build the receiving Gen3 dictionary, provision administrative nodes and ingest fixtures in `../submission_order.json`. Test forward/backref queries, authorization, file indexing, export and existing records in staging.
6. Approve clinical, radiopharmacy and ontology bindings before a production release. The local model is not a release-specification engine or a prescribing engine.

PT continues to mean PET; NM covers planar and SPECT, with the existing proposed NM subtype field. Clinical results and the outcome framework are retained. New identifiers are typed entity assignments; ontology axioms remain separately curated.

## Historical integration decisions retained from v0.3.0

The following material documents the original baseline reconciliation. Counts and revision labels in this historical section refer to v0.3.0; the current inventory and patches above govern 0.4.0.

'''+integration)
# Synchronize derived crosswalks, graph export and deltas, preserving richer old source metadata.
cross=read(OLD/'mappings/source_field_crosswalk.json')+read(OUT/'mappings/radiopharmaceutical_source_crosswalk.json');write(OUT/'mappings/source_field_crosswalk.json',cross)
def csvout(path,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in rows)
csvout(OUT/'mappings/source_field_crosswalk.csv',cross);csvout(OUT/'integration/node_delta.csv',read(OUT/'integration/node_delta.json'))
for name in ['radiopharmaceutical_source_crosswalk','radiopharmaceutical_revision_log']:csvout(OUT/'mappings'/f'{name}.csv',read(OUT/'mappings'/f'{name}.json'))
reuse=read(OLD/'mappings/midrc_property_reuse.json')
reuse += [dict(node='radiopharmaceutical_test',property=k,status='exact_baseline_property_definition_in_new_nonpatient_node',source_node='measurement',baseline_version='1.4.3-2-g7505333') for k in ['test_result_number','test_result_percent','test_result_ratio']];write(OUT/'mappings/midrc_property_reuse.json',reuse)
omop=read(OLD/'mappings/omop_domain_crosswalk.json')
for n in read(OUT/'integration/radiopharmaceutical_module.json')['new_nodes']:omop.append(dict(node=n,candidate_targets='External reference/provenance registry; any clinical projection requires context-specific ETL',status='conceptual_not_executable_etl',baseline_version='5.4',note='Do not create artificial PERSON or DRUG_EXPOSURE rows for products, batches, QC, preclinical results or computational predictions.'))
write(OUT/'mappings/omop_domain_crosswalk.json',omop)
g=read(OUT/'graph/model_graph.json');ns='http://graphml.graphdrawing.org/xmlns';ET.register_namespace('',ns);doc=ET.Element('{'+ns+'}graphml');key=ET.SubElement(doc,'{'+ns+'}key',{'id':'label','for':'all','attr.name':'label','attr.type':'string'});graph=ET.SubElement(doc,'{'+ns+'}graph',{'id':'lu177_psma_v040','edgedefault':'directed'})
for n in g['nodes']:el=ET.SubElement(graph,'{'+ns+'}node',{'id':n['id']});ET.SubElement(el,'{'+ns+'}data',{'key':'label'}).text=n['label']
for i,e in enumerate(g['edges']):el=ET.SubElement(graph,'{'+ns+'}edge',{'id':'e'+str(i),'source':e['source'],'target':e['target']});ET.SubElement(el,'{'+ns+'}data',{'key':'label'}).text=e['name']
ET.ElementTree(doc).write(OUT/'graph/model.graphml',encoding='utf-8',xml_declaration=True)
for name in ['document_check_previous_export.json','document_check.json','package_check.json','explorer_check.json']:
 p=OUT/'validation'/name
 if p.exists():p.unlink()
write(OUT/'documentation/repository_packaging.json',dict(packaging_date='2026-11-02',model_version='0.4.0-proposal',release='0.4.0',schema_changes_in_this_packaging=True,baseline=meta['pinned_compiled_dictionary'],authorship=authors,source_policy='Source field extracts preserve original coordinates and source-file SHA-256; unverified example values and suggested ontology codes are not populated as canonical data.'))
print('Current documentation and release metadata updated')
