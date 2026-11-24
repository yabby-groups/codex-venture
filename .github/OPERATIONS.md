# GitHub Actions 自动运营

在仓库 Settings → Secrets and variables → Actions 配置以下值。所有生产任务在 GitHub Hosted Runner 的 `main` 工作流运行。

| 类型 | 名称 | 用途 |
| --- | --- | --- |
| Secret | `CODEX_API_KEY` | 第三方 Responses API 密钥 |
| Secret | `VENTURE_PUBLISH_TOKEN` | 可选。仅在默认 `GITHUB_TOKEN` 推送后 Cloudflare 未收到部署事件，或分支规则要求独立身份时配置。使用仅限本仓库、Contents read/write 的 fine-grained PAT |
| Secret | `CLOUDFLARE_API_TOKEN` | 当前 Git 集成流程无需配置。若后续启用 Cloudflare API，需按具体操作限定权限 |
| Variable | `CODEX_BASE_URL` | 第三方 HTTPS API 基址，例如 `https://gateway.example/v1`。CLI 拼接 `/responses` |
| Variable | `CODEX_MODEL` | 第三方网关中的默认模型名 |
| Variable | `CODEX_REASONING_EFFORT` | 默认 `low` |
| Variable | `CODEX_CLI_VERSION` | npm 版本，默认 `0.171.0`。升级后重跑 smoke test |
| Variable | `CODEX_ADVANCED_MODEL` | 可选，周报使用。空值沿用默认模型 |
| Variable | `CODEX_ADVANCED_REASONING_EFFORT` | 可选，高级模型默认 `low` |
| Variable | `VENTURE_ENABLED` | 设为 `true` 启用定时和手动采编。清空或设为 `false` 暂停新采编。手动 health 和 smoke-test 仍可运行 |
| Variable | `VENTURE_DAILY_TOKEN_LIMIT` | 北京时间每日 Token 预算，默认 100000。填 `unlimited` 只记录用量，填 0 暂停模型调用 |
| Variable | `VENTURE_MAX_ARTICLES_PER_RUN` | 单批最多文章数，默认 3。每日及每周简报均最多一篇 |
| Variable | `VENTURE_MAX_MODEL_CALLS_PER_DAY` | 北京时间每日 Codex 会话上限，默认 6。填 0 暂停模型调用 |

`CODEX_BASE_URL` 与 `CODEX_MODEL` 也支持同名 Secret。两处都配置时 Variables 优先。

## 首次运行

1. 配置 API Secret、基址、模型和推理等级。打开 Actions → **Codex Venture Responses API smoke test** → Run workflow。也可从 **Codex Venture** 选择 `smoke-test`。工作流用真实 `codex exec` 验证流式事件、固定 MCP 工具往返、最终结构化结果和用量，然后运行站点构建。
2. Smoke test 通过后设置 `VENTURE_ENABLED=true`。在 **Codex Venture** 手动运行 `backfill`，填写回顾天数，默认 7，范围 1–30。回顾限于来源可见记录，有效候选批量编辑一次。文章按实际刊发时间归档。
3. 首次有文章的运行在推送后核对公网内容指纹、静态入口和新增文章 HTML。如果推送成功但 Cloudflare 验收超时，在 Cloudflare Workers Builds 核对该提交是否触发构建。确认 Git 集成没有响应默认令牌事件时，配置上述发布 Secret，并用下一次有有效内容的推送核验。已推送的提交可在 Cloudflare 控制台重试构建，完成后运行 `health`。

## 日常调度

| 北京时间 | 任务 |
| --- | --- |
| 每小时整点 | collect |
| 每日 07:30 | discover |
| 每日 08:20、12:20、18:20 | news |
| 每日 22:20 | daily |
| 周日 21:30 | weekly |

Actions 排程允许延迟。GitHub 同一并发组只有一个运行和一个待运行，新的待运行可能替换前一个待运行。手动任务还包括 `health`，用于查看来源健康并验证当前版本。失败后重新 dispatch 新运行，避免单独重跑 Job 时缺少本次尝试的产物。

`venture-state` 分支保存候选、内容指纹、来源缓存验证器、退避信息和近 31 天模型预算。每次模型调用前持久化额度预留，详细 JSONL 用量写入私有统计仓库。固定工具 smoke test 预留 40000，普通编辑预留 25000。公共预算台账按预留额度保守计数。预算按会话计数，单会话包含供应商完成工具往返所需的多次 HTTP 请求。设定数值预算时，供应商生成期间的 Token 超额由结算记录，超额草稿停止发布。每次任务最多一轮编辑，采集与空批无需调用模型。跨 Job 传递的候选和文章结果保留 3 天。

编辑 Job 仅获得只读仓库权限和第三方 API 密钥。文章模式关闭 shell 和查网，发布 Job 从工作流提交加载脚本，用可信候选与结构化响应重新生成 Markdown。只有新增文章通过验证和构建才推送 `main`。Git 推送坚持快进，人工并发提交时可在新 HEAD 重新运行。Cloudflare 保持现有 Workers Git 部署方式。

## 统计流程

Venture Analytics 使用独立调度同步平台并生成日周月报告。配置、统计口径和私有仓库权限见 [网站统计与运营分析](../docs/analytics.md)。
