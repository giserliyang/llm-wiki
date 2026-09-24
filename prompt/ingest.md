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
6. **丢掉原文案例**（必须沉淀到 practice 或 concept 的「## 案例」）  

## 主题判断与归类（自行分析）

| 类型 | wiki 目录 | `kind` |
| --- | ---: | ---: |
| 单一概念 | `concepts/` | `concept` |
| 两者对比 | `comparisons/` | `comparison` |
| **完整案例 / 实战 / 小项目** | **`practice/`** | **`practice`** |
| 工具/人物/产品 | `entities/` | `entity` |
| 短例（解释概念） | 写入对应 concept/comparison 的 **`## 案例`** | — |

- 优先更新已有页；禁止同主题重复建页  
- 总览页只摘要 + `[[专页]]`，禁止整表复制  
- 语义相关已有页（含其它教程）：在双方「关联」加 `[[页名]]`  
- **含代码的页必须写 `## 代码与坑`**  
- **有案例必须写 `## 案例` 或 `wiki/practice/` 专页**  

## 案例提取规则（强制）

1. 扫描原文中的「示例 / 案例 / 实战 / 小项目 / Demo / 端到端 / 实现 xxx」等  
2. **可独立复现的完整案例** → `wiki/practice/<案例名>.md`（`kind: practice`）：场景 → 步骤/代码 → 结果  
3. **为解释某一概念的短例** → 写入该概念/对比页的 **`## 案例`**，写清「场景 / 做法 / 结果」  
4. 案例与概念页互链：practice 页「关联」链 concept；concept 的「## 案例」链 practice 页  
5. **禁止**只写抽象要点而省略原文案例  

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
❌ [[raw/完整路径#浅拷贝 vs 深拷贝]]   ← 缺了原文序号「10. 」
❌ [[浅拷贝 vs 深拷贝]]                ← 无 raw 路径
❌ [[raw/完整路径]]                    ← 正文结论缺 #标题
❌ [[raw/完整路径#第 1 章#1.1. 硬件]]   ← 禁止两个 #
```

**抄标题规则：**

1. 在 raw 中找到标题行（例如 `### 10. 浅拷贝 vs 深拷贝`）  
2. `#` 后 = 整行去掉 `###` 与尾部空格 = `10. 浅拷贝 vs 深拷贝`  
3. **必须保留** `10.`、`1.1.`、`第 5 章` 等序号  
4. **禁止**删序号、改标点/空格、只写小节名  

每处结论/案例单独写完整 `[[raw/路径#完整标题]]`。

---

## Diff 包输出格式（强制）

例如：`diff/20260922_Python教程_尚硅谷_ingest/`

```text
diff/<包名>/
  MANIFEST.md
  pages/
    wiki/concepts/xxx.md
    wiki/practice/案例名.md     ← 有案例时
    wiki/comparisons/yyy.md
    wiki/overview.md            ← 仅需要时
    wiki/links.md
```

### MANIFEST.md 自检清单（摘录）

- [ ] **原文案例已沉淀**（practice 页或 concept 的「## 案例」，并带 raw 来源链接）
- [ ] 含代码时：有 `## 代码与坑`、代码首行「为解决【…】」注释、必要 Callout
- [ ] 正文来源为 [[raw/路径#原文标题全文]]（含序号）

### pages/ 下的 md

- 每个文件 = **将来 wiki 的那一整页**（YAML 到文末）  
- **含代码必须 `## 代码与坑`；有案例必须 `## 案例` 或独立 practice 页**  

---

## 用户每次只需说明

1. `raw/` 素材路径  
2. `source_type`（默认 tutorial）  
3. diff **包目录**名：`diff/YYYYMMDD_主题_ingest/`  
