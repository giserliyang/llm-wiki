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

# LLM Wiki vs RAG vs GraphRAG

## 摘要

三者并非互斥，而是**互补**关系：LLM Wiki 负责知识编译与沉淀，RAG 负责即时检索问答，GraphRAG 负责大规模实体关系推理。

## 对比表

| 维度 | LLM Wiki | 基础 RAG | GraphRAG（Microsoft） |
| --- | --- | --- | --- |
| **核心定位** | 人类可读的知识编译层，持续维护 | 查询时检索合成，即时响应 | 提取实体关系，强化关联检索 |
| **工作方式** | 提前编译，持续更新，人类审核 | 查询时检索 chunk，实时合成 | 提取实体/关系，构建图结构，检索关联 |
| **优势** | 知识可积累、可溯源、可读性强 | 灵活高效，适合实时查询 | 擅长大规模关系推理，关联更精准 |
| **劣势** | 需要维护，不适合实时高频更新 | 结论不积累，聊天记录易丢失 | 实现复杂，运维成本高 |
| **适用场景** | 个人学习、团队入职、故障复盘、决策记录 | 实时查询、临时检索、快速问答 | 大规模文档、复杂关系推理、企业级知识管理 |
| **体量阈值参考** | ≤100 页即可上手（Karpathy 实测 100 篇/40 万字） | 无门槛 | 500+ 页才值得投入 |

## 何时组合使用

1. **初期**：纯 LLM Wiki + Obsidian + Claude Code（Karpathy 个人用法）
2. **中期**：加上 qmd 做轻量全文检索
3. **后期**：Wiki 成熟后，对大体积或团队级知识库叠加 GraphRAG 做关系检索
4. **查询路径**：用户 → Claude Code 读 Wiki 直接回答（小体量），或走 RAG/GraphRAG 管道（大体量）

## 待验证

> [!question] 待补充
> - LLM Wiki 的「回写闭环」在实践中触发频率有多少？
> - GraphRAG 与本库 Schema 层的具体对接方式是否可行？
> - 是否需要为「回写结果」设定质量门禁（如 human-in-the-loop 阈值）？

## 引用来源

- [[raw/bookmarks/别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]] §"与RAG、GraphRAG的核心区别"
- Karpathy gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 关联页面

- [[wiki/concepts/LLM-Wiki]]
- [[wiki/concepts/三层架构]]
