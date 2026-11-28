---
category: "models"
summaryEn: "On a hard DeepMath-103K subset, branching from failed solutions reduced the estimated cost per accepted trace by 30%. The cost per recovered problem barely changed."
summaryZh: "在 DeepMath-103K 的难题子集上，从错解中分叉让每条合格轨迹的估算成本下降 30%，每道找回题目的成本则基本持平。"
tags: ["post-training", "math-reasoning", "training-data"]
titleEn: "DART solved 37% more hard math problems with the same number of traces"
titleZh: "从错解中分叉，DART 用同样多的轨迹多解出 37% 的难题"
editorial: {"score": 75, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T22:24:29+08:00"
sources: [{"title": "Diverse Alternative Reasoning Traces for Hard Math Problems", "url": "https://arxiv.org/abs/2611.34928"}]
---
<p lang="zh-CN">在 DeepMath-103K 中贪心解码未解出的那部分题上，DART 在生成相同条数轨迹的情况下，比独立采样多解出 37% 的题。Lukas Aichberger 等人于 11 月 25 日提交的预印本报告了这项结果。DART 从一条未通过验证的解题轨迹出发，挑出不确定性较高的步骤，借助参考答案生成不同的后续解法。</p>

<p lang="en">On the subset of DeepMath-103K that greedy decoding failed to solve, DART recovered 37% more problems than independent sampling at the same number of generated traces. Lukas Aichberger and colleagues report the result in a preprint submitted on November 25. DART starts from a rejected solution trace, selects uncertain steps, and uses the reference answer to guide distinct continuations.</p>

<p lang="zh-CN">作者估算，每条通过验证的轨迹成本低 30%，而每道找回题目的成本与独立采样接近。对已有参考答案和验证器的后训练团队，这两个分母对应不同目标。要扩大题目覆盖，就看新增解出的题数和每道题的成本。要补充合格轨迹，就看每条通过验证的轨迹花了多少。</p>

<p lang="en">The authors estimate that each accepted trace costs 30% less, while the cost per recovered problem is close to that of independent sampling. For post-training teams with reference answers and a verifier, those denominators capture different goals. To broaden coverage, count the additional problems solved and the cost per recovered problem. To build up a pool of usable traces, track the cost per accepted trace.</p>
