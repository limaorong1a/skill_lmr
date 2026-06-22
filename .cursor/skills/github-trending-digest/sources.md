# 热门库发现：数据源与方法

按优先级使用以下来源发现"高星 + 近期热度高"的库。优先用 WebFetch 抓页面，WebSearch 补充。

## 1. GitHub Trending（近期热度首选）

抓取趋势页（支持按语言、时间窗口过滤）：

- 综合：`https://github.com/trending`
- 按时间窗口加 `?since=daily|weekly|monthly`，默认用 `weekly`。
- 按语言：`https://github.com/trending/python?since=weekly`（语言名小写，C++ 用 `c++`）。

从页面提取：仓库全名、描述、主语言、总 star、`stars this week/today` 增量。

## 2. GitHub 搜索（高星 + 近期活跃）

用搜索 URL 或 API 组合 star 与时间条件：

- 近期创建的高星新秀：`https://github.com/search?q=stars:>1000+created:>2026-01-01&s=stars&type=Repositories`
- 近期有更新的高星库：`https://github.com/search?q=stars:>5000+pushed:>2026-05-01&s=stars&type=Repositories`
- 按领域加关键词/topic：追加 `topic:llm`、`topic:agent`、`topic:react`、`topic:database` 等。

> 把 URL 中的日期换成"当前日期往前推 1-3 个月"。

## 3. 领域定向 topic 页

- AI/LLM：`https://github.com/topics/llm`、`/topics/agent`、`/topics/rag`、`/topics/machine-learning`
- Web/全栈：`https://github.com/topics/react`、`/topics/nextjs`、`/topics/frontend`
- 后端/数据：`https://github.com/topics/database`、`/topics/distributed-systems`、`/topics/backend`

## 4. 第三方榜单（补充交叉验证）

- WebSearch 关键词示例：`"github trending this week" AI`、`"trending repositories" 2026 site:github.com`
- 社区热度信号：Hacker News、Reddit r/programming、各语言周报（可作热度佐证，不作唯一依据）。

## 候选去重与筛选标准

- 去掉纯 awesome-list / 教程合集（除非用户要这类）。
- 优先：近期 star 增速明显、有实质代码与文档、活跃维护（近 1-2 月有提交）。
- 每领域保留 3-5 个，附 star 数与周增量，交给用户挑选。

## 数据时效提醒

star、增速均为快照，记录抓取日期写进文档。日期相关 URL 用"当前日期"计算，不要硬编码过期日期。
