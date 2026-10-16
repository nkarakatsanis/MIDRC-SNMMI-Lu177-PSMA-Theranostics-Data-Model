"""Build release downloads from this checkout; no upload or network access.

Usage: python scripts/build_release_assets.py --output dist
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    version = (ROOT / 'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise SystemExit('VERSION must be a numeric major.minor.patch release.')
    metadata = json.loads((ROOT / 'release.json').read_text())
    if metadata['release_version'] != version or metadata['git_tag'] != 'v' + version:
        raise SystemExit('Release metadata does not match VERSION.')
    if not (ROOT / 'releases' / (version + '.md')).is_file():
        raise SystemExit('Missing release notes for ' + version)
    subprocess.run([sys.executable, str(ROOT / 'scripts/build_dictionary_docs.py'), '--check'], check=True)
    model = ROOT / metadata['model_directory']
    for line in (model / 'SHA256SUMS.txt').read_text().splitlines():
        expected, name = line.split('  ', 1)
        path = model / name
        if not path.resolve().is_relative_to(model.resolve()) or digest(path) != expected:
            raise SystemExit('Model checksum mismatch: ' + name)
    output = args.output.resolve()
    if output == ROOT or output.is_relative_to(model.resolve()):
        raise SystemExit('Choose a separate output directory.')
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise SystemExit('Output directory must be empty; existing assets will not be overwritten.')

    filenames = [
        ('NMMI_Model_Explorer.html', f'NMMI_Model_Explorer_v{version}.html'),
        ('NMMI_Lu177_PSMA_Architecture_and_Status.docx',
         f'NMMI_Lu177_PSMA_Architecture_and_Status_v{version}.docx'),
    ]
    for source, destination in filenames:
        shutil.copyfile(model / source, output / destination)
    archive = output / f'SNMMI_MIDRC_Lu177_PSMA_Model_{version}.zip'
    paths = []
    for dirname in ['extensions', 'docs', 'releases', 'scripts', 'gdcdictionary', '.github']:
        paths.extend(p for p in (ROOT / dirname).rglob('*') if p.is_file()
                     and '__pycache__' not in p.parts and p.suffix != '.pyc')
    paths.extend(ROOT / name for name in ['README.md', 'VERSION', 'release.json',
                  'CHANGELOG_LU177_PSMA.md', 'LICENSE', 'NOTICE', 'pyproject.toml', 'poetry.lock', '.gitignore'])
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in sorted(set(paths)):
            # Fixed archive metadata makes the same committed files reproducible.
            info = zipfile.ZipInfo(str(path.relative_to(ROOT)), (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    assets = sorted(p for p in output.iterdir() if p.is_file())
    (output / 'SHA256SUMS.txt').write_text(''.join(digest(p) + '  ' + p.name + '\n' for p in assets))
    print(json.dumps({'release_version': version, 'assets': [p.name for p in assets] + ['SHA256SUMS.txt']}, indent=2))

if __name__ == '__main__':
    main()
