---
name: github-trending-digest
description: >-
  Discover trending and high-star GitHub repositories and produce in-depth
  Chinese analysis documents for continuous learning. Use when the user wants to
  research popular/hot GitHub repos, track GitHub trending, learn about
  cutting-edge AI/LLM, web, or backend projects, or generate repository
  deep-dive / code analysis docs (代码库解析/调研/热门库/趋势).
---

# GitHub 热门库解析 (GitHub Trending Digest)

帮助用户持续发现 GitHub 上**高星 + 近期热度高**的代码库，并为每个库产出一份**深度解析文档**，便于实时学习前沿技术。

## 核心原则

- **文档语言**：中文为主，技术术语、API 名、代码原文保留英文。
- **深度优先**：每篇文档要讲清"它解决什么问题、架构怎么搭、关键源码在哪、设计为什么妙、我能学到什么"。
- **可验证**：所有结论尽量来自 README / 源码 / 官方文档，附上链接；不臆造。
- **关注领域**（默认）：AI / LLM / Agent、Web 前端与全栈、后端/数据库/分布式，以及综合热度榜。

## 工作流程

复制此清单并跟踪进度：

```
任务进度:
- [ ] 步骤 1: 发现候选热门库
- [ ] 步骤 2: 与用户确认要解析的库
- [ ] 步骤 3: 逐库深度调研
- [ ] 步骤 4: 按模板生成解析文档
- [ ] 步骤 5: 更新索引 README
```

### 步骤 1: 发现候选热门库

用联网工具拉取近期热门/高星库。优先级数据源与具体方法见 [sources.md](sources.md)。

- 默认时间窗口：**最近一周**（用户可指定 daily / weekly / monthly）。
- 每个关注领域筛 3-5 个候选，连同"综合热度榜"再筛 3-5 个。
- 对每个候选收集：仓库全名(owner/repo)、一句话定位、star 数、近期 star 增长/趋势、主语言、最近一次发版或活跃度。
- 用一个简表把候选列给用户，**不要**直接对所有库写文档（避免浪费）。

### 步骤 2: 与用户确认要解析的库

把候选简表给用户，让其勾选要深入解析哪些（默认可选热度最高的 3 个）。
若用户已明确指定某个库，跳过步骤 1-2 直接解析。

### 步骤 3: 逐库深度调研

对每个选定库，按此顺序收集信息（每条尽量带来源链接）：

1. **定位与背景**：仓库主页、README、官网/文档站。它解决什么问题、面向谁、由谁维护。
2. **核心能力**：主要 feature、对比同类项目的差异化。
3. **技术栈**：语言、关键依赖、运行环境。
4. **架构与目录**：顶层目录结构含义、核心模块划分、数据/控制流。读 README 架构图、`docs/`、关键源文件。
5. **关键源码**：定位 2-4 个最能体现设计精髓的模块/文件，说明其职责与巧妙之处（贴关键代码片段并标注文件路径）。
6. **设计亮点 / 可学知识点**：抽象出可迁移的工程思想、算法、模式（这是文档最有价值的部分）。
7. **上手示例**：最小可运行示例或核心 API 用法。
8. **局限与适用场景**：已知限制、何时该用/不该用。

调研手段：优先 WebFetch 抓 README/docs，WebSearch 补充评测与对比；需要看具体源码时可抓 raw 文件 URL。

### 步骤 4: 按模板生成解析文档

严格使用 [template.md](template.md) 的结构生成 Markdown。

- 输出目录：当前工作区的 `library-digests/`（不存在则创建）。
- 文件命名：`library-digests/<YYYY-Www>/<owner>__<repo>.md`，例如 `library-digests/2026-W26/langchain-ai__langchain.md`。
- 代码片段必须标注来源文件路径；引用结论附链接。

### 步骤 5: 更新索引 README

维护 `library-digests/README.md` 作为总索引：按周/领域列出已解析库，每条含一句话定位 + 文档链接 + star/热度快照。新文档生成后追加或更新对应条目。

## 复用方式（给用户的常用指令）

- "用 github-trending-digest 帮我调研本周 AI 方向的热门库" → 跑完整流程。
- "解析一下 owner/repo" → 跳到步骤 3 直接深度解析指定库。
- "更新本周热门库解析" → 重跑步骤 1，对比已有索引，只补新增/上升的库。

## 注意事项

- star 数与热度是**时间快照**，文档里写明数据获取日期。
- 不确定的信息标注"待核实"，不要编造架构或源码细节。
- 一次解析的库不宜过多（建议 ≤5 个），保证每篇深度。
