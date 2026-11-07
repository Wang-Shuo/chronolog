---
card_id: cline-2026-08-22-76e4e9
date: '2026-08-22'
description: 'Cline · 2026-08-22 · Model Support: Restore tool calling for custom
  OpenAI-Compatible models whose capability list was inferred from convenience flags
  like…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1321
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 2f1042a8dc38432a4ee94e79eaf17cba8744bd7ed6e67cbfe89e70b7868ba169
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-22-76e4e9
  comparison: ''
  date: '2026-08-22'
  description: 'Cline — v4.1.13: Restore tool calling for custom OpenAI-Compatible
    models whose capability list was inferred from convenience flags like `supportsReasoning`.
    The inferred list read as an authoritative denial and stripped every tool from
    the request; an explicitly authored capability list still decides.'
  evidence:
  - quote: Restore tool calling for custom OpenAI-Compatible models whose capability
      list was inferred from convenience flags like `supportsReasoning`. The inferred
      list read as an authoritative denial and stripped every tool from the request;
      an explicitly authored capability list still decides.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.13
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cline
  product_name: Cline
  slug: restore-tool-calling-for-custom-openai-compatible-models-whose-capability-list-w
  source_release: cline-2026-08-22-v4-1-13-github-375030518-eeba0b7b
  source_type: github_releases
  theme: model-support
  title: Restore tool calling for custom OpenAI-Compatible models whose capability
    list…
  type: change
related_changes:
- '[[Changes/OpenCode/2026-08-21-continue-responses-when-a-model-reports-an-unknown-finish-reason-instead-of-stop|Continue
  responses when a model reports an unknown finish reason instead of stopping early]]'
- '[[Changes/OpenCode/2026-08-21-core-route-vertex-ai-eu-and-us-multi-region-gemini-requests-through-rep-endpoint|Core
  Route Vertex AI eu and us multi-region Gemini requests through REP endpoints]]'
- '[[Changes/OpenHands/2026-08-21-perf-batch-streamingdeltaevents-so-the-ui-keeps-up-with-fast-models-by-vascosch9|perf:
  batch StreamingDeltaEvents so the UI keeps up with fast models]]'
source_release: '[[Releases/Cline/cline-2026-08-22-v4-1-13-github-375030518-eeba0b7b|cline-2026-08-22-v4-1-13-github-375030518-eeba0b7b]]'
source_type: github_releases
theme: model-support
title: Restore tool calling for custom OpenAI-Compatible models whose capability list…
type: change
---

<!-- chronolog:begin region="header" -->
# Restore tool calling for custom OpenAI-Compatible models whose capability list…

**Cline** · 2026-08-22 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.13) · from [[Releases/Cline/cline-2026-08-22-v4-1-13-github-375030518-eeba0b7b|v4.1.13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Restore tool calling for custom OpenAI-Compatible models whose capability list was inferred from convenience flags like `supportsReasoning`. The inferred list read as an authoritative denial and stripped every tool from the request; an explicitly authored capability list still decides.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-22-everything-here-lands-through-the-sdk-bundle-so-it-applies-to-windows-running-th|Everything here lands through the SDK bundle, so it applies to windows running that bundle]] · Apps and Integrations
- [[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry session and client identity into Langfuse traces for Hub-backed…]] · Agent Mode
- [[Changes/Cline/2026-08-22-keep-hub-backed-sessions-intact-across-a-hub-restart-or-upgrade-clients-replay-t|Keep Hub-backed sessions intact across a Hub restart or upgrade]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-21 · OpenHands · [[Changes/OpenHands/2026-08-21-perf-batch-streamingdeltaevents-so-the-ui-keeps-up-with-fast-models-by-vascosch9|perf: batch StreamingDeltaEvents so the UI keeps up with fast models]]
- Later: 2026-08-23 · Cline · [[Changes/Cline/2026-08-23-refresh-the-built-in-model-catalog-new-entries-include-claude-fable-5-grok-4-6-o|Refresh the built-in model catalog]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-22-76e4e9&body=Card%3A%20Changes%2FCline%2F2026-08-22-restore-tool-calling-for-custom-openai-compatible-models-whose-capability-list-w.md%0ACard%20ID%3A%20cline-2026-08-22-76e4e9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->