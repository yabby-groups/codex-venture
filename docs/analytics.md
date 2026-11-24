# 网站统计与私有运营分析

## 人工配置

| 平台 | 操作 |
| --- | --- |
| Cloudflare | 在账号的 **Observability → Analytics → Web Analytics** 添加 `codex-venture.com`，选择 Automatic。生产站 Astro 默认不写入 Beacon。只有确认边缘无法注入时，先在后台关闭自动注入，再在 Workers Builds 设置 `VENTURE_WEB_ANALYTICS_MODE=manual` 和官方片段的 `CLOUDFLARE_WEB_ANALYTICS_SITE_TAG`。部署后检查 HTML、浏览器脚本请求及 Beacon 上报。 |
| Cloudflare API | 创建限定到目标账号的 **Account → Account Analytics → Read** Token，独立于部署权限。设置下表变量和 Secret。通过 smoke test 核查 Dataset、字段与回溯范围。 |
| Google Search Console | 添加 Domain Property `codex-venture.com`，把 Google 提供的 TXT 记录加到域名根并完成验证。也可用已验证的 URL-prefix Property。通过界面提交 `https://codex-venture.com/sitemap-index.xml`。 |
| Google 授权 | 在 Google Cloud 启用 Search Console API，创建专用服务账号和 GitHub OIDC Workload Identity Provider。将条件限定为 `yabby-groups/codex-venture` 的 `refs/heads/main`，仅给匹配的主体授予该服务账号的 Workload Identity User。把服务账号加入 Search Console 属性，先使用受限权限核查搜索与 URL Inspection。同步请求使用 `webmasters.readonly`。 |
| Bing Webmaster Tools | 添加站点并按控制台指引通过 DNS、验证文件或导入已验证的 Search Console 站点完成验证。在 Sitemaps 中提交站点地图。在 Settings → API access 查找 Webmaster API Key。Bing 的 API Key 权限由账号提供，建议使用仅管理本站的身份。 |
| 私有存储 | 创建并初始化独立 **Private** 仓库。当前可使用 `yabby-groups/codex-venture-analytics`。为目标私库配置独立的可写 deploy key，将私钥存入生产工作流 Secret。也支持只限该仓库的 fine-grained PAT，权限为 Metadata Read 和 Contents Read/Write。两者都配置时优先使用 deploy key。 |
| 首次运行 | 打开 Actions → **Venture Analytics** → Run workflow → `analytics-smoke-test`。检查各服务状态后设 `VENTURE_ANALYTICS_ENABLED=true`。按保留期运行 `analytics-backfill`，之后可手动运行每日、每周、每月报告。 |

| GitHub Actions 配置 | 类型 | 填写 |
| --- | --- | --- |
| `VENTURE_ANALYTICS_PRIVATE_REPO` | Variable | 私有仓库 `owner/name` |
| `VENTURE_ANALYTICS_DEPLOY_KEY` | Secret | 目标私库可写 deploy key 对应的完整私钥 |
| `VENTURE_ANALYTICS_TOKEN` | Secret | 使用 PAT 时填入仓库范围凭据 |
| `VENTURE_ANALYTICS_ENABLED` | Variable | `true` 启用定时同步及报告 |
| `CLOUDFLARE_ACCOUNT_ID` | Variable | Cloudflare 账号 ID |
| `CLOUDFLARE_WEB_ANALYTICS_SITE_TAG` | Variable | 官方 RUM 站点标识 |
| `CLOUDFLARE_ANALYTICS_TOKEN` | Secret | 单独的 Analytics Read Token |
| `GOOGLE_SEARCH_CONSOLE_PROPERTY` | Variable | `sc-domain:codex-venture.com` 或完整 URL-prefix（含尾斜杠） |
| `GOOGLE_WORKLOAD_IDENTITY_PROVIDER` | Variable | `projects/NUMBER/locations/global/workloadIdentityPools/POOL/providers/PROVIDER` |
| `GOOGLE_SERVICE_ACCOUNT` | Variable | 服务账号邮箱 |
| `BING_SITE_URL` | Variable | Bing 后台确认的站点 URL |
| `BING_WEBMASTER_API_KEY` | Secret | 专用账号的 Webmaster Key |
| `VENTURE_MODEL_PRICING_JSON` | Secret | 实际合同价格 JSON 数组 |
| `VENTURE_DAILY_COST_LIMIT` | Secret | 可选，每日估算费用上限，十进制金额 |
| `VENTURE_COST_CURRENCY` | Variable | 费用上限的币种，例如 `USD` |
| `VENTURE_STRATEGY_AUTO_UPDATE` | Variable | `true` 启用有边界的策略更新和应用 |

