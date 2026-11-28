---
category: "coding"
summaryEn: "A simulator's sentence-splitting bug inflated the apparent cost of RAG citation checks. Recheck input format, first verified sentence latency, and quota held by cancelled streams."
summaryZh: "模拟器的断句缺陷夸大了 RAG 引用校验的开销。复测时分别检查输入格式、首个已校验句子的延迟和取消后仍占用的配额。"
tags: ["rag", "load-testing", "streaming"]
titleEn: "Check the simulator before judging the cost of RAG citation checks"
titleZh: "评估 RAG 引用校验开销前，先检查压测模拟器的断句"
blocks: [{"items": [{"en": "Run representative real-model and simulated outputs through the same checker. Include boundaries such as bullets and footnote markers, and record which cases each source causes the checker to stop.", "zh": "用同一个检查器处理有代表性的真实模型输出和模拟输出，覆盖项目符号、脚注编号等边界，并记录两类输入各自触发了哪些拦截。"}, {"en": "Change one neighboring feature at a time under the same load. Record check time, time to the first verified sentence, and delivered answers separately.", "zh": "保持负载一致，每次只调整一项相邻功能。分别记录检查耗时、首个已校验句子的延迟和成功交付的回答数。"}, {"en": "Test deliberate failures at several rates and track how long cancelled streams continue to occupy quota.", "zh": "按不同的比例主动制造失败，记录取消的流还会占用配额多久。"}], "kind": "workflow", "title": {"en": "Rerun the load test", "zh": "重新跑一轮压测"}}]
type: "workflows"
version: "Ayush Singh's revised test, 2026-11-26"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 84, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:03:20+08:00"
sources: [{"title": "My Simulation Exaggerated the Cost of My Own Safety Feature", "url": "https://dev.to/ayush_singh321/my-simulation-exaggerated-the-cost-of-my-own-safety-feature-565p"}]
---
<p lang="zh-CN">Ayush Singh 用模拟模型服务给流式 RAG 做压测。模拟器会复制材料中的句子并附上引用，但它在项目符号和脚注编号前漏判了句界，导致两句话共用一个引用标记。逐句检查器因此拦下缺少引用的句子。Singh 让模拟器采用与检查器一致的断句方式后，在 82 条测试提示中观察到的模拟误停从 15 次降到 0 次。<a href="https://dev.to/ayush_singh321/my-simulation-exaggerated-the-cost-of-my-own-safety-feature-565p">Singh 的复盘</a></p>

<p lang="en">Ayush Singh load-tested a streaming RAG system with a simulated model service. It copied sentences from source passages and appended citations, but missed sentence boundaries before bullets and footnote numbers. That left two sentences sharing one citation marker, so the checker stopped the uncited sentence. After Singh aligned the simulator's sentence splitting with the checker's, reported false stops fell from 15 to zero across 82 test prompts. <a href="https://dev.to/ayush_singh321/my-simulation-exaggerated-the-cost-of-my-own-safety-feature-565p">Singh's write-up</a></p>

<p lang="zh-CN">Singh 在修正后的测试中报告，逐句检查约耗时 3 毫秒，新旧版本交付的回答数接近。当他将故意失败的回答提高到四分之一时，已取消的流继续占用配额，新版交付量随之落后。数字来自作者自己的测试，适合用来确定下一轮要测哪些指标。</p>

<p lang="en">In the revised test, Singh reported that sentence checks took about 3 ms and the two versions delivered nearly the same number of answers. When he raised the deliberately failing share to one in four, cancelled streams still held quota and the newer version fell behind. These are the author's measurements and can help identify what to track in a separate load test.</p>
