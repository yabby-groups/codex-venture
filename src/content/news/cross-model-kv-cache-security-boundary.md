---
category: "agents"
summaryEn: "A preprint reports that the same model handled prompt injection differently on text and cache inputs, giving platform teams a reason to assess tool permissions separately for each path."
summaryZh: "预印本比较了同一模型在文本与缓存两条路径上的提示注入表现，为推理平台按路径评估工具调用权限提供了依据。"
tags: ["kv-cache", "agent-security", "inference"]
titleEn: "Cross-model KV cache handoffs need their own safety evaluation"
titleZh: "跨模型交接 KV 缓存，需要单独做防护评估"
editorial: {"score": 79, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T22:24:29+08:00"
sources: [{"title": "Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems", "url": "https://arxiv.org/abs/2611.34278"}]
---
<p lang="zh-CN">同一个目标模型直接处理文本时，在作者所测基准上遵从了 0.4% 的提示注入。改为接收另一模型经映射的 KV 缓存后，比例最高升到 44.2%。Manit Baser 等人在 11 月 25 日提交的《Latent-in-the-Middle》预印本中报告了这一差异。</p>

<p lang="en">In the authors’ benchmark, a target model followed 0.4% of prompt injections when it processed text directly. When it received a mapped KV cache from another model, that rate reached as high as 44.2%. Manit Baser and colleagues reported the gap in the Latent-in-the-Middle preprint submitted on November 25.</p>

<p lang="zh-CN">跨模型交接可以节省重复的预填充计算，但接收端读到的上下文由另一模型编码。对正在评估这种架构的团队，缓存交接应作为独立输入路径做防护评估，并用这条路径的测试结果决定是否向接收端开放工具调用权限。论文中的比例来自作者测试的模型与基准。</p>

<p lang="en">A cross-model handoff can save repeated prefill computation, but the receiver reads context encoded by another model. Teams evaluating this architecture should assess the cache handoff as a separate input path and use the results to decide whether the receiving agent gets tool permissions. The reported rates apply to the models and benchmark the authors tested.</p>
