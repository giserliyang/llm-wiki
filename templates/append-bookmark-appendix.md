---

# 学习附录

## 书签卡

| 字段 | 值 |
| --- | --- |
| URL | <% tp.frontmatter.source_url ? tp.frontmatter.source_url : tp.frontmatter.url %> |
| 为什么存 | |
| 什么时候用 | |

## 阅读进度

> 用 Templater `gen-reading-progress` 生成；纯「以后查」可删本段。  
> 未勾选会出现在 [[dashboards/素材收件箱]]。  
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过

- [ ] 
  - [ ] 

## 拆解索引

```dataview
LIST
FROM "notes"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。
