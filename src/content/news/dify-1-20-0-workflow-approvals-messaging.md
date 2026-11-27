---
category: "agents"
summaryEn: "Dify 1.20.0 lets Human Input nodes send approval requests by email or through team chat apps, with shared channels and contacts that multiple workflows can reuse."
summaryZh: "Dify 1.20.0 让 Human Input 节点通过邮件或团队聊天工具发送审批请求，并支持多个工作流复用渠道和联系人。"
tags: ["dify", "human-in-the-loop", "workflow-approvals"]
titleEn: "Dify 1.20.0 sends workflow approval requests to team chat and email"
titleZh: "Dify 1.20.0 将工作流审批请求送到团队聊天工具和邮箱"
editorial: {"score": 67, "tier": "standard", "audience": "core"}
published: "2026-11-28T06:32:25+08:00"
sources: [{"title": "v1.20.0", "url": "https://github.com/langgenius/dify/releases/tag/1.20.0"}]
---
<p lang="zh-CN">Dify 在 2026 年 11 月 18 日发布的 1.20.0 中扩展了 Human Input 节点的人工审批功能。一个需要在继续执行前由业务同事审核的流程，可以在该节点等待决定，并通过邮件或团队聊天工具发送审批请求。</p>

<p lang="en">Dify expanded human approvals in its Human Input node with version 1.20.0, released November 18, 2026. A workflow that needs someone on the business team to review it before it continues can wait for a decision at the node and send the approval request by email or through the team’s chat platform.</p>

<p lang="zh-CN">发布说明列出的新功能包括共享渠道、集中管理的联系人、通知模板和经过验证的审批表单。管理员可以集中配置收件人，再由多个 Human Input 节点复用。流程负责人则可以把审批放在具体的业务决策点，例如在对外发送报价之前增加审核。</p>

<p lang="en">The release notes list shared channels, centrally managed contacts, notification templates, and verified approval forms. Administrators can configure recipients centrally for reuse across Human Input nodes. Workflow owners can place each approval at the relevant decision point, such as before sending a quote to a customer.</p>

<p lang="zh-CN">审批请求可通过邮件、Slack、飞书或 Lark、Microsoft Teams、钉钉及企业微信发送。1.20.0 默认启用 NEXT_PUBLIC_ENABLE_HITL_IM，团队仍需配置要使用的通知渠道。</p>

<p lang="en">Approval requests can go out by email or through Slack, Feishu or Lark, Microsoft Teams, DingTalk, or WeCom. Version 1.20.0 enables NEXT_PUBLIC_ENABLE_HITL_IM by default. Teams still need to configure the channels they want to use.</p>
