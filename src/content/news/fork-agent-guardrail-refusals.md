---
category: "agents"
summaryEn: "The FORK preprint tests whether agent guardrails can give authorized users enough information to recover from a refusal while limiting what attackers learn. On one benchmark, the authors report 93.1% utility on benign tasks and a drop in attack success from 70.6% to 9.1%."
summaryZh: "FORK 预印本研究如何让拒绝消息帮助获授权用户继续任务，同时限制攻击者从中获得的信息。作者报告，在一项基准上，正常任务效用为 93.1%，攻击成功率从 70.6% 降至 9.1%。"
tags: ["agent-safety", "guardrails", "research"]
titleEn: "FORK tests how much agent guardrails should reveal when they block an action"
titleZh: "FORK 研究智能体拦截操作时该透露多少信息"
published: "2026-11-27T03:03:38+08:00"
sources: [{"title": "FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal", "url": "https://arxiv.org/abs/2611.33879"}]
---
<p lang="zh-CN">当 AI 智能体的一项操作被拦截时，拒绝理由太笼统，获授权的用户可能不知道如何继续。解释太具体，又可能向观察者泄露防护规则。Hieu Man、Chao Shang、Rui Dong、Devang Kulshreshtha、Yanjun Qi 和 Sandesh Swamy 于 11 月 25 日提交的 FORK 预印本，将拦截决定与对外解释放在一起评估。</p>

<p lang="en">When a guardrail blocks an AI agent’s action, a vague refusal can leave an authorized user unsure how to proceed. A detailed explanation can reveal how the guardrail works to anyone watching. In a preprint submitted November 25, Hieu Man, Chao Shang, Rui Dong, Devang Kulshreshtha, Yanjun Qi, and Sandesh Swamy evaluate the blocking decision and the public explanation together.</p>

<p lang="zh-CN">作者报告，在 FORK-World 基准上，三个智能体的平均攻击成功率从 78.4% 降至 14.1%，效用保持在 85% 以上。在训练时未见过其环境和任务的 MT-AgentRisk 基准上，攻击成功率从 70.6% 降至 9.1%，正常任务效用为 93.1%。这些是作者报告的基准结果，适用范围限于论文评估的条件。</p>

<p lang="en">On FORK-World, the authors report that average attack success across three agents fell from 78.4% to 14.1%, with utility above 85%. On MT-AgentRisk, whose environments and tasks were unseen during training, attack success fell from 70.6% to 9.1%, with 93.1% utility on benign tasks. These are author-reported benchmark results under the conditions evaluated in the paper.</p>
