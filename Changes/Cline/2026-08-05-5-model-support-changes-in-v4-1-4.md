---
card_id: cline-2026-08-05-c44e78
date: '2026-08-05'
description: 'Cline · 2026-08-05 · Model Support: 5 changes in v4.1.4 — Remove model-initiated
  plan-to-act switching. Switching out of plan mode is now driven by you, not by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1304
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 082f496fe4c7bb34c039ac4d8c5d5fbc6527d8507a7f32bf0c6fbc412f7f737d
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-05-c44e78
  comparison: ''
  date: '2026-08-05'
  description: 'Cline — v4.1.4: 5 Model Support changes'
  evidence:
  - quote: Remove model-initiated plan-to-act switching. Switching out of plan mode
      is now driven by you, not by the model deciding mid-turn.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  - quote: Retry empty model responses on every provider rather than only Ollama,
      fixing hard "Model returned empty response" failures on OpenRouter, Cline, and
      OpenAI-compatible endpoints.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  - quote: Stop Claude 4.6+ and 5.x models being rejected with "thinking.type.enabled
      is not supported" when they resolve from the offline catalog or from a hand-typed
      model id.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  - quote: Restore Bedrock prompt caching, which reported zero cache reads and writes
      because the provider sent a cache format Bedrock discards, and route Bedrock
      foundation models through geo inference profiles.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  - quote: Inherit the MiniMax default model from models.dev, and refresh the bundled
      catalog, which adds Infomaniak and SCX.ai.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 5-model-support-changes-in-v4-1-4
  source_release: cline-2026-08-05-v4-1-4-github-365446897-8becc947
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v4.1.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-04-improved-the-refusal-when-claude-tries-to-invoke-a-skill-with-disable-model-invo|Improved
  the refusal when Claude tries to invoke a skill with disable-model-invocation]]'
- '[[Changes/Kimi Code/2026-08-04-fall-back-to-the-built-in-models-dev-catalog-snapshot-when-the-public-catalog-is|Fall
  back to the built-in models.dev catalog snapshot when the public catalog…]]'
- '[[Changes/Ollama/2026-08-04-ollama-run-kimi-k3-now-offers-kimi-k3-cloud-for-cloud-only-models-that-publish-n|ollama
  run kimi-k3 now offers kimi-k3:cloud for cloud-only models that publish…]]'
source_release: '[[Releases/Cline/cline-2026-08-05-v4-1-4-github-365446897-8becc947|cline-2026-08-05-v4-1-4-github-365446897-8becc947]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v4.1.4
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v4.1.4

**Cline** · 2026-08-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.4) · from [[Releases/Cline/cline-2026-08-05-v4-1-4-github-365446897-8becc947|v4.1.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remove model-initiated plan-to-act switching. Switching out of plan mode is now driven by you, not by the model deciding mid-turn.

> Retry empty model responses on every provider rather than only Ollama, fixing hard "Model returned empty response" failures on OpenRouter, Cline, and OpenAI-compatible endpoints.

> Stop Claude 4.6+ and 5.x models being rejected with "thinking.type.enabled is not supported" when they resolve from the offline catalog or from a hand-typed model id.

> Restore Bedrock prompt caching, which reported zero cache reads and writes because the provider sent a cache format Bedrock discards, and route Bedrock foundation models through geo inference profiles.

> Inherit the MiniMax default model from models.dev, and refresh the bundled catalog, which adds Infomaniak and SCX.ai.

Source: https://github.com/cline/cline/releases/tag/v4.1.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-05-recover-from-running-out-of-context-instead-of-failing-with-a-raw-provider-error|Recover from running out of context instead of failing with a raw provider error]] · Context Window
- [[Changes/Cline/2026-08-05-2-developer-workflow-changes-in-v4-1-4|2 Developer Workflow changes in v4.1.4]] · Developer Workflow
- [[Changes/Cline/2026-08-05-3-interface-experience-changes-in-v4-1-4|3 Interface Experience changes in v4.1.4]] · Interface Experience
- [[Changes/Cline/2026-08-05-2-apps-and-integrations-changes-in-v4-1-4|2 Apps and Integrations changes in v4.1.4]] · Apps and Integrations
- [[Changes/Cline/2026-08-05-5-other-changes-in-v4-1-4|5 other changes in v4.1.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-04 · Ollama · [[Changes/Ollama/2026-08-04-ollama-run-kimi-k3-now-offers-kimi-k3-cloud-for-cloud-only-models-that-publish-n|ollama run kimi-k3 now offers kimi-k3:cloud for cloud-only models that publish…]]
- Later: 2026-08-05 · Cline · [[Changes/Cline/2026-08-05-explain-when-a-free-model-promotion-ends-requests-to-a-retired-free-model-now-sh|Explain when a free model promotion ends]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-05-c44e78&body=Card%3A%20Changes%2FCline%2F2026-08-05-5-model-support-changes-in-v4-1-4.md%0ACard%20ID%3A%20cline-2026-08-05-c44e78%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->