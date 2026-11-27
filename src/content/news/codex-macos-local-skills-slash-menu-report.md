---
category: "agents"
summaryEn: "After a macOS desktop update, one Codex user reported that enabled local skills vanished from the slash menu while the skill inventory still listed them."
summaryZh: "一位 macOS 用户报告，升级 Codex 桌面版后，斜杠菜单找不到已启用的本地技能，但技能清单仍能识别它们。"
tags: ["codex", "macos", "skills"]
titleEn: "A Codex macOS report traces missing slash-menu entries to a desktop update"
titleZh: "一位 Codex 用户记录了 macOS 升级后本地技能从斜杠菜单消失"
type: "stories"
version: "Codex desktop for macOS 26.1111.71025 and 26.1117.31558"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:21:07+08:00"
sources: [{"title": "macOS desktop regression in 26.1117.31558: enabled local skills disappear from the slash menu", "url": "https://github.com/openai/codex/issues/62700"}]
---
<p lang="zh-CN">11 月 20 日，hongboji 在 <a href="https://github.com/openai/codex/issues/62700">Codex 的公开问题跟踪器</a>上记录了 Apple Silicon Mac 上的一次升级前后对照。桌面版 26.1111.71025 的聊天输入框原本能通过斜杠菜单选中本地技能。升级到 26.1117.31558 后，输入完整技能名称也找不到对应条目。</p>

<p lang="en">On November 20, hongboji documented a before-and-after comparison on an Apple Silicon Mac in the <a href="https://github.com/openai/codex/issues/62700">public Codex issue tracker</a>. In desktop build 26.1111.71025, a local skill was selectable from the chat composer’s slash menu. After updating to 26.1117.31558, even entering the full skill name failed to surface it.</p>

<p lang="zh-CN">为了确认技能是否仍被识别，hongboji 强制刷新了 <code>skills/list</code>。据报告，结果仍将全部 16 个 NocoBase 技能列为已启用，且没有解析错误。对这个环境而言，检查技能清单和检查输入框的候选菜单给出了不同结果。</p>

<p lang="en">To check whether the skills were still recognized, hongboji forced a refresh of <code>skills/list</code>. They reported that all 16 NocoBase skills still appeared as enabled, with no parsing errors. In that setup, the skill inventory and the composer’s suggestions gave different answers.</p>

<p lang="zh-CN">截至 11 月 26 日核对，工单状态为「关闭，未列入计划」。可确认的影响范围是报告者在这两版上的菜单表现，技能实际执行和其他环境仍待核实。</p>

<p lang="en">As checked on November 26, the issue was closed as not planned. The evidence covers the reporter’s menu behavior in those two builds. Skill execution and other environments remain unverified.</p>
