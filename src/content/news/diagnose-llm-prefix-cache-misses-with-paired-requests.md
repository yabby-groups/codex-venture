---
category: "coding"
summaryEn: "Establish a baseline with identical requests, then vary one early field at a time. Cached input tokens and request timing help distinguish prefix changes from cache expiry."
summaryZh: "先原样重发建立基线，再逐项改变靠前的字段，用缓存输入 token 数和请求间隔区分前缀变化与缓存过期。"
tags: ["llm-api", "prompt-caching", "diagnostics"]
titleEn: "How to diagnose LLM prompt cache misses with paired requests"
titleZh: "请求几乎一样，为什么缓存输入变少了？用成对请求排查"
blocks: [{"items": [{"en": "Confirm that an unchanged request qualifies for prefix caching under your provider’s rules, then repeat it within the documented cache window.", "zh": "确认原样请求符合供应商的前缀缓存条件，再在文档给出的有效窗口内重发。"}, {"en": "Change one early field per comparison, such as a timestamp or tool order. Compare cached input tokens against the unchanged baseline at a similar interval.", "zh": "每次对照只改一个靠前的字段，例如时间戳或工具顺序。控制发送间隔，与原样请求的缓存输入 token 数对比。"}, {"en": "Repeat the unchanged request at a longer interval to check expiry. After a fix, compare cached input and billed usage over a representative conversation.", "zh": "拉长间隔再发原样请求，检查过期因素。调整后用一段有代表性的多轮会话核对缓存输入量和计费用量。"}], "kind": "steps", "title": {"en": "Isolate a cache miss with paired requests", "zh": "用成对请求定位缓存未命中"}}]
type: "workflows"
version: "Provider-neutral prefix caching workflow documented on 2026-11-25"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 85, "tier": "featured", "audience": "core"}
published: "2026-11-28T20:10:38+08:00"
sources: [{"title": "LLM Prompt Cache Misses: Find the Changes That Break Prefix Reuse", "url": "https://dev.to/jackm-singularity/llm-prompt-cache-misses-find-the-changes-that-break-prefix-reuse-5g08"}]
---
<p lang="zh-CN">如果多轮请求看起来几乎相同，缓存输入 token 却很少，先检查每次实际发送的请求开头。Jack M 在排查指南中举了两个容易漏掉的变化：靠前的时间戳每次都更新，或者工具清单包含相同的工具却每次排序不同。对于按匹配前缀复用计算的实现，越靠前的变化越可能缩短可复用部分。<a href="https://dev.to/jackm-singularity/llm-prompt-cache-misses-find-the-changes-that-break-prefix-reuse-5g08">Jack M 的排查指南</a></p>

<p lang="en">If requests look almost identical across turns but usage shows few cached input tokens, inspect the beginning of the request you actually send. Jack M’s diagnostic guide calls out two easy-to-miss changes. An early timestamp can update on every request, or the same tools can arrive in a different order. With matching-prefix caches, an early change can shorten the reusable portion. <a href="https://dev.to/jackm-singularity/llm-prompt-cache-misses-find-the-changes-that-break-prefix-reuse-5g08">Jack M’s diagnostic guide</a></p>

<p lang="zh-CN">选一条有代表性的请求作基线。诊断日志只留够用的结构信息，例如块的位置、类型、工具顺序和同一测试内用于对比的结构指纹，省去原始提示词、工具参数和会话内容。如果原样重发也复用不稳，先核对当前模型的最低长度、缓存有效期和路由条件，再解释单字段实验的差异。上线前用供应商的实际用量或账单核对费用变化。本流程来自文档分析，未对特定供应商运行测试。</p>

<p lang="en">Pick one representative request as a baseline. In diagnostic logs, keep only the structural details needed for comparison, such as block positions and types, tool order, and structural fingerprints for that test. Omit raw prompts, tool arguments, and conversation text. If unchanged repeats show inconsistent reuse, check the model’s minimum length, expiry window, and routing conditions before interpreting single-field tests. Verify any cost change against provider usage or billing before rollout. This workflow is based on documentation and was not tested against a specific provider.</p>
