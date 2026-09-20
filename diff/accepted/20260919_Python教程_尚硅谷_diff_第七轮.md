# Diff: 20260919_Python教程_尚硅谷 摄入（第七轮：第 11 章 迭代器 vs 生成器）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 11 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-迭代器与生成器.md`** — Python 迭代器与生成器（第 11 章）
   - 可迭代对象 vs 迭代器（`__iter__` / `__next__` / 迭代器协议）
   - for 循环的本质（iter → next → StopIteration）
   - 自定义迭代器（实现 `__iter__` 和 `__next__`）
   - 迭代器的优势（惰性计算、内存节约）
   - 生成器函数与生成器对象（`yield` 暂停/恢复机制）
   - `yield from` 和 `send()` 用法
   - 生成器表达式 vs 列表推导式

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 迭代器与生成器」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 8 条术语：可迭代对象、迭代器、生成器、yield、yield from、生成器表达式、send()，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 11 章 迭代器 vs 生成器]]`

---

## 待处理（后续可继续摄入）

- 第 12 章：文件操作（open、读写模式、with 上下文管理器）
- 第 13 章：进程与线程（Process、Thread、GIL、Queue）
- 第 14 章：协程（async/await、asyncio）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「for 循环底层机制」**：iter() → __next__() → StopIteration 的完整过程
2. **「生成器 vs 迭代器类实现对比」**：yield 自动实现协议 vs 手动写 __iter__/__next__ 的优劣
