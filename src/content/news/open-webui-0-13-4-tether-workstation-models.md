---
category: "coding"
summaryEn: "Open WebUI v0.13.4 replaces Direct Connections with Tether, letting users access workstation models, tools, and terminals from another device through a connected Open WebUI instance."
summaryZh: "Open WebUI v0.13.4 用 Tether 取代 Direct Connections。用户可以从另一台设备打开已连接的 Open WebUI，调用工作站上的模型、工具和终端。"
tags: ["open-webui", "tether", "local-models", "mcp"]
titleEn: "Open WebUI 0.13.4 brings workstation models and tools to other devices with Tether"
titleZh: "Open WebUI 0.13.4 用 Tether 连接工作站上的模型和工具"
blocks: [{"kind": "notice", "text": {"en": "If a workstation model is missing, compare its ID with the IDs of models already in Open WebUI. A Tether model with a matching ID is hidden.", "zh": "如果找不到工作站上的模型，先对照 Open WebUI 已有模型的 ID。Tether 模型的 ID 与已有模型重复时会被隐藏。"}, "title": {"en": "Check for duplicate model IDs", "zh": "检查模型 ID 是否重复"}}]
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T06:32:25+08:00"
sources: [{"title": "v0.13.4", "url": "https://github.com/open-webui/open-webui/releases/tag/v0.13.4"}]
---
<p lang="zh-CN">Open WebUI 在 2026 年 11 月 17 日发布的 v0.13.4 中用 Tether 取代 Direct Connections。在工作站上运行 Ollama、LM Studio 或其他 OpenAI 兼容服务的用户，可以从笔记本打开已连接的 Open WebUI，选用同一台工作站上的模型。</p>

<p lang="en">Open WebUI replaced Direct Connections with Tether in v0.13.4, released November 17, 2026. If you run Ollama, LM Studio, or another OpenAI-compatible service on a workstation, you can open a connected Open WebUI instance on your laptop and select models served by that workstation.</p>

<h2><span lang="zh-CN">从工作站到远端界面</span><span lang="en">From the workstation to the remote interface</span></h2>

<p lang="zh-CN">先在工作站的 Tether 应用中添加本地服务，再将 Tether 与 Open WebUI 连接。打开已连接的实例后，模型出现在模型选择器中，OpenAPI 和 MCP 工具出现在加号菜单的工具列表中，Open Terminal 服务出现在终端菜单中。这些入口仅对连接用户可见。根据发布说明，Open WebUI 经由 Tether 访问这些服务，服务地址、启动命令和密钥留在工作站上。</p>

<p lang="en">Add the local services in the Tether app on your workstation, then connect Tether to Open WebUI. In the connected instance, models appear in the model picker, OpenAPI and MCP tools appear in the Tools list under the plus menu, and Open Terminal servers appear in the terminal menu. These entries are visible only to the connected user. According to the release notes, Open WebUI reaches the services through Tether, while their addresses, launch commands, and keys stay on the workstation.</p>

<p lang="zh-CN">基础连接需要 Tether 0.1.14 或更新版本，MCP 服务需要 0.1.16 或更新版本。如果模型已经出现，但工具或终端没有出现，检查 Open WebUI 实例是否启用了 ENABLE_TOOL_SERVERS。</p>

<p lang="en">Basic connections require Tether 0.1.14 or later, and MCP servers require 0.1.16 or later. If models appear but tools or terminals are missing, check whether ENABLE_TOOL_SERVERS is enabled on the Open WebUI instance.</p>
