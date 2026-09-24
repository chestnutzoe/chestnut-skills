from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib, json
root = Path(__file__).resolve().parents[1]
out = root / 'dist'
out.mkdir(exist_ok=True)
for stale in out.glob('*.zip'):
    stale.unlink()
paths = sorted((root / 'skills').iterdir())
assert len(paths) == 7
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
print('Built 7 standalone ZIPs and 1 complete ZIP.')
