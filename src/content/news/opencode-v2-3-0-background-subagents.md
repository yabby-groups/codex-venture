---
category: "coding"
summaryEn: "Developers can delegate independent code investigations and keep working in the parent session while subagents run. Each subagent reports back when it goes idle."
summaryZh: "开发者可以把互不依赖的代码调查交给子代理，同时在主会话继续工作。子代理进入空闲状态时会回报结果。"
tags: ["opencode", "subagents", "terminal-ui"]
titleEn: "OpenCode v2.3.0 runs subagents in the background by default"
titleZh: "OpenCode v2.3.0 默认在后台运行子代理"
editorial: {"score": 73, "tier": "standard", "audience": "core"}
published: "2026-11-28T07:45:54+08:00"
sources: [{"title": "v2.3.0", "url": "https://github.com/anomalyco/opencode/releases/tag/v2.3.0"}]
---
<p lang="zh-CN">OpenCode 在 11 月 13 日发布的 v2.3.0 中，将子代理任务转到后台执行。发起任务后，父会话会立即收到子代理的会话 ID，可以接着工作。子代理进入空闲状态时，会把结果报告给父会话。<a href="https://github.com/anomalyco/opencode/releases/tag/v2.3.0">发布说明</a></p>

<p lang="en">OpenCode v2.3.0, released on November 13, moves subagent tasks to the background. The parent session receives the subagent’s session ID immediately and can keep working. The subagent reports back to the parent when it goes idle. <a href="https://github.com/anomalyco/opencode/releases/tag/v2.3.0">Release notes</a></p>

<p lang="zh-CN">例如，重构前可以把两项只读调查并行分派。一项梳理某个模块的代码入口和调用方，另一项盘点现有测试覆盖了哪些行为。主会话可以同时整理改动目标和验收条件。等两份报告到齐，再对照调用方和测试覆盖，决定哪些接口可以改、哪些行为需要先补测试。</p>

<p lang="en">Before a refactor, for example, you can delegate two read-only investigations in parallel. Ask one subagent to map the module’s entry points and callers, and the other to identify the behaviors covered by existing tests. Use the parent session to draft the goals and acceptance criteria in the meantime. Once both reports arrive, use the caller map and test coverage together to decide which interfaces to change and which behaviors need tests first.</p>

<p lang="zh-CN">同一版本的终端界面默认将连续的工具调用和思考过程合并到一条可展开的活动行。需要逐步查看时，可在设置中把 Verbosity 调到 <code>medium</code> 或 <code>high</code>，也可以通过终端界面配置中的 <code>session.verbosity</code> 调整。升级时会保留已有的详细度设置。<a href="https://github.com/anomalyco/opencode/releases/tag/v2.3.0">发布说明</a></p>

<p lang="en">The same release groups runs of tool calls and reasoning into a single expandable activity row by default in the terminal UI. To see each step, set Verbosity to <code>medium</code> or <code>high</code> in settings, or adjust <code>session.verbosity</code> in the terminal UI configuration. Upgrading preserves an existing verbosity setting. <a href="https://github.com/anomalyco/opencode/releases/tag/v2.3.0">Release notes</a></p>
