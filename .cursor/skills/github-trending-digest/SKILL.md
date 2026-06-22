---
name: github-trending-digest
description: >-
  Discover trending and high-star GitHub repositories and produce Chinese
  learning material for them: quick breadth scans, in-depth deep-dives,
  side-by-side comparisons, and release/trend tracking. Use when the user wants
  to research popular/hot GitHub repos, explore many new projects, track GitHub
  trending, compare similar tools, follow a repo's latest releases, or learn
  cutting-edge AI/LLM, web, or backend projects (代码库解析/调研/速览/对比/热门库/趋势).
---

# GitHub 热门库解析 (GitHub Trending Digest)

帮助用户持续发现 GitHub 上**高星 + 近期热门**的代码库，并按需产出不同深度的学习材料，让其又快又深地了解更多前沿项目。

## 核心原则

- **文档语言**：中文为主，技术术语、API 名、代码原文保留英文。
- **可验证**：结论尽量来自 README / 源码 / 官方文档并附链接；不确定标"待核实"，绝不臆造。
- **不重复**：每次先读已解析索引，优先覆盖**新项目**，持续扩大视野。
- **快照标注**：star/热度是时间快照，文档内写明数据获取日期。
- **关注领域**（默认）：AI/LLM/Agent、Web 前端与全栈、后端/数据库/分布式，以及综合热度榜。

## 四种模式（按需选用）

| 模式 | 目标 | 产出 | 适用 |
|---|---|---|---|
| A. 速览 | 一次了解**很多**项目 | 15-30 条一句话卡片清单 | "本周都火了啥" |
| B. 深度 | 吃透**少量**项目 | 每库一篇深度解析（≤5 个） | "讲透 owner/repo" |
| C. 对比 | 看懂一个**赛道** | 同类项目横向对比表 | "几个 Agent 框架怎么选" |
| D. 追踪 | 跟进**最新动态** | 某库 release/重要 PR 演进 | "X 最近更新了啥" |

模板均在 [template.md](template.md)；发现库的数据源与方法见 [sources.md](sources.md)。

不确定用户要哪种时，默认先跑**模式 A 速览**给全貌，再问要对哪些进入模式 B 深度。

## 统一前置：去重记忆

任何模式开始前，先读 `library-digests/INDEX.md`（不存在则视为空）。它记录所有已处理过的库（owner/repo + 模式 + 日期）。

- 速览/对比时：已深度解析过的库可标注"✅已解析"，把发现名额留给新项目。
- 重跑"更新本周"时：跳过近期已覆盖的，只列**新增或热度明显上升**的。

每次产出后，把涉及的库追加/更新进 `INDEX.md`。

## 模式 A：速览（广度）

```
- [ ] 1. 读 INDEX.md 去重
- [ ] 2. 按领域抓候选（每领域 5-8 个 + 综合榜 5-8 个）
- [ ] 3. 用「速览卡片」模板批量输出
- [ ] 4. 写入 library-digests/<YYYY-Www>/SCAN.md，更新 INDEX.md
- [ ] 5. 问用户：要对哪几个进入深度模式？
```

每条卡片只需：`owner/repo` · 一句话定位 · 1 个亮点 · 主语言 · star（近期增量）· 链接。**不深挖源码**，追求覆盖面。

## 模式 B：深度解析

```
- [ ] 1. 读 INDEX.md，确认目标库未重复
- [ ] 2. 深度调研（见下）
- [ ] 3. 用「深度解析」模板生成
- [ ] 4. 存 library-digests/<YYYY-Www>/<owner>__<repo>.md，更新 INDEX.md
```

调研顺序（每条尽量带来源链接）：
1. 定位与背景（解决什么问题、面向谁、谁维护）
2. 核心能力与差异化
3. 技术栈与依赖
4. 架构与目录结构（读 README 架构图、`docs/`、关键源文件）
5. 关键源码：定位 2-4 个最能体现设计精髓的模块/文件，贴片段并标注路径
6. 设计亮点 / 可迁移知识点（**最有价值部分**）
7. 上手示例（最小可运行）
8. 局限与适用场景
9. TL;DR + 自测问题（帮助记忆）

调研手段：WebFetch 抓 README/docs，WebSearch 补评测对比，需要看源码时抓 raw 文件 URL；结构化检索用 GitHub Search API（见 sources.md）。

## 模式 C：横向对比

给定一个赛道（用户指定，或从速览里挑同类），选 3-6 个代表项目，用「对比表」模板输出：

- 维度示例：定位、star/活跃度、核心机制、性能/规模、生态与集成、学习曲线、许可、适合场景。
- 表后给**选型建议**：什么需求选哪个。
- 存 `library-digests/compare/<赛道名>.md`。

## 模式 D：动态追踪

对指定库追踪"最近发生了什么"：

- 抓 Releases 页 / CHANGELOG，总结最近 2-3 个版本的关键变更与意义。
- 抓近期合并的重要 PR / 里程碑 issue，提炼方向趋势。
- 输出追加到该库深度文档的"动态"小节，或单独 `library-digests/tracking/<owner>__<repo>.md`。

## 索引与输出约定

- 输出根目录：当前工作区 `library-digests/`（不存在则创建）。
- `library-digests/INDEX.md`：总索引/去重表，按领域+周列出所有已处理库，含一句话定位、模式标记、文档链接、star 快照。
- 文件命名：深度 `<owner>__<repo>.md`；速览 `SCAN.md`；对比 `compare/<赛道>.md`；追踪 `tracking/<owner>__<repo>.md`。

## 复用方式（给用户的常用指令）

- "本周热门项目速览" → 模式 A
- "深度解析 owner/repo" → 模式 B
- "对比一下 RAG 框架 / Agent 框架" → 模式 C
- "X 最近更新了什么" → 模式 D
- "更新本周热门库解析" → 读 INDEX 去重，只补新增/上升项目

## 注意事项

- 一次深度解析的库 ≤5，保证质量；速览可多但每条简短。
- 日期相关的搜索 URL 用"当前日期"计算，不要硬编码过期日期。
- 每篇文档末尾标注数据获取日期与生成来源。
