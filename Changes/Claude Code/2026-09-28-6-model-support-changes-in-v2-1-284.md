---
card_id: claude-code-2026-09-28-de8651
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Model Support: 6 changes in v2.1.284 — Added
  Claude Sonnet 5.5 (`claude-sonnet-5-5`), now the default Sonnet model on the Anthropic…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1358
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5c6c9ba05afef3ab5961810368d26bd35a227bf733d19e32962e7747ff116326
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-de8651
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 6 Model Support changes'
  evidence:
  - quote: Added Claude Sonnet 5.5 (`claude-sonnet-5-5`), now the default Sonnet model
      on the Anthropic API — 1M context, $2/$10 per Mtok with $0.20/Mtok cache reads
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Added Claude apps gateway startup warnings when a managed policy's `availableModels`
      is empty, or leaves out the model Claude Code starts on without setting `model`
      or `enforceAvailableModels`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed the notice shown when a Sonnet model's safeguards flag a message
      to explain why it happened and to offer editing and retrying
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Changed safety-related model switches in sessions that pin an Opus model
      with `ANTHROPIC_DEFAULT_OPUS_MODEL` or `modelOverrides`: on the Anthropic API,
      the API now picks the model to switch to for each kind of flag, not the pinned
      model'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[VSCode] Added an Ultracode on/off switch under the Effort slider, replacing
      the slider''s Ultracode stop; the model pill shows "· Ultracode" at any effort
      level'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Added model family choices such as "Opus (latest)" for a
      thread, a channel default or your DM, so the choice follows the newest model
      in that family'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-model-support-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v2.1.284
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved
  interactive startup time]]'
- '[[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support
  changes in v2.1.282]]'
- '[[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support
  changes in v2.1.283]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Claude Sonnet 5.5 (`claude-sonnet-5-5`), now the default Sonnet model on the Anthropic API — 1M context, $2/$10 per Mtok with $0.20/Mtok cache reads

> Added Claude apps gateway startup warnings when a managed policy's `availableModels` is empty, or leaves out the model Claude Code starts on without setting `model` or `enforceAvailableModels`

> Changed the notice shown when a Sonnet model's safeguards flag a message to explain why it happened and to offer editing and retrying

> Changed safety-related model switches in sessions that pin an Opus model with `ANTHROPIC_DEFAULT_OPUS_MODEL` or `modelOverrides`: on the Anthropic API, the API now picks the model to switch to for each kind of flag, not the pinned model

> [VSCode] Added an Ultracode on/off switch under the Effort slider, replacing the slider's Ultracode stop; the model pill shows "· Ultracode" at any effort level

> [Claude Tag] Added model family choices such as "Opus (latest)" for a thread, a channel default or your DM, so the choice follows the newest model in that family

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
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]]
- Later: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-gpt-6-1-sol-improves-on-gpt-6-sol-in-agentic-coding-computer-use-and-professiona-815850|GPT-6.1 Sol in ChatGPT Work and Codex]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-de8651&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-6-model-support-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-de8651%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->