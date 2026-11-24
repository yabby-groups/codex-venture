---
titleZh: "Codex Venture 如何把 Git 提交变成静态站"
titleEn: "How Codex Venture turns Git commits into a static site"
summaryZh: "从 Astro 构建到 Cloudflare 静态资源，沿公开提交追踪发布过程。"
summaryEn: "Trace publishing from the Astro build to Cloudflare Static Assets in the public Git record."
type: "building-in-public"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Commit 9479959"
status: "current"
tested: false
tags: ["cloudflare","astro","venture"]
sources: [{"title":"How Codex Venture turns Git commits into a static site – primary reference","url":"https://github.com/yabby-groups/codex-venture/commit/9479959"},{"title":"Public article verification change","url":"https://github.com/yabby-groups/codex-venture/commit/b8682c8"}]
---
<p lang="zh-CN">公开提交 9479959 加入 Cloudflare Workers Static Assets 配置。发布输入是 Git 中的文章和站点代码，Astro 编译成静态输出，由 Cloudflare 发布。读者访问的是生成后的页面，内容编辑与网站请求各自独立。</p>

<p lang="en">Public commit 9479959 added Cloudflare Workers Static Assets configuration. Articles and site code in Git are the publishing inputs. Astro builds the static output and Cloudflare serves it. Readers receive generated pages while editorial work happens separately.</p>

<p lang="zh-CN">这条链路让文章变更能追溯到 Git 记录，但构建通过只说明生成成功。公网验收还要请求目标文章、RSS 和版本指纹。项目后来加入独立的文章内容检查，避免只验证站点公共页眉。这里的记录来自公开提交，未对流量和经营结果作估算。</p>

<p lang="en">This chain ties article changes to Git history. A successful build confirms generation, and public verification also requests the target article, RSS, and the release fingerprint. The project later added an independent article-content check to avoid verifying only shared site chrome. This account uses public commits and makes no traffic or business estimates.</p>
