---
title: "LLM Wiki 的 5 个常见坑"
tags:
  - wiki
  - 知识管理
  - 避坑
source: "[[raw/bookmarks/别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云.md]]"
source_type: bookmark
source_url: "https://developer.cloud.tencent.com/article/2680461?policyId=1004"
status: draft
understanding_level: 0
need_practice: "对照 checklist 自检一次当前 Wiki 的健康度"
last_review: 2026-09-19
aliases: ["LLM Wiki 避坑"]
---

# LLM Wiki 的 5 个常见坑

## 我的理解

> 用自己的话回答：「这 5 个坑中，我目前踩过几个？最严重的是哪个？」

## 要点

| # | 坑 | 后果 | 解法 |
|---|---|---|---|
| 1 | 不设 Schema 规则，让 LLM 自由发挥 | 页面格式混乱、引用缺失 | 先写好 AGENTS.md 与文件模板 |
| 2 | 手动编辑 Wiki 页面 | LLM 后续更新会覆盖手动内容 | 所有修改走 diff 审核流 |
| 3 | 忽视原始素材溯源 | 无法验证 LLM 总结的真实性 | raw/ 保持只读，强制 source 字段 |
| 4 | 一开始就上 GraphRAG 等复杂架构 | 运维成本高，半途而废 | 从小体量起步，循序渐进 |
| 5 | 不做定期校验 | 小错误累积成「错误知识库」 | 每周执行 lint，人工审核报告 |

## 疑问

- 「定期校验」的频率：每周/每月？由谁执行？
- 「手动编辑 Wiki」是否绝对禁止？紧急修正是否可以例外？
- 有没有「自动校验」的工具/脚本可以辅助 lint？

## 待验证

- [ ] 对照 5 条 checklist，逐条标记「已规避 / 有风险 / 已踩坑」
- [ ] 为每条风险项制定一条具体行动（如：本周内补 AGENTS.md 规则）

## 关联

- [[wiki/concepts/LLM-Wiki]]
- [[wiki/concepts/三层架构]]