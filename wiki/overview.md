---
title: LLM Wiki 总览
status: ready
kind: overview
tags:
  - wiki
last_reviewed: 2026-09-11
---

# LLM Wiki 总览

这是 **LLM 维护、人类审核** 的结构化知识层入口。个人手写原子笔记见 [[dashboards/学习仪表盘]]。

## 这个 Wiki 是什么

把 `raw/` 中的教程、视频、网页书签，提前编译成可复用、可溯源、可互链的概念页——而不是每次临时检索。

## 怎么用

| 你想…     | 去哪                   |            |
| ------- | -------------------- | ---------- |
| 看体系地图   | [[wiki/links         | links]]    |
| 查术语     | [[wiki/glossary      | glossary]] |
| 学概念     | `wiki/concepts/`     |            |
| 查工具/人物  | `wiki/entities/`     |            |
| 看对比     | `wiki/comparisons/`  |            |
| 看自己的掌握度 | [[dashboards/学习仪表盘]] |            |

## 核心概念

```dataview
TABLE status, file.mtime AS "更新"
FROM "wiki/concepts"
SORT file.mtime DESC
```

## 核心实体

```dataview
LIST
FROM "wiki/entities"
SORT file.name ASC
```

## 最近更新的 Wiki 页

```dataview
TABLE status, file.mtime AS "更新"
FROM "wiki"
WHERE file.name != "overview" AND file.name != "links" AND file.name != "glossary"
SORT file.mtime DESC
LIMIT 20
```

## 与个人笔记的边界

- `wiki/`：LLM 写，你审
- `notes/`：你写，LLM 最多建议
- `raw/`：只读归档，保证溯源
