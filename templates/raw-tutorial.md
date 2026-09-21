---
title: "{{title}}"
type: raw
source_type: tutorial
tags: []
status: 未读
created: "{{date}}"
source_url: ""
author: ""
---

（教程/文章原文。完整教程请保留原有 `# 第N章`，不要在外面再包一层 `# 总标题`。）

---

# 学习附录

## 阅读进度

> 用 Templater 生成章节骨架后，改成任务清单。
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过  
> 未勾选任务会出现在 [[dashboards/素材收件箱]]。

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
