---
title: llm-wiki搭建实录
type: essay
tags: []
status: 已理解
understanding_level: 1
need_practice: true
last_review: 2026-09-18
source: "[[别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云]]"
source_url: ""
aliases: []
---

# llm-wiki搭建实录

此文档为我的笔记系统搭建实录。

## 一句话结论

搭建符合我的笔记系统。

## 背景 / 要解决什么
搭建符合我的笔记系统。

## 正文

### 核心理念

|角色|职责|
|---|---|
|**你**|丢素材、写疑难点、审 diff、升级掌握度|
|**LLM**|把 `raw/` 编译成 `wiki/`，生成待审变更|
|**Obsidian**|阅读、双链、图谱、仪表盘前端|

目标不是「再做一个笔记软件」，而是：**素材只进一次，结论可复用、可溯源、可进化**。
### 架构
```
raw/        教程 / 视频 / 公众号 / 书签（只读归档）
wiki/       LLM 编译的概念/实体页（人审 diff）
notes/      你的原子笔记（LLM 禁改）
dashboards/ 学习仪表盘 + 素材收件箱
templates/  四类来源模板 + 原子笔记 + wiki 页
prompt/     ingest / lint / writeback
AGENTS.md   LLM 操作规则（Schema 层）
```

#### 三层 + 个人层

```
raw/          原始素材（只读）——教程/视频/公众号/书签
     ↓ LLM 编译（你审 diff）
wiki/         结构化知识——概念、实体、对比、决策
     ↑ 你亲手写
notes/        原子笔记——疑难点、洞见、实战
```

约束写在根目录 **`AGENTS.md`**：LLM 禁止改 `raw/` 和 `notes/`，无来源不写进 wiki，变更先落 `diff/`。
#### 两条路径
1. 个人笔记（主路径）
	1. 1. 原文进 `raw/`（套对应模板）
	2. Copy Outline 复制章节骨架 → 改成阅读进度清单，标 🔴急需 / ⚪暂跳过
	3. **真正卡住时**才新建 `notes/` 原子笔记（不要按目录预建空壳）
	4. YAML 写 `source: "[[原文]]"`，正文写 `[[原文#章节]]`
	5. 只有真的会默写/会讲/用过，才改 `understanding_level`
2. LLM Wiki（编译路径）
	1. 新素材进 `raw/`
	2. 用 `prompt/ingest.md` 让 Agent 按 `AGENTS.md` 更新 `wiki/`
	3. 在 `diff/` 审核，通过再合并
	4. 优质问答可用 `prompt/writeback.md` 回写进 wiki

#### 两个仪表盘
你最该盯的两个仪表盘

- **`dashboards/学习仪表盘`**：重点复习（level<3）、待实践、超 30 天没碰、按 source 分组
- **`dashboards/素材收件箱`**：raw 里有什么、读没读完

字段纪律（OKR + GTD + 卡片盒）：

| 字段                        | 含义                                      |
| ------------------------- | --------------------------------------- |
| `understanding_level` 0–5 | 掌握程度（行为结果，不是阅读次数）                       |
| `need_practice`           | 下一步行动                                   |
| `last_review`             | 真正复习过的日期                                |
| `source` / `source_type`  | 溯源：tutorial / video / wechat / bookmark |

### 1. 资料收集

#### 1. 教程
1. 复制md文档
2. 使用*Templates插件*添加yaml
3. 使用Templates插件添加学习附件
4. 使用*Templates插件*`gen-reading-progress`模版添加阅读进度
#### 2. 书签
1. 使用*obsidian web clipper插件*添加书签
2. 使用*Templates插件*`gen-reading-progress`模版添加阅读进度
##### 配置：
1. 配置模版属性
2. 配置模版内容
```markdown

{{content}}

---

# 学习附录

## 书签卡

| 字段 | 值 |
| --- | --- |
| URL | {{url}} |
| 为什么存 | |
| 什么时候用 | |

## 阅读进度

> 用 Templater `gen-reading-progress` 生成（~~脚本~~碰到「学习附录」会停）。
> 纯参考书签可删掉本段。未勾选会出现在 [[dashboards/素材收件箱]]。
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过

- [ ] 
  - [ ] 

## 拆解索引

/```dataview
LIST
FROM "notes"
WHERE source = this.file.link
SORT understanding_level DESC
/```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。

```

