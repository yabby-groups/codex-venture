---
category: "coding"
summaryEn: "Tokendoctor can send requests during a pause to keep a long Claude Code session cached. The trade-off is the cost of extra cache reads against a possible cache rewrite when work resumes."
summaryZh: "tokendoctor 可在暂停期间发请求，为 Claude Code 长会话保留提示词缓存。是否划算，取决于额外的缓存读取成本与恢复工作时可能产生的重写成本。"
tags: ["claude-code", "prompt-caching", "tokendoctor"]
titleEn: "What it costs to keep a Claude Code session cached during a break"
titleZh: "Claude Code 暂停期间保留缓存，有哪些成本"
type: "insights"
version: "tokendoctor keepalive documentation, November 2026"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T12:03:38+08:00"
sources: [{"title": "Keep Claude Code's prompt cache warm over lunch, if your breaks pay", "url": "https://github.com/localixai/tokendoctor/blob/main/site/content/docs/keepalive.md"}]
---
<p lang="zh-CN">按照 tokendoctor 的项目文档，Claude Code 的长会话在缓存过期后，恢复工作时可能要重新写入整段对话。tokendoctor 为此提供了默认关闭的 keepalive。启用后，它会在文档所述的一小时缓存窗口结束前约六分钟发出请求，尝试通过一次缓存读取延长窗口。</p>

<p lang="en">According to the tokendoctor documentation, resuming a long Claude Code session after its cache entry expires can require writing the conversation to the cache again. Tokendoctor offers a keepalive feature that is off by default. Once enabled, it attempts to renew the documented one-hour window with a cache read about six minutes before it expires.</p>

<p lang="zh-CN">项目文档称，每次保活都会在会话分支里重发上一条请求，再要求模型给出简短回复。分支没有工具，回复也不会进入主会话。每次保活仍会产生请求，因此是否划算取决于用户何时回来，以及缓存读取和重新写入的相对成本。文档描述的是预期机制，实际节省需要结合会话用量核算。<a href="https://github.com/localixai/tokendoctor/blob/main/site/content/docs/keepalive.md">tokendoctor 项目文档</a></p>

<p lang="en">The project documentation says each ping repeats the last request in a fork and asks for a short reply. The fork has no tools, and the reply stays out of the main conversation. Every ping still makes a request, so the economics depend on when the user returns and the relative cost of cache reads and writes. The documentation describes the intended mechanism. Actual savings depend on session usage. <a href="https://github.com/localixai/tokendoctor/blob/main/site/content/docs/keepalive.md">Tokendoctor project documentation</a></p>
