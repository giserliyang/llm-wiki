# Diff: 20260919_Python教程_尚硅谷 摄入（第九轮：第 13 章 进程与线程）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 13 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-进程与线程.md`** — Python 进程与线程（第 13 章）
   - 核心概念：并发 vs 并行、同步 vs 异步、进程 vs 线程
   - Process 创建（target/args/kwargs、if __name__ 必要性）
   - 进程控制（start/join/terminate/is_alive）
   - Lock / RLock（临界区保护、with 语法）
   - 守护进程（daemon）
   - 进程间不共享变量、Queue 进程通信、Pipe 通信
   - 继承 Process 类创建进程
   - 进程池（ProcessPoolExecutor、Future、as_completed）
   - Thread 创建与继承 Thread 类
   - 线程池（ThreadPoolExecutor）
   - GIL（全局解释器锁）原理与影响
   - CPU 密集型 vs IO 密集型任务的选择策略

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 进程与线程」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 10 条术语：进程、线程、守护进程、GIL、并发、并行、Queue、进程池、线程池等，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 13 章 进程与线程]]`

---

## 待处理（后续可继续摄入）

- 第 14 章：协程（async/await、asyncio、事件循环、gather）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「GIL 的底层原理与影响」**：为什么 CPython 需要 GIL、它对多线程性能的实质影响、如何绕过（多进程）
2. **「进程通信机制对比」**：Queue vs Pipe 的适用场景、各自的优势与局限
3. **「CPU 密集型 vs IO 密集型实践」**：如何通过实际计时实验验证多进程/多线程在不同任务上的表现差异
