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

## Nginx 部署与运营环境

1. 确认已有 Linux 服务器的公网 IP、SSH 用户及授权，以及现有反向代理和 TLS 配置。安装 Node.js 24、Python 3.9+、Git、Docker Compose v2、GNU coreutils 和支持 `CRON_TZ` 的 Cron。
2. 在服务器部署仓库，运行 `npm ci`。复制 `.env.example` 为 `.env`，设定专用运行用户、绝对部署路径及 Codex CLI 路径。在该用户下完成现有 Codex 账号登录并检查 `codex login status`。运行用户需要写入仓库的内容、Git 元数据和部署目录。
3. 运行 `docker compose up -d --build`。Compose 默认将 Nginx 暴露在 `127.0.0.1:8080`。把现有 HTTPS 反向代理指向该地址，保留源主机名并让 `/release.txt` 保持不缓存。Docker 镜像也可独立提供其内置静态站点。
4. 首次执行 `./ops/run deploy`。DNS 切换前可临时将 `VENTURE_SITE_URL` 配置为本机 Nginx 地址。域名完成指向服务器、HTTPS 可访问之后，用生产 URL 再执行一次，以核对公网确实返回指定版本。DNS 使用服务器对应的 A 或 AAAA 记录，保留其他业务记录。
5. 确认生产访问、身份验证和任务用量配置后，以运营用户安装 `ops/codex-venture.cron` 中的条目。按实际路径调整 `VENTURE_REPO`，在现有 crontab 中追加这些条目。

上线前按 OpenAI 品牌规则核实项目名及域名所需授权。站点使用原创标识，关于页标明独立运营。品牌使用核查和 DNS 写入均需要域名管理方确认。 [OpenAI 品牌规范](https://openai.com/brand/)

## 日常运行

- `collect` 每小时运行。RSS、Atom、GitHub Releases 使用条件请求与来源退避。索引记录规范化地址、内容指纹、来源及处理状态。首次读取最近七天，编辑窗口为 48 小时。独立文章与简报可共享原始来源。
- `news` 在北京时间 08:20、12:20、18:20 运行，`daily` 在 22:20 运行。没有候选时不会调用模型。当前简报已经存在时重复执行会退出。编辑器使用一次独立 Codex 会话，以结构化结果返回草稿。来源配置与内容发布规则分别位于 `config/sources.yaml` 和 `ops/editor.md`。 [Codex 非交互执行文档](https://developers.openai.com/codex/noninteractive)
- 每周检查源健康、发布覆盖和线上状态，从 GitHub 发现新的活跃开源来源，并停用持续失败的来源。当前无受众统计集成。
- 每轮只有一个任务持锁。模型命令设置 4 分钟超时，调度外层设置总超时。用量从 CLI JSONL 读取，按北京时间累计，调用前预留额度并限制候选量。单次超额结果会丢弃，额度无法在供应商生成途中截断。
- `touch .venture-runtime/PAUSE` 暂停后续任务，移除文件恢复。日志在 `.venture-runtime/logs`，按大小切分并清理 14 天前的文件。
- 构建通过后，先复制完整静态目录，再原子替换版本指针。HTTP 探测失败或提交失败会恢复前一版本。中断后的下一轮会从发布日志恢复。保留最近五个版本及回滚目标。使用 `./ops/run rollback RELEASE_ID` 回到已保留的版本。正式发布随后会继续以仓库的当前内容为准。
- 运营任务记录本地 Git 提交。当前自动运营脚本使用本地提交与 Nginx 发布流程。自动推送到 GitHub 及 Cloudflare 发布验收尚未接入该脚本。凭据和运行文件保存在 Git 之外。

启用定时运营时，需要提供运行主机、运营用户的 Codex 登录和相应的 GitHub 发布权限。
