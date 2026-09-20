# Diff: 20260919_Python教程_尚硅谷 摄入（第四轮：第 8 章 函数进阶）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 8 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-函数进阶.md`** — Python 函数进阶（第 8 章）
   - 函数是一等对象（可赋值、可作参数、可作返回值）
   - 多返回值与参数打包/解包（*args/**kwargs）
   - 高阶函数（map / filter / sorted / reduce）
   - lambda 匿名函数
   - 列表/字典/集合推导式
   - 浅拷贝 vs 深拷贝（copy.copy / copy.deepcopy）
   - 四种作用域 LEGB
   - 闭包（概念、产生条件、优点与缺点）
   - 装饰器（函数装饰器 / 类装饰器 / 多层装饰器 / 带参数装饰器）
   - 类型注解（变量 / 容器 / 函数）

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 函数进阶」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 13 条术语：高阶函数、lambda、map、filter、reduce、列表推导式、浅拷贝、深拷贝、闭包、装饰器、LEGB、类型注解等，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 8 章 函数进阶]]`

---

## 待处理（后续可继续摄入）

- 第 9 章：错误与异常（try/except/finally、异常类、自定义异常）
- 第 10 章：模块与包（import、__init__.py、相对导入）
- 第 11 章：迭代器 vs 生成器（yield、__iter__、__next__）
- 第 12 章：文件操作（open、读写模式、上下文管理器）
- 第 13 章：进程与线程（Process、Thread、GIL、Queue）
- 第 14 章：协程（async/await、asyncio）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「闭包与装饰器的底层原理」**：`__closure__`、cell 机制、装饰器执行时机
2. **「浅拷贝 vs 深拷贝的内存模型」**：可变/不可变对象在拷贝时的不同行为
3. **「高阶函数三剑客」**：map / filter / reduce 与列表推导式的适用场景对比
