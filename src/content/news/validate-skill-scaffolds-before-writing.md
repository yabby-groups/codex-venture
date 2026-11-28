---
category: "coding"
summaryEn: "Ankita AI’s scaffolder validates skill inputs before writing files and generates an offline fixture with an expected result for review."
summaryZh: "Ankita AI 的脚手架在创建目录前校验技能输入，并生成带预期结果的离线样例，供评审时检查。"
tags: ["ankita-ai", "skills", "scaffolding", "offline-fixtures"]
titleEn: "Validating a skill scaffold before writing its files"
titleZh: "在写入技能文件前校验脚手架输入"
blocks: [{"items": [{"en": "Before writing, validate the name and description against the host parser and check the requested permissions against the host’s supported list.", "zh": "写入前，按宿主解析器的规则校验名称和描述，并核对申请的权限是否在宿主支持的列表中。"}, {"en": "Generate the skill definition and permission manifest together. Include an offline fixture with a sample input and its expected output.", "zh": "同时生成技能定义和权限清单，并附上包含示例输入与预期输出的离线 fixture。"}, {"en": "Review the generated permission declaration and check the offline fixture. If generation fails midway, roll back the partial folder.", "zh": "审阅生成的权限声明并检查离线 fixture。如果生成中途失败，回滚未完成的目录。"}], "kind": "workflow", "title": {"en": "Review checklist for a skill scaffolder", "zh": "技能脚手架评审清单"}}]
type: "workflows"
version: "Ankita AI skill scaffolder documented 2026-11-26"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 73, "tier": "standard", "audience": "core"}
published: "2026-11-28T08:04:15+08:00"
sources: [{"title": "How I built a skill scaffolder for my desktop AI companion: 3 questions, 20 tests, and a registry two installers can't corrupt", "url": "https://dev.to/krish_verma_77e28d3fd63ca/how-i-built-a-skill-scaffolder-for-my-desktop-ai-companion-3-questions-20-tests-and-a-registry-40m9"}]
---
<p lang="zh-CN">Krish Verma 为桌面助手 Ankita AI 写技能时遇到过一种难排查的失败：技能目录已经装好，宿主却没有加载它。他在脚手架中把名称、权限和示例输入的校验提前到建目录之前。维护自建助手的团队可以用同样的顺序检查生成器，把用户填的字段与宿主实际读取的格式对应起来。<a href="https://dev.to/krish_verma_77e28d3fd63ca/how-i-built-a-skill-scaffolder-for-my-desktop-ai-companion-3-questions-20-tests-and-a-registry-40m9">Krish Verma 的原文</a></p>

<p lang="en">While writing skills for the Ankita AI desktop assistant, Krish Verma ran into a failure that was hard to diagnose. The skill folder could be installed and still fail to load. His scaffolder checks the name, permissions, and sample input before creating the folder. Teams maintaining their own assistants can use that order to check that the values users enter match what the host expects. <a href="https://dev.to/krish_verma_77e28d3fd63ca/how-i-built-a-skill-scaffolder-for-my-desktop-ai-companion-3-questions-20-tests-and-a-registry-40m9">Krish Verma’s original write-up</a></p>

<p lang="zh-CN">在 Verma 描述的实现里，名称只能使用小写字母、数字和连字符，权限声明从 files、network、shell、browser 四类中选择。示例输入会用作技能描述，因此长度须在 1 至 200 个字符之间。生成成功后，技能目录用 SKILL.md 保存技能定义，用 plugin.json 声明权限。离线 fixture 将输入和预期输出配成一对，给评审人一个具体的检查样例。</p>

<p lang="en">In the implementation Verma describes, names use lowercase letters, digits, and hyphens. The supported permission declarations are files, network, shell, and browser. The sample input also serves as the skill description, so it must be 1 to 200 characters long. The generated folder holds the skill definition in SKILL.md and declares its permissions in plugin.json. An offline fixture pairs an input with its expected output, giving reviewers a concrete case to check.</p>

<p lang="zh-CN">迁移这套做法时，校验规则应取自目标宿主的加载器。权限枚举、描述长度和清单文件名是 Ankita AI 的约定。本文依据 Verma 对脚手架的说明，未运行生成器或离线样例。</p>

<p lang="en">When adapting the workflow, derive the validation rules from the target host’s loader. The permission list, description limit, and manifest filename are Ankita AI conventions. This article draws on Verma’s description of the scaffolder. We did not run the generator or the offline fixture.</p>
