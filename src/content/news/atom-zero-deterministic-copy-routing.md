---
category: "coding"
summaryEn: "Atom Zero 0.50.0 sends explicit requests to transcribe two to four key-value pairs to a dedicated tool. Its release notes give developers three concrete checks for reviewing a route like this: when it fires, which inputs bypass it, and how callers identify tool output."
summaryZh: "Atom Zero 0.50.0 将明确要求原样转录 2 至 4 对键值的请求交给专用工具。开发者可以借鉴它的设计，在代码审查时核对触发条件、绕过条件和结果来源标记。"
tags: ["atom-zero", "tool-routing", "structured-data"]
titleEn: "How Atom Zero routes exact key-value transcription to a dedicated tool"
titleZh: "Atom Zero 如何把键值对原样转录交给专用工具"
blocks: [{"kind": "notice", "text": {"en": "This workflow draws on Atom Zero’s November 24, 2026 release notes. The expected behavior comes from the project’s description of version 0.50.0 and has not been independently tested.", "zh": "本文依据 Atom Zero 于 2026 年 11 月 24 日发布的版本说明整理。预期行为来自项目对 0.50.0 的描述，未经独立运行验证。"}, "title": {"en": "Source and scope", "zh": "资料与适用范围"}}]
type: "workflows"
version: "0.50.0"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 67, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:47:21+08:00"
sources: [{"title": "Atom Zero 0.50.0: copy routing, weak-stage rehearsal and QKV LoRA", "url": "https://dev.to/mycute_97b39c4e34027570f9/atom-zero-0500-copy-routing-weak-stage-rehearsal-and-qkv-lora-59f"}]
---
<p lang="zh-CN">用户给出 a=1 和 b=2，要求原样转成紧凑 JSON 时，应用要保留用户给出的键和值。Atom Zero 在 0.50.0 的版本说明中介绍了一个做法。聊天和代理路径都可以把符合条件的请求交给确定性的 atomzero-copy 工具，结果中的 source 字段会标记为 copy_tool。<a href="https://dev.to/mycute_97b39c4e34027570f9/atom-zero-0500-copy-routing-weak-stage-rehearsal-and-qkv-lora-59f">Atom Zero 发布说明</a></p>

<p lang="en">When a user supplies a=1 and b=2 and asks for an exact transcription into compact JSON, the app needs to preserve the supplied keys and values. Atom Zero’s 0.50.0 release notes describe one approach. Both chat and agent paths can send matching requests to the deterministic atomzero-copy tool, and the result identifies that path with a source field set to copy_tool. <a href="https://dev.to/mycute_97b39c4e34027570f9/atom-zero-0500-copy-routing-weak-stage-rehearsal-and-qkv-lora-59f">Atom Zero release notes</a></p>

<h2><span lang="zh-CN">审查路由时核对三件事</span><span lang="en">Three checks for a routing review</span></h2>

<ul><li><span lang="zh-CN">把转录意图和输入范围都写进触发条件。按发布说明，Atom Zero 在用户明确要求原样转录、且输入含 2 至 4 对格式有效的键值时才走复制工具。说明列出了紧凑 JSON 示例，也提到键值文本和 YAML 变体。</span><span lang="en">Make intent and input shape part of the trigger. According to the release notes, Atom Zero routes to the copy tool when the user explicitly requests exact transcription and supplies two to four well-formed key-value pairs. The notes give a compact JSON example and mention key-value text and YAML variants.</span></li><li><span lang="zh-CN">分别检查转录内容和结果来源。对符合条件的样例，核对输出是否保留输入的键和值，再检查 source 是否为 copy_tool。来源字段让调用方能直接识别工具路径。</span><span lang="en">Check the transcription and its source separately. For a matching example, verify that the output preserves the input keys and values, then check that source is set to copy_tool. The source field lets callers identify the tool path directly.</span></li><li><span lang="zh-CN">给绕过路由的情况留测试样例。按该版本说明，只有 1 对或有 5 对及以上、键值对格式错误，以及问答、摘要、开放式聊天和比较请求，都应绕过复制工具。</span><span lang="en">Include cases that should bypass the route. The release notes list one pair, five or more pairs, malformed pairs, questions, summaries, open-ended chat, and comparisons as cases that bypass the copy tool.</span></li></ul>
