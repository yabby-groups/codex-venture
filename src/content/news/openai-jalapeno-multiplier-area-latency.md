---
category: "models"
summaryEn: "OpenAI reports that a Jalapeño multiplier redesign cut synthesized cell area by about 15% and halved cycle latency. An adder redesign saved a similar amount of area while keeping its two-cycle latency."
summaryZh: "OpenAI 披露，Jalapeño 的一项乘法器改版将综合单元面积缩小约 15%，延迟从两周期降至一周期。另一项加法器改版节省了相近的面积，延迟仍为两周期。"
tags: ["openai", "jalape-o", "chip-design", "eda"]
titleEn: "OpenAI reports a smaller, one-cycle multiplier design for Jalapeño"
titleZh: "OpenAI 披露 Jalapeño 乘法器改版，综合面积缩小且延迟降至一周期"
editorial: {"score": 63, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T12:04:16+08:00"
sources: [{"title": "Advancing chip design with OpenAI models", "url": "https://openai.com/index/advancing-chip-design-with-our-models"}]
---
<p lang="zh-CN">OpenAI 在 11 月 18 日披露了 Jalapeño 推理芯片的两项算术电路设计结果。一项矩阵单元的乘法器改版将延迟从两个时钟周期降到一个，综合单元面积约减少 15%。另一项加法器改版的单元面积也约减少 15%，延迟保持两个周期。<a href="https://openai.com/index/advancing-chip-design-with-our-models">OpenAI 工程披露</a></p>

<p lang="en">On November 18, OpenAI disclosed two arithmetic circuit redesigns for its Jalapeño inference chip. A matrix-unit multiplier redesign cut latency from two clock cycles to one and reduced synthesized cell area by about 15%. A separate adder redesign cut cell area by about 15% while retaining its two-cycle latency. <a href="https://openai.com/index/advancing-chip-design-with-our-models">OpenAI’s engineering report</a></p>

<p lang="zh-CN">OpenAI 还称，模型在向量单元中探索了替代逻辑与不同的流水线划分，以寻找共享硬件和减少中间存储的机会。评估类似改版时，可以分别记录综合单元面积和周期延迟。这里的数字是厂商披露的电路级设计结果，整芯片性能和功耗仍需对应的测量数据。</p>

<p lang="en">OpenAI also says its models explored alternative logic and pipeline splits in the vector unit to find opportunities to share hardware and reduce intermediate storage. For similar redesigns, track synthesized cell area and cycle latency as separate metrics. The figures here are circuit-level design results reported by OpenAI. Whole-chip performance and power require their own measurements.</p>
