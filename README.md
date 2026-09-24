# Chestnut Skills · 栗子工具箱

每个 Skill 都可以单独下载、独立使用。想一次下载全部，直接拿整包；不要求按顺序使用。

**[下载全部七个 Skills](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-skills.zip)**

## 按需下载

| Skill | 用途 | 下载 |
| --- | --- | --- |
| [chestnut-brand-story](skills/chestnut-brand-story/SKILL.md) | 个人品牌故事 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-brand-story.zip) |
| [chestnut-positioning-statement](skills/chestnut-positioning-statement/SKILL.md) | 一句话定位 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-positioning-statement.zip) |
| [chestnut-brand-guidance](skills/chestnut-brand-guidance/SKILL.md) | 品牌表达指南 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-brand-guidance.zip) |
| [chestnut-product-brief](skills/chestnut-product-brief/SKILL.md) | 产品说明书 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-product-brief.zip) |
| [chestnut-style-analyzer](skills/chestnut-style-analyzer/SKILL.md) | 文风分析 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-style-analyzer.zip) |
| [chestnut-copy](skills/chestnut-copy/SKILL.md) | 文案工作流 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-copy.zip) |
| [chestnut-wechat-publisher](skills/chestnut-wechat-publisher/SKILL.md) | 公众号草稿发布 | [单独 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-wechat-publisher.zip) |

## 怎么用

解压后，每个 `chestnut-*` 文件夹都是一个完整 Skill，里面包含 `SKILL.md` 和它需要的参考资料或脚本。将你需要的文件夹放入所用 AI 工具的 skills 目录即可；整包只是把这七个独立文件夹放在一起。

也可以把表格里的 Skill 链接发给支持读取 GitHub 的 AI，明确说要用它完成什么。涉及脚本或参考文件时，请下载完整的单项 ZIP，不要只复制 SKILL.md。

已经安装 Copy 时，不必重复安装 `chestnut-copy`；文风分析和公众号发布现在也是独立 Skill，按需单独下载。

## 已经在用 Copy Skill？

原来的 [chestnut-copy-skill](https://github.com/chestnutzoe/chestnut-copy-skill) 地址从 2.3.0 起只提供 Copy 文案 Skill，原插件身份保留。文风分析与公众号发布已迁入本仓库，独立维护和下载。

旧版组合包用户请看 [迁移说明](https://github.com/chestnutzoe/chestnut-copy-skill/blob/main/MIGRATION.md)。更新 Copy 前，先单独下载你还需要的其他工具。

## 维护与发布

- 六个非 Copy 工具（包括文风分析、公众号发布）的公开维护源是本仓库 `skills/` 下的对应目录。
- 只有 `chestnut-copy` 的公开维护源仍在旧 Copy 仓库。本仓库保留明确版本的发行副本，只有发布时才有意更新；不与私人工作 Skills 同步。
- 文风分析和公众号发布迁入时的内容来源：`chestnut-copy-skill` 提交 `092e0af861c911b96aed147b8512ab75ca7b0aa9`。四个品牌工具也由该版本迁入。Copy 发行副本更新至 2.3.1，Skill 正式名称为 `chestnut-copy`（Chestnut Copy）；两个伴随工具为可选独立下载。
- 运行 `python3 scripts/package.py` 生成七个单项 ZIP、整包 ZIP 和 SHA-256 校验记录；上传到 GitHub Release。
- 这个仓库提供独立 Skills 下载，不复用旧仓库的 `chestnut` marketplace 或插件身份。
