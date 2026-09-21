---
title: "<% tp.file.title %>"
type: raw
source_type: bookmark
tags: []
status: 未读
created: <% tp.date.now("YYYY-MM-DD") %>
source_url: ""
author: ""
---

（剪藏正文。保留原文标题层级，**不要**再包一层 `#` 总标题。）

---

# 学习附录

## 书签卡

| 字段 | 值 |
| --- | --- |
| URL | <% tp.frontmatter.source_url ? tp.frontmatter.source_url : tp.frontmatter.url %> |
| 为什么存 | |
| 什么时候用 | |

## 阅读进度

> 系统要学才保留本段。未勾选 → [[dashboards/素材收件箱]]。

- [ ] 
  - [ ] 

## 拆解索引

```dataview
LIST
FROM "wiki"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。
