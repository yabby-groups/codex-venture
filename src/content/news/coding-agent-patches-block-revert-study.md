---
category: "coding"
summaryEn: "On SWE-bench Verified, about 11% of the code blocks in an agent patch could be reverted individually without failing the task tests. Most of those blocks changed behavior, giving reviewers a concrete place to start."
summaryZh: "在 SWE-bench Verified 上，Agent 补丁平均约有 11% 的代码块可单独撤回且任务测试仍通过，其中大多涉及行为变化。评审者可从这些改动入手核对需求与测试覆盖。"
tags: ["coding-agents", "swe-bench-verified", "code-review"]
titleEn: "Study reverts coding agent edits one block at a time to see what tests need"
titleZh: "编码 Agent 补丁逐块撤回后，哪些改动是任务测试所需的？"
editorial: {"score": 88, "tier": "featured", "audience": "core"}
published: "2026-11-28T17:45:22+08:00"
sources: [{"title": "How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches", "url": "https://arxiv.org/abs/2611.34875"}]
---
<p lang="zh-CN">在 11 月 26 日的 arXiv v1 公告中，研究团队用逐块撤回的方法衡量编码 Agent 补丁中的改动是否为任务测试所需。他们回放 18 个模型通过任务测试的 7,660 条 GitHub Copilot CLI 轨迹，追溯最终补丁的每个改动块，逐个撤回并重跑测试，也用同一方法检查开发者补丁。</p>

<p lang="en">In a November 26 arXiv v1 announcement, the authors measured which edits in coding agent patches were needed to pass the task tests. They replayed 7,660 successful GitHub Copilot CLI runs across 18 models, traced each block in the final patch, and reran the tests after reverting one block at a time. They applied the same method to developer patches.</p>

<p lang="zh-CN">额外改动的构成随基准而变。在 SWE-bench Verified 上，相比开发者补丁多出的改动主要是测试（61%）和文档（13%）。在 DeepSWE 上，代码占额外改动的 58%。在 SWE-bench Verified 上，Agent 补丁平均约有 11% 的代码块可单独撤回并保持任务测试通过，其中 89% 涉及行为变化。</p>

<p lang="en">The makeup of the extra edits varied by benchmark. On SWE-bench Verified, tests accounted for 61% of the edits beyond those in developer patches and documentation accounted for 13%. On DeepSWE, code accounted for 58% of the extra edits. On SWE-bench Verified, about 11% of the code blocks in an agent patch could be reverted individually while keeping the task tests green. Of those blocks, 89% changed behavior.</p>

<p lang="zh-CN">评审大补丁时，可以先挑出超出任务范围的行为改动，逐块暂时撤回并重跑相关测试。如果测试仍然通过，就追问该行为对应哪项需求，以及是否应补一个能区分撤回前后行为的测试。研究中的「必要」由当时运行的任务测试界定。<a href="https://arxiv.org/abs/2611.34875">论文摘要</a></p>

<p lang="en">When reviewing a large patch, start with behavior changes outside the task’s scope. Temporarily revert them one at a time and rerun the relevant tests. If the tests still pass, ask which requirement the change serves and whether a test should distinguish the two behaviors. The study defines necessity relative to the task tests it ran. <a href="https://arxiv.org/abs/2611.34875">Paper abstract</a></p>
