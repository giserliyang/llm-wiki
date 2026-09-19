---
title: 2026-09-12 LLM Wiki Karpathy 书签摄入 diff
status: draft
kind: diff
tags:
  - wiki
  - ingest
source_count: 1
last_reviewed: 2026-09-19
---
# Diff：Karpathy LLM Wiki 书签摄入

> 本 diff 基于 [[raw/bookmarks/别再用RAG当"冤大头"！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]（2026-09-17 采集）。
> 请人审后再合并到 wiki/。禁止修改 raw/ 与 notes/。

---

## 1. 更新 `wiki/concepts/LLM-Wiki.md`

### 改动摘要

| 字段/章节 | 旧内容 | 新内容 |
| --- | --- | --- |
| `source_count` | 2 | 3 |
| `last_reviewed` | 2026-09-11 | 2026-09-19 |
| `related_wiki` | 原子笔记、三层架构 | + [[wiki/comparisons/LLM-Wiki-vs-RAG]] |
| 新增章节「与 RAG 的关系」 | 二列简表 | 三列对照表（含 GraphRAG），来源明确标注 |
| 新增章节「闭环：查询→回写」 | 无 | 描述 4 步回写流程与 diff 命名规范 |
| 新增章节「演进路线」 | 无 | 初期/中期/后期工具组合表格 |
| 新增「待补充/疑问」2 条 | 1 条 | 3 条 |

### 精确 diff（关键段落）

```diff
  source_count: 2
+ source_count: 3
  last_reviewed: 2026-09-11
+ last_reviewed: 2026-09-19
  related_wiki:
    - "[[wiki/concepts/原子笔记]]"
    - "[[wiki/concepts/三层架构]]"
+   - "[[wiki/comparisons/LLM-Wiki-vs-RAG]]"

  ### 它是什么
  3. **人机分工**：LLM 写入/链接/校验，人审核/升级/否决

+ ### 与 RAG 的关系（三栏对比）
+ > 来源：[[raw/bookmarks/...腾讯云.md]] §"与RAG、GraphRAG的核心区别"
+
+ | 维度 | LLM Wiki | 基础 RAG | GraphRAG（Microsoft） |
+ | --- | --- | --- | --- |
+ | 核心定位 | 人类可读的知识编译层，持续维护 | 查询时检索合成，即时响应 | 提取实体关系，强化关联检索 |
+ | 工作方式 | 提前编译，持续更新，人类审核 | 查询时检索 chunk，实时合成 | 提取实体/关系，构建图结构，检索关联 |
+ | 优势 | 知识可积累、可溯源、可读性强 | 灵活高效，适合实时查询 | 擅长大规模关系推理，关联更精准 |
+ | 劣势 | 需要维护，不适合实时高频更新场景 | 结论不积累，聊天记录易丢失 | 实现复杂，运维成本高 |
+ | 适用场景 | 个人学习、团队入职、故障复盘、决策记录 | 实时查询、临时检索、快速问答 | 大规模文档、复杂关系推理、企业级知识管理 |
+ | 体量阈值参考 | ≤100 页、单篇 300–800 字即可上手（Karpathy 实测） | 无门槛 | 500+ 页后才值得投入 |

+ ### 闭环：查询 → 回写
+ LLM Wiki 最核心的优势是「越用越完善」：
+ 1. 用自然语言在 Claude Code / Obsidian 中查询 Wiki
+ 2. 优质结果经 LLM 提炼后生成 diff
+ 3. 人类审核后回写到对应 wiki 页面
+ 4. 形成 **查询 → 合成 → 回写 → 优化** 的正循环
+
+ > [!note] 提示
+ > 回写时 diff 命名规范：`YYYYMMDD_页面名_diff.md`，以便版本回溯。
+
+ ### 演进路线（按 Wiki 体量）
+
+ | 阶段 | 规模 | 工具组合 |
+ | --- | --- | --- |
+ | 初期 | ≤100 页 | Obsidian + Markdown + Claude Code + Git |
+ | 中期 | 100–500 页 | 同上 + qmd（轻量搜索） |
+ | 后期 | 500+ 页 | 同上 + GraphRAG（关系检索） |

  ## 引用来源
  - 腾讯云文章《别再用RAG当"冤大头"！Karpathy的LLM Wiki》思路整理
  - Karpathy gist 理念（社区解读）
+ - [[raw/bookmarks/别再用RAG当"冤大头"！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]
  - Karpathy gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
```

---

## 2. 更新 `wiki/concepts/三层架构.md`

### 改动摘要

| 字段/章节 | 旧内容 | 新内容 |
| --- | --- | --- |
| `source_count` | 无 | 2 |
| `last_reviewed` | 无 | 2026-09-19 |
| Raw Sources 小节 | 仅 3 行列表 | 补全命名规范示例 + 目录树 |
| Wiki 小节 | 仅 3 行列表 | 补全标准目录结构 + 文件模板强制说明 |
| Schema 小节 | 仅 3 行列表 | 列出 ingest/lint 提示词 + 规则清单 |

### 精确 diff

```diff
  tags:
    - wiki
    - 知识管理
+ source_count: 2
+ last_reviewed: 2026-09-19

  ### 1. Raw Sources（原始素材层）
  - 教程、视频字幕、网页书签、截图
+ - 命名：`YYYYMMDD_主题_来源`（例：`20260912_LLMWiki_Karpathy_bookmark.md`）
  - **只读不改**，保证溯源
+ - 目录结构参考：
+
+ ```
+ raw/
+ ├── docs/          # 官方文档、论文
+ ├── prs/           # 代码 PR / 评审意见
+ ├── incidents/     # 故障复盘
+ ├── meetings/      # 会议记录
+ ├── images/        # 截图、架构图
+ └── others/        # 书签导出、零散素材
+ ```
+
+ > 来源：[[raw/bookmarks/...腾讯云.md]] §"Raw Sources 原始素材层：只读不改"

  ### 2. Wiki（结构化知识层）
  - 概念页 / 实体页 / 对比 / 决策 / 实战
  - LLM 写入，人审核
  - 统一 Frontmatter 模板
+ - 标准目录：
+
+ ```
+ wiki/
+ ├── overview.md    # 全局概览入口
+ ├── glossary.md    # 术语表
+ ├── concepts/      # 概念页
+ ├── entities/      # 人物/工具/产品页
+ ├── comparisons/   # 对比分析页
+ ├── decisions/     # 决策记录页
+ ├── incidents/     # 故障知识页
+ └── links.md       # 全局链接索引
+ ```
+
+ > [!note] 文件模板强制
+ > 每页须有 Frontmatter：`title / status / kind / tags / source_count / last_reviewed`；正文含摘要、核心内容、引用来源、关联页面、待补充/疑问五节。

  ### 3. Schema（规则层）
  - 根目录 `AGENTS.md`
  - 禁止改 raw/notes、无来源不写入、diff 审核流
+ - `prompt/ingest.md`：摄入提示词，指导 LLM 如何处理 raw/ 素材
+ - `prompt/lint.md`：校验提示词，定期自检 Wiki 规范性
+ - 关键规则：
+   - 禁止修改 raw/ 与 notes/
+   - 无来源不写入
+   - 不确定内容标记 `> [!question] 待补充`
+   - 禁止强制无关链接
+   - 重要修改必须产出 diff 等待人审
+   - 禁止删除，仅可标记「废弃」
+ - 可附加 `lint.md` 定义语法检查规则
```

---

## 3. 新建 `wiki/comparisons/LLM-Wiki-vs-RAG.md`

### 新建文件

路径：`wiki/comparisons/LLM-Wiki-vs-RAG.md`

```yaml
---
title: LLM Wiki vs RAG vs GraphRAG
status: draft
kind: comparison
tags:
  - wiki
  - 知识管理
  - RAG
source_count: 1
last_reviewed: 2026-09-19
---
```

正文：含三栏对比表、组合使用建议、3 条待验证问题。详见文件本体。

> [!caution] 人审注意
> 此页 `status: draft`，需人审后改为 `ready`。

---

## 4. 更新 `wiki/glossary.md`

### 精确 diff

```diff
  | LLM Wiki | LLM Wiki | 以 Markdown 为载体、LLM 为维护者、人类监督者的知识编译层 | [[wiki/concepts/LLM-Wiki]] |
  | 原子笔记 | Atomic Note | 只记一个想法、可被独立复用的笔记 | [[wiki/concepts/原子笔记]] |
  | MOC | Map of Content | 用一篇入口笔记导航一片主题 | |
  | Dataview | Dataview | 把笔记当数据库查询的 Obsidian 插件 | [[wiki/entities/Dataview]] |
  | Frontmatter | YAML Frontmatter | 文件头 `---` 区元数据，给工具检索用 | |
  | understanding_level | | 0–5 掌握度，行为结果不是阅读次数 | [[dashboards/学习仪表盘]] |
+ | RAG | Retrieval-Augmented Generation | 查询时临时检索素材并合成答案，结论不积累 | [[wiki/comparisons/LLM-Wiki-vs-RAG]] |
+ | GraphRAG | Graph-based RAG | Microsoft 提出的基于实体关系图的大规模知识检索方案 | [[wiki/comparisons/LLM-Wiki-vs-RAG]] |
```

---

## 5. 更新 `wiki/links.md`

### 精确 diff

```diff
  ### 知识管理
  - [[wiki/concepts/LLM-Wiki]]
  - [[wiki/concepts/原子笔记]]
  - [[wiki/concepts/三层架构]]
+ - [[wiki/comparisons/LLM-Wiki-vs-RAG]]
```

---

## 变更汇总

| 操作 | 文件路径 |
| --- | --- |
| 更新 | `wiki/concepts/LLM-Wiki.md` |
| 更新 | `wiki/concepts/三层架构.md` |
| 新建 | `wiki/comparisons/LLM-Wiki-vs-RAG.md`（draft） |
| 更新 | `wiki/glossary.md` |
| 更新 | `wiki/links.md` |
| — | `raw/` 与 `notes/` 未触碰 |

## 人审清单

1. 三列对比表是否需要调整列宽或补充 Row 来源？
2. 新 comparison 页 `status` 是否改为 `ready`？
3. 回写闭环与演进路线的描述是否准确？
4. glossary 新增的 RAG/GraphRAG 条目是否需要合并到 existing 概念页？
