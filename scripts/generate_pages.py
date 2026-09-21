#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate wiki pages for diff package from the Python tutorial source.
Output files go to diff/20260922_Python教程_尚硅谷_ingest/pages/wiki/
"""
import os

BASE = r'C:\Users\HP\Documents\llm_wiki\llm-wiki\diff\20260922_Python教程_尚硅谷_ingest\pages\wiki'
SOURCE = r'[[raw/tutorials/Python教程/20260921_Python教程_尚硅谷]]'
TODAY = '2026-09-21'

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def write_file(path, content):
    ensure_dir(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def concept_page(title, tags, content, parent_section=None):
    """Generate a concept wiki page."""
    yaml = f"""---
title: {title}
kind: concept
status: 未读
understanding_level: 1
need_practice: true
last_review: {TODAY}
source: "{SOURCE}"
source_type: tutorial
tags:
  - python
  - {" ".join(tags)}
---

"""
    return yaml + content

def comparison_page(title, tags, content):
    yaml = f"""---
title: {title}
kind: comparison
status: 未读
understanding_level: 1
need_practice: true
last_review: {TODAY}
source: "{SOURCE}"
source_type: tutorial
tags:
  - python
  - {" ".join(tags)}
---

"""
    return yaml + content

def entity_page(title, tags, content):
    yaml = f"""---
title: {title}
kind: entity
status: 未读
understanding_level: 1
need_practice: true
last_review: {TODAY}
source: "{SOURCE}"
source_type: tutorial
tags:
  - python
  - {" ".join(tags)}
---

"""
    return yaml + content

def practice_page(title, tags, content):
    yaml = f"""---
title: {title}
kind: practice
status: 未读
understanding_level: 1
need_practice: true
last_review: {TODAY}
source: "{SOURCE}"
source_type: tutorial
tags:
  - python
  - {" ".join(tags)}
---

"""
    return yaml + content

# ============================================================
# CONCEPT PAGES (22 pages)
# ============================================================

pages = []

# 1. 变量与常量
pages.append(('concepts/变量与常量.md', concept_page(
    '变量与常量', ['变量', '常量', '赋值', '标识符'],
    f"""## 变量

变量是数据的"代号"，它可以和数据建立绑定关系。语法为`变量名 = 值`。在 Python 中，变量的创建与赋值是同时完成的，变量名必须立即与某个值建立绑定关系{SOURCE}#2. 变量与常量。

```python
name = '张三'
age = 18
weight = 65.2
```

> [!warning]
> 📢 **注意：** 变量名不需要加引号！且变量无类型，数据有类型（如`a = 10`，`a`没有类型，但`a`所关联的数据`10`是整型）。{SOURCE}#2.1. 变量

## 常量

在程序中一旦被赋值就**不希望**被修改的量。Python 中没有强制的常量机制，一般约定使用**全大写**变量名来表示常量{SOURCE}#2.3. 常量。

```python
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
```

当强制对常量进行修改时，最终也能改掉，但要自觉不改，这是 Python 程序员之间的约定{SOURCE}#2.3. 常量。

## 标识符命名规则

标识符是程序中可以自己起的名字（变量名、函数名、类名等），命名规则如下{SOURCE}#2.2. 标识符命名规则：

1. 只能包含数字、字母、下划线，且**不能**以数字开头，**不能**包含空格。
2. 区分大小写（Name 和 name 是两个不同的标识符）。
3. **不能**使用关键字（`False`、`None`、`True`、`and`、`as`、`assert`、`async`、`await`、`break`、`class`、`continue`、`def`、`del`、`elif`、`else`、`except`、`finally`、`for`、`from`、`global`、`if`、`import`、`in`、`is`、`lambda`、`nonlocal`、`not`、`or`、`pass`、`raise`、`return`、`try`、`while`、`with`、`yield`）。
4. 尽量**不要**与内置函数同名。
5. 追求简洁清晰，具有描述性。

💡 Python 中推荐使用『蛇形（snake_case）』写法，如`user_name`。

## 几个关键点

- `age = 18` 中，等号表示将右侧的值与左侧的变量建立绑定关系，称为"赋值语句"。
- Python 中变量创建与赋值同时完成，出现变量时必须立即与某个值绑定。
"""
)))

# 2. 数据类型
pages.append(('concepts/数据类型.md', concept_page(
    '数据类型', ['int', 'float', 'str', '类型'],
    f"""## 概述

数据都有自己所属的**数据类型**。三种最常见的数据类型{SOURCE}#5. 数据类型：

| 类型名称 | 英文名 | 举例 | 说明 |
| --- | --- | --- | --- |
| **整型** | `int` | `5`, `-3`, `0`, `2025` | 整数（不带小数点的数） |
| **浮点型** | `float` | `3.14`, `-0.01` | 带小数点的数 |
| **字符串** | `string` | `"Hello"`, `'Python'` | 文本，要用引号包起来 |

> [!tip]
> 📋 **备注**：数据类型不只上述这三种，还有很多种，其他数据类型会在后续章节中逐步讲解。

## 查看数据类型

通过`type()`可以查看数据类型，`type()`返回当前数据的具体类型{SOURCE}#5.2. 查看数据类型。

```python
result1 = type('张三')  # <class 'str'>
result2 = type(18)     # <class 'int'>
result3 = type(72.5)   # <class 'float'>
```

> [!warning]
> 📢 **注意：** 在 Python 中：变量无类型，数据有类型。

## 整型（int）

所谓整型就是没有小数点的数字，Python 中的整型可以是**任意大小**的整数，包括负整数{SOURCE}#5.3. 整型。

```python
num1 = 10_000_000  # 使用下划线分组，使其更清晰易读（Python3.6+）
print(num1)  # 10000000
```

> [!NOTE]
> Python 对超大整数转换字符串的长度有限制（默认 4300 位），但整数本身可以任意大，可以进行数学运算。

## 浮点型（float）

所谓浮点型，就是带小数点的数字{SOURCE}#5.4. 浮点型。

```python
weight = 65.2
balance = 1425.58
speed_of_sound = 3.4e+2  # 科学计数法
```

## 字符串（str）

字符串是由"字符"组成的"串"，属于文本类型{SOURCE}#5.5. 字符串。

```python
message1 = '尚硅谷'
message2 = "尚硅谷"
message3 = '''多行字符串'''
message4 = """也可以多行"""
```

> [!warning]
> 📢 **注意：** 字符串必须要放到引号中，使用单引号、双引号、三个单引号、三个双引号都可以，但必须是英文的引号。
"""
)))

# 3. 运算符
pages.append(('concepts/运算符.md', concept_page(
    '运算符', ['算术', '赋值', '比较', '布尔', '逻辑'],
    f"""## 算数运算符

