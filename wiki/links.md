---
title: 全局链接索引
status: ready
kind: links
tags:
  - wiki
  - moc
---

# 全局链接索引

> LLM 更新 wiki 后必须检查本页。人也可手动整理主题聚类。

## 按主题

### 知识管理
- [[wiki/concepts/LLM-Wiki]]
- [[wiki/concepts/原子笔记]]
- [[wiki/concepts/三层架构]]
- [[wiki/comparisons/LLM-Wiki-vs-RAG]]

### 工具
- [[wiki/entities/Obsidian]]
- [[wiki/entities/Dataview]]

## 自动：所有概念页

```dataview
LIST
FROM "wiki/concepts"
SORT file.name ASC
```

## 自动：所有实体页

```dataview
LIST
FROM "wiki/entities"
SORT file.name ASC
```

## 自动：对比页

```dataview
LIST
FROM "wiki/comparisons"
SORT file.name ASC
```
