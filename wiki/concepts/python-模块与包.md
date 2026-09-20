---
title: Python 模块与包
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 模块
  - 包
related_notes: []
related_wiki:
  - "Python"
---

# Python 模块与包

## 摘要

模块是代码组织的基本单位，包是管理模块的目录结构。理解模块导入机制和虚拟环境是编写可维护 Python 项目的基础 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包]]。

## 核心内容

### 模块（Module）

**定义：** 一个 `.py` 文件就是一个模块，可以包含变量、函数、类等内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.1. 概述]]。

**分类：** 标准库模块（随 Python 安装）、自定义模块（用户编写的 `.py` 文件）、第三方模块（通过 pip 安装）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.2. 模块的分类]]。

**命名规范：**
- 符合标识符命名规则
- 区分大小写
- 不要与标准库模块同名（否则优先引入标准库）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.3. 创建模块]]。

**导入方式：**

| 写法 | 说明 |
| --- | --- |
| `import 模块名` | 全部导入，通过`模块名.成员`访问 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.4. 导入模块]] |
| `import 模块名 as 别名` | 导入并设置别名，避免冲突 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.4. 导入模块]] |
| `from 模块名 import 成员1, 成员2` | 导入指定成员，直接访问无需前缀 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.4. 导入模块]] |
| `from 模块名 import *` | 导入所有成员（受 `__all__` 控制）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.4. 导入模块]] |

> [!warning]
> Python 导入模块时会执行对应模块中的代码；模块只加载一次，后续导入直接复用缓存 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.4. 导入模块]]。

**`__all__`：** 控制 `from 模块 import *` 能导入哪些内容，值为列表或元组 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.5. `__all__` 与 `__name__`]]。

**`__name__`：** 模块内置变量，主程序运行时值为 `'__main__'`，被导入时值为模块文件名（不带 `.py`）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.5. `__all__` 与 `__name__`]]。

### 常用标准库模块示例

| 模块       | 功能                                                                                                 |
| -------- | -------------------------------------------------------------------------------------------------- |
| `os`     | 操作系统操作（文件、文件夹、路径）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]         |
| `random` | 随机数相关（choice、shuffle 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]   |
| `time`   | 时间操作（sleep、strftime 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]    |
| `math`   | 数学运算（sqrt、fabs 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]         |
| `sys`    | Python 解释器相关操作（version 等）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]] |
| `copy`   | 浅拷贝、深拷贝 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]                  |

> [!tip]
> 内置模块（如 `time`、`math`、`sys`）没有 `__file__` 属性，无法查看具体实现位置；非内置标准库模块可通过 `__file__` 查看文件路径 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##1.6. 标准库模块]]。

### 包（Package）

**定义：** 包含 `__init__.py` 的文件夹就是包，包中可以包含多个模块和子包 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.1. 概述]]。

**包命名规范：**
- 符合标识符命名规范
- 全部使用小写字母
- 不与标准库包同名 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.4. 创建包]]。

**`__init__.py` 的作用：**
1. 包被导入时自动执行（初始化逻辑）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]]
2. 定义的内容可通过 `from 包名 import *` 导入
3. 可用 `__all__` 控制可导入内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]]

**包导入方式：**

| 写法 | 说明 |
| --- | --- |
| `import 包名.模块名` | 通过包路径访问模块 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]] |
| `from 包名.模块名 import 成员` | 从包的模块中导入指定内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]] |
| `from 包名 import 模块名` | 导入包中的模块 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]] |
| `from 包名 import *` | 导入包中 `__init__.py` 定义的内容 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.5. 导入包]] |

**子包：** 包中可以嵌套子包（子包也是包含 `__init__.py` 的文件夹），导入时加一层路径：`from 包名.子包名.模块名 import 成员` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.6. 引入子包]]。

### 第三方包与 pip

**PyPI：** Python 官方包发布与分发平台（https://pypi.org）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]]。

**pip 常用命令：**

| 命令 | 说明 |
| --- | --- |
| `pip install 包名` | 安装指定包 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |
| `pip install -i 镜像地址 包名` | 使用镜像临时安装 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |
| `pip config set global.index-url 地址` | 永久设置镜像地址 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |
| `pip list` | 列出已安装包 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |
| `pip uninstall 包名` | 卸载指定包 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |

**国内镜像：**
- 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
- 阿里云：https://mirrors.aliyun.com/pypi/simple
- 中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]]

### 全局环境 vs 虚拟环境

| 维度 | 全局环境 | 虚拟环境 |
| --- | --- | --- |
| 组成 | Python 解释器 + 依赖包 | 独立的 Python 解释器 + 依赖包 |
| 影响范围 | 所有项目共用 | 仅当前项目 |
| 优点 | 简单直接 | 项目间依赖互不干扰 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]] |
| 缺点 | 容易互相影响和干扰 | 需要手动激活和切换 |

- 全局环境：`pip install` 直接安装的包，所有项目可用
- 虚拟环境：通过 `activate` 激活后安装包，仅当前项目可用
- 二者共享：Python 标准库 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]]。

> [!tip]
> 退出虚拟环境用 `deactivate` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包##2.7. 第三方包]]。

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包]]`

## 关联页面

- [[Python]]
