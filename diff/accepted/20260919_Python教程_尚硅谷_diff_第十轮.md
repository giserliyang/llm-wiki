# Diff: 20260919_Python教程_尚硅谷 摄入（第十轮：第 14 章 协程）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 14 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-协程.md`** — Python 协程（第 14 章，全文最后一章）
   - 协程概念（5 个关键点：用户态、线程内、挂起/恢复、事件循环、单线程 CPU 利用率最大化）
   - 协程函数（async）vs 协程对象
   - asyncio.run() 三件事
   - await 关键字（挂起/等待/恢复、可等待对象）
   - 多任务同步执行（逐个 await）
   - 多任务异步执行（asyncio.create_task）
   - asyncio.gather（批量并发 + 批量结果）
   - 实战案例：传统同步下载 vs 协程异步下载图片

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 协程」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 7 条术语：协程、async、await、asyncio.run、asyncio.create_task、asyncio.gather、事件循环，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 14 章 协程]]`

---

## 本次摄入完成通知

> 本教程共 14 章已全部摄入完毕。

**累计新建概念页：13 个**

| # | 页面 | 对应章节 |
|---|---|---|
| 1 | `wiki/concepts/python.md` | 第 2 章 Python 概述 |
| 2 | `wiki/comparisons/编译型与解释型语言.md` | 第 1 章 编译/解释对比 |
| 3 | `wiki/concepts/python-基础语法.md` | 第 3 章 字面量/变量/运算符 |
| 4 | `wiki/concepts/数据类型.md` | 第 3 章 整型/浮点型/字符串 |
| 5 | `wiki/concepts/python-流程控制.md` | 第 4 章 分支/循环 |
| 6 | `wiki/concepts/python-函数.md` | 第 5 章 函数入门 |
| 7 | `wiki/concepts/python-数据容器.md` | 第 6 章 列表/元组/字符串容器 |
| 8 | `wiki/concepts/python-面向对象.md` | 第 7 章 类/继承/多态 |
| 9 | `wiki/concepts/python-函数进阶.md` | 第 8 章 高阶函数/闭包/装饰器 |
| 10 | `wiki/concepts/python-错误与异常.md` | 第 9 章 try/except/raise |
| 11 | `wiki/concepts/python-模块与包.md` | 第 10 章 import/pip/虚拟环境 |
| 12 | `wiki/concepts/python-迭代器与生成器.md` | 第 11 章 yield/生成器表达式 |
| 13 | `wiki/concepts/python-文件操作.md` | 第 12 章 open/with/目录操作 |
| 14 | `wiki/concepts/python-进程与线程.md` | 第 13 章 Process/Thread/GIL |
| 15 | `wiki/concepts/python-协程.md` | 第 14 章 async/await/asyncio |

**累计更新术语表：36 条术语**

**Diff 文件路径：**
- `diff/20260919_Python教程_尚硅谷_diff.md`
- `diff/20260919_Python教程_尚硅谷_diff_第二轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第三轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第四轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第五轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第六轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第七轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第八轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第九轮.md`
- `diff/20260919_Python教程_尚硅谷_diff_第十轮.md`

**后续建议：**
1. 人审通过后逐轮合并 diff 进对应 wiki 页
2. 考虑将 diff/suggestions/ 中的原子笔记建议落成 notes/ 原子笔记
3. 更新 `wiki/overview.md` 中可能需要的 dataview 查询条件
4. 如后续有新 raw 素材，可继续按此流程摄入
