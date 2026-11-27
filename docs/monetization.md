# 流量与商业化运营

## 审计与部署

生产域名使用 Astro 预渲染、Cloudflare Workers Static Assets 和 GitHub main 自动部署。VPS Compose 负责采编队列，现有 Analytics Actions 负责使用原凭据同步 Cloudflare RUM、Search Console、Bing 与私有分析仓库。本站沿用这些生产入口。运营提供的 5,790 PV、4,530 Visits、24 小时 2,050 Visits 和美日英合计约 81% 缺少同期指标来源与请求分层，暂作为待核实的基线。

本轮加入浏览器端统计、广告和推广配置、联系与条款页面、合规披露、边缘诊断和私有商业日报。Cloudflare Beacon 使用生产域名的公开站点标识，检测已有自动注入以避免重复。可用 Workers Builds 的 `VENTURE_WEB_ANALYTICS_MODE=automatic|manual|disabled` 切换，覆盖标识用 `CLOUDFLARE_WEB_ANALYTICS_SITE_TAG`。标为自动化的浏览器测试隔离跨站请求。

## 审核与授权

1. GA4 创建属性和 Web 数据流。将 Measurement ID 配置到 Workers Builds 的 `VENTURE_GA4_ID`，将数字属性 ID 配置到统计环境的 `GOOGLE_GA4_PROPERTY_ID`。开启 Google Analytics Data API，为报表用户授予只读访问，授权 `analytics.readonly` OAuth。使用 `GOOGLE_GA4_CLIENT_ID`、`GOOGLE_GA4_CLIENT_SECRET`、`GOOGLE_GA4_REFRESH_TOKEN` 保存凭据。GA4 只有访问者明确选择同意后才加载。
2. AdSense 注册或绑定已有账号，添加站点并提交审核。按 AdSense 提供的方式验证所有权。所有权验证使用 `ads.txt`。构建从统一配置的 `ads.publisher` 读取公开发布商 ID，Workers Builds 的 `VENTURE_ADSENSE_PUBLISHER` 可覆盖该值。等站点审核通过后完成身份、地址、税务和收款认证。报表另需 AdSense Management API 和 `adsense.readonly` OAuth。用 `GOOGLE_ADSENSE_ACCOUNT=accounts/pub-…` 和 `GOOGLE_ADSENSE_CLIENT_ID`、`GOOGLE_ADSENSE_CLIENT_SECRET`、`GOOGLE_ADSENSE_REFRESH_TOKEN` 配置。
3. 在 Google 认证 CMP 中配置法定地区的广告同意及撤回，包括 EEA、英国、瑞士和适用的美国州。在 Workers Builds 设置认证 CMP 提供的 HTTPS 脚本 `VENTURE_CERTIFIED_CMP_SCRIPT`。该脚本需独立引导并暴露 TCF v2 API，且提供适用美国州的隐私信号与撤回界面。使用供应商预览功能验证拒绝、接受、撤回及区域配置。本站对可选统计和广告采用全球主动选择。GPC、DNT 和自动化测试拒绝加载 Google SDK。生产验证避免点按正式广告。
4. 领取已获审核的广告单元 ID，填入 [统一配置](../config/monetization.json)。确认站点和 CMP 验收后，开启 `ads.enabled`，并在生产构建设置 `VENTURE_ADSENSE_APPROVED=true` 和 `VENTURE_ADSENSE_SERVE=true`。AdSense 控制台关闭自动广告，只使用站点配置的广告位。广告位置限当前有效的实测长文文末。停投可关任一开关并重新部署。
5. 联盟平台由运营人员选择、注册并确认协议、结算、授权链接和披露。配置项包含唯一 `id`、`category`（`ai-tools`、`saas`、`vps`、`developer-tools`）、`articles`（规范文章路径数组）、`name`、HTTPS `url` 和 `terms`、ISO 日期 `starts` 和 `expires`、`disclosureZh` 和 `disclosureEn`。起日含、截止日不含，按 UTC。活动有变更时重新部署。广告位和联盟推广配置初始均为空。
6. Cloudflare 边缘请求需要 `CLOUDFLARE_ZONE_ID` 和只读 Zone Analytics 权限的 `CLOUDFLARE_ZONE_ANALYTICS_TOKEN`。先验证账号套餐允许查询的字段。若缺少明细数据权限，爬虫类别及相关异常保持 UNKNOWN。Search Console 沿用已验证的域名属性和现有 OIDC。需要 VPS 独立同步 Search Console 时，为 VPS 配置只读 OAuth（`GOOGLE_SEARCH_CLIENT_ID`、`GOOGLE_SEARCH_CLIENT_SECRET`、`GOOGLE_SEARCH_REFRESH_TOKEN`）和 `GOOGLE_SEARCH_CONSOLE_PROPERTY`。

## 私有日报与诊断

Actions 复用私有分析仓库。VPS 每日北京时间 12 点将 `analytics-daily` 加入现有队列，可用 `docker compose exec -T scheduler venture run analytics-daily` 即时触发。VPS 的提供者凭据从受保护的 Compose `.env` 读入。日报位于私有卷 `/venture-private/analytics/reports/daily/YYYY-MM-DD.json`。GitHub 的分析任务继续通过现有授权收集数据。VPS 独立报告按其已配置的数据源覆盖。

报告提供最近已结束日期、Cloudflare 浏览器端 Visits 与 PV、来源域名、热门文章、最近可用的最终 Search Console 数据、GA4 来源与 key events、AdSense 预估收益和网络报告的佣金及转化。RUM 是能执行并上报 Beacon 的浏览器活动，自动化和跟踪阻止会影响覆盖。边缘请求含资源、机器人和错误。按各自日期及平台口径阅读，金额和浏览器访问分别保存。缺测为 `UNKNOWN`，经验证的零单独保留。边缘报告查看 4xx 路径、端口分布和小时峰值，至少三个历史峰值后报告三倍基线信号。

如有官方请求导出，在私有卷 `analytics/imports/requests/YYYY-MM-DD.ndjson` 原子写入 UTC 日的规范化记录，字段为 `timestamp`、`user_agent`、`status`、`port`、`verified_bot`。Verified Bot 只由可信平台证据填写，浏览器 UA 归为未验证。原始文件只存私有目录并按运营需要缩短保留。联盟网络报表可通过 API 或导出文件加工到 `analytics/imports/affiliate/YYYY-MM-DD.json`，每行为包含 `program`、`conversions`、`currency` 和十进制 `commission` 的对象。各联盟平台的采集授权与导入由运营配置。

下一轮内容策略从已观测文章和搜索表现生成选题参考，优先原创实践、部署教程、工具实测和产品对比。现有发布校验检查内容形态、唯一标题及 canonical、站内链接、RSS、Sitemap 和 Pagefind。审核前抽查不同栏目首页、文章、归档与搜索，核对来源链接、可独立阅读性、广告密度和编辑附加价值，低价值或重叠条目应合并、补证据或延后。禁止伪造体验、优惠及佣金，禁止自动点击、诱导点击或流量注入。

官方要求见 [AdSense 资格](https://support.google.com/adsense/answer/9724)、[认证 CMP](https://support.google.com/adsense/answer/13554116)、[Google 发布商政策](https://support.google.com/publisherpolicies/answer/10502938) 和 [Cloudflare GraphQL](https://developers.cloudflare.com/analytics/graphql-api/)。
