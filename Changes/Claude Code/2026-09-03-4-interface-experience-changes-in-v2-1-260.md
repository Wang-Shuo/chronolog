---
card_id: claude-code-2026-09-03-8debb6
date: '2026-09-03'
description: 'Claude Code · 2026-09-03 · Interface Experience: 4 changes in v2.1.260
  — Added a diff panel that opens beside the conversation in fullscreen mode and shows…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1333
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e74fd359c86a5f51da707536158e13cee35e423751135e7888ec507a835a91a4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-03-8debb6
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: 4 Interface Experience changes'
  evidence:
  - quote: Added a diff panel that opens beside the conversation in fullscreen mode
      and shows your uncommitted changes as Claude edits; toggle it with `/diff`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Added a likely cause for prompt-cache misses (e.g. tool definitions or
      system prompt changed, idle past the TTL) to `/cost` and the status line's `prompt_cache`
      field
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed `ctrl+l` / `cmd+k` in fullscreen mode to clear the transcript view
      like a terminal `clear`; scroll up to see earlier messages
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: '[VSCode] Added Open and Closed to the session list''s status filter menu'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-interface-experience-changes-in-v2-1-260
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: interface-experience
  title: 4 Interface Experience changes in v2.1.260
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-added-a-spend-limit-bar-to-usage-and-a-rate-limits-spend-limit-status-line-field|Added
  a Spend limit bar to /usage and a rate_limits.spend_limit status line…]]'
- '[[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface
  Experience changes in v2.1.257]]'
- '[[Changes/Claude Code/2026-09-02-vscode-added-an-active-quick-filter-and-a-status-filter-menu-needs-input-working|VSCode
  Added an Active quick filter and a status filter menu…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc]]'
source_type: github_releases
theme: interface-experience
title: 4 Interface Experience changes in v2.1.260
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Interface Experience changes in v2.1.260

**Claude Code** · 2026-09-03 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) · from [[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a diff panel that opens beside the conversation in fullscreen mode and shows your uncommitted changes as Claude edits; toggle it with `/diff`

> Added a likely cause for prompt-cache misses (e.g. tool definitions or system prompt changed, idle past the TTL) to `/cost` and the status line's `prompt_cache` field

> Changed `ctrl+l` / `cmd+k` in fullscreen mode to clear the transcript view like a terminal `clear`; scroll up to see earlier messages

> [VSCode] Added Open and Closed to the session list's status filter menu

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Model Support
- [[Changes/Claude Code/2026-09-03-improved-the-settings-error-for-rules-such-as-edit-c-dir-name-where-is-read-as-a|Improved the settings error for rules such as Edit(C:\dir\(name)\), where…]] · Editor Experience
- [[Changes/Claude Code/2026-09-03-improved-deleting-a-background-session-whose-worktree-has-unpushed-commits-the-m|Improved deleting a background session whose worktree has unpushed commits]] · Developer Workflow
- [[Changes/Claude Code/2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260|3 Mobile and Desktop changes in v2.1.260]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Agent Mode
- [[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context Window changes in v2.1.260]] · Context Window
- [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-3-other-changes-in-v2-1-260|3 other changes in v2.1.260]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-vscode-added-an-active-quick-filter-and-a-status-filter-menu-needs-input-working|VSCode Added an Active quick filter and a status filter menu…]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-3-interface-experience-changes-in-v2-1-261|3 Interface Experience changes in v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-03-8debb6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-03-4-interface-experience-changes-in-v2-1-260.md%0ACard%20ID%3A%20claude-code-2026-09-03-8debb6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.260%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->