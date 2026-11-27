# Codex Venture

面向全球 AI 工具、模型、产品与技术的中英双语资讯站。Markdown 经 Astro 生成静态 HTML，Pagefind 在浏览器中搜索，生产站由 Cloudflare Workers Static Assets 提供访问。首期内容收录 2026 年 11 月 24 日简报与两条有官方发布说明的独立资讯。

## 本地开发与验收

需要 Node.js 24、npm、Python 3.9+ 和 Git。

```sh
npm ci
npm run dev
ASTRO_TELEMETRY_DISABLED=1 npm run check
ASTRO_TELEMETRY_DISABLED=1 npm run build
npm run preview
```

在构建后的预览中验证全文搜索。每次构建检查双语格式、独立文章重复来源、元数据、站内链接、RSS、Sitemap 和 Pagefind 文件。

## 生产发布

生产域名 `codex-venture.com` 绑定 Cloudflare Workers 项目 `codex-venture`。GitHub 仓库 `yabby-groups/codex-venture` 的 `main` 分支推送触发自动发布。构建命令为 `npm run build`，部署命令为 `npx wrangler deploy`。`wrangler.jsonc` 将仓库根目录下的 `dist/` 声明为静态资源目录。

1. 本地运行 `npm run build`，检查构建和站内校验。
2. 提交变更并推送到 `origin/main`。在 Cloudflare Workers 控制台核对本次构建对应的提交及部署结果。
3. 检查公网首页、`/daily/`、`/search/`、`/rss.xml` 和 `/sitemap-index.xml` 的状态码与实际内容。首页应包含 Codex Venture 标题，RSS 和站点地图应返回各自的 XML。占位 Worker 也可能返回 HTTP 200 和 `Hello world`。
4. 发布回退通过 Cloudflare Workers 的 Deployments 页面选择上一条已验证的部署。

### 2026-11-24 部署记录

- 初始静态产物部署到 `jl01:/data/codex-venture/public`。Nginx 源站校验通过，当时公网域名返回 Cloudflare 521。
- 迁移期间曾建立直接上传的 Pages 项目 `codex-venture.pages.dev`。生产域名随后绑定到已连接 GitHub 的 Workers 项目。
- 首次 GitHub 构建通过。部署阶段 Wrangler 自动为 Astro 加装 Cloudflare 适配器并再次构建，首页改为输出到 `dist/client/index.html`，原校验报 `ValueError: missing index.html`。同时公网域名仍由占位 Worker 响应。
- 提交 `9479959` 增加显式静态资源配置。Wrangler 本地试运行通过，推送到 `main` 后，公网首页、每日简报、搜索页、RSS 和站点地图均返回实际站点内容。

## 自主运营

生产所有权切换前由 GitHub Hosted Runner 定时运行。VPS 四服务 Compose 的部署、Secrets、状态迁移、回退和验收见 [VPS 自主运营](docs/vps-operator.md)。原 Hosted 入口保留用于切换前运营及回退，配置见 [GitHub Actions 运营说明](.github/OPERATIONS.md)。

本地静态预览使用 `npm run build && npm run preview`。

## 网站统计

公开内容产出见 `/stats/`，访问统计及本地偏好说明见 `/privacy/`。网站统计、搜索接入、模型计价、私有数据保存和策略回滚见 [人工配置清单](docs/analytics.md)。

## 免费资讯采集

固定来源见 [来源注册表](config/sources.yaml)。主动发现、二次证据、平台访问条件和实测记录见 [免费采集运营说明](docs/free-collection.md)。采集服务费用为零，编辑使用现有模型预算。

广告、联盟推广、流量诊断与人工审核步骤见 [流量与商业化运营](docs/monetization.md)。
