---
category: "audio"
summaryEn: "Use an n8n HTTP Request node to send a video link for transcription, then check the returned item before wiring up an automatic reply."
summaryZh: "用 n8n 的 HTTP Request 节点提交视频链接，在接入自动回复前检查返回的转录条目。"
tags: ["n8n", "apify", "transcription"]
titleEn: "Check video transcripts in n8n before turning on automatic replies"
titleZh: "用 n8n 转录视频时，先检查结果再开启自动回复"
blocks: [{"kind": "notice", "text": {"en": "The URL is sent to a hosted Apify Actor. Choose inputs you are authorized to share with that service.", "zh": "链接会发送给 Apify 托管的 Actor。选用你有权向该服务提供的素材。"}, "title": {"en": "Where the input goes", "zh": "输入发往哪里"}}]
type: "workflows"
version: "n8n 1.x · author-documented Apify Actor workflow"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:17:31+08:00"
sources: [{"title": "3 Free n8n Workflows That Turn TikToks and Podcasts Into Data (Copy and Paste)", "url": "https://dev.to/aemon-cz/3-free-n8n-workflows-that-turn-tiktoks-and-podcasts-into-data-copy-and-paste-30dh"}]
---
<p lang="zh-CN">Aemon 的 n8n 示例用同一条 HTTP 调用处理几种转录任务。以收取视频链接的流程为例，n8n 将链接交给作者的 Apify Actor，等待返回视频条目，再由下游节点整理转录和摘要。作者报告使用 n8n 1.x 测试。</p>

<p lang="en">Aemon’s n8n examples use the same HTTP call for several transcription jobs. In the video-link workflow, n8n sends a link to the author’s Apify Actor, waits for the video items, then passes them to downstream nodes to format the transcript and summary. The author reports testing on n8n 1.x.</p>

<p lang="zh-CN">先用一个获准处理的视频链接检查调用。按作者的做法，把 Apify 令牌存入 n8n 的 Header Auth 凭据，让 HTTP Request 节点用 Bearer 认证发起同步调用，并启用 AI 分析。按文档预期，响应中的视频列表会在 n8n 中拆成独立条目。<a href="https://dev.to/aemon-cz/3-free-n8n-workflows-that-turn-tiktoks-and-podcasts-into-data-copy-and-paste-30dh">Aemon 的调用示例</a></p>

<p lang="en">Start with one video link you have permission to process. Following Aemon’s setup, store the Apify token in an n8n Header Auth credential. Use it for Bearer authentication in the HTTP Request node, call the Actor synchronously, and enable AI analysis. The documented result is a video list that n8n splits into individual items. <a href="https://dev.to/aemon-cz/3-free-n8n-workflows-that-turn-tiktoks-and-podcasts-into-data-copy-and-paste-30dh">Aemon’s request example</a></p>

<p lang="zh-CN">连接回复节点前，先把返回条目与原视频对照，确认转录与摘要可读。将空列表或调用失败转为明确的失败提示，避免发送空白摘要。遇到认证错误时，先检查节点是否选择了正确的 Header Auth 凭据。</p>

<p lang="en">Before connecting the reply node, check the returned item against the source video and confirm that the transcript and summary are usable. Route empty lists and request failures to an explicit error message so users receive a clear outcome. If authentication fails, first check which Header Auth credential the node is using.</p>
