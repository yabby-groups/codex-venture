---
titleZh: "n8n 2.48.8 扩展工作流迁移报告"
titleEn: "n8n 2.48.8 expands its workflow migration report"
summaryZh: "迁移报告增加工作流上次运行状态说明，自定义实例角色也可获得报告访问权限。"
summaryEn: "The migration report explains the last workflow run state and can be made available to custom instance roles."
published: "2026-11-24T15:01:03+08:00"
category: "agents"
tags: ["n8n", "automation", "mcp"]
sources:
  - title: "n8n n8n@2.48.8 release notes"
    url: https://github.com/n8n-io/n8n/releases/tag/n8n%402.48.8
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 23 日（北京时间），n8n 发布 n8n@2.48.8。迁移报告增加工作流上次运行状态说明，自定义实例角色也可获得报告访问权限。</p>

<p lang="en">n8n published n8n@2.48.8 on November 23 (China Standard Time). The migration report explains the last workflow run state and can be made available to custom instance roles.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">有大量历史流程的团队可以先按运行状态确定迁移验证顺序。新版还报告 MCP 工作流触发器激活失败，便于区分配置启用与运行成功。</p>

<p lang="en">Teams with many older workflows can use run states to prioritize migration checks. The release also reports MCP workflow trigger activation failures, making configuration activation and successful execution easier to distinguish.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">从版本页获取 2.48.8。迁移前应核对角色访问范围，并使用代表性工作流检查触发器及依赖凭据。</p>

<p lang="en">Get 2.48.8 from the release page. Check role access and exercise representative workflows and their trigger credentials before migrating.</p>
