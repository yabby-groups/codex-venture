---
category: "models"
summaryEn: "Ministral-3B achieved 79.2% localization accuracy on the RTL consistency questions and flagged all 41 compliant controls as violations. The benchmark gives hardware teams a concrete example of why to score those abilities separately."
summaryZh: "Ministral-3B 在 RTL 一致性题上的定位准确率为 79.2%，同时把 41 个合规对照全部判为违规。团队验收审查助手时可以把定位和违规判定分开评分。"
tags: ["hardware-verification", "rtl", "benchmarks"]
titleEn: "SpecRead finds Ministral-3B flagged every compliant RTL control"
titleZh: "SpecRead 评测中，Ministral-3B 将 41 个合规 RTL 对照全部判为违规"
editorial: {"score": 79, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T17:45:22+08:00"
sources: [{"title": "SpecRead: A Benchmark for Measuring Whether Language Models Understand Hardware Specifications", "url": "https://arxiv.org/abs/2609.33699"}]
---
<p lang="zh-CN">硬件审查助手给出一个可疑位置后，团队还需要知道它能否判断 RTL 是否真的违反规范。11 月 26 日公布的 arXiv v2 摘要介绍了 SpecRead v2.2。基准以 10 个开源 OpenTitan IP 块为材料，包含 383 道题，覆盖条文检索、跨章节推理、矛盾检测和规范与 RTL 一致性检查，并设置了 41 个合规 RTL 对照。</p>

<p lang="en">When a hardware review assistant points to a suspect location, teams still need to know whether it can judge if the RTL actually violates the specification. The arXiv v2 abstract announced on November 26 describes SpecRead v2.2. The benchmark draws on 10 open-source OpenTitan IP blocks and contains 383 questions covering retrieval, cross-section reasoning, contradiction detection, and consistency between specifications and RTL. It also includes 41 compliant RTL controls.</p>

<p lang="zh-CN">作者报告，在规范与 RTL 一致性题上，Ministral-3B 的定位准确率为 79.2%，但 41 个合规对照全部被它判为违规。这是该模型在论文评测设置下的表现。内部验收可以加入已知合规的样例，并分别记录违规判定、位置定位和合规样例误报率。<a href="https://arxiv.org/abs/2609.33699">论文摘要</a></p>

<p lang="en">On the specification-to-RTL consistency questions, the authors report 79.2% localization accuracy for Ministral-3B, which also flagged all 41 compliant controls as violations. The result applies to the model and evaluation setup described in the paper. An internal evaluation can include known-compliant examples and score violation verdicts, localization, and false positives on compliant cases separately. <a href="https://arxiv.org/abs/2609.33699">Paper abstract</a></p>
