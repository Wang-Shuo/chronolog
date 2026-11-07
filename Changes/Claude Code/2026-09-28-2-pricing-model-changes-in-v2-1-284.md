---
card_id: claude-code-2026-09-28-34b73c
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Pricing Model: 2 changes in v2.1.284 — Added
  dollar amounts to the Claude apps gateway spend limit in `/usage` and the status
  line…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3001
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 413e34175db0c7f9d369f361e64544c87c19fa532106977b776211e82397ba15
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-34b73c
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 2 Pricing Model changes'
  evidence:
  - quote: Added dollar amounts to the Claude apps gateway spend limit in `/usage`
      and the status line (for example "$271.40 / $500.00 spent this month") when
      the gateway runs this version or later; the status line's `rate_limits.spend_limit`
      also gains `used_usd`, `limit_usd` and `period`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved the usage-limit wait: the limit''s state and the countdown with
      the usage-credits option now show as one block under the prompt, and limit messages
      no longer repeat the countdown'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-pricing-model-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: pricing-model
  title: 2 Pricing Model changes in v2.1.284
  type: change
related_changes:
- '[[Changes/Midjourney/2026-09-24-polish-bugs|POLISH & BUGS]]'
- '[[Changes/Codex CLI/2026-09-25-47086-format-analytics-credit-usage-with-consistent-decimal-precision-fcoury-oai|♯47086
  Format analytics credit usage with consistent decimal precision @fcoury-oai]]'
- '[[Changes/OpenHands/2026-09-25-feat-scope-openai-subscription-caches-by-backend-by-uczltw6-in-https-github-com|feat:
  scope OpenAI subscription caches by backend]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: pricing-model
title: 2 Pricing Model changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Pricing Model changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added dollar amounts to the Claude apps gateway spend limit in `/usage` and the status line (for example "$271.40 / $500.00 spent this month") when the gateway runs this version or later; the status line's `rate_limits.spend_limit` also gains `used_usd`, `limit_usd` and `period`

> Improved the usage-limit wait: the limit's state and the countdown with the usage-credits option now show as one block under the prompt, and limit messages no longer repeat the countdown

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Agent Mode
- [[Changes/Claude Code/2026-09-28-claude-tag-improved-notify-members-now-in-admin-settings-one-press-reaches-every|Claude Tag Improved "Notify members now" in admin settings]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-28-added-effortslider-decreaseeffort-increaseeffort-and-toggleultracode-keybinding|Added effortSlider:decreaseEffort, increaseEffort and toggleUltracode…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved auto-memory loading]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]] · Account and Access
- [[Changes/Claude Code/2026-09-28-2-collaboration-changes-in-v2-1-284|2 Collaboration changes in v2.1.284]] · Collaboration
- [[Changes/Claude Code/2026-09-28-improved-startup-time-and-memory-use-by-building-only-the-parts-of-the-settings|Improved startup time and memory use by building only the parts of the settings…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-25 · OpenHands · [[Changes/OpenHands/2026-09-25-feat-scope-openai-subscription-caches-by-backend-by-uczltw6-in-https-github-com|feat: scope OpenAI subscription caches by backend]]
- Later: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-python-sdk|Python SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-34b73c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-2-pricing-model-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-34b73c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->