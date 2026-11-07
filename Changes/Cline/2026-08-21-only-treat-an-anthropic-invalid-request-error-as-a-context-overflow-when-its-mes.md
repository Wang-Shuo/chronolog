---
card_id: cline-2026-08-21-7b0ddd
date: '2026-08-21'
description: 'Cline · 2026-08-21 · Context Window: Only treat an Anthropic `invalid_request_error`
  as a context-overflow when its message says so. An unrelated invalid…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2529
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 1707f1c1a3b9f2a360bfc4ea40b6d549a03b3a9912b9f1452360f725a7cbde2d
product: cline
product_name: Cline
record:
  ai_generated: true
  card_id: cline-2026-08-21-7b0ddd
  comparison: ''
  confidence: low
  date: '2026-08-21'
  description: 'Cline — v4.1.11: Only treat an Anthropic `invalid_request_error` as
    a context-overflow when its message says so. An unrelated invalid request (bad
    tool schema, oversized image, unknown model id) no longer triggers context-overflow
    recovery.'
  evidence:
  - quote: Only treat an Anthropic `invalid_request_error` as a context-overflow when
      its message says so. An unrelated invalid request (bad tool schema, oversized
      image, unknown model id) no longer triggers context-overflow recovery.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: cline
  product_name: Cline
  slug: only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes
  source_release: cline-2026-08-21-v4-1-11-github-374187578-938b5fa5
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Only treat an Anthropic `invalid_request_error` as a context-overflow…
  type: change
related_changes:
- '[[Changes/Notion/2026-08-19-manage-your-workers-connections-and-personal-access-tokens-from-the-new-develope|Your
  Developer Portal, now in the sidebar]]'
- '[[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context
  Window changes in rust-v0.149.0]]'
- '[[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved
  the reminder shown after compaction so a skill''s original arguments are not…]]'
source_release: '[[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|cline-2026-08-21-v4-1-11-github-374187578-938b5fa5]]'
source_type: github_releases
theme: context-window
title: Only treat an Anthropic invalid_request_error as a context-overflow…
type: change
---

<!-- chronolog:begin region="header" -->
# Only treat an Anthropic `invalid_request_error` as a context-overflow…

**Cline** · 2026-08-21 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.11) · from [[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|v4.1.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Only treat an Anthropic `invalid_request_error` as a context-overflow when its message says so. An unrelated invalid request (bad tool schema, oversized image, unknown model id) no longer triggers context-overflow recovery.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-21-stop-offering-image-voice-and-other-non-chat-models-in-chat-model-pickers|Stop offering image, voice, and other non-chat models in chat model pickers]] · Voice and Audio
- [[Changes/Cline/2026-08-21-let-models-that-support-it-generate-images-during-a-task-generated-images-render|Let models that support it generate images during a task]] · Image Generation
- [[Changes/Cline/2026-08-21-show-the-billed-cost-for-cline-gateway-usage|Show the billed cost for Cline gateway usage]] · Pricing Model
- [[Changes/Cline/2026-08-21-show-the-diff-edit-view-for-multi-line-edits-in-files-with-crlf-line-endings|Show the diff edit view for multi-line edits in files with CRLF line endings]] · Editor Experience
- [[Changes/Cline/2026-08-21-3-model-support-changes-in-v4-1-11|3 Model Support changes in v4.1.11]] · Model Support
- [[Changes/Cline/2026-08-21-2-apps-and-integrations-changes-in-v4-1-11|2 Apps and Integrations changes in v4.1.11]] · Apps and Integrations
- [[Changes/Cline/2026-08-21-8-other-changes-in-v4-1-11|8 other changes in v4.1.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved the reminder shown after compaction so a skill's original arguments are not…]]
- Later: 2026-08-21 · Ollama · [[Changes/Ollama/2026-08-21-disabled-claude-code-s-tokens-left-token-countdown-system-message-which-ollama-m|Disabled Claude Code's "tokens left" token-countdown system message, which Ollama…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-21-7b0ddd&body=Card%3A%20Changes%2FCline%2F2026-08-21-only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes.md%0ACard%20ID%3A%20cline-2026-08-21-7b0ddd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->