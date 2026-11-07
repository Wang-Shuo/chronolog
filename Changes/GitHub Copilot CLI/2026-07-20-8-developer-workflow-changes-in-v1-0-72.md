---
card_id: github-copilot-cli-2026-07-20-38a47d
date: '2026-07-20'
description: 'GitHub Copilot CLI · 2026-07-20 · Developer Workflow: 8 changes in 1.0.72
  — Command approvals no longer carry over to another repository after you switch
  with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1220
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7ab7355754b0d0f03458784da86973eddd7158a14e4390c88e2aa3a68304496
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-20-38a47d
  comparison: ''
  date: '2026-07-20'
  description: 'GitHub Copilot CLI — 1.0.72: 8 Developer Workflow changes'
  evidence:
  - quote: Command approvals no longer carry over to another repository after you
      switch with /cd
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: '/worktree and /move no longer fail to create a worktree for an auto-generated
      branch name when many similarly-named branches or a leftover worktree directory
      already exist: the numeric-suffix search is no longer capped at 5 and now skips
      stale unregistered worktree directories (an explicitly supplied branch name
      still errors on a collision)'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: /worktree <task> no longer intermittently runs the kickoff task in the
      main repo instead of the new worktree
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: /worktree and /move now propagate folder trust to the new worktree before
      switching when the source is already trusted (avoiding a spurious folder-trust
      prompt in that case), /move addresses its git stash precisely so a concurrent
      stash can't misplace changes, and worktree creation skips a leftover directory
      instead of failing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Type $ at the prompt to open an interactive shell in the current session
      directory (enable it with `/settings shellShortcut on`; off by default)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: '`copilot skill list` now strips terminal control characters from skill
      names and descriptions, so a crafted skill can no longer inject ANSI escape
      sequences into the listing output.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Detect VS Code, Cursor, and Windsurf through parent processes in /terminal-setup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: '`/terminal-setup` now refuses to modify a VS Code keybindings.json that
      contains a JSON syntax error (instead of rewriting it and reporting success),
      matching its documented invalid-JSON handling.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-developer-workflow-changes-in-v1-0-72
  source_release: github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91
  source_type: github_releases
  theme: developer-workflow
  title: 8 Developer Workflow changes in v1.0.72
  type: change
related_changes:
- '[[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow
  changes in 1.16.0]]'
- '[[Changes/Claude Code/2026-07-19-claude-no-longer-runs-the-verify-and-code-review-skills-on-its-own-invoke-them-w|Claude
  no longer runs the /verify and /code-review skills on its own]]'
- '[[Changes/Claude Code/2026-07-20-2-developer-workflow-changes-in-v2-1-216|2 Developer
  Workflow changes in v2.1.216]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91]]'
source_type: github_releases
theme: developer-workflow
title: 8 Developer Workflow changes in v1.0.72
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Developer Workflow changes in v1.0.72

**GitHub Copilot CLI** · 2026-07-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.72) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|1.0.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Command approvals no longer carry over to another repository after you switch with /cd

> /worktree and /move no longer fail to create a worktree for an auto-generated branch name when many similarly-named branches or a leftover worktree directory already exist: the numeric-suffix search is no longer capped at 5 and now skips stale unregistered worktree directories (an explicitly supplied branch name still errors on a collision)

> /worktree \<task> no longer intermittently runs the kickoff task in the main repo instead of the new worktree

> /worktree and /move now propagate folder trust to the new worktree before switching when the source is already trusted (avoiding a spurious folder-trust prompt in that case), /move addresses its git stash precisely so a concurrent stash can't misplace changes, and worktree creation skips a leftover directory instead of failing

> Type $ at the prompt to open an interactive shell in the current session directory (enable it with `/settings shellShortcut on`; off by default)

> `copilot skill list` now strips terminal control characters from skill names and descriptions, so a crafted skill can no longer inject ANSI escape sequences into the listing output.

> Detect VS Code, Cursor, and Windsurf through parent processes in /terminal-setup

> `/terminal-setup` now refuses to modify a VS Code keybindings.json that contains a JSON syntax error (instead of rewriting it and reporting success), matching its documented invalid-JSON handling.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-20-the-sessions-sidebar-is-now-navigable-with-the-keyboard-and-mouse-arrows-open-an|The Sessions sidebar is now navigable with the keyboard and mouse…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-2-context-window-changes-in-v1-0-72|2 Context Window changes in v1.0.72]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-20-10-apps-and-integrations-changes-in-v1-0-72|10 Apps and Integrations changes in v1.0.72]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-20-4-safety-and-privacy-changes-in-v1-0-72|4 Safety and Privacy changes in v1.0.72]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve pasted prompt content when changing models through Ctrl+X /model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-20-2-editor-experience-changes-in-v1-0-72|2 Editor Experience changes in v1.0.72]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-13-other-changes-in-v1-0-72|13 other changes in v1.0.72]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-20 · Claude Code · [[Changes/Claude Code/2026-07-20-2-developer-workflow-changes-in-v2-1-216|2 Developer Workflow changes in v2.1.216]]
- Later: 2026-07-20 · OpenCode · [[Changes/OpenCode/2026-07-20-sync-the-embedded-terminal-theme-with-the-app-theme|Sync the embedded terminal theme with the app theme]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-20-38a47d&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-20-8-developer-workflow-changes-in-v1-0-72.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-20-38a47d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->