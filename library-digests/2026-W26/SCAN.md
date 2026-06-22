# 2026-W26 热门项目速览（截至 2026-06-22）

> 数据源：GitHub Trending（本周，综合榜）。⭐为总星，括号内为本周新增。
> 想深挖哪个？回复仓库名即可进入深度解析（模式 B）。

## AI / LLM / Agent

### [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) · `Python` · ⭐37.6k（+8.2k）
- **是什么**：让 AI agent 读取/搜索各大内容平台的命令行工具。
- **解决什么**：agent 缺实时联网能力，且各平台官方 API 割裂又收费。
- **核心能力**：读取&搜索 Twitter / Reddit / YouTube / GitHub / B站 / 小红书；统一 CLI 调用。
- **亮点 / 为什么火**：一个 CLI 打通多平台、零 API 费用，本周暴涨 +8.2k。
- **技术栈**：Python，CLI 工具形态。
- **适合谁**：做联网 agent、舆情/信息聚合的开发者。

### [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) · `JavaScript` · ⭐44.9k（+2.0k）
- **是什么**：主流 AI 产品系统提示词(system prompt)的提取/泄露合集。
- **解决什么**：想直接学习顶级产品如何设计 prompt 与行为约束。
- **核心能力**：收录 Claude / GPT / Gemini / Grok / Cursor / Copilot 等的 prompt，持续更新。
- **亮点 / 为什么火**：一手 prompt 工程素材，研究 LLM 约束设计的最佳范本。
- **技术栈**：文本为主的仓库（JS 标注）。
- **适合谁**：prompt 工程师、做 agent/AI 产品的人。

### [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) · `Shell` · ⭐65.2k（+5.6k）
- **是什么**：面向 AI 编码 agent 的生产级工程技能(skill)集。
- **解决什么**：让 agent 按工程最佳实践干活，并把经验沉淀为可复用 skill。
- **核心能力**：成体系的 skill 集合，覆盖常见工程实践。
- **亮点 / 为什么火**：与你正在做的 skill 同源，是高质量参考样板；作者是知名前端工程师 Addy Osmani。
- **技术栈**：Shell + Markdown 的 skill 形态。
- **适合谁**：写 agent skill、想规范 AI 编码流程的人。

### [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) · `Python` · ⭐10.9k（+2.9k）
- **是什么**：开源的 agentic 视频制作系统。
- **解决什么**：自动化视频生产，把 AI 编码助手变成"视频制作工作室"。
- **核心能力**：12 条流水线、52 个工具、500+ agent skill。
- **亮点 / 为什么火**：号称首个开源 agentic 视频生产系统，复杂 agent 编排范例。
- **技术栈**：Python。
- **适合谁**：做多模态/媒体自动化、研究多 agent 编排的人。

### [google-research/timesfm](https://github.com/google-research/timesfm) · `Python` · ⭐25.1k（+4.1k）
- **是什么**：Google Research 的时间序列预测基础大模型。
- **解决什么**：开箱即用做时序预测，免去逐任务训练。
- **核心能力**：预训练 time-series foundation model，支持零样本/少样本预测。
- **亮点 / 为什么火**：把"基础模型"范式带入时序领域。
- **技术栈**：Python（含预训练模型权重）。
- **适合谁**：做需求预测、运维监控、金融时序的人。

### [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) · `Python` · ⭐9.3k（+4.1k）
- **是什么**：NVIDIA 出的 AI agent skill 安全扫描器。
- **解决什么**：第三方 agent skill 可能含漏洞或恶意代码，需要事前检测。
- **核心能力**：检测漏洞、恶意模式与安全风险。
- **亮点 / 为什么火**：切中 agent 生态"供应链安全"新痛点，NVIDIA 背书。
- **技术栈**：Python，安全扫描工具。
- **适合谁**：使用/分发 agent skill 的团队、安全工程师。

### [LMCache/LMCache](https://github.com/LMCache/LMCache) · `Python` · ⭐9.6k（+1.4k）
- **是什么**：LLM 推理的 KV Cache 加速层。
- **解决什么**：长上下文/重复前缀推理慢、显存紧张。
- **核心能力**：最快的 KV cache 复用，跨请求/跨实例缓存卸载与共享。
- **亮点 / 为什么火**：与 vLLM 等结合可显著降低首 token 延迟。
- **技术栈**：Python，配合推理引擎使用。
- **适合谁**：部署 LLM 推理、做推理性能优化的人。

### [withastro/flue](https://github.com/withastro/flue) · `TypeScript` · ⭐6.4k（+1.3k）
- **是什么**：Astro 团队出品的沙箱(sandbox) agent 框架。
- **解决什么**：需要安全、隔离地运行 agent 代码/工具。
- **核心能力**：沙箱执行环境 + agent 框架原语。
- **亮点 / 为什么火**：知名 Astro 团队背书，主打安全沙箱。
- **技术栈**：TypeScript。
- **适合谁**：构建需隔离执行的 agent 应用的人。