#### 3. 视频
##### 1. B站
1. 使用*bilibili obsidian clipper+Local REST API with MCP插件*添加带时间戳的视频笔记
###### 配置：
1. 配置yaml
2. 配置Local REST API with MCP
##### 2. 本地视频
1. 使用*video_to_note脚本*添加带时间戳的视频笔记

###### 一、首次安装（只需一次）

```bash
# 1. 依赖
brew install python@3.12 ffmpeg

# 2. 虚拟环境（放在 vault 外）
python3 -m venv ~/venvs/whisper
source ~/venvs/whisper/bin/activate
pip install -U pip faster-whisper

# 3. HuggingFace 国内镜写入 zsh
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc
source ~/.zshrc

# 4. 验证模型能下载
python -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8'); print('ok')"
```

 ###### 二、每次转写（日常）

```bash
# 1. 激活环境
source ~/venvs/whisper/bin/activate

# 2. 进入 Vault 根目录（必须，脚本按此找 raw/videos/）
cd /Users/ly/Developer/_Externals/llm_wiki

# 3. 执行脚本 + 视频完整路径
python scripts/video_to_note.py "/Users/ly/Developer/_Externals/Videos/芋道源码/工作流 04：如何实现流程表单的展示？.mp4"
```


###### 三、结果在哪

|产出|路径|
|---|---|
|笔记|`raw/videos/<文件名>.md`（含 `<video>`、字幕、学习附录）|
|本地视频路径|写在 YAML `source_url`（`file://…`）|
|srt|**不保留**，字幕只在 md 正文|

###### 四、可选：一条命令（别名）

写入 `~/.zshrc`：

```bash
alias wnote='source ~/venvs/whisper/bin/activate && export HF_ENDPOINT=https://hf-mirror.com && cd /Users/ly/Developer/_Externals/llm_wiki && python scripts/video_to_note.py'
```

```bash
source ~/.zshrc
wnote "/Users/ly/Developer/_Externals/Videos/芋道源码/xxx.mp4"
```

#### 4. 随笔
1. 使用*Templates插件*添加随笔
#### 5. 灵感随手记
使用*Templates插件*添加灵感随手记
##### 一、电脑端（Vault 已就绪）

|步骤|内容|
|---|---|
|1|Obsidian 桌面打开 Vault（Windows：`Documents\llm_wiki`；Mac：`Developer/_Externals/llm_wiki`）|
|2|结构已有：`notes/inbox/`、`templates/node-quick-capture.md`|
|3|社区插件：**Dataview**、**Templater**（模板用 `<% tp.date.now() %>`）|
|4|GitHub：`git init` → `commit` → `push`（私有仓库）|
|5|SSH：`id_ed25519` + passphrase / 重新生成公钥加入 GitHub|

##### 二、手机端（iOS App）

|步骤|内容|
|---|---|
|1|App Store 安装 **Obsidian**（你本机为 1.13.x）|
|2|安装 **Working Copy**（Git 客户端，Clone 用）|
|3|Working Copy：Clone `git@github.com:用户/llm_wiki.git`|
|4|库放到 **iCloud**：`iCloud Drive/Obsidian/llm_wiki`（Obsidian 才能「使用现有仓库」/ iCloud 检测到）|
|5|Obsidian → **使用现有仓库** → iCloud → 打开 `llm_wiki`（iOS 引导可能要先建临时库再切换）|

> 说明：iOS 首次引导常不弹「任意文件夹」；最终路径是 **iCloud 顶层 `Obsidian/` 文件夹**。

##### 三、手机上写随手记（日常）


```text
1. 打开 Obsidian（iCloud 库）
2. 文件列表 → notes/inbox/
3. 新建当日笔记，如 2026-09-18
4. Templater → Insert template → node-quick-capture
   （或手写几行也行）
5. 30 秒写完：灵感一两句 + 可选来源
```

模板要点：YAML `created`、`# 日期 随手记`、周清勾选；**靠目录 `inbox` 区分，不必 `tags: inbox`**。

##### 四、同步回 Git（当前做法）

|方式|做法|
|---|---|
|**推荐（简单）**|手机只在 iCloud 库写 inbox → 定期把 md **拷到电脑** Vault 的 `notes/inbox/` → 电脑 `git add && commit && push`|
|**Working Copy**|若 Pro 可用：在 iCloud 路径上 Commit/Push（你已了解位置/费用限制）|

电脑侧 Git 示例：

```bash
cd /path/to/llm_wiki
git pull
# 将手机同步过来的 notes/inbox/*.md 纳入版本库
git add notes/inbox
git commit -m "inbox: ..."
git push
```

