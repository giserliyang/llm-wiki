---
title: Python 函数
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 函数
related_notes: []
related_wiki:
  - "Python"
  - "Python 基础语法"
---

# Python 函数

## 摘要

函数是组织好的、可重复使用的、用于执行特定任务的代码块。Python 中函数分为内置函数、模块提供的函数、自定义函数三类 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门]]。

## 核心内容

### 函数的概念与分类

- **函数**：组织好的、可重复使用、用于执行特定任务的代码块 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##1.1. 函数的概念]]。
- 比喻：如同智能家居中的「场景」，提前配置好操作，需要时呼唤名字即可执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##1.1. 函数的概念]]。
- **分类**：① 内置函数（如 `print()`、`len()`）② 模块提供的函数 ③ 自定义函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##1.2. Python 中函数的分类]]。

### 定义与调用

**定义函数：**

```python
def 函数名():
    函数体
```

> [!warning]
> 函数必须先定义再调用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##2.2. 调用函数]]。
> 函数定义后只是告诉 Python 存在该函数，函数体不会执行，需调用后才执行。

**调用函数：**

```python
函数名()
```

### 参数

**形参与实参：**
- **形参（形式参数）**：函数定义时用来接收数据的变量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.2. 实参与形参]]。
- **实参（实际参数）**：调用函数时传递的具体值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.2. 实参与形参]]。

**参数类型：**

| 类型 | 写法 | 说明 |
| --- | --- | --- |
| 位置参数 | `def f(a, b)` | 按顺序传参，个数和顺序必须一致 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.3. 位置参数]] |
| 关键字参数 | `f(a=1, b=2)` | 通过形参名传参，不受顺序限制 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.4. 关键字参数]] |
| 默认参数 | `def f(a, b=10)` | 调用时不传则用默认值；默认参数必须放在必选参数后面 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.6. 参数默认值]] |
| 可变位置参数 | `def f(*args)` | 接收任意数量位置参数，打包成元组 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.7. 可变参数]] |
| 可变关键字参数 | `def f(**kwargs)` | 接收任意数量关键字参数，打包成字典 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.7. 可变参数]] |

> [!tip]
> 位置参数与关键字参数可混用，但位置参数必须写在关键字参数之前 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.4. 关键字参数]]。
> 可通过 `/` 前只能位置参数、`*` 后只能关键字参数来限制传参方式 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.5. 限制传参方式]]。

**特殊的字面量 None：**
- `None` 表示空值/无值，类型是 `NoneType` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.8. 特殊的字面量 None]]。
- 在布尔判断中被当作 `False` 处理 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.8. 特殊的字面量 None]]。
- 不给函数设置返回值，默认返回 `None` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##3.8. 特殊的字面量 None]]。

### 返回值

- 使用 `return` 关键字设置返回值，`return` 同时结束函数运行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##4.2. 如何设置返回值]]。
- 不写 `return` 或 `return` 后无值，函数返回 `None`。

### 作用域

**全局作用域与全局变量：** 整个 `.py` 文件最外层范围，全局变量在整个程序中可访问 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##5.2. 全局作用域 _ 全局变量]]。

**局部作用域与局部变量：** 函数内部范围，局部变量只能在当前函数中使用，函数执行结束后自动销毁 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##5.3. 局部作用域 _ 局部变量]]。

**global 关键字：** 在函数内部使用 `global 变量名` 声明变量为全局变量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##5.4. global 关键字]]。

### 嵌套调用与递归

**嵌套调用：** 一个函数执行过程中调用另一个函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##6. 嵌套调用]]。

**递归调用：** 函数自己调用自己，必须具备终止条件，否则会无限循环 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##7. 递归调用]]。

典型例子：阶乘
```python
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
```

### 函数说明文档（docstring）

写在函数体内、用三引号包裹的文字说明，描述函数功能、参数和返回值，可通过鼠标悬浮查看 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门##8. 函数说明文档]]。

```python
def add(n1, n2):
    """
    计算两个数相加的结果
    :param n1: 第一个数
    :param n2: 第二个数
    :return: 二者相加的结果
    """
    return n1 + n2
```

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 5 章 函数入门]]`

## 关联页面

- [[Python]]
- [[python-基础语法]]
