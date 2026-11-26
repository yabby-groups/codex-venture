---
category: "coding"
summaryEn: "Review an AI-proposed test fix by recording the behavior the assertion must protect, then check that the assertion itself fails on an input that violates that contract."
summaryZh: "审查 AI 提交的测试修复时，先记录断言必须保护的行为，再用一份违反约定的输入确认目标断言确实会失败。"
tags: ["ai-code-review", "testing", "ci"]
titleEn: "How to verify an AI-proposed fix for a flaky test"
titleZh: "AI 修好间歇性失败的测试后，如何验证断言仍然有效"
blocks: [{"kind": "notice", "text": {"en": "Changing a fixture can make several assertions fail at once. Check the failing assertion or run the target assertion in isolation to confirm what it caught.", "zh": "修改测试数据可能同时触发多条断言。核对具体失败的断言，或单独运行目标断言，确认它实际捕获了什么。"}, "title": {"en": "Confirm which assertion failed", "zh": "确认失败的是哪条断言"}}]
type: "workflows"
version: "Assertion review for intermittent CI failures"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T00:04:30+08:00"
sources: [{"title": "A green build does not prove the AI made the right change", "url": "https://dev.to/redfred7/a-green-build-does-not-prove-the-ai-made-the-right-change-49ig"}, {"title": "A Flaky Test or a Real Bug? Start With the Evidence", "url": "https://dev.to/muhammad_usman_sqa/a-flaky-test-or-a-real-bug-start-with-the-evidence-16h8"}, {"title": "My Guard Test Could Never Fail: Two Backslashes Arrived as One", "url": "https://dev.to/dbsoul/my-guard-test-could-never-fail-two-backslashes-arrived-as-one-2j2p"}]
---
<p lang="zh-CN">代码代理把一条间歇性失败的测试改绿后，审查者可以先写下这条测试原本要保护的行为。Fred Heath 用一个假想的订单案例说明了这个判断的价值。代理发现断言依赖事件顺序，于是放宽断言，测试随即通过。在案例设定中，原来的失败恰好暴露了竞态。若事件顺序属于业务约定，审查就应追查顺序在哪一步失去保证。<a href="https://dev.to/redfred7/a-green-build-does-not-prove-the-ai-made-the-right-change-49ig">Fred Heath 的原文</a></p>

<p lang="en">When a coding agent turns an intermittently failing test green, start the review by writing down the behavior the test was meant to protect. Fred Heath illustrates the value of that step with a hypothetical order-processing example. The agent notices that the assertion depends on event order, relaxes it, and gets a passing test. In the scenario, the original failure exposed a race condition. If event order is part of the business contract, the review should trace where that guarantee breaks down. <a href="https://dev.to/redfred7/a-green-build-does-not-prove-the-ai-made-the-right-change-49ig">Fred Heath’s article</a></p>

<p lang="zh-CN">接着保留第一次失败的具体报错，比较同一代码修订上的运行结果。Muhammad Usman 在讨论 Playwright 测试时指出，一次失败后重跑成功，仍可能涉及应用竞态、共享测试数据或网络中断。把首个失败位置和报错与后续运行对照，再决定要检查产品行为、测试逻辑还是运行环境。<a href="https://dev.to/muhammad_usman_sqa/a-flaky-test-or-a-real-bug-start-with-the-evidence-16h8">Muhammad Usman 的原文</a></p>

<p lang="en">Keep the detailed error from the first failure and compare runs on the same revision. In his discussion of Playwright tests, Muhammad Usman notes that a passing rerun can follow an application race, shared test data problems, or a network interruption. Compare the original failure location and error with later runs before deciding whether to investigate product behavior, test logic, or the environment. <a href="https://dev.to/muhammad_usman_sqa/a-flaky-test-or-a-real-bug-start-with-the-evidence-16h8">Muhammad Usman’s article</a></p>

<p lang="zh-CN">最后用一份符合约定的输入和一份明确违反约定的输入检查目标断言。Sungsoo Youn 报告，他的代理生成测试文件时，正则表达式的单词边界变成了退格字符。他把旧措辞放回文档后，测试确实变红，但报错来自另外两项检查。审查记录可写下要保护的行为、两份输入的预期结果，以及实际失败的断言位置。这一流程整理自三位作者的公开文章，案例性质分别见各段归属。<a href="https://dev.to/dbsoul/my-guard-test-could-never-fail-two-backslashes-arrived-as-one-2j2p">Sungsoo Youn 的原文</a></p>

<p lang="en">Finally, check the target assertion with one input that satisfies the contract and one that clearly violates it. Sungsoo Youn reports that when his agent generated a test file, regex word boundaries became backspace characters. Restoring the old wording made the test fail, but two other checks caused that failure. The review record can capture the behavior under test, the expected result for each input, and the location of the assertion that actually failed. This workflow draws on the three authors’ published accounts, with each example attributed above. <a href="https://dev.to/dbsoul/my-guard-test-could-never-fail-two-backslashes-arrived-as-one-2j2p">Sungsoo Youn’s article</a></p>
