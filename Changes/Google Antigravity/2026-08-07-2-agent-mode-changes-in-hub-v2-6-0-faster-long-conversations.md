---
card_id: google-antigravity-2026-08-07-f4abd8
date: '2026-08-07'
description: 'Google Antigravity · 2026-08-07 · Agent Mode: 2 changes in HUB v2.6.0
  — Faster long conversations, more reliable hooks and subagents — Agents no longer
  hang…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9e15956283501de209ac5029921fd177d261344e34b4ce8226f525428bb4f201
product: google-antigravity
product_name: Google Antigravity
record:
  card_id: google-antigravity-2026-08-07-f4abd8
  comparison: ''
  date: '2026-08-07'
  description: 'Google Antigravity — HUB v2.6.0 — Faster long conversations, more
    reliable hooks and subagents: 2 Agent Mode changes'
  evidence:
  - quote: Agents no longer hang forever when a stop hook keeps blocking the end of
      a turn; the turn now finishes after repeated blocks.
    source_release: https://antigravity.google/releases?tab=hub&version=2.6.0
  - quote: Stopping a subagent now also stops everything it spawned, including nested
      subagents and their background tasks, instead of leaving them running.
    source_release: https://antigravity.google/releases?tab=hub&version=2.6.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: google-antigravity
  product_name: Google Antigravity
  slug: 2-agent-mode-changes-in-hub-v2-6-0-faster-long-conversations
  source_release: google-antigravity-2026-08-07-rel-hub-2-6-0-1cc55d28
  source_type: antigravity_changelog
  theme: agent-mode
  title: 2 Agent Mode changes in HUB v2.6.0 — Faster long conversations…
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-08-06-feat-pr-generator-agent-implement-antigravity-agent-runner-and-prompt-templates|feat(pr-generator-agent):
  implement Antigravity agent runner and prompt templates …]]'
- '[[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed
  the 200-subagent-per-session spawn cap]]'
- '[[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent
  Mode changes in rust-v0.147.0]]'
source_release: '[[Releases/Google Antigravity/google-antigravity-2026-08-07-rel-hub-2-6-0-1cc55d28|google-antigravity-2026-08-07-rel-hub-2-6-0-1cc55d28]]'
source_type: antigravity_changelog
theme: agent-mode
title: 2 Agent Mode changes in HUB v2.6.0 — Faster long conversations…
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in HUB v2.6.0 — Faster long conversations…

**Google Antigravity** · 2026-08-07 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://antigravity.google/releases?tab=hub&version=2.6.0) · from [[Releases/Google Antigravity/google-antigravity-2026-08-07-rel-hub-2-6-0-1cc55d28|HUB v2.6.0 — Faster long conversations, more reliable hooks and subagents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Agents no longer hang forever when a stop hook keeps blocking the end of a turn; the turn now finishes after repeated blocks.

> Stopping a subagent now also stops everything it spawned, including nested subagents and their background tasks, instead of leaving them running.

Source: https://antigravity.google/releases?tab=hub&version=2.6.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Google Antigravity/2026-08-07-you-can-now-copy-an-image-to-your-clipboard-from-an-artifact-or-the-file-viewer|Copy an image to your clipboard from an artifact or the file viewer, using the menu…]] · Interface Experience
- [[Changes/Google Antigravity/2026-08-07-2-reliability-and-performance-changes-in-hub-v2-6-0-faster-long-conversations|2 Reliability and Performance changes in HUB v2.6.0 — Faster long conversations…]] · Reliability and Performance
- [[Changes/Google Antigravity/2026-08-07-2-apps-and-integrations-changes-in-hub-v2-6-0-faster-long-conversations|2 Apps and Integrations changes in HUB v2.6.0 — Faster long conversations…]] · Apps and Integrations
- [[Changes/Google Antigravity/2026-08-07-conversations-started-by-background-automations-no-longer-disappear-from-the-sid|Conversations started by background automations no longer disappear from the sidebar list]] · Automation and Scheduling
- [[Changes/Google Antigravity/2026-08-07-2-editor-experience-changes-in-hub-v2-6-0-faster-long-conversations|2 Editor Experience changes in HUB v2.6.0 — Faster long conversations…]] · Editor Experience
- [[Changes/Google Antigravity/2026-08-07-faster-long-conversations-more-reliable-hooks-and-subagents|Faster long conversations, more reliable hooks and subagents]] · Apps and Integrations
- [[Changes/Google Antigravity/2026-08-07-2-interface-experience-changes-in-hub-v2-6-0-faster-long-conversations|2 Interface Experience changes in HUB v2.6.0 — Faster long conversations…]] · Interface Experience
- [[Changes/Google Antigravity/2026-08-07-steps-waiting-on-your-input-now-show-the-icon-for-the-tool-involved-including-in|Steps waiting on your input now show the icon for the tool involved, including…]] · Safety and Privacy
- [[Changes/Google Antigravity/2026-08-07-6-other-changes-in-hub-v2-6-0-faster-long-conversations|6 other changes in HUB v2.6.0 — Faster long conversations…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-07 · Codex CLI · [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]]
- Later: 2026-08-07 · OpenHands · [[Changes/OpenHands/2026-08-07-feat-add-a-typed-agent-action-for-launching-local-or-cloud-child-conversations-b|feat: add a typed agent action for launching local or Cloud child conversations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20google-antigravity-2026-08-07-f4abd8&body=Card%3A%20Changes%2FGoogle%20Antigravity%2F2026-08-07-2-agent-mode-changes-in-hub-v2-6-0-faster-long-conversations.md%0ACard%20ID%3A%20google-antigravity-2026-08-07-f4abd8%0ASource%3A%20https%3A%2F%2Fantigravity.google%2Freleases%3Ftab%3Dhub%26version%3D2.6.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->