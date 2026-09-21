---
title: "<% tp.file.title %>"
type: raw
source_type: tutorial
tags: []
status: 未读
created: <% tp.date.now("YYYY-MM-DD") %>
source_url: ""
author: ""
---

（教程/文章原文。保留原有章节标题层级，**不要**再包一层 `#` 总标题。）

---

# 学习附录

## 阅读进度

> Templater `gen-reading-progress` 生成骨架后再改任务。  
> 未勾选会出现在 [[dashboards/素材收件箱]]。  
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过

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
