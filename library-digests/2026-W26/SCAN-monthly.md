# 2026-06 月度榜新发现（截至 2026-06-22）

> 数据源：GitHub Trending（本月，综合榜）。已用 INDEX 去重，仅列与上次周榜不重叠的新项目。
> ⭐为总星，括号内为本月新增。想深挖哪个？回复仓库名进入深度解析（模式 B）。

## AI 应用 / 模型

### [microsoft/markitdown](https://github.com/microsoft/markitdown) · `Python` · ⭐157.6k（+33.2k/月）
- **是什么**：微软出的"文件/Office 文档 → Markdown"转换工具。
- **解决什么**：把 PDF/Word/PPT/Excel 等转成适合喂给 LLM 的干净 Markdown。
- **核心能力**：多格式批量转换、尽量保留结构。
- **亮点 / 为什么火**：LLM 数据预处理刚需，微软背书，星标已 157k。
- **技术栈**：Python，库/CLI。
- **适合谁**：做 RAG、文档处理、数据管道的人。

### [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) · `Python` · ⭐91.2k（+13.1k/月）
- **是什么**：用 AI 大模型一键生成高清短视频。
- **解决什么**：批量做短视频成本高、流程繁琐。
- **核心能力**：按主题自动生成文案、配素材、字幕、配音并合成成片。
- **亮点 / 为什么火**：一键出片的国民级项目。
- **技术栈**：Python（LLM + 视频合成）。
- **适合谁**：做自媒体/营销短视频自动化的人。

### [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) · `TypeScript` · ⭐32.5k（+8.7k/月）
- **是什么**：开源版 Google NotebookLM。
- **解决什么**：本地/可控地做资料笔记 + AI 问答。
- **核心能力**：导入资料、AI 摘要与问答，比官方更灵活。
- **亮点 / 为什么火**：自托管替代闭源产品。
- **技术栈**：TypeScript 全栈。
- **适合谁**：做个人知识库、研究型用户。

### [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) · `TypeScript` · ⭐11.5k（+8.1k/月）
- **是什么**：聚合 16 家免费 LLM 额度的 OpenAI 兼容代理。
- **解决什么**：把多家免费额度统一到一个 `/v1` 端点。
- **核心能力**：智能路由、自动故障转移、密钥加密，约 1.7B token/月。
- **亮点 / 为什么火**：一个端点白嫖多家模型。
- **技术栈**：TypeScript 代理服务。
- **适合谁**：个人实验、想省 API 成本的开发者（作者注明仅限个人实验）。

## AI 编码 agent / 终端工具

### [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) · `Go` · ⭐23.8k（+18.5k/月）
- **是什么**：DeepSeek 原生的终端 AI 编码 agent。
- **解决什么**：在终端里用 DeepSeek 持续做编码任务。
- **核心能力**：围绕 prefix-cache 稳定性优化，可长驻后台运行。
- **亮点 / 为什么火**：针对 DeepSeek 缓存特性做深度工程优化，本月 +18.5k。
- **技术栈**：Go，CLI。
- **适合谁**：用 DeepSeek、偏好终端编码 agent 的人。

### [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) · `TypeScript` · ⭐14.1k（+8.2k/月）
- **是什么**：终端 AI 编码 agent。
- **解决什么**：在终端高效编码并带完整工具链。
- **核心能力**：hash 锚定编辑、优化的工具 harness、LSP、Python、浏览器、子 agent。
- **亮点 / 为什么火**：工具链齐全、编辑用 hash 锚定更稳。
- **技术栈**：TypeScript。
- **适合谁**：想研究编码 agent 工具设计的人。

### [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) · `Rust` · ⭐6.8k（+4.7k/月）
- **是什么**：终端里的 agent 多路复用器(multiplexer)。
- **解决什么**：同时管理/编排多个 agent。
- **核心能力**：在终端并行驾驭多个 agent。
- **亮点 / 为什么火**：Rust 写的轻量 agent 管理器。
- **技术栈**：Rust，CLI。
- **适合谁**：同时跑多个 agent 的重度用户。

## 代码知识图谱 / 代码智能

### [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) · `TypeScript` · ⭐66.0k（+49.3k/月）
- **是什么**：把任意代码变成可交互的知识图谱。
- **解决什么**：快速理解陌生代码库，可搜索、可问答。
- **核心能力**：生成"教学型"交互图谱，兼容 Claude Code/Codex/Cursor/Copilot/Gemini CLI。
- **亮点 / 为什么火**：本月暴涨 +49k，与"用图谱学代码"思路高度契合。
- **技术栈**：TypeScript。
- **适合谁**：读大型代码库、做代码理解工具的人。

### [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) · `TypeScript` · ⭐53.1k（+40.9k/月）
- **是什么**：预索引的代码知识图谱，代码变更自动同步。
- **解决什么**：给编码 agent 提供低 token、100% 本地的代码上下文。
- **核心能力**：预索引、增量自动同步、本地运行，支持多家 agent。
- **亮点 / 为什么火**：本地化 + 省 token + 省工具调用，本月 +40.9k。
- **技术栈**：TypeScript。
- **适合谁**：给 agent 接本地代码索引的人。