##### 五、周清（消化 inbox）


```text
notes/inbox/xxx
  ├─ 值得留 → notes/ 原子笔记（Templater → node-atomic-note）
  ├─ 只是链接 → raw/bookmarks/
  └─ 可丢 → 删除
```

### 2. 原子笔记流程

#### 1. 模拟真实学习
1. `cmd+.`等方式打开双屏
2. 使用Templates建，回填该有字段，并编写内容
3. `学习仪表盘`，应能在「重点复习」里看到它（level < 3）
#### 2. 以后升等级的规则
| 动作                 | 才改字段                      |
| ------------------ | ------------------------- |
| 真的默写出代码            | `understanding_level` → 3 |
| 真的给别人讲明白           | → 4                       |
| 真的用来修过 bug / 迁移过场景 | → 5                       |
| 上机做完了              | `need_practice: false`    |
| 真正重看有收获            | 更新 `last_review`          |
#### 字段分类标准

##### 1. `type` — 笔记角色

|值|含义|放哪|
|---|---|---|
|`raw`|原始素材（只读归档）|`raw/`|
|`essay`|自己写的长文/总结|`notes/essays/`|
|（可不写）|短原子笔记|`notes/`|
|`dashboard`|仪表盘（只查不写）|`dashboards/`|

##### 2. `source_type` — 素材来源类型

|值|含义|对应目录|
|---|---|---|
|`tutorial`|教程、文档、讲义|`raw/tutorials/`|
|`video`|视频字幕/文稿/本地课|`raw/videos/`|
|`bookmark`|网页书签、剪藏、公众号等|`raw/bookmarks/`|
|`other`|零散、不好归类|`raw/others/`|

##### 3. `status` — 阅读/消化状态

1. 用于 `raw/` 素材
	
	|值|含义|
	|---|---|
	|`未读`|刚入库|
	|`进行中`|正在读/看|
	|`已理解`|通读完，主要点心里有数|
	|`已归档`|不再跟或已消化完|

2. 用于 `notes/` 原子笔记、essay
	
	|值|含义|
	|---|---|
	|`未读`|刚建，还没认真写完|
	|`进行中`|在写/在琢磨|
	|`已理解`|自己话写清了，能复述|
	|`已归档`|不再投入|

3. 用于 `wiki/`（LLM 页）
	
	|值|含义|
	|---|---|
	|`draft`|草稿|
	|`ready`|可用|
	|`review`|待人审|
	|`废弃`|不删页，只标记废弃|

##### 4. `understanding_level` — 掌握度（0–5）

|值|含义|判断标准|
|---|---|---|
|`0`|未读|没碰过|
|`1`|见过|知道有这么回事，说不清|
|`2`|能复述|自己话大致讲得出|
|`3`|能默写|不看资料能写出步骤/代码|
|`4`|能讲懂|能给别人讲清并回答追问|
|`5`|能改|能迁移、改实现、解决变体问题|

**原则：** 只有「行为」结果到了才升级（会默写/会讲/用过），不是又读了一遍。

##### 5. `need_practice` — 是否还要实操

|值|含义|
|---|---|
|`true`|还要上机/做项目才能算掌握|
|`false`|已不需要（做完实践，或纯概念已够）|

##### 6. `source` / `source_url`

| 字段           | 含义                                   |
| ------------ | ------------------------------------ |
| `source`     | 双链，指向 raw 或相关页，如 `"[[Python_V3.0]]"` |
| `source_url` | 原始 URL（网页/本地 `file://`）；纯原创可空        |
##### 7. `tags` — 主题（不表示类型）

|用途|示例|
|---|---|
|学科/主题|`python`、`cesium`、`gis`|
|用途标记|可选；**不要**用 tags 代替 `source_type`|

##### 8. 速查：该用哪个字段

|你想问|看哪个字段|
|---|---|
|这是什么材料？|`type` + `source_type`|
|读没读完？|`status`（raw）|
|真的会了吗？|`understanding_level` + `need_practice`|
|还要动手吗？|`need_practice`|
|从哪来的？|`source` + `source_url` + 目录|
|主题是什么？|`tags`|
### 3. llm wiki流程

Claudian会遵守根目录的 `AGENTS.md`；具体流程提示在 `prompt/ingest.md`、`prompt/lint.md`。

#### 1. 最常用的一条（摄入并生成 Wiki）

