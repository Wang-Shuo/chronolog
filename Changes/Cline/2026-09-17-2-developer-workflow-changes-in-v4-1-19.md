---
card_id: cline-2026-09-17-862370
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Developer Workflow: 2 changes in v4.1.19 — Checkpoints
  no longer re-hash every untracked file on each message. In workspaces holding large…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2928
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f30eb4c9b56708289be25ba0996b44995949e6125d562f5b2ca3823aecade406
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-17-862370
  comparison: ''
  date: '2026-09-17'
  description: 'Cline — v4.1.19: 2 Developer Workflow changes'
  evidence:
  - quote: Checkpoints no longer re-hash every untracked file on each message. In
      workspaces holding large untracked directories this delayed every message by
      seconds to minutes; a persistent per-task index now lets git skip files it has
      already seen.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: '`run_commands` no longer hangs until its timeout after a command that
      backgrounds a child process. The command had finished, but the backgrounded
      process held the output pipes open.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 2-developer-workflow-changes-in-v4-1-19
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v4.1.19
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-16-5-developer-workflow-changes-in-v1-19-0|5 Developer
  Workflow changes in v1.19.0]]'
- '[[Changes/Claude Code/2026-09-17-7-developer-workflow-changes-in-v2-1-274|7 Developer
  Workflow changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer
  Workflow changes in v2.1.275]]'
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v4.1.19
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v4.1.19

**Cline** · 2026-09-17 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Checkpoints no longer re-hash every untracked file on each message. In workspaces holding large untracked directories this delayed every message by seconds to minutes; a persistent per-task index now lets git skip files it has already seen.

> `run_commands` no longer hangs until its timeout after a command that backgrounds a child process. The command had finished, but the backgrounded process held the output pipes open.

Source: https://github.com/cline/cline/releases/tag/v4.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-17-on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow|On Windows, opening a repository that contains a file named rg.exe, git.exe…]] · Mobile and Desktop
- [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]] · Model Support
- [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Agent Mode
- [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]] · Context Window
- [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing Model
- [[Changes/Cline/2026-09-17-web-search-is-now-enabled-by-default-on-models-that-support-it-outside-yolo-mode|Web search is now enabled by default on models that support it, outside YOLO mode]] · Search and Browsing
- [[Changes/Cline/2026-09-17-cline-s-logo-and-icons-have-been-refreshed-throughout-the-extension-including-th|Cline's logo and icons have been refreshed throughout the extension, including…]] · Interface Experience
- [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Apps and Integrations
- [[Changes/Cline/2026-09-17-5-other-changes-in-v4-1-19|5 other changes in v4.1.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer Workflow changes in v2.1.275]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-862370&body=Card%3A%20Changes%2FCline%2F2026-09-17-2-developer-workflow-changes-in-v4-1-19.md%0ACard%20ID%3A%20cline-2026-09-17-862370%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->