## Agent Skills / Plugins 生态（与你正在做的事高度相关）

### [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · `Python` · ⭐45.7k（+19.3k/月）
- **是什么**：研究任意话题"最近动态"的 agent skill。
- **解决什么**：跨平台聚合并综合最新信息。
- **核心能力**：跨 Reddit/X/YouTube/HN/Polymarket/web 检索，生成有依据的综述。
- **亮点 / 为什么火**：和你做的"趋势调研 skill"思路一致，**可直接借鉴其检索+综合做法**。
- **技术栈**：Python，skill。
- **适合谁**：做调研/趋势追踪的人（对你参考价值最大）。

### [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · `JavaScript` · ⭐48.9k（+29.9k/月）
- **是什么**：给 AI "审美/品味"的 skill。
- **解决什么**：避免 AI 产出平庸、模板化内容。
- **核心能力**：约束生成风格、提升输出质感。
- **亮点 / 为什么火**：聚焦"输出质量"这一软痛点，本月 +29.9k。
- **技术栈**：JavaScript，skill。
- **适合谁**：在意 AI 输出质感的写作/产品人。

### [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · `Python` · ⭐21.7k（+9.3k/月）
- **是什么**：Anthropic 官方面向知识工作者的 Claude 插件库。
- **解决什么**：在 Claude Cowork 里用现成插件干活。
- **核心能力**：开源插件集合。
- **亮点 / 为什么火**：官方出品，是了解插件规范的权威参考。
- **技术栈**：Python。
- **适合谁**：做 Claude 插件/skill 的人。

### [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) · `Python` · ⭐18.3k（+10.8k/月）
- **是什么**：754 个结构化网络安全 agent skill。
- **解决什么**：给安全 agent 提供成体系的现成能力。
- **核心能力**：映射 MITRE ATT&CK/NIST CSF/ATLAS 等 5 大框架，26 个安全域，遵循 agentskills.io 标准。
- **亮点 / 为什么火**：超大规模 skill 库 + 跨 20+ 平台兼容，是 skill 标准化的范例。
- **技术栈**：Python，skill 集。
- **适合谁**：安全工程、研究 skill 标准化的人。

### [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · `Markdown` · ⭐20.5k（+8.9k/月）
- **是什么**：产品经理(PM)的 agentic skill 市场。
- **解决什么**：用 agent 覆盖产品发现→策略→执行→增长全流程。
- **核心能力**：100+ skill / 命令 / 插件。
- **亮点 / 为什么火**：把 PM 工作流系统地 agent 化。
- **技术栈**：以 Markdown skill 为主。
- **适合谁**：产品经理、做领域 skill 包的人。

### [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) · `Markdown` · ⭐11.8k（+8.0k/月）
- **是什么**：去除"AI 腔"的写作 skill 文件。
- **解决什么**：让 AI 写的文字更像人、去套路。
- **核心能力**：移除 AI tells 的规则集。
- **亮点 / 为什么火**：单文件 skill，轻量实用。
- **技术栈**：Markdown skill。
- **适合谁**：用 AI 做写作的人。

### [openai/plugins](https://github.com/openai/plugins) · `JavaScript` · ⭐3.3k（+2.1k/月）
- **是什么**：OpenAI 官方插件库。
- **解决什么**：扩展 OpenAI 生态能力。
- **核心能力**：官方插件集合。
- **亮点 / 为什么火**：官方规范参考。
- **技术栈**：JavaScript。
- **适合谁**：做 OpenAI 生态扩展的人。

## 学习资源

### [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) · `Python` · ⭐35.6k（+25.1k/月）
- **是什么**：从零学 AI 工程的实战教程。
- **解决什么**：系统学习并动手构建 AI 工程项目。
- **核心能力**：Learn it / Build it / Ship it 的实战路线。
- **亮点 / 为什么火**：实战导向，本月 +25k。
- **技术栈**：Python（含 notebooks）。
- **适合谁**：想系统入门 AI 工程的人。

## 系统 / 基础设施

### [apple/container](https://github.com/apple/container) · `Swift` · ⭐39.5k（+12.8k/月）
- **是什么**：Apple 官方在 Mac 上用轻量 VM 跑 Linux 容器的工具。
- **解决什么**：在 Apple Silicon 上更高效地运行容器。
- **核心能力**：基于轻量虚拟机的 Linux 容器，针对 Apple 芯片优化。
- **亮点 / 为什么火**：Apple 官方出品，Swift 编写。
- **技术栈**：Swift，CLI。
- **适合谁**：在 Mac 上做容器/开发环境的人。

---
*数据获取日期：2026-06-22 ｜ 由 github-trending-digest 生成（模式 A 速览·月度榜去重）*
*注：GitHub Search API 本次因网络超时未启用，仅用月度 trending 综合榜；技术栈部分细节为依据描述推断。*
