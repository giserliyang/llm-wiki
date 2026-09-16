---
title: LLM Wiki
status: ready
kind: concept
tags:
  - wiki
  - 知识管理
source_count: 2
last_reviewed: 2026-09-11
related_wiki:
  - "[[wiki/concepts/原子笔记]]"
  - "[[wiki/concepts/三层架构]]"
---

# LLM Wiki

## 摘要

LLM Wiki 是「知识编译层」：把零散素材提前整理成结构化、可溯源、可互链的 Markdown Wiki，由 LLM 持续维护、人类审核；与「查询时临时检索合成」的 RAG 互补。

## 核心内容

### 它不是什么

- 不是聊天记录堆积
- 不是让 LLM 自由发挥的黑盒摘要
- 不是取代人工原子笔记

### 它是什么

1. **提前编译**：读一次素材，多次复用结论
2. **三层结构**：`raw/` 只读 → `wiki/` 编译 → Schema（[[wiki/concepts/三层架构|AGENTS.md]]）约束
3. **人机分工**：LLM 写入/链接/校验，人审核/升级/否决

### 与 RAG 的关系

| | LLM Wiki | RAG |
| --- | --- | --- |
| 时机 | 提前编译，持续更新 | 查询时检索合成 |
| 产出 | 可积累的人类可读页面 | 单次答案 |
| 适合 | 学习、入职、决策沉淀 | 临时问答 |

## 引用来源

- 腾讯云文章《别再用RAG当"冤大头"！Karpathy的LLM Wiki》思路整理
- Karpathy gist 理念（社区解读）

## 关联页面

- [[wiki/concepts/三层架构]]
- [[wiki/concepts/原子笔记]]
- [[wiki/overview]]

## 待补充/疑问

> [!question] 待补充
> 与 Microsoft GraphRAG 的工程落地对比可另开 comparison 页。
