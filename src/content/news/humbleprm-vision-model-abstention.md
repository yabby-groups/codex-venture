---
category: "models"
summaryEn: "HumblePRM scores what a vision model sees separately from whether it has enough evidence to answer. The authors report more abstention on ambiguous images and roughly steady accuracy on clear ones."
summaryZh: "HumblePRM 分别评价模型看见了什么、证据是否足够作答。作者报告，训练后模型在歧义图像上更常放弃作答，清晰图像的准确率大致持平。"
tags: ["vision-language-models", "evaluation", "abstention"]
titleEn: "HumblePRM trains vision models to abstain when images are ambiguous"
titleZh: "HumblePRM 训练视觉模型在图像证据不足时放弃作答"
editorial: {"score": 80, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:33:12+08:00"
sources: [{"title": "HumblePRM: Improving VLM Abstention in Ambiguous Situations through Process Reward Modeling", "url": "https://arxiv.org/abs/2611.33452"}]
---
<p lang="zh-CN">一张照片里的字迹如果只看得清一半，视觉模型要先描述能辨认的内容，再判断这些线索是否足以回答问题。Saket Reddy、Ke Yang 和 ChengXiang Zhai 于 11 月 24 日提交的 HumblePRM 预印本把这两步分开评分。第一步评价场景描述是否符合图像，第二步评价模型表现出的把握是否与手头证据相称。<a href="https://arxiv.org/abs/2611.33452">HumblePRM 预印本</a></p>

<p lang="en">When only part of the text in a photo is legible, a vision model has two jobs: describe what it can make out and judge whether that evidence is enough to answer. In a preprint submitted November 24, Saket Reddy, Ke Yang, and ChengXiang Zhai introduce HumblePRM to score those steps separately. One score checks whether the description matches the image. The other checks whether the model’s confidence matches the available evidence. <a href="https://arxiv.org/abs/2611.33452">HumblePRM preprint</a></p>

<p lang="zh-CN">作者报告，训练后模型更常在歧义输入上放弃作答，在清晰图像上的准确率大致持平，并在 Gemma 4 E4B 上也观察到改进。做照片、截图或扫描件的产品验收时，可以把画面误读和证据不足时仍作答分别记录。再检查产品能否在后一种情况下请用户重拍或转人工，同时统计清晰样本被误拒的频率。重拍与转人工属于产品侧的验收场景。</p>

<p lang="en">The authors report that training made models abstain more often on ambiguous inputs while accuracy on clear images stayed roughly steady. They also observed an improvement on Gemma 4 E4B. In product evaluations for photos, screenshots, or scans, track image misreads separately from answers given on insufficient evidence. Then test whether the product can request a retake or hand the case to a person in the latter situation, and track how often it turns away clear inputs. Retakes and human review are product-level test cases.</p>
