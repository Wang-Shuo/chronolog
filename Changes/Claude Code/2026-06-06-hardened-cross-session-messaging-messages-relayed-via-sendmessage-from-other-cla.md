---
card_id: claude-code-2026-06-06-931934
date: '2026-06-06'
description: 'Claude Code · 2026-06-06 · Safety and Privacy: Hardened cross-session
  messaging: messages relayed via `SendMessage` from other Claude sessions no longer
  carry…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1147
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 36955396ae2f412dbf69b5302ec066b8a7e204644bb296bb14560b1fb82af4e4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-06-931934
  comparison: ''
  date: '2026-06-06'
  description: 'Claude Code — v2.1.166: Hardened cross-session messaging: messages
    relayed via `SendMessage` from other Claude sessions no longer carry user authority
    — receivers refuse relayed permission requests, and auto mode blocks them'
  evidence:
  - quote: 'Hardened cross-session messaging: messages relayed via `SendMessage` from
      other Claude sessions no longer carry user authority — receivers refuse relayed
      permission requests, and auto mode blocks them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla
  source_release: claude-code-2026-06-06-v2-1-166-github-335118845-ef990727
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Hardened cross-session messaging
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|Teams
  are the operating unit for a department, region, or subsidiary]]'
- '[[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown
  Mode is now available to all logged-in users across account types and workspaces]]'
- '[[Changes/Cursor/2026-06-04-you-can-now-hand-the-local-agent-your-own-tools-by-passing-function-definitions|Hand
  the local agent your own tools by passing function definitions through…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
source_type: github_releases
theme: safety-privacy
title: Hardened cross-session messaging
type: change
---

<!-- chronolog:begin region="header" -->
# Hardened cross-session messaging

**Claude Code** · 2026-06-06 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.166) · from [[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|v2.1.166]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hardened cross-session messaging: messages relayed via `SendMessage` from other Claude sessions no longer carry user authority — receivers refuse relayed permission requests, and auto mode blocks them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|Added fallbackModel setting to configure up to three fallback models tried…]] · Model Support
- [[Changes/Claude Code/2026-06-06-claude-code-now-retries-a-turn-once-on-the-fallback-model-when-the-api-rejects-a|Claude Code now retries a turn once on the fallback model when the API rejects…]] · Model Support
- [[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added glob pattern support in deny rule tool-name position ("" denies all tools)]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-06-max-thinking-tokens-0-thinking-disabled-and-the-per-model-thinking-toggle-now-di|MAX_THINKING_TOKENS=0, --thinking disabled, and the per-model thinking toggle…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-you-can-now-hand-the-local-agent-your-own-tools-by-passing-function-definitions|Hand the local agent your own tools by passing function definitions through…]]
- Later: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|Added --safe-mode flag (and CLAUDE_CODE_SAFE_MODE) to start Claude Code with all…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-06-931934&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla.md%0ACard%20ID%3A%20claude-code-2026-06-06-931934%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.166%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->