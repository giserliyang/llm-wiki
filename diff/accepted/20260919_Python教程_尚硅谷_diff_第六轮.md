# Diff: 20260919_Python教程_尚硅谷 摄入（第六轮：第 10 章 模块与包）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 10 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-模块与包.md`** — Python 模块与包（第 10 章）
   - 模块的定义、分类、命名规范
   - 5 种导入方式对比（import / import as / from import / from import * / from import as）
   - `__all__` 与 `__name__` 的作用
   - 常用标准库模块速查（os、random、time、math、sys、copy）
   - 包的结构（含 `__init__.py` 的文件夹）、子包导入
   - `__init__.py` 的三个作用
   - pip 常用命令与国内镜像
   - 全局环境 vs 虚拟环境对比

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 模块与包」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 4 条术语：模块、包、虚拟环境、pip，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 10 章 模块与包]]`

---

## 待处理（后续可继续摄入）

- 第 11 章：迭代器 vs 生成器（`__iter__`/`__next__`、`yield`、生成器.send()）
- 第 12 章：文件操作（open、读写模式、with 上下文管理器）
- 第 13 章：进程与线程（Process、Thread、GIL、Queue）
- 第 14 章：协程（async/await、asyncio）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「模块导入机制与 __name__ 技巧」**：导入时执行逻辑、`if __name__ == '__main__'` 的实际用途
2. **「pip 与虚拟环境实战」**：镜像配置、环境切换、项目隔离的最佳实践
