---
category: "agents"
summaryEn: "Three models completed only six of 150 episodes in the Gridworld preview. Its independently adjustable maze mechanics offer a design for regression tests that help locate where an agent gets stuck."
summaryZh: "三个模型在 Gridworld 预览评测的 150 个回合中只通关 6 次。可独立调整的迷宫机关为视觉 Agent 的配对回归测试提供了设计参考。"
tags: ["vision-language-models", "agent-evaluation", "gridworld"]
titleEn: "MultiNet Gridworld uses adjustable maze mechanics to probe visual agent failures"
titleZh: "MultiNet Gridworld 用可拆换的迷宫机关定位视觉 Agent 失败"
editorial: {"score": 80, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:16:12+08:00"
sources: [{"title": "Attributing Agentic Failure in Reasoning Vision-Language Models with Interactive 2D Environments", "url": "https://arxiv.org/abs/2611.33162"}]
---
<p lang="zh-CN">三个视觉语言模型在 150 个迷宫回合中只通关 6 次，含开关门机制的回合全部失败。这组数字来自 11 月 26 日公布的 MultiNet v2.0-Gridworld 早期预览。作者把钥匙与门、开关与闸门、干扰物以及需要按顺序操作的组合做成可独立调整的机制，以便对照失败出现在哪类任务里。<a href="https://arxiv.org/abs/2611.33162">预印本</a></p>

<p lang="en">Three vision-language models completed just six of 150 maze episodes and failed every episode with a switch-controlled gate. The results come from the MultiNet v2.0-Gridworld early preview announced on November 26. The authors made keys and doors, switches and gates, distractors, and ordered combinations independently adjustable so they could compare which tasks caused failures. <a href="https://arxiv.org/abs/2611.33162">Preprint</a></p>

<p lang="zh-CN">评测用最短动作数标定迷宫难度，并为未完成的回合评分。做界面自动化回归时，可以沿用它的配对测试思路，每组只改一个交互条件，再查看动作记录，定位失败出现在识别控件、安排操作顺序，还是出错后的恢复阶段。</p>

<p lang="en">The benchmark uses the shortest possible action sequence to set maze difficulty and score unfinished episodes. For UI automation regression tests, teams can adapt the paired-test design by changing one interaction condition at a time, then inspecting the action trace to see whether the failure occurred during control recognition, action sequencing, or recovery from a mistake.</p>
