---
category: "open-source"
summaryEn: "Pascal Editor uses building scans as references for editable elements and documents MCP access to the same scene. A single wall gives teams a concrete starting point for evaluating agent edits and designer review."
summaryZh: "Pascal Editor 可将建筑扫描用作可编辑构件的建模参考，项目文档也说明了代理如何通过 MCP 访问同一场景。团队可以从一面墙入手，评估代理编辑与设计师审阅之间的交接。"
tags: ["pascal-editor", "bim", "scan-to-bim", "mcp"]
titleEn: "Pascal Editor turns building scans into references for editable models"
titleZh: "Pascal Editor 用建筑扫描作参考，在浏览器里建立可编辑构件"
type: "open-source"
version: "Official repository documentation reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
project: "e1ae8aa0ded84424cccfdbf3960aa3e60313235aa03b03a40c8a3a5e27299cf2"
editorial: {"score": 61, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T11:04:08+08:00"
sources: [{"title": "pascalorg/editor", "url": "https://github.com/pascalorg/editor"}]
---
<p lang="zh-CN">拿到一份建筑扫描后，可以在 Pascal Editor 的浏览器场景中把它放作参考层，再沿着扫描建立可编辑的墙体、楼板和洞口。Pascal Group 的 README 将这条路径用于扫描转 BIM。要评估它是否适合自己的项目，可以先取一个小房间，核对建出的墙体和洞口是否符合设计意图。</p>

<p lang="en">With a building scan in hand, you can bring it into a Pascal Editor browser scene as a reference layer, then model editable walls, slabs, and openings against it. Pascal Group’s README describes this as a scan-to-BIM workflow. A single room is enough for an initial evaluation of whether the resulting walls and openings match your design intent.</p>

<p lang="zh-CN">对于想把后续修改交给代理的团队，README 还说明代理可以通过 MCP 读取、编辑、校验和保存同一场景。评估交接时，可以把范围限定在一面墙，检查代理能否定位已有构件，以及设计师能否在浏览器中核对保存后的结果。构件定位、修改如何反映到浏览器、撤销和变更记录都需要在实际环境中确认。<a href="https://github.com/pascalorg/editor">Pascal Editor 官方仓库</a></p>

<p lang="en">For teams that want an agent to make follow-up edits, the README also describes MCP access for reading, editing, validating, and saving the same scene. To evaluate that handoff, start with one wall and check whether the agent can target the existing element and the designer can review the saved result in the browser. Element targeting, how edits appear in the browser, undo, and change history all need verification in the working environment. <a href="https://github.com/pascalorg/editor">Official Pascal Editor repository</a></p>

<p lang="zh-CN">资料核对日期为 2026 年 11 月 28 日。Pascal Editor 代码采用 MIT 许可证。本文所述能力依据项目 README，墙体编辑和浏览器审阅的交接流程待实测。</p>

<p lang="en">Documentation reviewed November 28, 2026. Pascal Editor’s code is MIT-licensed. The capabilities described here come from the project README. The handoff from wall edit to browser review still needs hands-on verification.</p>
