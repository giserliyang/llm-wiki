---
title: Python
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
related_notes: []
related_wiki:
  - "编译型与解释型语言"
  - "Python 基础语法"
  - "Python 流程控制"
  - "Python 函数"
  - "Python 数据容器"
  - "Python 面向对象"
  - "Python 函数进阶"
  - "Python 错误与异常"
  - "Python 模块与包"
  - "Python 迭代器与生成器"
  - "Python 文件操作"
  - "Python 进程与线程"
  - "Python 协程"
---

# Python

## 摘要

Python 是由 Guido van Rossum 于 1989 年圣诞节开始编写、1991 年首次公开发布的**解释型高级语言**，设计哲学为「优雅、明确、简单」。因其简洁语法、丰富生态和对 AI/数据分析的良好支持，已成为全球最流行的编程语言之一 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python]]。

## 核心内容

### Python 的起源

- 作者：Guido van Rossum（荷兰人，国内爱称「龟叔」），拥有数学与计算机背景 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.1. Python 的起源]]。
- 动机：发现用 C、Fortran 写程序太费劲，Shell 虽轻松但功能有限，希望创造一种**既能像 C 那样全面操控系统，又能像 Shell 一样好上手**的语言 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.1. Python 的起源]]。
- 命名灵感：来自喜剧《Monty Python's Flying Circus》[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.1. Python 的起源]]。
- 第一个公开版本：1991 年 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.1. Python 的起源]]。

### Python 的设计哲学

> [!NOTE]
> "优雅、明确、简单"；提倡「最好只有一种方法来做一件事」[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.1. Python 的起源]]。

### Python 的版本历史

| 年份 | 版本 | 说明 |
| --- | --- | --- |
| 1991 | 0.9.0 | 首个公开版本 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 1994 | 1.0 | 进入正式版阶段 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2000 | 2.0 | Python 2 发布 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2008 | 3.0 | 与 Python 2 **不兼容** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2010 | 2.7 | Python 2.x 最后主版本 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2020 | 2 停维 / 3.9 | Python 2 官方停止维护 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2022 | 3.11 | 平均性能提升 10%-60% [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |
| 2024 | 3.13 | 持续迭代 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.4. Python 的版本]] |

> [!question] 待补充
> Python 2 已于 2020 年停止维护，实际项目中是否还有人在使用？

### 为何 AI 领域广泛使用 Python

1. 简洁直观的开发体验 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.3. 为何 AI 领域广泛使用 Python ？]]。
2. 丰富强大的框架生态（如 TensorFlow、PyTorch 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.3. 为何 AI 领域广泛使用 Python ？]]。
3. 与底层语言高效协作（C/C++ 扩展）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.3. 为何 AI 领域广泛使用 Python ？]]。
4. 社区活跃且人才充足 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.3. 为何 AI 领域广泛使用 Python ？]]。
5. 业内大厂 + 主流推动 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##1.3. 为何 AI 领域广泛使用 Python ？]]。

### Python 的运行方式

- Python 是**解释型语言**：运行时由解释器逐句翻译执行，不生成可执行文件 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 1 章 必备基础知识##4.2. 解释型语言]]。
- 运行方式包括：命令行模式、脚本模式、IDE 模式（如 PyCharm）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python##3. 运行 Python 程序的几种方式总结]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 1 章 必备基础知识]]`
- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 2 章 初识 Python]]`

## 关联页面

- [[编译型与解释型语言]]
