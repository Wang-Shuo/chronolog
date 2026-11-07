---
card_id: kimi-code-2026-06-05-86165c
date: '2026-06-05'
description: 'Kimi Code · 2026-06-05 · Model Support: 4 changes in Kimi Code 0.11.0
  (2026-06-05) — `KIMI_MODEL_TEMPERATURE`, `KIMI_MODEL_TOP_P` — sampling parameters
  applied…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1243
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3a986a6395ace5a41a5ef2dadd9f9302fa6a5ca4f57b4e712962275f1670378f
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-06-05-86165c
  comparison: ''
  date: '2026-06-05'
  description: 'Kimi Code — Kimi Code 0.11.0 (2026-06-05): 4 Model Support changes'
  evidence:
  - quote: '`KIMI_MODEL_TEMPERATURE`, `KIMI_MODEL_TOP_P` — sampling parameters applied
      globally to any `kimi` provider (not tied to `KIMI_MODEL_NAME`).'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: '`KIMI_MODEL_THINKING_KEEP` — Moonshot preserved-thinking passthrough (`thinking.keep`),
      injected only while Thinking is on.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Clamp OpenAI Chat Completions `xhigh` and `max` thinking effort to `high`
      unless the model supports `xhigh` on `v1/chat/completions`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Refresh provider model metadata when capabilities change without model
      ID changes.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 4-model-support-changes-in-kimi-code-0-11-0
  source_release: kimi-code-2026-06-05-0-11-0-96565a16
  source_type: kimi_code_changelog
  theme: model-support
  title: 4 Model Support changes in Kimi Code 0.11.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model
  Support changes in rust-v0.137.0]]'
- '[[Changes/Cline/2026-06-05-3-model-support-changes-in-v3-88-0|3 Model Support changes
  in v3.88.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model
  Support changes in v1.0.60]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-06-05-0-11-0-96565a16|kimi-code-2026-06-05-0-11-0-96565a16]]'
source_type: kimi_code_changelog
theme: model-support
title: 4 Model Support changes in Kimi Code 0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in Kimi Code 0.11.0

**Kimi Code** · 2026-06-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-06-05-0-11-0-96565a16|Kimi Code 0.11.0 (2026-06-05)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `KIMI_MODEL_TEMPERATURE`, `KIMI_MODEL_TOP_P` — sampling parameters applied globally to any `kimi` provider (not tied to `KIMI_MODEL_NAME`).

> `KIMI_MODEL_THINKING_KEEP` — Moonshot preserved-thinking passthrough (`thinking.keep`), injected only while Thinking is on.

> Clamp OpenAI Chat Completions `xhigh` and `max` thinking effort to `high` unless the model supports `xhigh` on `v1/chat/completions`.

> Refresh provider model metadata when capabilities change without model ID changes.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-06-05-use-a-fixed-30-minute-timeout-for-subagents-and-show-concise-resume-instructions|Use a fixed 30-minute timeout for subagents and show concise resume instructions…]] · Agent Mode
- [[Changes/Kimi Code/2026-06-05-support-multiline-edits-when-managing-upcoming-goals|Support multiline edits when managing upcoming goals]] · Editor Experience
- [[Changes/Kimi Code/2026-06-05-show-unknown-command-instead-of-too-many-arguments-when-an-invalid-subcommand-is|Show "unknown command" instead of "too many arguments" when an invalid subcommand…]] · Developer Workflow
- [[Changes/Kimi Code/2026-06-05-10-other-changes-in-kimi-code-0-11-0|10 other changes in Kimi Code 0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model Support changes in v1.0.60]]
- Later: 2026-06-05 · OpenCode · [[Changes/OpenCode/2026-06-05-4-model-support-changes-in-v1-16-0|4 Model Support changes in v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-06-05-86165c&body=Card%3A%20Changes%2FKimi%20Code%2F2026-06-05-4-model-support-changes-in-kimi-code-0-11-0.md%0ACard%20ID%3A%20kimi-code-2026-06-05-86165c%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->