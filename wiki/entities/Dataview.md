---
title: Dataview
status: ready
kind: entity
tags:
  - wiki
  - 工具
---

# Dataview

## 摘要

Obsidian 社区插件：把 Markdown + Frontmatter 当数据库查询；本库仪表盘的引擎。

## 核心内容

### 本库用到的查询

- `TABLE` / `LIST` / `TASK` / `GROUP BY`
- 数据源：`FROM "notes"`、`FROM "raw"`、`FROM "wiki/..."`

### 安全注意

- `dataviewjs` 可改文件，慎用他人脚本
- 市场打不开时手动装到 `.obsidian/plugins/dataview/`

### 与官方 Bases 的关系

- Bases 可覆盖约 80% 表格筛选
- 复杂 JS / 行内查询仍属 Dataview

## 引用来源

- Dataview 社区文档常识

## 关联页面

- [[wiki/entities/Obsidian]]
- [[dashboards/学习仪表盘]]
