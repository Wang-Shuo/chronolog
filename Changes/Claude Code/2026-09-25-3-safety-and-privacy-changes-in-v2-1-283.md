---
card_id: claude-code-2026-09-25-1e83b0
date: '2026-09-25'
description: 'Claude Code · 2026-09-25 · Safety and Privacy: 3 changes in v2.1.283
  — Fixed permission dialogs in screen-reader mode reading quoted commands and paths
  as if…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1258
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 54b4b79cf04e350d6f197fc0e22c77548f49baca5c0dd6d6a797ef66d3350411
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-1e83b0
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed permission dialogs in screen-reader mode reading quoted commands
      and paths as if they were the dialog's own text
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Changed interactive sessions on third-party providers or with telemetry
      off to start in auto mode when no permission mode is configured; `permissions.defaultMode`
      still overrides it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: '[VSCode] Fixed the permission mode indicator showing Default while the
      session kept running in auto or bypass mode after an automatic switch out of
      it failed; the switch is now retried until it lands'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-283
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.283
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-findings|Findings]]'
- '[[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety
  and Privacy changes in v2.1.282]]'
- '[[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security
  history in ChatGPT]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.283
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.283

**Claude Code** · 2026-09-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) · from [[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed permission dialogs in screen-reader mode reading quoted commands and paths as if they were the dialog's own text

> Changed interactive sessions on third-party providers or with telemetry off to start in auto mode when no permission mode is configured; `permissions.defaultMode` still overrides it

> [VSCode] Fixed the permission mode indicator showing Default while the session kept running in auto or bypass mode after an automatic switch out of it failed; the switch is now retried until it lands

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer Workflow changes in v2.1.283]] · Developer Workflow
- [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Agent Mode
- [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-25-improved-prompt-audit-on-claude-code-configuration-stale-paths-stale-commands-an|Improved prompt-audit on Claude Code configuration]] · Files and Data
- [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Context Window
- [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-25-2-interface-experience-changes-in-v2-1-283|2 Interface Experience changes in v2.1.283]] · Interface Experience
- [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-25 · ChatGPT · [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security history in ChatGPT]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-25-1e83b0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-25-3-safety-and-privacy-changes-in-v2-1-283.md%0ACard%20ID%3A%20claude-code-2026-09-25-1e83b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.283%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->