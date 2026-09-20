---
title: 继承ProcessThread与target参数的两种风格
tags:
  - python
  - 并发编程
  - 进程
  - 线程
status: 未读
understanding_level: 1
need_practice: false
last_review: 2026-09-19
source: "[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##3/10/12/13 节]]"
source_type: tutorial
source_url: ""
aliases:
  - "并发编程两种风格"
---

# 继承ProcessThread与target参数的两种风格

> 本篇拆解自 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##3. 使用 Process 创建进程]]、[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##10. 继承 Process 类创建进程]]、[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##12. 使用 Thread 创建线程]] 和 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##13. 继承 Thread 创建线程]]。（正文里用 `[[原文#章节]]` 带锚点）

## 我的理解

target 函数式风格适合简单任务，继承式面向对象风格适合需要状态持久化的复杂场景。用自己的话说明两种方式的适用边界。

## 要点

1. **target 方式**：`Process(target=func, args=(...))`，函数是纯逻辑，无状态 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##3. 使用 Process 创建进程]]
2. **继承方式**：重写 `run()` 方法，适合需要保存状态（实例属性）的复杂任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##10. 继承 Process 类创建进程]]
3. 两种方式都通过 `start()` 启动，**不要手动调用 `run()`** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##10. 继承 Process 类创建进程]]
4. 继承 Process 时需调用 `super().__init__(**kwargs)` 传递命名等参数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##10. 继承 Process 类创建进程]]
5. 继承 Thread 同理，`run()` 内写逻辑，`start()` 触发执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##13. 继承 Thread 创建线程]]

## 疑问 / 待验证

> [!question] 待补充
> 继承方式中 `__init__` 的参数如何通过 `super()` 传递给父类？kwargs 的作用是什么？

## 实战记录

（完成练习后在此记录你的代码和踩坑过程）

## 关联

- 相关原子笔记：[[进程vs线程vs协程三层并发模型]]
- 相关 wiki：[[python-进程与线程]]
