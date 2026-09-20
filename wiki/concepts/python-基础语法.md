---
title: Python 基础语法
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 语法
related_notes: []
related_wiki:
  - "Python"
  - "数据类型"
---

# Python 基础语法

## 摘要

本节涵盖 Python 编程的基础语法要素：字面量、变量与常量、标识符命名规则、注释和运算符，是学习 Python 编程的第一步 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础]]。

## 核心内容

### 字面量

- 字面量是直接写在代码中的「具体值」，即字面上的含义，一看就能理解，不需要计算或转换 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##1.1. 概述]]。
- 示例：`'张三'`、`18`、`65.2` 都是字面量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##1.2. 写法]]。
- 写在 Python 文件头部的字符串会被自动识别为 docstring（文档字符串），必须用三个双引号 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##1.2. 写法]]。

### 变量与常量

**变量：** 数据的「代号」，可以与数据建立绑定关系，并通过变量名使用或更新数据 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.1. 变量]]。

- 语法：`变量名 = 值`，等号表示将右侧的值与左侧的变量建立绑定关系 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.1. 变量]]。
- Python 中变量的创建与赋值是同时完成的，出现变量时必须立即绑定一个值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.1. 变量]]。
- **关键点：变量无类型，数据有类型** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.1. 变量]]。

**常量：** 一旦赋值就不希望被修改的量。Python 中没有强制的常量机制，约定使用**全大写**变量名表示常量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.3. 常量]]。

```python
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.3. 常量]]

> [!warning]
> 对常量强行赋值也能改掉，但这是违反约定的行为 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.3. 常量]]。

### 标识符命名规则

标识符是给变量、函数、类等起名字的统称 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。

**命名规则：**

1. 只能包含数字、字母、下划线，且**不能以数字开头**，不能包含空格 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。
2. 区分大小写（`Name` 和 `name` 是两个不同的标识符）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。
3. **不能使用关键字**（如 `def`、`class`、`if`、`return` 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。
4. 尽量避免与内置函数同名 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。
5. 简洁清晰，具有描述性 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。

**三种命名风格：**

- 大驼峰（UpperCamelCase）：`UserName`
- 小驼峰（lowerCamelCase）：`userName`
- 蛇形（snake_case）：`user_name` ← **Python 推荐使用** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##2.2. 标识符命名规则]]。

### 注释

注释是对代码的备注和解释，执行时不起任何作用，核心作用是**提高代码可读性**和**屏蔽暂时不需要的代码** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##3.2. 注释的作用]]。

**单行注释：** 使用 `#`，Python 官方建议在 `#` 和内容之间加一个空格 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##3.3. 单行注释]]。

```python
# name 是张三的名字
name = '张三'
```

**多行注释：** 使用三引号（`'''` 或 `"""`），本质是多行字符串 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##3.4. 多行注释]]。

```python
"""
这是一段多行注释
可以换行
"""
```

> [!tip]
> Python 中并没有真正的多行注释语法，多行注释的本质是字符串 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##3.4. 多行注释]]。

**文件编码注释：** 写在文件首行，指定字符编码。Python 3 默认 UTF-8，一般可不写 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##3.5. 文件编码注释]]。

```python
# coding=utf-8
```

### 运算符

**算数运算符：**

| 运算符 | 说明 | 示例 |
| --- | --- | --- |
| `+` | 加法 | `9 + 7` → `16` |
| `-` | 减法 | `7 - 2` → `5` |
| `*` | 乘法 | `3 * 4` → `12` |
| `/` | 除法（浮点） | `9 / 3` → `3.0` |
| `//` | 取整除法 | `9 // 6` → `1` |
| `%` | 取余 | `9 % 6` → `3` |
| `**` | 指数 | `2 ** 3` → `8` |

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.1. 算数运算符]]

**赋值运算符：**

| 运算符 | 等价写法 |
| --- | --- |
| `+=` | `a = a + b` |
| `-=` | `a = a - b` |
| `*=` | `a = a * b` |
| `/=` | `a = a / b` |
| `//=` | `a = a // b` |
| `%=` | `a = a % b` |
| `**=` | `a = a ** b` |

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.2. 赋值运算符]]

**比较运算符：**

`==`、`!=`、`>`、`<`、`>=`、`<=`，同样适用于字符串比较 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.3. 比较运算符]]。

**逻辑运算符：**

`and`、`or`、`not` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.5. 逻辑运算符]]。

**布尔类型：**

- 布尔类型是 `int` 的子类型，底层用 `1` 表示 `True`，用 `0` 表示 `False` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.4. 布尔类型]]。
- 可用 `bool()` 将其他类型转为布尔类型 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础##7.4. 布尔类型]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 3 章 Python 核心基础]]`

## 关联页面

- [[Python]]
- [[数据类型]]
