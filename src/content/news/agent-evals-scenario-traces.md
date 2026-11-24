---
titleZh: "技术专题：Agent 评估怎样记录工具轨迹"
titleEn: "How to capture tool traces in agent evaluations"
summaryZh: "Hugging Face 11 月 23 日发布的评估指南涵盖任务、环境、评分与轨迹，为团队搭建可复查的 Agent 评估提供了参照。"
summaryEn: "Hugging Face’s November 23 guide covers tasks, environments, scoring and traces, giving teams a reference for reviewable agent evaluations."
published: "2026-11-24T14:59:51+08:00"
category: "agents"
tags: ["evaluations", "agent-traces", "benchmarks"]
sources:
  - title: "Hugging Face: Building and maintaining an agentic evaluation"
    url: https://huggingface.co/blog/agentic-evals
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">Hugging Face 11 月 23 日发布的评估指南涵盖任务、环境、评分与轨迹，为团队搭建可复查的 Agent 评估提供了参照。</p>

<p lang="en">Hugging Face’s November 23 guide covers tasks, environments, scoring and traces, giving teams a reference for reviewable agent evaluations.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">以处理工单为例，先定义能从测试环境验证的状态变化，再记录工具调用、关键参数和结果。最终答复可以单独打分。这样能看出失败来自任务理解、接口调用还是评分逻辑。</p>

<p lang="en">For a support-ticket task, define a state change that can be checked in the test environment, then capture tool calls, key arguments and results. Score the final reply separately to distinguish failures in task understanding, tool use and scoring logic.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">指南链接 Hub 上的轨迹、基准和环境入口。对比模型或工具配置时应固定任务版本和允许的操作，并检查记录是否涉及用户数据或凭据。</p>

<p lang="en">The guide links to traces, benchmarks and environments on the Hub. When comparing models or tool setups, pin task versions and permitted actions, and check traces for user data or credentials.</p>
