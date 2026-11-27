---
category: "coding"
summaryEn: "Use Glance and a small Python service to build a shared family start page, then check that the kitchen tablet refreshes only when the page is visible, idle, and reachable."
summaryZh: "用 Glance 和一个小型 Python 服务搭建家庭共享首页，再验证厨房平板只在页面可见、无人操作且服务器可达时刷新。"
tags: ["glance", "python", "home-assistant", "self-hosting"]
titleEn: "Build a Glance start page that refreshes when the kitchen tablet is idle"
titleZh: "用 Glance 搭建家庭首页，让厨房平板在空闲时刷新"
blocks: [{"kind": "notice", "text": {"en": "The source is fullast.nu’s write-up of their own setup. Its November 26, 2026 excerpt leaves package versions and the local model’s role unspecified. The checks above describe expected behavior.", "zh": "资料来自 fullast.nu 对自家部署的记录。2026 年 11 月 26 日的摘录未给出软件版本或本地模型的具体职责。上文的检查项描述的是预期行为。"}, "title": {"en": "Source and scope", "zh": "来源与适用范围"}}]
type: "workflows"
version: "Glance and Python deployment described on 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T12:03:26+08:00"
sources: [{"title": "A family startpage that knows when to run the dishwasher", "url": "https://dev.to/fullast/a-family-startpage-that-knows-when-to-run-the-dishwasher-1l31"}]
---
<p lang="zh-CN">厨房平板需要定时更新家庭首页，但刷新时机取决于人是否正在看、刚刚有没有操作，以及页面能否连上服务器。fullast.nu 在自家部署中给平板启用了一套单独的刷新规则，同一个首页也能从两部手机打开。<a href="https://dev.to/fullast/a-family-startpage-that-knows-when-to-run-the-dishwasher-1l31">查看部署记录</a></p>

<p lang="en">A kitchen tablet needs to refresh the family start page periodically, but the timing depends on whether the page is visible, whether someone just interacted with it, and whether the server is reachable. In their own setup, fullast.nu enabled a separate refresh policy for the tablet while keeping the same start page available on two phones. <a href="https://dev.to/fullast/a-family-startpage-that-knows-when-to-run-the-dishwasher-1l31">Read the deployment write-up</a></p>

<h2><span lang="zh-CN">用 Glance 展示，由 Python 服务取数</span><span lang="en">Render with Glance and fetch data with a Python service</span></h2>

<p lang="zh-CN">作者用一个 YAML 文件配置 Glance，再用旁边的 Python 服务接入 Home Assistant、交通和电价 API 以及 RSS。Python 服务把数据整理成 Glance 小组件可读取的 JSON，部分内容通过 iframe 展示。采用这个分工前，可以先选一个数据源，确认服务能读取它，再检查对应小组件是否显示预期内容。</p>

<p lang="en">The author configured Glance in a single YAML file and used a companion Python service to connect to Home Assistant, transit and electricity price APIs, and RSS feeds. The service provides JSON for Glance widgets and exposes some content through iframes. Start with one feed, confirm that the service can read it, and check that its widget displays the expected content.</p>

<h2><span lang="zh-CN">为平板启用刷新并检查三个条件</span><span lang="en">Enable tablet refresh and check three conditions</span></h2>

<p lang="zh-CN">在作者的实现中，平板第一次用 <code>?autorefresh=10</code> 打开页面时，页面会把设置保存到 <code>localStorage</code>。之后每十分钟检查一次。页面可见、过去一分钟内无人操作、且对首页的 <code>HEAD</code> 请求成功时，才重新加载。</p>

<p lang="en">In the author’s implementation, opening the page on the tablet with <code>?autorefresh=10</code> saves the setting in <code>localStorage</code>. The page then checks every ten minutes. It reloads only when it is visible, nobody has interacted with it in the past minute, and a <code>HEAD</code> request to the home page succeeds.</p>

<ul><li><span lang="zh-CN">页面可见、平板闲置且首页可达时，到下一次检查应重新加载。</span><span lang="en">With the page visible, the tablet idle, and the home page reachable, expect a reload at the next check.</span></li><li><span lang="zh-CN">切到后台，或在检查前一分钟内操作页面，应跳过该次刷新。</span><span lang="en">Put the page in the background or interact with it within a minute of the check. Expect that refresh to be skipped.</span></li><li><span lang="zh-CN">让首页暂时不可达。探测失败时应保留当前页面。若连通后仍不刷新，检查首页的 HEAD 请求是否成功。</span><span lang="en">Make the home page temporarily unreachable. Expect the current page to stay visible when the probe fails. If refresh still fails after connectivity returns, check the home page’s HEAD response.</span></li></ul>
