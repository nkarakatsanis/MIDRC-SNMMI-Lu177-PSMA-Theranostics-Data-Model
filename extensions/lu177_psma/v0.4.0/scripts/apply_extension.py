"""Apply the additive proposal to its exact pinned baseline, locally only.
Usage: python scripts/apply_extension.py baseline.json output.json
"""
import json,sys,hashlib,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    src,dst=map(Path,sys.argv[1:]);manifest=json.loads((ROOT/'release_manifest.json').read_text())
    if hashlib.sha256(src.read_bytes()).hexdigest()!=manifest['midrc_baseline']['sha256']:raise SystemExit('Baseline bytes differ from the pinned snapshot. Rebase and review the changes; no output written.')
    d=json.loads(src.read_text())
    for op in json.loads((ROOT/'integration/midrc_additive_patch.json').read_text()):
        parts=op['path'].lstrip('/').split('/');p=d
        for k in parts[:-1]:p=p[int(k)] if isinstance(p,list) else p[k]
        if isinstance(p,list):
            if parts[-1]!='-':raise ValueError('Only append is expected for lists')
            p.append(copy.deepcopy(op['value']))
        else:p[parts[-1]]=copy.deepcopy(op['value'])
    dst.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
