---
card_id: claude-code-2026-04-08-537c97
date: '2026-04-08'
description: 'Claude Code · 2026-04-08 · Editor Experience: 4 changes in v2.1.97 —
  Added syntax highlighting for Cedar policy files (`.cedar`, `.cedarpolicy`)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1121
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a5e56363614eaae0111516297c26f7ee540604ac2fcd16996499f6217b2f16f8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-08-537c97
  comparison: ''
  date: '2026-04-08'
  description: 'Claude Code — v2.1.97: 4 Editor Experience changes'
  evidence:
  - quote: Added syntax highlighting for Cedar policy files (`.cedar`, `.cedarpolicy`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
  - quote: Improved Accept Edits mode to auto-approve filesystem commands prefixed
      with safe env vars or process wrappers (e.g. `LANG=C rm foo`, `timeout 5 mkdir
      out`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
  - quote: Improved slash command and `@`-mention completion to trigger after CJK
      sentence punctuation, so Japanese/Chinese input no longer requires a space before
      `/` or `@`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
  - quote: Improved session transcript size by skipping empty hook entries and capping
      stored pre-edit file copies
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-editor-experience-changes-in-v2-1-97
  source_release: claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v2.1.97
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-02-2-editor-experience-changes-in-3-0|2 Editor Experience
  changes in 3.0]]'
- '[[Changes/Cursor/2026-04-02-agent-tabs-in-the-editor|Agent Tabs in the Editor]]'
- '[[Changes/Claude Code/2026-04-04-removed-vim-command-toggle-vim-mode-via-config-editor-mode|Removed
  /vim command (toggle vim mode via /config → Editor mode)]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33|claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v2.1.97
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v2.1.97

**Claude Code** · 2026-04-08 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.97) · from [[Releases/Claude Code/claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33|v2.1.97]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added syntax highlighting for Cedar policy files (`.cedar`, `.cedarpolicy`)

> Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe env vars or process wrappers (e.g. `LANG=C rm foo`, `timeout 5 mkdir out`)

> Improved slash command and `@`-mention completion to trigger after CJK sentence punctuation, so Japanese/Chinese input no longer requires a space before `/` or `@`

> Improved session transcript size by skipping empty hook entries and capping stored pre-edit file copies

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-08-improved-context-low-warning-to-show-as-a-transient-footer-notification-instead|Improved context-low warning to show as a transient footer notification instead…]] · Context Window
- [[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety and Privacy changes in v2.1.97]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-08-2-interface-experience-changes-in-v2-1-97|2 Interface Experience changes in v2.1.97]] · Interface Experience
- [[Changes/Claude Code/2026-04-08-3-developer-workflow-changes-in-v2-1-97|3 Developer Workflow changes in v2.1.97]] · Developer Workflow
- [[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes in v2.1.97]] · Agent Mode
- [[Changes/Claude Code/2026-04-08-4-other-changes-in-v2-1-97|4 other changes in v2.1.97]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-04-04 · Claude Code · [[Changes/Claude Code/2026-04-04-removed-vim-command-toggle-vim-mode-via-config-editor-mode|Removed /vim command (toggle vim mode via /config → Editor mode)]]
- Later: 2026-04-09 · Claude Code · [[Changes/Claude Code/2026-04-09-2-editor-experience-changes-in-v2-1-98|2 Editor Experience changes in v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-08-537c97&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-08-4-editor-experience-changes-in-v2-1-97.md%0ACard%20ID%3A%20claude-code-2026-04-08-537c97%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.97%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->