---
category: "models"
summaryEn: "SEPO selects a pool of system prompts and samples one for each response. In the authors’ tests, model judges gave the outputs higher novelty and diversity scores, but lower average quality scores."
summaryZh: "SEPO 从筛选过的系统提示词组中为每次生成抽取一条。作者的实验中，模型评审给出的新颖性和多样性得分上升，平均质量得分下降。"
tags: ["creative-generation", "system-prompts", "llm-evaluation"]
titleEn: "SEPO Gets More Varied Ideas From One Model by Rotating System Prompts"
titleZh: "SEPO 轮换系统提示词，让同一个模型写出更多样的构思"
editorial: {"score": 82, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:45:54+08:00"
sources: [{"title": "One Model, Many Modes: Evolving System Prompt Ensembles for Creative Generation", "url": "https://arxiv.org/abs/2611.34760"}]
---
<p lang="zh-CN">同一份创作简报反复交给同一个模型，收到的点子可能还是围绕同一种构思。11 月 26 日公布的 arXiv 预印本提出 SEPO，一种无需重新训练模型的方法。研究团队先迭代系统提示词，在满足质量约束的前提下筛出生成表现差异较大的提示词，再在每次生成时从这组提示词中等概率抽取一条。<a href="https://arxiv.org/abs/2611.34760">arXiv 预印本</a></p>

<p lang="en">Give the same model the same creative brief repeatedly and its ideas may still follow the same pattern. An arXiv preprint announced on November 26 proposes SEPO, a method that requires no model retraining. The researchers refine a pool of system prompts, select prompts that produce distinct responses while meeting a quality constraint, and then pick one uniformly at random for each generation. <a href="https://arxiv.org/abs/2611.34760">arXiv preprint</a></p>

<p lang="zh-CN">作者在四项创作任务和三个开放权重模型上测试了这一方法。按质量、多样性和新颖性的调和平均分，SEPO 在 12 种组合中有 8 种排名第一。与直接从基础模型采样相比，模型评审给出的平均多样性从 1.92 升至 3.43，新颖性从 1.00 升至 3.34，质量则从 3.72 降至 3.30，均为五分制。这些结果反映的是所测任务和模型上的权衡。维护共用提示词库的创作团队可以用同一份简报筛选提示词，检查构思是否真的不同，以及输出是否仍达到交稿标准。</p>

<p lang="en">The authors tested SEPO across four creative tasks and three open-weight models. It ranked first in 8 of 12 settings on the harmonic mean of quality, diversity, and novelty. Compared with direct sampling from the base models, average model-judged diversity rose from 1.92 to 3.43 and novelty from 1.00 to 3.34, while quality fell from 3.72 to 3.30, all on a five-point scale. The trade-off reflects the tasks and models tested. Creative teams with a shared prompt library can use a single brief to check whether different prompts produce genuinely different ideas and whether the results still meet their editorial standards.</p>
