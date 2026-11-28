---
category: "video"
summaryEn: "StateWeaver tracks approved visual references alongside story time and asset state. The design gives video teams a way to record what changes in a shot and what the next one should inherit."
summaryZh: "StateWeaver 将已确认的参考图与故事时间、素材状态关联。视频团队可以借用这一设计，在分镜表里记录本镜发生的变化和下一镜应延续的属性。"
tags: ["video-generation", "storyboards", "continuity"]
titleEn: "StateWeaver tracks visual changes across AI-generated shots"
titleZh: "StateWeaver 让下一镜继承已经确认的角色状态"
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:16:12+08:00"
sources: [{"title": "StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation", "url": "https://arxiv.org/abs/2611.34290"}]
---
<p lang="zh-CN">角色在上一镜换了外套，下一镜生成时却可能沿用旧参考图。11 月 26 日公布的 StateWeaver v1 预印本提出，把审核发现的差异写成具体的素材更新要求，例如更新外套，同时保留已经正确的角色身份和其他属性。<a href="https://arxiv.org/abs/2611.34290">预印本</a></p>

<p lang="en">A character changes jackets in one shot, and the next shot may still be generated from the old reference. The StateWeaver v1 preprint, announced on November 26, proposes turning discrepancies found in review into specific asset updates, such as changing the jacket while preserving the character’s identity and other attributes that are already correct. <a href="https://arxiv.org/abs/2611.34290">Preprint</a></p>

<p lang="zh-CN">StateWeaver 把确认后的生成结果与素材状态、故事时间和参考图版本关联起来，供后续镜头核对和复用。作者报告，这套方法在多项基准中改善了跨镜头一致性，摘要所述结果限于论文评测。制作团队可以把这个设计用在现有分镜表里，为每镜写清剧情引发的变化、应延续的属性和已确认的参考图版本。</p>

<p lang="en">StateWeaver links approved results to the asset state, story time, and reference version so later shots can check and reuse them. The authors report better cross-shot consistency across several benchmarks, with the evidence in the abstract limited to the paper’s evaluations. Production teams can apply the same idea to an existing storyboard by recording what changes in each shot, what carries forward, and which reference version has been approved.</p>
