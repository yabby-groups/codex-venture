---
category: "coding"
summaryEn: "Use the original error and the intended page control to decide whether to accept an AI-suggested locator change, even when the rerun passes."
summaryZh: "评审 AI 建议的定位器变更时，结合原始报错和测试要操作的控件判断是否接受修改，即使重跑已经通过。"
tags: ["playwright", "testing", "ai-assisted-coding"]
titleEn: "How to review AI-suggested Playwright locator fixes"
titleZh: "如何审查 AI 建议的 Playwright 定位器修复"
blocks: [{"items": [{"en": "Read the original failure and identify whether the locator or the assertion failed.", "zh": "查看原始报错，判断失败发生在定位阶段还是断言阶段。"}, {"en": "For a locator failure, compare the proposed selector’s match with the original test’s intended control.", "zh": "如果是定位失败，对照原测试的意图，检查候选选择器匹配的是哪个控件。"}, {"en": "Record the selected control, the reason for accepting or rejecting the change, and the result of rerunning the original assertion if the change is accepted.", "zh": "记录候选定位器匹配的控件、接受或拒绝修改的理由，以及接受修改后重跑原断言的结果。"}], "kind": "workflow", "title": {"en": "What to capture in the review", "zh": "评审记录应包含什么"}}]
type: "workflows"
version: "Playwright locator review guidance, November 26, 2026"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T03:02:50+08:00"
sources: [{"title": "When a Self-Healing Locator Should Say No", "url": "https://dev.to/muhammad_usman_sqa/when-a-self-healing-locator-should-say-no-3ico"}]
---
<p lang="zh-CN">页面上有两个名称相近的按钮时，AI 建议的新定位器可能让 Playwright 测试通过，却把点击操作转到了另一个按钮。QA 从业者 Muhammad Usman 用这类情形说明定位器修复的评审难点。下面的工作流依据他的文章整理，适用于人工审查 AI 提出的选择器变更。<a href="https://dev.to/muhammad_usman_sqa/when-a-self-healing-locator-should-say-no-3ico">Usman 的原文</a></p>

<p lang="en">When a page has two buttons with similar names, an AI-suggested locator can make a Playwright test pass while sending the click to a different button. QA practitioner Muhammad Usman uses cases like this to explain why locator repairs need review. This workflow adapts his written guidance for human review of AI-proposed selector changes. <a href="https://dev.to/muhammad_usman_sqa/when-a-self-healing-locator-should-say-no-3ico">Usman’s original article</a></p>

<p lang="zh-CN">评审时，将失败日志、原测试的操作和断言、候选定位器一并提交。若原定位器已找到元素，只是显示文本与断言不符，就先保留失败并调查产品行为。若报错发生在定位阶段，则根据测试步骤确认它原本要操作的控件，再检查新定位器在页面上指向哪里。比如两个区域都有“保存”按钮，评审者应确认命中的是当前测试正在编辑的表单。</p>

<p lang="en">Bring the failure log, the original test action and assertion, and the proposed locator into the review. If the original locator found an element and the assertion failed on its displayed text, preserve the failure and investigate the product behavior. If element lookup failed, use the test steps to identify the intended control, then check what the proposed locator finds. If two sections have a Save button, for example, verify that the match is in the form the test is editing.</p>
