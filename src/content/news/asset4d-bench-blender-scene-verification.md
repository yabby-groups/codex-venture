---
category: "agents"
summaryEn: "In Asset4D-Bench, both coding agents produced scenes that earned full marks for dynamics and zero for object relationships. Reopening the Blender project makes both checks possible."
summaryZh: "Asset4D-Bench 中，两款编码 Agent 都交付过动力学满分、物体关系零分的场景。重新打开 Blender 工程，可以把这两项分开验收。"
tags: ["blender", "coding-agents", "benchmarks"]
titleEn: "Asset4D-Bench checks what moves together in AI-built Blender scenes"
titleZh: "小车轨迹正确，货物却悬空：Asset4D-Bench 拆解 Blender 场景验收"
editorial: {"score": 87, "tier": "featured", "audience": "core"}
published: "2026-11-28T18:02:25+08:00"
sources: [{"title": "Asset4D-Bench: Benchmarking Coding Agents for Editable 3D and 4D Reconstruction", "url": "https://arxiv.org/abs/2611.33728"}]
---
<p lang="zh-CN">小车可以沿着正确的轨迹移动，车上的货物却悬在车板上。11 月 26 日发布的 Asset4D-Bench 预印本用这个例子说明可编辑场景需要怎样验收。研究者重新打开编码 Agent 交付的 Blender 工程，对照原生参考场景的状态，分别评估运动和物体之间的关系。 <a href="https://arxiv.org/abs/2611.33728">arXiv 预印本</a></p>

<p lang="en">A cart can follow the right path while its cargo floats above the deck. The Asset4D-Bench preprint, released on November 26, uses that example to show what reviewing an editable scene entails. The researchers reopened Blender projects delivered by coding agents and checked motion and object relationships separately against the native reference scenes. <a href="https://arxiv.org/abs/2611.33728">arXiv preprint</a></p>

<p lang="zh-CN">在 24 项从头重建任务中，GPT-6.1-Sol 和 GPT-6-Astra 各有 14 项拿到满额动力学分。在这两组满分作品中，前者有 3 项物体关系得分为零，后者有 8 项。各归档运行采用的执行和恢复策略有差异，因此起始素材本身的作用仍无法从这些记录中单独估计。</p>

<p lang="en">On 24 from-scratch tasks, GPT-6.1-Sol and GPT-6-Astra each earned full dynamics credit on 14. Of those full-credit scenes, three from Sol and eight from Astra scored zero on object relationships. Execution and recovery policies varied across the archived runs, leaving the effect of starter assets unresolved.</p>

<p lang="zh-CN">验收类似的 Blender 交付物，可以分别记录外观、运动轨迹和物体关系。重新打开交付工程，在关键帧检查本应接触的物件是否贴合，并沿时间轴确认应随主体移动的物件有没有脱离。</p>

<p lang="en">For similar Blender handoffs, reviewers can record separate judgments for appearance, motion paths, and object relationships. Reopen the project, inspect expected contact at key frames, and scrub the timeline to see whether objects that should move together stay together.</p>
