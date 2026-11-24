---
titleZh: "用 Codex Playwright Skill 检查表单"
titleEn: "Check a form with the Codex Playwright Skill"
summaryZh: "把一次页面验证变成带截图和可核对步骤的交付。"
summaryEn: "Turn a page check into a reproducible run with screenshots."
type: "skills"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Codex / legacy skills repository"
status: "current"
tested: false
project: "codex-playwright"
tags: ["agent-skills","codex"]
sources: [{"title":"Check a form with the Codex Playwright Skill – primary reference","url":"https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md"},{"title":"OpenAI skills repository","url":"https://github.com/openai/skills"}]
resource: {"id": "codex-playwright", "type": "skills", "name": "OpenAI Playwright Skill", "summary": ["用浏览器测试表单、记录页面行为并截图。", "Test forms in a browser, observe page behavior and capture screenshots."], "categories": [["浏览器自动化", "Browser automation"]], "site": "https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md", "repository": "https://github.com/openai/skills", "platforms": ["Codex"], "license": "Apache-2.0", "notes": ["官方仓库已弃用，文章记录历史用法。", "The upstream repository is deprecated. The guide covers legacy usage."]}
---
<p lang="zh-CN">OpenAI 技能仓库的 Playwright 技能通过终端控制浏览器。它用页面快照记录控件引用，并建议导航或明显的界面变化后重新获取快照。适合检查测试环境中的表单反馈。</p>

<p lang="en">The Playwright skill in OpenAI’s repository drives a browser from the terminal. It captures control references in page snapshots and recommends refreshing the snapshot after navigation or significant UI changes. That fits form checks in a test environment.</p>

<p lang="zh-CN">OpenAI 已将该技能仓库标记为弃用。它记录的历史安装方式是在 Codex 内调用 skill-installer 并指定 playwright，运行时需要 Node.js 和 npx。启用后可要求 Codex 打开测试页、提交虚构数据并截图。浏览器可读取页面和执行有状态的操作，应使用测试账号，该技能目录附 Apache 2.0 许可证。本文未运行该技能。</p>

<p lang="en">OpenAI has deprecated this skill repository. Its documented legacy installation used skill-installer with playwright in Codex and required Node.js and npx. Then ask Codex to open the test page, submit dummy data, and save a screenshot. The browser can read pages and perform stateful actions. Use a test account. The skill directory includes an Apache 2.0 license. We did not run this skill.</p>
