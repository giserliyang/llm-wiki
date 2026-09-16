---

# 学习附录

## 视频信息

| 字段 | 值 |
| --- | --- |
| URL | <% tp.frontmatter.url ? tp.frontmatter.url : tp.frontmatter.source_url %> |
| bvid | <% tp.frontmatter.bvid %> |
| 平台 | Bilibili |
| 频道/UP主 | <% tp.frontmatter.author %> |
| 时长 | |
| 为什么看 | |
| 什么时候用 | |

## 观看进度

> 用 Templater `gen-reading-progress` 从字幕章节标题生成；或手写 3–8 条。  
> 未勾选会出现在 [[dashboards/素材收件箱]]。  
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过

- [ ] 
  - [ ] 

## 关键帧截图

（图片放本视频文件夹 `images/`，命名 `01_主题.png`；外链图可直接贴 URL）

## 拆解索引

```dataview
LIST
FROM "notes"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。
