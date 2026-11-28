---
category: "models"
summaryEn: "SealedLoop uses an evaluator outside the automated improvement loop to decide which policy revisions to keep. In the reported driving comparisons, its test accepted 11 of 12 gains and none of 59 regressions."
summaryZh: "SealedLoop 用自动改进循环之外的评估结果判断是否保留新策略。在论文报告的驾驶策略对照中，检验接受了 12 项提升中的 11 项，59 项退步均未通过。"
tags: ["embodied-ai", "evaluation", "robotics", "driving"]
titleEn: "SealedLoop uses independent tests to decide when to keep a new policy"
titleZh: "SealedLoop 用独立评估决定是否保留新策略"
editorial: {"score": 78, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T21:46:05+08:00"
sources: [{"title": "Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies", "url": "https://arxiv.org/abs/2611.33794"}]
---
<p lang="zh-CN">一项驾驶策略可能在自动改进循环使用的画面上得分更高，却在陌生城市表现退步。Zilin Huang、Zhengyang Wan、Kangan Qian、Zihao Sheng 和 Sikai Chen 在 2026 年 11 月 25 日提交的预印本中提出 SealedLoop，让自动改进过程无法访问的独立评估器为版本保留决策提供证据。<a href="https://arxiv.org/abs/2611.33794">arXiv 预印本</a></p>

<p lang="en">A driving policy can score higher on the frames used by an automated improvement loop and perform worse in an unfamiliar city. In a preprint submitted on November 25, 2026, Zilin Huang, Zhengyang Wan, Kangan Qian, Zihao Sheng, and Sikai Chen propose SealedLoop, which uses evidence from an independent evaluator that the improvement process cannot access to decide whether to keep a new policy. <a href="https://arxiv.org/abs/2611.33794">arXiv preprint</a></p>

<p lang="zh-CN">作者将两种问题分开衡量：循环内的评估器可能判错，循环内真实的提升也可能无法迁移。机械臂操作实验中，成功分类器在一轮里将 196 次失败中的 65 次判为成功。驾驶实验中，即使循环内评估完全准确，也会保留 15 个在陌生城市退步的候选策略中的 8 个。</p>

<p lang="en">The authors measured two problems separately. The in-loop evaluator can misjudge outcomes, and genuine gains within the loop may fail to carry over. In one generation of the manipulation experiment, a success classifier marked 65 of 196 failures as successes. In the driving experiment, even an accurate in-loop evaluator would have kept eight of the 15 candidate policies that performed worse in an unfamiliar city.</p>

<p lang="zh-CN">在已知独立评估结果的驾驶策略配对中，顺序检验接受了 12 项提升中的 11 项，59 项退步均未通过。对负责决定是否替换机器人或驾驶策略的团队，这项实验给出了一个可参考的上线门槛：用独立场景的结果确认新版本是否仍有提升。这些数字对应论文中的驾驶策略配对。</p>

<p lang="en">For driving-policy pairs with known outcomes on the independent evaluation, the sequential test accepted 11 of 12 gains and none of 59 regressions. Teams deciding whether to replace a robotics or driving policy can use the study to inform a release criterion: check whether the new version improves performance in independent scenarios. The counts apply to the driving-policy pairs in the paper.</p>
