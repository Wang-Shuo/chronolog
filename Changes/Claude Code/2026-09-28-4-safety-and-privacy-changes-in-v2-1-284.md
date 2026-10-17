---
card_id: claude-code-2026-09-28-9538b0
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Safety and Privacy: 4 changes in v2.1.284
  — Fixed the workspace trust dialog appearing a second time after switching renderers
  or…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1261
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39910c1dba81e95909e5831de67493f1b87ec5016e8d621cf5b7210007a816ab
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-9538b0
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed the workspace trust dialog appearing a second time after switching
      renderers or updating when Claude Code was started in the home directory
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Improved Workflow tool sandbox hardening for errors thrown by async script
      hooks
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved `claude remote-control`: in a folder you haven''t trusted yet,
      it now asks for workspace trust on the terminal instead of exiting'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed interactive terminal and VS Code sessions to start in auto mode
      when no permission mode is configured, on every plan and provider; `permissions.defaultMode`
      still overrides it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.284
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety
  and Privacy changes in v2.1.282]]'
- '[[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security
  history in ChatGPT]]'
- '[[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety
  and Privacy changes in v2.1.283]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed the workspace trust dialog appearing a second time after switching renderers or updating when Claude Code was started in the home directory

> Improved Workflow tool sandbox hardening for errors thrown by async script hooks

> Improved `claude remote-control`: in a folder you haven't trusted yet, it now asks for workspace trust on the terminal instead of exiting

> Changed interactive terminal and VS Code sessions to start in auto mode when no permission mode is configured, on every plan and provider; `permissions.defaultMode` still overrides it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Agent Mode
- [[Changes/Claude Code/2026-09-28-claude-tag-improved-notify-members-now-in-admin-settings-one-press-reaches-every|Claude Tag Improved "Notify members now" in admin settings]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-28-2-memory-and-personalization-changes-in-v2-1-284|2 Memory and Personalization changes in v2.1.284]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-28-added-effortslider-decreaseeffort-increaseeffort-and-toggleultracode-keybinding|Added effortSlider:decreaseEffort, increaseEffort and toggleUltracode…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]] · Pricing Model
- [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]] · Account and Access
- [[Changes/Claude Code/2026-09-28-2-collaboration-changes-in-v2-1-284|2 Collaboration changes in v2.1.284]] · Collaboration
- [[Changes/Claude Code/2026-09-28-9-apps-and-integrations-changes-in-v2-1-284|9 Apps and Integrations changes in v2.1.284]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]]
- Later: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-9538b0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-4-safety-and-privacy-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-9538b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->