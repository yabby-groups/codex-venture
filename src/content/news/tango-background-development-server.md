---
category: "coding"
summaryEn: "Tango can start a development server in the background so the turn can continue, while keeping the process available for log inspection and shutdown."
summaryZh: "Tango 可以在后台启动开发服务器，让代理继续当前轮次，并支持随后查看日志和停止进程。"
tags: ["tango", "terminal-agents", "development-servers"]
titleEn: "Run a development server in the background with Tango"
titleZh: "用 Tango 在后台启动开发服务器并管理进程"
blocks: [{"items": [{"en": "Start the development command with `background: true` in Tango's bash tool. Keep the returned Tango process ID for follow-up.", "zh": "让 Tango 的 bash 工具以 `background: true` 启动开发命令，保留返回的 Tango 进程 ID。"}, {"en": "Use `process_logs` to check status and recent output. If startup fails with a port conflict, use `process_list` to see whether this Tango session already started a service.", "zh": "用 `process_logs` 查看状态和近期输出。如果启动时提示端口占用，用 `process_list` 检查本次 Tango 会话是否已启动过服务。"}, {"en": "Once you have identified a Tango-managed process you no longer need, stop it with `process_stop`.", "zh": "确认某个由 Tango 管理的进程已不再需要后，用 `process_stop` 停止它。"}], "kind": "workflow", "title": {"en": "Start, inspect, and stop the server", "zh": "启动、检查和停止服务"}}]
type: "workflows"
version: "Tango author demo, 2026-11-26"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 67, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:03:20+08:00"
sources: [{"title": "Three things I fixed so my terminal AI agent stops making me wait", "url": "https://dev.to/cnshsliu/three-things-i-fixed-so-my-terminal-ai-agent-stops-making-me-wait-1a77"}]
---
<p lang="zh-CN">终端编码代理启动开发服务器时，前台命令会一直等服务退出。Tango 作者 cnshsliu 演示了后台启动方式。Tango 给命令约两秒钟暴露启动错误，随后返回自己的进程 ID、系统 PID 和初始输出，当前轮次可以继续。演示的模型回复由脚本提供，界面和进程工具使用的是真实实现。<a href="https://dev.to/cnshsliu/three-things-i-fixed-so-my-terminal-ai-agent-stops-making-me-wait-1a77">作者的演示</a></p>

<p lang="en">A foreground command keeps a terminal coding agent waiting for its development server to exit. Tango author cnshsliu demonstrated a background mode that gives the command about two seconds to surface startup errors, then returns a Tango process ID, the system PID, and initial output so the turn can continue. The demo used scripted model replies with Tango's actual interface and process tools. <a href="https://dev.to/cnshsliu/three-things-i-fixed-so-my-terminal-ai-agent-stops-making-me-wait-1a77">The author's demo</a></p>

<p lang="zh-CN">按作者描述，Tango 同时最多管理八个后台进程，每个保留最后 200,000 个字符的输出，退出 Tango 时会清理这些进程。只读模式拒绝后台启动。</p>

<p lang="en">According to the author, Tango manages up to eight background processes at once, retains the last 200,000 characters of output per process, and cleans up those processes on exit. Read-only mode rejects background starts.</p>
