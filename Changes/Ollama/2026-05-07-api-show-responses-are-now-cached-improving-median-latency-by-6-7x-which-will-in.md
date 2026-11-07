---
card_id: ollama-2026-05-07-8c7667
date: '2026-05-07'
description: 'Ollama · 2026-05-07 · Reliability and Performance: `/api/show` responses
  are now cached, improving median latency by **~6.7x** which will increase load speed…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 7b10e881ba1d633ea77c8eeb6aa0fa91e4189349dd7df237750307576aa43661
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-05-07-8c7667
  comparison: ''
  date: '2026-05-07'
  description: 'Ollama — v0.23.2: `/api/show` responses are now cached, improving
    median latency by **~6.7x** which will increase load speed for integrations like
    VS Code.'
  evidence:
  - quote: '`/api/show` responses are now cached, improving median latency by **~6.7x**
      which will increase load speed for integrations like VS Code.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.23.2
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: ollama
  product_name: Ollama
  slug: api-show-responses-are-now-cached-improving-median-latency-by-6-7x-which-will-in
  source_release: ollama-2026-05-07-v0-23-2-github-319160539-b5438b6d
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - latency
    - speed
    score: 100
    theme: reliability-performance
  - matched_terms:
    - integrations
    score: 50
    theme: apps-integrations
  title: '`/api/show` responses are now cached, improving median latency…'
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2
  Reliability and Performance changes in rust-v0.129.0]]'
- '[[Changes/Cursor/2026-05-07-pin-skills-as-quick-actions|Pin skills as quick actions]]'
- '[[Changes/Cursor/2026-05-07-build-in-parallel-from-plans|Build in parallel from
  plans]]'
source_release: '[[Releases/Ollama/ollama-2026-05-07-v0-23-2-github-319160539-b5438b6d|ollama-2026-05-07-v0-23-2-github-319160539-b5438b6d]]'
source_type: github_releases
theme: reliability-performance
title: /api/show responses are now cached, improving median latency…
type: change
---

<!-- chronolog:begin region="header" -->
# `/api/show` responses are now cached, improving median latency…

**Ollama** · 2026-05-07 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/ollama/ollama/releases/tag/v0.23.2) · from [[Releases/Ollama/ollama-2026-05-07-v0-23-2-github-319160539-b5438b6d|v0.23.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/api/show` responses are now cached, improving median latency by **~6.7x** which will increase load speed for integrations like VS Code.
>
> Source: https://github.com/ollama/ollama/releases/tag/v0.23.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-05-07-2-apps-and-integrations-changes-in-v0-23-2|2 Apps and Integrations changes in v0.23.2]] · Apps and Integrations
- [[Changes/Ollama/2026-05-07-use-ollama-launch-claude-desktop-restore-to-restore-claude-desktop-to-its-normal|Use ollama launch claude-desktop --restore to restore Claude Desktop to its normal state]] · Mobile and Desktop
- [[Changes/Ollama/2026-05-07-cleaner-image-generation-layout-in-the-mlx-runner|Cleaner image generation layout in the MLX runner]] · Image Generation
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-build-in-parallel-from-plans|Build in parallel from plans]]
- Later: 2026-05-08 · Codex CLI · [[Changes/Codex CLI/2026-05-08-added-a-faster-cargo-profiling-build-profile-and-disabled-empty-doctest-targets|Added a faster Cargo profiling build profile and disabled empty doctest targets…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-05-07-8c7667&body=Card%3A%20Changes%2FOllama%2F2026-05-07-api-show-responses-are-now-cached-improving-median-latency-by-6-7x-which-will-in.md%0ACard%20ID%3A%20ollama-2026-05-07-8c7667%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.23.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->