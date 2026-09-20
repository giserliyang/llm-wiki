---
title: Python 迭代器与生成器
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 迭代器
  - 生成器
related_notes: []
related_wiki:
  - "Python"
  - "Python 函数进阶"
---

# Python 迭代器与生成器

## 摘要

迭代器通过 `__iter__` 和 `__next__` 协议实现惰性取值，生成器通过 `yield` 关键字以函数形式自动实现迭代器协议。两者均支持延迟计算，适合处理大量数据，显著降低内存占用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器]]。

## 核心内容

### 可迭代对象 vs 迭代器

**可迭代对象（iterable）：** 能被 `for` 循环遍历的对象，拥有 `__iter__` 方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

```python
names = ['张三', '李四', '王五']
print(hasattr(names, '__iter__'))  # True
```

常见可迭代对象：列表、元组、字符串、字典、集合；不可迭代的：整数、函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

**迭代器（iterator）：** 调用 `__iter__()` 得到的对象，拥有 `__iter__` 和 `__next__` 方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

```python
it = iter(names)        # 等价于 names.__iter__()
print(next(it))         # 等价于 it.__next__()
print(next(it))
```

> [!warning]
> 迭代器是一次性的，状态只向前推进，遍历完会被"耗尽"，需要重新调用 `iter()` 创建新迭代器 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。
> 所有元素取完后继续调用 `__next__`，会抛出 `StopIteration` 异常 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

**迭代器协议：** 同时满足以下两个条件就是迭代器：
1. 能被 `iter()` 接受（有 `__iter__`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]
2. 能被 `next()` 逐步取值（有 `__next__`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]

> [!NOTE]
> `iter(迭代器)` 返回迭代器自身，让 for 循环也能遍历迭代器 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

**for 循环的本质：**

```python
# for 循环背后的逻辑
it = iter(names)       # ① 获取迭代器
while True:
    try:
        item = next(it)  # ② 逐个取值
        print(item)
    except StopIteration:  # ③ 耗尽时停止
        break
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]

### 自定义迭代器

实现迭代器协议的两个魔法方法：`__iter__` 和 `__next__` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。

```python
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__index = 0
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__attrs):
            raise StopIteration
        value = self.__attrs[self.__index]
        self.__index += 1
        return value

p1 = Person('张三', 18, '男', '北京昌平')
for item in p1:
    print(item)
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]

### 迭代器的优势

1. **惰性计算**：不会一次性生成所有结果，显著降低内存占用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]]。
2. **大数据场景**：数据量很大且不确定要用多少结果时，推荐用迭代器。

对比示例（斐波那契数列）：

| 实现方式 | 内存行为 |
| --- | --- |
| 迭代器版 `Fibo` | 只保留当前两个值，O(1) 内存 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]] |
| 普通函数版 `fibo()` | 一次性生成完整列表，O(n) 内存 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##1. 迭代器]] |

### 生成器（Generator）

**两个概念：**
- **生成器函数：** 函数体中包含 `yield` 关键字的函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。
- **生成器对象：** 调用生成器函数返回的对象，函数体不会立即执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

> [!tip]
> 只要函数中有 `yield`，不管能否执行到，该函数就是生成器函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

**执行细节：**

1. 调用 `__next__`（或 `next()`）时，生成器函数代码开始执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。
2. 遇到 `yield` 会"暂停"并记录位置，`yield` 后的表达式作为返回值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。
3. 下次调用 `__next__` 从上次暂停处继续，直到再次遇到 `yield` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。
4. 遇到 `return` 抛出 `StopIteration` 异常，`return` 表达式作为异常信息 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

```python
def demo():
    print('开始')
    yield '第1个值'
    a = 200
    yield '第2个值'
    return '结束'

d = demo()          # 不执行函数体，返回生成器对象
print(next(d))      # 打印'开始'，输出'第1个值'
print(next(d))      # 输出'第2个值'
try:
    next(d)
except StopIteration as e:
    print(e)        # 输出'结束'
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]

**生成器是特殊的迭代器：** 通过 `yield` 自动实现了迭代器协议（拥有 `__iter__` 和 `__next__`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

**`yield from`：** 将可迭代对象中的元素依次 yield 出去，替代 `for + yield` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

```python
def demo():
    nums = [10, 20, 30, 40]
    yield from nums   # 等价于 for n in nums: yield n
```

**`send()` 方法：** 让生成器继续执行的同时给上一个 `yield` 传值。`next()` 只能取值，`send()` 既能取值也能送值。第一次调用不能传值（或传 `None`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

```python
def demo():
    print('开始')
    a = yield '第1个值'   # send(666) 会把 666 赋给 a
    print(f'收到: {a}')
    b = yield '第2个值'

d = demo()
print(next(d))          # 开始执行，输出'第1个值'
print(d.send(666))      # 继续执行，a=666，输出'第2个值'
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]

### 生成器表达式

类似列表推导式，用括号创建生成器对象，惰性求值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

```python
# 列表推导式：立即生成全部结果
result1 = [n * 2 for n in [10, 20, 30, 40]]  # [20, 40, 60, 80]

# 生成器表达式：延迟计算，只生成一个对象
result2 = (n * 2 for n in [10, 20, 30, 40])  # <generator object>
```

> [!warning]
> 用 `list()`、`tuple()`、`set()` 可以将迭代器/生成器的内容一次性取出，但如果数据量很大可能会挤爆内存 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器##2. 生成器]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器]]`

## 关联页面

- [[Python]]
- [[python-函数进阶]]