常用的算数运算符{SOURCE}#7.1. 算数运算符：

| 运算符 | 含义 | 示例 |
| --- | --- | --- |
| `+` | 加 | `9 + 7` → `16` |
| `-` | 减 | `7 - 2` → `5` |
| `*` | 乘 | `3 * 4` → `12` |
| `/` | 除 | `9 / 3` → `3.0` |
| `//` | 取整 | `9 // 6` → `1` |
| `%` | 取余 | `9 % 6` → `3` |
| `**` | 指数 | `2 ** 3` → `8` |

## 赋值运算符

| 运算符 | 示例 | 等价于 |
| --- | --- | --- |
| `+=` | `age += 1` | `age = age + 1` |
| `-=` | `age -= 1` | `age = age - 1` |
| `*=` | `price *= discount` | `price = price * discount` |
| `/=` | `pay /= 5` | `pay = pay / 5` |
| `//=` | `apple //= num` | `apple = apple // num` |
| `%=` | `seconds %= minutes` | `seconds = seconds % minutes` |
| `**=` | `a **= b` | `a = a ** b` |

## 比较运算符

| 运算符 | 含义 | 示例 |
| --- | --- | --- |
| `==` | 等于 | `a == b` |
| `!=` | 不等于 | `a != b` |
| `>` | 大于 | `a > b` |
| `<` | 小于 | `a < b` |
| `>=` | 大于等于 | `a >= b` |
| `<=` | 小于等于 | `a <= b` |

> [!NOTE]
> 字符串进行比较时，是依次比较每个字符的 Unicode 编码。

## 布尔类型

布尔类型表示真（`True`）或假（`False`）{SOURCE}#7.4. 布尔类型。

```python
# 自定义的布尔值
is_student = True
is_adult = False

# 通过运算得到的布尔值
result = 5 > 3  # True
```

> [!NOTE]
> 任何数据类型都可以转成布尔值：数字 `0`、空字符串 `''`、空容器等转成 `False`，其余转成 `True`。

## 逻辑运算符

| 运算符 | 含义 | 示例 |
| --- | --- | --- |
| `and` | 与 | `a and b` |
| `or` | 或 | `a or b` |
| `not` | 非 | `not a` |
"""
)))

# 4. 分支语句
pages.append(('concepts/分支语句.md', concept_page(
    '分支语句', ['if', 'elif', 'else', '条件'],
    f"""## 分支语句概述

分支语句根据条件执行不同的代码块{SOURCE}#1. 分支。

## 单分支

```python
age = 20
if age >= 18:
    print('成年人')
```

## 双分支

```python
age = 15
if age >= 18:
    print('成年人')
else:
    print('未成年人')
```

## 多分支

```python
score = 85
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
```

## 嵌套分支

```python
age = 25
gender = '女'
if age >= 18:
    if gender == '女':
        print('成年女性')
    else:
        print('成年男性')
else:
    print('未成年')
```

> [!NOTE]
> Python 没有 switch/case 语句，多分支用 if/elif/else 实现。
"""
)))

# 5. 循环语句
pages.append(('concepts/循环语句.md', concept_page(
    '循环语句', ['while', 'for', 'range', 'break', 'continue'],
    f"""## while 循环

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## for 循环

```python
# 遍历范围
for i in range(5):
    print(i)

# 遍历字符串
for char in 'hello':
    print(char)
```

> [!NOTE]
> for 循环可以遍历任何可迭代对象（字符串、列表、元组、字典等）。

## continue 与 break

- `continue`：跳过本次循环，进入下一次循环。
- `break`：终止整个循环。

```python
for i in range(10):
    if i == 3:
        continue  # 跳过3
    if i == 7:
        break     # 7时终止
    print(i)
```

## 九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i*j}', end='\t')
    print()
```
"""
)))

# 6. 函数
pages.append(('concepts/函数.md', concept_page(
    '函数', ['def', '参数', '返回值', '调用'],
    f"""## 函数的概念

函数是一段可重复使用的代码块，用于完成特定功能。定义函数使用`def`关键字{SOURCE}#1.1. 函数的概念。

```python
def greet(name):
    print(f'你好，{name}！')
```

## 函数的分类

1. **内置函数**：Python 自带的函数，如`print()`、`len()`、`type()`等。
2. **自定义函数**：由程序员自己定义的函数。

## 定义函数

```python
def 函数名(参数1, 参数2):
    """函数说明文档"""
    # 函数体
    return 返回值
```

## 调用函数

```python
greet('张三')  # 输出：你好，张三！
```

## 参数

- **位置参数**：按顺序传入的参数。
- **关键字参数**：使用`参数名=值`的形式传入。
- **默认参数**：定义时给参数指定默认值。
- **可变参数**：使用`*args`接收位置参数，`**kwargs`接收关键字参数{SOURCE}#3. 参数。

## 返回值

函数可以使用`return`语句返回值{SOURCE}#4. 返回值。

```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

> [!NOTE]
> 函数如果没有 return 语句，默认返回 `None`。
"""
)))

# 7. 字符串
pages.append(('concepts/字符串.md', concept_page(
    '字符串', ['str', '格式化', '切片', '方法'],
    f"""## 概述

字符串是由字符组成的序列，可以用单引号、双引号、三个单引号或三个双引号定义{SOURCE}#4. 字符串。

```python
s1 = '尚硅谷'
s2 = "尚硅谷"
s3 = '''多行字符串'''
s4 = """也可以多行"""
```

## 字符串的特点

- 字符串是**不可变**的序列类型。
- 支持索引和切片操作。
- 可以使用各种内置方法进行操作。

## 字符串常用方法

| 方法 | 说明 | 示例 |
| --- | --- | --- |
| `upper()` | 转大写 | `'abc'.upper()` → `'ABC'` |
| `lower()` | 转小写 | `'ABC'.lower()` → `'abc'` |
| `strip()` | 去首尾空格 | `' abc '.strip()` → `'abc'` |
| `split()` | 分割字符串 | `'a,b,c'.split(',')` → `['a','b','c']` |
| `join()` | 拼接字符串 | `'-'.join(['a','b'])` → `'a-b'` |
| `replace()` | 替换 | `'hello'.replace('l','L')` → `'heLLo'` |
| `find()` | 查找子串位置 | `'hello'.find('ll')` → `2` |
| `startswith()` | 判断前缀 | `'hello'.startswith('he')` → `True` |
| `endswith()` | 判断后缀 | `'hello'.endswith('lo')` → `True` |
| `isdigit()` | 判断是否全为数字 | `'123'.isdigit()` → `True` |

