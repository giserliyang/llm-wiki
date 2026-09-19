---
title: "RAG vs LLM Wiki vs GraphRAG 选型决策"
tags:
  - wiki
  - 知识管理
  - RAG
source: "[[raw/bookmarks/别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]"
source_type: bookmark
source_url: "https://developer.cloud.tencent.com/article/2680461?policyId=1004"
status: draft
understanding_level: 0
need_practice: "在自己的 vault 上评估当前规模，并写下选型结论"
last_review: 2026-09-19
aliases: ["RAG 选型"]
---

# RAG vs LLM Wiki vs GraphRAG 选型决策

## 我的理解

> 用自己的话回答：「三者是替代还是互补」？你目前处于哪个阶段？

## 要点

1. 三者在定位上的本质差异（见 comparison 页三栏表）
2. 体量阈值参考：
   - ≤100 页：LLM Wiki + Obsidian + Claude Code
   - 100–500 页：+ qmd
   - 500+ 页：+ GraphRAG
3. 组合使用路径：小体量先用 Wiki 沉淀，再按需叠加 RAG/GraphRAG

## 疑问

- 「100 页」是页数还是 token 数？单篇字数是否影响阈值？
- GraphRAG 落地需要哪些基础设施？Microsoft 官方实现 vs LlamaIndex/LangChain 各有什么取舍？
- 是否需要为「从 Wiki 过渡到 RAG」设定迁移 checklist？

## 待验证

- [ ] 统计当前 wiki/ 目录下 Markdown 页面数与总字数，定位所处阶段
- [ ] 查阅 GraphRAG 官方文档，评估落地成本（时间/算力/运维）

## 关联

- [[wiki/comparisons/LLM-Wiki-vs-RAG]]
- [[wiki/concepts/LLM-Wiki]]
