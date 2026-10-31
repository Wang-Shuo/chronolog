---
card_id: claude-code-2026-09-28-c6ba83
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Account and Access: 4 changes in v2.1.284
  — Added certificate client authentication (`private_key_jwt`) between the Claude
  apps…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c854ab155d671c2830ff0c713fc2d3d37050e6be7b8028d3b405c03fe10412ad
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-c6ba83
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 4 Account and Access changes'
  evidence:
  - quote: Added certificate client authentication (`private_key_jwt`) between the
      Claude apps gateway and its identity provider, for identity providers that issue
      certificate credentials instead of client secrets
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved the startup refusal when managed settings require a sign-in (`forceLoginMethod`
      or `forceLoginOrgUUID`) and an API key, token or `apiKeyHelper` is configured:
      it now names the credential in use, where it is set, and how to remove it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Changed Claude to post its private sign-in notice at every
      @mention from someone who hasn''t connected their Claude account, instead of
      going quiet after the first'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Improved adding repositories as a channel manager: when your
      GitHub sign-in can''t confirm you''re a repository admin, the page asks you
      to sign in with GitHub'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-account-and-access-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v2.1.284
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-22-claude-tag-improved-the-github-banner-in-claude-tag-admin-settings-to-say-why-gi|Claude
  Tag Improved the GitHub banner in Claude Tag admin settings to say why…]]'
- '[[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account
  and Access changes in v2.1.281]]'
- '[[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added
  /mcp reconnect all in the interactive terminal to retry every MCP server…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added certificate client authentication (`private_key_jwt`) between the Claude apps gateway and its identity provider, for identity providers that issue certificate credentials instead of client secrets

> Improved the startup refusal when managed settings require a sign-in (`forceLoginMethod` or `forceLoginOrgUUID`) and an API key, token or `apiKeyHelper` is configured: it now names the credential in use, where it is set, and how to remove it

> [Claude Tag] Changed Claude to post its private sign-in notice at every @mention from someone who hasn't connected their Claude account, instead of going quiet after the first

> [Claude Tag] Improved adding repositories as a channel manager: when your GitHub sign-in can't confirm you're a repository admin, the page asks you to sign in with GitHub

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Agent Mode
- [[Changes/Claude Code/2026-09-28-claude-tag-improved-notify-members-now-in-admin-settings-one-press-reaches-every|Claude Tag Improved "Notify members now" in admin settings]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-28-added-effortslider-decreaseeffort-increaseeffort-and-toggleultracode-keybinding|Added effortSlider:decreaseEffort, increaseEffort and toggleUltracode…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved auto-memory loading]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]] · Pricing Model
- [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]] · Account and Access
- [[Changes/Claude Code/2026-09-28-2-collaboration-changes-in-v2-1-284|2 Collaboration changes in v2.1.284]] · Collaboration
- [[Changes/Claude Code/2026-09-28-improved-startup-time-and-memory-use-by-building-only-the-parts-of-the-settings|Improved startup time and memory use by building only the parts of the settings…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]]
- Later: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-c6ba83&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-4-account-and-access-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-c6ba83%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->