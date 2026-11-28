---
category: "agents"
summaryEn: "In a 16-case test, refund reviewers still let through requests that should have been blocked. Use acceptance cases to verify both model decisions and tool-side authorization."
summaryZh: "一组 16 条用例的测试中，两种模型审核都漏放了退款请求。上线验收应同时检查模型判断和退款工具的业务授权。"
tags: ["agents", "authorization", "tool-calls"]
titleEn: "Test refund authorization at the tool before an agent goes live"
titleZh: "退款 Agent 上线前，在工具端验收订单与操作权限"
type: "workflows"
version: "Strands Decider 2B and Nova Pro author test, 2026-11-25"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:03:20+08:00"
sources: [{"title": "Stop AI Agents Acting on Bluffs? A Strands Decider 2B Tool Gate Test", "url": "https://dev.to/aws-builders/stop-ai-agents-acting-on-bluffs-a-strands-decider-2b-tool-gate-test-5004"}]
---
<p lang="zh-CN">Sarvar Nadaf 在 AWS Community Builders 的文章中，用同一组 16 个退款请求比较两种模型审核。在 11 个不应放行的请求中，Strands Decider 2B 拦下 7 个，Nova Pro 拦下 9 个。Strands 漏放的四个请求置信度介于 0.80 和 0.95。把这些数字当作作者的一组测试结果，适合用来设计验收用例。<a href="https://dev.to/aws-builders/stop-ai-agents-acting-on-bluffs-a-strands-decider-2b-tool-gate-test-5004">Nadaf 的测试记录</a></p>

<p lang="en">Writing for AWS Community Builders, Sarvar Nadaf compared two model reviewers on the same 16 refund requests. Of the 11 requests that should have been blocked, Strands Decider 2B blocked seven and Nova Pro blocked nine. Confidence on the four requests Strands let through ranged from 0.80 to 0.95. Treat the figures as results from the author's single test set and use them to design acceptance cases. <a href="https://dev.to/aws-builders/stop-ai-agents-acting-on-bluffs-a-strands-decider-2b-tool-gate-test-5004">Nadaf's test record</a></p>

<p lang="zh-CN">用测试订单做一张验收表，先为每个请求标注预期决定，再分别记下模型决定和工具是否实际执行。覆盖合法退款、信息不全和不满足业务条件的请求，分别记录正确放行、误拦和漏放。执行退款前，由工具根据可信业务记录核对订单归属、可退金额和操作者权限。缺少必要信息时，转人工或要求补充信息；放行判断与最终退款动作都应能回查。</p>

<p lang="en">Build an acceptance sheet with test orders. Label the expected decision for each request, then record the model's decision and whether the tool executed the refund. Include valid refunds, incomplete requests, and requests that fail business rules. Count correct approvals, false blocks, and erroneous approvals separately. Before issuing a refund, have the tool verify order ownership, the refundable amount, and operator permissions against trusted business records. Route missing information to a person or ask for clarification, and make both the approval decision and the eventual refund traceable.</p>
