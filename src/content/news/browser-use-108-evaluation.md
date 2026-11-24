---
titleZh: "Browser Use 1.0.8 调整评判和无头环境授权"
titleEn: "Browser Use 1.0.8 changes judging and headless authorization"
summaryZh: "评判器复用同次运行的会话，SSH 环境也可通过另一台设备完成授权。"
summaryEn: "The judge reuses the run’s conversation, and SSH users can authenticate from another device."
published: "2026-11-24T15:01:03+08:00"
category: "agents"
tags: ["browser-use", "browser-automation"]
sources:
  - title: "browser-use 1.0.8 release notes"
    url: https://github.com/browser-use/browser-use/releases/tag/1.0.8
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 22 日（北京时间），browser-use 发布 1.0.8。评判器复用同次运行的会话，SSH 环境也可通过另一台设备完成授权。</p>

<p lang="en">browser-use published 1.0.8 on November 22 (China Standard Time). The judge reuses the run’s conversation, and SSH users can authenticate from another device.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">维护者说明，评判改成同次运行中的额外一轮，以便供应商从缓存读取已有记录。连接 CDP 时，新版会使用已经打开的页面，适合需要检查同一页面前后状态的自动化。</p>

<p lang="en">The maintainers moved judging into an additional turn of the same run so the provider can read the existing trace from cache. CDP connections attach to the open page, which helps workflows that inspect one page before and after a change.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">发布页提供安装版本 browser-use==1.0.8。缓存收益取决于供应商和实际命中情况，账单应以自己的运行记录为准。</p>

<p lang="en">The release page gives the install version browser-use==1.0.8. Savings depend on the provider and actual cache hits, so use your own runs to check billing.</p>
