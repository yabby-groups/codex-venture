---
category: "video"
summaryEn: "AffectWorld holds the scene and event fixed to test whether a change in emotion affects what a character does and what happens next. The authors report low sensitivity scores across all eight world models they tested."
summaryZh: "AffectWorld 固定场景和事件，检验情绪变化会不会传递到角色行动和之后的场景。作者报告，八个受测世界模型在这项测试中的敏感度得分都偏低。"
tags: ["affectworld", "world-models", "video-generation", "benchmarks"]
titleEn: "AffectWorld tests whether changing a character’s emotion changes what happens next"
titleZh: "AffectWorld 测试只改角色情绪，接下来发生的事会不会变"
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T14:04:28+08:00"
sources: [{"title": "AffectWorld: Benchmarking Emotion-Driven Future World Prediction", "url": "https://arxiv.org/abs/2610.18305"}]
---
<p lang="zh-CN">同一场戏、同一个触发事件，只换角色情绪，生成的视频会让角色采取不同的行动吗？Changhao Song、Yacong Chen、Hui Gao、Yazhou Zhang 和 Peng Zhang 在 11 月 25 日修订的 AffectWorld v2 预印本中，用 1,498 个日常视频样本评估情绪、行动和场景状态之间的一致性，其中 223 个反事实样本固定场景和事件，只改变角色情绪。</p>

<p lang="en">Keep the scene and the event that sets it in motion the same, then change the character’s emotion. Will the generated video show the character acting differently? In the AffectWorld v2 preprint, revised on November 25, Changhao Song, Yacong Chen, Hui Gao, Yazhou Zhang, and Peng Zhang use 1,498 everyday video samples to evaluate consistency across emotions, actions, and scene states. A counterfactual subset of 223 samples holds the scene and event fixed while changing the character’s emotion.</p>

<p lang="zh-CN">作者报告，八个受测世界模型在这项基准上的反事实情绪敏感度得分为 0.027 至 0.070，量表为 0 至 1。团队可以把同样的对照搬进分镜评审。用相同的开场和事件生成两版，再依次核对角色动作是否随情绪改变，以及动作有没有在后续画面留下可见的结果。<a href="https://arxiv.org/abs/2610.18305">AffectWorld 预印本</a></p>

<p lang="en">The authors report counterfactual emotion sensitivity scores of 0.027 to 0.070 on a 0-to-1 scale across the eight world models they tested. Storyboard teams can borrow the paired setup. Generate two versions with the same opening and event, then check whether the emotion changes the character’s action and whether that action has a visible consequence in the frames that follow. <a href="https://arxiv.org/abs/2610.18305">AffectWorld preprint</a></p>