## 字符串常用内置函数

| 函数 | 说明 | 示例 |
| --- | --- | --- |
| `len()` | 长度 | `len('hello')` → `5` |
| `max()` | 最大值 | `max('abc')` → `'c'` |
| `min()` | 最小值 | `min('abc')` → `'a'` |
| `sorted()` | 排序 | `sorted('cba')` → `['a','b','c']` |
| `reversed()` | 反转 | `list(reversed('abc'))` → `['c','b','a']` |

## 遍历字符串

```python
for char in 'hello':
    print(char)
```

## 转义字符

| 转义字符 | 含义 |
| --- | --- |
| `\'` | 单引号 |
| `\"` | 双引号 |
| `\\` | 反斜杠 |
| `\n` | 换行 |
| `\t` | 水平制表符 |
| `\r` | 回车 |
"""
)))

# 8. 列表
pages.append(('concepts/列表.md', concept_page(
    '列表', ['list', '增删改查', '切片'],
    f"""## 概述

列表是 Python 中最常用的**可变序列**类型，用方括号`[]`定义，元素之间用逗号分隔{SOURCE}#2. 列表。

```python
names = ['张三', '李四', '王五']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]
empty = []
```

## 定义列表

```python
# 直接定义
nums = [10, 20, 30, 40]

# 动态创建
scores = []
scores.append(90)
```

## 下标（索引值）

列表支持正向索引（从 0 开始）和反向索引（从 -1 开始）{SOURCE}#2.3. 下标（索引值）。

```python
nums = [10, 20, 30, 40]
print(nums[0])   # 10（第一个元素）
print(nums[-1])  # 40（最后一个元素）
```

## 列表的增删改查

| 操作 | 方法 | 示例 |
| --- | --- | --- |
| 增加 | `append()` | `lst.append(5)` |
| 增加 | `insert(位置, 值)` | `lst.insert(0, 1)` |
| 增加 | `extend()` | `lst.extend([6,7])` |
| 删除 | `remove(值)` | `lst.remove(3)` |
| 删除 | `pop(位置)` | `lst.pop(0)` |
| 删除 | `del lst[位置]` | `del lst[1]` |
| 修改 | `lst[位置] = 新值` | `lst[0] = 99` |
| 查询 | `值 in lst` | `3 in lst` → `True` |
| 查询 | `lst.index(值)` | `lst.index(3)` → `1` |

## 列表的常用方法

| 方法 | 说明 |
| --- | --- |
| `append()` | 末尾添加元素 |
| `insert()` | 指定位置插入 |
| `remove()` | 删除指定值（只删第一个） |
| `pop()` | 删除并返回指定位置的元素 |
| `clear()` | 清空列表 |
| `count()` | 统计元素出现次数 |
| `index()` | 查找元素位置 |
| `sort()` | 原地排序 |
| `reverse()` | 原地反转 |
| `copy()` | 浅拷贝 |

## 列表的常用内置函数

| 函数 | 说明 | 示例 |
| --- | --- | --- |
| `len()` | 长度 | `len([1,2,3])` → `3` |
| `max()` | 最大值 | `max([1,3,2])` → `3` |
| `min()` | 最小值 | `min([1,3,2])` → `1` |
| `sum()` | 求和 | `sum([1,2,3])` → `6` |
| `sorted()` | 返回排序后新列表 | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed()` | 返回反转迭代器 | `list(reversed([1,2,3]))` → `[3,2,1]` |

## 列表的循环遍历

```python
nums = [10, 20, 30, 40]
for num in nums:
    print(num)

# 带索引遍历
for i, num in enumerate(nums):
    print(i, num)
```

## 列表特点总结

- 有序、可变、可重复。
- 支持任意类型混合。
- 支持嵌套（列表中的元素可以是列表）。
"""
)))

# 9. 元组
pages.append(('concepts/元组.md', concept_page(
    '元组', ['tuple', '不可变', '解包'],
    f"""## 概述

元组是 Python 中的**不可变序列**类型，用圆括号`()`定义{SOURCE}#3. 元组。

```python
coordinates = (10, 20)
names = ('张三', '李四', '王五')
single = (1,)  # 单元素元组必须有逗号
empty = ()
```

## 定义元组

```python
# 直接定义
tup = (10, 20, 30)

# 不带括号的元组
tup2 = 10, 20, 30
```

## 读取数据

```python
tup = (10, 20, 30)
print(tup[0])   # 10
print(tup[-1])  # 30
```

## 元组不可修改

```python
tup = (10, 20, 30)
# tup[0] = 99  # ❌ TypeError: 'tuple' object does not support item assignment
```

## 元组的常用方法

| 方法 | 说明 |
| --- | --- |
| `count()` | 统计元素出现次数 |
| `index()` | 查找元素位置 |

## 元组的常用内置函数

| 函数 | 说明 |
| --- | --- |
| `len()` | 长度 |
| `max()` | 最大值 |
| `min()` | 最小值 |
| `sum()` | 求和（元素为数字时） |
| `sorted()` | 返回排序后新列表 |
| `reversed()` | 返回反转迭代器 |

## 解包列表或元组传参

```python
def show_info(name, age):
    print(f'{name}, {age}岁')

# 元组解包
info = ('张三', 18)
show_info(*info)  # 张三, 18岁

# 字典解包
data = {'name': '李四', 'age': 20}
show_info(**data)  # 李四, 20岁
```

## 元组特点总结

- 有序、**不可变**、可重复。
- 适用于不应被修改的数据集合。
- 可作为字典的键（因为不可变）。
"""
)))

# 10. 字典
pages.append(('concepts/字典.md', concept_page(
    '字典', ['dict', '键值对', '增删改查'],
    f"""## 概述

字典是 Python 中的**可变映射**类型，用花括号`{}`定义，以键值对（key-value）形式存储数据{SOURCE}#8. 字典。

```python
student = {'name': '张三', 'age': 18, 'score': 90}
empty = {}
```

## 定义字典

```python
# 直接定义
person = {'name': '李四', 'age': 20}

# 使用 dict() 构造
person2 = dict(name='王五', age=25)

# 空字典
empty_dict = dict()
```

## 字典的增删改查

| 操作 | 语法 | 示例 |
| --- | --- | --- |
| 增加/修改 | `d[key] = value` | `d['age'] = 19` |
| 删除 | `del d[key]` | `del d['age']` |
| 删除 | `d.pop(key)` | `d.pop('age')` |
| 删除 | `d.popitem()` | 删除最后一对 |
| 查询 | `d[key]` | `d['name']` → `'张三'` |
| 查询 | `d.get(key)` | `d.get('age', 0)` |
| 查询 | `key in d` | `'name' in d` → `True` |

## 字典的常用方法

| 方法 | 说明 |
| --- | --- |
| `keys()` | 返回所有键 |
| `values()` | 返回所有值 |
| `items()` | 返回所有键值对 |
| `get(key, default)` | 安全获取值 |
| `update()` | 批量更新 |
| `setdefault()` | 设置默认值 |
| `clear()` | 清空字典 |

## 字典的循环遍历

```python
person = {'name': '张三', 'age': 18}

