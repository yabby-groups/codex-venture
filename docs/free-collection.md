# 免费采集运营

固定注册表包含 80 条来源。GitHub Releases 使用 GitHub REST API，新闻和博客使用发布者提供的 RSS 与 Atom。新增 Release 来源至少返回过一条正式发布记录，启用的五个新增 Feed 已通过正式采集器读取。新增来源接受条件包括访问条款、robots.txt、编辑价值和实际返回。文章使用事实摘要和链接，项目和文档的版权及再利用条件由原作者或许可证决定。

## 访问和测试记录

| 来源 | 本地访问结果 | 生产设置 |
| --- | --- | --- |
| GitHub REST Releases | vLLM 样本 3 条正式 Release。其余新增入口使用相同 API 分别探测 | 启用。Actions 使用仓库自带 token。受 GitHub REST 主额度、搜索及次级限流约束 |
| Simon Willison、Hamel Husain、Apple ML、Microsoft Foundry、Meta Engineering | 正式采集器分别解析 30、20、10、10、9 条 | 每 12 小时最多刷新一次 |
| HN Algolia | 关键词样本解析 4 条 | 免认证。讨论、原始链接及有限评论分别进入证据链 |
| Open VSX、MCP Registry | 各解析 4 条 | 公共入口，免认证。扩展及服务的许可证和配置以发布者资料为准 |
| Hugging Face Hub | 公开 Spaces API 直接访问返回 200，本地正式直连未完成 | 生产按来源记录实际健康，Models、Datasets、Spaces 并行覆盖由调度分轮执行 |
| DEV Community | 正式传输读取 AI 标签 4 条。另一环境探针收到 403 | 免认证公开文章接口，按标签查询与独立退避 |
| Bluesky | 搜索探测 403，作者 Feed 本地直连失败 | 搜索适配器停用，等待公开访问验证 |
| Lobsters、V2EX | Lobsters 被 robots.txt 阻止，V2EX 正式直连失败 | 停用 |
| X、Reddit、Mastodon、Product Hunt | 本轮未确认合适的公开自动访问入口 | 停用 |

平台文档见 [GitHub REST 额度](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)、[HN Algolia API](https://hn.algolia.com/api)、[Hugging Face Hub API](https://huggingface.co/docs/hub/api)、[Open VSX API](https://github.com/eclipse-openvsx/openvsx/wiki/Using-the-Open-VSX-API)、[MCP Registry](https://registry.modelcontextprotocol.io/docs)、[DEV API](https://developers.forem.com/api/v1) 和 [Bluesky AppView](https://docs.bsky.app/docs/advanced-guides/rate-limits)。

## 运行和证据

当前每小时执行固定来源采集，每六小时主动发现一次。耗时较长的来源基于最近成功时间轮转，扩展 Release 入口至少间隔六小时。现有编辑频率、模型费用和每日 token 预算沿用原机制。候选按内容类型轮转，预算同时约束候选数及序列化证据大小。新闻、Release、项目和研究具有不同窗口，长期资源可持续等待。

来源退避及条件请求标头存入 health.json，UTC 小时和日请求计数及限流恢复时间存入 requests.json。Trending 使用分榜名次和已观察的 Star 快照。候选、补充证据及发现元数据存入 items.json。以上状态沿用 venture-state。私有运营统计记录真实采集计数、证据补充结果及零采集服务费用。无新增付费凭据或服务。

二次资料只请求公开 HTTPS，校验并固定解析 IP，验证 TLS 及重定向目标，应用 robots.txt、流量上限及请求退避。资料进入模型前截取并标识来源。SKILL.md 作为文档读取，技能身份基于 GitHub 仓库 ID 和文件路径。网页、README、评论和清单均为外部证据。

分页和游标持久化、Bluesky 作者及讨论串、跨域同事件语义合并、独立长期复查和逐来源发布归因尚待完善。各来源的当前 HTTP 状态和最近成功时间以运行记录为准。

## 2026-11-25 端到端验收

- 主动发现成功。GitHub Trending、GitHub Search、Hugging Face 三类 API、HN Algolia、DEV 五个标签、Open VSX 和 MCP Registry 均实际返回数据。状态分支新增 213 条候选，16 条带榜单名次，9 条记录新增二次证据。其中包括 Skills、插件、MCP、教程和使用故事。[发现运行](https://github.com/yabby-groups/codex-venture/actions/runs/45524448036)
- 固定来源采集任务成功。该次运行记录 12 个来源成功或无变化，Hugging Face Papers Feed、PyTorch Blog Feed 和 MLX Release 请求失败并进入退避。其余入口受刷新间隔及已有健康状态调度。[固定采集运行](https://github.com/yabby-groups/codex-venture/actions/runs/45525049988)
- 使用现有 Codex CLI 和 Responses API 完成一轮编辑，自动发布一篇双语资讯。Chromium 检查和 Cloudflare 验收通过。公网文章返回 HTTP 200，线上 release.txt 与本地构建一致。[编辑发布运行](https://github.com/yabby-groups/codex-venture/actions/runs/45524659016) · [公开文章](https://codex-venture.com/news/github-notification-subscription-rules/)
- Python 编译、公开 HTTPS 地址限制、429 后暂停、六种内容类型轮转和安装证据截取检查通过。发布后本地构建通过 169 个 HTML 页面及站内链接、元数据、RSS、Sitemap 和 Pagefind 校验。

### 资源积压与取证

资源同步在待处理量达到两轮编辑容量时暂停常规资源发现，继续补证和编辑。专题发现可以单独运行。资讯采集、主动发现和文章编辑有独立的运行任务。

GitHub、MCP Registry、Open VSX、JetBrains Marketplace 和 Hugging Face 的发布者描述可以支持基础目录简介。只有平台索引占位语句的 Hugging Face 候选继续读取模型卡。JetBrains 接口为公开搜索，采集限于已验证发布者，并使用默认免费请求预算。GitHub 仓库级资料缓存 6 小时，过期时优先用 ETag 或 Last-Modified 重新验证。技能扫描以文件 SHA 判断变化。

资源运行日志记录送审候选、补证成功、文档缺失、模型实际用量与无效编辑条数。按两次独立日期检查到 404 或 410 标记不可用，仅适用于目录入口本身。队列快照记录最早待处理日期和等待七天以上的条数。
