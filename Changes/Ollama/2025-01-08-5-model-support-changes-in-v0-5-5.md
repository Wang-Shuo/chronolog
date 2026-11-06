---
card_id: ollama-2025-01-08-eca5a0
date: '2025-01-08'
description: 'Ollama · 2025-01-08 · Model Support: 5 changes in v0.5.5 — [Phi-4](https://ollama.com/library/phi4):
  Phi 4 is a 14B parameter, state-of-the-art open model from…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 730
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8b408876b24c1c416e12d828e6721f71742b947dc2c69f682d7fff00f174b239
product: ollama
product_name: Ollama
record:
  card_id: ollama-2025-01-08-eca5a0
  comparison: ''
  date: '2025-01-08'
  description: 'Ollama — v0.5.5: 5 Model Support changes'
  evidence:
  - quote: '[Phi-4](https://ollama.com/library/phi4): Phi 4 is a 14B parameter, state-of-the-art
      open model from Microsoft.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.5
  - quote: '[DeepSeek-V3](https://ollama.com/library/deepseek-v3): A strong Mixture-of-Experts
      (MoE) language model with 671B total parameters with 37B activated for each
      token.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.5
  - quote: '[Dolphin 3](https://ollama.com/library/dolphin3): the next generation
      of the Dolphin series of instruct-tuned models designed to be the ultimate general
      purpose local model, enabling coding, math, agentic, function calling, and general
      use cases.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.5
  - quote: '[SmallThinker](https://ollama.com/library/smallthinker): A new small reasoning
      model fine-tuned from the Qwen 2.5 3B Instruct model.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.5
  - quote: 'The `/api/create` API endpoint that powers `ollama create` has been changed
      to improve conversion time and also accept a JSON object. **Note: this change
      is not backwards compatible**. If importing models, make sure you''re using
      version `0.5.5` or later for both Ollama and the `ollama` CLI when running `ollama
      create`. If using `ollama.create` in the Python or JavaScript libraries, make
      sure to update to the latest version.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.5.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 5-model-support-changes-in-v0-5-5
  source_release: ollama-2025-01-08-v0-5-5-github-193800987-48cb1ade
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.5.5
  type: change
related_changes:
- '[[Changes/DeepSeek API/2024-12-26-deepseek-chat|deepseek-chat]]'
- "[[Changes/Open WebUI/2024-12-31-ollama-parameters-respected-resolved-an-issue-where-input-parameters-for-ollama|\U0001F6E0️
  Ollama Parameters Respected]]"
- '[[Changes/Dify/2025-01-07-7-model-support-changes-in-0-15-0|7 Model Support changes
  in 0.15.0]]'
source_release: '[[Releases/Ollama/ollama-2025-01-08-v0-5-5-github-193800987-48cb1ade|ollama-2025-01-08-v0-5-5-github-193800987-48cb1ade]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.5.5
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.5.5

**Ollama** · 2025-01-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.5.5) · from [[Releases/Ollama/ollama-2025-01-08-v0-5-5-github-193800987-48cb1ade|v0.5.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> [Phi-4](https://ollama.com/library/phi4): Phi 4 is a 14B parameter, state-of-the-art open model from Microsoft.

> [DeepSeek-V3](https://ollama.com/library/deepseek-v3): A strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token.

> [Dolphin 3](https://ollama.com/library/dolphin3): the next generation of the Dolphin series of instruct-tuned models designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases.

> [SmallThinker](https://ollama.com/library/smallthinker): A new small reasoning model fine-tuned from the Qwen 2.5 3B Instruct model.

> The `/api/create` API endpoint that powers `ollama create` has been changed to improve conversion time and also accept a JSON object. **Note: this change is not backwards compatible**. If importing models, make sure you're using version `0.5.5` or later for both Ollama and the `ollama` CLI when running `ollama create`. If using `ollama.create` in the Python or JavaScript libraries, make sure to update to the latest version.

Source: https://github.com/ollama/ollama/releases/tag/v0.5.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2025-01-08-granite-3-1-dense-https-ollama-com-library-granite3-1-dense-2b-and-8b-text-only|Granite 3.1 Dense((source link)]] · Reliability and Performance
- [[Changes/Ollama/2025-01-08-granite-3-1-moe-https-ollama-com-library-granite3-1-moe-1b-and-3b-long-context-m|Granite 3.1 MoE((source link)]] · Context Window
- [[Changes/Ollama/2025-01-08-command-r7b-https-ollama-com-library-command-r7b-the-smallest-model-in-cohere-s|Command R7B((source link) the smallest model…]] · Developer Workflow
- [[Changes/Ollama/2025-01-08-2-other-changes-in-v0-5-5|2 other changes in v0.5.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-01-07 · Dify · [[Changes/Dify/2025-01-07-7-model-support-changes-in-0-15-0|7 Model Support changes in 0.15.0]]
- Later: 2025-01-10 · Aider · [[Changes/Aider/2025-01-10-2-model-support-changes-in-v0-71-0|2 Model Support changes in v0.71.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2025-01-08-eca5a0&body=Card%3A%20Changes%2FOllama%2F2025-01-08-5-model-support-changes-in-v0-5-5.md%0ACard%20ID%3A%20ollama-2025-01-08-eca5a0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.5.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->