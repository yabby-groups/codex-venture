---
category: "models"
summaryEn: "A six-model preprint reports that MXFP4 gains more from Hadamard rotation than NVFP4. Its calibration-free Midmax method also improved accuracy in most tested MXFP4 configurations."
summaryZh: "一篇覆盖六个大语言模型的预印本发现，Hadamard 旋转对 MXFP4 的收益大于 NVFP4。论文提出的免校准方法 Midmax 也提高了大多数受测 MXFP4 配置的精度。"
tags: ["quantization", "inference", "mxfp4", "nvfp4"]
titleEn: "MXFP4 and NVFP4 respond differently to Hadamard rotation in six-model study"
titleZh: "六模型量化研究发现，MXFP4 比 NVFP4 更受益于 Hadamard 旋转"
published: "2026-11-25T19:50:11+08:00"
sources: [{"title": "MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques and Their Interactions", "url": "https://arxiv.org/abs/2611.32873"}]
---
<p lang="zh-CN">Natalia Frumkin、Alireza Khodamoradi、Kristof Denolf、Eric Dellinger 和 Stuart Biles 于 11 月 24 日向 arXiv 提交预印本。他们在六个大语言模型上比较了 MXFP6、MXFP4 和 NVFP4，分别调整 Hadamard 旋转粒度、训练后量化算法和分块缩放因子选择策略，观察这些设置如何共同影响推理精度。</p>

<p lang="en">Natalia Frumkin, Alireza Khodamoradi, Kristof Denolf, Eric Dellinger, and Stuart Biles submitted the preprint to arXiv on November 24. They evaluated MXFP6, MXFP4, and NVFP4 across six large language models, varying the granularity of Hadamard rotation, the post-training quantization algorithm, and the block-scale selection strategy to see how those choices interact.</p>

<p lang="zh-CN">实验中，MXFP4 从旋转和带误差校正的训练后量化中获得了明显收益，NVFP4 从旋转中获得的收益较小。作者还提出无需校准的缩放因子选择方法 Midmax，在大多数受测 MXFP4 配置中提高了精度。对准备切换 4 位推理格式的团队，这些结果表明，原有量化配方需要在目标格式上重新验证。</p>

<p lang="en">In the experiments, MXFP4 benefited substantially from rotation and error-correcting post-training quantization, while NVFP4 gained less from rotation. The authors also introduced Midmax, a calibration-free scale-selection method that improved accuracy in most of the MXFP4 configurations they tested. For teams switching 4-bit inference formats, the results point to validating the existing quantization recipe on the target format.</p>
