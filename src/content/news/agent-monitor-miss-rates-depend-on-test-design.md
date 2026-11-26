---
category: "agents"
summaryEn: "An arXiv case study found that the same agent monitor’s measured false-negative rate varied sharply with how the evaluation cases were generated."
summaryZh: "一项 arXiv 案例研究发现，即使监控器相同，测试用例的生成方式也会显著影响测得的漏报率。"
tags: ["agent-monitoring", "evaluation", "ai-safety"]
titleEn: "Agent monitor miss rates vary with test design, preprint finds"
titleZh: "预印本发现代理监控器的漏报率随测试设计变化"
published: "2026-11-26T23:05:04+08:00"
sources: [{"title": "Attack Policy Selection can Mislead Monitor Evaluators", "url": "https://arxiv.org/abs/2611.34934"}]
---
<p lang="zh-CN">Charlie Griffin、Oliver Makins、Asa Cooper Stickland、Alessandro Abate、Yarin Gal、Abby D’Cruz 和 Xander Davies 于 2026 年 11 月 25 日向 arXiv 提交预印本，以一个曾在生产环境使用的 OpenAI 监控器为案例。作者报告，在同一类测试用例生成方法下，仅改变优化程度，测得的漏报率就从 0.5% 到 20.8% 不等。</p>

<p lang="en">Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D’Cruz, and Xander Davies submitted an arXiv preprint on November 25, 2026, examining an OpenAI monitor formerly used in production. The authors report that changing the degree of optimization within a single test-generation method yielded measured false-negative rates from 0.5% to 20.8%.</p>

<p lang="zh-CN">对负责代理监控的团队来说，比较漏报率时需要同时看测试用例的构造方式。论文中的数字来自特定测试记录。若要用这些数字判断部署后的监控效果，还需要说明测试记录能在多大程度上代表实际运行中需要识别的行为。</p>

<p lang="en">Teams evaluating agent monitors need to account for how test cases were generated when comparing false-negative rates. The paper’s figures come from specific test transcripts. Using those figures to assess deployment performance requires evidence that the transcripts represent the behavior the monitor will need to flag in practice.</p>