供人工阅读的官方文档见 [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)、[Search Console Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)、[Google GitHub Actions Auth](https://github.com/google-github-actions/auth) 和 [Bing Webmaster](https://www.bing.com/webmasters/).

## 调度与数据口径

| 北京时间 | 工作 |
| --- | --- |
| 03:35 | Cloudflare RUM 回补 |
| 06:35 | 搜索数据回补 |
| 23:35 | 当日报告 |
| 周一 07:15 | 上周报告和条件式 Codex 分析 |
| 每月一日 07:45 | 上月报告 |
| 每次采编运行 | 按阶段记录采集、模型、发布和公网验收 |

Cloudflare 快照按 UTC 原生日保存。它的浏览量和访问次数来自浏览器端 RUM，使用官方访问口径。唯一访客、缺少权限的指标和超出保留期的快照标记为 `unavailable`。浏览器统计与 Workers HTTP 请求量各有口径。

Google 数据按太平洋时间保存，读取 final 数据并保守等待三天。每个维度最多取 1,000 条，可能受 API 内部截断、匿名查询和属性级聚合限制。查询行数上限由本实现主动收紧，API 单次请求允许至 25,000 行。抽查为执行时的索引快照。Sitemap 仅用于发现 URL。Bing 的滚动快照保留原始平台日期及爬取指标。

文章主键使用内容集合与 slug，对路径去除尾斜杠差异、查询字符串和片段。已知旧链接在 `config/article-aliases.json` 中显式映射。来源覆盖率以有原始来源的文章占比计算，重复率使用独立资讯的规范化来源 URL。同一来源在简报与独立新闻复用是正常用法。

私有仓库按原生日期保存 `analytics/{traffic,search,content,operations,reports,strategy}`。报告重复运行按相同键重算。公开 Job Summary 仅显示阶段状态、时间，以及适合公开的发布数量。切换后应按需要检查旧工作流日志、Artifacts 和公开 `venture-state` 历史中的既有记录。既有历史需要单独授权处理。

## 用量与策略

公开模型价格配置默认为空。使用实际网关费率填写 Secret。每项价格样例如下，样例金额仅用于说明格式。

```json
[
  {
    "provider": "venture",
    "model": "provider-model-name",
    "effective": "2026-11-24",
    "currency": "USD",
    "input_per_million": "1.00",
    "cached_input_per_million": "0.10",
    "output_per_million": "4.00",
    "cache_in_input": true,
    "reasoning_in_output": true
  }
]
```

`estimated_cost` 按真实会话 Token 与有效价格计算。未知价格或缺失必要用量时记录 null。账单字段保留为空，待确认服务商账单接口。调用数表示 Codex 会话数。JSONL 中未报告的 HTTP 请求次数和 Reasoning Token 保持未知。每日费用上限依据会话预留与已观测费用。需要供应商侧硬停止时，应在网关设置限额。

Codex 每周从私有汇总读取证据。低覆盖期跳过模型分析。启用策略更新后，程序只接受分类权重、每轮候选数和每轮发布上限三个字段。所有分类保有资格，并保留探索候选。每次变更记录前后值、证据、目标与验证方式。回滚时关闭 `VENTURE_STRATEGY_AUTO_UPDATE` 并按历史记录恢复 `strategy/current.json`。预算、授权与来源真实性要求由人工管理。
