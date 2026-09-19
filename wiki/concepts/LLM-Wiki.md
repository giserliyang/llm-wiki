---
title: LLM Wiki
status: ready
kind: concept
tags:
  - wiki
  - 知识管理
source_count: 3
last_reviewed: 2026-09-19
related_wiki:
  - "[[wiki/concepts/原子笔记]]"
  - "[[wiki/concepts/三层架构]]"
  - "[[wiki/comparisons/LLM-Wiki-vs-RAG]]"
---

# LLM Wiki

## 摘要

LLM Wiki 是「知识编译层」：把零散素材提前整理成结构化、可溯源、可互链的 Markdown Wiki，由 LLM 持续维护、人类审核；与「查询时临时检索合成」的 RAG 互补，而非替代。

## 核心内容

### 它不是什么

- 不是聊天记录堆积
- 不是让 LLM 自由发挥的黑盒摘要
- 不是取代人工原子笔记
- 不是 RAG 的替代品，而是 RAG 的前置知识编译层

### 它是什么

1. **提前编译**：读一次素材，多次复用结论
2. **三层结构**：`raw/` 只读 → `wiki/` 编译 → Schema（[[wiki/concepts/三层架构|AGENTS.md]]）约束
3. **人机分工**：LLM 写入/链接/校验，人审核/升级/否决

### 与 RAG 的关系（三栏对比）

> 来源：[[raw/bookmarks/别再用RAG当"冤大头"！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]] §"与RAG、GraphRAG的核心区别"

| 维度 | LLM Wiki | 基础 RAG | GraphRAG（Microsoft） |
| --- | --- | --- | --- |
| **核心定位** | 人类可读的知识编译层，持续维护 | 查询时检索合成，即时响应 | 提取实体关系，强化关联检索 |
| **工作方式** | 提前编译，持续更新，人类审核 | 查询时检索 chunk，实时合成 | 提取实体/关系，构建图结构，检索关联 |
| **优势** | 知识可积累、可溯源、可读性强 | 灵活高效，适合实时查询 | 擅长大规模关系推理，关联更精准 |
| **劣势** | 需要维护，不适合实时高频更新场景 | 结论不积累，聊天记录易丢失 | 实现复杂，运维成本高 |
| **适用场景** | 个人学习、团队入职、故障复盘、决策记录 | 实时查询、临时检索、快速问答 | 大规模文档、复杂关系推理、企业级知识管理 |
| **体量阈值参考** | ≤100 页、单篇 300–800 字即可上手（Karpathy 实测） | 无门槛 | 500+ 页后才值得投入 |

### 闭环：查询 → 回写

LLM Wiki 最核心的优势是「越用越完善」：

1. 用自然语言在 Claude Code / Obsidian 中查询 Wiki
2. 优质结果经 LLM 提炼后生成 diff
3. 人类审核后回写到对应 wiki 页面
4. 形成 **查询 → 合成 → 回写 → 优化** 的正循环

> [!note] 提示
> 回写时 diff 命名规范：`YYYYMMDD_页面名_diff.md`，以便版本回溯。
> 来源：同上书签文章 §"结果回写：让知识持续积累"

### 演进路线（按 Wiki 体量）

| 阶段 | 规模 | 工具组合 |
| --- | --- | --- |
| 初期 | ≤100 页 | Obsidian + Markdown + Claude Code + Git |
| 中期 | 100–500 页 | 同上 + qmd（轻量搜索） |
| 后期 | 500+ 页 | 同上 + GraphRAG（关系检索） |

> [!question] 待补充
> - GraphRAG 与本库 AGENTS.md Schema 层如何具体对接，待工程验证
> - 与个人原子笔记（`notes/`）的接口约定未明确定义

## 引用来源

- [[raw/bookmarks/别再用RAG当"冤大头"！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]
- Karpathy gist 理念（https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f）

## 关联页面

- [[wiki/concepts/三层架构]]
- [[wiki/concepts/原子笔记]]
- [[wiki/comparisons/LLM-Wiki-vs-RAG]]
- [[wiki/overview]]
