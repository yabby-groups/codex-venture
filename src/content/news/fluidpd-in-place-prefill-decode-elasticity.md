---
category: "models"
summaryEn: "FluidPD lets decode workers absorb short prefill bursts and reassigns running workers when demand shifts persist. At a fixed worker count, the authors report gains of up to 47.9 percentage points in latency SLO attainment on their sustained-shift workloads."
summaryZh: "FluidPD 用有余量的 decode 工作者分担短时 prefill 压力，用原地切换角色处理持续偏移。作者在工作者数量固定的持续偏移实验中报告，延迟服务目标达标率最高提升 47.9 个百分点。"
tags: ["fluidpd", "inference-serving", "prefill-decode", "latency"]
titleEn: "FluidPD Shifts Workers Between Prefill and Decode Without Restarting"
titleZh: "FluidPD 无需重启即可调整 Prefill 与 Decode 分工"
editorial: {"score": 72, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T17:31:21+08:00"
sources: [{"title": "FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving", "url": "https://arxiv.org/abs/2610.06917"}]
---
<p lang="zh-CN">把大模型推理拆成处理输入的 prefill 池和生成输出的 decode 池后，固定配比可能让一边排队、另一边仍有余量。11 月 26 日列入 arXiv 公告的 FluidPD v2 预印本提出两种调度手段，分别对应短时突发和持续的需求配比偏移。</p>

<p lang="en">When LLM serving uses separate pools for processing input and generating output, a fixed worker split can leave one pool queueing while the other has spare capacity. The FluidPD v2 preprint listed in arXiv’s November 26 announcements describes two scheduling mechanisms for short bursts and sustained shifts in demand.</p>

<p lang="zh-CN">短时突发时，FluidToken 让有余量的 decode 工作者分担有限的 prefill 计算。需求偏移持续时，FluidRole 原地切换正在运行的工作者角色，省去模型重新加载和推理引擎重启。两种机制都依据反映各阶段压力的指标做调度。</p>

<p lang="en">During a burst, FluidToken gives decode workers with spare capacity a bounded share of prefill computation. When the shift persists, FluidRole reassigns running workers in place, avoiding a model reload or engine restart. Both mechanisms use indicators of pressure in each phase to guide scheduling.</p>

<p lang="zh-CN">作者在根据 Azure 生产轨迹和 ShareGPT 对话构造的持续偏移负载上报告，在相同工作者数量下，FluidPD 的延迟服务目标达标率比各负载对应的最佳静态配比最高高出 47.9 个百分点。做容量评审时，可以把短时突发和持续偏移分别纳入压测，同时记录两池的排队情况和可用余量，再判断短时借用算力和调整角色配比各能解决哪类问题。<a href="https://arxiv.org/abs/2610.06917">arXiv 预印本</a></p>

<p lang="en">On workloads with sustained demand shifts derived from Azure production traces and ShareGPT conversations, the authors report up to a 47.9-percentage-point gain in latency SLO attainment over the best static split for each load, with the same worker count. For capacity planning, test bursts and sustained shifts separately and track queueing and spare capacity in both pools. Those measurements help identify where temporary offloading or role reassignment could help. <a href="https://arxiv.org/abs/2610.06917">arXiv preprint</a></p>
