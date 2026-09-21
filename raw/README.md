# Raw 素材层（只读）

**只放外部素材**，不要放个人灵感或手写笔记（那些在 `wiki/`）。

| 子目录 | 内容 |
| --- | --- |
| `tutorials/` | 教程、文档 |
| `videos/` | 视频/本地课笔记（字幕等） |
| `bookmarks/` | 网页剪藏、公众号等 |
| `images/` | 跨素材共用图 |
| `others/` | 其它外源 |

## 命名

`YYYYMMDD_主题_来源.md`  
带图成套：`主题/` 文件夹 + 同名 md + `images/`

## 模板（Templater）

- 教程：`templates/raw-tutorial.md` 或剪完加 `append-tutorial-appendix` + `prepend-tutorial-yaml`
- 视频：`raw-video` / `append-video-appendix`
- 书签：`raw-bookmark` / `append-bookmark-appendix`

YAML 用 `status` / `source_type`；未完成任务进 [[dashboards/素材收件箱]]。
