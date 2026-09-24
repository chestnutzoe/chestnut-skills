"""Validate packaging and generated distribution without network access."""
import hashlib, json, subprocess, sys, tempfile, zipfile
from pathlib import Path
from render_mirror import ROOT, render

items = json.loads((ROOT / 'distribution/skills.json').read_text())
assert len({i['repo'] for i in items}) == len(items)
assert len({i['skill'] for i in items}) == len(items)
revision = 'a' * 40
subprocess.run([sys.executable, str(ROOT / 'scripts/package.py')], check=True)
with tempfile.TemporaryDirectory() as temp:
    for item in items:
        name = item['skill']
        source = ROOT / 'skills' / name
        assert f'name: {name}\n' in (source / 'SKILL.md').read_text()
        dest = Path(temp) / name
        render(name, dest, revision)
        metadata = json.loads((dest / 'source.json').read_text())
        assert metadata['commit'] == revision
        for file in metadata['files']:
            assert not (source / file).is_symlink()
            assert (source / file).read_bytes() == (dest / file).read_bytes()
        with zipfile.ZipFile(ROOT / 'dist' / (name + '.zip')) as z:
            assert z.testzip() is None
            assert set(z.namelist()) == {'LICENSE'} | {name + '/' + f for f in metadata['files']}
            for file in metadata['files']:
                assert z.read(name + '/' + file) == (source / file).read_bytes()
        if name == 'chestnut-copy':
            for folder in ['chestnut-copy', 'plugins/chestnut/skills/chestnut-copy', 'plugins/chestnut-copy/skills/chestnut-copy']:
                for file in metadata['files']:
                    assert (dest / folder / file).read_bytes() == (source / file).read_bytes()
        try:
            render(name, dest, revision)
        except ValueError:
            pass
        else:
            raise AssertionError('Non-empty render destination must be rejected.')
with zipfile.ZipFile(ROOT / 'dist/chestnut-skills.zip') as z:
    assert z.testzip() is None
    assert {p.split('/')[0] for p in z.namelist() if p.endswith('/SKILL.md')} == {i['skill'] for i in items}
for name, digest in json.loads((ROOT / 'dist/checksums.json').read_text()).items():
    assert hashlib.sha256((ROOT / 'dist' / name).read_bytes()).hexdigest() == digest
print('PASS: all standalone mirrors, Copy compatibility paths, ZIPs and provenance match the single source.')
