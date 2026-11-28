---
category: "audio"
summaryEn: "Camilo Quintas’s fictional bike-rental agent offers a way to evaluate a model switch. Find where callers wait, then use the same peak workload to compare latency, capacity and cost, and check how calls recover when the model fails."
summaryZh: "借 Camilo Quintas 的虚构租车案例，先定位来电者在哪个环节等待，再用同一组高峰负载比较延迟、容量和成本，最后验收模型故障时通话能否恢复。"
tags: ["voice-ai", "inference", "open-weight-models"]
titleEn: "What to measure before moving a phone agent to an open-weight model"
titleZh: "电话代理高峰期回复慢，换开放权重模型前该测什么？"
blocks: [{"kind": "notice", "text": {"en": "The bicycle-rental agent and figures are illustrative. The decision table draws on Quintas’s published scenario and has not been tested on a live phone system.", "zh": "自行车租赁代理和数字均为示意。决策表根据 Quintas 发表的案例整理，未经真实电话系统实测。"}, "title": {"en": "Scope of the example", "zh": "案例适用范围"}}, {"columns": [{"en": "Decision", "zh": "要做的决定"}, {"en": "What to record", "zh": "要记录的数据"}], "kind": "comparison", "rows": [[{"en": "Where does the caller’s wait come from?", "zh": "来电者的等待发生在哪一环？"}, {"en": "Measure from the end of the caller’s turn to the start of audible playback. Record stage timings for speech recognition, model response and speech synthesis.", "zh": "记录从来电者说完到听见回复的时间，同时记录语音识别、模型响应和语音合成各阶段的耗时。"}], [{"en": "Which configurations can handle the rush?", "zh": "哪些配置能撑住高峰？"}, {"en": "Compare the current API and each candidate using the same peak call volume and concurrency. Record long pauses, the capacity each configuration needs and its estimated cost.", "zh": "让现用 API 和候选配置使用相同的高峰来电量与并发条件，记录长停顿、各配置所需容量和预估成本。"}], [{"en": "What has to work before the switch?", "zh": "切换前要验收什么？"}, {"en": "Check that the agent keeps track of the requested bike count and asks for a missing pickup time. Define how the call should recover if the model times out, and check what the caller actually hears.", "zh": "检查代理能否记住租车数量，并在缺少取车时间时追问。约定模型超时后通话应如何恢复，并核对来电者实际听到的提示。"}]], "title": {"en": "A decision table for a voice model migration", "zh": "电话代理换模型的决策表"}}]
type: "insights"
version: "2026-11 · Choosing the Inference Stack for Voice AI, Part 1"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 73, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:35:16+08:00"
sources: [{"title": "From Closed to Open-Weight LLMs: Choosing the Inference Stack for Voice AI", "url": "https://github.com/KmiQ/articles/blob/main/choosing-the-inference-stack-for-voice-ai.md"}]
---
<p lang="zh-CN">周六早上，来电者想订第二天上午的两辆自行车，代理只需追问几点取车。门店一多，这句简短的追问却可能让来电者等得更久。Camilo Quintas 在 2026 年 11 月发表的文章中用这个虚构场景演练扩容决策。案例里的语言模型 API 账单随来电量上涨，高峰期部分回复前的停顿也变长。评估把语言模型作为替换变量，沿用原有的语音识别和语音合成。<a href="https://github.com/KmiQ/articles/blob/main/choosing-the-inference-stack-for-voice-ai.md">Quintas 的原文</a></p>

<p lang="en">On a Saturday morning, a caller asks for two bikes for the next day. The agent only needs to ask what time they want to pick them up. Once more shops use the agent, even that short follow-up can take longer to arrive. Camilo Quintas uses this fictional scenario in a November 2026 article to explore a scaling decision. The language model API bill grows with call volume, and some replies take longer to start during the rush. The exercise varies the language model while keeping the existing speech recognition and synthesis components in place. <a href="https://github.com/KmiQ/articles/blob/main/choosing-the-inference-stack-for-voice-ai.md">Quintas’s original article</a></p>

<p lang="zh-CN">把这套思路用到自己的试点时，先用通话时间戳判断长停顿集中在哪一环，再设定团队能接受的高峰等待时间。用同一批代表性通话比较现用 API 和开放权重候选配置，就能把各方案放在相同的负载和服务目标下估算容量与成本。</p>

<p lang="en">To apply the approach to your own pilot, start with call timestamps to see which stage accounts for the long pauses. Then set a wait-time target for peak hours. Using the same representative calls for the current API and each open-weight configuration lets you estimate capacity and cost against the same load and service target.</p>

<p lang="zh-CN">把对话行为和故障恢复设为切换条件。比如，代理收到“两辆车、明天上午”后，应该记住数量并继续问具体时间。团队也可以在评估中模拟一次模型超时，检查这一轮如何继续，以及来电者会听到什么。配置达到高峰容量、成本和对话验收目标后，团队才有依据决定是否切换。</p>

<p lang="en">Make conversation behavior and failure recovery part of the cutover criteria. After hearing “two bikes tomorrow morning,” the agent should retain the quantity and ask for a specific time. The team can also simulate a model timeout to check how the turn resumes and what the caller hears. Once a configuration meets the peak capacity, cost and conversation targets, the team has a basis for deciding whether to switch.</p>
