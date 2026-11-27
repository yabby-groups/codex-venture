---
category: "coding"
summaryEn: "In an illustrative demonstration, researchers changed only the wording of a coding agent’s prompt and got different architectures for the same task. Their preprint proposes ways to review and document the decisions agents make along the way."
summaryZh: "一篇预印本通过示例展示，同一个任务仅改变给代码代理的提示词措辞，就可能生成不同的软件架构。作者建议在代码审查中识别并记录代理隐式做出的架构决定。"
tags: ["coding-agents", "software-architecture", "code-review", "research"]
titleEn: "How Prompt Wording Can Change a Coding Agent’s Architecture Choices"
titleZh: "提示词措辞如何改变代码代理的架构选择"
type: "insights"
version: "arXiv:2604.04990v1"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T16:03:25+08:00"
sources: [{"title": "AI Coding Agents Shape Software Architecture", "url": "https://arxiv.org/abs/2604.04990"}]
---
<p lang="zh-CN">代码代理选框架、搭建基础设施或接入外部服务时，一次实现任务就可能定下软件架构。Phongsakon Mark Konrad、Tim Lukas Adam、Riccardo Terrenzi 和 Serkan Ayvaz 在 2026 年 4 月 5 日提交的 arXiv 预印本《Architecture Without Architects》中，把这些容易藏在实现细节里的决定作为研究对象。</p>

<p lang="en">When a coding agent picks a framework, scaffolds infrastructure, or wires up an external integration, an implementation task can turn into an architecture decision. Phongsakon Mark Konrad, Tim Lukas Adam, Riccardo Terrenzi, and Serkan Ayvaz examine these easily overlooked decisions in <em>Architecture Without Architects</em>, an arXiv preprint submitted on April 5, 2026.</p>

<p lang="zh-CN">作者归纳了代理隐式做出架构选择的五种机制，并提出六种提示词与架构之间的关联模式。他们以结构化输出校验为例，认为这类基础设施需求可能随模型能力提升而减弱。相比之下，他们将工具调用编排归为模型能力提升后仍会存在的架构需求。在作者给出的示例中，同一个任务仅改变提示词措辞，就生成了结构不同的系统。</p>

<p lang="en">The authors identify five ways agents make implicit architectural choices and propose six patterns that connect prompt requirements to architecture. They suggest that the infrastructure needed to validate structured output may become less necessary as models improve, while tool-call orchestration will remain an architectural requirement. In their illustrative demonstration, changing only the prompt wording for the same task produced systems with different structures.</p>

<p lang="zh-CN">在代码审查中，可以把代理新引入的框架、基础设施和集成逐项对应到任务要求，再把团队决定保留的架构选择及理由写入架构决策记录。这是把作者提出的审查与记录建议落到代码变更上的一种做法。论文摘要给出的是示例演示。类似的架构差异在其他项目或模型中有多常见，仍需进一步验证。<a href="https://arxiv.org/abs/2604.04990">arXiv 预印本</a></p>

<p lang="en">In code review, teams can trace each new framework, infrastructure component, and integration back to a task requirement, then record the choices they keep and the reasons in an architecture decision record. That is one way to apply the authors’ proposals for review and documentation to a code change. The abstract describes an illustrative demonstration. How often similar differences arise across other projects or models remains an open question. <a href="https://arxiv.org/abs/2604.04990">arXiv preprint</a></p>
