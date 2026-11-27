---
category: "models"
summaryEn: "Estimate VRAM for concurrent 32K sequences by adding KV cache and runtime overhead to the model weights, then check peak usage under your target workload."
summaryZh: "把并发 32K 序列的 KV 缓存、运行时开销和模型权重加在一起做容量初筛，再用目标负载验证峰值显存。"
tags: ["vram", "kv-cache", "llm-inference"]
titleEn: "Estimate VRAM for concurrent 32K requests on a 70B model"
titleZh: "70B 模型跑多路 32K 上下文，需要多少显存？"
blocks: [{"kind": "notice", "text": {"en": "The 10 GiB and 160 GiB figures cover KV cache only. Add weight memory and runtime overhead in the same units before comparing the total with GPU capacity.", "zh": "10 GiB 和 160 GiB 都是 KV 缓存的预算。对照显卡容量前，把权重和运行时开销换算为相同单位后再相加。"}, "title": {"en": "Keep the units consistent", "zh": "统一容量单位"}}]
type: "tutorials"
version: "70B GQA example with BF16 KV cache, 2026-11-27"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T04:01:06+08:00"
sources: [{"title": "How to Stop Guessing GPU Size: Checking VRAM & Memory Bandwidth Before Provisioning", "url": "https://dev.to/hydenring/how-to-stop-guessing-gpu-size-checking-vram-memory-bandwidth-before-provisioning-3lmg"}]
---
<p lang="zh-CN">给 70B 模型选显卡前，先定下每路序列的最大长度和同时处理的路数。Hydenring 的容量估算文章给出一个 GQA 算例。在 80 层、8 个 KV 头、头维度 128、BF16 缓存的配置下，一路满长 32,768 token 的序列需要 10 GiB KV 缓存，16 路需要 160 GiB。<a href="https://dev.to/hydenring/how-to-stop-guessing-gpu-size-checking-vram-memory-bandwidth-before-provisioning-3lmg">Hydenring 原文</a></p>

<p lang="en">Before choosing a GPU for a 70B model, set the maximum length of each sequence and how many sequences you want to serve at once. Hydenring’s sizing guide gives a grouped-query attention example with 80 layers, eight KV heads, a head dimension of 128, and a BF16 cache. One full 32,768-token sequence needs 10 GiB of KV cache, and 16 such sequences need 160 GiB. <a href="https://dev.to/hydenring/how-to-stop-guessing-gpu-size-checking-vram-memory-bandwidth-before-provisioning-3lmg">Hydenring’s guide</a></p>

<p lang="zh-CN">复算时，从目标模型配置里找出层数、KV 头数和头维度，再从推理配置确认缓存精度。每 token 的缓存字节数等于 2 × 层数 × KV 头数 × 头维度 × 每元素字节数。开头的 2 计入 key 和 value。代入算例得到 327,680 字节/token，再乘以 32,768 和并发路数，最后除以 2 的 30 次方换算成 GiB。这里假设每路序列都达到预算长度。</p>

<p lang="en">To repeat the calculation, read the layer count, KV head count, and head dimension from the target model’s configuration, then confirm the cache precision in the inference configuration. KV bytes per token equal 2 × layers × KV heads × head dimension × bytes per element. The leading 2 accounts for keys and values. The example works out to 327,680 bytes per token. Multiply by 32,768 and by the number of concurrent sequences, then divide by 2 to the power of 30 to get GiB. This assumes every sequence reaches the budgeted length.</p>

<p lang="zh-CN">权重可以先按参数量乘以每参数字节数粗估。70B 权重按 BF16 的每参数 2 字节计算，约为 140 GB，即约 130.4 GiB。加上单路满长序列的缓存后约为 140.4 GiB，随后还要计入运行时开销。若换了权重量化方式，按实际配置分别更新权重与缓存的精度。上述数字是按原文配置复算的容量预算。选定推理框架后，用目标上下文和并发负载测峰值显存，再确认可用容量。</p>

<p lang="en">For a first-pass weight estimate, multiply the parameter count by the bytes per parameter. At two bytes per BF16 parameter, 70B weights take about 140 GB, or 130.4 GiB. Adding the cache for one full-length sequence brings the estimate to about 140.4 GiB before runtime overhead. If you change weight quantization, update the weight and cache precisions according to their respective settings. These figures are capacity estimates calculated from the source configuration. Once you’ve chosen an inference engine, measure peak VRAM at your target context length and concurrency to confirm the fit.</p>
