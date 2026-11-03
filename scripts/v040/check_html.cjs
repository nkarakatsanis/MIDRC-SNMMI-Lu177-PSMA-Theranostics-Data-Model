const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'../..');
fs.mkdirSync(root+'/dist_work',{recursive:true});
const errors=[],downloads=[];const vc=new VirtualConsole();vc.on('jsdomError',e=>{if(!e.message.includes('navigation'))errors.push(e.message)});
const dom=new JSDOM(fs.readFileSync(root+'/extensions/lu177_psma/v0.4.0/NMMI_Model_Explorer.html','utf8'),{runScripts:'dangerously',virtualConsole:vc,beforeParse(w){w.URL.createObjectURL=()=> 'blob:test';w.URL.revokeObjectURL=()=>{};w.HTMLElement.prototype.scrollIntoView=()=>{};w.HTMLAnchorElement.prototype.click=function(){downloads.push(this.download)}}});
const w=dom.window,d=w.document;const click=s=>{const e=d.querySelector(s);if(!e)throw Error('Missing '+s);e.click()};
const change=(id,val)=>{d.getElementById(id).value=val;d.getElementById(id).dispatchEvent(new w.Event('change'))};
const checks={nodes:d.querySelectorAll('#nodeList button').length,views:d.querySelectorAll('#viewSelect option').length};
for(const t of ['graph','table','source','journey','usecases','outcomes','radiopharm','integration','about']){click(`nav button[data-tab="${t}"]`);if(d.getElementById(t+'Panel').hidden)throw Error('Hidden selected panel '+t)}
change('viewSelect','radiopharmaceutical_trace');checks.rp_graph_nodes=d.querySelectorAll('#graphInner .node').length;
change('sourceSet','radiopharm');checks.source_count=d.getElementById('sourceCount').textContent;
change('useCaseSelect','prediction_trace');click('[data-record="RP-PREDICTION"]');checks.prediction_opened=d.getElementById('recordJson').textContent.includes('RP-PREDICTION');click('#recordSchema');click('#schemaDownload');click('#templateDownload');checks.downloads=downloads;
checks.errors=errors;
if(checks.nodes!==90||checks.views!==12||checks.rp_graph_nodes!==12||!checks.source_count.includes('450')||!checks.prediction_opened||downloads.length!==2||errors.length)throw Error(JSON.stringify(checks));
fs.writeFileSync(root+'/dist_work/explorer_dom_check.json',JSON.stringify(checks,null,2));console.log(JSON.stringify(checks));dom.window.close();
