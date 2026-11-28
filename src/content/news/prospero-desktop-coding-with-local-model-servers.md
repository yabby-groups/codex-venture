---
category: "coding"
summaryEn: "Prospero connects to an existing compatible model server and puts the session transcript, subagents, and background jobs in one desktop workspace. It ships without a preconfigured provider."
summaryZh: "Prospero 可接入已有的兼容模型服务，把会话记录、子代理和后台任务放在同一个桌面工作区。模型供应商需要自行配置。"
tags: ["prospero", "local-models", "imgui"]
titleEn: "Prospero gives existing model servers a desktop coding workspace"
titleZh: "Prospero 给已有模型服务接上桌面编码工作区"
type: "insights"
version: "Windows、macOS、Linux · README 核对于 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 67, "tier": "standard", "audience": "core"}
published: "2026-11-28T16:02:11+08:00"
sources: [{"title": "Prospero: Bloat-free, native AI coding harness with ImGui", "url": "https://github.com/skeeto/prospero"}]
---
<p lang="zh-CN">已经运行 llama.cpp 或 vLLM 的开发者，可以先对照现有服务的 API 判断 Prospero 是否适合接入。项目 README 将它描述为基于 ImGui 的原生桌面编码工具，支持 Windows、macOS 和 Linux，可连接本地或远程的 OpenAI Chat Completions 兼容端点，也支持 Anthropic Messages API。首次使用时需要自行配置模型供应商。</p>

<p lang="en">If you already run llama.cpp or vLLM, start by checking whether your existing endpoint speaks an API Prospero supports. The project README describes an ImGui-based native desktop coding tool for Windows, macOS, and Linux. It connects to local or remote OpenAI Chat Completions-compatible endpoints and also supports the Anthropic Messages API. Users supply their own provider configuration.</p>

<p lang="zh-CN">README 中的 macOS 截图展示了标准布局：左侧列出会话与子代理，中间保留交互记录，右侧显示后台任务和计划。如果你经常在长任务中回来查看进度，可以据此判断自己关心的信息能否在同一屏找到。具体端点的连接表现，以及后台任务实际跑得怎样，仍需在自己的环境里验证。</p>

<p lang="en">The README’s macOS screenshot shows the standard layout with sessions and subagents on the left, the transcript in the middle, and background jobs and the plan on the right. If you regularly return to long tasks to check their progress, the layout shows whether the information you look for is visible together. Connection behavior and background execution still need to be checked in your own environment.</p>

<p lang="zh-CN">项目通过 Unlicense 将自身代码奉献至公有领域，README 亦注明随附的第三方代码各有许可。接口和布局信息来自项目文档。<a href="https://github.com/skeeto/prospero">项目仓库</a></p>

<p lang="en">The project dedicates its own code to the public domain through the Unlicense. The README notes that bundled third-party code has its own licenses. The API and layout details come from the project documentation. <a href="https://github.com/skeeto/prospero">Project repository</a></p>
