---
card_id: claude-code-2026-10-07-b10df1
date: '2026-10-07'
description: 'Claude Code · 2026-10-07 · Safety and Privacy: 3 changes in v2.1.293
  — Fixed Claude being told to continue or message subagents with `SendMessage` in
  sessions…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1270
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0c6ecb13ceac4013d1bbdd431b8af8109e64f6925fcc38b37fc141e813aa89b0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-07-b10df1
  comparison: ''
  date: '2026-10-07'
  description: 'Claude Code — v2.1.293: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed Claude being told to continue or message subagents with `SendMessage`
      in sessions, including resumed ones, where a host, a permission rule or a `--tools`
      list removed that tool
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
  - quote: Fixed `claude agents` offering bypass permissions that background sessions
      then ignored when consent was saved only in `.claude/settings.local.json` or
      a `--settings` file; it now asks for consent first, and a session that ignores
      bypass shows a short notice that stays
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
  - quote: Fixed Esc, or No without feedback, on a permission prompt not stopping
      the turn when `←` had just been pressed to move the session to the background
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-293
  source_release: claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.293
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety
  and Privacy changes in v2.1.290]]'
- '[[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety
  and Privacy changes in v2.1.292]]'
- '[[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed
  a regression in 2.1.290 where cloud sessions could drop answers to permission…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d|claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.293
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.293

**Claude Code** · 2026-10-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.293) · from [[Releases/Claude Code/claude-code-2026-10-07-v2-1-293-github-405988533-66d1bb8d|v2.1.293]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Claude being told to continue or message subagents with `SendMessage` in sessions, including resumed ones, where a host, a permission rule or a `--tools` list removed that tool

> Fixed `claude agents` offering bypass permissions that background sessions then ignored when consent was saved only in `.claude/settings.local.json` or a `--settings` file; it now asks for consent first, and a session that ignores bypass shows a short notice that stays

> Fixed Esc, or No without feedback, on a permission prompt not stopping the turn when `←` had just been pressed to move the session to the background

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-07-3-enterprise-and-administration-changes-in-v2-1-293|3 Enterprise and Administration changes in v2.1.293]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]] · Model Support
- [[Changes/Claude Code/2026-10-07-improved-the-bash-edit-diff-note-to-say-the-listed-files-changed-while-the-comma|Improved the Bash edit diff note to say the listed files changed while the command…]] · Editor Experience
- [[Changes/Claude Code/2026-10-07-code-review-improved-code-review-s-add-a-repository-dialog-to-list-each-reposito|Code Review Improved Code Review's Add a repository dialog to list each repository…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3 Apps and Integrations changes in v2.1.293]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode changes in v2.1.293]] · Agent Mode
- [[Changes/Claude Code/2026-10-07-5-other-changes-in-v2-1-293|5 other changes in v2.1.293]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]]
- Later: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-07-b10df1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-07-3-safety-and-privacy-changes-in-v2-1-293.md%0ACard%20ID%3A%20claude-code-2026-10-07-b10df1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.293%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->