from build_module import OUT,OLD,read
import json,re,html
from lxml import html as lh
source=(OLD/'NMMI_Model_Explorer.html').read_text()
data=json.loads(re.search(r'<script[^>]*id="modelData"[^>]*>(.*?)</script>',source,re.S).group(1))
stats=read(OUT/'inventory_summary.json');schemas={p.stem:read(p) for p in (OUT/'schemas').glob('*.json')}
data.update(schemas=schemas,templates={n:read(OUT/'templates'/f'submission_{n}_template.json') for n in schemas},graph=read(OUT/'graph/model_graph.json'),fields=read(OUT/'source_field_catalog.json'),views=read(OUT/'graph/view_manifest.json'),guide=read(OUT/'examples/patient_journey_guide.json'),records=read(OUT/'examples/full_patient_journey.json'),authorship=read(OUT/'AUTHORS.json'),stats=stats,metadata={x['id']:x for x in read(OUT/'node_catalog.json')},propertyrows=read(OUT/'tables/node_property_catalog.json'),delta=read(OUT/'integration/node_delta.json'),manifest=read(OUT/'release_manifest.json'),checks=read(OUT/'validation/validation_report.json'),revisions=read(OUT/'mappings/radiopharmaceutical_revision_log.json'),rp_profiles=read(OUT/'profiles/radiopharmaceutical_v040.json'))
data['svgs']={v['view']:(OUT/'graph'/(v['view']+'.svg')).read_text() for v in data['views']}
doc=lh.fromstring(source)
scripts=doc.xpath('//script');app=next(s for s in scripts if "const D=JSON.parse" in (s.text or ''))
script=app.text
script=script.replace("'outcomes','integration','about'","'outcomes','radiopharm','integration','about'")
script=script.replace("(set==='earlier'&&!f.source_element_id.startsWith('outcome_revision:')&&!f.source_element_id.startsWith('outcomes_paper:'))", "(set==='radiopharm'&&/^(nz_model|nk_blueprint|idrp_ontology):/.test(f.source_element_id))||(set==='earlier'&&!/^(outcome_revision|outcomes_paper|nz_model|nk_blueprint|idrp_ontology):/.test(f.source_element_id))")
app.text=script
doc.xpath('//script[@id="modelData"]')[0].text=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
doc.xpath('//title')[0].text='Lu177 PSMA Model Explorer | 0.4.0'
head=doc.xpath('//header')[0]
for c in list(head):head.remove(c)
head.text=None
header=f'''<div><p class="muted">DEVELOPMENT RELEASE 0.4.0 · 2 NOVEMBER 2026</p><h1>Lu177 PSMA Theranostics Data Model</h1><p>Radiopharmaceutical identity, preparation, quality, administration and research evidence</p><p><b>tentative authors list</b><br>{html.escape(', '.join(data['authorship']['authors']))}</p><p><b>90 nodes · {stats['edge_count']} relationships · 29 MIDRC baseline nodes + 61 proposed extension nodes</b></p><p>Additive technical proposal against MIDRC 1.4.3-2-g7505333. The original 29 nodes and their property definitions remain, with the seven enum additions proposed in v0.3.0. The catalog traces 1,371 source occurrences, including 450 radiopharmaceutical entries; these are not 1,371 distinct approved concepts.</p></div>'''
head.append(lh.fromstring(header))
prov=lh.fromstring('<section id="releaseProvenance"></section>')
head.addnext(prov)
for c in list(prov):prov.remove(c)
prov.text=None
prov.append(lh.fromstring('''<div><h2>Release and MIDRC baseline provenance</h2><p>Lu177-PSMA theranostics data model release 0.4.0 extends the deployed MIDRC Gen3 dictionary version <code>1.4.3-2-g7505333</code>, commit <code>7505333d56c87a289463a814131e38d0f2be6674</code>, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.</p><p>Model schema revision <b>0.4.0-proposal</b> resides under <code>extensions/lu177_psma/v0.4.0/</code>. Release 0.3.2 was a documentation patch over the 0.3.0 schema. Version 0.4.0 adds 23 nodes, optional fields and links, traceable radiopharmaceutical revisions and three new worked use cases. Historical tags and files remain unchanged.</p><p>Baseline SHA-256: <code>578e57dc45f719b07f1ac31482fed9129675c133aaafc3004dc346e5e4928e21</code>. The retained upstream <code>gdcdictionary/</code> tree is a different source revision; it requires reconciliation in a receiving Gen3 build.</p><a href="https://github.com/nkarakatsanis/MIDRC-SNMMI-Lu177-PSMA-Theranostics-Data-Model/releases/tag/v0.4.0">Repository release 0.4.0</a></div>'''))
nav=doc.xpath('//nav')[0];nav.append(lh.fromstring('<button data-tab="radiopharm">Radiopharmaceutical revision</button>'))
panel=lh.fromstring('<section id="radiopharmPanel" hidden="hidden"><h2>Radiopharmaceutical revision</h2><p>The three supplied drafts are reconciled at the record-identity level. Product specifications, batch evidence and actual administrations remain separate. Individual human observations reuse the existing clinical model; preclinical evidence and computational predictions have explicit research contexts.</p></section>')
for v in data['rp_profiles']['profiles']:
 panel.append(lh.fromstring('<article class="step"><h3>'+html.escape(v['name'].replace('_',' ').title())+'</h3><p>'+html.escape(v['scope'])+'</p><p>'+html.escape(v['requirements'])+'</p><p class="muted">'+html.escape(v['not_required'])+'</p></article>'))
