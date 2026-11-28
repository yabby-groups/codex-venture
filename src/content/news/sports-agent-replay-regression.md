---
category: "agents"
summaryEn: "Sports Agent turns recurring errors into cases it can replay before accepting a prompt or skill change, including when it removes rules."
summaryZh: "Sports Agent 把反复出现的错答变成可回放用例，增删提示词或 Skill 里的规则都有了验收依据。"
tags: ["sql", "regression-testing", "agent-evaluation"]
titleEn: "Before changing a SQL agent’s rules, replay the questions it got wrong"
titleZh: "给 SQL 助手改规则前，先重跑它答错的问题"
editorial: {"score": 75, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:24:29+08:00"
sources: [{"title": "Sports Agent: A Self-Evolving System for Conversational Data Analytics", "url": "https://arxiv.org/abs/2611.33700"}]
---
<p lang="zh-CN">Sports Agent 遇到反复出现的错答，会把它归结为一项范围明确的提示词或 Skill 改动，再通过独立审查、执行回放和回归测试来验收。Chao Chen 等人于 11 月 25 日提交的预印本描述了这套体育数据问答系统。它的反馈引擎既核查回答中的事实，也检查从问题到答案的执行轨迹。</p>

<p lang="en">When Sports Agent encounters a recurring error, it turns that failure into a narrowly scoped prompt or skill change, then checks the change through independent review, execution replay, and regression testing. Chao Chen and colleagues describe the sports analytics system in a preprint submitted on November 25. Its feedback engine checks both the factual claims in an answer and the execution trace that led to it.</p>

<p lang="zh-CN">维护 SQL 助手时，可以把原问题、查询轨迹和需要核对的事实放进同一个回归用例。这样，重跑时既能看用户收到的答案是否正确，也能查问题出在哪一步。论文还给删减规则设了性能容忍度检查，避免配置变短的同时，问答表现跌出可接受范围。这套流程来自作者的体育结构化数据问答系统。</p>

<p lang="en">For a SQL assistant, a regression case can bundle the original question, the query trace, and the facts the answer needs to get right. A replay can then show both whether the user got a correct answer and where the run went wrong. The paper also describes a performance tolerance check for simplifications, so a shorter configuration still has to meet an acceptable standard. The workflow comes from the authors’ question-answering system for structured sports data.</p>
