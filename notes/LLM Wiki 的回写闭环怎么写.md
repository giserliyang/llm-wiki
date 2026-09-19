---
title: "LLM Wiki 的回写闭环"
tags:
  - wiki
  - 知识管理
  - RAG
source: "[[raw/bookmarks/别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]"
source_type: bookmark
source_url: "https://developer.cloud.tencent.com/article/2680461?policyId=1004"
status: draft
understanding_level: 0
need_practice: "在 Obsidian 里实测一次查询→回写流程，记录耗时与痛点"
last_review: 2026-09-19
aliases: ["LLM Wiki 回写"]
---

# LLM Wiki 的回写闭环

## 我的理解

> 用你自己的话回答：「回写」解决的是 RAG 的什么短板？为什么它让 Wiki 「越用越完善」？

## 要点

1. 回写触发条件：什么算「优质结果」？是否所有查询都回写，还是只回写高复用结论？
2. 回写流程：查询 → LLM 提炼 → 生成 diff → 人审 → 回写 wiki 页面
3. 命名规范：`YYYYMMDD_页面名_diff.md`
4. 风险：回写内容若未经审核，可能固化错误（即「错误知识库」陷阱）

## 疑问

- 回写频率：每天/每周/按需？
- 回写范围：只写概念页，还是可以写决策/故障页？
- 与「原子笔记」的边界：回写到 wiki 的内容 vs 写进 notes 的内容如何区分？

## 待验证

- [ ] 用 Claude Code 在本地 vault 上跑一次真实回写，记录 5 个关键操作点
- [ ] 对比「直接问 RAG」与「回写后问 Wiki」的答案质量差异

## 实战记录

（留空，等你实测后填）

## 关联

- [[wiki/concepts/LLM-Wiki]]
- [[wiki/concepts/三层架构]]
- [[wiki/comparisons/LLM-Wiki-vs-RAG]]