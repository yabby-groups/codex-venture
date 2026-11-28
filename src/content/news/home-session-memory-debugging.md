---
category: "agents"
summaryEn: "HoMe pairs memory snapshots with execution traces to help developers distinguish a missed write from a maintenance or retrieval failure."
summaryZh: "HoMe 把记忆快照和执行轨迹对起来，帮助开发者区分漏写、后续维护丢失和查询时没捞到。"
tags: ["memory", "evaluation", "reme"]
titleEn: "When an assistant forgets, check the session where it should have remembered"
titleZh: "助手忘了旧信息，先查它该记住的那轮会话"
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:24:29+08:00"
sources: [{"title": "HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants", "url": "https://arxiv.org/abs/2611.34624"}]
---
<p lang="zh-CN">跨会话助手漏掉一条旧信息时，可以先查它在相关会话结束后有没有进入记忆。Yifei Xu 等人于 11 月 25 日提交的 HoMe 预印本，把会话级记忆版本和执行轨迹放在一起，用来判断多个错答是否源于同一轮会话、同一个记忆组件。</p>

<p lang="en">When an assistant misses something from an earlier conversation, first check whether the information made it into memory at the end of that session. In the HoMe preprint submitted on November 25, Yifei Xu and colleagues pair session-level memory versions with execution traces to see whether several wrong answers point to the same session and memory component.</p>

<p lang="zh-CN">排查时，可以先找信息写入后的版本，再沿版本检查它是否在后续维护中消失。如果查询前仍然存在，就看检索轨迹里有没有它。HoMe 还会复用已经构建的记忆。作者在开源 ReMe 上做了完整初测，随后在 LongMemEval-S 和 BEAM 上各进行六次正式候选评估。据作者报告，找到的配置在两个基准上都提高了任务表现，同时减少了查询阶段的 token 用量。</p>

<p lang="en">Start with the memory version after the information should have been written, then check later versions to see whether maintenance removed it. If it was still present just before the query, check the retrieval trace. HoMe also reuses previously built memory. After a full baseline evaluation on the open-source ReMe system, the authors ran six formal candidate evaluations apiece on LongMemEval-S and BEAM. They report finding configurations that improved task performance on both benchmarks while using fewer tokens at query time.</p>
