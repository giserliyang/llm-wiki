---
title: Python 数据容器
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 数据容器
related_notes: []
related_wiki:
  - "Python"
  - "数据类型"
---

# Python 数据容器

## 摘要

数据容器用来存放一组有序的数据（元素），每个元素可以是任意类型，并提供多种操作元素的方法。Python 常用数据容器包括：列表、元组、字符串、集合、字典 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器]]。

## 核心内容

### 列表（list）

**定义：** 用来存放一组**有序**的数据，可对其进行增删改查 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.1. 概述]]。

**定义方式：** 使用方括号 `[]`，元素间用逗号分隔 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.2. 定义列表]]。

```python
list1 = [34, 56, 21]
list2 = ['北京', '尚硅谷']
list3 = [23, '尚硅谷', True, None]  # 可存放不同类型
list4 = [10, 20, [100, 200, 300]]  # 嵌套列表
list5 = []
list6 = list()
```

**下标（索引）：** 正索引从 0 开始，负索引从 -1 开始；超出范围会报错 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.3. 下标（索引值）]]。

**增删改查方法：**

| 操作 | 方法 | 说明 |
| --- | --- | --- |
| 新增 | `append(元素)` | 在尾部追加一个元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 新增 | `insert(下标, 元素)` | 在指定位置插入元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 新增 | `extend(可迭代对象)` | 将可迭代对象内容依次追加到尾部 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 删除 | `pop(下标)` | 删除指定位置元素并返回 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 删除 | `remove(值)` | 删除第一次出现的指定值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 删除 | `clear()` | 清空所有元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 删除 | `del 列表[下标]` | 删除指定位置元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 修改 | `列表[下标] = 值` | 通过下标修改元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |
| 查询 | `列表[下标]` | 通过下标读取元素 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.4. 列表的增删改查]] |

**常用方法：**

| 方法 | 说明 |
| --- | --- |
| `index(值)` | 返回第一次出现的下标 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.5. 列表的常用方法]] |
| `count(值)` | 统计元素出现次数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.5. 列表的常用方法]] |
| `reverse()` | 反转列表（原地修改） [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.5. 列表的常用方法]] |
| `sort(reverse=布尔值)` | 排序（原地修改，默认从小到大） [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.5. 列表的常用方法]] |

**常用内置函数：**

| 函数 | 说明 |
| --- | --- |
| `sorted(容器, reverse=布尔值)` | 返回排序后的新列表（不修改原容器） [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.6. 列表的常用内置函数]] |
| `len(容器)` | 返回元素个数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.6. 列表的常用内置函数]] |
| `max(容器)` | 返回最大值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.6. 列表的常用内置函数]] |
| `min(容器)` | 返回最小值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.6. 列表的常用内置函数]] |
| `sum(容器)` | 对数值元素求和 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.6. 列表的常用内置函数]] |

**遍历方式：** for 循环（最常用）、while 循环、`enumerate()` 同时获取索引和值 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.7. 列表的循环遍历]]。

**一句话总结：** 列表是最常用的数据容器，遇到要"存储一批数据"的场景，首选列表 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##2.8. 列表特点总结]]。

### 元组（tuple）

**定义：** 用来存放一组有序的数据，内容一旦创建就**不可修改**（只读）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.1. 概述]]。

**定义方式：** 使用圆括号 `()`，单元素元组末尾必须加逗号 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.2. 定义元组]]。

```python
t1 = (28, 67, 21)
t2 = ('北京', '尚硅谷')
t3 = (100, True, '你好', None)
t4 = (100,)  # 单元素元组，必须有逗号
t5 = ()
t6 = tuple()
```

**常用方法：** `index(元素)` 返回下标、`count(值)` 统计次数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.5. 元组的常用方法]]。

**不可变的特例：** 元组内若存放可变类型（如列表），该可变类型的内容仍可修改 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.4. 元组不可修改]]。

**一句话总结：** 元组是"只读"容器，保存"不会变的数据"时首选元组 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.9. 元组特点总结]]。

**元组 vs 列表：**

| 区别点 | 列表 | 元组 |
| --- | --- | --- |
| 是否可变 | 可变 | 不可变 |
| 使用场景 | 可变数据集合 | 不变的结构化数据，安全性更高 |
| 语义 | 表示一组可能变化的数据 | 表示一组固定结构的数据 |

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##3.10. 元组 VS 列表]]

### 字符串（str）作为容器

字符串也是有序容器，支持下标访问，但内容不可修改 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.1. 概述]]。

**常用方法：**

| 方法 | 说明 |
| --- | --- |
| `index(字符)` | 返回第一次出现的下标 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.3. 字符串常用方法]] |
| `split(字符)` | 按指定字符分隔，返回列表 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.3. 字符串常用方法]] |
| `replace(旧, 新)` | 替换字符串片段，返回新字符串 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.3. 字符串常用方法]] |
| `count(字符)` | 统计字符出现次数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.3. 字符串常用方法]] |
| `strip()` | 删除两端指定字符，返回新字符串 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.3. 字符串常用方法]] |

**常用内置函数：** `len()` 最常用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##4.4. 字符串常用内置函数]]。

### 序列切片

> [!question] 待补充
> 切片操作（`序列[start:stop:step]`）是本教程第 6 章的重要内容，当前 wiki 尚未收录，待后续补充。

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##5. 序列的切片操作]]

### 集合（set）

> [!question] 待补充
> 集合是无序、不重复的元素集合，本教程第 6 章有介绍，当前 wiki 尚未收录。

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##7. 集合]]

### 字典（dict）

> [!question] 待补充
> 字典是键值对集合，本教程第 6 章有介绍，当前 wiki 尚未收录。

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##8. 字典]]

### 通用操作与总结

所有数据容器共享的内置函数：`max`、`min`、`len`、`sorted`、`sum` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器##9. 数据容器_通用操作]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 6 章 数据容器]]`

## 关联页面

- [[Python]]
- [[数据类型]]
