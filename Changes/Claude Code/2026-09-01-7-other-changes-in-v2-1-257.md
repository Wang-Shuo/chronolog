---
card_id: claude-code-2026-09-01-0296cb
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Other changes: 7 changes in v2.1.257 — Added
  "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour, 24-hour
  UTC, or…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5026eff2705569f9e5db5628fa5c0d013be235281af9f44a985ce9d54f985fec
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-0296cb
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 7 other changes'
  evidence:
  - quote: 'Added "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour,
      24-hour UTC, or a strftime pattern for the turn-end clock and transcript-view
      timestamps'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Improved policy helper diagnostics — refresh failures now show in `/status`,
      declining the managed-settings dialog prints why Claude Code exited, and helper
      timeouts are reported as timeouts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed a `policyHelper` in MDM or `managed-settings.json` shadowed at
      launch by cached server-managed settings to run (or exit) as soon as the fetch
      reports them removed, not at the next launch
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed `claude --resume <session-id> --bg` to continue that session under
      its own ID when nothing is running it, instead of silently starting a copy;
      a copy is now announced
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: '[VSCode] Added collapsible ACCOUNT & USAGE and SESSION MANAGER section
      headers to the session list panel, with the account email, the usage meter,
      and a View details link opening the usage dialog'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: '[VSCode] Added a collapse toggle to the Ungrouped section of the session
      list'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: '[VSCode] Changed "Delete session" to "Archive session": archived sessions
      move to a collapsible "Archived sessions" group at the bottom of the list with
      an Unarchive action'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-other-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v2.1.257
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v2.1.257

**Claude Code** · 2026-09-01 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour, 24-hour UTC, or a strftime pattern for the turn-end clock and transcript-view timestamps

> Improved policy helper diagnostics — refresh failures now show in `/status`, declining the managed-settings dialog prints why Claude Code exited, and helper timeouts are reported as timeouts

> Changed a `policyHelper` in MDM or `managed-settings.json` shadowed at launch by cached server-managed settings to run (or exit) as soon as the fetch reports them removed, not at the next launch

> Changed `claude --resume <session-id> --bg` to continue that session under its own ID when nothing is running it, instead of silently starting a copy; a copy is now announced

> [VSCode] Added collapsible ACCOUNT & USAGE and SESSION MANAGER section headers to the session list panel, with the account email, the usage meter, and a View details link opening the usage dialog

> [VSCode] Added a collapse toggle to the Ungrouped section of the session list

> [VSCode] Changed "Delete session" to "Archive session": archived sessions move to a collapsible "Archived sessions" group at the bottom of the list with an Unarchive action

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-0296cb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-7-other-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-0296cb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->