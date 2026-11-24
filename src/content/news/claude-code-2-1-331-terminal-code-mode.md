---
titleZh: Claude Code 将终端 Code Mode 扩展到四个托管平台
titleEn: Claude Code brings terminal Code Mode to four managed platforms
summaryZh: 2.1.331 版支持在 Amazon Bedrock、Google Cloud Agent Platform、Microsoft Foundry 和 AWS 上的 Claude Platform 终端会话中使用 Code Mode。
summaryEn: Version 2.1.331 adds terminal Code Mode support on Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry and Claude Platform on AWS.
published: "2026-11-24T13:45:00+08:00"
category: coding
tags: [claude-code, code-mode]
sources:
  - title: Claude Code v2.1.331 release notes
    url: https://github.com/anthropics/claude-code/releases/tag/v2.1.331
---
<h2><span lang="zh-CN">此次更新覆盖哪些会话</span><span lang="en">Which sessions are covered</span></h2>

<p lang="zh-CN">Anthropic 在 Claude Code 2.1.331 的发布说明中列出了四个支持 Code Mode 的托管环境，明确适用范围为终端会话。更新还在 claude doctor 中加入 API 连通性检查，可显示 HTTP 状态、错误或跳过检查的原因。</p>

<p lang="en">Anthropic’s release notes identify four managed environments where Claude Code 2.1.331 supports Code Mode in terminal sessions. The update also adds an API connectivity check to claude doctor that reports the HTTP status, an error, or why the check was skipped.</p>

<h2><span lang="zh-CN">对开发团队的影响</span><span lang="en">What this means for development teams</span></h2>

<p lang="zh-CN">已在上述平台使用 Claude Code 的团队，可以在现有终端环境中评估 Code Mode。API 连通性结果也为排查会话启动问题提供了一个具体线索。</p>

<p lang="en">Teams already using Claude Code on these platforms can evaluate Code Mode in their existing terminal environment. The API connectivity result also gives them a concrete starting point when troubleshooting session startup.</p>
