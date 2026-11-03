import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile,Workbook} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const model=root+'/extensions/lu177_psma/v0.4.0';
const out=process.env.LU177_ARTIFACT_OUTPUT||root+'/dist_work';
const qa=process.env.LU177_QA_OUTPUT||root+'/dist_work/qa';
await fs.mkdir(out,{recursive:true});await fs.mkdir(qa,{recursive:true});
const books=[['radiopharmaceutical_workbook_content.json','Radiopharmaceutical_Data_Model_v0.4.0.xlsx'],['radiopharmaceutical_revision_workbook_content.json','Radiopharmaceutical_Revisions_and_Rationale_v0.4.0.xlsx']];
const letter=i=>{let s='';while(i>0){i--;s=String.fromCharCode(65+i%26)+s;i=Math.floor(i/26);}return s;};
for (const [src,name] of books){
 const sheets=JSON.parse(await fs.readFile(model+'/documentation/'+src,'utf8'));const wb=Workbook.create();
 for(const data of sheets){
  const sh=wb.worksheets.add(data.name);sh.showGridLines=false;sh.tabColor='#205873';
  const matrix=[data.headers,...data.rows].map(row=>row.map(v=>typeof v==='string'&&v.startsWith('=')?"'"+v:v));
  const range=sh.getRange(`A1:${letter(data.headers.length)}${matrix.length}`);range.values=matrix;
  range.format.font={name:'Aptos',size:11,color:'#172E3C'};range.format.wrapText=true;range.format.verticalAlignment='top';
  range.format.borders={insideHorizontal:{style:'thin',color:'#DDE5EA'}};
  const head=sh.getRange(`A1:${letter(data.headers.length)}1`);head.format.fill='#173F57';head.format.font={name:'Aptos',size:11,bold:true,color:'#FFFFFF'};head.format.rowHeight=34;
  data.widths.forEach((width,c)=>sh.getRange(`${letter(c+1)}1:${letter(c+1)}${matrix.length}`).format.columnWidth=width);
  for(let r=1;r<matrix.length;r++){
   const row=sh.getRange(`A${r+1}:${letter(data.headers.length)}${r+1}`);
   row.format.fill=r%2?'#F0F5F8':'#FFFFFF';
   const lines=Math.max(...matrix[r].map((v,i)=>String(v??'').split('\n').reduce((sum,s)=>sum+Math.max(1,Math.ceil(s.length/Math.max(10,data.widths[i]*0.93))),0)));
   row.format.rowHeight=Math.max(34,Math.min(220,lines*15+12));
  }
  sh.freezePanes.freezeRows(1);sh.freezePanes.freezeColumns(data.name==='Read me'?1:2);
  sh.tables.add(`A1:${letter(data.headers.length)}${matrix.length}`,true,`${name.startsWith('Radiopharmaceutical_Data')?'Model':'Review'}_${data.name.replace(/[^a-z0-9]/gi,'_')}`);
  // Codes and all scientific source labels stay text; no numerical inference is applied to identifiers.
  if(data.name.includes('crosswalk')||data.name.includes('review')||data.name==='Sources')range.setNumberFormat('@');
 }
 wb.recalculate();
 console.log((await wb.inspect({kind:'workbook,sheet',maxChars:2200,tableMaxRows:2,tableMaxCols:3})).ndjson);
 for(const data of sheets){
  const endRow=Math.min(7,data.rows.length+1),endCol=letter(Math.min(data.headers.length,5));
  const image=await wb.render({sheetName:data.name,range:`A1:${endCol}${endRow}`,scale:1,format:'png'});
  await fs.writeFile(qa+'/'+name.replace('.xlsx','')+'_'+data.name.replaceAll(' ','_')+'.png',new Uint8Array(await image.arrayBuffer()));
 }
 await (await SpreadsheetFile.exportXlsx(wb)).save(out+'/'+name);
 console.log('Saved '+name);
}
