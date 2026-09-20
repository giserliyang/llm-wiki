# Diff: 20260919_Python教程_尚硅谷 摄入

> 本 diff 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]`（尚硅谷 Python V3.0 教程）生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python.md`** — Python 概述
   - Python 起源（Guido van Rossum、1989年启动、1991年首发）
   - 设计哲学："优雅、明确、简单"
   - 版本历史时间线（0.9.0 → 1.0 → 2.0 → 3.0 不兼容 → 2.7 → 3.9/3.11/3.13）
   - 为何 AI 领域广泛使用 Python（5 点原因）
   - Python 运行方式（解释型）

2. **`wiki/concepts/python-基础语法.md`** — Python 基础语法
   - 字面量定义与示例
   - 变量（绑定关系、变量无类型数据有类型）
   - 常量（全大写约定、无强制机制）
   - 标识符命名规则（三种风格，推荐 snake_case）
   - 注释（单行 #、多行三引号、文件编码注释）
   - 运算符（算数 / 赋值 / 比较 / 逻辑 / 布尔类型）

3. **`wiki/concepts/数据类型.md`** — Python 数据类型
   - 整型（任意大小、分隔符、超大整数限制）
   - 浮点型（科学计数法）
   - 字符串（四种写法、三种格式化方式含 f-string、转义字符）
   - 数据类型转换（int/float/str）
   - 字符编码（ASCII / ISO 8859-1 / GB2312 / GBK / UTF-8）

### 新建对比页

4. **`wiki/comparisons/编译型与解释型语言.md`**
   - 编译型语言 vs 解释型语言 全方位对比（举例、执行流程、可执行文件、速度、跨平台性、场景）
   - Python 归入解释型语言

### 更新已有页

5. **`wiki/glossary.md`** — 术语表
   - 新增 11 个 Python 相关术语条目（变量、常量、标识符、整型、浮点型、字符串、字面量、f-string、UTF-8、编译型语言、解释型语言），每条均附来源锚点

6. **`wiki/overview.md`** — 总览
   - 补充「对比页」dataview 区块

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 1 章 必备基础知识]]`
- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python]]`
- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础]]`

---

## 待处理（后续可继续摄入）

本教程共 14 章，本次仅摄入前 3 章（必备基础 + 初识 Python + 核心基础）。以下章节建议后续继续：

- 第 4 章：流程控制语句（分支、循环）→ 可建 `python-流程控制.md`
- 第 5 章：函数入门 → 可建 `python-函数.md`
- 第 6 章：数据容器（列表、元组、字典、集合）→ 可建 `python-数据容器.md`
- 第 7 章：面向对象 → 可建 `python-面向对象.md`
- 第 8-14 章：进阶主题

---

## 原子笔记建议

见 `diff/suggestions/20260919_Python基础建议.md`
