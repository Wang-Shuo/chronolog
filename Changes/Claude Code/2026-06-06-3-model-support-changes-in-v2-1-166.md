---
card_id: claude-code-2026-06-06-e78874
date: '2026-06-06'
description: 'Claude Code · 2026-06-06 · Model Support: 3 changes in v2.1.166 — Added
  `fallbackModel` setting to configure up to three fallback models tried in order
  when…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 76884e1c6fce0bddc7547051cebff70b6b1ed8829f015b8b9bb094bca682f59b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-06-e78874
  comparison: ''
  date: '2026-06-06'
  description: 'Claude Code — v2.1.166: 3 Model Support changes'
  evidence:
  - quote: Added `fallbackModel` setting to configure up to three fallback models
      tried in order when the primary model is overloaded or unavailable; `--fallback-model`
      now also applies to interactive sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
  - quote: '`MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking
      toggle now disable thinking on models that think by default via the Claude API
      (3P providers unchanged)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
  - quote: Claude Code now retries a turn once on the fallback model when the API
      rejects an unexpected non-retryable error; auth, rate-limit, request-size, and
      transport errors still surface immediately
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-model-support-changes-in-v2-1-166
  source_release: claude-code-2026-06-06-v2-1-166-github-335118845-ef990727
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v2.1.166
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-05-4-model-support-changes-in-kimi-code-0-11-0|4 Model
  Support changes in Kimi Code 0.11.0]]'
- '[[Changes/OpenCode/2026-06-05-4-model-support-changes-in-v1-16-0|4 Model Support
  changes in v1.16.0]]'
- '[[Changes/OpenCode/2026-06-05-2-model-support-changes-in-v1-16-2|2 Model Support
  changes in v1.16.2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v2.1.166
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v2.1.166

**Claude Code** · 2026-06-06 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.166) · from [[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|v2.1.166]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `fallbackModel` setting to configure up to three fallback models tried in order when the primary model is overloaded or unavailable; `--fallback-model` now also applies to interactive sessions

> `MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking toggle now disable thinking on models that think by default via the Claude API (3P providers unchanged)

> Claude Code now retries a turn once on the fallback model when the API rejects an unexpected non-retryable error; auth, rate-limit, request-size, and transport errors still surface immediately

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened cross-session messaging]] · Safety and Privacy
- [[Changes/Claude Code/2026-06-06-added-glob-pattern-support-in-deny-rule-tool-name-position-denies-all-tools-allo|Added glob pattern support in deny rule tool-name position ("" denies all tools)]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-06-claude-agents-typing-a-url-into-the-list-now-filters-to-the-session-whose-first|claude agents: typing a URL into the list now filters to the session whose first…]] · Agent Mode
- [[Changes/Claude Code/2026-06-06-claude-update-now-announces-the-target-version-before-downloading-instead-of-goi|claude update now announces the target version before downloading instead of going…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-05 · OpenCode · [[Changes/OpenCode/2026-06-05-2-model-support-changes-in-v1-16-2|2 Model Support changes in v1.16.2]]
- Later: 2026-06-07 · Ollama · [[Changes/Ollama/2026-06-07-openai-compatible-api-models-list-now-aligns-with-available-model-tags|OpenAI-compatible API models list now aligns with available model tags]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-06-e78874&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-06-3-model-support-changes-in-v2-1-166.md%0ACard%20ID%3A%20claude-code-2026-06-06-e78874%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.166%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->