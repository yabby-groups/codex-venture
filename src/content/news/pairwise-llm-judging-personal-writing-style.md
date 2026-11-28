---
category: "models"
summaryEn: "A NeurIPS workshop study found that model judges were more consistent and performed better when comparing drafts in pairs than when scoring them individually. Editors can use the format to evaluate usefulness and tone separately."
summaryZh: "一项 NeurIPS 工作坊研究发现，让模型在两份稿件间做选择，比逐稿打分更稳定、评审表现也更好。编辑可用这种方式分别判断内容是否有用、语气是否贴合。"
tags: ["llm-evaluation", "writing", "personalization"]
titleEn: "Choosing the draft that sounds more like you? Ask AI to compare the two"
titleZh: "让 AI 选出更像你的一稿，可以先试两两比较"
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T13:15:58+08:00"
sources: [{"title": "Evaluating the Evaluators: Investigating LLM Judges for Personalized Writing Style Assessment", "url": "https://machinelearning.apple.com/research/evaluating-evaluators-llm-judges"}]
---
<p lang="zh-CN">同一封邮件有两份草稿时，可以让模型直接判断哪份更贴近你指定的语气。Natalie Mackraz、Andrew Silva 等人在苹果研究网站刊载的一篇 NeurIPS 2026 工作坊论文中，用四个模型生成了三类长文任务的回答，再把模型的判断与人工标注对照。在这些任务中，两两比较比逐稿独立打分更稳定，评审表现也更好。</p>

<p lang="en">When you have two drafts of the same email, you can ask a model which one better matches your preferred tone. In a NeurIPS 2026 workshop paper posted on Apple’s research site, Natalie Mackraz, Andrew Silva, and colleagues used four models to generate responses for three long-form writing tasks, then compared model judgments with human labels. In those tasks, pairwise comparisons were more consistent and performed better than scoring each draft independently.</p>

<p lang="zh-CN">评审效果随写作任务和评审目标而变。研究分别考察了整体有用性与个人风格匹配，发现评审质量和 MMLU 衡量的通用能力仅呈弱相关，皮尔逊相关系数不超过 0.2。编辑可以据此把审稿拆成两个问题：哪稿更能完成沟通任务，哪稿更符合指定语气。再用几组自己已经选过的草稿，检查模型是否和自己的判断一致。</p>

<p lang="en">Judge performance varied by writing task and evaluation goal. The researchers examined general helpfulness and style matching separately, and judge quality correlated only weakly with general ability as measured by MMLU, with a Pearson correlation coefficient of at most 0.2. Editors can turn that distinction into two review questions. Which draft better serves the purpose of the message? Which better fits the requested tone? A few draft pairs you’ve already judged can help you check whether the model agrees with your choices.</p>
