---
title: Python 面向对象
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 面向对象
related_notes: []
related_wiki:
  - "Python"
  - "Python 函数"
---

# Python 面向对象

## 摘要

面向对象是一种以**对象**为中心组织代码的编程思想。对象拥有**属性**和**行为**，类是对象的**模板**，实例化是从类创建对象的过程。本章涵盖类与实例、属性、方法、继承、多态等核心概念 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象]]。

## 核心内容

### 对象与类

**对象：** 拥有**属性**和**行为**的个体，是构成程序世界的基本单位（如：一个人、一辆车、一部手机）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##1.1. 对象]]。

**类（class）：** 描述一类事物的**模板**，规定了一类事物具有的**属性**和**行为** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##1.3. 类]]。

**实例 / 实例对象：** 根据类创建出的具体对象，三者是同一个意思 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##1.4. 实例 VS 实例化]]。

**实例化：** 根据类"制造"出一个对象的过程 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##1.4. 实例 VS 实例化]]。

### 类的定义与实例化

**定义类：**

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
```

- 类名通常采用**大驼峰**命名法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##2.1. 类的定义]]。
- `__init__` 是**初始化方法**，实例化时 Python **自动调用**，用于给实例添加属性 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##2.1. 类的定义]]。
- `self` 是当前正在创建的实例对象，第一个参数必须是 `self` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##2.1. 类的定义]]。

**创建实例：**

```python
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##2.2. 创建实例]]

**访问与修改属性：** 使用 `实例.属性名` 语法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##2.2. 创建实例]]。

```python
print(p1.name)   # 访问
p1.name = '阿三'  # 修改
p1.address = '北京'  # 追加属性
print(p1.__dict__)  # 查看所有属性
```

### 实例属性 vs 类属性

| 维度 | 实例属性 | 类属性 |
| --- | --- | --- |
| 定义方式 | `self.属性名 = 值`（在 `__init__` 中） | 直接在类体中写 `属性名 = 值` |
| 归属 | 每个实例独立一份 | 所有实例共享同一份 |
| 访问方式 | 只能通过**实例**访问 | 可通过**类**或**实例**访问 |
| 用途 | 存储个体特征（name、age） | 存储公共数据（max_age、planet） |

> [!warning]
> `实例.属性名 = 值` 操作只影响实例自身，不会修改类属性 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##3.2. 类属性]]。

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##3. 实例属性、类属性]]

### 实例方法、类方法、静态方法

| 方法类型 | 装饰器 | 第一个参数 | 访问范围 | 典型用途 |
| --- | --- | --- | --- | --- |
| 实例方法 | 无 | `self` | 实例属性、类属性 | 操作实例数据 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##4.1. 实例方法]] |
| 类方法 | `@classmethod` | `cls` | 类属性 | 工厂方法、操作类级别信息 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##4.2. 类方法]] |
| 静态方法 | `@staticmethod` | 无 | 无特殊访问权限 | 与类相关的工具方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##4.3. 静态方法]] |

> [!tip]
> 类方法和静态方法**强烈推荐通过类名调用**以体现语义，通过实例调用也能工作但不推荐 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##4.2. 类方法]][[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##4.3. 静态方法]]。

### 继承

**概念：** 一个类（子类/派生类）继承另一个类（父类/基类）的属性和方法，实现代码复用与扩展 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.1. 基本语法]]。

**语法：**

```python
class Student(Person):  # Student 继承自 Person
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)  # 调用父类初始化
        self.stu_id = stu_id
        self.grade = grade
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.1. 基本语法]]

**方法重写：** 子类定义与父类同名方法，子类方法会覆盖父类方法。可通过 `super()` 调用父类方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.2. 方法重写]]。

**多重继承：** 一个类可同时继承多个父类 `class 子类(父类A, 父类B):` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.4. 多重继承]]。

**MRO（方法解析顺序）：** 通过 `类.__mro__` 可查看属性和方法的查找顺序 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.4. 多重继承]]。

**isinstance() 与 issubclass()：**

| 函数 | 作用 |
| --- | --- |
| `isinstance(obj, Class)` | 判断对象是否为指定类或其子类的实例 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.3. isinstance()和 issubclass()]] |
| `issubclass(Sub, Super)` | 判断一个类是否是另一个类的子类 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##5.3. isinstance()和 issubclass()]] |

### 权限控制

| 权限类型 | 定义方式 | 当前类内部 | 子类内部 | 类外部 |
| --- | --- | --- | --- | --- |
| 公有属性 | `属性名` | ✅ | ✅ | ✅ |
| 受保护属性 | `_属性名` | ✅ | ✅ | ⚠️ 能（不推荐） |
| 私有属性 | `__属性名` | ✅ | ❌ | ❌ |

> [!tip]
> Python 的「私有」并非真正不可访问，是通过**名称改写**实现的（`__idcard` 被改写为 `_Person__idcard`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##6.1. 三种访问权限]]。

**getter / setter（@property）：** 通过装饰器将方法变成像属性一样使用，可加入访问逻辑进行验证 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##6.2. getter 与 setter]]。

```python
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value <= 120:
        self._age = value
    else:
        self._age = 120
```

### 魔法方法

以 `__xxx__` 命名的特殊方法，**不需要手动调用**，Python 会在特定场景自动调用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##7. 魔法方法]]。

| 方法 | 调用时机 |
| --- | --- |
| `__init__(self)` | 实例创建时初始化 |
| `__str__(self)` | `print(对象)` 或 `str(对象)` 时 |
| `__len__(self)` | `len(对象)` 时 |
| `__lt__(self, other)` | `对象1 < 对象2` 时 |
| `__gt__(self, other)` | `对象1 > 对象2` 时 |
| `__eq__(self, other)` | `对象1 == 对象2` 时 |
| `__getattr__(self, item)` | 访问不存在的属性时 |

### object 类

`object` 是所有类的**最终祖先**，所有类都隐式继承自 `object` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##8. object 类]]。

```python
print(issubclass(Person, object))  # True
```

### 多态

**定义：** 不同的对象调用同一个方法名时，表现出不同的行为 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##9. 多态]]。

**标准多态：** 基于继承实现，要求传入对象是某一父类（或其子类）的实例 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##9.2. 标准多态]]。

**鸭子多态（Duck Typing）：** 不检查类型，只要对象有对应方法即可调用——"如果看起来像鸭子，叫起来也像鸭子，那它就是鸭子" [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##9.3. 鸭子多态]]。

```python
def make_sound(animal):
    animal.speak()  # 不关心 animal 是什么类型，只要有 speak 方法就行

make_sound(Dog())   # 汪汪汪！
make_sound(Cat())   # 喵喵喵！
make_sound(Pig())   # 哼哼哼！
```

### 抽象类

抽象类不能被直接实例化，作为"规范"让子类继承并实现抽象方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##10. 抽象类]]。

```python
from abc import ABC, abstractmethod

class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass
```

### 内存模型

- Python 中**变量保存的是引用**（内存地址），数据保存在堆内存中 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##12. 内存分析]]。
- **不可变对象**：重新赋值会创建新对象（int、float、bool、str、tuple、frozenset、None）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##12. 内存分析]]。
- **可变对象**：修改内容不改变地址（list、dict、set、自定义类实例）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象##12. 内存分析]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 7 章 面向对象]]`

## 关联页面

- [[Python]]
- [[python-函数]]
- [[python-基础语法]]