### [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) · `C` · ⭐11.1k（+6.4k）
- **是什么**：高性能代码智能 MCP 服务。
- **解决什么**：让 AI 高效理解大型代码库，同时大幅省 token。
- **核心能力**：把代码库索引成持久知识图谱；毫秒级索引、158 语言、亚毫秒查询、省 99% token。
- **亮点 / 为什么火**：单文件静态二进制、零依赖，本周暴涨 +6.4k。
- **技术栈**：C，单二进制，走 MCP 协议。
- **适合谁**：给编码 agent 接代码检索/记忆能力的人。

## Web / 全栈

### [koala73/worldmonitor](https://github.com/koala73/worldmonitor) · `TypeScript` · ⭐58.5k（+9.2k）
- **是什么**：实时全球情报/态势感知看板。
- **解决什么**：把分散的新闻、地缘、基建信息聚成统一视图。
- **核心能力**：AI 新闻聚合、地缘政治监控、基础设施追踪、实时仪表盘。
- **亮点 / 为什么火**：本周新增最高(+9.2k)，实时数据前端的标杆案例。
- **技术栈**：TypeScript（前端 dashboard）。
- **适合谁**：做实时数据看板、信息聚合产品的前端工程师。

### [penpot/penpot](https://github.com/penpot/penpot) · `Clojure` · ⭐52.7k（+2.6k）
- **是什么**：开源设计与代码协作工具（Figma 替代）。
- **解决什么**：设计-开发协作，且可自托管。
- **核心能力**：矢量设计、设计交付、团队实时协作。
- **亮点 / 为什么火**：少见地用 Clojure/ClojureScript 构建的大型前端。
- **技术栈**：Clojure + ClojureScript，可自托管。
- **适合谁**：设计团队；想研究大型函数式前端架构的人。

### [makeplane/plane](https://github.com/makeplane/plane) · `TypeScript` · ⭐52.5k（+1.5k）
- **是什么**：开源项目管理平台（Jira / Linear / ClickUp 替代）。
- **解决什么**：任务/冲刺/文档/工单一体化管理且可自托管。
- **核心能力**：Tasks、Sprints、Docs、Triage。
- **亮点 / 为什么火**：完整 SaaS 级前后端架构，工程参考价值高。
- **技术栈**：TypeScript 前端 + Python/Django 后端（典型组合）。
- **适合谁**：想读完整 SaaS 架构、需自托管 PM 工具的人。

### [Kong/insomnia](https://github.com/Kong/insomnia) · `TypeScript` · ⭐39.5k（+1.0k）
- **是什么**：跨平台开源 API 客户端。
- **解决什么**：调试 REST / GraphQL / gRPC / WebSocket / SSE。
- **核心能力**：多协议请求、云/本地/Git 三种存储。
- **亮点 / 为什么火**：Electron 复杂桌面应用工程范例，由 Kong 维护。
- **技术栈**：TypeScript + Electron。
- **适合谁**：做 API 工具、桌面应用的开发者。

### [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) · `TypeScript` · ⭐450k（+3.3k）
- **是什么**：免费学编程的开源课程与平台。
- **解决什么**：系统化学习编程、数学与计算机科学。
- **核心能力**：交互式课程、认证体系、社区。
- **亮点 / 为什么火**：星标最高的开源项目之一，超大型代码组织的范例。
- **技术栈**：TypeScript 全栈 monorepo。
- **适合谁**：学习者；想看超大型开源项目如何工程化的人。

## 后端 / 网络 / 基础设施

### [n0-computer/iroh](https://github.com/n0-computer/iroh) · `Rust` · ⭐10.5k（+1.7k）
- **是什么**：Rust 编写的模块化网络栈。
- **解决什么**：IP 易变、NAT 穿透难——主张"用 dial key 直连节点"。
- **核心能力**：基于公钥的节点直连、P2P、可插拔传输。
- **亮点 / 为什么火**：现代 P2P 网络基础设施，工程质量高。
- **技术栈**：Rust，库形态。
- **适合谁**：做分布式、P2P、实时数据同步的人。

### [teslamate-org/teslamate](https://github.com/teslamate-org/teslamate) · `Elixir` · ⭐8.6k（+431）
- **是什么**：自托管的特斯拉数据记录器。
- **解决什么**：记录并可视化自己车辆的行驶、充电、电池数据。
- **核心能力**：数据采集、Grafana 可视化、MQTT 推送。
- **亮点 / 为什么火**：Elixir/Phoenix 实战 + 时序数据栈的完整范例。
- **技术栈**：Elixir(Phoenix) + PostgreSQL + Grafana，Docker 部署。
- **适合谁**：Tesla 车主；学 Elixir、数据采集/可视化栈的人。

## 其他热门（非典型学习向）

### [iptv-org/iptv](https://github.com/iptv-org/iptv) · `TypeScript` · ⭐127k（+7.3k）
- **是什么**：全球公开 IPTV 频道合集。
- **解决什么**：集中收录、维护可用的公开直播源。
- **核心能力**：海量频道清单 + 自动化有效性校验。
- **亮点 / 为什么火**：大型数据集的自动化维护与 CI 校验范例。
- **技术栈**：TypeScript（脚本 + CI）。
- **适合谁**：想要直播源；想学大型数据仓库自动化维护的人。

---
*数据获取日期：2026-06-22 ｜ 由 github-trending-digest 生成（模式 A 速览）*
*注：本周分语言 trending 页抓取异常，仅用综合榜；技术栈中部分细节为依据常识推断，深度解析时以源码为准。*
