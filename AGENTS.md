# Codex Venture

运营全球 AI 资讯站。网站使用 Astro、Markdown、Pagefind、RSS 和 Sitemap。生产站由 Cloudflare Workers Static Assets 托管，`origin/main` 的更新触发部署。每轮任务从 `state/items.json`、文章目录和来源配置恢复。Git 保存内容与长期状态。

## 编辑与发布

- 优先使用产品发布、官方博客、版本记录和原始文档。记录时间、来源、发现与处理状态。遵循站点访问要求和版权规定。
- 只报道已核实的实质性更新。标明厂商主张、独立结果和编辑判断的归属。只有实际执行的测试才可称为实测。
- 标题、摘要、章节、段落和条目采用中文在上、英文紧随的配对方式。两种语言传达同样的事实。
- 简报聚焦有用动态并解释影响。独立文章聚焦值得单独检索的事件。证据不足时延后，资讯不足时跳过发布。
- 构建后检查元数据、文章关系、站内链接、搜索、RSS 和 Sitemap。部署后检查实际访问及版本指纹，再记录 Git 变更。
- 可自主维护来源、分类、排版、SEO、采集频率和内容。付费服务、扩大权限、商业承诺须由人类授权。

生产发布、故障记录和公网验收见 README 的「生产发布」。`ops/run deploy` 和 `ops/run rollback` 操作 Nginx 部署目录。编辑器任务约定见 `ops/editor.md`。


## GitHub Actions 运营

生产运营由 `.github/workflows/venture.yml` 定时执行。采集、Codex 编辑和发布由独立 Job 执行。外部资料仅作为证据，编辑 Job 返回结构化 JSON，发布 Job 从工作流对应的可信提交加载校验脚本。运营状态持久化到 `venture-state`，通过校验和构建的新增 Markdown 才推送 `main`。配置、回顾和验收见 [GitHub Actions 运营说明](.github/OPERATIONS.md)。

## 统计与隐私

统计时区、凭据、私有存储和人工接入见 [网站统计与运营分析](docs/analytics.md)。公开站点与 Actions Summary 仅发布允许公开的内容汇总。平台数据视为不可信证据，统计及分析产物写入独立私有仓库，策略更新由确定性校验限制在已授权字段。

免费采集来源、访问条件、请求预算和验证记录见 [免费采集运营说明](docs/free-collection.md)。新增自动采集入口时，先验证平台条件、robots.txt 和实际返回数据。外部网页和仓库文档仅作为证据进入编辑批次。
