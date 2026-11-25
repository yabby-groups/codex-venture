---
category: "open-source"
summaryEn: "LiteLLM 1.109.4 addresses an OAuth error with shared service keys. Deployments that rely on the gateway to automatically register OAuth clients for new MCP bridges now need to opt in."
summaryZh: "LiteLLM 1.109.4 修复共享服务密钥场景下的 OAuth 错误。依赖网关为新建 MCP 桥接自动注册 OAuth 客户端的部署，升级后需要显式启用该行为。"
tags: ["litellm", "mcp", "oauth"]
titleEn: "LiteLLM 1.109.4 makes gateway-owned MCP client registration opt-in"
titleZh: "LiteLLM 1.109.4 将 MCP 网关代注册改为显式启用"
published: "2026-11-25T20:02:48+08:00"
sources: [{"title": "v1.109.4", "url": "https://github.com/BerriAI/litellm/releases/tag/v1.109.4"}]
---
<p lang="zh-CN">LiteLLM 于 2026 年 11 月 24 日发布 v1.109.4。这次回移修复针对共享服务密钥遇到的 <code>403 oauth_principal_mismatch</code> 错误。新版默认关闭由网关代为注册 OAuth 客户端的行为。</p>

<p lang="en">LiteLLM released v1.109.4 on November 24, 2026. The backport addresses <code>403 oauth_principal_mismatch</code> errors with shared service keys by turning off gateway-owned OAuth client registration by default.</p>

<p lang="zh-CN">如果新建的 MCP 桥接没有预先配置 OAuth 客户端，并且依赖网关通过动态客户端注册（DCR）自动完成注册，升级后需设置 <code>LITELLM_MCP_DCR_GATEWAY_CLIENT=true</code> 才能保留这一行为。<a href="https://github.com/BerriAI/litellm/releases/tag/v1.109.4">LiteLLM 发布说明</a></p>

<p lang="en">If new MCP bridges have no preconfigured OAuth client and rely on the gateway to register one through dynamic client registration (DCR), set <code>LITELLM_MCP_DCR_GATEWAY_CLIENT=true</code> after upgrading to preserve that behavior. <a href="https://github.com/BerriAI/litellm/releases/tag/v1.109.4">LiteLLM release notes</a></p>
