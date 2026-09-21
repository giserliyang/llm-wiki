# Claudian 命令速查

打开方式：`Ctrl/Cmd + P` → **Claudian: Open chat view**（或侧边栏图标）。  
工作目录 = 本 Vault 根，会遵守 [[AGENTS]]。

## 前置

1. 本机已安装并登录 **Claude Code** CLI（或在 Claudian 设置里选好 Agent/模型）
2. 素材已在 `raw/`，例如 `raw/tutorials/xxx.md`

## 常用指令（可直接粘贴）

### 1. 摄入一篇 raw，生成 wiki

```
按根目录 AGENTS.md 和 prompt/ingest.md 处理：
读取 raw/tutorials/【文件名】.md，
更新 wiki/（优先改已有页，无相关主题才新建），
不要改 raw/ 和 notes/，
把变更写到 diff/【YYYYMMDD_主题】_diff.md，
最后用不超过 10 行总结你改了哪些页、diff 路径。
```

### 2. 只提炼概念页（细粒度）

```
读 raw/tutorials/【文件名】.md，按 AGENTS.md，
为文中 3–8 个核心概念各写/更新一页 wiki/concepts/，
互相用 [[]] 链接，关键结论标注 raw 来源，
输出到 diff/，不要直接覆盖 wiki/ 正文。
```

### 3. 质量校验

```
按 prompt/lint.md 扫描 wiki/，
只读检查，不改文件，
报告写到 report/【YYYYMMDD】_lint.md。
```

### 4. 问答 + 回写

```
基于 wiki/ 和相关 raw/ 回答：【你的问题】。
若结论可复用，按 AGENTS.md 生成 diff 到 diff/，
说明建议回写到哪一页。
```

### 5. 建议（不要代写）个人原子笔记

```
读 raw/tutorials/【文件名】.md 和 AGENTS.md，
不要修改 notes/。
在 diff/suggestions/ 里给出 1–3 篇原子笔记骨架建议
（含 YAML 字段与 source 双链），由我决定是否采纳。
```

### 6. 同时处理多个来源

```
按 AGENTS.md 与 prompt/ingest.md，
处理 raw/bookmarks/ 下 status 为未读 的文件，
更新 wiki/，统一输出 diff/2026XXXX_batch_ingest_diff.md。
```

## 审核闭环

1. Claudian 写出 `diff/*.md`
2. 你在 Obsidian 打开 diff，人工看一遍
3. 确认后把内容合并进 `wiki/` 对应页（或让它「已审核，应用 diff 到 wiki/」）
4. 打开 [[dashboards/学习仪表盘]] / [[wiki/overview]] 确认索引

## 它不会自动做的事

- 不会替你改 `notes/` 原子笔记（除非你明确授权）
- 不会删 raw
- 不会「一键全自动升级 understanding_level」——那是你的行为结果

## 出问题时

- 提示找不到 CLI / Node：在 Claudian 设置里指定 Claude Code 路径
- 权限模式：首次可允许写 vault；若只读，改 permissionMode
- 命令面板搜不到：确认社区插件已启用 Claudian
