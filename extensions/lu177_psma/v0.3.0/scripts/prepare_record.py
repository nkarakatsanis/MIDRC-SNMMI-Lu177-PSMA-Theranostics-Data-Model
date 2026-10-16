"""Clean a filled portal template. No submission or file registration is performed.
Usage: python scripts/prepare_record.py input.json output.json
Required fields and relationship groups must still be validated after cleanup.
"""
import json,sys
from pathlib import Path
def clean(value):
    if isinstance(value,dict):
        result={}
        for key,v in value.items():
            v=clean(v)
            if v is not None and v!={} and v!=[]:result[key.lstrip('*')]=v
        return result
    if isinstance(value,list):return [clean(v) for v in value if v is not None]
    return value
if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    src,dst=map(Path,sys.argv[1:]);dst.write_text(json.dumps(clean(json.loads(src.read_text())),indent=2)+'\n')
