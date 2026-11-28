---
category: "models"
summaryEn: "PersonaFactory’s authors report that controlling style through separate attributes preserved user intent better than free-text personas at comparable style fidelity. That matters when several rewrites need to test the same assistant behavior."
summaryZh: "PersonaFactory 作者报告，在风格还原程度相近时，按属性控制改写更能保留用户原意。用不同问法测试同一个助手行为时，原用例的验收条件可以用来复核改写。"
tags: ["synthetic-data", "evaluation", "prompt-augmentation"]
titleEn: "PersonaFactory varies how users ask while preserving what they want"
titleZh: "PersonaFactory 用分项控制改写用户问法，尽量保留原意"
editorial: {"score": 78, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:37:18+08:00"
sources: [{"title": "PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona Bank", "url": "https://arxiv.org/abs/2611.34785"}]
---
<p lang="zh-CN">把「帮我改一下收货地址」改成「我想问问怎么改收货地址」，措辞更委婉了，任务也从代办变成了问流程。Bich Ngoc Doan、Hanna Yukhymenko 和 Imanol Schlag 在 2026 年 11 月 25 日提交的 PersonaFactory 预印本中报告，在风格还原程度相近时，用结构化人物属性逐项控制改写，比用自由文本描述人物更能保留原提问的意图。</p>

<p lang="en">Rewriting “Please change my delivery address” as “How do I change my delivery address?” changes what the customer wants the assistant to do. In the PersonaFactory preprint submitted on November 25, 2026, Bich Ngoc Doan, Hanna Yukhymenko, and Imanol Schlag report that rewrites guided by structured persona attributes preserved the original intent better than those guided by free-text persona descriptions at comparable levels of style fidelity.</p>

<p lang="zh-CN">作者用大语言模型评审和启发式指标评估改写效果，并报告专家对对话的原意保留、表达自然度和多语言真实性给出了正面评价。用合成提问扩充客服测试集时，可以每次只改一个维度，比如详略，再用原用例的验收条件复核。如果原用例要求助手代办地址变更，一条只询问操作步骤的改写就应该另立用例。</p>

<p lang="en">The authors assessed the rewrites with an LLM judge and heuristic metrics. They also report that human experts rated the conversations favorably for intent preservation, naturalness, and multilingual authenticity. When expanding a customer support test set with synthetic prompts, vary one dimension at a time, such as how much detail the customer gives, and check each rewrite against the original acceptance criteria. If the original case asks the assistant to change the address, a rewrite asking for instructions belongs in a separate test case.</p>
