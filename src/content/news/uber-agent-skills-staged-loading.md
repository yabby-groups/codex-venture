---
category: "agents"
summaryEn: "Uber engineers describe how agents choose from a catalog of more than 5,000 skills by reading short descriptions first, then loading instructions and supporting files as needed."
summaryZh: "Uber 工程团队介绍了代理如何从 5,000 多项技能中选取所需流程，先读简述，再按执行需要加载指令和辅助文件。"
tags: ["agent-skills", "context-management", "uber"]
titleEn: "How Uber’s agents load instructions from a catalog of more than 5,000 skills"
titleZh: "Uber 的代理如何从 5,000 多项技能中按需读取指令"
type: "insights"
version: "Uber engineering account, November 23, 2026"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:43+08:00"
sources: [{"title": "How Uber Evals 1 Million Agent Skill Invocations a Month", "url": "https://www.uber.com/in/en/blog/optimizing-ubers-agent-skills"}]
---
<p lang="zh-CN">Uber 的共享代理技能目录从 2025 年 10 月的 1 项技能增至一年后的 5,000 多项。Andrew Mager、Jason Varbedain 和 Uday Kiran Medisetty 在 2026 年 11 月 23 日的工程文章中回顾了这段增长，并报告代理在一个月内调用技能超过 100 万次。目录变大后，代理需要知道有哪些流程可用，同时控制运行时要读入的指令量。</p>

<p lang="en">Uber’s shared agent skill catalog grew from one skill in October 2025 to more than 5,000 a year later. Andrew Mager, Jason Varbedain, and Uday Kiran Medisetty described that growth in a November 23, 2026 engineering post and reported more than one million skill invocations in a single month. As the catalog grows, agents need a way to discover available workflows while limiting how many instructions they read at runtime.</p>

<p lang="zh-CN">作者把每项技能组织成一个目录，用 SKILL.md 封装一项工作流程，例如创建拉取请求或按手册处理故障。代理先根据名称和简述判断技能是否适用。选中技能后，再读取正文中的操作说明。脚本和参考文件由具体步骤按需读取。这样，目录可以保留详细流程，代理在选择时只需读每项技能的简述。</p>

<p lang="en">The authors describe organizing each skill as a directory with a SKILL.md file that packages one workflow, such as opening a pull request or following an incident runbook. The agent uses the name and short description to decide whether a skill applies. Once selected, it reads the instructions. Individual steps load scripts and references as needed. This lets the catalog hold detailed procedures while keeping the initial selection focused on short descriptions.</p>

<p lang="zh-CN">这些数字来自 Uber 自报，分别衡量目录规模和调用次数。三阶段加载说明了代理何时读取材料。技能是否选对、任务是否完成，需要另外的评估结果来衡量。</p>

<p lang="en">Uber’s figures measure catalog size and invocation volume. The three-stage design explains when the agent loads each kind of material. Skill selection accuracy and task completion require separate evaluation results.</p>
