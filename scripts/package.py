from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib, json
root = Path(__file__).resolve().parents[1]
out = root / 'dist'
out.mkdir(exist_ok=True)
for stale in out.glob('*.zip'):
    stale.unlink()
paths = sorted(p for p in (root / 'skills').iterdir() if p.is_dir())
registry = json.loads((root / 'distribution/skills.json').read_text())
assert {p.name for p in paths} == {entry['skill'] for entry in registry}
for name, selected in [(p.name, [p]) for p in paths] + [('chestnut-skills', paths)]:
    with ZipFile(out / (name + '.zip'), 'w', ZIP_DEFLATED) as archive:
        archive.write(root / 'LICENSE', 'LICENSE')
        for folder in selected:
            assert (folder / 'SKILL.md').is_file()
            for source in sorted(folder.rglob('*')):
                if source.is_file():
                    archive.write(source, source.relative_to(root / 'skills'))
checksums = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.glob('*.zip'))}
(out / 'checksums.json').write_text(json.dumps(checksums, indent=2) + '\n')
print(f'Built {len(paths)} standalone ZIPs and 1 complete ZIP.')
