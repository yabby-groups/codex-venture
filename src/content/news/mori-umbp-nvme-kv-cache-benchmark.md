---
category: "coding"
summaryEn: "AMD and Embedded LLM report throughput within 1% of an equally sized DRAM pool for Kimi-K3 on MI355X. The benchmark gives inference teams a reason to test NVMe when their DRAM pool evicts long prefixes before sessions return."
summaryZh: "AMD 与 Embedded LLM 报告，在 MI355X 的 Kimi-K3 测试中，NVMe 与等容量 DRAM 缓存池的吞吐差距在 1% 以内。如果长前缀常在会话恢复前被淘汰，可以把 NVMe 纳入容量测试。"
tags: ["vllm", "kv-cache", "nvme", "amd"]
titleEn: "MoRI’s NVMe KV cache comes within 1% of DRAM throughput in Kimi-K3 tests"
titleZh: "MoRI 用 NVMe 存 KV 缓存，Kimi-K3 测试吞吐与 DRAM 相差不到 1%？"
editorial: {"score": 79, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T21:33:12+08:00"
sources: [{"title": "Skip the DRAM Tier: MoRI UMBP Runs the Agentic KV Cache on NVMe", "url": "https://news.ycombinator.com/item?id=50623833"}, {"title": "Targeted research", "url": "https://vllm.ai/blog/2026-11-23-skip-the-dram-tier"}]
---
<p lang="zh-CN">当多轮 Agent 反复发送长前缀时，缓存容量会影响下一轮能否复用前缀的计算结果。AMD 与 Embedded LLM 在 11 月 23 日发布于 vLLM 的联合报告中，把 Kimi-K3 的共享 KV 缓存池放到 NVMe。测试使用 AMD Instinct MI355X GPU 和 MoRI 的 UMBP 缓存池。两套机器上的等容量比较中，NVMe 与 DRAM 池的吞吐差距都在 1% 以内。另一项提示更长的负载也报告了 1% 以内的差距。<a href="https://vllm.ai/blog/2026-11-23-skip-the-dram-tier">vLLM 原始测试报告</a></p>

<p lang="en">When a multi-turn agent repeatedly sends a long prefix, cache capacity affects whether the next turn can reuse the work already done. In a November 23 report on the vLLM blog, AMD and Embedded LLM moved Kimi-K3’s shared KV cache pool to NVMe using AMD Instinct MI355X GPUs and MoRI UMBP. On two machines, throughput was within 1% of an equally sized DRAM pool. The authors reported a gap within 1% on another workload with longer prompts. <a href="https://vllm.ai/blog/2026-11-23-skip-the-dram-tier">Original vLLM benchmark report</a></p>

<p lang="zh-CN">NVMe 方案仍使用约 80 GB 主机 DRAM 暂存读写数据。作者报告，Kimi-K3 每小时向池中写入 2.3 至 4.6 TB 的 KV 数据，1.8 TB 的 DRAM 池在这些运行中只能保留约 23 至 47 分钟。如果生产会话经常隔这么久才回来，且缓存未命中会触发长前缀重算，就值得把 NVMe 纳入容量测试。对照时可记录会话间隔、前缀命中率和每小时写入量，再核算 SSD 耐久度，并单独测首 token 延迟和吞吐。</p>

<p lang="en">The NVMe setup still used about 80 GB of host DRAM to stage reads and writes. The authors reported that Kimi-K3 wrote 2.3 to 4.6 TB of KV data per hour, giving the 1.8 TB DRAM pool about 23 to 47 minutes of retention in those runs. NVMe is worth including in a capacity test if production sessions often return after a gap like that and a miss forces long prefixes to be recomputed. Record the time between turns, prefix cache hit rate, and hourly write volume. Check SSD endurance and measure time to first token separately from throughput.</p>
