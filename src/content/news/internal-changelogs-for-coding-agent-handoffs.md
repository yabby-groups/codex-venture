---
category: "coding"
summaryEn: "Adam Juhasz’s team recorded why changes were made and which approaches had already been ruled out. He reports less rework across coding sessions. A four-field template adapts the practice for repository handoffs."
summaryZh: "Adam Juhasz 的团队把改动理由和已否决的方案写进仓库日志。据他分享，这减少了编码代理跨会话的返工。文末提供可复制的四栏交接模板。"
tags: ["coding-agents", "developer-workflow", "changelogs"]
titleEn: "A changelog that tells the next coding agent what the team already ruled out"
titleZh: "用内部变更日志告诉下一轮编码代理，哪些方案已经被否决"
blocks: [{"code": "## YYYY-MM-DD — 决策标题 / Decision title\n\n### 改了什么 / What changed\n[写出行为变化和适用范围 / Describe the behavior change and its scope]\n\n### 为什么改 / Why it changed\n[记录触发改动的观察或需求 / Record the observation or requirement that prompted it]\n\n### 否决了什么 / What was ruled out\n[写出试过或考虑过的方案，以及放弃的原因 / Name the option tried or considered and why it was dropped]\n\n### 有什么后果 / Consequences\n[说明保留的限制、代价或需要留意的边界行为 / Note any remaining limit, trade-off, or edge-case behavior]", "file": "", "kind": "code", "language": "text", "title": {"en": "Four-field template for a repository changelog", "zh": "可放进仓库的四栏变更日志模板"}}]
type: "stories"
version: "Adam Juhasz’s November 23, 2026 account"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 85, "tier": "featured", "audience": "core"}
published: "2026-11-28T06:01:22+08:00"
sources: [{"title": "Internal Changelogs unlock autonomous coding agents", "url": "https://rallywith.ai/blog/internal-changelogs"}]
---
<p lang="zh-CN">Adam Juhasz 在 2026 年 11 月 23 日发表的文章里写到，编码代理开了新会话后，有时会重新实现团队已经放弃的设计，甚至把上个月删掉的功能加回来。他的做法是把内部变更日志放在代码旁边，请代理写下每次改动的理由。团队查看了一些运行记录后，又把试过或考虑过的弯路加进日志。</p>

<p lang="en">In a November 23, 2026 post, Adam Juhasz describes coding agents starting a fresh session and sometimes rebuilding a design the team had abandoned or restoring a feature it had removed the month before. His approach was to keep an internal changelog alongside the code and have agents record why each change was made. After reviewing some agent traces, the team added options that had been tried or considered and then dropped.</p>

<p lang="zh-CN">文中的一条日志记录了图片预览遇到的问题。读取存储中的图片后，第二次授权调用耗时约一秒。团队将授权调整为每次读取操作检查一次，放弃了需要额外处理失效状态的跨请求授权缓存。日志也写明了代价。权限撤销时，已经在途的读取可能继续完成，后续请求会重新验证并看到权限变化。</p>

<p lang="en">One entry describes an image preview whose second authorization call took about a second after the image was read from storage. The team moved to a single authorization check per read operation and dropped a cross-request authorization cache that would have added invalidation state. The entry also records the trade-off. A read already in progress may finish after access is revoked, while later requests reauthenticate and pick up the permission change.</p>

<p lang="zh-CN">Juhasz 报告说，加上内部日志后，团队在新会话里少做了重复工作，也少花时间盯着代理走偏。原文给出了具体决策，但没有提供量化的前后对照。下次把相关代码交给新会话时，可以先请代理读对应条目，指出哪些旧方案已经排除，以及这次改动是否会触及当时接受的代价。<a href="https://rallywith.ai/blog/internal-changelogs">Adam Juhasz 的原文</a></p>

<p lang="en">Juhasz reports that the internal log reduced repeated work between sessions and the time his team spent watching for false starts. The post gives a concrete decision example, with no measured before-and-after comparison. When handing the same part of the codebase to a fresh session, ask the agent to read the relevant entry first, identify which approaches were ruled out, and check whether the new change affects a trade-off the team accepted. <a href="https://rallywith.ai/blog/internal-changelogs">Adam Juhasz’s original post</a></p>
