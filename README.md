# boy

存放个人 Cursor Skills 与学习资料的仓库。

## Skills

### github-trending-digest

发现 GitHub 上高星 + 近期热门的代码库，并生成深度中文解析文档，用于持续学习前沿技术。

- 位置：`.cursor/skills/github-trending-digest/`
- 用法：在 Cursor 中说「用 github-trending-digest 调研本周 AI 方向热门库」或「解析一下 owner/repo」。

生成的解析文档默认输出到当前工作区的 `library-digests/` 目录。

## 在新电脑上恢复

```bash
git clone <本仓库地址>
```

克隆后，Cursor 会自动识别 `.cursor/skills/` 下的项目级 Skill。
若想全局可用，可把 `github-trending-digest` 目录复制到 `~/.cursor/skills/`。
