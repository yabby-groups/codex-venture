---
category: "coding"
summaryEn: "In a preprint testing 90 Django patches, higher reasoning effort reduced false approvals, yet every Claude 5.5 configuration accepted at least 45% of patches labeled incorrect."
summaryZh: "一项覆盖 90 个 Django 补丁的预印本发现，提高推理强度减少了误放行，但所有受测的 Claude 5.5 配置都放行了至少 45% 被判定有误的补丁。"
tags: ["claude", "code-review", "django", "swe-bench"]
titleEn: "Claude 5.5 reviewers approved at least 45% of incorrect Django patches in a study"
titleZh: "Claude 5.5 审查研究中，各配置均放行至少 45% 的错误 Django 补丁"
published: "2026-11-26T23:05:04+08:00"
sources: [{"title": "How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches", "url": "https://arxiv.org/abs/2611.33639"}]
---
<p lang="zh-CN">Zax Shen、Hanling Zhang 和 Zixu Wang 于 2026 年 11 月 25 日向 arXiv 提交预印本。他们让 Claude Opus、Sonnet 和 Haiku 5.5 分别以低、中、高三档推理强度审查同一批 90 个由代理生成的 Django 补丁。这些补丁来自 SWE-bench Verified。按更严格的 SWE-ABS 测试判定，其中 55 个补丁有误。</p>

<p lang="en">Zax Shen, Hanling Zhang, and Zixu Wang submitted their preprint to arXiv on November 25, 2026. They had Claude Opus, Sonnet, and Haiku 5.5 review the same 90 agent-written Django patches from SWE-bench Verified at low, medium, and high reasoning effort. The stricter SWE-ABS tests labeled 55 of those patches incorrect.</p>

<p lang="zh-CN">三款模型在高档的误放行率均低于低档，其中 Opus 和 Haiku 的差异得到统计支持。Opus 的中档在预设的 15 个百分点界值内达到非劣效标准，审查成本比高档低 20%。这一成本降幅小于预注册的 30% 目标。就这批 Django 补丁而言，任何一档单独用作合并关卡，都会放行至少 45% 的错误补丁。</p>

<p lang="en">All three models let fewer incorrect patches through at high effort than at low effort, with statistical support for the difference in Opus and Haiku. For Opus, medium effort met the preset noninferiority criterion with a 15-percentage-point margin and cost 20% less than high effort. The savings fell short of the preregistered 30% target. On this set of Django patches, every setting would have let at least 45% of incorrect patches through if used as the sole merge gate.</p>
