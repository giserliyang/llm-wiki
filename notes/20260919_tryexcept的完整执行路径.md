---
title: tryexcepy的完整执行路径
tags:
  - python
  - 异常处理
status: 未读
understanding_level: 1
need_practice: true
last_review: 2026-09-19
source: "[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常]]"
source_type: tutorial
source_url: ""
aliases:
  - "异常处理流程"
---

# tryexcepy的完整执行路径

> 本篇拆解自 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常]]。（正文里用 `[[原文#章节]]` 带锚点）

## 我的理解

画一张流程图：try 正常结束 → else 执行 → finally 执行；try 抛出异常 → 匹配 except → 未匹配则向上传递 → finally 仍执行。用自己的话描述每种情况的触发路径。

## 要点

1. **else 块**：仅在 try 无异常时执行，适合放"依赖 try 成功"的代码 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]
2. **finally 块**：无论是否异常都执行，适合放清理逻辑（关闭文件、释放锁）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]
3. **异常传递**：未被当前层捕获的异常沿调用链向上回溯 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##4. 异常的传递机制]]
4. **自定义异常**：继承 Exception，类名以 Error 结尾，增强业务语义 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##5. 自定义异常类]]
5. **traceback**：`e.__traceback__.tb_lineno` 可获取出错行号，`traceback.format_exc()` 格式化完整栈 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]

## 疑问 / 待验证

> [!question] 待补充
> `raise` 不带参数时重新抛出当前异常，这在 except 块中有何用途？

## 实战记录

- [ ] 写一个登录系统，捕获 FileNotFoundError / ValueError / 自定义异常，输出不同提示

## 关联

- 相关原子笔记：
- 相关 wiki：[[python-错误与异常]]
