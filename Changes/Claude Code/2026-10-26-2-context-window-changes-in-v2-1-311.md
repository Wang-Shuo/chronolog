---
card_id: claude-code-2026-10-26-be3227
date: '2026-10-26'
description: 'Claude Code · 2026-10-26 · Context Window: 2 changes in v2.1.311 — Improved
  `/teleport` and `claude --teleport` to warn when a compacted cloud session loads…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1271
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 55c1f9322f61ae89bea163b872c652debaaadb8eb491d5d0c3b5607a460e5c06
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-26-be3227
  comparison: ''
  date: '2026-10-26'
  description: 'Claude Code — v2.1.311: 2 Context Window changes'
  evidence:
  - quote: Improved `/teleport` and `claude --teleport` to warn when a compacted cloud
      session loads from its last compaction, so the messages it summarized aren't
      in the local copy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  - quote: Changed `DISABLE_COMPACT` in settings files and in a mod's `$.env.set`
      so they can only turn compaction off, not back on
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-311
  source_release: claude-code-2026-10-26-v2-1-311-github-424682562-151da26b
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.311
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-16-2-context-window-changes-in-v2-1-302|2 Context
  Window changes in v2.1.302]]'
- '[[Changes/Claude Code/2026-10-19-3-context-window-changes-in-v2-1-304|3 Context
  Window changes in v2.1.304]]'
- '[[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated
  the /claude-api skill]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-26-v2-1-311-github-424682562-151da26b|claude-code-2026-10-26-v2-1-311-github-424682562-151da26b]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.311
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.311

**Claude Code** · 2026-10-26 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.311) · from [[Releases/Claude Code/claude-code-2026-10-26-v2-1-311-github-424682562-151da26b|v2.1.311]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/teleport` and `claude --teleport` to warn when a compacted cloud session loads from its last compaction, so the messages it summarized aren't in the local copy

> Changed `DISABLE_COMPACT` in settings files and in a mod's `$.env.set` so they can only turn compaction off, not back on

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed startup warnings about permission rules in settings files to show once per…]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-26-changed-clicks-on-scrollbar-arrows-and-bars-in-fullscreen-lists-to-act-when-the|Changed clicks on scrollbar arrows and bars in fullscreen lists to act…]] · Interface Experience
- [[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode changes in v2.1.311]] · Agent Mode
- [[Changes/Claude Code/2026-10-26-vscode-changed-the-session-list-side-bar-to-load-web-sessions-when-the-web-tab-i|VSCode Changed the session list side bar to load Web sessions when the Web tab…]] · Editor Experience
- [[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support changes in v2.1.311]] · Model Support
- [[Changes/Claude Code/2026-10-26-3-accessibility-and-localization-changes-in-v2-1-311|3 Accessibility and Localization changes in v2.1.311]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-26-improved-the-artifact-tool-s-choice-between-a-page-and-a-document-explainers-and|Improved the Artifact tool's choice between a page and a document]] · Files and Data
- [[Changes/Claude Code/2026-10-26-4-developer-workflow-changes-in-v2-1-311|4 Developer Workflow changes in v2.1.311]] · Developer Workflow
- [[Changes/Claude Code/2026-10-26-improved-the-message-shown-when-a-pasted-sign-in-code-is-refused-it-now-says-the|Improved the message shown when a pasted sign-in code is refused]] · Account and Access
- [[Changes/Claude Code/2026-10-26-12-other-changes-in-v2-1-311|12 other changes in v2.1.311]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-22 · Claude Code · [[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated the /claude-api skill]]
- Later: 2026-10-27 · Claude Code · [[Changes/Claude Code/2026-10-27-changed-a-subagent-s-autocompactwindow-to-lower-the-window-set-by-claude-code-au|Changed a subagent's autoCompactWindow to lower the window set…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-26-be3227&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-26-2-context-window-changes-in-v2-1-311.md%0ACard%20ID%3A%20claude-code-2026-10-26-be3227%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.311%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->