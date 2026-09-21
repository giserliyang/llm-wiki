---

# 学习附录

## 视频信息

| 字段 | 值 |
| --- | --- |
| URL | <% tp.frontmatter.source_url ? tp.frontmatter.source_url : tp.frontmatter.url %> |
| bvid | <% tp.frontmatter.bvid %> |
| 平台 | |
| 频道/UP主 | <% tp.frontmatter.author %> |
| 时长 | |
| 为什么看 | |
| 什么时候用 | |

## 观看进度

> Templater `gen-reading-progress` 或手写。未勾选 → [[dashboards/素材收件箱]]。

- [ ] 
  - [ ] 

## 关键帧截图

（`images/`）

## 拆解索引

```dataview
LIST
FROM "wiki"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。
