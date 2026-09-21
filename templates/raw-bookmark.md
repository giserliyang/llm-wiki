---
title: "{{title}}"
type: raw
source_type: bookmark
tags: []
status: 未读
created: "{{date}}"
source_url: ""
author: ""
---

（剪藏正文放这里。保留文章原有标题层级，**不要**再包一层 `# 总标题`。）

---

# 学习附录

## 书签卡

| 字段 | 值 |
| --- | --- |
| URL | {{source_url}} |
| 为什么存 | |
| 什么时候用 | |

## 阅读进度

> 用 Templater `gen-reading-progress` 生成（~~脚本~~碰到「学习附录」会停）。
> 纯参考书签可删掉本段。未勾选会出现在 [[dashboards/素材收件箱]]。
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