# 遍历键
for key in person:
    print(key)

# 遍历键值对
for key, value in person.items():
    print(f'{key}: {value}')
```

## 字典总结

- 无序（Python 3.7+ 保持插入顺序）、可变、键唯一。
- 键必须是不可变类型（字符串、数字、元组等）。
- 值可以是任意类型。
- 查找效率高（基于哈希表）。
"""
)))

# 11. 集合
pages.append(('concepts/集合.md', concept_page(
    '集合', ['set', '去重', '交集', '并集'],
    f"""## 概述

集合是 Python 中的**可变无序**类型，元素**不重复**，用花括号`{}`或`set()`定义{SOURCE}#7. 集合。

```python
fruits = {'苹果', '香蕉', '橙子'}
empty = set()
```

## 定义集合

```python
# 直接定义（注意：{} 定义的是空字典，不是空集合）
nums = {1, 2, 3, 3, 2}  # {1, 2, 3} 自动去重

# 使用 set() 构造
letters = set('hello')  # {'h', 'e', 'l', 'o'}
```

## 增删改查

| 操作 | 方法 | 说明 |
| --- | --- | --- |
| 增加 | `add()` | 添加单个元素 |
| 增加 | `update()` | 添加多个元素 |
| 删除 | `remove()` | 删除指定元素（不存在时报错） |
| 删除 | `discard()` | 删除指定元素（不存在时不报错） |
| 删除 | `pop()` | 随机删除并返回一个元素 |
| 删除 | `clear()` | 清空集合 |
| 查询 | `x in s` | 判断元素是否在集合中 |

## 集合的数学运算

| 运算 | 方法 | 符号 | 说明 |
| --- | --- | --- | --- |
| 交集 | `s1 & s2` / `intersection()` | `&` | 两个集合共有的元素 |
| 并集 | `s1 | s2` / `union()` | `|` | 两个集合所有元素 |
| 差集 | `s1 - s2` / `difference()` | `-` | 在 s1 但不在 s2 的元素 |
| 对称差集 | `s1 ^ s2` / `symmetric_difference()` | `^` | 只在一个集合中的元素 |

## 集合特点总结

- 无序、可变、元素唯一。
- 主要用于去重和集合运算。
- 支持数学上的集合运算（交、并、差、对称差）。
"""
)))

# 12. 序列切片
pages.append(('concepts/序列切片.md', concept_page(
    '序列切片', ['切片', 'step', '步长'],
    f"""## 概述

切片（slicing）是从序列中提取子序列的操作，适用于字符串、列表、元组等序列类型{SOURCE}#5. 序列的切片操作。

## 基本语法

```python
序列[起始索引:结束索引:步长]
```

- **起始索引**：默认为 0
- **结束索引**：默认为序列长度（不包含该位置）
- **步长**：默认为 1（负数表示反向）

## 示例

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]    # [2, 3, 4]         从索引2到4
nums[:5]     # [0, 1, 2, 3, 4]   前5个
nums[5:]     # [5, 6, 7, 8, 9]   从索引5到最后
nums[:]      # [0,1,...,9]       全部复制
nums[::2]    # [0, 2, 4, 6, 8]   步长为2
nums[::-1]   # [9,8,...,0]       反转
nums[-3:]    # [7, 8, 9]         最后3个
nums[:-3]    # [0,...,6]         除最后3个
```

## 切片特点

- 切片**不会修改原序列**，返回新序列。
- 起始索引包含，结束索引**不包含**。
- 步长为正时从左到右，为负时从右到左。
"""
)))

# 13. 数据类型转换
pages.append(('concepts/数据类型转换.md', concept_page(
    '数据类型转换', ['int', 'str', 'float', '类型转换'],
    f"""## 概述

数据类型转换是把一种类型的数据变成另一种类型{SOURCE}#6. 数据类型转换。

## 常见转换场景

1. 用户输入的内容都是字符串，若需要进行数学运算，必须进行类型转换。
2. 文件写入时，需将其他类型转为字符串。
3. 从数据库读取的内容是字符串，需要转换后才能计算。

## 具体转换方式

| 函数 | 说明 | 示例 |
| --- | --- | --- |
| `int(x)` | 转换为整数 | `int('123')` → `123` |
| `float(x)` | 转换为浮点数 | `float('3.14')` → `3.14` |
| `str(x)` | 转换为字符串 | `str(123)` → `'123'` |
| `bool(x)` | 转换为布尔值 | `bool(0)` → `False` |
| `list(x)` | 转换为列表 | `list('abc')` → `['a','b','c']` |
| `tuple(x)` | 转换为元组 | `tuple([1,2])` → `(1,2)` |
| `set(x)` | 转换为集合 | `set('aab')` → `{'a','b'}` |

> [!NOTE]
> 转换失败会抛出异常，如`int('abc')`会报错。
"""
)))

# 14. 注释
pages.append(('concepts/注释.md', concept_page(
    '注释', ['单行注释', '多行注释', 'docstring'],
    f"""## 概述

注释是对代码的备注和解释，执行时不起任何作用{SOURCE}#3. 注释。

## 注释的作用

1. 提高代码的可读性，辅助理解代码逻辑。
2. 屏蔽暂时不需要的代码。

> [!tip]
> 📢 **注意：** 编写清晰易懂的注释是程序员的基本素养之一。

## 单行注释

在 Python 中`#`后的一行内容被视为注释{SOURCE}#3.3. 单行注释。

```python
# name 是张三的名字
name = '张三'
# age 是张三的年龄
age = 18
```

> [!NOTE]
> Python 官方建议：在`#`和注释内容之间加一个空格，在代码和`#`之间加两个空格。

## 多行注释

多行注释使用一组三引号（单引号或双引号都可以）{SOURCE}#3.4. 多行注释。

```python
"""
这是一段多行注释
可以写多行
"""
```

> [!tip]
> 📢 **注意：** Python 中没有真正的多行注释语法，所谓多行注释的本质其实还是字符串。

## 文件编码注释

文件编码注释写在 Python 文件的首行{SOURCE}#3.5. 文件编码注释。

```python
# coding=utf-8
print('你好啊！')
```

