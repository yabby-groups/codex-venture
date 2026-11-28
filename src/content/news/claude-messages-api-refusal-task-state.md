---
category: "coding"
summaryEn: "Claude’s Messages API can return a classifier refusal in a normal response. Treat stop_reason set to refusal as a separate task outcome and test that it stays out of your completion metrics."
summaryZh: "Claude Messages API 可以在正常响应中返回分类器拒答。为 stop_reason 为 refusal 的响应设置独立业务状态，并补一条回归测试，避免把拒答计入完成率。"
tags: ["claude", "messages-api", "response-handling", "regression-testing"]
titleEn: "Handle Claude Messages API refusals as a separate task outcome"
titleZh: "Claude API 正常返回时，用 stop_reason 识别拒答"
type: "insights"
version: "Claude Messages API documentation as of 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T18:01:27+08:00"
sources: [{"title": "Refusals and Fallback of Anthropic Models", "url": "https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback"}]
---
<p lang="zh-CN">如果 Claude Messages API 的调用没有报错就触发任务完成，应用可能把分类器拒答也记成完成。Anthropic 的文档说明，这类拒答以正常响应返回，<code>stop_reason</code> 为 <code>refusal</code>，<code>stop_details.category</code> 给出对应的政策类别。应先检查停止原因，再把生成结果交给下游。<a href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">Anthropic 官方文档</a></p>

<p lang="en">If your app marks a task complete whenever a Claude Messages API call returns without an error, it can count a classifier refusal as a completed task. Anthropic’s documentation says this refusal arrives as a normal response with <code>stop_reason</code> set to <code>refusal</code>. The <code>stop_details.category</code> field identifies the policy category. Check the stop reason before handing the result downstream. <a href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">Anthropic documentation</a></p>

<p lang="zh-CN">可在响应处理测试中准备三个用例：已生成且符合应用完成条件的结果、带有 <code>refusal</code> 的正常响应，以及请求错误。分别核对任务状态、用户提示和指标。拒答用例应进入单独的业务状态、显示相应提示，并从成功完成的计数中排除。文档列出的模型包括 Claude Fable 5、5.1 和 5.2，Claude Opus 5 和 5.5，以及 Claude Sonnet 5.5 和 Claude Haiku 5.5。<a href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">Anthropic 官方文档</a></p>

<p lang="en">Use three response-handling cases in your regression tests: a generated result that meets your app’s completion criteria, a normal response with <code>refusal</code>, and a request error. Check the task state, user-facing message, and metrics for each case. The refusal should get its own task state and message, and stay out of the successful completion count. The documentation lists Claude Fable 5, 5.1, and 5.2, Claude Opus 5 and 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5. <a href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">Anthropic documentation</a></p>
