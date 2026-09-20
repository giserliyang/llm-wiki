---
title: Python 错误与异常
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 异常处理
related_notes: []
related_wiki:
  - "Python"
  - "Python 函数进阶"
---

# Python 错误与异常

## 摘要

**错误（Error）**是语法层面的问题，解释器无法执行，无法通过异常处理机制解决；**异常（Exception）**是程序运行过程中出现的问题，可以通过 `try/except/finally` 机制捕获并处理，让程序继续运行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]]。

## 核心内容

### 错误 vs 异常

| 维度 | 错误（Syntax Error） | 异常（Exception） |
| --- | --- | --- |
| 原因 | 代码语法不正确 | 代码语法正确，但执行时出现问题 |
| 能否通过异常处理解决 | ❌ 不能 | ✅ 可以 |
| 示例 | `if age >= 18`（缺少冒号） | `10 / 0`、`int('hello')` |

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]]

### 常见异常类型

| 异常类 | 触发场景 |
| --- | --- |
| `ZeroDivisionError` | 除数为 0 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `TypeError` | 操作数据类型不正确或不兼容（如 `'10' + 5`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `AttributeError` | 对象没有指定的属性或方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `IndexError` | 索引超出范围（越界）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `NameError` | 使用了不存在的变量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `KeyError` | 访问字典中不存在的 key [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |
| `ValueError` | 值不合法，但类型正确（如 `int('hello')`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]] |

> [!NOTE]
> `BaseException` 是所有异常类的父类，`Exception` 中包含的是开发中常见的业务异常 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##1. 错误与异常]]。
> 异常类继承关系参考官方文档：https://docs.python.org/zh-cn/3.13/library/exceptions.html#exception-hierarchy

### 异常处理

**为什么要处理异常：** 程序运行中出现异常若不被处理，程序会立即崩溃，后续代码无法执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。

**核心规则：**

1. 将可能出现异常的代码放在 `try` 中，处理代码写在 `except` 中 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。
2. `try` 中出现异常，后续代码不执行，自动跳转到 `except` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。
3. `try` 无异常，`except` 不执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。
4. `try-except` 后面的代码继续执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。
5. 直接写裸 `except` 会捕获所有异常，实际开发不推荐 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理]]。

**完整写法（try / except / else / finally）：**

```python
try:
    # 可能出异常的代码
    result = a / b
except ZeroDivisionError:
    # 处理除零异常
    print('0不能作为除数！')
except ValueError:
    # 处理值异常
    print('输入必须是数字！')
except Exception as e:
    # 兜底捕获其他异常
    print(f'程序异常：{e}')
else:
    # try 无异常时执行（可选）
    print('计算成功！')
finally:
    # 无论是否异常都执行（可选）
    print('计算结束！')
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理##8️⃣完整写法]]

> [!NOTE]
> 多个 `except` 从上往下匹配，匹配成功后不再向下匹配 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理##️5️⃣多个 except]]。

**获取异常详细信息：**

```python
except Exception as e:
    print(e)                    # 异常信息
    print(type(e))              # 异常类型
    print(e.args)               # 异常参数
    print(e.__traceback__.tb_lineno)  # 出错行号
```

也可用 `traceback.format_exc()` 格式化完整回溯 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理##6️⃣获取异常的具体信息]]。

**一个 except 捕获多种异常：**

```python
except (ZeroDivisionError, ValueError) as e:
    if isinstance(e, ZeroDivisionError):
        ...
    elif isinstance(e, ValueError):
        ...
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##2. 异常处理##7️⃣一个 except 捕获不同的异常]]

### 手动抛出异常（raise）

当程序遇到不符合预期情况时，可用 `raise` 主动触发异常 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##3. 手动抛出异常]]。

```python
if not (18 <= age <= 120):
    raise ValueError('年龄应该为0~120的整数')
```

### 异常的传递机制

异常未被当前代码块捕获时，会**沿调用链逐层向上传递**给调用者，直到被某一层捕获或程序因未处理异常而终止 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##4. 异常的传递机制]]。

```
test3() → test2() → test1() 抛出 TypeError
              ↑
         test2 的 except 捕获并处理
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##4. 异常的传递机制]]

### 自定义异常类

开发者自定义异常类，表示更具业务含义的异常。规则：类名以 `Error` 结尾，继承 `Exception` 或其子类 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常##5. 自定义异常类]]。

```python
class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__('【校名异常】' + msg)

def check_school_name(name):
    if len(name) > 10:
        raise SchoolNameError('学校名过长')
    else:
        print('学校名合法')

try:
    check_school_name('atguiguuuuuuuuuuuuuuu')
except SchoolNameError as e:
    print(f'程序异常：{e}')
```

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常]]`

## 关联页面

- [[Python]]
- [[python-函数进阶]]
