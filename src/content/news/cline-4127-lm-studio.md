---
titleZh: "Cline 扩展支持需要认证的 LM Studio"
titleEn: "Cline extension supports authenticated LM Studio"
summaryZh: "Cline 4.1.27 增加 LM Studio API 密钥字段，并显示 MCP 工具自行声明的只读属性。"
summaryEn: "Cline 4.1.27 adds an LM Studio API key field and displays read-only declarations for MCP tools."
published: "2026-11-24T15:01:03+08:00"
category: "coding"
tags: ["cline", "lm-studio", "mcp"]
sources:
  - title: "cline v4.1.27 release notes"
    url: https://github.com/cline/cline/releases/tag/v4.1.27
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 21 日（北京时间），cline 发布 v4.1.27。Cline 4.1.27 增加 LM Studio API 密钥字段，并显示 MCP 工具自行声明的只读属性。</p>

<p lang="en">cline published v4.1.27 on November 21 (China Standard Time). Cline 4.1.27 adds an LM Studio API key field and displays read-only declarations for MCP tools.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">开启 Require Authentication 的本地服务可以在扩展中配置密钥。新增的 MCP 标记有助于浏览工具。标记来自服务器声明，实际写权限仍取决于服务器和运行环境。</p>

<p lang="en">Local servers with Require Authentication enabled can be configured with a key in the extension. The new MCP badge helps users scan tools. It comes from the server declaration, while actual write access depends on server and runtime permissions.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">版本页对应编辑器扩展。升级后可在 LM Studio 提供商设置中录入密钥，并用一个已知可用的模型检查连接。</p>

<p lang="en">The release page covers the editor extension. After upgrading, enter the key in the LM Studio provider settings and check connectivity with a known working model.</p>