> [!tip]
> 📋 **备注：** 在 Python3 中，可以不写文件编码声明，因为 Python3 默认使用 UTF-8 编码。
"""
)))

# 15. 字符编码
pages.append(('concepts/字符编码.md', concept_page(
    '字符编码', ['ASCII', 'UTF-8', 'GBK', '编码'],
    f"""## 概述

计算机对数据进行**编码**（存储）和**解码**（读取）{SOURCE}#4. 字符编码。

> [!tip]
> 编码与解码必须遵循相同的编码规范，否则会出现乱码。

## 常见编码方式

| 编码 | 说明 | 字符数 |
| --- | --- | --- |
| `ASCII` | 大写字母、小写字母、数字、一些符号 | 128 |
| `ISO 8859-1` | 在 ASCII 基础上扩展，支持西欧语言 | 256 |
| `GB2312` | 中国国家编码标准，收录约 6763 个简体中文常用汉字 | ~6763 |
| `GBK` | 兼容 GB2312，支持简繁体中文和其他汉字 | ~20000+ |
| `UTF-8` | 国际通用编码格式，支持世界所有语言，向下兼容 ASCII | 无上限 |

> [!success]
> ✅ **最佳实践：** 实际开发中，几乎都采用 UTF-8 编码保存文件。

## 编码与解码

- 存储数据时，计算机会进行**编码**。
- 读取数据时，计算机会进行**解码**。

```python
# 编码：字符串 → 字节
text = '你好'
encoded = text.encode('utf-8')  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 解码：字节 → 字符串
decoded = encoded.decode('utf-8')  # '你好'
```

> [!tip]
> 📋 **备注：** 在 Python3 中，字符串默认使用 UTF-8 编码。
"""
)))

# 16. 输入语句
pages.append(('concepts/输入语句.md', concept_page(
    '输入语句', ['input', '用户输入'],
    f"""## 概述

Python 中使用`input()`函数获取用户输入{SOURCE}#9. 输入语句。

```python
name = input('请输入姓名：')
print('你好，' + name)
```

> [!NOTE]
> `input()`获取的内容**全都是字符串类型**，若需要数值需手动转换。

```python
age = int(input('请输入年龄：'))  # 转换为整数
score = float(input('请输入成绩：'))  # 转换为浮点数
```
"""
)))

# 17. 字面量
pages.append(('concepts/字面量.md', concept_page(
    '字面量', ['literal', '常量'],
    f"""## 概述

字面量就是直接写在代码中的"具体值"，即：字面上的含义，一看就能理解{SOURCE}#1. 字面量。

```python
'张三'    # 字符串字面量
18        # 整型字面量
65.2      # 浮点型字面量
True      # 布尔字面量
None      # 空值字面量
```

> [!warning]
> 📢 **注意：** 字符串必须要放到引号中，使用单引号、双引号、三个单引号、三个双引号都可以，但必须是英文的引号。
"""
)))

# 18. 模块
pages.append(('concepts/模块.md', concept_page(
    '模块', ['import', 'module'],
    f"""## 概述

模块是 Python 程序的**基本组织单位**，一个`.py`文件就是一个模块{SOURCE}#1. 模块。

## 模块的分类

1. **标准库模块**：Python 自带的模块，如`os`、`sys`、`math`等。
2. **第三方模块**：由社区开发的模块，如`requests`、`pandas`等。
3. **自定义模块**：程序员自己编写的模块。

## 创建模块

```python
# my_module.py
def say_hello(name):
    return f'你好，{name}！'

PI = 3.14159
```

## 导入模块

```python
# 导入整个模块
import my_module
my_module.say_hello('张三')

# 导入特定函数
from my_module import say_hello
say_hello('张三')

# 导入并重命名
import my_module as mm
mm.say_hello('张三')
```

## `__name__` 变量

```python
# my_module.py
print(__name__)  # 直接运行时输出 '__main__'，被导入时输出模块名
```

> [!NOTE]
> 常用写法：
> ```python
> if __name__ == '__main__':
>     # 测试代码
> ```
"""
)))

# 19. 包
pages.append(('concepts/包.md', concept_page(
    '包', ['package', '导入'],
    f"""## 概述

包是组织模块的**目录结构**，包目录下有一个`__init__.py`文件{SOURCE}#2. 包。

## 包与模块的关系

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

## 包的分类

1. **标准包**：Python 自带的包。
2. **第三方包**：通过 pip 安装的包。
3. **自定义包**：程序员自己创建的包。

## 导入包

```python
# 导入包中的模块
import mypackage.module1

# 从包中导入模块
from mypackage import module1

# 导入子包
from mypackage.subpackage import module3
```

## 创建包

```
项目/
├── __init__.py    # 根包
├── package_a/
│   ├── __init__.py
│   └── module_a.py
└── package_b/
    ├── __init__.py
    └── module_b.py
```
"""
)))

# 20. 异常处理
pages.append(('concepts/异常处理.md', concept_page(
    '异常处理', ['try', 'except', 'raise', '异常'],
    f"""## 错误与异常

- **错误**：语法错误或逻辑错误，需要修改代码。
- **异常**：程序运行过程中出现的异常事件，可以捕获和处理{SOURCE}#1. 错误与异常。

## 异常处理语法

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print('除数不能为零')
except Exception as e:
    # 处理其他异常
    print(f'发生错误：{e}')
else:
    # 没有异常时执行
    print('计算成功')
finally:
    # 无论是否异常都执行
    print('执行完毕')
```

## 完整写法

```python
try:
    # 主逻辑
    pass
except (ErrorType1, ErrorType2) as e:
    # 捕获多种异常
    pass
except Exception:
    # 捕获所有异常
    pass
else:
    # 无异常时
    pass
finally:
    # 清理工作
    pass
```

## 手动抛出异常

```python
raise ValueError('参数不合法')
```

## 异常的传递机制

异常会沿着调用链向上传递，如果未被捕获，最终导致程序终止{SOURCE}#4. 异常的传递机制。

## 自定义异常类

```python
class MyError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

raise MyError('自定义错误')
```
"""
)))

# 21. 迭代器
pages.append(('concepts/迭代器.md', concept_page(
    '迭代器', ['iterator', 'iterable', '__iter__', '__next__'],
    f"""## 可迭代对象（iterable）

可以被`for`循环遍历的对象称为可迭代对象{SOURCE}#1️⃣可迭代对象（iterable）。

常见的可迭代对象：字符串、列表、元组、字典、集合、 range 等。

判断方法：
```python
from collections.abc import Iterable
isinstance('hello', Iterable)  # True
isinstance(123, Iterable)      # False
```

## 迭代器（iterator）

迭代器是**可以记住遍历位置**的对象，具有以下特点{SOURCE}#2️⃣迭代器（iterator）：

1. 从第一个元素开始访问，直到所有元素被访问完。
2. 只能向前，不能后退。
3. 节省内存（惰性求值）。

判断方法：
```python
from collections.abc import Iterator
isinstance(iter('hello'), Iterator)  # True
isinstance('hello', Iterator)        # False
```

## 迭代器的应用

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration
```

