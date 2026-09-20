---
title: Python 协程
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 协程
  - 异步
related_notes: []
related_wiki:
  - "Python"
  - "Python 进程与线程"
---

# Python 协程

## 摘要

协程（Coroutine）是在线程内部通过事件循环实现任务挂起与恢复的调度机制，在遇到 IO 操作时将 CPU 交给其他任务，从而最大化单线程 CPU 利用率，特别适合 IO 密集型任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程]]。

## 核心内容

### 协程的概念

**本质：** 在一个线程里，趁着某些任务在等 IO，把 CPU 交给其它任务去用 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。

**关键点：**

1. **协程不是线程也不是进程**，是程序员在用户态用代码设计的任务切换机制，CPU 和操作系统都看不见协程 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。
2. **协程发生在一个线程内部**，是线程内多个任务之间的切换，不是线程间的切换 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。
3. **核心能力：挂起与恢复**——遇到 IO 时任务挂起，IO 完成后任务恢复执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。
4. **依赖事件循环**——事件循环负责调度任务、判断是否挂起、决定何时恢复，是协程系统的"大脑" [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。
5. **目标**——在单线程下最大化 CPU 利用率，特别适合 IO 密集型任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##1. 什么是协程]]。

### 协程函数 vs 协程对象

- **协程函数：** 使用 `async` 关键字修饰的函数 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##2. 协程函数 vs 协程对象]]。
- **协程对象：** 调用协程函数得到，**调用协程函数不会立即执行其中的代码** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##2. 协程函数 vs 协程对象]]。

```python
import asyncio

async def work():           # 协程函数
    print('work开始')
    return '工作结果'

coroutine_obj = work()      # 得到协程对象，代码未执行
result = asyncio.run(coroutine_obj)  # 运行，得到返回值
```

**`asyncio.run()` 做了三件事：**
1. 创建一个事件循环
2. 将协程对象包装成 Task 交给事件循环
3. 启动事件循环，阻塞当前线程直到任务完成并返回结果 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##2. 协程函数 vs 协程对象]]。

### await 关键字

`await` 三个作用：挂起、等待、恢复 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##3. await 关键字]]。

**执行 await 时的两种情况：**

| 情况 | 行为 |
| --- | --- |
| await 对象包含 IO 操作 | CPU 控制权交给事件循环，事件循环调度其他任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##3. await 关键字]] |
| await 对象不含 IO（如 print、计算） | 事件循环拿不到控制权，不发生任务切换 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##3. await 关键字]] |

> [!warning]
> `await` 后面只能写**可等待对象**：协程对象、Future 对象、Task 对象 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##3. await 关键字]]。

```python
async def work():
    print('work开始')
    res = await asyncio.sleep(2)   # 挂起，等待 IO 完成
    print('work结束')
    return '结果'

async def main():
    res = await work()             # 等待 work 协程完成
    return 'main结果'

asyncio.run(main())
```

### 多个任务同步执行

逐个 `await` 协程，任务按顺序依次执行，总耗时 = 各任务耗时之和 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##4. 多个任务同步执行]]。

```python
async def main():
    res1 = await work(1, 2)   # 等 work1 完成后才执行 work2
    res2 = await work(2, 2)   # 等 work2 完成后才执行 work3
    res3 = await work(3, 2)
```

### 多个任务异步执行

使用 `asyncio.create_task()` 将协程包装为 Task 注册到事件循环，任务并发执行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##5. 多个任务异步执行]]。

```python
async def main():
    task1 = asyncio.create_task(work(1, 2))  # 注册任务到事件循环
    task2 = asyncio.create_task(work(2, 2))
    task3 = asyncio.create_task(work(3, 2))
    res1 = await task1    # 依次等待各任务完成
    res2 = await task2
    res3 = await task3
```

> [!tip]
> `create_task` 将协程包装成可被事件循环调度的 Task 对象并注册到事件循环中，三个任务的 IO 等待可以重叠，总耗时约等于单个任务耗时 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##5. 多个任务异步执行]]。

### asyncio.gather

把多个协程一次性丢给事件循环，全部执行完后**一次性拿到所有结果** [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##6. asyncio.gather]]。

```python
async def main():
    results = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print(results)  # ['work1的返回值', 'work2的返回值', 'work3的返回值']
```

### 实战案例：协程下载图片

**传统方式（同步）：** 图片一张一张下载，前一张未完成后一张不能开始，总耗时 = 各图片下载时间之和 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##7. 下载图片案例]]。

```python
import requests

def download_picture(url):
    response = requests.get(url)   # 同步阻塞等待网络响应
    with open(url[-10:], 'wb') as f:
        f.write(response.content)
```

**协程方式（异步）：** 多张图片几乎同时发起请求，某张在等待网络数据时其他任务继续执行，总耗时显著降低 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##7. 下载图片案例]]。

```python
import aiohttp
import asyncio

async def download_picture(session, url):
    response = await session.get(url)        # 挂起等待网络响应
    content = await response.read()          # 挂起等待数据读完
    with open(url[-10:], 'wb') as f:
        f.write(content)
    await response.release()                 # 释放连接资源

async def main():
    session = aiohttp.ClientSession()
    urls = [...]
    coroutine_list = [download_picture(session, url) for url in urls]
    await asyncio.gather(*coroutine_list)
    await session.close()

asyncio.run(main())
```

[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程##7. 下载图片案例]]

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程]]`

## 关联页面

- [[Python]]
- [[python-进程与线程]]
