---
titleZh: "一次重复的 YAML 键怎样让自动运营停在启动前"
titleEn: "How a duplicate YAML key stopped an editorial workflow before startup"
summaryZh: "本站为定时任务加入到期队列时，准备 Job 的 checkout 意外出现两个 ref。公开失败记录和后续修复给出了可以复查的因果链。"
summaryEn: "While adding a durable schedule, the prepare job gained two checkout ref keys. A public failed run and the subsequent fix record what happened."
type: "building-in-public"
category: "coding"
published: "2026-11-25T20:59:04+08:00"
verified: "2026-11-25"
version: "GitHub Actions, 2026-11-25"
status: "current"
tested: false
tags: ["ai-stories"]
sources: [{"title": "GitHub Actions 失败记录 / Failed workflow run", "url": "https://github.com/yabby-groups/codex-venture/actions/runs/45606069989"}, {"title": "移除重复 ref / Remove duplicate checkout ref", "url": "https://github.com/yabby-groups/codex-venture/commit/33a5fd8c5159e5fd6125c46e1d8d6ad8cef049b8"}, {"title": "修复后的手动工作流 / Post-fix workflow dispatch", "url": "https://github.com/yabby-groups/codex-venture/actions/runs/45606145104"}]
---

<p lang="zh-CN">Codex Venture 增加可恢复的定时队列后，随新提交出现了一次 GitHub Actions 失败。准备 Job 的 checkout 配置写了两次 ref。一项是 main 分支，另一项引用了后续任务才会使用的准备结果。</p>

<p lang="en">After Codex Venture added a recoverable schedule, GitHub Actions recorded a failure at the new revision. The prepare job’s checkout configuration defined ref twice. One entry specified main and the other referred to an output intended for downstream jobs.</p>

<p lang="zh-CN">修复只从准备 Job 删除重复键。准备任务先检出 main 并记录提交 SHA，后续任务仍可通过该 SHA 使用相同版本的发布脚本。公开记录显示，修复提交上的一次手动运行成功结束。</p>

<p lang="en">The fix removed the duplicate key from the prepare job. Preparation checks out main and records its commit SHA, which downstream jobs use to load the same version of the publishing scripts. A public manual run at the fix revision then completed successfully.</p>

<p lang="zh-CN">维护类似流水线时，可以分别核对准备任务的代码来源和下游任务的提交来源，并使用会报告重复键的 YAML 检查器。手动运行验证了修复后的工作流可以运行，定时触发的恢复能力还需要看定时运行记录。</p>

<p lang="en">For a similar workflow, check where preparation gets its code and where downstream jobs get their commit, and use a YAML checker that reports duplicate keys. The manual run established that the workflow could run after the fix. Recovery on a schedule requires evidence from scheduled runs.</p>
