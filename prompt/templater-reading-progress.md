# Templater：生成带跳转的阅读进度

前提：已安装社区插件 **Templater**。

## 一次性设置

1. 设置 → Templater  
2. **Template folder location** 填：`templates`  
3. 建议开启：`Trigger Templater on new file creation` 可关（不必）  
4. 记下快捷键，或用命令面板

## 日常怎么用

1. 打开教程，例如 `raw/tutorials/Python_V3.0/Python_V3.0.md`  
2. 光标点到 `## 阅读进度` 的下一行（若有旧清单，先清空）  
3. `Ctrl+P` → **Templater: Open insert template modal**  
4. 选择 `gen-reading-progress`  
5. 得到全部层级标题（`#`～`######`）嵌套清单：

```markdown
- [ ] [[Python_V3.0#第 1 章 必备基础知识]]
	- [ ] [[Python_V3.0#1. 计算机组成]]
		- [ ] [[Python_V3.0#1.1. 硬件]]
	- [ ] [[Python_V3.0#2. 计算机语言、代码、程序]]
- [ ] [[Python_V3.0#第 2 章 初识 Python]]
```

链接带**笔记名**，因此在 [[dashboards/素材收件箱]] 的 TASK 列表里点击，也能跳回教程对应标题（若只写 `[[#标题]]`，在收件箱里会解析错文件）。

6. **手动删掉**不想跟的节点；可加 🔴 / 🟡 / ⚪  
7. 阅读模式下点击链接可跳到对应标题

## 注意

- 链接文字与正文标题一字不差（脚本直接抽取，一般没问题）  
- 代码块里的 `# 注释` 不会进清单  
- 遇到 `# 学习附录` 停止  
- 缩进按标题层级自动生成（用 Tab）  
- 这是「插入」，不会自动替换旧进度；旧的要自己删

## 和 Copy Outline 的分工

| 工具 | 产出 |
| --- | --- |
| Copy Outline | 纯标题树，无链接、无复选框 |
| 本 Templater | 全级标题 + `[[#标题]]` + 复选框 + 按层级缩进 |
