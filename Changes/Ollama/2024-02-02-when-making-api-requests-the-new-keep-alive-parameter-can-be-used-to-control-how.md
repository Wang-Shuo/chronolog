---
card_id: ollama-2024-02-02-b7e549
date: '2024-02-02'
description: 'Ollama · 2024-02-02 · Reliability and Performance: When making API requests,
  the new `keep_alive` parameter can be used to control how long a model stays…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 414
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: b66df0185669240e011b7e9116d054349a073df50049194390b7678d250b6623
product: ollama
product_name: Ollama
record:
  ai_generated: true
  card_id: ollama-2024-02-02-b7e549
  comparison: ''
  confidence: low
  date: '2024-02-02'
  description: 'Ollama — v0.1.23: When making API requests, the new `keep_alive` parameter
    can be used to control how long a model stays loaded in memory:'
  evidence:
  - quote: 'When making API requests, the new `keep_alive` parameter can be used to
      control how long a model stays loaded in memory:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.1.23
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: ollama
  product_name: Ollama
  slug: when-making-api-requests-the-new-keep-alive-parameter-can-be-used-to-control-how
  source_release: ollama-2024-02-02-v0-1-23-github-139618642-fffe661f
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v2
  title: When making API requests, the new `keep_alive` parameter can be used to control
    how…
  type: change
related_changes:
- '[[Changes/Dify/2024-01-25-refine-faster-rsa-implement-by-yeuoly-in-https-github-com-langgenius-dify-pull-2|refine:
  faster rsa implement]]'
- '[[Changes/Cursor/2024-02-02-0-25-2-copilot-performance-improvements|0.25.2: Copilot++
  performance improvements]]'
- '[[Changes/Cursor/2024-02-02-apply-diffs-from-chat-should-be-a-bit-faster|"Apply
  Diffs" from chat should be a bit faster]]'
source_release: '[[Releases/Ollama/ollama-2024-02-02-v0-1-23-github-139618642-fffe661f|ollama-2024-02-02-v0-1-23-github-139618642-fffe661f]]'
source_type: github_releases
theme: reliability-performance
title: When making API requests, the new keep_alive parameter can be used to control
  how…
type: change
---

<!-- chronolog:begin region="header" -->
# When making API requests, the new `keep_alive` parameter can be used to control how…

**Ollama** · 2024-02-02 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/ollama/ollama/releases/tag/v0.1.23) · from [[Releases/Ollama/ollama-2024-02-02-v0-1-23-github-139618642-fffe661f|v0.1.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> When making API requests, the new `keep_alive` parameter can be used to control how long a model stays loaded in memory:
>
> Source: https://github.com/ollama/ollama/releases/tag/v0.1.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2024-02-02-ollama-serve-will-now-print-prompt-when-ollama-debug-1-is-set|ollama serve will now print prompt when OLLAMA_DEBUG=1 is set]] · Developer Workflow
- [[Changes/Ollama/2024-02-02-3-multimodal-input-changes-in-v0-1-23|3 Multimodal Input changes in v0.1.23]] · Multimodal Input
- [[Changes/Ollama/2024-02-02-13-model-support-changes-in-v0-1-23|13 Model Support changes in v0.1.23]] · Model Support
- [[Changes/Ollama/2024-02-02-6-other-changes-in-v0-1-23|6 other changes in v0.1.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2024-02-02 · Cursor · [[Changes/Cursor/2024-02-02-apply-diffs-from-chat-should-be-a-bit-faster|"Apply Diffs" from chat should be a bit faster]]
- Later: 2024-02-13 · Dify · [[Changes/Dify/2024-02-13-pref-optimize-add-hit-count-query-performance-when-dataset-hit-by-takatost-in-ht|pref: optimize add hit count query performance when dataset hit]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2024-02-02-b7e549&body=Card%3A%20Changes%2FOllama%2F2024-02-02-when-making-api-requests-the-new-keep-alive-parameter-can-be-used-to-control-how.md%0ACard%20ID%3A%20ollama-2024-02-02-b7e549%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.1.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->