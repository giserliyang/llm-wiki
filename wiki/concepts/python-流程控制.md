---
title: Python 流程控制
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 流程控制
related_notes: []
related_wiki:
  - "Python"
  - "Python 基础语法"
---

# Python 流程控制

## 摘要

程序执行流程分为三种：**顺序**、**分支**、**循环**。流程控制语句让程序能根据不同条件做出不同选择，或重复执行某些代码 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句]]。

## 核心内容

### 分支语句

分支通过条件判断决定执行哪些代码，有三种形式：

**单分支（if）：**

```python
if 判断条件:
    条件成立时执行的代码
```

> [!warning]
> Python 靠**代码缩进**识别代码范围，条件成立的代码前必须加空格 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##1.1. 单分支]]。

**双分支（if-else）：**

```python
if 判断条件:
    条件成立时执行的代码
else:
    条件不成立时执行的代码
```

**多分支（if-elif-else）：**

```python
if 判断条件1:
    条件1成立时执行的代码
elif 判断条件2:
    条件2成立时执行的代码
else:
    所有条件都不成立时执行的代码
```

> [!NOTE]
> 一个 `if` 只能匹配 1 个 `else`，但可匹配多个 `elif`；`else` 必须在所有 `elif` 之后 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##1.3. 多分支]]。
> 一旦某个分支检测为 `True`，其余 `elif` 和 `else` 不再执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##1.3. 多分支]]。

**嵌套分支：** 在分支内部再写分支 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##1.4. 嵌套分之]]。

### 循环语句

**while 循环：**

```python
while 循环条件:
    条件成立时执行的操作
```

> [!warning]
> 如果条件一直成立就是**死循环**，例如忘记写 `n += 1` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.1. while 循环]]。

执行逻辑：先判断条件 → 成立则执行循环体 → 再次判断 → 直到条件不成立停止。

**for 循环：**

```python
for 临时变量 in 可迭代对象:
    要执行的操作
```

> [!NOTE]
> 「可迭代对象」指能一个个取出来的对象，如 `range()`、字符串、列表等 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.2. for 循环]]。

执行逻辑：从可迭代对象中取出第一个元素 → 赋值给临时变量 → 执行循环体 → 取出下一个元素 → 直到所有元素取完。

**while vs for 对比：**

| 维度 | while | for |
| --- | --- | --- |
| 适用场景 | 循环次数不确定 | 遍历已知集合 |
| 条件控制 | 手动维护循环变量 | 自动迭代 |
| 典型用法 | 等待用户输入、定时任务 | 遍历列表/字符串/range |

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.3. 对比 while 与 for]]

### 循环控制：continue 与 break

- **continue**：跳过本次循环剩余语句，直接进入下一次循环判断 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.6. continue 与 break]]。
- **break**：立即终止整个循环，不再执行后续循环 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.6. continue 与 break]]。

### 嵌套循环

在一个循环内部再写一个或多个循环，常用于处理二维结构数据（如九九乘法表）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.4. 嵌套循环]]。

```python
# 九九乘法表示例
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={item * row}', end='\t')
    print()
```

### print 的 end 参数

`print('内容', end='')` 中的 `end` 控制打印后结尾的内容，默认是换行符 `\n` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句##2.5. 九九乘法表案例]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 4 章 流程控制语句]]`

## 关联页面

- [[Python]]
- [[python-基础语法]]
