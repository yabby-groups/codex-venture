---
category: "image"
summaryEn: "A preprint reports that ResNet-50 identified the source of images from four specified models with 100% accuracy on held-out prompts. Texture and unprompted style choices give blind-review organizers concrete cues to check."
summaryZh: "一篇预印本报告，ResNet-50 在保留提示词测试中以 100% 准确率区分了四个指定图像模型。组织盲评时，可检查纹理和提示词未指定的风格是否泄露模型来源。"
tags: ["text-to-image", "model-attribution", "evaluation"]
titleEn: "Texture and style give away the source of images from four models in a preprint study"
titleZh: "四款生图模型的纹理和风格能暴露图像来源"
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:17:47+08:00"
sources: [{"title": "Probing Visual Idiosyncrasies in Text-to-Image Models", "url": "https://arxiv.org/abs/2611.34843"}]
---
<p lang="zh-CN">提示词没交代背景和风格，图像模型补上的细节仍可能暴露来源。11 月 26 日公告的一篇预印本比较了 HiDream-O1-Dev、FLUX.2-dev、HunyuanImage-3.0 和 Qwen-Image-2512。作者发现，低层纹理统计含有可用于识别模型的信号，图像描述也显示各模型倾向于补上不同的背景和风格。<a href="https://arxiv.org/abs/2611.34843">arXiv 预印本</a></p>

<p lang="en">When a prompt leaves the background and style unspecified, the details an image model fills in can still give it away. A preprint announced on November 26 compared HiDream-O1-Dev, FLUX.2-dev, HunyuanImage-3.0, and Qwen-Image-2512. The authors found that low-level texture statistics carried clues to the source model. Image captions also revealed differences in the backgrounds and styles each model tended to add. <a href="https://arxiv.org/abs/2611.34843">arXiv preprint</a></p>

<p lang="zh-CN">作者报告，ResNet-50 对保留提示词生成的图像进行四分类时，准确率为 100%。人类参与者则是在两个候选来源之间选择，准确率为 62.61%。两项数字对应不同的识别任务。组织生图盲评时，可以先跨多条提示词检查反复出现的纹理、背景和风格，并把来源猜测与画质评分分别记录。<a href="https://arxiv.org/abs/2611.34843">实验摘要</a></p>

<p lang="en">The authors report 100% accuracy when ResNet-50 classified images from held-out prompts among the four models. Human participants scored 62.61% on a separate task with two candidate sources per judgment. For a blind image review, organizers can check multiple prompts for recurring textures, backgrounds, and styles, then record source guesses separately from image quality scores. <a href="https://arxiv.org/abs/2611.34843">Study abstract</a></p>
