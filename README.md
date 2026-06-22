# boy

存放个人 Cursor Skills 与学习资料的仓库。

## Skills

### github-trending-digest

发现 GitHub 上高星 + 近期热门的代码库，并生成中文学习材料，用于持续了解更多前沿项目。

- 位置：`.cursor/skills/github-trending-digest/`
- 四种模式：
  - 速览：「本周热门项目速览」→ 一次扫读 15-30 个项目卡片
  - 深度：「深度解析 owner/repo」→ 单库吃透（架构/源码/可学知识点）
  - 对比：「对比一下 Agent 框架」→ 同类项目横向对比 + 选型建议
  - 追踪：「X 最近更新了什么」→ release/重要 PR 演进
- 自带去重记忆（`library-digests/INDEX.md`），重跑时只补新增/上升的项目。

生成的解析文档默认输出到当前工作区的 `library-digests/` 目录。

### 一键 HTML 学习看板

把调研到的仓库渲染成可交互的离线网页（搜索 / 领域筛选 / 排序 / 随机抽卡 / 学习进度，零依赖，双击即开）：

```bash
python .cursor/skills/github-trending-digest/scripts/build_html.py library-digests/data.json library-digests/index.html
```

打开 `library-digests/index.html` 即可使用。学习进度保存在浏览器本地。

## 在新电脑上恢复

```bash
git clone <本仓库地址>
```

克隆后，Cursor 会自动识别 `.cursor/skills/` 下的项目级 Skill。
若想全局可用，可把 `github-trending-digest` 目录复制到 `~/.cursor/skills/`。
