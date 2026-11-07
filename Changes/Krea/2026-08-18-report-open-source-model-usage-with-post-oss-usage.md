---
card_id: krea-2026-08-18-07e98f
date: '2026-08-18'
description: 'Krea · 2026-08-18 · Model Support: **Enterprise customers running Krea
  2 open weights can now report usage directly to Krea over HTTP.** Send an authenticated…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: db6ba605c11bcfa48046203d6783c9e3451e7c8ce11598f92c668f7f728f05df
product: krea
product_name: Krea
record:
  ai_generated: true
  card_id: krea-2026-08-18-07e98f
  comparison: ''
  confidence: low
  date: '2026-08-18'
  description: 'Krea — Report Krea 2 open-source usage over HTTP: **Enterprise customers
    running Krea 2 open weights can now report usage directly to Krea over HTTP.**
    Send an authenticated `POST` to `https://api.krea.ai/oss/usage` with Krea''s share
    as `amount_usd`, the `model` name, and the `generations` count. Reports feed into
    your monthly Krea invoice.'
  evidence:
  - quote: '**Enterprise customers running Krea 2 open weights can now report usage
      directly to Krea over HTTP.** Send an authenticated `POST` to `https://api.krea.ai/oss/usage`
      with Krea''s share as `amount_usd`, the `model` name, and the `generations`
      count. Reports feed into your monthly Krea invoice.'
    source_release: https://www.krea.ai/docs/changelog
  - quote: Report after each generation or aggregate and send once a month — both
      are acceptable, as long as usage is reported at least monthly.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Pass an optional `key` as an idempotency key so retries collapse to the
      same `job_id` and bill at most once.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Node.js, Python, and cURL snippets are included in the guide.
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: krea
  product_name: Krea
  slug: report-open-source-model-usage-with-post-oss-usage
  source_release: krea-2026-08-18-2026-08-18-report-krea-2-open-source-usage-over-http-8f9cae5f
  source_type: krea_changelog
  theme: model-support
  title: Report open-source model usage with `POST /oss/usage`
  type: change
related_changes:
- '[[Changes/OpenHands/2026-08-17-feat-add-llm-pre-flight-validation-to-prevent-saving-misconfigured-profiles-by-n|feat:
  add LLM pre-flight validation to prevent saving misconfigured profiles]]'
- '[[Changes/Superwhisper/2026-08-17-redesigned-the-model-details-sheet-with-a-cleaner-layout-download-size-info-and|Redesigned
  the model details sheet with a cleaner layout, download size info…]]'
- '[[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model
  Support changes in rust-v0.148.0]]'
source_release: '[[Releases/Krea/krea-2026-08-18-2026-08-18-report-krea-2-open-source-usage-over-http-8f9cae5f|krea-2026-08-18-2026-08-18-report-krea-2-open-source-usage-over-http-8f9cae5f]]'
source_type: krea_changelog
theme: model-support
title: Report open-source model usage with POST /oss/usage
type: change
---

<!-- chronolog:begin region="header" -->
# Report open-source model usage with `POST /oss/usage`

**Krea** · 2026-08-18 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-08-18-2026-08-18-report-krea-2-open-source-usage-over-http-8f9cae5f|Report Krea 2 open-source usage over HTTP]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Enterprise customers running Krea 2 open weights can now report usage directly to Krea over HTTP.** Send an authenticated `POST` to `https://api.krea.ai/oss/usage` with Krea's share as `amount_usd`, the `model` name, and the `generations` count. Reports feed into your monthly Krea invoice.
>
> Report after each generation or aggregate and send once a month — both are acceptable, as long as usage is reported at least monthly.
>
> Pass an optional `key` as an idempotency key so retries collapse to the same `job_id` and bill at most once.
>
> Node.js, Python, and cURL snippets are included in the guide.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-18 · Codex CLI · [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]]
- Later: 2026-08-18 · Lovable · [[Changes/Lovable/2026-08-18-gemini-3-7-flash-is-now-the-default-model-for-your-app-s-ai-features|Gemini 3.7 Flash is now the default model for your app's AI features]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-08-18-07e98f&body=Card%3A%20Changes%2FKrea%2F2026-08-18-report-open-source-model-usage-with-post-oss-usage.md%0ACard%20ID%3A%20krea-2026-08-18-07e98f%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->