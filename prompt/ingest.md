# 摄入提示词（Ingest Prompt）

发给 Claudian / LLM。工作目录 = Vault 根。遵守 `AGENTS.md`。

---

## 任务

读取用户指定的一份 `raw/` 文档，产出 **diff 包目录**（一页一个 md 文件），供人工审核后合并进 `wiki/`。

**不要**直接改 `wiki/` 正文。  
**不要**把多页 wiki 内容塞进同一个 `.md` 里用 ` ```markdown ` 包裹（页内代码块会打断围栏，无法合并）。

## 禁止

1. 修改 `raw/`  
2. 未经 diff 包就改 `wiki/`  
3. 修改用户已填的 `understanding_level` / `need_practice` / `status` / `last_review`（新建页默认值除外）  
4. 写入 `inbox/` 或本 Vault 以外目录  

## 主题判断与归类（自行分析）

| 类型 | wiki 目录 | `kind` |
| --- | ---: | ---: |
| 单一概念 | `concepts/` | `concept` |
| 两者对比 | `comparisons/` | `comparison` |
| 工具/人物/产品 | `entities/` | `entity` |
| 步骤/清单 | `practice/` | `practice` |

- 优先更新已有页；禁止同主题重复建页  
- 总览页只摘要 + `[[专页]]`，禁止整表复制  
- **已有 wiki 中语义相关的其它页**（含其它教程）：在本页「关联」及对方页「关联」中加 `[[页名]]`（双向织网；只链真实存在的页）

## 可学习页 YAML（必填）

```yaml
title: <页标题>
kind: concept|comparison|entity|practice
status: 未读
understanding_level: 1
need_practice: true
last_review: <YYYY-MM-DD>
source: "[[raw/用户给出的完整路径]]"
source_type: tutorial|video|bookmark|other
tags: [主题...]
```

## 正文与双链

- 摘要 ≤7 句；不确定处 `> [!question] 待补充`  
- 正文结论来源（**只允许一个 `#`**；**`#` 后必须是原文标题全文，含序号，不得删减**）：

```markdown
✅ [[raw/完整路径#10. 浅拷贝 vs 深拷贝]]
✅ [[raw/完整路径#1.1. 硬件]]
✅ [[raw/完整路径#第 5 章 函数]]
❌ [[raw/完整路径#浅拷贝 vs 深拷贝]]   ← 缺了原文序号「10. 」
❌ [[浅拷贝 vs 深拷贝]]                ← 无 raw 路径
❌ [[raw/完整路径]]                    ← 正文结论缺 #标题
❌ [[raw/完整路径#第 1 章#1.1. 硬件]]   ← 禁止两个 #
```

**抄标题规则（最重要）：**

1. 在 raw 文件中找到该行标题原文（例如 `### 10. 浅拷贝 vs 深拷贝`）  
2. `#` 后 = **整行去掉 `###` 和尾部空格后的文本** = `10. 浅拷贝 vs 深拷贝`  
3. **必须保留**序号：`10.`、`1.1.`、`第 5 章` 等  
4. **禁止**自己删序号、改标点、改空格、只写小节名  

每处结论单独写完整 `[[raw/路径#完整标题]]` 链接。

---

## Diff 包输出格式（强制）

用户指定包目录名，例如：

`diff/20260922_Python教程_尚硅谷_ingest/`

必须生成：

```text
diff/<包名>/
  MANIFEST.md
  pages/
    wiki/concepts/xxx.md          ← 与 vault 内目标路径一致
    wiki/comparisons/yyy.md
    wiki/entities/zzz.md
    wiki/overview.md              ← 仅当需要更新索引时
    wiki/links.md                 ← 同上
```

### MANIFEST.md 模板

```markdown
# Ingest Diff 包

## Meta

- raw：`raw/...`
- source_type：tutorial
- 包路径：`diff/<包名>/`
- 合并方式：将 `pages/` 下文件按相对路径复制到 Vault 同名路径

## 变更清单

| # | 操作 | 目标路径（Vault 内） | 包内文件 |
| --- | --- | --- | --- |
| 1 | CREATE | wiki/concepts/xxx.md | pages/wiki/concepts/xxx.md |
| 2 | CREATE | wiki/comparisons/yyy.md | pages/wiki/comparisons/yyy.md |
| 3 | UPDATE | wiki/overview.md | pages/wiki/overview.md |

## 自检清单

- [ ] pages/ 路径与 vault 目标一致
- [ ] 每页 YAML 含 understanding_level 等
- [ ] source 无 # 且路径正确
- [ ] 正文来源为 [[raw/路径#原文标题全文]]（**含 10. / 1.1. / 第 5 章 等序号，未删减**）
- [ ] 未改 raw/、未改用户 mastery 旧值
- [ ] 无把多页写进同一 md

## 总结（≤10 行）

- 主题与页数
- 包路径
- 下一步
```

### pages/ 下的 md

- 每个文件 = **将来 wiki 里那一整页**（从 YAML 到文末）  
- 可以正常包含 ` ```python ` 等内部代码块，**不要再包外层 markdown 围栏**  
- 文件名与 vault 目标名一致（含中文、空格规则与目标一致）  

---

## 应用（人审后发给 Claudian）

```text
我已审阅 diff/<包名>/MANIFEST.md，同意合并。

按 AGENTS.md：
1. 读 MANIFEST「变更清单」。
2. 将包内 pages/** 按相对路径复制到 Vault 对应路径（CREATE 新建，UPDATE 覆盖）。
3. 不要合并 MANIFEST.md 本身到 wiki/。
4. 不要改 raw/；不要改我已填的 understanding_level、need_practice、status、last_review（新建页默认值除外）。
5. ≤5 行总结：写入路径列表、有无失败项。
```

---

## 用户每次只需说明

1. `raw/` 素材路径  
2. `source_type`（默认 tutorial）  
3. diff **包目录**名：`diff/YYYYMMDD_主题_ingest/`  
