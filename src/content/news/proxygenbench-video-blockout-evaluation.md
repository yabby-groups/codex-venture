---
category: "video"
summaryEn: "ProxyGenBench evaluated five video generators and found that structural guides improved control over space and time, while more detailed guides sometimes coincided with poorer completion. The benchmark separates three checks for reviewing a shot: structure, completion, and whether prompts reach the intended entities or events."
summaryZh: "ProxyGenBench 评估了五款视频生成器，发现草模能改善时空控制，但草模更精细时，画面补全有时反而更差。验收镜头可以分开看结构、画面补全和提示是否落到指定对象或事件上。"
tags: ["video-generation", "3d-blockouts", "benchmarks"]
titleEn: "ProxyGenBench finds that more detailed blockouts can coincide with poorer video completion"
titleZh: "ProxyGenBench 发现，更精细的动画草模有时伴随更差的画面补全"
blocks: [{"kind": "notice", "text": {"en": "The preprint abstract reports patterns across the evaluation of five video generators. The findings here are limited to the benchmark and conditions described in the abstract.", "zh": "预印本摘要报告了对五款视频生成器评估中观察到的现象。这里的结论范围限于摘要描述的基准和测试条件。"}, "title": {"en": "Scope of the findings", "zh": "结果适用范围"}}]
editorial: {"score": 82, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:32:15+08:00"
sources: [{"title": "ProxyGenBench: Benchmarking Proxy-Guided Video Generation", "url": "https://arxiv.org/abs/2611.34457"}]
---
<p lang="zh-CN">11 月 26 日发布的 ProxyGenBench 预印本用动画草模等结构参考来测试视频生成器。草模可以沿整段镜头交代场景布局、动作、机位和事件顺序。生成器还得补齐草模省略的画面细节、修正其中的瑕疵，并把文字、参考图和声音用到指定的对象或事件上。</p>

<p lang="en">The ProxyGenBench preprint, posted November 26, tests video generators with structural guides such as animated 3D blockouts. A blockout can specify layout, motion, camera behavior, and event order throughout a shot. The generator also has to fill in omitted visual details, correct artifacts in the guide, and apply text, reference images, and audio to the intended entities or events.</p>

<p lang="zh-CN">作者从 60 个场景构建了 312 个用例，覆盖三类场景任务。他们改变草模精细度、文字描述的详细程度和多模态输入，并用逐用例核验的清单评估五款视频生成器。作者报告，提供草模改善了时空控制，但更精细的草模有时伴随较差的画面补全。即使镜头准确跟随了草模，提示也可能落到错误的对象或事件上。<a href="https://arxiv.org/abs/2611.34457">arXiv 预印本</a></p>

<p lang="en">The authors built 312 cases from 60 scenes across three types of scene tasks. They varied blockout fidelity, the level of detail in the text, and the multimodal inputs, then evaluated five video generators using verified, case-specific checklists. They report that structural guides improved control over space and time, while more detailed guides sometimes coincided with poorer completion. A shot could follow its guide closely and still apply a prompt to the wrong entity or event. <a href="https://arxiv.org/abs/2611.34457">arXiv preprint</a></p>

<h2><span lang="zh-CN">看样片时分开验收三项</span><span lang="en">Three checks for reviewing a generated shot</span></h2>

<ul><li><span lang="zh-CN">结构。对照预演，检查动作、机位和事件顺序是否保留。</span><span lang="en">Structure. Compare the shot with the previs and check whether it preserves the motion, camera behavior, and event order.</span></li><li><span lang="zh-CN">补全。检查省略的画面细节是否补齐，草模里的瑕疵是否被带进成片。</span><span lang="en">Completion. Check whether the shot fills in omitted details and whether artifacts from the blockout carry over.</span></li><li><span lang="zh-CN">提示归属。逐项核对文字、参考图和声音是否对应指定的对象或事件。</span><span lang="en">Condition binding. Check whether each text instruction, reference image, and audio cue applies to the intended entity or event.</span></li></ul>
