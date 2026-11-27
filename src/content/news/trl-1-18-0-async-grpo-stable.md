---
category: "open-source"
summaryEn: "TRL v1.18.0 makes AsyncGRPOTrainer stable. Background generation can overlap with training updates, and scripts that import experimental submodules need to migrate."
summaryZh: "TRL v1.18.0 将 AsyncGRPOTrainer 转为稳定功能，后台生成可以与训练更新并行。直接导入旧实验子模块的脚本需要迁移。"
tags: ["trl", "grpo", "vllm", "reinforcement-learning"]
titleEn: "TRL v1.18.0 makes AsyncGRPOTrainer stable and changes experimental imports"
titleZh: "TRL v1.18.0 稳定异步 GRPO 训练，旧实验子模块导入失效"
blocks: [{"kind": "notice", "text": {"en": "The package-level import of AsyncGRPOConfig and AsyncGRPOTrainer from trl.experimental.async_grpo still works with a FutureWarning and is slated for removal in v2.0.0. Imports from the old experimental submodules already fail in v1.18.0.", "zh": "从 trl.experimental.async_grpo 包顶层导入 AsyncGRPOConfig 和 AsyncGRPOTrainer 仍可用，但会触发 FutureWarning，计划在 v2.0.0 移除。旧实验子模块的导入在 v1.18.0 已经失效。"}, "title": {"en": "Check imports before upgrading", "zh": "升级前检查导入路径"}}]
editorial: {"score": 72, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T07:32:25+08:00"
sources: [{"title": "v1.18.0", "url": "https://github.com/huggingface/trl/releases/tag/v1.18.0"}]
---
<p lang="zh-CN">TRL 在 11 月 13 日发布的 v1.18.0 中将 AsyncGRPOTrainer 转为稳定功能。后台进程从 vLLM 服务流式接收模型生成的回答，评分后放入队列。训练循环从队列取样并更新模型，因此下一批回答的生成可以和当前批次的梯度更新重叠。</p>

<p lang="en">TRL promoted AsyncGRPOTrainer to stable in v1.18.0, released November 13. A background process streams completions from a vLLM server, scores them, and puts them on a queue. The training loop pulls samples from that queue and updates the model, so generation for the next batch can overlap with gradient updates for the current one.</p>

<p lang="zh-CN">训练器每隔 weight_sync_steps 个训练步通过 NCCL 向 vLLM 服务同步权重。这个参数控制生成端接收新权重的频率，队列中已生成的样本可能仍来自较早的权重。评估迁移时，可以一起核对 vLLM 服务和 NCCL 连接、训练循环等待样本的时间，以及采样与训练所用权重之间的滞后。<a href="https://github.com/huggingface/trl/releases/tag/v1.18.0">发布说明</a></p>

<p lang="en">The trainer syncs weights to the vLLM server over NCCL every weight_sync_steps training steps. That setting controls how often the server receives fresh weights, and samples already in the queue may have been generated with earlier weights. When evaluating a migration, check the vLLM service and NCCL connection, how long the training loop waits for samples, and how far the weights used for sampling lag behind training. <a href="https://github.com/huggingface/trl/releases/tag/v1.18.0">Release notes</a></p>

<p lang="zh-CN">迁移实验版脚本时，从 trl 导入 AsyncGRPOTrainer。直接引用内部组件的代码需要检查新路径。生成循环位于 trl.trainer.async_grpo_trainer，vLLM 客户端在 trl.generation.async_vllm_client 中，类名改为 AsyncVLLMClient。</p>

<p lang="en">When migrating scripts from the experimental version, import AsyncGRPOTrainer from trl. Code that references internal components directly needs to check the new paths. The rollout loop lives in trl.trainer.async_grpo_trainer, and the vLLM client is now named AsyncVLLMClient in trl.generation.async_vllm_client.</p>
