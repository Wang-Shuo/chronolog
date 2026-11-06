---
card_id: cline-2026-09-30-cd6efa
date: '2026-09-30'
description: 'Cline · 2026-09-30 · Model Support: 6 changes in v4.1.22 — Direct Anthropic
  requests now use Anthropic''s server-side refusal fallback. On OpenRouter and Cline…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1360
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f830252d3f5c6b39040ebc43c084bc0004856c898592bfc6d8460338a2981eb3
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-30-cd6efa
  comparison: ''
  date: '2026-09-30'
  description: 'Cline — v4.1.22: 6 Model Support changes'
  evidence:
  - quote: Direct Anthropic requests now use Anthropic's server-side refusal fallback.
      On OpenRouter and Cline, Anthropic models can fail over to another upstream
      provider instead of failing the request.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  - quote: When a response is blocked by a content filter, Cline now says so and suggests
      rephrasing, instead of "Model returned empty response".
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  - quote: Refreshed the model catalog. GPT-6.1 Sol becomes the default model for
      OpenAI, OpenRouter, GitHub Copilot, Cortecs, Eden AI, Kilo Gateway, both LLM
      Gateway providers, NanoGPT, OpenCode Zen, and Requesty. Vercel AI Gateway moves
      to Ling 3.1 Flash, Tempr Gateway to MiMo V2.6 Flash, CrossModel and Ofox to
      Claude Sonnet 5.5, Pioneer to GLiNER 2.5 Decide, and Scaleway to Qwen 3.8 27B.
      The Cline recommended list adds Claude Sonnet 5.5 and Claude Opus 5.5. If you
      use one of those providers without pinning a model, expect a different default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  - quote: After an API error you can type and send a new message instead of only
      using Retry. A `/compact` (or `/smol`, `/newtask`) typed during recovery stays
      in the composer instead of being sent to the model as text.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  - quote: 'Amazon Bedrock: GPT-6 and GPT-5.6 route through inference profiles, and
      India regions (`ap-south-1`, `ap-south-2`) resolve the `in.` profile. OpenAI
      models behind inference profiles get the reasoning effort setting they support.
      Nova 2 Lite with high reasoning, application inference-profile ARNs, and Nova
      Micro no longer get requests Bedrock rejects. A legacy AWS profile setting saved
      without the "use profile" flag now carries over as profile authentication instead
      of being dropped.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  - quote: Gateway models on providers that mix endpoints keep their own API protocol
      instead of falling back to the provider-wide default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.22
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 6-model-support-changes-in-v4-1-22
  source_release: cline-2026-09-30-v4-1-22-github-399711754-cf15d339
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v4.1.22
  type: change
related_changes:
- '[[Changes/v0/2026-09-29-what-counts-towards-chatgpt-usage|What counts towards ChatGPT
  usage?]]'
- '[[Changes/v0/2026-09-29-supported-models-currently-include-gpt-6-astra-gpt-5-6-sol-and-gpt-5-6-luna-use|Supported
  models currently include GPT-6 Astra, GPT-5.6 Sol, and GPT-5.6 Luna]]'
- '[[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed
  how failed API requests are retried]]'
source_release: '[[Releases/Cline/cline-2026-09-30-v4-1-22-github-399711754-cf15d339|cline-2026-09-30-v4-1-22-github-399711754-cf15d339]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v4.1.22
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v4.1.22

**Cline** · 2026-09-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.22) · from [[Releases/Cline/cline-2026-09-30-v4-1-22-github-399711754-cf15d339|v4.1.22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Direct Anthropic requests now use Anthropic's server-side refusal fallback. On OpenRouter and Cline, Anthropic models can fail over to another upstream provider instead of failing the request.

> When a response is blocked by a content filter, Cline now says so and suggests rephrasing, instead of "Model returned empty response".

> Refreshed the model catalog. GPT-6.1 Sol becomes the default model for OpenAI, OpenRouter, GitHub Copilot, Cortecs, Eden AI, Kilo Gateway, both LLM Gateway providers, NanoGPT, OpenCode Zen, and Requesty. Vercel AI Gateway moves to Ling 3.1 Flash, Tempr Gateway to MiMo V2.6 Flash, CrossModel and Ofox to Claude Sonnet 5.5, Pioneer to GLiNER 2.5 Decide, and Scaleway to Qwen 3.8 27B. The Cline recommended list adds Claude Sonnet 5.5 and Claude Opus 5.5. If you use one of those providers without pinning a model, expect a different default.

> After an API error you can type and send a new message instead of only using Retry. A `/compact` (or `/smol`, `/newtask`) typed during recovery stays in the composer instead of being sent to the model as text.

> Amazon Bedrock: GPT-6 and GPT-5.6 route through inference profiles, and India regions (`ap-south-1`, `ap-south-2`) resolve the `in.` profile. OpenAI models behind inference profiles get the reasoning effort setting they support. Nova 2 Lite with high reasoning, application inference-profile ARNs, and Nova Micro no longer get requests Bedrock rejects. A legacy AWS profile setting saved without the "use profile" flag now carries over as profile authentication instead of being dropped.

> Gateway models on providers that mix endpoints keep their own API protocol instead of falling back to the provider-wide default.

Source: https://github.com/cline/cline/releases/tag/v4.1.22
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-30-if-a-new-task-fails-cline-sign-in-signing-in-and-submitting-a-revised-prompt-now|If a new task fails Cline sign-in, signing in and submitting a revised prompt now…]] · Account and Access
- [[Changes/Cline/2026-09-30-reasoning-tokens-are-no-longer-counted-twice-in-token-usage-cost-is-unchanged|Reasoning tokens are no longer counted twice in token usage]] · Context Window
- [[Changes/Cline/2026-09-30-3-other-changes-in-v4-1-22|3 other changes in v4.1.22]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]]
- Later: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-2-model-support-changes-in-v1-0-90|2 Model Support changes in v1.0.90]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-30-cd6efa&body=Card%3A%20Changes%2FCline%2F2026-09-30-6-model-support-changes-in-v4-1-22.md%0ACard%20ID%3A%20cline-2026-09-30-cd6efa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.22%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->