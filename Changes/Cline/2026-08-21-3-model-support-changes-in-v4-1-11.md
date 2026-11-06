---
card_id: cline-2026-08-21-eace8d
date: '2026-08-21'
description: 'Cline · 2026-08-21 · Model Support: 3 changes in v4.1.11 — Restore custom
  base URLs for Gemini, and normalize legacy host-root values so they keep working.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1320
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 42ab0e6511d5b9cb27492a806d61575d41ed9c8389586fe5be02d037b3bab6db
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-21-eace8d
  comparison: ''
  date: '2026-08-21'
  description: 'Cline — v4.1.11: 3 Model Support changes'
  evidence:
  - quote: Restore custom base URLs for Gemini, and normalize legacy host-root values
      so they keep working.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Deliver a `PreToolUse` hook's `contextModification` to the model again,
      and wait for `PostToolUse` hooks so their output and `cancel` control are honored.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Refresh the model catalog, which adds AMD, Arcee, Echo, Jalapeno, Kosmik,
      LLM Gateway, RunInfra, and SCNet as providers and updates model lists, pricing,
      and per-provider default models across the board.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-11
  source_release: cline-2026-08-21-v4-1-11-github-374187578-938b5fa5
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s|Added
  ANTHROPIC_DEFAULT_MODEL environment variable]]'
- '[[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model
  Support changes in rust-v0.149.0]]'
- '[[Changes/Cline/2026-08-21-restore-tool-calling-for-custom-openai-compatible-models-whose-stored-capability|Restore
  tool calling for custom OpenAI-Compatible models whose stored capability…]]'
source_release: '[[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|cline-2026-08-21-v4-1-11-github-374187578-938b5fa5]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.11
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.11

**Cline** · 2026-08-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.11) · from [[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|v4.1.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Restore custom base URLs for Gemini, and normalize legacy host-root values so they keep working.

> Deliver a `PreToolUse` hook's `contextModification` to the model again, and wait for `PostToolUse` hooks so their output and `cancel` control are honored.

> Refresh the model catalog, which adds AMD, Arcee, Echo, Jalapeno, Kosmik, LLM Gateway, RunInfra, and SCNet as providers and updates model lists, pricing, and per-provider default models across the board.

Source: https://github.com/cline/cline/releases/tag/v4.1.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-21-stop-offering-image-voice-and-other-non-chat-models-in-chat-model-pickers|Stop offering image, voice, and other non-chat models in chat model pickers]] · Voice and Audio
- [[Changes/Cline/2026-08-21-only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes|Only treat an Anthropic invalid_request_error as a context-overflow…]] · Context Window
- [[Changes/Cline/2026-08-21-let-models-that-support-it-generate-images-during-a-task-generated-images-render|Let models that support it generate images during a task]] · Image Generation
- [[Changes/Cline/2026-08-21-show-the-billed-cost-for-cline-gateway-usage|Show the billed cost for Cline gateway usage]] · Pricing Model
- [[Changes/Cline/2026-08-21-show-the-diff-edit-view-for-multi-line-edits-in-files-with-crlf-line-endings|Show the diff edit view for multi-line edits in files with CRLF line endings]] · Editor Experience
- [[Changes/Cline/2026-08-21-2-apps-and-integrations-changes-in-v4-1-11|2 Apps and Integrations changes in v4.1.11]] · Apps and Integrations
- [[Changes/Cline/2026-08-21-8-other-changes-in-v4-1-11|8 other changes in v4.1.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-21 · Cline · [[Changes/Cline/2026-08-21-restore-tool-calling-for-custom-openai-compatible-models-whose-stored-capability|Restore tool calling for custom OpenAI-Compatible models whose stored capability…]]
- Later: 2026-08-21 · OpenHands · [[Changes/OpenHands/2026-08-21-perf-batch-streamingdeltaevents-so-the-ui-keeps-up-with-fast-models-by-vascosch9|perf: batch StreamingDeltaEvents so the UI keeps up with fast models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-21-eace8d&body=Card%3A%20Changes%2FCline%2F2026-08-21-3-model-support-changes-in-v4-1-11.md%0ACard%20ID%3A%20cline-2026-08-21-eace8d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->