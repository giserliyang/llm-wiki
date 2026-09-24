# 个人学习系统（Obsidian Vault）

> **本 Vault：** `C:\Users\HP\Documents\llm_wiki\llm-wiki - 副本`  
> 一层 `wiki/` ｜ YAML 管掌握度 ｜ LLM 只出 `diff/`

```text
raw/      外部素材（只读）
wiki/     知识库（concepts / comparisons / practice / 根下 note…）
inbox/    库根临时速记（不进 wiki、不进 LLM）
diff/     待审 wiki 变更（包目录）
dashboards/
AGENTS.md
```

## 内容入口决策表

| 你有什么 | 放哪 | 模板 / 工具 | `source_type` |
| --- | ---: | --- | ---: |
| 教程 MD / 长文档 | `raw/tutorials/` | `raw-tutorial` 或 `prepend-tutorial-yaml` + 正文 + `append-tutorial-appendix` | `tutorial` |
| B 站在线课 | `raw/videos/` | **Bilibili Obsidian Clipper** 剪字幕 → 补 YAML + `append-video-appendix` | `video` |
| 本地 mp4 课 | 本地磁盘；笔记进 `raw/videos/` | `python scripts/video_to_note.py "完整路径.mp4"` | `video` |
| 网页 / 公众号 / 书签 | `raw/bookmarks/` | Web Clipper 或 `raw-bookmark` / `append-bookmark-appendix` | `bookmark` |
| 灵感一句话 | `inbox/` | `node-quick-capture` | — |
| 概念专页 / 对比 | `wiki/concepts`、`comparisons` | `node-concept`；LLM 经 diff | 由素材决定 |
| **完整案例 / 实战 / 小项目** | **`wiki/practice/`** | `node-practice`；LLM 经 diff | 同上 |
| 概念短例 | 概念/对比页的 **`## 案例`** | `node-concept` 已含该小节 | 同上 |
| 个人短笔记 | `wiki/` 根下 | `node-atomic-note` | 同上 |
| 长文总结 | `wiki/` 根下 | `node-essay`（`kind: essay`） | 可空 |

**代码：** 含代码的 wiki 页用 `## 代码与坑` + 首行「为解决什么」注释 + Callout（阶段 2）。  
**案例：** 教程里的案例/实战必须沉淀到 `wiki/practice/` 或概念页 `## 案例`，并带 raw 来源链接。

## 合并 diff 后的收尾清单

1. 按 `MANIFEST` 把 `pages/**` 复制进 `wiki/`（不合并 MANIFEST 本身）  
2. **删除**该 `diff/<包名>/`（Git 已有历史）  
3. 自己改 YAML：`status` / `understanding_level` / `need_practice` / `last_review`  
4. 打开 [[wiki/overview]]、[[wiki/links]] 与 [[dashboards/学习仪表盘]] 点验  
5. 可选：跑 `prompt/lint.md`  

## 日常入口

- [[dashboards/学习仪表盘]]
- [[dashboards/素材收件箱]]
- [[wiki/overview]]
- [[AGENTS]]
- Claudian 命令见 `prompt/claudian-cheatsheet.md`
