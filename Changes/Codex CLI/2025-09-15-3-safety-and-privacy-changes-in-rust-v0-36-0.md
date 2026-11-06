---
card_id: codex-cli-2025-09-15-71cbe5
date: '2025-09-15'
description: 'Codex CLI · 2025-09-15 · Safety and Privacy: 3 changes in 0.36.0 — Unified
  execution improvements (#3288, #3479) and race-condition fix (#3644); include…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 883
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 16a5fd96f33aa6c30473e1c22f0441112440a44a0fe5479c8c4c0e6aab0c2c07
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-15-71cbe5
  comparison: ''
  date: '2025-09-15'
  description: 'Codex CLI — 0.36.0: 3 Safety and Privacy changes'
  evidence:
  - quote: 'Unified execution improvements (#3288, #3479) and race-condition fix (#3644);
      include command output on timeouts (#3576); do not execute when command parses
      as a patch (#3382); improved sandbox timeout handling (#3435); flaky test fixes
      (#3596, #3564).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: 'Experimental automatic context compaction (#3446); expanded default sandbox
      (#3483); Azure Responses API workaround (#3528); preserve more item IDs in Azure
      (#3542); logging and clippy improvements (#3488, #3489); `just test` via nextest
      (#3508).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: 'core: expand default sandbox (#3483)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-safety-and-privacy-changes-in-rust-v0-36-0
  source_release: codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in rust-v0.36.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]]'
- '[[Changes/Gemini CLI/2025-09-09-2-safety-and-privacy-changes-in-v0-4-0|2 Safety
  and Privacy changes in v0.4.0]]'
- '[[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build:
  faster tests with nextest, add shear; minor macOS permission adjustment]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2|codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in rust-v0.36.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in rust-v0.36.0

**Codex CLI** · 2025-09-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.36.0) · from [[Releases/Codex CLI/codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2|0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Unified execution improvements (#3288, #3479) and race-condition fix (#3644); include command output on timeouts (#3576); do not execute when command parses as a patch (#3382); improved sandbox timeout handling (#3435); flaky test fixes (#3596, #3564).

> Experimental automatic context compaction (#3446); expanded default sandbox (#3483); Azure Responses API workaround (#3528); preserve more item IDs in Azure (#3542); logging and clippy improvements (#3488, #3489); `just test` via nextest (#3508).

> core: expand default sandbox (#3483)

Source: https://github.com/openai/codex/releases/tag/rust-v0.36.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-15-5-interface-experience-changes-in-rust-v0-36-0|5 Interface Experience changes in rust-v0.36.0]] · Interface Experience
- [[Changes/Codex CLI/2025-09-15-2-developer-workflow-changes-in-rust-v0-36-0|2 Developer Workflow changes in rust-v0.36.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-15-16-model-support-changes-in-rust-v0-36-0|16 Model Support changes in rust-v0.36.0]] · Model Support
- [[Changes/Codex CLI/2025-09-15-3-context-window-changes-in-rust-v0-36-0|3 Context Window changes in rust-v0.36.0]] · Context Window
- [[Changes/Codex CLI/2025-09-15-add-readme-ide-3494|add(readme): IDE (♯3494)]] · Editor Experience
- [[Changes/Codex CLI/2025-09-15-5-apps-and-integrations-changes-in-rust-v0-36-0|5 Apps and Integrations changes in rust-v0.36.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-09-15-6-account-and-access-changes-in-rust-v0-36-0|6 Account and Access changes in rust-v0.36.0]] · Account and Access
- [[Changes/Codex CLI/2025-09-15-49-other-changes-in-rust-v0-36-0|49 other changes in rust-v0.36.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-09-10 · Codex CLI · [[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build: faster tests with nextest, add shear; minor macOS permission adjustment]]
- Later: 2025-09-17 · Gemini CLI · [[Changes/Gemini CLI/2025-09-17-2-safety-and-privacy-changes-in-v0-5-3|2 Safety and Privacy changes in v0.5.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-15-71cbe5&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-15-3-safety-and-privacy-changes-in-rust-v0-36-0.md%0ACard%20ID%3A%20codex-cli-2025-09-15-71cbe5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.36.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->