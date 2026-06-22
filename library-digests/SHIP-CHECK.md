# 学习引擎 Ship-Check 报告

> 方法来源：[phuryn/pm-skills](https://github.com/phuryn/pm-skills) 的 `pm-ai-shipping` 插件
> 应用方法：`shipping-artifacts`（应有文档清单）+ `intended-vs-implemented`（声称 vs 实际，附证据）+ `strategy-red-team`（按最便宜的验证排序风险）
> 审查对象：`skill_lmr` 项目（github-trending-digest skill + 学习引擎网页）
> 日期：2026-06-22

---

## 1. Shipping Artifacts 清单（AI 应用应有的可审查文档）

| 文档项 | 是否需要 | 现状 | 结论 |
|---|---|---|---|
| 架构说明（数据流/模块） | 是 | 仅 README 片段 | ⚠️ 缺独立架构文档 |
| 用户/权限流 | 否（纯前端、无登录） | — | ✅ 不适用 |
| 权限模型 | 否 | — | ✅ 不适用 |
| 变量/密钥清单 | 是 | 无任何密钥，纯本地、零网络 | ✅ 无密钥泄露面 |
| 测试覆盖地图 | 是 | **无任何测试/校验** | 🔴 缺失 |

结论：本项目攻击面小（无密钥、无后端），主要短板是**缺测试**和**缺架构文档**。

---

## 2. Intended vs Implemented（声称 vs 实际）

逐条核对 SKILL.md / README 声称的能力与 `build_html.py` 实际代码。

| # | 声称（intended） | 实际（implemented，证据） | 判定 |
|---|---|---|---|
| 1 | 📅 每日一库：当天固定、推未学的 | `todayRepo()` 按日期 hash 取未学池，确定性选取（build_html.py:168-176） | ✅ 一致 |
| 2 | 🧭 选型顾问：需求→推荐→对比 | `advise()` 关键词打分 + `renderCompare()` 生成对比表（:303-345） | ✅ 一致 |
| 3 | 搜索/领域筛选/排序 | `currentList()` 实现三者（:237-250） | ✅ 一致 |
| 4 | 卡片展开深度内容 | `detailHTML()` + `.a-detail` 切换（:203-211, :270-275） | ✅ 一致 |
| 5 | 学习进度存 localStorage | `save()` 写入 `learning-engine-done`（:160） | ✅ 一致 |
| 6 | 每条卡片显示 star 数 | `starText(s)` 在 `stars` 缺失时返回 `NaN`（:165） | 🔴 **gap：缺字段会显示 NaN** |
| 7 | 数据来自 README/源码、可验证 | `data.json` 部分技术栈/star 为推断（SCAN 已注明"推断/待核实"） | ⚠️ 部分推断 |
| 8 | data.json 写入前按 name 去重 | 去重靠人工流程，脚本侧无校验/去重 | ⚠️ 无自动保障 |

---

## 3. 风险（按"最便宜的验证/修复"排序）

1. **🔴 [已修] star 缺失显示 NaN**（#6）— 一行健壮性修复：`starText` 对非数字返回 `—`。
2. **⚠️ 脚本无 data.json 校验**（#8）— 缺必填字段时静默渲染。建议加最简校验：检查每条含 `name/url/what`，重复 name 给出警告。
3. **🔴 无测试**（测试覆盖地图）— 至少加一个冒烟测试：跑 `build_html.py` 后断言输出含全部仓库数、无残留占位符 `__DATA__`。
4. **⚠️ 数据准确性**（#7）— 推断字段在深扒（README 提炼 detail）时逐步以源码替换；已在 SCAN 注明。
5. **⚠️ 缺架构文档** — 本报告 + README 已部分覆盖，可补一张数据流图。

---

## 4. 绿灯合并门（建议）

- [x] 修复 NaN（#1）
- [ ] `build_html.py` 增加 data.json 必填字段校验（#2）
- [ ] 增加冒烟测试：生成后校验仓库数 + 无残留占位符（#3）
- [ ] 深扒时用源码替换推断字段（#4，持续）

---

*本报告由 github-trending-digest 借用 pm-skills · pm-ai-shipping 的方法生成，演示"用调研到的优质仓库的方法论反哺自己的项目"。*
