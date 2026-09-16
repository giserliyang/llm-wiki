# 个人学习 LLM Wiki（Obsidian Vault）

> 卡帕西三层架构 × 原子笔记 × Dataview 仪表盘  
> 前端：Obsidian ｜ 编译：LLM ｜ 监督：你

## 三层架构

```
raw/          原始素材层（只读，不改）
  tutorials/  教程原文
  videos/     视频字幕/文稿
  bookmarks/  网页书签/剪藏（含公众号等网页文章）
  images/     截图
  others/     零散素材

wiki/         结构化知识层（LLM 主导写入，人审核）
  overview.md
  glossary.md
  links.md
  concepts/   概念页
  entities/   实体页（人物/工具/产品）
  comparisons/ 对比分析
  decisions/  决策记录
  practice/   实战总结

notes/        个人原子笔记层（你亲手写，LLM 只可建议不可覆盖）
dashboards/   Dataview 仪表盘（只查不写）
templates/    模板
prompt/       LLM 提示词（ingest / lint）
diff/         待审核 diff
report/       校验报告
AGENTS.md     LLM 操作规则（强制）
```

## 两条工作流

### A. 读教程 / 剪文章（个人笔记主路径）

1. 把原文放进 `raw/` 对应目录，命名：`YYYYMMDD_主题_来源.md`
2. 用模板 `templates/tutorial-raw.md` 补 Frontmatter + 阅读进度清单
3. 用 Copy Outline 复制章节骨架 → 粘到「阅读进度」改成任务清单，标优先级
4. **真正卡住时**才建原子笔记 → `notes/`，用模板 `templates/atomic-note.md`
5. YAML 写 `source: "[[原文]]"`，正文写 `[[原文#章节]]`
6. 实战后才改 `understanding_level` / `need_practice` / `last_review`

### B. LLM 摄入（Wiki 编译路径）

1. 新素材进 `raw/`
2. 对 LLM 说（或用 `prompt/ingest.md`）：
   > 读 raw/xxx，按 AGENTS.md 更新 wiki/，生成 diff/ 待审，不要改 raw/ 和 notes/
3. 你在 Obsidian 审核 diff，通过后覆盖 wiki 页面
4. 优质问答结果可回写 wiki（查询 → 合成 → 回写）

## 原子笔记 Frontmatter 字段

| 字段 | 含义 |
| --- | --- |
| `status` | 未读 / 进行中 / 已理解 / 已归档 |
| `understanding_level` | 0未读 1见过 2能复述 3能默写 4能讲懂 5能改 |
| `need_practice` | 是否还要上机/实操 |
| `last_review` | 最后一次真正复习/使用日期 |
| `source` | 指向 raw 的双链 |
| `source_type` | tutorial / video / bookmark / wiki |
| `source_url` | 原始 URL（网页类） |

**原则：状态是行为的结果，不是阅读的产物。**

## 快速入口

- [[wiki/overview|Wiki 总览]]
- [[dashboards/学习仪表盘|学习仪表盘]]
- [[dashboards/素材收件箱|素材收件箱]]
- [[AGENTS|LLM 操作规则]]

## Obsidian 必做配置

1. 打开 Vault 根目录为本文件夹
2. 核心插件开启：大纲、反向链接、关系图谱、模板、快速切换
3. 设置 → 文件与链接 → 内部链接类型 → **基于当前笔记的路径**（或始终最短路径，保持一致）
4. 社区插件推荐：**Dataview**（仪表盘）、Copy Outline、Web Clipper、Templater（可选）
5. 如社区市场打不开：手动把 Dataview 的 `main.js`/`manifest.json`/`styles.css` 放到 `.obsidian/plugins/dataview/`
