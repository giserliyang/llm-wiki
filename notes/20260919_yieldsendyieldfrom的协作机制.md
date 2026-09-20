---
title: yieldsendyieldfrom的协作机制
tags:
  - python
  - 生成器
  - 迭代器
status: 未读
understanding_level: 1
need_practice: true
last_review: 2026-09-19
source: "[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器]]"
source_type: tutorial
source_url: ""
aliases:
  - "生成器协作机制"
---

# yieldsendyieldfrom的协作机制

> 本篇拆解自 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器]]。（正文里用 `[[原文#章节]]` 带锚点）

## 我的理解

把生成器想象成一个可以暂停和恢复的函数。用自己的话描述：`next()` 和 `send()` 的区别是什么？第一次为什么不能 send 值？

## 要点

1. `yield` 暂停函数并返回值，下次 `next()` 从暂停处继续 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]
2. `send(value)` 既能取值也能送值：送的值成为上一次 `yield` 表达式的结果 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]
3. **第一次必须用 `next()` 或 `send(None)`**：因为此时没有"上一次 yield"来接收值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]
4. `yield from` 将可迭代对象的元素逐个 yield 出去，替代 `for + yield` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]
5. 生成器是特殊的迭代器，自动实现了 `__iter__` 和 `__next__` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]
6. `return` 在生成器中抛出 StopIteration，return 值成为异常信息 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]

## 疑问 / 待验证

> [!question] 待补充
> `yield from` 如何传递 send 的值到子生成器？PEP 380 的设计意图是什么？

## 实战记录

- [ ] 用生成器实现一个简单的状态机（如：等待输入→处理→输出→循环）

## 关联

- 相关原子笔记：
- 相关 wiki：[[python-迭代器与生成器]]
