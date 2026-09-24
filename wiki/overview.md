---
title: 知识总览
status: ready
kind: index
tags:
  - index
last_reviewed: 2026-09-23
---

# 知识总览

`wiki/` = 唯一知识库。下面列表由 Dataview **动态读取全部** 已有页，不靠手写清单。

## 入口

| 去哪                   | 内容     |
| -------------------- | ------ |
| [[wiki/links]]       | 链接索引   |
| [[wiki/glossary]]    | 术语     |
| [[dashboards/学习仪表盘]] | 掌握度    |
| [[dashboards/素材收件箱]] | raw 进度 |

## 全部概念页

```dataview
LIST
FROM "wiki/concepts"
SORT file.name ASC
```

## 全部对比页

```dataview
LIST
FROM "wiki/comparisons"
SORT file.name ASC
```

## 全部实体页

```dataview
LIST
FROM "wiki/entities"
SORT file.name ASC
```

## 全部实践页

```dataview
LIST
FROM "wiki/practice"
SORT file.name ASC
```

## 按素材 source 分组（两套教程是否齐全一眼可见）

```dataview
TABLE rows.file.link AS "wiki 页", length(rows) AS "数量"
FROM "wiki"
WHERE source
GROUP BY source
```

## 根下笔记（非分类目录）

```dataview
TABLE kind, understanding_level AS "level", status
FROM "wiki"
WHERE !contains(file.path, "/concepts/") AND !contains(file.path, "/comparisons/")
  AND !contains(file.path, "/entities/") AND !contains(file.path, "/practice/")
  AND !contains(file.path, "/decisions/")
  AND kind != "index"
  AND file.name != "overview" AND file.name != "links" AND file.name != "glossary" AND file.name != "README"
SORT file.mtime DESC
```

