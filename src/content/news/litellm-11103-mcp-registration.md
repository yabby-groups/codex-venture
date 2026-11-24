---
titleZh: "LiteLLM 1.110.3 将 MCP 网关动态注册改为显式启用"
titleEn: "LiteLLM 1.110.3 makes MCP gateway dynamic registration opt-in"
summaryZh: "更新把 MCP 网关动态客户端注册的显式启用行为移植到 1.110 分支，并修复审计日志和路由回退。"
summaryEn: "The release backports opt-in dynamic client registration to the 1.110 MCP gateway branch and fixes audit logging and routing fallback."
published: "2026-11-24T15:01:03+08:00"
category: "open-source"
tags: ["litellm", "mcp", "api-gateway"]
sources:
  - title: "litellm v1.110.3 release notes"
    url: https://github.com/BerriAI/litellm/releases/tag/v1.110.3
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 24 日（北京时间），litellm 发布 v1.110.3。更新把 MCP 网关动态客户端注册的显式启用行为移植到 1.110 分支，并修复审计日志和路由回退。</p>

<p lang="en">litellm published v1.110.3 on November 24 (China Standard Time). The release backports opt-in dynamic client registration to the 1.110 MCP gateway branch and fixes audit logging and routing fallback.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">依赖客户端自动注册的部署，应在测试环境复查授权流程。路由回退改为依据请求实际被路由到的组，拥有多组模型的服务可复查自己的故障转移路径。</p>

<p lang="en">Deployments that rely on automatic client registration should recheck the authorization flow in staging. Routing fallback now uses the group a request was actually routed to, giving multi-group deployments a concrete failover case to verify.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">发布页提供 1.110.3 镜像签名验证信息。此更新对应 1.110 分支，应按当前部署分支核对迁移记录。</p>

<p lang="en">The release page provides signature verification details for the 1.110.3 image. These changes apply to the 1.110 branch, so check migration notes for your deployed branch.</p>
