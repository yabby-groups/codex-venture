---
category: "coding"
summaryEn: "Give a fresh Claude Code session one SKILL.md, a read-only repository, and a one-line client request. Review missed checks and unsupported claims, then rerun the revised skill in another fresh session."
summaryZh: "给 Claude Code 的新会话一份 SKILL.md、一个只读仓库和一句客户请求。记录漏检和无依据的结论，修改技能后换新会话复跑。"
tags: ["claude-code", "skills", "qa"]
titleEn: "How to test Claude Code skills in fresh sessions"
titleZh: "用新会话验收 Claude Code 技能"
blocks: [{"kind": "notice", "text": {"en": "This workflow draws on Matias Arratibel’s account of testing eight skills he wrote for client work. The excerpt covers the session setup and two failure patterns. It does not identify the Claude Code version or provide per-skill retest results.", "zh": "本文依据 Matias Arratibel 对八个自写客户交付技能的试跑记录。摘录涵盖会话设置和两类失败，未提供 Claude Code 版本或逐项复测结果。"}, "title": {"en": "Source and scope", "zh": "资料与适用范围"}}]
type: "workflows"
version: "Claude Code SKILL.md workflow described on 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 77, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:01:09+08:00"
sources: [{"title": "I tested eight Claude Code skills on a production codebase. Here is everything that broke.", "url": "https://dev.to/kiioys/i-tested-eight-claude-code-skills-on-a-production-codebase-here-is-everything-that-broke-27bg"}]
---
<p lang="zh-CN">给客户网站做交付前检查时，Claude Code 的技能可能跑完了流程，却一个无障碍检查结果也没给出。Matias Arratibel 在生产仓库里试跑八个自写技能时就遇到了这种情况。他按静态网页写的检查去找字面上的 HTML 标签和事件属性，在使用组件库的 React 项目里没有找到预期的写法。Arratibel 随后调整了顺序，先弄清项目怎样渲染页面，再决定怎样执行检查。</p>

<p lang="en">A Claude Code skill can finish a pre-delivery review without returning any accessibility findings. Matias Arratibel ran into this while trying eight skills he wrote on a production repository. His checks looked for literal HTML tags and event attributes, but the React project used a component library and did not contain the expected patterns. Arratibel revised the instructions to establish how the project renders its pages before choosing how to run the checks.</p>

<h2><span lang="zh-CN">在新会话里做两轮验收</span><span lang="en">Run both acceptance checks in fresh sessions</span></h2>

<p lang="zh-CN">选一个团队自写的 <code>SKILL.md</code>，准备一个以只读方式提供的真实仓库，以及一句客户可能会说的请求。开启全新会话，只提供这三项。执行后请 Claude 说明交付了什么，再指出技能指令里哪些要求无法完成或缺少依据。由审查人核对产物，记下漏掉的检查和无法追溯到输入的结论。</p>

<p lang="en">Pick one <code>SKILL.md</code> your team wrote, a real repository available in read-only mode, and a one-line request a client might make. Give a fresh session only those three inputs. After the run, ask Claude what it delivered and which instructions it could not complete or substantiate. Have a reviewer check the output and record missed checks and conclusions they cannot trace to the inputs.</p>

<p lang="zh-CN">修订时，把依赖项目结构的检查放在识别实现方式之后。把需要额外信息的输出也写清楚。例如，客户没给截止日期、团队没提供每周可用工时，就把这些信息标为待确认。换一个从未看过首轮输出的新会话，用同一仓库和请求复跑。审查时对比原先漏掉的检查现在是否有可核对的结果，以及缺失信息是否被明确指出。<a href="https://dev.to/kiioys/i-tested-eight-claude-code-skills-on-a-production-codebase-here-is-everything-that-broke-27bg">Arratibel 的试跑记录</a></p>

<p lang="en">When revising the skill, put checks that depend on project structure after the step that identifies how the project is built. Specify how to handle missing inputs, too. For example, flag the deadline or weekly capacity as open questions if the client or team has not supplied them. Rerun the same request against the same repository in a session that has never seen the first output. Check whether the previously missed work now has an inspectable result and whether the output calls out the missing inputs. <a href="https://dev.to/kiioys/i-tested-eight-claude-code-skills-on-a-production-codebase-here-is-everything-that-broke-27bg">Arratibel’s test account</a></p>
