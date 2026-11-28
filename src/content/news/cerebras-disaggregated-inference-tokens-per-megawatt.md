---
category: "agents"
summaryEn: "Cerebras says its production setup pairs GPU prompt processing with wafer-scale decoding, yielding five times as many tokens per megawatt at its existing generation speed. Buyers still need their own measurements of response time and cost."
summaryZh: "Cerebras 称其生产系统由 GPU 处理提示词、晶圆级系统生成输出，在保持原有生成速度的同时，每兆瓦 token 产出达到原来的五倍。应用响应时间和费用仍需按自身负载核对。"
tags: ["inference", "cerebras", "latency"]
titleEn: "Cerebras splits prompt processing and generation. What does five times the tokens per megawatt measure?"
titleZh: "Cerebras 用 GPU 处理提示词，每兆瓦五倍 token 衡量的是什么？"
blocks: [{"columns": [{"en": "Metric", "zh": "指标"}, {"en": "What to check", "zh": "采购时核对什么"}], "kind": "comparison", "rows": [[{"en": "Time to first token", "zh": "首 token 延迟"}, {"en": "How long the application waits from sending the request to seeing the first token. Compare at representative prompt lengths and concurrency levels.", "zh": "应用从发出请求到收到首个 token 要等多久。在有代表性的提示词长度和并发下比较。"}], [{"en": "Generation speed", "zh": "后续生成速度"}, {"en": "How quickly tokens arrive on an individual streaming request after output begins.", "zh": "单条流式请求开始输出后，后续 token 到达得有多快。"}], [{"en": "Throughput per megawatt", "zh": "每兆瓦 token 吞吐"}, {"en": "How much output the infrastructure serves per unit of power. Ask which baseline, workload and components the comparison includes.", "zh": "基础设施在单位功耗下能提供多少输出。核对比较所用的基线、工作负载和纳入统计的组件。"}], [{"en": "Actual bill", "zh": "实际账单"}, {"en": "What the application would pay under the service’s billing terms for its own mix of requests.", "zh": "按服务计费条款和自身请求构成，应用实际要支付多少。"}]], "title": {"en": "Four numbers to check when comparing inference services", "zh": "比较推理服务时要分别核对的四项数据"}}]
type: "insights"
version: "2026-11-17 · Cerebras disaggregated inference production deployment"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 71, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:35:16+08:00"
sources: [{"title": "Cerebras Disaggregated Inference", "url": "https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference"}]
---
<p lang="zh-CN">在 Cerebras 于 2026 年 11 月 17 日公布的生产方案里，一条推理请求由两类硬件接力处理。GPU 先读取提示词，完成预填充（prefill）。Cerebras 的晶圆级系统接着逐个生成输出 token，完成解码（decode）。Atharva Talpade 在 Cerebras 官方博客中介绍了这套分工。公司称，这套方案已投入生产，可为其推理云提供更多生成容量，也可供基础设施合作伙伴在自有数据中心采用。<a href="https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference">Cerebras 官方发布</a></p>

<p lang="en">In the production setup Cerebras announced on November 17, 2026, two kinds of hardware handle each inference request. GPUs read and process the prompt during prefill. Cerebras wafer-scale systems then decode the response one token at a time. Atharva Talpade described the split on the company’s blog. Cerebras says the system is in production, adds generation capacity to its inference cloud and is available for infrastructure partners to use in their own data centers. <a href="https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference">Cerebras announcement</a></p>

<p lang="zh-CN">对交互式 Agent 来说，提示词处理和两套硬件之间的交接都发生在首个 token 到达之前。输出开始后，解码决定后续 token 的生成节奏。一次请求可能等得久才开始输出，但随后返回得很快，因此选型时应分别记录首 token 延迟和后续生成速度。</p>

<p lang="en">For an interactive agent, prompt processing and the handoff between the two systems happen before the first token arrives. Once output begins, decoding sets the pace of generation. A request can take a while to start and then stream quickly, so measure time to first token and subsequent generation speed separately.</p>

<p lang="zh-CN">Talpade 报告称，在维持 Cerebras 原有生成速度的同时，这套部署让每兆瓦的 token 产出达到原来的五倍。这是厂商报告的基础设施效率指标。公开摘录未给出足以复算五倍结果的基线口径和负载细节。采购方可用自己的典型提示词和峰值并发核对两项延迟表现，再按供应商的计费条款估算账单。</p>

<p lang="en">Talpade reports that the deployment delivers five times as many tokens per megawatt while maintaining Cerebras’s existing generation speed. That figure is the vendor’s measure of infrastructure efficiency. The published excerpt gives too little detail about the baseline and workload to reproduce the fivefold result. Buyers can check both latency measures using their own typical prompts and peak concurrency, then estimate the bill from the provider’s pricing terms.</p>
