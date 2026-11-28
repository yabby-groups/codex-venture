---
category: "open-source"
summaryEn: "Git 2.56.0 adds git add --resolved, which stages only paths still marked as unmerged in the index and checks their regular files for leftover conflict markers first."
summaryZh: "Git 2.56.0 新增 git add --resolved，只暂存索引中仍处于未合并状态的路径，并在暂存前检查这些路径中的常规文件是否残留冲突标记。"
tags: ["git", "merge-conflicts", "coding-agents"]
titleEn: "Git 2.56 can stage conflict resolutions without picking up unrelated edits"
titleZh: "Git 2.56 可单独暂存合并冲突的处理结果"
blocks: [{"items": [{"en": "Ask the coding agent to resolve the conflicts in the working tree and leave staging to you.", "zh": "让编码 Agent 在工作区处理冲突，把暂存这一步留给自己。"}, {"en": "Run `git add --resolved`. If Git reports leftover conflict markers, review the listed files and retry after fixing them.", "zh": "运行 `git add --resolved`。如果 Git 报告残留的冲突标记，检查列出的文件，修正后重试。"}, {"en": "Use `git status --short` to check which changes are staged, then use `git diff --cached` to review what would go into the merge commit. The marker check can catch leftover markers. Whether the resolution preserves the intended behavior still takes human review.", "zh": "用 `git status --short` 核对暂存范围，再用 `git diff --cached` 审阅即将进入合并提交的改动。标记检查能发现残留标记，合并结果是否符合预期仍需人工判断。"}], "kind": "steps", "title": {"en": "Review a merge after an agent resolves conflicts", "zh": "Agent 处理冲突后的核对步骤"}}]
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T19:15:37+08:00"
sources: [{"title": "Highlights from Git 2.56", "url": "https://github.blog/open-source/git/highlights-from-git-2-56"}]
---
<p lang="zh-CN">一次合并可能只在一个文件上产生冲突，工作区里却还留着你为另一项任务做的修改。让编码 Agent 修完冲突后，可以用 Git 2.56.0 新增的 <code>git add --resolved</code> 暂存冲突处理结果，让原本未暂存的无关改动继续留在工作区。Elijah Newren 在 2026 年 9 月 28 日的 <a href="https://github.blog/open-source/git/highlights-from-git-2-56">GitHub 版本解读</a>中用两个文件演示了这一点。</p>

<p lang="en">A merge can conflict in one file while edits for another task are still sitting in your working tree. After a coding agent resolves the conflict, Git 2.56.0’s new <code>git add --resolved</code> command can stage the resolution while leaving those unrelated edits unstaged. Elijah Newren demonstrated this with two files in <a href="https://github.blog/open-source/git/highlights-from-git-2-56">GitHub’s September 28, 2026 release overview</a>.</p>

<p lang="zh-CN">暂存范围由 Git 索引决定。命令只处理索引中仍处于未合并状态的路径，并在暂存前扫描其中的常规文件。只要发现残留的冲突标记，Git 就会列出受影响的路径，并在写入索引前停止。</p>

<p lang="en">The Git index determines the staging scope. The command considers only paths that are still unmerged in the index and scans regular files among them before staging. If Git finds any leftover conflict markers, it lists the affected paths and stops before writing to the index.</p>
