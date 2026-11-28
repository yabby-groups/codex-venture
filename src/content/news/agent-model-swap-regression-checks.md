---
category: "agents"
summaryEn: "In a 100-item diagnostic, each model solved cases the other missed. The authors’ acceptance-contract approach gives teams a way to check which tasks still meet their requirements after a model swap."
summaryZh: "一项 100 条样例的诊断发现，两个模型各有对方答错、自己答对的题。论文提出用逐项验收条件检查换模型后哪些任务仍然合格。"
tags: ["agents", "model-migration", "evaluation"]
titleEn: "Swapping an agent’s model? Check which tasks it stopped getting right"
titleZh: "给 Agent 换模型，先查哪些原本能做对的任务退步了"
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:37:18+08:00"
sources: [{"title": "Agent Calibration under Deployment Change: Acceptance Contracts, Trajectory Repair, and Adaptation Costs", "url": "https://arxiv.org/abs/2609.35149"}]
---
<p lang="zh-CN">在一组 100 条意图识别样例里，两个模型都答对了一些对方答错的题。Yaxiao Liu、Pengbo Liu、Yiwen Liu、Yihua Guan、Xingjian Li 和 Jiaxing Song 在 2026 年 11 月 25 日修订的 arXiv 预印本 v4 中报告了这项诊断。对准备给生产 Agent 换模型的团队来说，新模型多答对的题可能拉高总分，同时掩盖原先能处理的个别任务已经退步。</p>

<p lang="en">On a 100-item intent recognition task, each model got some cases right that the other got wrong. Yaxiao Liu, Pengbo Liu, Yiwen Liu, Yihua Guan, Xingjian Li, and Jiaxing Song reported the diagnostic in revision v4 of their arXiv preprint, dated November 25, 2026. For teams swapping the model behind a production agent, new successes can lift the overall score while hiding regressions on individual tasks the agent used to handle.</p>

<p lang="zh-CN">作者提出为部署目标写一份带版本的验收约定，涵盖任务能否端到端完成、结果是否符合技术和业务要求，以及目标用户能否接受。换模型前，可以挑出几条业务上不能退步的任务，先写清最终交付物怎样才算合格，再用同一批输入逐条对照新旧结果。复核时，先看旧模型通过、新模型未通过的那几条。</p>

<p lang="en">The authors propose a versioned acceptance contract for each deployment target. It covers whether the agent can complete tasks end to end, whether its outputs meet technical and professional requirements, and whether intended users accept them. Before a model swap, pick a few tasks where a regression would matter, define what counts as an acceptable final output, and run both models on the same inputs. Start the review with cases the old model passed and the new one failed.</p>
