---
category: "models"
summaryEn: "A preprint comparing six small reasoning models with an exact solver found that the models sometimes chose the wrong bid even after ranking the best one first. The experiment also showed that the token budget and the timing of answer extraction affected performance."
summaryZh: "一项预印本用精确求解器对照六款小型推理模型，发现模型即使已在推理记录中把最优报价排在首位，仍可能选错。实验还显示，推理 token 预算和答案读取时机都会影响表现。"
tags: ["reasoning-models", "model-evaluation", "auction-bidding"]
titleEn: "Small Reasoning Models Can Rank the Best Bid First and Still Pick the Wrong One"
titleZh: "小型推理模型把最优报价排在首位，最终仍可能选错"
editorial: {"score": 80, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:15:44+08:00"
sources: [{"title": "Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding", "url": "https://arxiv.org/abs/2611.34068"}]
---
<p lang="zh-CN">即使推理记录已经把某个报价排在第一位，小型推理模型仍可能提交另一个报价。Mahbod Khaleti 等人于 2026 年 11 月 25 日提交的预印本，用来自 eBay 成交价和 AuctionNet 模拟广告市场的胜率曲线，测试了六款 40 亿至 140 亿参数的开放推理模型。研究者把每档报价的预估胜率直接交给模型，再用精确求解器评估模型在留出样本中的选择。</p>

<p lang="en">Even when a small reasoning model ranks a bid first in its own trace, it can still submit a different bid. In a preprint submitted on November 25, 2026, Mahbod Khaleti and colleagues tested six open reasoning models with 4 billion to 14 billion parameters. They supplied estimated win probabilities for each candidate bid, using curves derived from eBay closing prices and from the simulated AuctionNet ad market, then used an exact solver to evaluate the models’ choices on held-out auctions.</p>

<p lang="zh-CN">作者发现，模型选错时偏向金额最高的报价。这种偏向与报价在列表中的位置无关，在采样时仍然存在。在基于 eBay 数据、按自身出价支付的设置下，强制使用 768 个推理 token 时，选错报价造成的盈余损失相当于精确求解器可获得盈余的 7% 至 17%。</p>

<p lang="en">The authors found that when models chose incorrectly, they favored the highest-priced bid regardless of where it appeared in the list. The bias persisted under sampling. In the eBay-based pay-your-bid setup, with a forced budget of 768 reasoning tokens, incorrect choices cost bidders 7% to 17% of the surplus the exact solver would have earned.</p>

<p lang="zh-CN">推理预算和答案读取时机也影响结果。允许模型在 4,096 个 token 内自行结束推理后，六款模型中有五款追回了精确求解器相对无推理基线优势的 91% 至 100%。作者还发现，等推理块关闭后再读取答案，可以改善表现最弱的模型在两组测试中的结果。</p>

<p lang="en">The reasoning budget and the timing of answer extraction also affected the results. When models could stop on their own within 4,096 tokens, five of the six recovered 91% to 100% of the exact solver’s advantage over a no-reasoning baseline. The authors also found that waiting for the reasoning block to close before extracting the answer improved the weakest model’s results on both datasets.</p>

<p lang="zh-CN">对于同样能用代码算出最优选项的自动化任务，可以用求解器核对最终输出，再检查模型提交的选项是否与推理记录中的首选一致。单独改变 token 上限和答案读取时机，有助于判断问题出现在哪一步。论文中的盈余损失比例适用于研究测试的竞价条件。<a href="https://arxiv.org/abs/2611.34068">arXiv 预印本</a></p>

<p lang="en">For other automation tasks where code can compute the best option, use a solver to check the final output, then see whether the model submitted the option it ranked first. Varying the token cap and answer extraction timing separately can help pinpoint where the error occurs. The reported surplus losses apply to the auction conditions tested in the study. <a href="https://arxiv.org/abs/2611.34068">arXiv preprint</a></p>
