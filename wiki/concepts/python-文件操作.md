---
title: Python 文件操作
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 文件操作
related_notes: []
related_wiki:
  - "Python"
  - "Python 模块与包"
---

# Python 文件操作

## 摘要

文件操作是实际开发中最常用的 I/O 主题之一。本章涵盖文件分类、路径、读取/写入模式、`with` 上下文管理器、目录操作等核心内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作]]。

## 核心内容

### 文件分类

| 类型 | 特点 | 示例 |
| --- | --- | --- |
| 纯文本文件 | 按字符编码规范（如 UTF-8）存储，最终呈现为可直接阅读的文本 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##1. 文件的分类]] | `.txt`、`.py`、`.md`、`.html` |
| 二进制文件 | 不涉及字符编码，按文件格式规范转为二进制存储，需特定软件解析 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##1. 文件的分类]] | `.mp3`、`.mp4`、`.doc`、`.jpg`、`.png` |

### 路径

- **绝对路径：** 从文件系统根目录开始，完整描述位置，如 `D:/demo/test/a.txt` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##2. 绝对路径 vs 相对路径]]。
- **相对路径：** 以当前工作目录为参照，如 `./../a.txt`（`..` 表示上一级目录）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##2. 绝对路径 vs 相对路径]]。

### open 函数与文件模式

**标准流程：** ① 创建文件对象 → ② 操作文件（读写）→ ③ 关闭文件 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]]。

**open 函数参数：**

| 参数 | 说明 |
| --- | --- |
| `file` | 文件路径 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `mode` | 打开模式（见下表）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `encoding` | 字符编码（文本模式必需）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |

**mode 参数：**

| 模式 | 说明 |
| --- | --- |
| `r` | 读取（默认）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `w` | 写入，**先截断（清空）文件** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `x` | 排它性创建，文件已存在则失败 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `a` | 追加写入，文件末尾添加内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `b` | 二进制模式 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `t` | 文本模式（默认）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |
| `+` | 更新模式（可读可写）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##3. Python 中操作文件的标准流程]] |

### 读取文件

**read(size)：** 读取指定字符数或字节数；不传 size 则读取全部（注意内存占用！）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##4. 读取文件]]。

```python
with open('a.txt', 'rt', encoding='utf-8') as file:
    # 每次读取10个字符，直到读完
    while True:
        result = file.read(10)
        if result == '':
            break
        print(result, end='')
```

**readline()：** 读取一行，从上次位置继续，到末尾返回空字符串 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##4. 读取文件]]。

**for 循环遍历文件对象：** 逐行遍历，最简洁的方式 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##4. 读取文件]]。

```python
with open('a.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
```

> [!tip]
> **最佳实践：** 使用 `with` 上下文管理器 + `for` 循环逐行读取，自动关闭文件且对内存友好 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##4. 读取文件]]。

**readlines(hint)：** 一次性读取所有行，返回列表；hint 为可选的字符/字节数提示。**不适合大文件**（一次性加载所有数据到内存）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##4. 读取文件]]。

### with 上下文管理器

**概念：** `with` 用于管理"需要成对出现的操作"（打开/关闭、加锁/解锁等），编码者只管做具体事，"进入"和"离开"由 Python 自动处理 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##5. 关于with]]。

```python
with open('a.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
# with 结束后文件自动关闭
```

**上下文管理器协议：**

- `__enter__()`：with 代码执行**之前**调用，返回值赋给 `as` 后的变量 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##5. 关于with]]。
- `__exit__(exc_type, exc_val, exc_tb)`：with 代码执行**结束后**调用（无论是否异常），返回 `True` 表示异常已被处理，不再抛出 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##5. 关于with]]。

### 写入文件

| 模式 | 说明 |
| --- | --- |
| `w` | 写入，**先清空文件** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##6. 写入文件]] |
| `x` | 排它性创建，文件已存在则失败 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##6. 写入文件]] |
| `a` | 追加，在文件末尾写入内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##6. 写入文件]] |

```python
# w 模式：覆盖写入
with open('b.txt', 'wt', encoding='utf-8') as file:
    file.write('你好')

# a 模式：追加写入
with open('a.txt', 'at', encoding='utf-8') as file:
    file.write('你好')
```

### flush 方法

Python 写入文件时先写入**缓冲区**，不立即落盘。`flush()` 方法可将缓冲区数据立刻写入文件 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##7. `flush`方法]]。

### 组合模式

`+` 表示可读可写，配合 `r/w/a/x` 使用：

| 模式 | 说明 | 文件指针初始位置 |
| --- | --- | --- |
| `rt+` / `r+` | 可读可写 | 文件开头 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]] |
| `wt+` / `w+` | 可读可写，先清空文件 | 文件开头 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]] |
| `xt+` / `x+` | 可读可写，排它性创建 | 文件开头 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]] |
| `at+` / `a+` | 可读可写，追加模式 | **文件末尾** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]] |

**seek(offset, whence)：** 改变文件指针位置 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]]。

- `offset`：偏移量
- `whence`：参考点（`0` 文件开头/`1` 当前位置/`2` 文件末尾，默认 `0`）
- > [!warning]
> 文本模式下不要随意定位中文字符位置，可能破坏文件编码 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##8. 组合模式]]。

```python
with open('a.txt', 'wt+', encoding='utf-8') as file:
    file.write('你好')
    file.seek(0, 0)        # 回到开头
    result = file.read()
    print(result)          # 输出'你好'
```

### 目录操作（os 与 shutil）

| 操作 | 代码 | 说明 |
| --- | --- | --- |
| 创建单级目录 | `os.mkdir(path)` | 目录已存在则报错 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 创建多级目录 | `os.makedirs(path)` | 路径中所有目录都存在才报错 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 删除空目录 | `os.rmdir(path)` | 目录不存在或非空则报错 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 递归删除空目录 | `os.removedirs(path)` | 删除末尾目录后向上尝试删除父目录（直到非空）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 判断路径存在 | `os.path.exists(path)` | 文件或目录存在返回 True [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 判断是否为目录 | `os.path.isdir(path)` | 路径是目录返回 True [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 判断是否为文件 | `os.path.isfile(path)` | 路径是文件返回 True [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 扫描目录 | `os.scandir(path)` | 返回目录下的 Entry 对象迭代器 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 递归遍历目录 | `os.walk(path)` | 按层级递归遍历所有子目录和文件 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |
| 删除非空目录 | `shutil.rmtree(path)` | ⚠️ 危险操作，不可恢复 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##9. 目录操作]] |

### 综合案例

**二进制文件复制：** 每次读取 1KB 逐步复制，对内存友好 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##10. 两个小练习]]。

```python
import os
source = 'music.mp3'
target = 'D:/media'
if not os.path.isdir(target):
    os.makedirs(target)

with open(source, 'rb') as f1, open(target + '/my_music.mp3', 'wb') as f2:
    while True:
        data = f1.read(1024)
        if not data:
            break
        f2.write(data)
print('复制完毕')
```

**日志记录：** 登录系统按不同结果写入日志 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作##10. 两个小练习]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作]]`

## 关联页面

- [[Python]]
- [[python-模块与包]]
