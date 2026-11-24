# GEO 审计和运营

## 2026-11-24 生产基线

检出提交 84f132491613cecda88712a3a79962648f3655c6 与 origin/main 对应。HTTPS GET 样本中首页、发布工作流文章、robots.txt、Sitemap 分片和 RSS 返回 200，随机缺失路径返回 404。Cloudflare 提供响应，首页和文章样本无 X-Robots-Tag 和挑战标头。公网 robots.txt 只有通配允许和 Sitemap 声明，样本响应没有托管增补。该证据仅覆盖采样边缘与时间。

P0 保留公开抓取、现有安全控制和双语静态正文。文章已有 main、article、标题、可见来源与核实记录。编辑政策公布独立身份、AI 参与、核实和纠错渠道。P1 补足文章 Sitemap lastmod，连接作者、发布组织和具备已有内容的实体。实体页按编辑证据维护，新增关系随构建校验。代表性修订补足 Ollama 对比的原生 API 地址、接口验证和流式边界，证据类型仍是文档分析。P2 提供公开实体 JSON、轻量资源索引和查询样本。

## 官方依据

- Google 的 AI 优化指南强调可抓取、经验证的原创技术价值和现有 SEO 基础。AI 功能主要沿用 Search 的索引与摘要资格。使用 Googlebot 和 Search 摘要控制管理 Google Search，Google-Extended 对应其自身公布的其他用途。 [AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [AI Features](https://developers.google.com/search/docs/appearance/ai-features)
- OpenAI 将 OAI-SearchBot、GPTBot 和 ChatGPT-User 分别用于搜索、训练和用户触发访问。用户触发请求的 robots.txt 行为以官方说明为准。 [OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- PerplexityBot 用于搜索发现，Perplexity-User 用于用户触发访问。本次文档访问也遇到安全检查，后台配置前应重新核对公开 IP 清单。 [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- Bing Webmaster Guidelines 覆盖抓取、索引及质量。AI Performance 公告列出引用次数、被引页面和 Grounding Queries。账号报表和受支持的引用 API 能力目前 UNKNOWN。 [Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- Cloudflare 可以按爬虫审查流量和策略，托管 robots.txt 可以改变边缘上实际提供的内容。 [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) · [Managed robots.txt](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/)
- Schema.org 类型表达页面本身的事实。搜索富结果资格和平台是否引用由各平台决定。IndexNow 用于有变化的公开 URL，提交前须核实 key 和托管范围。 [Schema.org TechArticle](https://schema.org/TechArticle) · [IndexNow](https://www.indexnow.org/documentation)
- llms.txt 是可选的社区资源索引。主题页提升读者发现和理解的效果可以观测，引用增量属于待验证假设。 [llms.txt](https://llmstxt.org/)

## Cloudflare 人工配置清单

1. 在 AI Crawl Control 核对爬虫类别、验证状态、路径、计数、状态码和拦截。在 WAF 和 Security Events 核对 Challenge、429 和 403。
2. 检查 Bot Fight Mode、AI Crawl Control、Managed robots.txt 和 Content Signals 的实际设置。用 Cloudflare 验证信号或厂商公开 IP 范围识别合法请求。策略例外应限于经验证的目标爬虫和公开路径。
3. 搜索和训练采用独立决策。当前通配规则延续现有公开响应，运营方可确认现有默认、明确禁止指定训练用途，或明确允许指定用途。GPTBot、Google-Extended 和其他用途须逐一对照官方说明。后台配置与站点 robots.txt 共同复核。
4. 查看普通访问和已验证爬虫请求的响应完整性。脚本模拟 UA 的 200 只表明该样本可达。后台状态及真实爬虫记录目前 UNKNOWN。

## 数据与抽样

GitHub 仓库已有 Cloudflare、Google 和 Bing 的分析配置项，账号权限和最近数据覆盖以运行结果与私有快照为准。周报沿用私有仓库和当前 Codex 调用额度，增加 Cloudflare RUM 引荐主机分类、报告覆盖天数及引用数据状态。统计限每天返回的前 100 个主机，计数单位是来源页面浏览，无法分类的主机归入 unknown。已验证爬虫、Google AI 专属报表和 Bing AI 引用在获得账号证据前保留 UNKNOWN。

手工查询使用 config/geo-queries.json，同一问题可选不同语言和平台。每次在私有记录里保存查询、时间、平台和模型、是否实际启用搜索、本站引用 URL、品牌提及、其他来源。无合规搜索样本时状态为 UNKNOWN。普通 Responses API 文本不计作搜索样本。

每日 GitHub Actions 执行构建和公网检查。监控结果用于编辑排查。周报沿用已有采样门槛，分析主题缺口、原始证据和教程时效。新增专题通过实体索引和真实文章关系进入发布构建。Markdown 副本暂缓，公开 HTML 已提供可访问正文。IndexNow 待完成 key 托管及部署增量验证后启用。

## 验收命令

- `npm run check`
- `npm run build`，检查静态 HTML、Sitemap、RSS、语义、实体关系和 Pagefind。
- `python3 -m unittest discover -s tests`
- `node scripts/check-articles-browser.mjs`，覆盖已有文章桌面和移动视口。
- `python3 scripts/geo.py`，检查公开响应及模拟用户代理，并检查不存在路径返回 404。
- 部署时比对公网 release.txt 和本地 dist/release.txt，抽样比对新增实体 JSON 和文章 HTML。


## 生产验收记录

内容部署提交 1c63348a76e7accd17b5f9dcf5c2ff6a6daeed04 的 Cloudflare Workers Build 成功。公网 release.txt 与本地一致，公网实体 JSON 逐字节一致。GitHub GEO 检查运行 45421153133 成功。模拟 Googlebot、Bingbot、OAI-SearchBot、PerplexityBot 请求均为 200，随机缺失页为 404。Chromium 通过七条文章路由的桌面和移动测试。Ego 浏览器另检查技术主题和修订文章的页面截图及桌面宽度。

Cloudflare AI Crawl Control 后台可访问。最近七天 Metrics 界面显示 Googlebot、OAI-SearchBot 和 PerplexityBot 标签，提供请求状态码和热门路径视图。数据自动采集、验证身份口径和完整日志仍为 UNKNOWN。Signals 页面提供 Bot Preference Sync 和 robots.txt 可用性视图，生产抽样以实际 robots.txt 为准。

Bing AI Performance 如可导出，将官方数据映射到私有存储的 `analytics/geo/bing/<开始日>_<结束日>.csv`，日期使用 ISO 格式，与报告窗口一致。文件表头为 `kind,value,citations`，kind 可为 url、query、date。URL 使用本站 canonical，date 使用 ISO 日期。每个维度独立汇总，保留原始导出于私有存储。周报读取规范化 CSV，查询原文留在私有报告。账号真实导入和报告覆盖仍待验证。
