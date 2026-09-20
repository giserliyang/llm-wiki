# Diff: 20260919_Python教程_尚硅谷 摄入（第五轮：第 9 章 错误与异常）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 9 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-错误与异常.md`** — Python 错误与异常（第 9 章）
   - 错误 vs 异常的核心区别
   - 常见异常类型速查表（ZeroDivisionError、TypeError、AttributeError、IndexError、NameError、KeyError、ValueError 等）
   - 异常处理完整写法：try / except / else / finally
   - 多 except 匹配规则、异常信息获取（`e.args`、`traceback`）
   - 手动抛出异常（`raise`）
   - 异常的传递机制（调用链逐层向上）
   - 自定义异常类（继承 Exception，类名以 Error 结尾）

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 错误与异常」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 5 条术语：异常、raise、finally、异常传递、自定义异常，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 9 章 错误与异常]]`

---

## 待处理（后续可继续摄入）

- 第 10 章：模块与包（import 机制、__init__.py、相对导入）
- 第 11 章：迭代器 vs 生成器（yield、__iter__、__next__）
- 第 12 章：文件操作（open、读写模式、with 上下文管理器）
- 第 13 章：进程与线程（Process、Thread、GIL、Queue）
- 第 14 章：协程（async/await、asyncio）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「try/except/else/finally 的执行顺序」**：各子句的触发条件与执行时机，配合流程图理解
2. **「异常类继承体系速记」**：常用异常类的层次关系（BaseException → Exception → 具体异常），配合实际踩坑记忆
3. **「自定义异常的最佳实践」**：何时自定义、如何设计异常类（命名规范、消息设计）
