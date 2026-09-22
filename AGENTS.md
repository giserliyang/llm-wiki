# LLM 操作规则（AGENTS）

Vault：**一层 `wiki/` 知识库**。掌握度写 **YAML**。`raw/` 只读。

## 目录

```
raw/    外部素材只读
wiki/   知识库（唯一知识层）
  concepts/ entities/ comparisons/ decisions/ practice/
  （根下）    note / essay 等
  overview.md glossary.md links.md
diff/   仅待审的 wiki 变更
inbox/  （库根）临时速记，与 wiki 无关，LLM 勿碰
```

## 所有权

| 对象 | 规则 |
| --- | ---: |
| `raw/` | LLM 只读 |
| `wiki/` 正文与 YAML | 人写/改（含审 diff 时合并） |
| LLM 对 wiki 的变更 | 只写 `diff/`，人审后合入 |

## 双链与来源（强制）

### 1. YAML `source`（**文件级**，可不带 `#`）

```yaml
source: "[[raw/tutorials/Python教程/20260921_Python教程_尚硅谷]]"
```

- 路径与磁盘一致；禁止 `../raw/`、只写文件名、`[[同上]]`
- **YAML 里不要带 `#章节`**（那是正文引用的事）

### 2. 正文关键结论（**章/节级**，必须带单个 `#`）

```markdown
✅ [[raw/tutorials/Python教程/20260921_Python教程_尚硅谷#第 5 章 函数]]
✅ [[raw/tutorials/Python教程/20260921_Python教程_尚硅谷#1.1. 硬件]]
❌ [[raw/tutorials/Python教程/20260921_Python教程_尚硅谷]]          ← 正文写结论时缺 #标题
❌ [[第 5 章 函数]] / [[../raw/...]] / [[同上]]
❌ [[raw/...尚硅谷#第 5 章 函数#1.1. 硬件]]                          ← 禁止两个 #，Obsidian 无法跳转
```

- **只允许一个 `#`**；`#` 后必须是原文某行标题**全文**（含 `10.`、`1.1.`、`第 5 章` 等序号，**不得删序号**）
- 示例：`#10. 浅拷贝 vs 深拷贝` 正确；`#浅拷贝 vs 深拷贝` 错误（缺 `10.`）
- 每一处结论单独写完整链接；禁止简写、禁止双锚点

### 3. Lint 必查

- YAML `source` 路径是否存在（不应含错误相对路径）
- 正文是否出现无路径 `[[标题]]`
- 正文章/节引用是否缺 `#` 或出现 **两个及以上 `#`**
- 含代码页是否缺 `## 代码与坑` 或「为解决【…】」说明

## YAML（可学习 wiki 页必填）

| 字段 | 要求 |
| --- | --- |
| `kind` | concept / comparison / entity / practice / note / essay / decision / index |
| `status` | 新建建议 `未读` |
| `understanding_level` | 新建建议 `1` |
| `need_practice` | 新建建议 `true` |
| `last_review` | 入库日期 |
| `source` | 见上「双链」规则 |
| `source_type` | tutorial / video / bookmark / other |
| `tags` | 主题标签 |

用户已填的 mastery 字段，LLM 勿擅自改。

## 正文中的代码（阶段 2）

wiki 页若含代码示例（LLM 产出或人工合并时）：

- 代码块**第一行注释**写：`# 这一步是为了解决：【问题/报错】`
- 易错点用 Callout：`> [!tip]` / `> [!danger]`
- 禁止只粘贴原文命令/代码而不说明用途
- 示例与说明放在 `## 代码与坑` 小节（若页内已有该小节则写入其中）

## 目录类型

| 主题 | 路径 | kind |
| --- | ---: | --- |
| 单概念 | `wiki/concepts/` | `concept` |
| 两者对比 | `wiki/comparisons/` | `comparison` |
| 总览提到专页 | 一句话 + `[[专页]]`，**不复制整表** |

## 摄入 Ingest

1. 读 `raw/`，自行提炼主题  
2. 变更写入 **diff 包目录**（禁止用单文件 + 外层 ```markdown 包裹多页）：

```text
diff/<YYYYMMDD_主题>_ingest/
  MANIFEST.md          # Meta + 变更清单（目标路径 ↔ 包内路径）+ 自检 + 总结
  pages/
    wiki/concepts/....md
    wiki/comparisons/....md
    ...
    wiki/overview.md   # 仅需要时
    wiki/links.md
```

3. `pages/` 下每个 md = **将来 wiki 的整页**（含 YAML 与内部代码块），路径与 vault 目标一致  
3. 优先更新已有页；新建时在「关联」中链到**已有**相关 wiki 页（含其它 source 的页）  
4. 禁止改 `raw/`；禁止未经 diff 包改 `wiki/` 正文  
5. `wiki/overview.md`、`wiki/links.md` 用 **Dataview 动态列表**（TABLE/LIST + GROUP BY source），不要手写「关键主题」点名清单，避免与文件夹不一致  
6. 合并：将 `pages/**` 复制到 vault 对应路径；`MANIFEST.md` 不进入 `wiki/`  

人审合并后删除 diff 包。跨两套 raw 的互链可另开 diff 包做 `UPDATE`。

## Lint

扫描 `wiki/`：来源路径是否存在、**正文链接是否含路径与 `#章节`**、YAML、重复页、索引是否过期 → `report/`。

## 语气

中文，先结论，不确定就标出。
