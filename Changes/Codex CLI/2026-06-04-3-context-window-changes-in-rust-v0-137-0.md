---
card_id: codex-cli-2026-06-04-9e91bd
date: '2026-06-04'
description: 'Codex CLI · 2026-06-04 · Context Window: 3 changes in 0.137.0 — Shared
  prompts, context fragments, and skills plumbing moved into dedicated crates/extension…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1127
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7f2613175d06a34ecfa1c2f5bb297425623d01bfa0595885d3ab6637c1218db4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-04-9e91bd
  comparison: ''
  date: '2026-06-04'
  description: 'Codex CLI — 0.137.0: 3 Context Window changes'
  evidence:
  - quote: 'Shared prompts, context fragments, and skills plumbing moved into dedicated
      crates/extension paths to reduce `codex-core` coupling (#25151, #25953, #25959,
      #26106, #26122, #26167).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26122 chore: extract context fragments into dedicated crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26106 skills: resolve per-turn catalogs from turn input context @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-context-window-changes-in-rust-v0-137-0
  source_release: codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in rust-v0.137.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window
  changes in v0.9.6]]'
- '[[Changes/Gemini CLI/2026-06-03-feat-context-complete-simplification-work-by-joshualitt-in-https-github-com-goog|feat(context):
  Complete simplification work]]'
- '[[Changes/Ollama/2026-06-03-the-llama-cpp-backend-now-includes-cached-prompt-tokens-in-token-accounting-impr|The
  llama.cpp backend now includes cached prompt tokens in token accounting…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in rust-v0.137.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in rust-v0.137.0

**Codex CLI** · 2026-06-04 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.137.0) · from [[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|0.137.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Shared prompts, context fragments, and skills plumbing moved into dedicated crates/extension paths to reduce `codex-core` coupling (#25151, #25953, #25959, #26106, #26122, #26167).

> #26122 chore: extract context fragments into dedicated crate @jif-oai

> #26106 skills: resolve per-turn catalogs from turn input context @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.137.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6 Developer Workflow changes in rust-v0.137.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-04-25702-codex-enable-parallel-standalone-web-search-calls-sayan-oai|♯25702 codex enable parallel standalone web search calls @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image Generation changes in rust-v0.137.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-04-2-interface-experience-changes-in-rust-v0-137-0|2 Interface Experience changes in rust-v0.137.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0|19 Apps and Integrations changes in rust-v0.137.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-04-2-enterprise-and-administration-changes-in-rust-v0-137-0|2 Enterprise and Administration changes in rust-v0.137.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-04-local-session-history-is-safer-for-compressed-rollouts-renamed-titles-pathless-s|Local session history is safer for compressed rollouts, renamed titles, pathless…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-06-04-4-collaboration-changes-in-rust-v0-137-0|4 Collaboration changes in rust-v0.137.0]] · Collaboration
- [[Changes/Codex CLI/2026-06-04-2-mobile-and-desktop-changes-in-rust-v0-137-0|2 Mobile and Desktop changes in rust-v0.137.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Model Support
- [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-04-69-other-changes-in-rust-v0-137-0|69 other changes in rust-v0.137.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-06-03 · Ollama · [[Changes/Ollama/2026-06-03-the-llama-cpp-backend-now-includes-cached-prompt-tokens-in-token-accounting-impr|The llama.cpp backend now includes cached prompt tokens in token accounting…]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders|Cursor introduces Design Mode for faster canvas editing, new ways to understand…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-04-9e91bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-04-3-context-window-changes-in-rust-v0-137-0.md%0ACard%20ID%3A%20codex-cli-2026-06-04-9e91bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.137.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->