## 迭代器的优势

1. **节省内存**：不需要一次性加载所有数据。
2. **延迟计算**：按需生成数据。
3. **统一接口**：所有可迭代对象都可以用迭代器遍历。
"""
)))

# 22. 文件操作
pages.append(('concepts/文件操作.md', concept_page(
    '文件操作', ['open', 'read', 'write', 'with'],
    f"""## 文件的分类

1. **纯文本文件**：用文本编辑器可以正常打开的文件，如`.txt`、`.py`等。
2. **二进制文件**：不能用文本编辑器正常打开的文件，如图片、音频、视频等{SOURCE}#1. 文件的分类。

## 绝对路径 vs 相对路径

- **绝对路径**：从盘符开始的完整路径，如`C:\\Users\\test.py`。
- **相对路径**：相对于当前工作目录的路径，如`test.py`、`./data/test.py`{SOURCE}#2. 绝对路径 vs 相对路径。

## Python 中操作文件的标准流程

1. **创建文件对象**：`f = open('file.txt', 'r')`
2. **操作文件**：读取或写入
3. **关闭文件**：`f.close()`{SOURCE}#3. Python 中操作文件的标准流程。

## 读取文件

```python
# read() 读取全部内容
f = open('test.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

# readline() 读取一行
line = f.readline()

# readlines() 读取所有行，返回列表
lines = f.readlines()

# for 循环遍历文件对象（推荐）
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
```

## 写入文件

```python
# w 模式：覆盖写
f = open('test.txt', 'w', encoding='utf-8')
f.write('Hello, World!')
f.close()

# x 模式：创建写（文件已存在则报错）
f = open('test.txt', 'x', encoding='utf-8')

# a 模式：追加写
f = open('test.txt', 'a', encoding='utf-8')
f.write('\\nNew line')
f.close()
```

## 关于 with

使用`with`语句可以自动关闭文件，推荐方式{SOURCE}#5. 关于with。

```python
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 自动关闭文件
```

## 组合模式

| 模式 | 说明 |
| --- | --- |
| `rt` | 只读文本模式 |
| `wt` | 只写文本模式 |
| `xt` | 创建写文本模式 |
| `at` | 追加写文本模式 |
| `rb` | 只读二进制模式 |
| `wb` | 只写二进制模式 |
| `rt+` | 读写文本模式 |
| `wt+` | 写读文本模式 |

## flush 方法

```python
f = open('test.txt', 'w')
f.write('Hello')
f.flush()  # 强制刷新缓冲区
```
"""
)))

# ============================================================
# COMPARISON PAGES (6 pages)
# ============================================================

pages.append(('comparisons/编译型语言-vs-解释型语言.md', comparison_page(
    '编译型语言 vs 解释型语言', ['编译', '解释', '语言'],
    f"""## 概述

对于高级语言，根据其转换成二进制指令过程的不同，可将其分为**编译型**和**解释型**{SOURCE}#4. 『编译型语言』与『解释型语言』。

## 编译型语言

将程序翻译成计算机能理解的二进制内容，并且通常会**生成一个可执行文件**，例如 Windows 系统上生成的可执行文件是`.exe`文件{SOURCE}#4.1. 编译型语言。

**特点**：
- 优势：同一运行平台，代码只需编译一次，且执行效率高。
- 劣势：跨平台性差，大型项目编译时间较长，开发效率略低。

## 解释型语言

将程序一句一句地翻译为计算机可以执行的指令，整个过程通常**不生成可执行文件**{SOURCE}#4.2. 解释型语言。

**特点**：
- 优势：跨平台性好，无需编译，开发调试灵活高效。
- 劣势：每次运行都需要解释，执行效率较低。

## 二者对比

| | **编译型语言** | **解释型语言** |
| --- | --- | --- |
| **举例** | C、C++、Go、Rust 等 | Python、JavaScript、Ruby 等 |
| **执行流程** | 运行前把所有程序一次性翻译成机器码，并生成可执行文件 | 运行时靠对应的解释器，把代码一句一句翻译成机器码执行 |
| **是否生成可执行文件** | 是，一次编译多处运行 | 否，每次都要靠解释器翻译后再运行 |
| **运行速度** | 快 | 慢 |
| **是否跨平台** | 否，需要针对平台编译 | 是，只要该平台下有解释器就能运行 |
| **适合场景** | 系统底层、性能要求较高的场景 | 脚本、数据分析、AI 应用、Web 开发等 |
"""
)))

pages.append(('comparisons/while-循环-vs-for-循环.md', comparison_page(
    'while 循环 vs for 循环', ['while', 'for', '循环'],
    f"""## 概述

Python 中有两种循环语句：`while`循环和`for`循环{SOURCE}#2. 循环。

## while 循环

适用于**未知循环次数**的场景，只要条件为真就持续执行{SOURCE}#2.1. while 循环。

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

## for 循环

适用于**已知可迭代对象**的场景，遍历序列中的每个元素{SOURCE}#2.2. for 循环。

```python
for i in range(10):
    print(i)

for char in 'hello':
    print(char)
```

## 对比 while 与 for

| | **while 循环** | **for 循环** |
| --- | --- | --- |
| **适用场景** | 循环次数未知，依赖条件控制 | 循环次数已知，遍历序列 |
| **语法** | `while 条件:` | `for 变量 in 序列:` |
| **灵活性** | 更灵活，可以任意条件终止 | 更简洁，自动处理迭代 |
| **风险** | 条件永远为真时会死循环 | 不会出现死循环 |
| **典型用法** | 等待用户输入、游戏主循环 | 遍历列表、range、字符串 |
"""
)))

pages.append(('comparisons/浅拷贝-vs-深拷贝.md', comparison_page(
    '浅拷贝 vs 深拷贝', ['拷贝', 'copy', '深拷贝', '浅拷贝'],
    f"""## 为什么要拷贝？

赋值语句`b = a`只是让`b`指向和`a`一样的对象，如果指向的是可变对象，通过`b`修改后，`a`访问到的数据也会变化{SOURCE}#10. 浅拷贝 vs 深拷贝。

```python
nums1 = [10, 20, 30, 40]
nums2 = nums1
nums2[3] = 99
print(nums1[3])  # 99（影响了原列表）
```

