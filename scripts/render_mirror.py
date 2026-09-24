"""Render one public distribution repo. Source content lives ONLY in skills/."""
import argparse, json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def render(skill, destination, revision):
    items = json.loads((ROOT / 'distribution/skills.json').read_text())
    item = next(x for x in items if x['skill'] == skill)
    source = ROOT / 'skills' / skill
    destination = Path(destination)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError('Render destination must be empty; render outside the git checkout first.')
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    shutil.copy2(ROOT / 'LICENSE', destination / 'LICENSE')
    skill_files = sorted(str(p.relative_to(source)) for p in source.rglob('*') if p.is_file())
    if skill == 'chestnut-copy':
        shutil.copytree(ROOT / 'distribution/templates/copy', destination, dirs_exist_ok=True)
        for target in ['chestnut-copy', 'plugins/chestnut/skills/chestnut-copy', 'plugins/chestnut-copy/skills/chestnut-copy']:
            shutil.copytree(source, destination / target)
        for manifest in (destination / 'plugins').glob('*/.*-plugin/plugin.json'):
            obj = json.loads(manifest.read_text())
            obj['version'] = '2.4.0+source.' + revision[:12]
            manifest.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    workflow = destination / '.github/workflows/release.yml'
    workflow.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / 'distribution/templates/mirror-release.yml', workflow)
    (destination / 'source.json').write_text(json.dumps({
        'repository': 'chestnutzoe/chestnut-skills', 'commit': revision,
        'path': 'skills/' + skill, 'skill': skill, 'files': skill_files,
    }, ensure_ascii=False, indent=2) + '\n')
    url = 'https://github.com/' + item['repo']
    origin = 'https://github.com/chestnutzoe/chestnut-skills'
    text = f'''# {item['label']}

独立 Skill：`{skill}`。本仓库可以单独下载、提 Issue、点 Star。

- [读取 Skill](SKILL.md)
- [下载完整 Skill ZIP]({url}/releases/latest/download/{skill}.zip)
- [全部 Chestnut Skills 与整包下载]({origin})

把 Skill 链接交给能读取 GitHub 的 AI，并说明要完成什么；需要安装时，下载完整 ZIP，解压后把 `{skill}` 文件夹放入所用工具的 skills 目录，保留参考资料与脚本。

## 唯一维护源

内容在 [总仓库的 skills/{skill}]({origin}/tree/main/skills/{skill}) 修改。本仓库由 GitHub Actions 自动发布，不手动维护第二份。修订请提交到总仓库；这里的 Issue 可以用来反馈此 Skill 的问题。

本次来源：[提交 {revision[:12]}]({origin}/commit/{revision})。对应文件清单见 [source.json](source.json)。
'''
    if skill == 'chestnut-copy':
        text += '''
## 旧用户兼容

原仓库地址、`chestnut@chestnut` 插件身份及 Copy 文件夹链接保留。更新后调用 `/chestnut:chestnut-copy`。独立插件入口 `chestnut-copy@chestnut` 同样保留，两者只安装一个。

Claude Code 首次安装：

```text
/plugin marketplace add https://github.com/chestnutzoe/chestnut-copy-skill
/plugin install chestnut@chestnut
```

Codex 首次安装：

```text
codex plugin marketplace add chestnutzoe/chestnut-copy-skill
codex plugin add chestnut@chestnut
```

旧名称与组合包迁移见 [MIGRATION.md](MIGRATION.md)。Copy 只负责文案。
'''
    (destination / 'README.md').write_text(text)
    (destination / 'AGENTS.md').write_text('Generated distribution repository. Do not edit Skill content here. The only source of truth is https://github.com/chestnutzoe/chestnut-skills/tree/main/skills/' + skill + '. Submit fixes to that source. This repository is published automatically.\n')
    (destination / '.gitignore').write_text('dist/\n.DS_Store\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('skill'); parser.add_argument('destination'); parser.add_argument('revision')
    args = parser.parse_args()
    render(args.skill, args.destination, args.revision)
