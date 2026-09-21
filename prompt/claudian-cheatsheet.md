# Claudian 命令速查

**Vault 根：** `C:\Users\HP\Documents\llm_wiki\llm-wiki`  
规则：`AGENTS.md` + `prompt/ingest.md`（**diff 用包目录，一页一个 md**）。

---

## 1. 摄入

```text
按 AGENTS.md 与 prompt/ingest.md 执行摄入。

素材：
raw/tutorials/Python教程/20260921_Python教程_尚硅谷.md

source_type：tutorial

diff 包目录：
diff/20260922_Python教程_尚硅谷_ingest/

要求：按 ingest.md 生成 MANIFEST.md + pages/wiki/**；一页一个 md；不要用外层 ```markdown 包住整页。
```

---

## 2. 应用 diff 包

```text
我已审阅 diff/<包名>/MANIFEST.md，同意合并。

按 AGENTS.md：
1. 读 MANIFEST「变更清单」。
2. 将包内 pages/** 按相对路径复制到 Vault 对应路径（CREATE 新建，UPDATE 覆盖）。
3. 不要把 MANIFEST.md 写入 wiki/。
4. 不要改 raw/；不要改我已填写的 understanding_level、need_practice、status、last_review（新建页默认值除外）。
5. ≤5 行总结：写入了哪些路径、有无失败项。
```

---

## 3. Lint

```text
按 AGENTS.md 与 prompt/lint.md 执行，只读不改。
扫描 wiki/；检查 source、YAML、正文链接（缺 # / 双 # / 无路径 / # 后缺序号如 10.）。
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

## 6. 跨素材织网（两套教程互链）

```text
按 AGENTS.md，生成互链 diff 包：
diff/20260922_跨教程互链/

素材范围：
- raw/tutorials/Python教程/20260921_Python教程_尚硅谷.md
- raw/tutorials/Python数据分析教程/20260921_Python数据分析教程_尚硅谷.md

任务：
1. 扫描 wiki/ 全部页，按语义在「关联」小节互相链接（只用真实存在的页名 [[]]）。
   例如：列表/字典 ↔ Pandas DataFrame/Series；Python 环境 ↔ Anaconda；注释规范 等。
2. 若无「关联」小节则追加在页尾。
3. 不改正文技术结论；不改 raw/；不改 mastery YAML。
4. 每个被改的页输出完整文件到 pages/wiki/...（MANIFEST 列 CREATE/UPDATE）。
5. 可选：UPDATE wiki/links.md（保持 Dataview 结构即可）。

输出格式按 prompt/ingest.md 的 Diff 包。
```

---

## 边界

- 不改 `raw/`、不直接改 `wiki/`（须先有 diff 包）  
- diff：**目录包**，不是单文件嵌套代码块  
- 合并：只拷 `pages/**`，不拷 `MANIFEST.md`  
