---
category: "coding"
summaryEn: "Compare float32 KL values with a float64 reference on nearly identical distributions, then check whether rounding changes a training alert or distillation decision."
summaryZh: "用几乎相同的分布比较 float32 KL 值和 float64 对照，检查舍入误差会不会改变训练告警或蒸馏评估的阈值判断。"
tags: ["pytorch", "kl-divergence", "numerical-precision"]
titleEn: "Test whether near-zero KL values in PyTorch can flip an alert"
titleZh: "PyTorch 算出接近零的负 KL，怎么检查它会不会误触发告警？"
blocks: [{"kind": "notice", "text": {"en": "The 25.7% figure comes from one group in frank chu’s CPU rerun. His reference used the same formula evaluated in float64. A decision that needs a certified error bound requires a reference with its own error analysis.", "zh": "25.7% 来自 frank chu 在 CPU 上复跑的一组样本。他用同一公式的 float64 结果作对照。若决策需要经过认证的误差界，应选用带误差分析的参考计算。"}, "title": {"en": "What the reported rate measures", "zh": "如何理解这个比例"}}]
type: "workflows"
version: "PyTorch 2.15.0 CPU, source-reported float32 and float64 comparison"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 74, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T20:18:21+08:00"
sources: [{"title": "35% of my KL divergences came back negative", "url": "https://dev.to/frankchu/35-of-my-kl-divergences-came-back-negative-51hc"}]
---
<p lang="zh-CN">如果训练告警或蒸馏评估用到了接近零的 KL 散度，可以先用几乎相同的分布做数值回归测试。frank chu 报告，他在 CPU 上用 PyTorch 2.15.0 复跑时，一组 float64 参考 KL 约为 10⁻⁸ 的样本中，25.7% 的 float32 结果为负。理论上的 KL 散度非负，但计算中的舍入误差可能盖过接近零的结果。<a href="https://dev.to/frankchu/35-of-my-kl-divergences-came-back-negative-51hc">frank chu 的复跑记录</a></p>

<p lang="en">If a training alert or distillation metric uses KL divergence near zero, start with a numerical regression test on nearly identical distributions. In frank chu’s reported CPU rerun with PyTorch 2.15.0, 25.7% of float32 results were negative in one group whose float64 reference KL was around 10⁻⁸. KL divergence is mathematically nonnegative, but rounding error can overwhelm a result this close to zero. <a href="https://dev.to/frankchu/35-of-my-kl-divergences-came-back-negative-51hc">frank chu’s rerun report</a></p>

<h2><span lang="zh-CN">用自己的告警阈值做对照</span><span lang="en">Test against your own alert threshold</span></h2>

<p lang="zh-CN">固定几对接近的概率分布，覆盖实际阈值两侧。可以从作者采用的伯努利分布或八分类分布入手。计算 KL(p‖q) 时，按作者示例把 log(q) 作为 F.kl_div 的输入，把 p 作为 target，单对分布用 reduction='sum'。从同一组原始概率分别构造 float32 输入和 float64 对照，记录两种计算的差值、负值和跨过业务阈值的样本。</p>

<p lang="en">Fix a few pairs of nearby probability distributions that cover both sides of your operational threshold. The Bernoulli and eight-category distributions in the report are starting points. For KL(p‖q), follow the example by passing log(q) as the input to F.kl_div and p as the target, using reduction='sum' for a single pair. Build the float32 inputs and the float64 reference from the same original probabilities, then record the differences, negative results, and cases that cross your threshold.</p>

<p lang="zh-CN">如果两种精度在同一对输入上触发了不同的告警结果，把该分布对保存为回归样例，并记录 PyTorch 版本、设备、精度和归约方式。评估时优先看误差是否足以改变阈值判断。参考值极接近零时，单看相对误差百分比很难判断实际影响。</p>

<p lang="en">If the two precisions trigger different alert decisions on the same pair, save that pair as a regression case and record the PyTorch version, device, precision, and reduction. Judge the error by whether it can change the threshold decision. When the reference is extremely close to zero, relative error alone gives little indication of the operational impact.</p>
