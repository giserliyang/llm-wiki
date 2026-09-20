---
title: Python 函数进阶
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
  - "Python 函数"
---

# Python 函数进阶

## 摘要

本章在基础函数之上深入讲解：函数作为一等对象的特性、高阶函数（map/filter/reduce/lambda）、列表推导式、浅拷贝与深拷贝的区别，以及闭包和装饰器的核心原理 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶]]。

## 核心内容

### 函数是对象

- 函数本身也是对象（`function` 类的实例），可以赋值给变量、动态添加属性、作为参数传递、作为返回值返回 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##1. 重新认识函数]]。
- 可变对象作为参数传入函数时，函数内部修改会影响外部；不可变对象修改后地址改变，不影响外部 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##1. 重新认识函数]]。

### 多返回值

`return a, b` 会自动打包成元组，支持解包赋值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##2. 函数的多返回值]]。

```python
def calculate(x, y):
    return x + y, x - y  # 实际返回 (res1, res2)

r1, r2 = calculate(10, 20)
```

### 参数打包与解包

| 操作 | 写法 | 说明 |
| --- | --- | --- |
| 打包位置参数 | `*形参名` | 收进元组 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##3. 参数的打包与解包]] |
| 打包关键字参数 | `**形参名` | 收进字典 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##3. 参数的打包与解包]] |
| 解包传参 | `*变量名` / `**变量名` | 拆开元组/字典作为独立参数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##3. 参数的打包与解包]] |

### 高阶函数

当一个函数的**参数是函数**或**返回值是函数**，该函数就是高阶函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##4. 高阶函数]]。

```python
# 参数是函数 → 高阶函数
def caller(f):
    f()

# 返回值是函数 → 高阶函数
def outer():
    def inner():
        print('inner')
    return inner
```

**意义：** 代码复用性高、让函数更灵活通用、是装饰器和闭包的基础 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##4. 高阶函数]]。

### lambda 匿名函数

`lambda 参数: 表达式` — 只能写一行，不能写代码块，结果自动作为返回值返回 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##6. 匿名函数]]。

### 数据处理函数

| 函数 | 功能 | 语法 | 特点 |
| --- | --- | --- | --- |
| `map(func, iterable)` | 对每个元素统一加工 | `map(lambda x: x*2, [1,2,3])` | 延迟执行，返回迭代器，元素数量不变 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##7.1. map 函数]] |
| `filter(func, iterable)` | 按条件过滤元素 | `filter(lambda n: n>30, [10,20,30,40])` | 延迟执行，返回迭代器，元素数量可能变化 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##7.2. filter 函数]] |
| `sorted(iterable, key, reverse)` | 排序返回新列表 | `sorted(nums, key=len, reverse=True)` | 不影响原容器，`key` 可接收函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##7.3. sorted 函数]] |
| `reduce(func, iterable, init)` | 归并计算 | `reduce(lambda a,b: a+b, [1,2,3], 0)` | 需 `from functools import reduce` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##7.4. reduce 函数]] |

### 列表推导式

用一条简洁语句从可迭代对象生成新列表 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##8. 列表推导式]]。

```python
# 基本形式：[表达式 for 变量 in 可迭代对象]
result = [n * 2 for n in [10, 20, 30, 40]]

# 带条件
result = [n * 2 for n in [10, 20, 30, 40] if n > 20]

# 字典推导式
result = {names[i]: scores[i] for i in range(len(names))}

# 集合推导式
result = {n + '!' for n in ['张三', '李四']}
```

### 浅拷贝 vs 深拷贝

| 方式 | 效果 | 嵌套可变对象 |
| --- | --- | --- |
| 直接赋值 `b = a` | 两个变量指向同一对象 | 完全共享 |
| 浅拷贝 `copy.copy(a)` | 外层容器新创建 | **共享**，修改嵌套对象互相影响 |
| 深拷贝 `copy.deepcopy(a)` | 外层容器及所有嵌套可变对象都复制 | **独立**，互不影响 |

> [!warning]
> 深拷贝遇到不可变对象不复制，直接引用；元组中若只含不可变对象，深拷贝无效果 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##10. 浅拷贝 vs 深拷贝]]。

```python
import copy

nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)   # 浅拷贝：外新内共享
nums3 = copy.deepcopy(nums1)  # 深拷贝：内外都新

nums2[3][0] = 99   # nums1[3][0] 也变成 99（浅拷贝问题）
nums3[3][0] = 99   # nums1[3][0] 不受影响（深拷贝安全）
```

### 四种作用域（LEGB 规则）

访问变量时，Python 按以下顺序查找 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##11. 四种作用域]]：

| 优先级 | 作用域 | 说明 |
| --- | --- | --- |
| 1 | **L**ocal（局部） | 函数内部，优先级最高 |
| 2 | **E**nclosing（外层） | 嵌套函数中外层函数的作用域 |
| 3 | **G**lobal（全局） | `.py` 文件最外层 |
| 4 | **B**uilt-in（内建） | Python 预定义名称，优先级最低 |

> `nonlocal` 用于修改 Enclosing 作用域变量；`global` 用于修改 Global 作用域变量。

### 闭包

**定义：** 闭包 = 内层函数 + 被内层函数引用的外层变量，产生条件：① 函数嵌套 ② 内层用了外层变量 ③ 外层返回内层 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##12. 闭包]]。

```python
def outer():
    num = 10
    def inner():
        nonlocal num
        num += 1
        print(num)
    return inner

f = outer()
f()  # 11
f()  # 12
```

**优点：** 能"记住"状态、可以做配置过的函数、实现数据隐藏、是装饰器的基础 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##12.6. 闭包的优点]]。

**缺点：** 理解成本高、内存占用风险、复杂场景用类更清晰 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##12.7. 闭包的缺点]]。

### 装饰器

**定义：** 在不修改原函数代码的前提下，对函数进行增强的工具 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##13. 装饰器]]。

**函数装饰器基本结构：**

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 增强逻辑
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(x, y):
    return x + y
```

**核心规则：**
1. 接收被装饰函数，返回 wrapper 函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##13.1. 函数装饰器]]
2. wrapper 用 `*args, **kwargs` 保证参数兼容
3. wrapper 必须 return 原函数返回值
4. `@decorator` 等价于 `add = decorator(add)`

**带参数的装饰器：** 三层嵌套结构，外层接收配置，中间层接收函数，内层接收参数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##13.1. 函数装饰器]]。

**类装饰器：** 包含 `__call__` 方法的类，调用实例对象时触发 `__call__` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##13.2. 类装饰器]]。

**多个装饰器顺序：** 离函数最近的先工作 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##13.1. 函数装饰器]]。

### 类型注解

- **变量注解：** `变量名: 类型 = 值`，不影响运行，仅提示 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##14.1. 变量类型注解]]。
- **容器注解：** `list[str]`、`dict[str, int]`、`tuple[int, ...]` 等 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##14.1. 变量类型注解]]。
- **函数注解：** `def add(x: int, y: int) -> int:` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##14.2. 函数类型注解]]。

> [!tip]
> 类型注解不影响程序运行，仅供人和工具（IDE、静态检查）使用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶##14. 类型注解 vs 函数类型注解]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶]]`

## 关联页面

- [[Python]]
- [[python-函数]]