## 浅拷贝

浅拷贝会创建一个新的外层容器，但内部的元素仍然引用原来的对象{SOURCE}#10.3. 浅拷贝。

```python
import copy
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99
print(nums1[3])  # 40（外层不受影响）
```

**浅拷贝存在的问题**：嵌套数据仍然是共享的，修改嵌套数据会互相影响。

```python
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)
nums2[3][0] = 99
print(nums1[3][0])  # 99（内层受影响！）
```

## 深拷贝

深拷贝创建一个新的外层容器，同时对内部所有**可变对象**进行递归复制（不可变对象不复制，继续引用）{SOURCE}#10.4. 深拷贝。

```python
import copy
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99
print(nums1[3][0])  # 40（完全独立）
```

## 对比

| | **直接赋值** | **浅拷贝** | **深拷贝** |
| --- | --- | --- | --- |
| **外层容器** | 共享 | 新建 | 新建 |
| **内层元素** | 共享 | 共享引用 | 递归复制 |
| **嵌套修改影响** | 影响原对象 | 影响原对象 | 不影响 |
| **性能** | 最快 | 中等 | 最慢 |
| **内存占用** | 最小 | 中等 | 最大 |
"""
)))

pages.append(('comparisons/元组-vs-列表.md', comparison_page(
    '元组 vs 列表', ['tuple', 'list', '对比'],
    f"""## 概述

元组和列表都是 Python 中的序列类型，但有一个关键区别：元组**不可变**，列表**可变**{SOURCE}#3.10. 元组 VS 列表。

## 对比

| 特性 | **列表** | **元组** |
| --- | --- | --- |
| **定义符号** | `[]` | `()` |
| **可变性** | 可变（可增删改） | 不可变 |
| **性能** | 较慢 | 较快 |
| **内存占用** | 较大 | 较小 |
| **可作字典键** | 否 | 是（元素均为不可变类型时） |
| **适用场景** | 需要修改的数据集合 | 不应被修改的数据集合 |

## 列表示例

```python
nums = [10, 20, 30]
nums.append(40)  # ✅ 可以修改
nums[0] = 99     # ✅ 可以修改
```

## 元组示例

```python
coords = (10, 20, 30)
# coords.append(40)  # ❌ TypeError
# coords[0] = 99     # ❌ TypeError
```
"""
)))

pages.append(('comparisons/多进程-vs-多线程.md', comparison_page(
    '多进程 vs 多线程', ['进程', '线程', '并发', '并行'],
    f"""## 核心概念

### 并发 vs 并行

- **并发**：CPU 将多个任务交替执行，同一时刻只执行一个任务，但高频切换让多个任务"同时"推进{SOURCE}#1️⃣并发 vs 并行。
- **并行**：依赖多个 CPU 或多核 CPU，同一时刻每个核心执行不同任务，真正同时执行。

### 进程 vs 线程

- **进程**：操作系统进行资源分配的基本单位，每个进程有独立的内存空间{SOURCE}#3️⃣进程 vs 线程。
- **线程**：进程内部的执行单元，是 CPU 调度的基本单位，同一进程内的线程共享进程资源。

## 对比

| 特性 | **多进程** | **多线程** |
| --- | --- | --- |
| **内存空间** | 独立 | 共享 |
| **通信方式** | 复杂（Queue、Pipe等） | 简单（共享变量） |
| **开销** | 大 | 小 |
| **GIL 影响** | 不受影响 | 受 GIL 限制 |
| **稳定性** | 一个崩溃不影响其他 | 一个崩溃可能导致全部 |
| **适用场景** | CPU 密集型任务 | I/O 密集型任务 |

## GIL（全局解释器锁）

CPython 中，同一时刻只有一个线程在执行 Python 字节码{SOURCE}#15. GIL 全局解释器锁。

> [!warning]
> GIL 使得多线程在 CPU 密集型任务中无法真正实现并行，但对 I/O 密集型任务影响较小。

## 如何选择？

- **CPU 密集型**：优先使用多进程。
- **I/O 密集型**：优先使用多线程或协程。
- **需要简单通信**：多线程更方便。
- **需要隔离性**：多进程更安全。
"""
)))

pages.append(('comparisons/绝对路径-vs-相对路径.md', comparison_page(
    '绝对路径 vs 相对路径', ['路径', '文件'],
    f"""## 概述

文件路径有两种表示方式：绝对路径和相对路径{SOURCE}#2. 绝对路径 vs 相对路径。

## 绝对路径

从盘符开始的完整路径{SOURCE}#1️⃣绝对路径：

```python
# Windows
path = r'C:\\Users\\test.py'
# Linux/Mac
path = '/home/user/test.py'
```

## 相对路径

相对于当前工作目录的路径{SOURCE}#2️⃣相对路径：

```python
# 当前目录下的文件
path = 'test.py'
# 上一层目录
path = '../config.ini'
# 子目录
path = 'data/result.txt'
```

## 对比

| | **绝对路径** | **相对路径** |
| --- | --- | --- |
| **定义** | 从盘符/根目录开始的完整路径 | 相对于当前工作目录的路径 |
| **可移植性** | 差（依赖具体路径） | 好（随项目移动） |
| **清晰度** | 明确 | 依赖当前目录 |
| **适用场景** | 固定位置的文件 | 项目内部文件 |
"""
)))

# ============================================================
# ENTITY PAGES (3 pages)
# ============================================================

pages.append(('entities/Python.md', entity_page(
    'Python', ['语言', '开源', '解释型'],
    f"""## 概述

Python 是一门广泛使用的高级编程语言，由 Guido van Rossum 于 1989 年圣诞节期间开始编写，1991 年发布第一个公开版本{SOURCE}#1.1. Python 的起源。

## 起源

Python 的作者 Guido van Rossum 来自荷兰（国内爱称：龟叔），拥有数学与计算机背景。他发现用 C、Fortran 等语言写程序太费劲，而 Shell 虽然轻松，但功能却很有限。以他喜爱的喜剧《Monty Python's Flying Circus》为灵感，命名为"Python"{SOURCE}#1.1. Python 的起源。

> [!NOTE]
> Python 的设计哲学是"优雅、明确、简单"，提倡：最好只有一种方法来做一件事。

## 特点

**优点**：
- 简洁直观的开发体验
- 丰富强大的框架生态
- 与底层语言高效协作
- 社区活跃且人才充足
- 业内大厂 + 主流推动

**缺点**：
- 执行速度较慢（解释型语言）
- 内存消耗较大
- 全球化问题（GIL）

## 为何 AI 领域广泛使用 Python？

