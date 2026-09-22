# Claudian 命令速查

**Vault 根：** `C:\Users\HP\Documents\llm_wiki\llm-wiki - 副本`  
规则：`AGENTS.md` + `prompt/ingest.md`（diff 用包目录；含代码页须有 `## 代码与坑`）。

---

## 1. 摄入

```text
按 AGENTS.md 与 prompt/ingest.md 执行摄入。

素材：
raw/tutorials/Python教程/20260921_Python教程_尚硅谷.md

source_type：tutorial

diff 包目录：
diff/20260922_Python教程_尚硅谷_ingest/

要求：按 ingest.md 生成 MANIFEST.md + pages/wiki/**；一页一个 md；不要用外层 ```markdown 包住整页；含代码的页必须有 ## 代码与坑。
```

---

## 2. 应用 diff 包

```text
我已审阅 diff/<包名>/MANIFEST.md，同意合并。

按 AGENTS.md：
1. 读 MANIFEST「变更清单」。
2. 将包内 pages/** 按相对路径复制到 Vault 对应路径。
3. 不要把 MANIFEST.md 写入 wiki/。
4. 不要改 raw/；不要改我已填的 understanding_level、need_practice、status、last_review（新建页默认值除外）。
5. ≤5 行总结：写入了哪些路径、有无失败项。
```

---

## 3. Lint

```text
按 AGENTS.md 与 prompt/lint.md 执行，只读不改。
扫描 wiki/；检查 source、YAML、正文链接（缺 # / 双 # / 无路径 / # 后缺序号）、代码是否缺「为解决【…】」。
输出：report/YYYYMMDD_lint.md
```

---

## 4. 修复 lint → diff 包

```text
读 report/【文件】阻断项与应改进，
按 AGENTS.md 与 prompt/ingest.md 的 Diff 包格式，
生成：
diff/【日期】_lint_fix/
  MANIFEST.md
  pages/wiki/**（仅问题页的完整目标文件）
不改 raw/；不改我的 mastery 字段。
≤5 行总结。
```

---

## 5. 应用 lint 修复包

```text
我已审阅 diff/<lint_fix 包>/MANIFEST.md，同意应用。
将 pages/** 复制到 MANIFEST 中的 vault 目标路径；
不要把 MANIFEST 写入 wiki/；
不要改 raw/ 与我的 mastery 字段；
≤5 行总结。
```

---

## 边界

- 不改 `raw/`、不直接改 `wiki/`（须先有 diff 包）  
- diff：**目录包**，不是单文件嵌套代码块  
- 合并：只拷 `pages/**`，不拷 `MANIFEST.md`  
- 含代码页：`## 代码与坑` + 「为解决【…】」注释 + Callout  
