import fs from 'node:fs/promises';
import path from 'node:path';
import { instance } from '@viz-js/viz';
import sharp from 'sharp';
import {fileURLToPath} from 'node:url';
const dir=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../extensions/lu177_psma/v0.4.0/graph');
const viz=await instance();
const views=JSON.parse(await fs.readFile(path.join(dir,'view_manifest.json'),'utf8'));
for(const v of views){const dot=await fs.readFile(path.join(dir,v.view+'.dot'),'utf8');const svg=viz.renderString(dot,{format:'svg'});await fs.writeFile(path.join(dir,v.view+'.svg'),svg);await sharp(Buffer.from(svg)).resize({width:2000}).png().toFile(path.join(dir,v.view+'.png'));}
console.log(JSON.stringify({svg_views:views.length}));
