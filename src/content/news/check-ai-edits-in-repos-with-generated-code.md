---
category: "coding"
summaryEn: "Use a small edit and a regeneration run to check whether a coding assistant updates the source of truth and produces a patch that survives the build."
summaryZh: "用一次小改动和重新生成，检查编程助手是否改对了源文件，以及补丁能否在项目构建后保留。"
tags: ["coding-agents", "generated-code", "nbdev"]
titleEn: "Check where coding assistants edit in repositories with generated code"
titleZh: "检查编程助手在含生成代码的仓库里改对了文件没有"
type: "workflows"
version: "基于作者自述设计的工作流 / Workflow based on the author’s account published 2026-01-18."
verified: "2026-11-25"
status: "current"
tested: false
published: "2026-11-25T20:56:31+08:00"
sources: [{"title": "Why I Stopped Using nbdev", "url": "https://hamel.dev/blog/posts/ai-stack"}]
---
<p lang="zh-CN">Hamel Husain 曾参与构建和维护 nbdev。他在 2026 年 1 月 18 日的文章中写道，自己后来停止使用它，因为在以 Jupyter Notebook 为源头、再生成 Python 库和文档的工作流里，他用过的 AI 编程工具有时会弄混该编辑笔记本还是生成后的源码。这是作者报告的个人经历，可以用来设计一次针对自己仓库的检查。<a href="https://hamel.dev/blog/posts/ai-stack">Hamel Husain 的原文</a></p>

<p lang="en">Hamel Husain helped build and maintain nbdev. In a January 18, 2026 post, he wrote that he stopped using it after seeing AI coding tools struggle to tell where edits belonged in a workflow that generates a Python library and documentation from Jupyter notebooks. His account suggests a check you can run in your own repository. <a href="https://hamel.dev/blog/posts/ai-stack">Hamel Husain’s account</a></p>

<p lang="zh-CN">在工作分支里挑一个小改动，例如更新一个公开函数及其文档示例。先按项目文档确认源文件、生成产物与更新步骤，写下预期哪些文件应该有差异。把任务和仓库规则交给助手，记录它首先编辑了哪个文件，并保存补丁供人工审查。</p>

<p lang="en">On a working branch, pick a small change, such as updating a public function and its documentation example. Use your project’s documentation to identify the source files, generated outputs, and regeneration steps. Record which files you expect to change. Give the assistant the task and repository rules, then note which file it edits first and save the patch for review.</p>

<p lang="zh-CN">按项目现有流程重新生成并运行相关测试，检查预期改动是否保留，以及最终 diff 是否符合项目约定。如果重新生成覆盖了改动，就定位原始修改落在哪个文件，再补充一条具体的编辑规则，用同类任务复查。保留两轮的任务说明、补丁、测试结果和人工修正次数，供团队判断当前工作流的维护成本。</p>

<p lang="en">Regenerate the outputs and run the relevant tests using the project’s existing workflow. Check that the intended change survives and that the final diff follows repository conventions. If regeneration overwrites the change, locate the original edit, add a specific editing rule, and repeat the check with a similar task. Keep the task descriptions, patches, test results, and counts of manual corrections so the team can assess the maintenance cost of its current workflow.</p>
