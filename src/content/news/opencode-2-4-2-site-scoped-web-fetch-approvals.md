---
category: "coding"
summaryEn: "New “Always allow” approvals for web fetch in OpenCode v2.4.2 apply to a single site. If you used the option before upgrading, review those approvals because they can still cover every URL."
summaryZh: "OpenCode v2.4.2 将新设的网页抓取「始终允许」限定在单个站点。升级前保存的授权仍可能覆盖所有 URL，曾使用该选项的开发者应复查历史授权。"
tags: ["opencode", "web-fetch", "permissions"]
titleEn: "OpenCode v2.4.2 limits new web fetch approvals to one site"
titleZh: "OpenCode v2.4.2 将网页抓取的新增长期授权限定在单个站点"
editorial: {"score": 71, "tier": "standard", "audience": "core"}
published: "2026-11-28T00:16:05+08:00"
sources: [{"title": "v2.4.2", "url": "https://github.com/anomalyco/opencode/releases/tag/v2.4.2"}]
---
<p lang="zh-CN">OpenCode 于 2026 年 11 月 26 日发布 v2.4.2。用网页抓取工具查技术文档时，如果你在新版里为某个站点选择「始终允许」，这项授权只覆盖该站点。旧版的同一选项则会放行所有 URL。<a href="https://github.com/anomalyco/opencode/releases/tag/v2.4.2">OpenCode v2.4.2 发布说明</a></p>

<p lang="en">OpenCode released v2.4.2 on November 26, 2026. If you use its web fetch tool to look up documentation and choose “Always allow” for a site in the new version, that approval covers only that site. In earlier versions, the same option allowed fetching from any URL. <a href="https://github.com/anomalyco/opencode/releases/tag/v2.4.2">OpenCode v2.4.2 release notes</a></p>

<p lang="zh-CN">如果你以前只为查某个文档站点点过「始终允许」，升级后应优先复查那条授权。发布说明指出，旧版保存的授权会沿用原有范围，因此当时为一个站点作出的决定，仍可能放行其他站点的网页抓取。</p>

<p lang="en">If you previously clicked “Always allow” just to look up documentation on one site, review that approval first after upgrading. The release notes say saved approvals retain their original scope, so a decision you made with one site in mind may still allow the tool to fetch pages from other sites.</p>
