# Raw 素材层（只读）

把所有原始内容丢这里，**不要在 LLM 流程里改这些文件**。

## 目录约定（重要）

**一篇带附件的素材 = 一个独立文件夹**，避免多教程共用 `images/` 时文件名冲突。

```
raw/tutorials/
  Python_V3.0/
    Python_V3.0.md          # 主文档
    images/                 # 本篇专用配图
      document_image_rId4.png
      ...
  另一篇教程/
    另一篇教程.md
    images/
  无图教程.md               # 单文件也可以
```

- 文件夹名用主题（建议 `YYYYMMDD_主题` 或稳定英文/中文短名）
- 文内图片用相对路径：`![](images/xxx.png)`
- 全局截图/示意图才放顶层 `raw/images/`

| 子目录 | 放什么 |
| --- | --- |
| `tutorials/` | 教程原文、文档、讲义 |
| `videos/` | 视频字幕、文稿、自述笔记 |
| `bookmarks/` | 网页书签、剪藏（含公众号等网页文章） |
| `images/` | 跨素材共用的全局图（尽量少用） |
| `others/` | 零散碎片 |

## 命名

单文件：`YYYYMMDD_主题_来源.md`  
成套素材：文件夹 `主题_版本/`，主文档与文件夹同名

## 模板（勿在本文用双链，避免污染图谱）


## 模板 

[[templates/raw-tutorial|教程]]
[[templates/raw-video|视频]]
[[templates/raw-bookmark|书签 / 网页剪藏]]
