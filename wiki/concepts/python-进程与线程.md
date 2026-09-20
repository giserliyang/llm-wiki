---
title: Python 进程与线程
status: ready
kind: concept
owners: ["me"]
source_count: 1
last_reviewed: 2026-09-19
sensitivity: internal
tags:
  - python
  - 并发编程
  - 进程
  - 线程
related_notes: []
related_wiki:
  - "Python"
  - "Python 文件操作"
---

# Python 进程与线程

## 摘要

本章涵盖并发与并行、同步与异步的核心概念，以及进程（Process）、线程（Thread）、GIL、队列通信、守护进程、进程池/线程池等并发编程关键主题 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程]]。

## 核心内容

### 并发 vs 并行、同步 vs 异步

| 维度 | 概念 | 说明 |
| --- | --- | --- |
| 并发 | 一段时间内交替执行多个任务 | CPU 高频切换，某瞬间只执行一个任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |
| 并行 | 同一时刻多个 CPU 同时执行多个任务 | 依赖多核 CPU [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |
| 同步 | 发起任务后需等待完成才能继续 | 当前执行流被阻塞 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |
| 异步 | 发起任务后不必等待，可继续执行其他任务 | 当前执行流不被阻塞 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |

> [!NOTE]
> 并发/并行描述的是任务如何被执行（CPU 如何处理）；同步/异步描述的是任务如何被组织和等待（是否阻塞等待）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]]。

### 进程 vs 线程

| 维度 | 进程 | 线程 |
| --- | --- | --- |
| 定义 | 正在运行的程序，操作系统资源分配的基本单位 | 进程内部的执行单元，操作系统 CPU 调度的基本单位 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |
| 内存空间 | 每个进程有独立内存空间 | 同进程内的线程共享进程资源 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##1. 一些核心概念]] |
| 创建开销 | 高（需创建独立内存空间） | 低（共享进程资源） |
| 最小数量 | 1 个 | 1 个（主线程） |

**进程 PID：** `os.getpid()` 获取当前进程 ID，`os.getppid()` 获取父进程 ID [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##2. 主进程 _ 子进程]]。

### 使用 Process 创建进程

```python
import os
from multiprocessing import Process

def speak():
    for i in range(10):
        print(f'pid={os.getpid()}, ppid={os.getppid()}')

if __name__ == '__main__':       # Windows 下必须加此判断
    p = Process(target=speak)
    p.start()                    # 向操作系统申请进程，交由调度
    p.join()                     # 阻塞等待进程结束
```

> [!warning]
> Windows 使用 `multiprocessing` 必须加 `if __name__ == '__main__':`，否则子进程会重新执行整个文件导致无限递归创建子进程 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##3. 使用 Process 创建进程]]。

**Process 参数：** `target`（任务函数）、`name`（进程名）、`args`（位置参数元组）、`kwargs`（关键字参数字典）、`daemon`（是否守护进程）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##4. 关于 Process 的参数]]。

### 进程控制

| 方法 | 说明 |
| --- | --- |
| `start()` | 向操作系统申请进程并交由调度 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]] |
| `join(timeout)` | 阻塞当前进程，等待目标进程结束；`timeout` 超时后不再等（不终止进程）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]] |
| `terminate()` | 强制终止进程；不会执行 `finally` 代码块 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]] |
| `is_alive()` | 判断进程是否还在运行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]] |

**Lock / RLock：** 防止多个进程同时操作共享资源导致数据错乱 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]]。

- `Lock`：传统锁，多次 acquire 会产生死锁 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]]。
- `RLock`：可重入锁，同一个进程可以多次 acquire 而不会死锁。
- 推荐用 `with lock:` 语法，自动加锁/释放锁，避免异常时死锁。

**守护进程（Daemon）：** 依附于主进程存在，主进程结束则守护进程自动终止。使用场景：后台监控、日志统计、辅助陪跑任务 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]]。

> [!warning]
> 守护进程必须在 `start()` 之前设置 `daemon=True`；守护进程中不允许再创建新的子进程 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##5. 进程控制]]。

### 进程之间不共享变量

进程之间不共享内存，因此也不共享任何变量（包括全局变量）。进程间通信必须通过队列（Queue）或管道（Pipe）等机制实现 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##6. 进程之间不共享变量]]。

> [!tip]
> Lock、RLock、Queue 等对象是天然被多个进程共享的 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##6. 进程之间不共享变量]]。

### Queue（队列）

**概念：** 先进先出（FIFO）的数据结构，可用于进程间通信 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##7. Queue（队列）]]。

