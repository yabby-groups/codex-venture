---
category: "coding"
summaryEn: "Sightline can wait for a Windows UI change to settle. Its README explains when the default capture can miss a fast transition and why supplying an earlier baseline helps."
summaryZh: "Sightline 可以等待 Windows 界面变化趋于稳定。项目文档指出了默认捕获可能漏掉快速变化的条件，以及何时需要预先指定基准画面。"
tags: ["sightline", "windows", "ui-automation"]
titleEn: "How Sightline’s first frame determines which Windows UI changes it can detect"
titleZh: "Sightline 的首帧为何决定它能检测到哪些 Windows 界面变化"
type: "insights"
version: "Windows 10 and 11 README verified 2026-11-25"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T18:03:28+08:00"
sources: [{"title": "Show HN: Sightline – Windows CLI for AI agents to capture UI and map DPI coords", "url": "https://github.com/sao-coding/sightline"}]
---
<p lang="zh-CN">给 Windows 桌面应用录制操作结果时，点击之后何时截图会影响看到的状态。Sightline 项目文档称，其命令行工具可以捕获被遮挡的窗口，并等待画面发生变化后趋于稳定。这让脚本可以按画面状态决定何时截图。<a href="https://github.com/sao-coding/sightline">Sightline 项目文档</a></p>

<p lang="en">When capturing the result of an action in a Windows desktop app, the timing of the screenshot determines which state it shows. Sightline’s project documentation says its CLI can capture covered windows and wait for the image to change and settle. That gives a script a visual condition for deciding when to capture the result. <a href="https://github.com/sao-coding/sightline">Sightline project documentation</a></p>

<p lang="zh-CN">时序上的限制出现在第一帧。根据 README，默认基准帧约在启动后 0.3 秒捕获。如果变化已经结束，等待逻辑就可能错过它。文档为这类场景提供了预先指定基准画面的选项。README 还注明，窗口坐标计算和裁剪仅在 100% DPI 缩放的显示器上经过验证。以上范围来自 2026 年 11 月 25 日核对的 Windows 10 和 11 项目文档。</p>

<p lang="en">The timing limit is in the first frame. The README says the default baseline is captured about 0.3 seconds after startup. If a change has already finished, the wait can miss it. The documentation offers a way to supply an earlier baseline for that case. It also says window coordinate calculations and cropping were verified only on displays at 100% DPI scaling. These details come from the Windows 10 and 11 project documentation verified November 25, 2026.</p>
