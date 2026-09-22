# 校验提示词（Lint Prompt）

只读检查；**不要修改** `wiki/` 与 `raw/`。

对 `wiki/` 检查：

1. **source 路径**是否为 `raw/` 下真实文件（禁止 `../raw`、简写、同上）  
2. **正文来源链接**是否为 `[[raw/完整路径#标题全文]]`；`#` 后与原文标题一致（**必须保留序号**如 `10.`、`1.1.`、`第 5 章`）；无路径 `[[标题]]`；缺 `#`；两个 `#`  
3. Frontmatter：`kind` / `status` / `understanding_level`(0–5) / `need_practice` / `last_review` / `source` / `source_type`  
4. 链接是否指向不存在的页  
5. 概念页与对比页是否整表重复  
6. `wiki/overview.md`、`wiki/links.md` 是否过期  
7. 同主题是否多页矛盾  
8. **含代码的页（阶段 2）：** 是否缺 `## 代码与坑`；代码是否缺首行 `# 这一步是为了解决：【…】`；是否只贴代码无 Callout/说明  

报告：`report/YYYYMMDD_lint.md`

```markdown
# Lint 报告 YYYY-MM-DD

## 阻断问题
- [ ] 页：... 问题：... 建议：...
  （链接：缺路径 / 缺 # / 双 # / # 后缺序号）
  （代码：缺 ## 代码与坑 / 缺「为解决【…】」）

## 应改进
- ...

## 建议合并
- A + B → C

## 通过项摘要
```

人审后再决定是否生成修复 diff。
