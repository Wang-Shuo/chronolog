---
card_id: ollama-2025-11-12-d42b7c
date: '2025-11-12'
description: 'Ollama · 2025-11-12 · Context Window: 2 changes in v0.12.11 — Ollama''s
  API and OpenAI-compatible API now support [log…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 923
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d217500a57f85e2cbe5de7b6cf63f09c74261ef80914b83dc4d083ea5c6462cd
product: ollama
product_name: Ollama
record:
  card_id: ollama-2025-11-12-d42b7c
  comparison: ''
  date: '2025-11-12'
  description: 'Ollama — v0.12.11: 2 Context Window changes'
  evidence:
  - quote: 'Ollama''s API and OpenAI-compatible API now support [log probabilities](https://cookbook.openai.com/examples/using_logprobs).
      Log probabilities of output tokens indicate the likelihood of each token occurring
      in the sequence given the context. This is useful for different use cases:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.12.11
  - quote: When setting `"top_logprobs"`, a number of most-likely tokens are also
      provided, making it possible to introspect alternative tokens. Below is an example
      request.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.12.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-context-window-changes-in-v0-12-11
  source_release: ollama-2025-11-12-v0-12-11-github-261869775-b0fab570
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v0.12.11
  type: change
related_changes:
- '[[Changes/Cline/2025-11-06-use-context-aware-task-manager-for-quick-auth-by-canvrno-in-https-github-com-cli|Use
  context-aware task manager for quick auth]]'
- '[[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window
  changes in v0.6.35]]'
- '[[Changes/Gemini CLI/2025-11-07-remove-context-percentage-in-footer-by-default-by-abhipatel12-in-https-github-co|Remove
  context percentage in footer by default]]'
source_release: '[[Releases/Ollama/ollama-2025-11-12-v0-12-11-github-261869775-b0fab570|ollama-2025-11-12-v0-12-11-github-261869775-b0fab570]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v0.12.11
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v0.12.11

**Ollama** · 2025-11-12 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.12.11) · from [[Releases/Ollama/ollama-2025-11-12-v0-12-11-github-261869775-b0fab570|v0.12.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama's API and OpenAI-compatible API now support [log probabilities](https://cookbook.openai.com/examples/using_logprobs). Log probabilities of output tokens indicate the likelihood of each token occurring in the sequence given the context. This is useful for different use cases:

> When setting `"top_logprobs"`, a number of most-likely tokens are also provided, making it possible to introspect alternative tokens. Below is an example request.

Source: https://github.com/ollama/ollama/releases/tag/v0.12.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2025-11-12-for-issues-or-feedback-on-using-vulkan-with-ollama-create-an-issue-labelled-vulk|For issues or feedback on using Vulkan with Ollama, create an issue labelled…]] · Developer Workflow
- [[Changes/Ollama/2025-11-12-autocomplete|Autocomplete]] · Editor Experience
- [[Changes/Ollama/2025-11-12-ollama-will-now-prefer-dedicated-gpus-over-igpus-when-scheduling-models|Ollama will now prefer dedicated GPUs over iGPUs when scheduling models]] · Model Support
- [[Changes/Ollama/2025-11-12-improved-rendering-performance-in-ollama-s-new-app-especially-when-rendering-cod|Improved rendering performance in Ollama's new app, especially when rendering code]] · Reliability and Performance
- [[Changes/Ollama/2025-11-12-13-other-changes-in-v0-12-11|13 other changes in v0.12.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2025-11-07 · Gemini CLI · [[Changes/Gemini CLI/2025-11-07-remove-context-percentage-in-footer-by-default-by-abhipatel12-in-https-github-co|Remove context percentage in footer by default]]
- Later: 2025-11-13 · Cline · [[Changes/Cline/2025-11-13-reduce-next-gen-model-context-window-anxiety-by-canvrno-in-https-github-com-clin|Reduce next-gen model context window anxiety]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2025-11-12-d42b7c&body=Card%3A%20Changes%2FOllama%2F2025-11-12-2-context-window-changes-in-v0-12-11.md%0ACard%20ID%3A%20ollama-2025-11-12-d42b7c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.12.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->