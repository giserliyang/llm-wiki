# 摄入提示词（Ingest Prompt）

发给 Claudian / LLM。工作目录 = **本 Vault 根：`C:\Users\HP\Documents\llm_wiki\llm-wiki - 副本`**。遵守 `AGENTS.md`。

---

## 任务

读取用户指定的一份 `raw/` 文档，产出 **diff 包目录**（一页一个 md），供人工审核后合并进 `wiki/`。

**不要**直接改 `wiki/` 正文。  
**不要**把多页 wiki 塞进同一个 `.md` 用 ` ```markdown ` 包裹（页内代码块会打断围栏）。

## 禁止

1. 修改 `raw/`  
2. 未经 diff 包就改 `wiki/`  
3. 修改用户已填的 `understanding_level` / `need_practice` / `status` / `last_review`（新建页默认值除外）  
4. 写入 `inbox/` 或本 Vault 以外目录  
5. 含代码的页省略 `## 代码与坑`，或只贴原文代码不写「为解决【…】」  

## 主题判断与归类（自行分析）

| 类型 | wiki 目录 | `kind` |
| --- | ---: | ---: |
| 单一概念 | `concepts/` | `concept` |
| 两者对比 | `comparisons/` | `comparison` |
| 工具/人物/产品 | `entities/` | `entity` |
| 步骤/清单 | `practice/` | `practice` |

- 优先更新已有页；禁止同主题重复建页  
- 总览页只摘要 + `[[专页]]`，禁止整表复制  
- 语义相关已有页（含其它教程）：在双方「关联」加 `[[页名]]`  
- **含代码的页必须写 `## 代码与坑`**  

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
- **含代码的页（阶段 2）：** `## 代码与坑`；代码首行 `# 这一步是为了解决：【问题/报错】`；易错点用 `> [!tip]` / `> [!danger]`；禁止只贴原文代码  
- 正文结论来源（**只允许一个 `#`**；**`#` 后必须是原文标题全文，含序号，不得删减**）：

```markdown
✅ [[raw/完整路径#10. 浅拷贝 vs 深拷贝]]
✅ [[raw/完整路径#1.1. 硬件]]
✅ [[raw/完整路径#第 5 章 函数]]
❌ [[raw/完整路径#浅拷贝 vs 深拷贝]]   ← 缺原文序号「10. 」
❌ [[浅拷贝 vs 深拷贝]]                ← 无 raw 路径
❌ [[raw/完整路径]]                    ← 正文结论缺 #标题
❌ [[raw/完整路径#第 1 章#1.1. 硬件]]   ← 禁止两个 #
```

**抄标题规则：**

1. 在 raw 中找到标题行（例如 `### 10. 浅拷贝 vs 深拷贝`）  
2. `#` 后 = 整行去掉 `###` 与尾部空格 = `10. 浅拷贝 vs 深拷贝`  
3. **必须保留** `10.`、`1.1.`、`第 5 章` 等序号  
4. **禁止**删序号、改标点/空格、只写小节名  

每处结论单独写完整 `[[raw/路径#完整标题]]`。

---

## Diff 包输出格式（强制）

例如：`diff/20260922_Python教程_尚硅谷_ingest/`

```text
diff/<包名>/
  MANIFEST.md
  pages/
    wiki/concepts/xxx.md
    wiki/comparisons/yyy.md
    wiki/overview.md    ← 仅需要时
    wiki/links.md
```

### MANIFEST.md 模板

```markdown
# Ingest Diff 包

## Meta

- raw：`raw/...`
- source_type：tutorial
- 包路径：`diff/<包名>/`
- 合并方式：`pages/` 按相对路径复制到 Vault 同名路径

## 变更清单

| # | 操作 | 目标路径（Vault 内） | 包内文件 |
| --- | --- | --- | --- |
| 1 | CREATE | wiki/concepts/xxx.md | pages/wiki/concepts/xxx.md |
| 2 | CREATE | wiki/comparisons/yyy.md | pages/wiki/comparisons/yyy.md |

## 自检清单

- [ ] pages/ 路径与 vault 目标一致
- [ ] 每页 YAML 含 understanding_level 等
- [ ] source 无 # 且路径正确
- [ ] 正文来源为 [[raw/路径#原文标题全文]]（含 10. / 1.1. / 第 5 章 等序号）
- [ ] 含代码时：有 `## 代码与坑`、首行「为解决【…】」、必要 Callout
- [ ] 未改 raw/、未改用户 mastery 旧值
- [ ] 无把多页写进同一 md

## 总结（≤10 行）

- 主题与页数
- 包路径
- 下一步
```

### pages/ 下的 md

- 每个文件 = **将来 wiki 的那一整页**（YAML 到文末）  
- 可包含 ` ```python ` 等内部代码块，**不要再包外层 markdown 围栏**  
- 文件名与 vault 目标名一致  
- **含代码时必须包含 `## 代码与坑`**  

---

## 应用（人审后发给 Claudian）

```text
我已审阅 diff/<包名>/MANIFEST.md，同意合并。

按 AGENTS.md：
1. 读 MANIFEST「变更清单」。
2. 将包内 pages/** 按相对路径复制到 Vault 对应路径（CREATE 新建，UPDATE 覆盖）。
3. 不要把 MANIFEST.md 写入 wiki/。
4. 不要改 raw/；不要改我已填的 understanding_level、need_practice、status、last_review（新建页默认值除外）。
5. ≤5 行总结：写入路径列表、有无失败项。
```

---

## 用户每次只需说明

1. `raw/` 素材路径  
2. `source_type`（默认 tutorial）  
3. diff **包目录**名：`diff/YYYYMMDD_主题_ingest/`  
