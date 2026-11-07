---
card_id: cline-2026-09-02-1470c1
date: '2026-09-02'
description: 'Cline · 2026-09-02 · Model Support: 3 changes in v4.1.17 — Cline provider
  models are now read from the live catalog, so newly published models appear without…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1332
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e1ef2fa44164f29b45415271c8803dd8564f8030eaed9e8cc36dadeb9157eca9
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-02-1470c1
  comparison: ''
  date: '2026-09-02'
  description: 'Cline — v4.1.17: 3 Model Support changes'
  evidence:
  - quote: Cline provider models are now read from the live catalog, so newly published
      models appear without an extension update.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: 'Refreshed the built-in model catalog. Adds ten providers (Bothub, OpenReason,
      SenseNova (China), TokenGo, TokenRouter, Vancine, Volcengine Ark, Volcengine
      Ark Coding Plan, above.dev, and klokintegration.se) and updates model lists
      and pricing throughout. This is an unusually wide refresh: the resolved default
      model changes for 57 providers, most consequentially Anthropic, which now resolves
      to Claude Fable 5.1 instead of Claude Opus 5, with Amazon Bedrock, Vertex, OpenRouter,
      Vercel AI Gateway, Kilo Gateway, LLM Gateway, DevPass, DigitalOcean, CrossModel,
      Eden AI, and NanoGPT following. If you use a provider without pinning a model,
      expect a different default.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: The message the model receives when you reject a tool call now names the
      rejected tool and reads as your decision rather than an error.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-17
  source_release: cline-2026-09-02-v4-1-17-github-381000681-694bbda2
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.17
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-01-guardian-approval-review-now-honors-node-repl-policies-provided-through-model-me|Guardian
  approval review now honors Node REPL policies provided through model metadata]]'
- '[[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support
  changes in v2026.8.2]]'
- '[[Changes/OpenCode/2026-09-01-2-model-support-changes-in-v1-18-26|2 Model Support
  changes in v1.18.26]]'
source_release: '[[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|cline-2026-09-02-v4-1-17-github-381000681-694bbda2]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.17
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.17

**Cline** · 2026-09-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.17) · from [[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|v4.1.17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Cline provider models are now read from the live catalog, so newly published models appear without an extension update.

> Refreshed the built-in model catalog. Adds ten providers (Bothub, OpenReason, SenseNova (China), TokenGo, TokenRouter, Vancine, Volcengine Ark, Volcengine Ark Coding Plan, above.dev, and klokintegration.se) and updates model lists and pricing throughout. This is an unusually wide refresh: the resolved default model changes for 57 providers, most consequentially Anthropic, which now resolves to Claude Fable 5.1 instead of Claude Opus 5, with Amazon Bedrock, Vertex, OpenRouter, Vercel AI Gateway, Kilo Gateway, LLM Gateway, DevPass, DigitalOcean, CrossModel, Eden AI, and NanoGPT following. If you use a provider without pinning a model, expect a different default.

> The message the model receives when you reject a tool call now names the rejected tool and reads as your decision rather than an error.

Source: https://github.com/cline/cline/releases/tag/v4.1.17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-02-2-apps-and-integrations-changes-in-v4-1-17|2 Apps and Integrations changes in v4.1.17]] · Apps and Integrations
- [[Changes/Cline/2026-09-02-aborting-a-task-now-also-cancels-the-delegated-subagents-and-teammates-it-spawne|Aborting a task now also cancels the delegated subagents and teammates it spawned…]] · Agent Mode
- [[Changes/Cline/2026-09-02-cost-estimates-no-longer-appear-in-task-history-for-subscription-billed-tasks-cl|Cost estimates no longer appear in task history for subscription-billed tasks…]] · Pricing Model
- [[Changes/Cline/2026-09-02-global-rules-are-now-also-read-from-cline-rules-which-is-where-the-rules-tab-wri|Global rules are now also read from ~/Cline/Rules, which is where the Rules tab…]] · Developer Workflow
- [[Changes/Cline/2026-09-02-2-account-and-access-changes-in-v4-1-17|2 Account and Access changes in v4.1.17]] · Account and Access
- [[Changes/Cline/2026-09-02-7-other-changes-in-v4-1-17|7 other changes in v4.1.17]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-2-model-support-changes-in-v1-18-26|2 Model Support changes in v1.18.26]]
- Later: 2026-09-02 · Ollama · [[Changes/Ollama/2026-09-02-honor-gguf-model-defined-default-parameters|Honor GGUF model defined default parameters]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-02-1470c1&body=Card%3A%20Changes%2FCline%2F2026-09-02-3-model-support-changes-in-v4-1-17.md%0ACard%20ID%3A%20cline-2026-09-02-1470c1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->