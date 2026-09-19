---
title: "别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法-腾讯云开发者社区-腾讯云"
type: "raw"
source_type: "bookmark"
tags:
status: "未读"
created: 2026-09-17
source_url: "https://developer.cloud.tencent.com/article/2680461?policyId=1004"
author:
---

## 别再用RAG当“冤大头”！Karpathy的LLM Wiki——知识管理的新解法

## Karpathy的LLM Wiki深度拆解：从理念到落地，如何构建可进化的知识底座

最近圈子里都在聊Karpathy的LLM Wiki，不少人把它和RAG搞混，甚至觉得这只是个“花里胡哨的笔记技巧”——说实话，这是没get到核心。

![](https://developer.qcloudimg.com/http-save/yehe-12521923/208dc1c237e3df684746e5435f495abc.png)

作为OpenAI前核心、特斯拉AI负责人，Karpathy搞出来的东西，肯定不是“小技巧”，而是一套解决「知识碎片化、重复劳动」的底层工作流。

![](https://developer.qcloudimg.com/http-save/yehe-12521923/5987fece806505f4c3906166fa32e38d.png)

我翻了他的原始gist:（https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f），结合Obsidian官方文档、Microsoft GraphRAG的实现逻辑，以及自己调研各大技术博主和实操经验，整理出了这篇全细节指南。

总体可以判断，LLM Wiki不是RAG的替代品，而是「知识编译层」——把零散的原始素材，通过LLM持续整理成结构化、可复用、可进化的Wiki，解决RAG“每次查询都要重新合成、有用结论藏在聊天记录里”的痛点。

### 一、先搞懂：LLM Wiki到底是什么？（拒绝玄学，只讲本质）

Karpathy在gist里给的定义很简洁，但还是很抽象，我重新拆解一下：

LLM Wiki是一套「以Markdown为载体、LLM为维护者、人类为监督者」的知识管理模式，核心是“提前编译知识，而非临时检索合成”。简单说，就是让LLM帮你把散乱的文档、笔记、PR、会议记录，整理成一本“活的百科全书”——你负责丢素材，LLM负责整理、更新、链接，你只需要审核和使用。

#### 1\. 核心三层架构（Karpathy原版架构+我补充的实操细节）

Karpathy在gist里提到了三层结构，但没说清楚每层的具体规范和实操边界，这边稍微做点补全后，直接照着搭就行：

LLM编译/转换

约束/指导

输出/反馈

优质结果回写

Raw Sources 原始素材层

Wiki 结构化知识层

Schema 规则定义层

文档/论文/PR/会议记录/图片/数据集

Markdown文件：摘要/概念页/实体页/对比分析

人类：阅读/审核/引导

LLM：写入/更新/链接/校验

文件夹结构/引用规则/摄入流程

问答行为规范/语法检查规则

应用层：查询/汇报/决策支持

每层的核心要求（必看，否则搭出来就是“伪Wiki”）：

##### （1）Raw Sources 原始素材层：只读不改，保留溯源能力

这层是整个Wiki的“数据源”，核心原则是「原始性、不可修改」——所有素材直接归档，不做任何编辑，目的是为了后续溯源，避免LLM总结出错后无法验证。

实操规范（目录结构）：

```javascript
raw/
├── docs/          # 官方文档、技术手册、论文（PDF/MD格式）
├── prs/           # 代码PR记录、代码评审意见（导出为MD）
├── incidents/     # 故障复盘、问题记录（会议纪要、复盘报告）
├── meetings/      # 会议记录（直接粘贴或导出MD）
├── images/        # 截图、架构图、可视化素材（命名规范：日期_主题.png）
└── others/        # 零散素材（书签导出、笔记碎片、网页剪辑）
```

关键细节：素材命名必须规范，格式为「日期\_主题\_来源」，比如「20260405\_LLM\_Wiki\_Karpathy\_gist.md」，方便LLM识别和链接。

##### （2）Wiki 结构化知识层：LLM主导，人类审核

这层是核心产出，全部由LLM维护，人类只做“审核+引导”，不直接编辑（除非紧急修正错误）。本质是「LLM对原始素材的二次加工」，重点是“结构化、可链接、可更新”。

实操规范（目录结构+文件模板）：

```javascript
wiki/
├── overview.md    # 全局概览：Wiki用途、结构说明、核心链接
├── glossary.md    # 术语表：领域内核心术语、缩写、释义
├── concepts/      # 概念页：核心概念、原理、对比分析（每个概念一个MD）
├── entities/      # 实体页：人物、工具、产品的详细说明（如Obsidian、GraphRAG）
├── incidents/     # 故障知识页：故障原因、解决方案、预防措施
├── decisions/     # 决策记录页：关键决策的背景、依据、结果
└── links.md       # 全局链接索引：所有页面的关联关系
```

文件模板（强制统一，否则LLM会乱写）：

```javascript
---
title: 【页面主题】
status: draft/ready/review  # 状态标记，方便审核
owners: 【负责人】
source_count: 【引用原始素材数量】
last_reviewed: 【最后审核日期】
sensitivity: internal/public  # 敏感级别
---

## 摘要
（1-2句话概括页面核心内容，方便LLM快速识别关联）

## 核心内容
（结构化撰写，用二级/三级标题拆分，避免大段文字）

## 引用来源
（列出所有引用的原始素材路径，格式：../raw/xxx/xxx.md，方便溯源）

## 关联页面
（用Obsidian链接格式 [[页面名称]]，建立页面间关联）

## 待补充/疑问
（LLM标记的不确定点、需要人类补充的内容）
```

##### （3）Schema 规则定义层：约束LLM，避免混乱

这层是“LLM的操作手册”，核心作用是告诉LLM「怎么维护Wiki」，避免LLM乱建页面、乱改内容、遗漏引用——很多人搭LLM Wiki失败，就是因为少了这层。

核心规则文件（必须放在根目录，命名为AGENTS.md）：

```javascript
# LLM Wiki 操作规则（AGENTS）
1.  禁止修改 raw/ 目录下的任何文件，仅可读取；
2.  优先更新现有Wiki页面，禁止随意新建页面（除非没有相关主题）；
3.  所有内容必须引用原始素材，关键结论需标注来源路径，无来源不写入；
4.  不确定的内容，标记为「待补充/疑问」，禁止作为确定结论；
5.  页面关联需合理，禁止强制链接无关页面；
6.  更新Wiki后，必须同步更新 overview.md 和 links.md 的索引；
7.  重要页面（如故障、决策）的修改，需生成diff，等待人类审核后再提交；
8.  禁止删除任何Wiki页面，如需删除，标记为「废弃」，保留历史版本。
```

补充：可以在根目录新增 lint.md 文件，定义语法检查规则（如标题层级、引用格式），让LLM定期自检Wiki的规范性。

#### 2\. 与RAG、GraphRAG的核心区别（终于讲清楚了）

很多人把LLM Wiki和RAG搞混，甚至觉得“有RAG就不需要LLM Wiki”——其实两者是互补关系，不是替代关系。这里用表格对比，一眼看明白：

| 维度 | LLM Wiki | 基础RAG | GraphRAG（Microsoft） |
| --- | --- | --- | --- |
| 核心定位 | 人类可读的知识编译层，持续维护 | 查询时检索合成，即时响应 | 提取实体关系，强化关联检索 |
| 工作方式 | 提前编译，持续更新，人类审核 | 查询时检索chunk，实时合成 | 提取实体/关系，构建图结构，检索关联 |
| 优势 | 知识可积累、可溯源、可读性强 | 灵活高效，适合实时查询 | 擅长大规模关系推理，关联更精准 |
| 劣势 | 需要维护，不适合实时高频更新场景 | 结论不积累，聊天记录易丢失 | 实现复杂，运维成本高 |
| 适用场景 | 个人学习、团队入职、故障复盘、决策记录 | 实时查询、临时检索、快速问答 | 大规模文档、复杂关系推理、企业级知识管理 |

### 二、Karpathy的实操 workflow（还原大佬的真实用法）

Karpathy在gist里只提了大概，后续的X推文补充了很多细节，我们结合自己的实操，把他的 workflow 拆成8步，每一步都有具体命令和配置，直接照搬就能用：

#### 1\. 数据摄入：从Raw到Wiki的转换（核心步骤）

不是简单的“上传素材”，而是让LLM对素材进行“加工转换”——这是LLM Wiki和普通笔记的核心区别。

实操步骤：

1. 1\. 将原始素材（论文、PR、会议记录等）放入 raw/ 对应目录，命名规范遵循「日期\_主题\_来源」；
2. 2\. 编写摄入提示词（放在根目录 prompt/ingest.md），让LLM按照规则处理素材：

```javascript
# 摄入提示词（Ingest Prompt）
请读取 raw/ 目录下的新文档，按照以下规则处理：
1.  优先更新Wiki中已有的相关页面，不新建重复页面；
2.  撰写摘要（不超过7句话），核心内容结构化拆分，避免大段文字；
3.  所有关键结论必须标注引用来源（格式：../raw/xxx/xxx.md）；
4.  不确定的内容，标记为「待补充/疑问」，不强行下结论；
5.  更新对应Wiki页面后，同步更新 overview.md 和 links.md 的索引；
6.  不直接修改Wiki页面，生成diff文件（放在 diff/ 目录），等待人类审核。
```

3\. 执行摄入命令（用Claude Code，Karpathy首选工具）： 注：需提前安装Node.js 16+版本，避免版本过低导致安装失败

```javascript
# 安装Claude Code（需Node.js环境）
# 注意：官方无claude-code独立包，Claude Code是Claude工具的代码交互模式
npm install -g @anthropic-ai/claude

# 导航到Wiki根目录
cd ~/llm-wiki

# 执行摄入（指定raw目录和prompt路径）
claude --ingest ./raw --prompt ./prompt/ingest.md --output ./diff
```

关键细节：diff文件命名规范「日期\_页面名称\_diff.md」，方便审核时对比原始内容和修改内容。

#### 2\. 前端展示：Obsidian作为“Wiki IDE”（Karpathy同款）

Karpathy在gist里明确提到用Obsidian作为前端，不是随便选的——Obsidian的本地Markdown存储、双向链接、图谱视图，完美适配LLM Wiki的需求。

实操配置（Obsidian必做设置）：

1. 1\. 安装Obsidian后，创建Vault，选择LLM Wiki的根目录（~/llm-wiki）；
2. 2\. 安装必备插件（提升效率，Karpathy大概率在用）：
	- • Advanced Tables：优化表格编辑，适配Wiki中的结构化内容；
		- • Backlinker：自动生成页面双向链接，减少LLM的工作量；
		- • Diff Viewer：直接在Obsidian中查看diff文件，方便审核；
		- • Web Clipper：一键将网页内容剪辑为Markdown，存入raw/docs目录。
3. 3\. 开启“图谱视图”：Obsidian左侧菜单栏点击「图谱」，可以直观看到所有Wiki页面的关联关系，方便排查链接遗漏。

重点：不要手动编辑Wiki页面，Obsidian只作为“阅读+审核”的前端，所有修改都通过LLM生成diff后，审核通过再应用，避免破坏LLM维护逻辑。

#### 3\. 问答交互：小体量无需复杂RAG（Karpathy亲测）

Karpathy在X推文中提到，他的研究Wiki有100篇文章、40万字（单篇平均4000字），这个体量下（对应wiki目录下100个以内Markdown页面，单页面平均300-800字），不需要复杂的RAG基础设施——LLM直接读取Wiki文件，就能给出精准答案。

实操命令（Claude Code直接查询）：

```javascript
# 导航到Wiki根目录
cd ~/llm-wiki

# 启动Claude Code，直接查询
claude

# 输入查询示例（自然语言即可）
"总结wiki/concepts/llm_wiki.md的核心内容，引用来源"
"查找所有与RAG相关的Wiki页面，并说明它们的关联关系"
"我要写一篇关于LLM Wiki的技术分享，需要用到哪些页面的内容？"
```

关键细节：查询时，Claude会自动读取Wiki页面和关联的原始素材，给出带来源标注的答案，避免 hallucination（幻觉）。

#### 4\. 结果回写：让知识持续积累（核心亮点）

这是LLM Wiki最核心的优势——查询的优质结果，可以回写到Wiki中，形成“查询→合成→回写→优化”的闭环，让Wiki越用越完善。

实操步骤：

1. 1\. 查询得到优质结果后，让Claude生成回写提示，指定要更新的Wiki页面；
2. 2\. Claude生成diff文件，放入 diff/ 目录；
3. 3\. 人类审核diff，确认无误后，执行回写命令：

回写diff文件（指定diff路径和目标Wiki页面）： 注：diff文件需符合Markdown diff规范，若提示“invalid diff”，需检查diff文件格式（如开头需标注---/+++区分原始/修改内容）

示例：查询“LLM Wiki与RAG的区别”后，将优质对比内容回写到 wiki/concepts/llm\_wiki\_vs\_rag.md 页面，丰富Wiki内容。

#### 5\. 质量校验：LLM自检查，人类做终审

Karpathy提到，他会用LLM对Wiki进行“健康检查”，避免错误内容固化——这一步不能少，否则Wiki会慢慢变成“错误 [知识库](https://cloud.tencent.com/product/lexiang?from_column=20065&from=20065) ”。

实操配置：

1. 1\. 编写校验提示词（放在 prompt/lint.md）：

```javascript
# 校验提示词（Lint Prompt）
请对Wiki所有页面进行以下检查：
1.  检查引用来源是否完整，无来源的关键结论是否标记为疑问；
2.  检查页面关联是否合理，无强制链接、无效链接；
3.  检查格式是否符合模板，标题层级、标签是否规范；
4.  检查内容是否存在矛盾，同一概念的释义是否一致；
5.  检查是否有重复页面，或内容过于零散的页面，提出合并建议；
6.  生成校验报告（放在 report/ 目录），标注问题页面和修改建议。
```

定期执行校验命令（建议每周1次）： 注：校验报告将生成在report/目录下，包含“问题页面ID、错误类型、修改建议”，人类需对照报告生成diff文件，审核后回写Wiki

```javascript
# 执行校验
claude --lint ./wiki --prompt ./prompt/lint.md --report ./report
```

重点：校验报告必须由人类审核，LLM只提修改建议，不直接修改Wiki，避免引入新的错误。

#### 6\. 工具扩展：从基础到进阶（循序渐进）

Karpathy在推文中提到，随着Wiki体量增长，会逐步添加工具——不要一开始就上复杂架构，循序渐进最稳妥：

1. 1\. 初期（wiki目录下100个以内Markdown页面，单页面平均300-800字）：Obsidian + Markdown + Claude Code + Git（版本控制）；
2. 2\. 中期（wiki目录下100-500个Markdown页面，单页面平均300-800字）：添加qmd（轻量搜索工具）；
3. 3\. 后期（wiki目录下500个以上Markdown页面，单页面平均300-800字）：添加GraphRAG（强化关系检索）；

#### 7\. 进阶探索：从Wiki到模型微调（Karpathy的未来设想）

Karpathy提到，当Wiki体量足够大（比如wiki目录下1000个以上Markdown页面，单页面平均300-800字），可以将Wiki内容作为合成数据，用于模型微调——需先对Wiki内容进行人工审核、去重、规范格式，再作为微调数据集，让模型“记住”Wiki中的知识，减少查询时的读取成本。

实操思路（目前可落地）：

1. 1\. 用Claude Code提取Wiki中的核心内容，生成微调数据集（格式：JSONL）；
2. 2\. 用Claude Code提取Wiki中的核心内容，生成JSONL格式的微调数据集（格式参考Anthropic官方规范）；
3. 3\. 使用Anthropic Claude 3 Fine-tuning API上传数据集进行微调（需在Anthropic官网申请API Key，配置请求参数：model=claude-3-opus-2024-02-29，input\_type=jsonl）；

注意：微调成本较高，个人用户可暂时不考虑，团队用户可根据需求尝试。

#### 8\. 团队协作：从个人到团队的适配（Karpathy提到的产品机会）

Karpathy在推文中说，LLM Wiki不只是个人工作流，更是一个“潜在的产品机会”——核心是解决团队知识碎片化的问题。

团队版实操配置（基于个人版扩展）：

1. 1\. 团队版LLM Wiki需在个人版基础上，增加“权限管控、协作流程、多工具集成”三大核心模块，目录结构优化如下（贴合团队协作场景，可直接复用）：

```javascript
llm-wiki-team/
├── raw/                # 原始素材层（团队共享，按部门/项目分类）
│   ├── department/     # 各部门专属素材（如技术部、设计部）
│   ├── project/        # 各项目专属素材（按项目ID分类）
│   ├── public/         # 团队公共素材（培训资料、通用规范）
│   └── sensitive/      # 敏感素材（权限管控，仅指定人员可访问）
├── wiki/               # 结构化知识层（团队共享，按业务模块分类）
│   ├── overview.md     # 团队Wiki概览、使用规范、核心负责人
│   ├── glossary.md     # 团队通用术语、业务缩写、接口释义
│   ├── business/       # 业务模块页面（按业务线分类）
│   ├── project/        # 项目专属页面（按项目ID分类，含决策、复盘）
│   ├── department/     # 部门专属页面（如技术部故障库、设计部规范）
│   └── links.md        # 全局链接索引，关联各模块页面
├── prompt/             # 团队专属提示词（适配团队业务场景）
│   ├── ingest.md       # 摄入提示词（增加部门/项目标签规则）
│   ├── lint.md         # 校验提示词（增加团队规范校验规则）
│   └──协作_prompt.md   # 协作提示词（如PR审核、素材分配提示）
├── diff/               # diff文件目录（按部门/项目分类，便于审核）
├── report/             # 校验报告目录（含团队Wiki健康度报告）
├── AGENTS.md           # 团队版操作规则（增加权限、协作相关规则）
├── permission.md       # 权限管控说明（明确各角色操作权限）
└── README.md           # 团队Wiki使用指南（新人上手必备）
```

1. 2\. 版本控制：用GitHub/GitLab托管Wiki仓库，核心规范：主分支（main）保护，禁止直接推送，仅允许通过PR合并diff文件；

### 三、不同人群的落地案例（直接照搬，零门槛）

LLM Wiki不是只有开发者能用，设计师、产品经理、普通人都能搭，我整理了3个最常见的案例，每个案例都有完整的目录结构和实操要点：

#### 案例1：开发者 - legacy项目入职Wiki（解决新人上手慢的问题）

很多legacy项目（遗留项目）的知识，都藏在PR、故障复盘、老员工的脑子里，新人入职要花几周才能上手——用LLM Wiki就能解决。

目录结构（核心简化版）：

```javascript
llm-wiki-legacy/
├── raw/
│   ├── docs/          # 项目文档、接口文档、架构图
│   ├── prs/           # 核心PR记录、代码评审意见
│   ├── incidents/     # 故障复盘报告、问题记录
│   └── meetings/      # 项目会议记录、技术评审纪要
├── wiki/
│   ├── overview.md    # 项目概览、技术栈、核心功能
│   ├── glossary.md    # 项目术语、接口缩写、域名释义
│   ├── systems.md     # 系统架构、服务依赖关系
│   ├── incidents.md   # 故障分类、解决方案、预防措施
│   └── decisions.md   # 关键技术决策、选型依据
├── prompt/
│   ├── ingest.md      # 摄入提示词
│   └── lint.md        # 校验提示词
├── diff/              # diff文件目录
├── report/            # 校验报告目录
├── AGENTS.md          # 操作规则
└── README.md          # 项目说明
```

核心要点：重点整理「故障复盘」和「决策记录」，新人遇到问题时，直接查询Wiki就能找到解决方案，不用反复问老员工。

#### 案例2：设计师 - 品牌/UX研究Wiki（解决灵感碎片化问题）

设计师的灵感、参考素材，通常散在Figma、浏览器书签、截图文件夹里，时间久了就忘了“为什么保存”——LLM Wiki能帮你保留灵感和背后的思考。

目录结构（核心简化版）：

```javascript
llm-wiki-design/
├── raw/
│   ├── screenshots/   # 优秀设计截图、落地页截图
│   ├── references/    # 设计参考文档、UX研究报告
│   ├── interviews/    # 用户访谈纪要、需求反馈
│   └── comments/      # 自己的设计思考、评审意见
├── wiki/
│   ├── overview.md    # 设计Wiki用途、结构说明
│   ├── visual-patterns.md  # 视觉设计模式、参考案例
│   ├── onboarding-flows.md # 引导页设计参考、亮点分析
│   ├── brand-voice.md # 品牌语气、用词规范、禁忌
│   └── user-pain-points.md # 用户痛点、设计解决方案
├── prompt/
│   ├── ingest.md      # 摄入提示词（重点强调设计思路提取）
│   └── lint.md        # 校验提示词
├── diff/
├── report/
├── AGENTS.md
└── README.md
```

核心要点：让LLM提取每张截图、每篇参考的「设计亮点」和「适用场景」，避免灵感变成“无意义的图片堆”。

#### 案例3：普通人 - 个人学习Wiki（解决知识碎片化问题）

不管是学编程、学理财，还是学历史，零散的笔记、教程、书籍摘要，时间久了就会遗忘——LLM Wiki能帮构建系统化的知识体系。

目录结构（核心简化版）：

```javascript
llm-wiki-personal/
├── raw/
│   ├── articles/      # 学习文章、教程链接导出
│   ├── book-notes/    # 书籍摘要、读书笔记
│   ├── videos/        # 视频教程笔记、关键知识点
│   └── practice/      # 练习记录、错题整理
├── wiki/
│   ├── overview.md    # 学习计划、知识体系概览
│   ├── concepts/      # 核心概念、原理拆解
│   ├── practice.md    # 练习总结、错题分析
│   └── resources.md   # 学习资源、工具推荐
├── prompt/
│   ├── ingest.md      # 摄入提示词（重点强调知识点提炼）
│   └── lint.md        # 校验提示词
├── diff/
├── report/
├── AGENTS.md
└── README.md
```

核心要点：每天花10分钟，将当天的学习素材放入raw目录，让LLM整理成Wiki页面，长期坚持，就能形成自己的知识体系。

### 四、避坑指南（我踩过的坑，你别再踩）

搭LLM Wiki的过程中，踩了几个坑，浪费了不少时间：

#### 1\. 坑1：让LLM自由发挥，不设Schema规则

后果：LLM乱建页面、内容格式混乱、引用缺失，Wiki越搭越乱，最后无法使用；

解决方案：必须先写好AGENTS.md和文件模板，让LLM严格按照规则操作，禁止自由发挥。

#### 2\. 坑2：手动编辑Wiki页面，破坏LLM维护逻辑

后果：LLM无法识别手动修改的内容，后续更新会覆盖手动修改，导致内容丢失；

解决方案：所有修改都通过“LLM生成diff→人工审核→回写”的流程，禁止手动编辑Wiki页面。

#### 3\. 坑3：忽视原始素材的溯源，导致LLM hallucination

后果：LLM总结的内容没有来源，无法验证真实性，慢慢变成“错误知识库”；

解决方案：强制要求LLM标注所有关键结论的来源，raw目录保持只读，方便随时溯源。

#### 4\. 坑4：一开始就上复杂架构（GraphRAG、向量索引）

后果：运维成本高，学习曲线陡，反而影响使用积极性，最后半途而废；

解决方案：循序渐进，从Obsidian+Claude Code开始，随着Wiki体量增长，再逐步添加工具。

#### 5\. 坑5：不做定期校验，错误内容固化

后果：LLM的小错误的会慢慢积累，最后Wiki失去参考价值；

解决方案：或许需要定期执行一次LLM校验，人工审核校验报告，及时修正错误。

### 五、工具选型汇总（Karpathy同款，按需选择）

整理了所有用到的工具，包括替代方案，按需选择，不用盲目跟风：

| 工具类型 | 首选工具（Karpathy同款） | 替代方案 | 适用场景 |
| --- | --- | --- | --- |
| 前端编辑器 | Obsidian | VS Code、Typora、iA Writer | 所有场景，Obsidian最适配双向链接和图谱视图 |
| LLM工具 | Claude Code | GPT-4 API、Gemini Code Assist | 个人用户用Claude Code，团队用户可考虑GPT-4 API（集成更灵活） |
| 版本控制 | Git + GitHub/GitLab | GitLab、Gitea | 所有场景，用于备份和团队协作 |
| 轻量搜索 | qmd | ripgrep、fzf | Wiki体量（wiki目录下Markdown页面）100-500个，单页面平均300-800字，需要快速搜索 |
| 关系检索 | Microsoft GraphRAG | LlamaIndex、LangChain Graph | Wiki体量（wiki目录下Markdown页面）500个以上，单页面平均300-800字，需要复杂关系推理 |
| 团队协作 | GitHub PR + Slack | GitLab CI + Teams | 团队用户，用于diff审核和通知 |

### 六、总结：LLM Wiki的核心价值（不止是“笔记”）

很多人看完Karpathy的gist，觉得LLM Wiki只是“高级笔记”——其实不然，它的核心价值是「让知识从“零散碎片”变成“可进化、可复用的资产”」。

对个人而言，它是你的“第二大脑”，帮你记住所有学到的知识，不用再担心遗忘；对团队而言，它是“团队知识库”，帮你沉淀隐性知识，减少重复劳动，降低新人入职成本。

最后提醒一句：LLM Wiki不是“一劳永逸”的，它需要你持续投入时间，上传素材、审核diff、优化规则——但只要坚持下来，你会发现，它能帮你节省大量的时间和精力。

现在，打开你的终端，按照上面的步骤，搭一个属于自己的LLM Wiki吧——这可能是你2026年最有价值的技术投资之一。

### 附录：参考资料（Karpathy原始gist及相关文档）

1. 1\. Andrej Karpathy, LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
2. 2\. Obsidian官方文档: https://help.obsidian.md/
3. 3\. Microsoft GraphRAG 官方文档: https://learn.microsoft.com/en-us/graph/rag/overview
4. 4\. qmd GitHub README: https://github.com/qmd-dev/qmd
5. 5\. OWASP LLM Prompt Injection 安全指南: https://owasp.org/www-project-top-ten-for-large-language-model-applications/

---

# 学习附录

## 书签卡

| 字段 | 值 |
| --- | --- |
| URL | https://developer.cloud.tencent.com/article/2680461?policyId=1004 |
| 为什么存 | |
| 什么时候用 | |

## 阅读进度

> 用 Templater `gen-reading-progress` 生成（~~脚本~~碰到「学习附录」会停）。
> 纯参考书签可删掉本段。未勾选会出现在 [[dashboards/素材收件箱]]。
> 标记：✅ 已掌握 / 🔴 急需 / 🟡 了解即可 / ⚪ 暂跳过

- [ ] 
  - [ ] 

## 拆解索引

```dataview
LIST
FROM "notes"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句，禁止大段抄原文。
