# Diff: 20260919_Python教程_尚硅谷 摄入（第八轮：第 12 章 文件操作）

> 基于 `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md]]` 第 12 章生成。
> 人审确认后手动合并进对应 wiki 页。

---

## 变更清单

### 新建概念页

1. **`wiki/concepts/python-文件操作.md`** — Python 文件操作（第 12 章）
   - 文件分类（纯文本 / 二进制）
   - 绝对路径 vs 相对路径
   - open 函数参数详解（mode：r/w/x/a/b/t/+）
   - 读取方法（read / readline / for 循环遍历 / readlines）
   - with 上下文管理器（__enter__ / __exit__ 协议）
   - 写入模式（w / x / a）
   - flush 方法（缓冲区刷盘）
   - 组合模式（rt+ / wt+ / at+ 等）与 seek()
   - 目录操作（os.mkdir / makedirs / rmdir / walk / shutil.rmtree）
   - 综合案例（二进制文件复制、日志记录）

### 更新已有页

2. **`wiki/concepts/python.md`** — Python 概述
   - `related_wiki` 补充「Python 文件操作」关联链接

3. **`wiki/glossary.md`** — 术语表
   - 新增 5 条术语：with、flush、seek、os.walk，均附来源锚点

---

## 来源汇总

- `[[raw/tutorials/python/20260919_Python教程_尚硅谷.md#第 12 章 文件操作]]`

---

## 待处理（后续可继续摄入）

- 第 13 章：进程与线程（Process / Thread / GIL / Queue / join / 守护进程）
- 第 14 章：协程（async / await / asyncio / gather）

---

## 原子笔记建议

建议拆解为以下原子笔记供用户精读：
1. **「with 上下文管理器原理」**：__enter__/__exit__ 完整执行流程，异常处理返回值规则
2. **「文件读取最佳实践对比」**：read() / readline() / for 循环 / readlines() 的内存行为与适用场景
