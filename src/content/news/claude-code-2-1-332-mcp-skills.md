---
category: "coding"
summaryEn: "Claude Code now lists skills from MCP servers in its slash menu in beta. A separate hook lets teams block inline shell commands as skills or commands load."
summaryZh: "Claude Code 开始在斜杠菜单中列出 MCP 服务器提供的技能，目前处于测试阶段。团队还可通过新增钩子，在加载技能或命令时拦截内联 Shell 命令。"
tags: ["claude-code", "mcp", "skills", "hooks"]
titleEn: "Claude Code v2.1.332 adds MCP skills to the slash menu"
titleZh: "Claude Code v2.1.332 在斜杠菜单中加入 MCP 技能"
published: "2026-11-25T13:22:37+08:00"
sources: [{"title": "v2.1.332", "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.332"}]
---
<p lang="zh-CN">Anthropic 在 Claude Code v2.1.332 中加入了 MCP 服务器技能的测试版支持。服务器提供的技能会以 <code>server:skill</code> 的形式出现在 <code>/</code> 菜单中，方便用户在选择技能时辨认它来自哪个服务器。</p>

<p lang="en">Claude Code v2.1.332 adds beta support for skills from MCP servers. The <code>/</code> menu shows them as <code>server:skill</code>, so users can see which server provides a skill before selecting it.</p>

<p lang="zh-CN">同一版本还新增了 <code>PreSkillShellCommand</code> 钩子，可在加载技能或命令时拒绝其中的内联 Shell 命令。如果团队把这个钩子写入共享设置，仍在使用 v2.1.331 或更早版本的成员会在启动时看到一个对话框。</p>

<p lang="en">The release also adds the <code>PreSkillShellCommand</code> hook, which can block inline shell commands as a skill or command loads. If a team adds the hook to its shared settings, members on v2.1.331 or earlier will see a dialog at startup.</p>