```
按 AGENTS.md 和 prompt/ingest.md 处理：
读取 raw/tutorials/你的文件名.md，
更新 wiki/（优先改已有页），
不要改 raw/ 和 notes/，
把变更写到 diff/20260911_主题_diff.md，
最后用 10 行以内总结改了哪些页。
```

##### 第一次建议命令（小步、可审）

```
按根目录 AGENTS.md 和 prompt/ingest.md 处理：
读取 raw/tutorials/20260911_Python入门教程_demo.md，
只更新/新建与「装饰器、闭包」最相关的 wiki 页，
不要改 raw/ 和 notes/，
把完整变更写到 diff/20260911_python_decorator_diff.md，
最后 5 行总结：改了哪些页、diff 在哪。
```

##### 你要做的

1. 打开 `diff/20260911_python_decorator_diff.md` 审内容
2. 认可 → 让它应用，或自己复制进 `wiki/concepts/`
3. 打开 `wiki/overview` 和 `wiki/links`，确认入口没坏
4. 不认可 → 直接说「不对，应该…」，让它重写 diff

更多命令模板见：[[claudian-cheatsheet]]
#### 2. 审核闭环（重要）

1. 它写 `diff/`，**不要**让它悄悄改完 `wiki/` 就完事
2. 你在 Obsidian 打开 diff 审一眼
3. 认可后让它「应用 diff」或你手动合并
4. 看 `wiki/overview` 和仪表盘是否正常

#### 更多可直接粘贴的指令

我加了速查文件：`prompt/claudian-cheatsheet.md`，含：

- 细粒度概念页提炼
- lint 校验（只读报告）
- 问答 + 回写
- 「只建议、不代写」个人原子笔记
- 批量处理 wechat / bookmarks

#### 边界（和系统设计一致）

|它能做|它不该做|
|---|---|
|读 `raw/`，写 `wiki/` / `diff/`|改 `raw/`、乱改 `notes/`|
|给笔记骨架**建议**|替你升 `understanding_level`|
|更新 overview / links|无来源写死结论|

### 4. 日常节奏

```
每天/每次学习
  ① 素材进 raw/（教程/视频/公众号/书签）
  ② 读原文 → 卡住才写 notes/ 原子笔记
  ③ 有余力：Claudian 摄入 → 审 diff → 更新 wiki/

每周（10 分钟）
  ④ 打开「学习仪表盘」
     - 清「待实践」
     - 看「超 30 天没碰」
     - 真用过的改 level
  ⑤ 可选：让 Claudian 跑 lint → report/
```

### 插件 & 脚本
#### 1. Claudian
llm wiki流程的主要工具。

#### 2. Templates
统一用第三方的Templates，这样才能读取脚本[[gen-reading-progress]]脚本，只是满足其语法。如：
```python
# 第三方Templates语法
{{title}} 改为 <% tp.file.title %>
```
>[!danger] 解决第三方Templates语法错误问题
#### 3. Dataview
复习原子笔记的主要工具。用于数据库查询。与moc区别？MOC（手工目录） 只是知识导航的一种；Dataview 更像「把笔记当数据库查」。

两者的差别

||传统 MOC|Dataview|
|---|---|---|
|谁维护|人手写双链|**查询自动生成**|
|更新|容易过期|打开就刷新|
|能力|列目录、导航|筛选、排序、分组、算|
|本质|一篇索引笔记|**查询引擎**|
#### 4. obsidian web clipper
做书签素材的工具。

#### 5. bilibili obsidian clipper
做B站带字幕的视频工具。
#### 6. Local REST API with MCP
与bilibili obsidian clipper插件配合使用。
#### 7. Spaced Repetition
做记忆卡片的工具。
##### 步骤：
1. 做tags标签
2. 卡片怎么做
	1. **单行问答：**
		```markdown
		装饰器的本质是什么？::高阶函数：接收函数，返回新函数
		```
	2. **多行 / 折叠式：**
	
		```markdown
		闭包循环陷阱的解法？
		?
		默认参数 `lambda i=i: i`，在定义时求值
		```

	3. **只复习高亮：**

		```markdown
		编译型是 ==先翻译成机器码再运行==
		```

#### 8. gen-reading-progress脚本
用于生成**文档内链接**使用。

#### 9. video_to_note脚本
用于生成本地视频的**AI字幕**。

## 要点回顾

- 

## 疑问 / 待补充

> [!question] 待补充
> 

## 关联

- 相关原子笔记：[[原子笔记法]]
- 相关 wiki：[[]]
- 来源素材：[[别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云]]