table='<div class="scroll"><table><thead><tr><th>Revision</th><th>Issue and change</th><th>Rationale</th></tr></thead><tbody>'
for r in data['revisions']:table+='<tr><td>'+html.escape(r['revision_id']+' · '+r['title'])+'</td><td>'+html.escape(r['source_issue']+' '+r['proposed_revision'])+'</td><td>'+html.escape(r['rationale'])+'</td></tr>'
panel.append(lh.fromstring(table+'</tbody></table></div>'))
panel.append(lh.fromstring('<p>Use the Source field crosswalk tab and select “450 radiopharmaceutical source entries” to inspect each source row. NucLex bindings remain pending. Source example codes, dosing ranges and vendor prices have not been imported as validated defaults.</p>'))
doc.xpath('//*[@id="aboutPanel"]')[0].addprevious(panel)
doc.xpath('//*[@id="sourceSet"]')[0].append(lh.fromstring('<option value="radiopharm">450 radiopharmaceutical source entries</option>'))
# Replace only static text nodes; embedded schema history and source provenance are not globally rewritten.
substitutions={'all 67 nodes and 293 edges':'all 90 nodes and 412 edges','all 67 schemas':'all 90 schemas','122 connected synthetic records':'153 connected synthetic records','27 negative cases':'49 negative cases','There are 38 proposed theranostics nodes.':'There are 61 proposed extension nodes, including 23 added in v0.4.0.','all 67 are required':'all 90 are required','Model revision 0.3.0':'Model revision 0.4.0'}
for el in doc.iter():
 if el.tag in ['script','style']:continue
 for attr in ['text','tail']:
  t=getattr(el,attr)
  if t:
   for a,b in substitutions.items():t=t.replace(a,b)
   setattr(el,attr,t)
about=doc.xpath('//*[@id="aboutPanel"]')[0]
about.append(lh.fromstring('<h3>A radiopharmaceutical example across the layers</h3>'))
about.append(lh.fromstring('<p><b>Model:</b> a unit references its batch; a QC test references that batch; dispensing links the unit and prescription to the patient; administration records what was delivered. <b>Dictionary:</b> molar activity is activity per amount of a specified compound at a reference time, with a numerical value and unit. <b>Terminology:</b> a reviewed identifier names the quantity or substance and records its coding-system release. <b>Ontology:</b> NucLex may define the conceptual relations among substances, processes and measurements. Those conceptual assertions do not supply a missing lot, timestamp or patient link. An NDC package identifier and an RxNorm ingredient identifier describe different levels even when they relate to the same therapy.</p>'))
result='<!DOCTYPE html>\n'+lh.tostring(doc,encoding='unicode',method='html')
(OUT/'NMMI_Model_Explorer.html').write_text(result)
print('Built offline HTML explorer with '+str(len(schemas))+' nodes and '+str(len(data['views']))+' views')
