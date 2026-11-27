---
category: "open-source"
summaryEn: "vLLM now sizes its KV cache from GPU memory available after warmup. Upgrading an existing deployment also means checking for a retired runner flag that prevents startup and a default block size that changes from 16 to 64."
summaryZh: "vLLM 改用预热后剩余的显存确定 KV 缓存大小。现有服务升级时，还要检查会导致启动失败的旧 runner 开关，以及从 16 改为 64 的默认块大小。"
tags: ["vllm", "inference", "kv-cache"]
titleEn: "vLLM v0.34.0 sizes the KV cache after warmup and removes the old GPU runner"
titleZh: "vLLM v0.34.0 按预热后剩余显存分配 KV 缓存，并移除旧 GPU Runner"
blocks: [{"kind": "notice", "text": {"en": "The release notes also require huggingface_hub 2.0.0 or later and say that ROCm 7.2 images have been removed.", "zh": "发布说明还要求 huggingface_hub 2.0.0 或更高版本，并注明已移除 ROCm 7.2 镜像。"}, "title": {"en": "Dependency and image changes", "zh": "依赖与镜像变更"}}]
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T07:01:26+08:00"
sources: [{"title": "v0.34.0", "url": "https://github.com/vllm-project/vllm/releases/tag/v0.34.0"}]
---
<p lang="zh-CN">vLLM 在 11 月 16 日发布 v0.34.0，默认启用可扩展 KV 缓存，按模型预热后实际剩余的显存确定缓存大小。维护现有推理服务时，可以先检查启动配置里是否显式设置了 gpu_memory_utilization。官方发布说明建议多数部署移除这项设置，交由新版默认机制确定缓存大小。</p>

<p lang="en">vLLM released v0.34.0 on November 16 with extensible KV caching enabled by default. It sizes the cache using the GPU memory still available after model warmup. When upgrading an existing inference service, check whether its launch configuration explicitly sets gpu_memory_utilization. The release notes recommend removing that setting in most deployments and letting the new default size the cache.</p>

<p lang="zh-CN">旧 GPU runner 的开关会直接影响启动。新版只保留 Model Runner V2，继续设置 VLLM_USE_V2_MODEL_RUNNER=0 会导致启动失败。使用 V1 logits processor 的部署也需要迁移到发布说明列出的 vllm.v1.worker.gpu.sample.logits_processor 路径。</p>

<p lang="en">The old GPU runner flag can prevent startup. Model Runner V2 is now the only GPU runner, and leaving VLLM_USE_V2_MODEL_RUNNER=0 set causes startup to fail. Deployments using V1 logits processors also need to migrate to the vllm.v1.worker.gpu.sample.logits_processor path listed in the release notes.</p>

<p lang="zh-CN">此次升级还把默认块大小从 16 改为 64。需要沿用旧块大小的部署可显式传入 --block-size 16。ROCm 的 paged attention 仍使用 16。<a href="https://github.com/vllm-project/vllm/releases/tag/v0.34.0">官方发布说明</a></p>

<p lang="en">The default block size also changes from 16 to 64. Deployments that need the previous size can explicitly pass --block-size 16. ROCm paged attention still uses 16. <a href="https://github.com/vllm-project/vllm/releases/tag/v0.34.0">Official release notes</a></p>