```python
from multiprocessing import Queue

q = Queue()          # 不限制大小
q = Queue(3)         # 最多存 3 个元素

q.put(10)            # 入队
value = q.get()      # 出队
q.empty()            # 判断是否为空
q.full()             # 判断是否已满
q.qsize()            # 获取队列长度
```

**等待模式：** 队列已满时 `put` 会阻塞等待；队列已空时 `get` 会阻塞等待。可用 `put(data, timeout=N)` 设置超时，或使用 `put_nowait()` / `get_nowait()` 立即抛异常 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##7. Queue（队列）]]。

**进程通信示例：** 一个进程生产数据放入 Queue，另一个进程从 Queue 取出消费 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##8. 使用 Queue 实现进程通信]]。

### Pipe（管道）

`Pipe()` 返回两个连接对象，代表管道的两端 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##9. 使用 Pipe 实现进程通信]]。

- `duplex=True`：双向通信
- `duplex=False`：单向通信（con1 只能发送，con2 只能接收）
- `send()` 发送数据，`recv()` 接收数据 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##9. 使用 Pipe 实现进程通信]]。

### 继承 Process 类创建进程

面向对象风格，把「进程 + 行为」封装成一个整体 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##10. 继承 Process 类创建进程]]。

```python
class SpeakProcess(Process):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def run(self):           # 把子进程要干的事写进 run()
        for i in range(10):
            print(f'{self.a}--{self.b}--{i}')

p1 = SpeakProcess(100, 200)
p1.start()    # 调用 start，不要手动调用 run()
```

### 进程池（ProcessPoolExecutor）

进程创建/销毁成本高，大量任务时用进程池统一管理，避免频繁创建/销毁进程 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##11. 进程池（ProcessPoolExecutor）]]。

```python
from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor(3)   # 池中有 3 个进程
futures = [executor.submit(work, i) for i in range(1, 8)]
executor.shutdown(wait=True)        # 不再接收新任务，等待所有任务完成

for f in futures:
    print(f.result())               # 获取返回值

# 按完成顺序获取结果
from concurrent.futures import as_completed
for f in as_completed(futures):
    print(f.result())
```

### 线程基础

每个 Python 程序至少有一个线程（主线程）。线程共享进程的内存空间，执行顺序由操作系统调度 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##12. 使用 Thread 创建线程]]。

**Thread 参数：** `target`、`name`、`args`、`kwargs`、`daemon` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##12. 使用 Thread 创建线程]]。

```python
from threading import Thread, RLock, get_native_id

def speak(lock):
    for i in range(5):
        with lock:
            print(f'说话{i}, pid={os.getpid()}, tid={get_native_id()}')

lock = RLock()
t1 = Thread(target=speak, args=(lock,))
t1.start()
t1.join()
```

### 继承 Thread 类创建线程

与继承 Process 类似，重写 `run()` 方法 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##13. 继承 Thread 创建线程]]。

### 线程池（ThreadPoolExecutor）

语法与进程池完全相同，使用 `ThreadPoolExecutor` 替代 `ProcessPoolExecutor` [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##14. 线程池]]。

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

executor = ThreadPoolExecutor(3)
futures = [executor.submit(work, i) for i in range(1, 8)]
executor.shutdown(wait=True)
```

### GIL（全局解释器锁）

**概念：** CPython 解释器中的一把互斥锁，确保解释器级别的数据安全（防止引用计数错误导致内存爆炸）[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##15. GIL 全局解释器锁]]。

**结论：** CPython 多线程本质上是**并发**而非并行——无论 CPU 有多少核心，某一时刻只允许一个线程执行 Python 代码 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##15. GIL 全局解释器锁]]。

- GIL 在遇到 I/O 操作或任务超时时释放
- 多进程可以绕过 GIL，发挥多核 CPU 性能
- GIL 是解释器层面的，业务代码中的 `Lock/RLock` 是用于保证业务逻辑正确的 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##15. GIL 全局解释器锁]]。

### 多进程 vs 多线程选择

| 任务类型 | 推荐方案 | 原因 |
| --- | --- | --- |
| **CPU 密集型**（大量计算） | 多进程 | 绕过 GIL，利用多核并行 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##16. 多进程 vs 多线程，该如何选择？]] |
| **IO 密集型**（文件读写、网络请求） | 多线程 | I/O 等待时 GIL 释放，线程切换开销小 [[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程##16. 多进程 vs 多线程，该如何选择？]] |

## 引用来源

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程]]`

## 关联页面

- [[Python]]
- [[python-文件操作]]
