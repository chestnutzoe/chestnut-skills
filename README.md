# Chestnut Skills · 栗子工具箱

每个 Skill 都能独立使用，也可以一次下载目前已收录的全部 Skills。

**[下载整套 ZIP](https://github.com/chestnutzoe/chestnut-skills/releases/latest/download/chestnut-skills.zip)**

## 独立使用与 Star

各 Skill 有独立仓库、调用链接、下载包和 Star。总仓库是唯一维护源，修改后由 GitHub Actions 自动更新各仓库和下载包。

| Skill | 用途 | 独立入口与 Star | 单独下载 |
| --- | --- | --- | --- |
| [chestnut-copy](https://github.com/chestnutzoe/chestnut-copy-skill/blob/main/SKILL.md) | Chestnut Copy | [独立仓库](https://github.com/chestnutzoe/chestnut-copy-skill) | [ZIP](https://github.com/chestnutzoe/chestnut-copy-skill/releases/latest/download/chestnut-copy.zip) |
| [chestnut-positioning-statement](https://github.com/chestnutzoe/chestnut-positioning-statement/blob/main/SKILL.md) | 一句话定位 | [独立仓库](https://github.com/chestnutzoe/chestnut-positioning-statement) | [ZIP](https://github.com/chestnutzoe/chestnut-positioning-statement/releases/latest/download/chestnut-positioning-statement.zip) |
| [chestnut-brand-guidance](https://github.com/chestnutzoe/chestnut-brand-guidance/blob/main/SKILL.md) | 品牌表达指南 | [独立仓库](https://github.com/chestnutzoe/chestnut-brand-guidance) | [ZIP](https://github.com/chestnutzoe/chestnut-brand-guidance/releases/latest/download/chestnut-brand-guidance.zip) |
| [chestnut-brand-story](https://github.com/chestnutzoe/chestnut-brand-story/blob/main/SKILL.md) | 个人品牌故事 | [独立仓库](https://github.com/chestnutzoe/chestnut-brand-story) | [ZIP](https://github.com/chestnutzoe/chestnut-brand-story/releases/latest/download/chestnut-brand-story.zip) |
| [chestnut-product-brief](https://github.com/chestnutzoe/chestnut-product-brief/blob/main/SKILL.md) | 产品说明书 | [独立仓库](https://github.com/chestnutzoe/chestnut-product-brief) | [ZIP](https://github.com/chestnutzoe/chestnut-product-brief/releases/latest/download/chestnut-product-brief.zip) |
| [chestnut-style-analyzer](https://github.com/chestnutzoe/chestnut-style-analyzer/blob/main/SKILL.md) | 文风分析 | [独立仓库](https://github.com/chestnutzoe/chestnut-style-analyzer) | [ZIP](https://github.com/chestnutzoe/chestnut-style-analyzer/releases/latest/download/chestnut-style-analyzer.zip) |

## 怎么用

- 单独使用：把表格中的 Skill 链接交给能读取 GitHub 的 AI，说明要完成什么。需要参考资料或脚本时，下载完整 ZIP。
- 安装：解压后把对应 `chestnut-*` 文件夹放入所用 AI 工具的 skills 目录；保留参考资料和脚本。
- 整套下载：整包包含同样的独立文件夹，不要求按顺序使用。已经装过的 Skill 不必重复安装。
- 原 Copy 仓库地址与兼容插件身份保留，详见 [Copy 迁移说明](https://github.com/chestnutzoe/chestnut-copy-skill/blob/main/MIGRATION.md)。

这里目前收录六个已公开的 Skills。尚未宣称覆盖云股东所有课程；课程覆盖、品牌合作与新版个人美学的接入另行核对，不以文件数量替代完整性验收。

## 只维护一处

**所有公开 Skill 内容只改本仓库 `skills/<skill-name>/`。** 包括 Copy，原 Copy 仓库已经变为自动生成的发布入口。

1. 修改对应 Skill 并合并到 `main`。
2. [Publish Chestnut Skills](https://github.com/chestnutzoe/chestnut-skills/actions/workflows/publish.yml) 自动生成单项 ZIP 和整包 ZIP，同时更新各独立仓库。
3. 独立仓库自动发布自己的 ZIP。来源提交记录在各仓库 `source.json`，可核对版本。

独立仓库的文件不手动编辑。修订/PR 提交到本仓库，Issue 可在对应独立仓库反馈。不从私人 Chestnut Skills 自动同步。

## 发布维护

- `distribution/skills.json`：Skill 与独立仓库的映射。
- `scripts/package.py`：生成所有单项包和整包。
- `scripts/render_mirror.py`：从唯一源文件生成独立仓库；Copy 的旧链接和插件结构按模板生成。
- `distribution/templates/`：发布模板，不保存第二份 Skill 内容。
- `python3 scripts/check_distribution.py`：校验独立仓库、ZIP 内容、Copy 兼容结构与来源记录。
- 自动化使用每个目标仓库各自的部署密钥。密钥仅存 GitHub Actions Secrets，不使用个人登录凭据。失败在 Actions 中可见，可重新运行失败任务或手动运行整个流程。
- 来源提交作为发布版本。只推送文档变更不会重复发包；Skill、打包脚本、发布模板或清单变化会触发自动发布。
