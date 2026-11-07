---
card_id: ollama-2025-08-25-752161
date: '2025-08-25'
description: 'Ollama · 2025-08-25 · Model Support: 3 changes in v0.11.7 — This model
  supports hybrid thinking, meaning thinking can be enabled or disabled by setting
  `think`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 959
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 56735d255ab851573f8073f7690d390e998aca9907f6c781faf0bacc90bc6a3b
product: ollama
product_name: Ollama
record:
  card_id: ollama-2025-08-25-752161
  comparison: ''
  date: '2025-08-25'
  description: 'Ollama — v0.11.7: 3 Model Support changes'
  evidence:
  - quote: 'This model supports hybrid thinking, meaning thinking can be enabled or
      disabled by setting `think` in Ollama''s API:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.11.7
  - quote: DeepSeek-V3.1 has over 671B parameters, and so a large amount of VRAM is
      required to run it. Ollama's [Turbo mode](https://ollama.com/turbo) (in preview)
      provides access to powerful hardware in the cloud you can use to run the model.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.11.7
  - quote: Ollama will now work with models who skip outputting the initial`<think>`
      tag (e.g. DeepSeek-V3.1)
    source_release: https://github.com/ollama/ollama/releases/tag/v0.11.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 3-model-support-changes-in-v0-11-7
  source_release: ollama-2025-08-25-v0-11-7-github-242072210-9cf2e263
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.11.7
  type: change
related_changes:
- '[[Changes/Cline/2025-08-21-removing-max-tokens-from-sonic-model-by-pashpashpash-in-https-github-com-cline-c|removing
  max tokens from sonic model]]'
- '[[Changes/Cursor/2025-08-21-2-model-support-changes-in-1-5|2 Model Support changes
  in 1.5]]'
- '[[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support
  changes in v0.6.23]]'
source_release: '[[Releases/Ollama/ollama-2025-08-25-v0-11-7-github-242072210-9cf2e263|ollama-2025-08-25-v0-11-7-github-242072210-9cf2e263]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.11.7
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.11.7

**Ollama** · 2025-08-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.11.7) · from [[Releases/Ollama/ollama-2025-08-25-v0-11-7-github-242072210-9cf2e263|v0.11.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This model supports hybrid thinking, meaning thinking can be enabled or disabled by setting `think` in Ollama's API:

> DeepSeek-V3.1 has over 671B parameters, and so a large amount of VRAM is required to run it. Ollama's [Turbo mode](https://ollama.com/turbo) (in preview) provides access to powerful hardware in the cloud you can use to run the model.

> Ollama will now work with models who skip outputting the initial`<think>` tag (e.g. DeepSeek-V3.1)

Source: https://github.com/ollama/ollama/releases/tag/v0.11.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2025-08-25-download-ollama-for-macos-or-windows|Download Ollama for macOS or Windows]] · Mobile and Desktop
- [[Changes/Ollama/2025-08-25-8-other-changes-in-v0-11-7|8 other changes in v0.11.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-08-21 · Open WebUI · [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]]
- Later: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-5-model-support-changes-in-rust-v0-24-0|5 Model Support changes in rust-v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2025-08-25-752161&body=Card%3A%20Changes%2FOllama%2F2025-08-25-3-model-support-changes-in-v0-11-7.md%0ACard%20ID%3A%20ollama-2025-08-25-752161%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.11.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->