---
category: "coding"
summaryEn: "Pair disk utilization with recent growth and give the on-call responder a first action and an escalation condition."
summaryZh: "把磁盘使用率与近期增长放在一起，并为值班人写明首项操作和升级条件。"
tags: ["sre", "monitoring", "alerting"]
titleEn: "Design disk alerts around the on-call response"
titleZh: "按值班响应流程设计磁盘告警"
type: "workflows"
version: "Platform-independent disk alert design"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:31+08:00"
sources: [{"title": "From Monitoring Alerts to IT Actions: A Practical Guide to Closing the Loop", "url": "https://dev.to/lynxtrac_team_b01b03e00a4/from-monitoring-alerts-to-it-actions-a-practical-guide-to-closing-the-loop-3n04"}]
---
<p lang="zh-CN">设计磁盘告警时，先确定值班人收到通知后需要作什么决定。LynxTrac Team 在原文中举了三个同为 85% 的情形：容量数月稳定、过去一周从 70% 升到 85%，以及过去一小时快速增长。判断紧迫程度时，把当前使用率与近期变化放在同一条告警里。<a href="https://dev.to/lynxtrac_team_b01b03e00a4/from-monitoring-alerts-to-it-actions-a-practical-guide-to-closing-the-loop-3n04">原文</a></p>

<p lang="en">When designing a disk alert, start with the decision the on-call responder needs to make. The LynxTrac Team gives three examples at 85% utilization: a volume stable for months, a rise from 70% over the past week, and rapid growth over the past hour. Put current utilization and recent change in the same alert so the responder can judge the urgency. <a href="https://dev.to/lynxtrac_team_b01b03e00a4/from-monitoring-alerts-to-it-actions-a-practical-guide-to-closing-the-loop-3n04">Original guide</a></p>

<p lang="zh-CN">把受影响的卷、观测窗口、预期服务影响、响应负责人、第一项安全操作和升级条件写进告警说明。用上述三种历史形态走查规则，检查值班人能否据此判断何时继续观察、何时排查增长来源，以及何时升级。缺少明确负责人与响应动作的指标，可以先保留采集，等响应规则补齐再启用值班通知。本文依据原作者的操作建议整理，85% 是示例中的观测值。</p>

<p lang="en">Document the affected volume, observation window, expected service impact, response owner, first safe action, and escalation condition. Walk through the three usage patterns and check whether the responder can tell when to keep watching, when to investigate the growth, and when to escalate. Where ownership and response steps are still open, keep collecting the metric and enable paging once those details are in place. This documentation-based workflow follows the authors’ guidance, with 85% serving as the example reading.</p>
