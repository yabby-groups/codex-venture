---
titleZh: "从 Open VSX 安装 Continue 前要核对什么"
titleEn: "What to check before installing Continue from Open VSX"
summaryZh: "把扩展版本、模型提供方和代码传输路径一起核对。"
summaryEn: "Check the extension version, model provider, and where code is sent."
type: "plugins"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Open VSX 2.1.0"
status: "current"
tested: false
project: "continue-extension"
tags: ["ide","open-vsx","continue"]
sources: [{"title":"What to check before installing Continue from Open VSX – primary reference","url":"https://open-vsx.org/extension/Continue/continue"},{"title":"Open VSX version metadata","url":"https://open-vsx.org/api/Continue/continue/latest"},{"title":"Continue telemetry documentation","url":"https://docs.continue.dev/telemetry"}]
---
<p lang="zh-CN">Open VSX 的 Continue 条目可用于在支持该扩展市场的 VS Code 系编辑器中查找安装包。核实当天公开 API 的最新条目为 2.1.0，列出 Apache 2.0 许可证。安装前以所用编辑器显示的发布者与兼容版本为准。</p>

<p lang="en">Open VSX provides Continue’s distribution listing for VS Code–based editors that use the marketplace. Its public API showed version 2.1.0 and Apache 2.0 on the verification date. Confirm the publisher and compatible version in your own editor before installation.</p>

<p lang="zh-CN">可先用公开仓库测试解释函数或提出补丁。模型走所选提供方，远程 API 的费用按对应服务计费。把编辑器遥测设置与推理数据路径分别核对，尤其要确认发送哪些代码上下文和由谁处理。本文仅核实资料。</p>

<p lang="en">Try explaining a function or requesting a patch in a public repository first. Model requests go to the selected provider, whose charges apply to remote API usage. Review editor telemetry settings and the inference data path separately, including which code context is sent and who processes it. This profile is documentation-based.</p>