1. 简洁直观的开发体验。
2. 丰富强大的框架生态（TensorFlow、PyTorch 等）。
3. 与底层语言高效协作。
4. 社区活跃且人才充足。
5. 业内大厂 + 主流推动{SOURCE}#1.3. 为何 AI 领域广泛使用 Python ？。

## 版本历史

- 1991年：Python 0.9.0 发布
- 1994年：Python 1.0 正式发布
- 2000年：Python 2.0 发布
- 2008年：Python 3.0 发布（与 Python 2 不兼容）
- 2020年：Python 2 官方停止维护
- 2024年：Python 3.13 发布
"""
)))

pages.append(('entities/PyCharm.md', entity_page(
    'PyCharm', ['IDE', '编辑器', 'JetBrains'],
    f"""## 概述

PyCharm 是 JetBrains 公司开发的 Python 集成开发环境（IDE），集成了代码编写、分析、编译、调试等多种功能{SOURCE}#2.3. 安装 PyCharm。

> [!NOTE]
> PyCharm 官方地址：https://www.jetbrains.com/pycharm/download

## 版本选择

PyCharm 目前没有专业版和社区版之分，现在的叫法是**完整版**（也叫**统一版**），包含付费功能 + 免费功能，付费功能可以免费试用 30 天{SOURCE}#2.3. 安装 PyCharm。

## 常用快捷键

| 快捷键 | 对应操作 |
| --- | --- |
| `Ctrl + /` | 行注释（可选中多行） |
| `Ctrl + Alt + L` | 代码格式化 |
| `Ctrl + C` | 复制当前行 / 复制选定的代码 |
| `Ctrl + D` | 重复当前行 / 重复选定的代码 |
| `Ctrl + Z` | 撤销 |
| `Ctrl + Y` | 删除当前行 / 反撤销(重做) |
| `Ctrl + X` | 剪切当前行 / 剪切选定的代码 |
| `Shift + Enter` | 换行（光标不在结尾处也可换行） |
"""
)))

pages.append(('entities/ Guido-van-Rossum.md', entity_page(
    'Guido van Rossum', ['创始人', 'Python', '荷兰'],
    f"""## 概述

Guido van Rossum 是 Python 编程语言的创始人，来自荷兰，被中国开发者亲切地称为"龟叔"{SOURCE}#1.1. Python 的起源。

## 背景

- 拥有数学与计算机背景。
- 发现用 C、Fortran 等语言写程序太费劲，而 Shell 虽然轻松但功能有限。
- 1989 年圣诞节开始编写 Python 解释器。
- 以喜爱的喜剧《Monty Python's Flying Circus》为灵感，命名为"Python"。

## Python 设计哲学

"优雅、明确、简单"，提倡：最好只有一种方法来做一件事{SOURCE}#1.1. Python 的起源。

> [!NOTE]
> Python 第一个公开版本于 1991 年问世，如今已成为全球最受欢迎的编程语言之一。
"""
)))

# ============================================================
# PRACTICE PAGES (2 pages)
# ============================================================

pages.append(('practice/搭建-Python-开发环境.md', practice_page(
    '搭建 Python 开发环境', ['安装', 'Python', 'PyCharm'],
    f"""## 任务目标

在 Windows 系统上安装 Python 解释器和 PyCharm IDE，并配置基本开发环境。

## 步骤一：安装 Python 解释器{SOURCE}#2.1. 安装 Python 解释器

1. 进入官网 https://www.python.org/downloads/，点击 Downloads，选择对应的操作系统。
2. 选择版本（建议使用 Python 3.13+），点击下载。
3. 双击下载好的文件，以管理员身份运行安装程序。
4. 保持默认设置，点击 Next。
5. 修改安装路径（可选），点击 Install 开始安装。
6. **强烈建议**点击"Disable path length limit"禁用系统路径长度限制。
7. 检查安装是否成功：同时按下 Win + R，输入 `cmd`，回车，输入`python --version`。

## 步骤二：安装 PyCharm{SOURCE}#2.3. 安装 PyCharm

1. 进入官网 https://www.jetbrains.com/pycharm/download/，点击下载完整版安装包。
2. 以管理员身份运行安装包，点击下一步。
3. 修改安装目录（可选），点击下一步。
4. 勾选安装选项（如桌面快捷方式），点击下一步。
5. 点击安装。
6. 安装完成。

## 步骤三：创建项目{SOURCE}#2.4. 设置 PyCharm

1. 打开 PyCharm，点击"新建项目"。
2. 设置项目名称、项目路径、解释器类型和 Python 版本。
3. 点击创建。

## 步骤四：运行 Python 程序

三种运行方式{SOURCE}#3. 运行 Python 程序的几种方式总结：

### 命令行模式
```
python  # 进入交互模式
print(100)
exit()  # 退出
```

### 脚本模式
```bash
python test.py
```

### IDE 模式
在 PyCharm 中右键 → Run。
"""
)))

pages.append(('practice/创建-模块与包.md', practice_page(
    '创建模块与包', ['模块', '包', '导入'],
    f"""## 任务目标

学习创建 Python 模块和包，掌握正确的导入方式。

## 步骤一：创建模块{SOURCE}#1.3. 创建模块

新建一个 Python 文件`mymath.py`：
```python
# mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

if __name__ == '__main__':
    print(add(1, 2))
```

## 步骤二：导入模块{SOURCE}#1.4. 导入模块

```python
# 方式1：导入整个模块
import mymath
print(mymath.add(3, 5))

# 方式2：导入特定函数
from mymath import add
print(add(3, 5))

# 方式3：导入并重命名
import mymath as m
print(m.subtract(10, 3))

# 方式4：导入所有（不推荐）
from mymath import *
```

## 步骤三：创建包{SOURCE}#2.4. 创建包

```
myproject/
├── __init__.py
├── math_ops/
│   ├── __init__.py
│   └── operations.py
└── string_ops/
    ├── __init__.py
    └── operations.py
```

## 步骤四：导入包{SOURCE}#2.5. 导入包

```python
# 导入包中的模块
import myproject.math_ops.operations as ops
print(ops.add(1, 2))

# 从包中导入模块
from myproject import math_ops
```

## 注意事项

1. 包的目录中必须有`__init__.py`文件（Python 3.3+ 可选，但建议保留）。
2. Windows 中使用 multiprocessing 必须加上`if __name__ == '__main__':`判断。
3. 避免模块名与标准库模块同名。
"""
)))

# ============================================================
# WRITE ALL FILES
# ============================================================
for rel_path, content in pages:
    full_path = os.path.join(BASE, rel_path)
    write_file(full_path, content)
    print(f'Created: {rel_path}')

print(f'\nTotal pages created: {len(pages)}')
