---
category: "coding"
summaryEn: "Design a read-only appointment lookup around the caller’s question, then test duplicate names, missing dates, and connection failures with sample rows."
summaryZh: "围绕来电者查询预约时间的需求设计只读流程，再用模拟记录检查同名、日期缺失和连接失败的处理。"
tags: ["spreadsheets", "automation", "read-only"]
titleEn: "Build a read-only appointment lookup from a shared spreadsheet"
titleZh: "用共享表格做一个只读预约查询"
blocks: [{"kind": "notice", "text": {"en": "Enforce read-only access through the spreadsheet account or connection. Removing edit controls from the interface leaves the underlying permissions as they were.", "zh": "由电子表格账号或连接强制执行只读权限。移除界面的编辑按钮不会改变底层权限。"}, "title": {"en": "Where to enforce access", "zh": "在哪里限制访问权限"}}]
type: "workflows"
version: "Platform-independent design · hypothetical example"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:17:31+08:00"
sources: [{"title": "Keep the spreadsheet. Start with the question callers keep asking.", "url": "https://dev.to/fusionaldev/keep-the-spreadsheet-start-with-the-question-callers-keep-asking-13f8"}]
---
<p lang="zh-CN">客户来电问上门时间时，接线员需要找到排期并判断记录是否还有效。FusionAL 以一家虚构的小型维修店为例，提出一个只读查询流程。接线员输入姓名或电话号码，界面显示匹配的工单、预约日期、状态和最近更新时间，再由接线员确认答复。<a href="https://dev.to/fusionaldev/keep-the-spreadsheet-start-with-the-question-callers-keep-asking-13f8">FusionAL 原文</a></p>

<p lang="en">When a customer calls to ask when a technician will arrive, the person answering needs to find the appointment and judge whether the record is current. FusionAL uses a hypothetical repair business to propose a read-only lookup. The operator enters a name or phone number, reviews the matching job, date, status, and last update time, then decides what to tell the caller. <a href="https://dev.to/fusionaldev/keep-the-spreadsheet-start-with-the-question-callers-keep-asking-13f8">FusionAL’s write-up</a></p>

<p lang="zh-CN">先请维护排期表的人解释底色、空白日期和备注里的简写。已确认的含义可以直接展示。含义不清的记录保留原值，并标记为需要人工核对。</p>

<p lang="en">Ask the people who maintain the schedule to explain row colors, blank dates, and shorthand in the notes. Display meanings they can confirm. For ambiguous entries, show the source value and flag it for human review.</p>

<h2><span lang="zh-CN">用模拟数据验收</span><span lang="en">Acceptance checks with sample data</span></h2>

<ul><li><span lang="zh-CN">同名客户应同时显示，并提供足够的信息让接线员区分。</span><span lang="en">Show both customers who share a name and give the operator enough information to tell them apart.</span></li><li><span lang="zh-CN">查询无匹配时明确提示。同一工单有两条记录时显示冲突。缺失的日期标为缺失。</span><span lang="en">Report when there is no match, surface conflicting rows for the same job, and label missing dates.</span></li><li><span lang="zh-CN">表格连接失败时显示故障。如果提供缓存副本，标出缓存时间。</span><span lang="en">Report a failed spreadsheet connection. If a cached copy is shown, display its timestamp.</span></li></ul>
