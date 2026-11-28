---
category: "coding"
summaryEn: "Use Mutek to replay end-to-end tests with one simulated fault at a time. A stronger assertion should pass on the normal app and fail when the business result it checks is wrong."
summaryZh: "用 Mutek 一次模拟一个故障，检查端到端测试能否发现业务结果出错。补强后的断言应在正常轮通过，并在对应结果出错时失败。"
tags: ["mutek", "kane-cli", "end-to-end-testing", "mutation-testing"]
titleEn: "How Mutek checks whether passing end-to-end tests catch a fault"
titleZh: "用 Mutek 检查全绿的端到端测试能否发现故障"
blocks: [{"kind": "notice", "text": {"en": "The workflow covers faults derived from traffic the suite already generates. A business path outside that traffic needs its own test before this workflow can assess it.", "zh": "这套流程覆盖从测试已有流量中生成的故障。业务路径没有进入这些流量时，需要先为该路径补上测试，才能用这套流程检查。"}, "title": {"en": "Coverage boundary", "zh": "覆盖边界"}}]
type: "workflows"
version: "Mutek and Kane CLI demo documented 2026-11-26"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 82, "tier": "standard", "audience": "core"}
published: "2026-11-28T08:04:15+08:00"
sources: [{"title": "Would your AI-written tests fail if the app were broken? I built Mutek to find out", "url": "https://dev.to/dab0s/would-your-ai-written-tests-fail-if-the-app-were-broken-i-built-mutek-to-find-out-4nj2"}]
---
<p lang="zh-CN">B0s 在一间演示商店里用 Kane CLI 跑了六条由编码代理编写的端到端测试，六条都通过。随后，Mutek 模拟了一次订单列表错误，六条测试仍然全绿。对维护自有 Web 应用的团队来说，可以把这个案例变成一项评审检查：挑一个业务结果，确认结果出错时，测试会因对应的断言而失败。<a href="https://dev.to/dab0s/would-your-ai-written-tests-fail-if-the-app-were-broken-i-built-mutek-to-find-out-4nj2">B0s 的原文</a></p>

<p lang="en">B0s used Kane CLI to run six end-to-end tests written by a coding agent for a demo shop. All six passed. Mutek then simulated an error in the order list, and all six still passed. Teams maintaining their own web apps can turn that example into a review check. Pick a business outcome and verify that the relevant assertion fails when the outcome is wrong. <a href="https://dev.to/dab0s/would-your-ai-written-tests-fail-if-the-app-were-broken-i-built-mutek-to-find-out-4nj2">B0s’s original write-up</a></p>

<h2><span lang="zh-CN">用两轮结果验收断言</span><span lang="en">Verify the assertion in two runs</span></h2>

<p lang="zh-CN">按作者描述，先在测试环境跑正常版本，再由 Mutek 在浏览器和应用之间的代理上一次模拟一个故障，例如返回错误的订单总额。用 Kane CLI 重跑同一套测试，并关闭自愈，避免测试在重跑时自行适应异常页面。故障轮仍全绿时，把漏报交给编码代理补强。作者的做法是每次只加一条自然语言测试步骤，再用两轮结果验收：正常轮通过，故障轮因目标断言失败。任一条件未满足，就撤回这次修改。</p>

<p lang="en">In the author’s workflow, start with a normal run in the test environment. Mutek then uses a proxy between the browser and the app to simulate one fault at a time, such as an incorrect order total. Replay the same suite with Kane CLI and turn off self-healing so the test cannot adapt to the faulty page during replay. If the suite still passes, send the missed fault to the coding agent. B0s allows one additional plain-English test step per attempt. Keep the change when the normal run passes and the faulty run fails at the intended assertion. Otherwise, revert it.</p>

<p lang="zh-CN">评审时可把故障描述、目标断言和两轮结果放在一起。比如总额显示错误时，记录失败是否来自金额断言，这样就能看出补上的步骤是否检查了预期的业务结果。本文依据 B0s 对演示及流程的说明，未复跑该演示。</p>

<p lang="en">Keep the simulated fault, the intended assertion, and both run results together in review. For an incorrect order total, record whether the amount assertion caused the failure. That tells reviewers whether the new step checked the intended business outcome. This article draws on B0s’s account of the demo and workflow, which we did not rerun.</p>
