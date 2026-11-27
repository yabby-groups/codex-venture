---
category: "coding"
summaryEn: "Cline CLI v3.0.75 defaults to yolo mode when a one-shot prompt arrives as an argument or through stdin. Check explicit modes and auto-approval settings before upgrading CI scripts."
summaryZh: "Cline CLI v3.0.75 将通过命令参数或 stdin 传入提示词的一次性运行默认切到 yolo 模式。维护 CI 脚本时，可先检查是否显式指定了模式，以及自动批准如何设置。"
tags: ["cline", "cli", "ci"]
titleEn: "Cline CLI v3.0.75 makes yolo mode the default for one-shot runs"
titleZh: "Cline CLI v3.0.75 将一次性运行默认切到 yolo 模式"
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T04:45:33+08:00"
sources: [{"title": "CLI v3.0.75", "url": "https://github.com/cline/cline/releases/tag/cli-v3.0.75"}]
---
<p lang="zh-CN">把提示词作为命令参数传给 Cline，或经由标准输入（stdin）送入提示词，都会触发一次性运行。Cline 在 2026 年 11 月 21 日发布的 CLI v3.0.75 中，将这两种入口的默认模式从 act 改为 yolo。升级后，采用这两种入口的 CI 和定时任务即使命令文本没变，也可能以不同的模式启动。<a href="https://github.com/cline/cline/releases/tag/cli-v3.0.75">Cline 发布说明</a></p>

<p lang="en">Passing a prompt as a command-line argument or piping it through standard input starts a one-shot Cline run. In CLI v3.0.75, released November 21, 2026, Cline changed the default for both entry points from act to yolo. CI jobs and scheduled tasks using either entry point can therefore start in a different mode after the upgrade even if the command itself stays the same. <a href="https://github.com/cline/cline/releases/tag/cli-v3.0.75">Cline release notes</a></p>

<p lang="zh-CN">如果脚本的执行方式依赖工具审批，先检查命令和保存设置。显式指定模式、通过 <code>--auto-approve false</code> 或保存设置关闭自动批准、保存了 plan 模式，以及使用 <code>/team</code> 提示词，都会让调用避开新的 yolo 默认值。团队工具需要在 act 模式下使用。如果一次性调用需要这些工具，可以显式传入 <code>--act</code>。</p>

<p lang="en">If a script depends on a particular tool approval behavior, check both the command and its saved settings. An explicit mode flag, disabling auto-approval with <code>--auto-approve false</code> or through saved settings, a saved plan mode, and <code>/team</code> prompts all take the invocation out of the new yolo default. Team tools require act mode. Pass <code>--act</code> when a one-shot invocation needs those tools.</p>

<p lang="zh-CN">同一版本还修复了一次性运行首轮无法中断的问题。现在 <code>--timeout</code> 和 Ctrl+C 都能在首轮生效。</p>

<p lang="en">The release also fixes an interruption bug in one-shot runs. Both <code>--timeout</code> and Ctrl+C can now stop the first turn.</p>
