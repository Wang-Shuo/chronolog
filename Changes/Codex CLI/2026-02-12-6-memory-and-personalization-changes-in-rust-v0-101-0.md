---
card_id: codex-cli-2026-02-12-768496
date: '2026-02-12'
description: 'Codex CLI · 2026-02-12 · Memory and Personalization: 6 changes in 0.101.0
  — Developer messages are now excluded from phase-1 memory input, reducing noisy
  or…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 938
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 69bc43332ed9f37a50bef7afc28b2e6b99d23c94c31de25fa5b03e27383dfb14
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-12-768496
  comparison: ''
  date: '2026-02-12'
  description: 'Codex CLI — 0.101.0: 6 Memory and Personalization changes'
  evidence:
  - quote: Developer messages are now excluded from phase-1 memory input, reducing
      noisy or irrelevant content entering memory. (#11608)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  - quote: Memory phase processing concurrency was reduced to make consolidation/staging
      more stable under load. (#11614)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  - quote: Cleaned and simplified the phase-1 memory pipeline code paths. (#11605)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  - quote: '#11608 exclude developer messages from phase-1 memory input @wendyjiao-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  - quote: '#11591 Add cwd to memory files @wendyjiao-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  - quote: '#11614 chore: reduce concurrency of memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.101.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-memory-and-personalization-changes-in-rust-v0-101-0
  source_release: codex-cli-2026-02-12-rust-v0-101-0-github-285845002-bcd2b414
  source_type: github_releases
  theme: memory
  title: 6 Memory and Personalization changes in rust-v0.101.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7
  Memory and Personalization changes in rust-v0.99.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-11-add-instructions-command-to-view-and-toggle-custom-instruction-files|Add
  /instructions command to view and toggle custom instruction files]]'
- '[[Changes/Codex CLI/2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0|11
  Memory and Personalization changes in rust-v0.100.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-101-0-github-285845002-bcd2b414|codex-cli-2026-02-12-rust-v0-101-0-github-285845002-bcd2b414]]'
source_type: github_releases
theme: memory
title: 6 Memory and Personalization changes in rust-v0.101.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Memory and Personalization changes in rust-v0.101.0

**Codex CLI** · 2026-02-12 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.101.0) · from [[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-101-0-github-285845002-bcd2b414|0.101.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Developer messages are now excluded from phase-1 memory input, reducing noisy or irrelevant content entering memory. (#11608)

> Memory phase processing concurrency was reduced to make consolidation/staging more stable under load. (#11614)

> Cleaned and simplified the phase-1 memory pipeline code paths. (#11605)

> #11608 exclude developer messages from phase-1 memory input @wendyjiao-openai

> #11591 Add cwd to memory files @wendyjiao-openai

> #11614 chore: reduce concurrency of memories @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.101.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-12-3-model-support-changes-in-rust-v0-101-0|3 Model Support changes in rust-v0.101.0]] · Model Support
- [[Changes/Codex CLI/2026-02-12-2-other-changes-in-rust-v0-101-0|2 other changes in rust-v0.101.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-02-12 · Codex CLI · [[Changes/Codex CLI/2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0|11 Memory and Personalization changes in rust-v0.100.0]]
- Later: 2026-02-12 · Open WebUI · [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-12-768496&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-12-6-memory-and-personalization-changes-in-rust-v0-101-0.md%0ACard%20ID%3A%20codex-cli-2026-02-12-768496%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.101.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->