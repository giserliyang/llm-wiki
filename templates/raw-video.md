---
title: "{{title}}"
type: raw
source_type: video
tags: []
status: 未读
created: "{{date}}"
source_url: ""
bvid: ""
cid: ""
author: ""
duration: ""
---

<!-- B 站可嵌入播放器（需 aid + bvid + cid + page）：
<iframe src="https://player.bilibili.com/player.html?aid=&bvid=&cid=&page=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allow="fullscreen; picture-in-picture" allowfullscreen="true" style="height:100%;width:100%; aspect-ratio: 16 / 9;"> </iframe>
也可用: python scripts/srt_to_video_note.py ... --aid --bvid --cid --page
-->

（字幕 / 文稿 / 自己整理的笔记放这里。若有时间轴章节，用 `### 01 开场` 这类标题，**不要**再包一层 `# 总标题`。）

---

# 学习附录

## 视频信息

| 字段 | 值 |
| --- | --- |
| URL | {{source_url}} |
| 平台 | Bilibili / YouTube / 其他 |
| 频道/UP主 | |
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
