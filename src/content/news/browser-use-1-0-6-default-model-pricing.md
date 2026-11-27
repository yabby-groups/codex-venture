---
category: "agents"
summaryEn: "Scripts that omit llm switch from bu-fast to bu-4.0 after upgrading. Input and output token rates are both 15 times higher, and explicitly selecting bu-fast keeps the previous rates."
summaryZh: "升级后，省略 llm 的脚本会从 bu-fast 切换到 bu-4.0，输入和输出 token 单价均为原来的 15 倍。显式指定 bu-fast 可保留原单价。"
tags: ["browser-use", "browser-automation", "pricing"]
titleEn: "Browser Use 1.0.6 switches to BU 4.0 by default, raising token rates 15-fold"
titleZh: "Browser Use 1.0.6 默认改用 BU 4.0，token 单价变为原来的 15 倍"
blocks: [{"kind": "notice", "text": {"en": "To keep the previous model and its token rates, pass llm='bu-fast' explicitly in calls that currently omit llm.", "zh": "如果需要沿用原模型和 token 单价，在原先省略 llm 的调用中显式传入 llm='bu-fast'。"}, "title": {"en": "Keeping the previous model", "zh": "如何保留原模型"}}]
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T07:15:50+08:00"
sources: [{"title": "browser-use 1.0.6", "url": "https://github.com/browser-use/browser-use/releases/tag/1.0.6"}]
---
<p lang="zh-CN">Browser Use 于 2026 年 11 月 16 日发布 1.0.6。在 Browser Use 网关上，现有脚本里的 <code>Agent(task)</code> 和 <code>ChatBrowserUse()</code> 只要没有指定 <code>llm</code>，升级后就会从 <code>bu-fast</code> 切换到 <code>bu-4.0</code>。默认推理档也从 medium 升到 high。<a href="https://github.com/browser-use/browser-use/releases/tag/1.0.6">官方发布说明</a></p>

<p lang="en">Browser Use released 1.0.6 on November 16, 2026. After the upgrade, existing <code>Agent(task)</code> and <code>ChatBrowserUse()</code> calls that omit <code>llm</code> switch from <code>bu-fast</code> to <code>bu-4.0</code> on the Browser Use gateway. The default reasoning level also rises from medium to high. <a href="https://github.com/browser-use/browser-use/releases/tag/1.0.6">Official release notes</a></p>

<p lang="zh-CN">按发布说明列出的价格，每百万输入 token 从 0.12 美元升至 1.80 美元，每百万输出 token 从 0.60 美元升至 9.00 美元。发布方报告的一次短任务从 0.0014 美元升至 0.022 美元，单次多花 0.0206 美元。这个差额来自该次测试，其他任务的费用取决于实际用量。</p>

<p lang="en">At the rates listed in the release notes, one million input tokens rose from $0.12 to $1.80, and one million output tokens rose from $0.60 to $9.00. In one short task reported by the project, the cost rose from $0.0014 to $0.022, an increase of $0.0206. That difference reflects the reported test. Costs for other runs depend on actual usage.</p>
