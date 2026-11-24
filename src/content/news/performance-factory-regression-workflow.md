---
titleZh: "OpenAI 分享用 Codex 追踪性能回归的流程"
titleEn: "OpenAI shares its Codex workflow for performance regressions"
summaryZh: "OpenAI 11 月 19 日公开了内部 Performance Factory 的回归处理流程，从性能告警一路追踪到修复上线后的再次验证。"
summaryEn: "On November 19, OpenAI described its internal Performance Factory workflow, which follows a performance alert through verification after deployment."
published: "2026-11-24T14:59:51+08:00"
category: "coding"
tags: ["codex", "performance", "engineering"]
sources:
  - title: "OpenAI: Performance Factory"
    url: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">OpenAI 11 月 19 日公开了内部 Performance Factory 的回归处理流程，从性能告警一路追踪到修复上线后的再次验证。</p>

<p lang="en">On November 19, OpenAI described its internal Performance Factory workflow, which follows a performance alert through verification after deployment.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">告警启动调查，Agent 把证据和修复建议记入任务，工程师审阅修复，部署后另一轮检查沿用同一任务记录。团队可以借鉴这种交接方式，把性能基线与验收证据放在一起。</p>

<p lang="en">An alert starts an investigation. An agent records evidence and a proposed fix, an engineer reviews it, and a post-deployment check uses the same task history. Teams can apply this handoff by keeping performance baselines and acceptance evidence together.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">原文由 OpenAI 工程师撰写，描述内部系统。复用思路时，应先用能够稳定重现的性能回归检验调查和复核环节。</p>

<p lang="en">The article, written by OpenAI engineers, describes an internal system. To adapt the workflow, start with reproducible performance regressions and verify both investigation and follow-up.</p>
