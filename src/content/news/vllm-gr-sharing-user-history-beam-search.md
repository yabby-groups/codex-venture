---
category: "open-source"
summaryEn: "vLLM-GR extends vLLM with beam search so a single recommendation request can explore multiple item IDs while sharing cached user history across candidate paths."
summaryZh: "vLLM-GR 为 vLLM 加入束搜索，让一次推荐请求可以探索多个条目 ID，并在候选路径之间复用用户历史缓存。"
tags: ["vllm", "recommendation", "inference"]
titleEn: "How vLLM-GR shares cached user history across recommendation candidates"
titleZh: "vLLM-GR 如何在推荐候选路径之间复用用户历史缓存"
type: "insights"
version: "2026-11-24 announcement"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T00:04:42+08:00"
sources: [{"title": "vLLM-GR: Efficient Inference for Generative Recommendation", "url": "https://vllm.ai/blog/2026-11-24-vllm-gr-announcement"}]
---
<p lang="zh-CN">视频流需要在一次请求的延迟预算内拿到一组可推荐的候选。vLLM-GR 团队在 2026 年 11 月 24 日的发布文章中以 OneRec-1.7B 为例，说明生成式推荐如何从观看历史出发，生成 128 个候选语义 ID。这些 ID 表示应用可考虑纳入推荐流的条目。</p>

<p lang="en">A video feed needs a set of recommendation candidates within a single request’s latency budget. In its November 24, 2026 announcement, the vLLM-GR team used OneRec-1.7B to illustrate how a generative recommender can turn viewing history into 128 candidate semantic IDs. Those IDs represent items the application can consider for the feed.</p>

<p lang="zh-CN">vLLM-GR 在 vLLM 的模型执行、调度和分页 KV 缓存之上加入束搜索。一次请求内的多条候选路径共享用户历史的缓存，候选筛选在加速器上进行。这一设计针对重复处理历史和反复与主机协调的开销。团队还将对已有候选打分列为另一种用法。128 是文中示例的候选数量，实际延迟和吞吐需要结合部署环境测量。<a href="https://vllm.ai/blog/2026-11-24-vllm-gr-announcement">vLLM-GR 团队发布文章</a></p>

<p lang="en">vLLM-GR adds beam search to vLLM’s model execution, scheduling, and paged KV cache. Candidate paths within a request share the cached user history, and candidate selection runs on the accelerator. The design targets repeated history processing and per-step coordination with the host. The team also describes scoring an existing set of candidates as a separate use case. The count of 128 comes from the example, while latency and throughput need to be measured in the deployment environment. <a href="https://vllm.ai/blog/2026-11-24-vllm-gr-announcement">vLLM-GR team announcement</a></p>
