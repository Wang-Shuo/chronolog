---
card_id: codex-cli-2026-03-08-dca523
date: '2026-03-08'
description: 'Codex CLI · 2026-03-08 · Other changes: 11 changes in 0.112.0 — Treated
  `SIGTERM` like Ctrl-C for graceful app-server websocket shutdown instead of abrupt…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 38f447471bf896b3fbc60bbb0cc6ba9e3f16fbf19335037ec172a9e675975688
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-08-dca523
  comparison: ''
  date: '2026-03-08'
  description: 'Codex CLI — 0.112.0: 11 other changes'
  evidence:
  - quote: Treated `SIGTERM` like Ctrl-C for graceful app-server websocket shutdown
      instead of abrupt termination behavior. (#13594)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: Hardened js_repl image emission to accept only `data:` URLs, preventing
      external URL forwarding through `emitImage`. (#13507)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: Surfaced feedback/diagnostics earlier in the workflow so connectivity and
      diagnostics are visible before later steps. (#13604)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: Clarified js_repl image guidance (emission and encoding semantics), including
      clearer usage around repeated `emitImage` calls. (#13639)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13594 treat SIGTERM like ctrl-c for graceful shutdown @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13605 Fix codespell warning about pre-selects @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13482 Persist initialized js_repl bindings after failed cells @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13604 [diagnostics] show diagnostics earlier in workflow @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13507 Harden js_repl emitImage to accept only data: URLs @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13602 feat(core): persist trace_id for turns in RolloutItem::TurnContext
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13639 Clarify js_repl image emission and encoding guidance @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-other-changes-in-rust-v0-112-0
  source_release: codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5
  source_type: github_releases
  theme: uncategorized
  title: 11 other changes in rust-v0.112.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5|codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5]]'
source_type: github_releases
theme: uncategorized
title: 11 other changes in rust-v0.112.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 other changes in rust-v0.112.0

**Codex CLI** · 2026-03-08 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.112.0) · from [[Releases/Codex CLI/codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5|0.112.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Treated `SIGTERM` like Ctrl-C for graceful app-server websocket shutdown instead of abrupt termination behavior. (#13594)

> Hardened js_repl image emission to accept only `data:` URLs, preventing external URL forwarding through `emitImage`. (#13507)

> Surfaced feedback/diagnostics earlier in the workflow so connectivity and diagnostics are visible before later steps. (#13604)

> Clarified js_repl image guidance (emission and encoding semantics), including clearer usage around repeated `emitImage` calls. (#13639)

> #13594 treat SIGTERM like ctrl-c for graceful shutdown @maxj-oai

> #13605 Fix codespell warning about pre-selects @fjord-oai

> #13482 Persist initialized js_repl bindings after failed cells @fjord-oai

> #13604 [diagnostics] show diagnostics earlier in workflow @rhan-oai

> #13507 Harden js_repl emitImage to accept only data: URLs @fjord-oai

> #13602 feat(core): persist trace_id for turns in RolloutItem::TurnContext @owenlin0

> #13639 Clarify js_repl image emission and encoding guidance @fjord-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.112.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update models.json @aibrahim-oai]] · Model Support
- [[Changes/Codex CLI/2026-03-08-12702-improve-macos-seatbelt-network-and-unix-socket-handling-viyatb-oai|♯12702 Improve macOS Seatbelt network and unix socket handling @viyatb-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-08-added-a-new-model-selection-surface-update-so-the-latest-model-catalog-changes-a|Added a new model-selection surface update so the latest model catalog changes…]] · Interface Experience
- [[Changes/Codex CLI/2026-03-08-6-safety-and-privacy-changes-in-rust-v0-112-0|6 Safety and Privacy changes in rust-v0.112.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-08-2-apps-and-integrations-changes-in-rust-v0-112-0|2 Apps and Integrations changes in rust-v0.112.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-08-dca523&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-08-11-other-changes-in-rust-v0-112-0.md%0ACard%20ID%3A%20codex-cli-2026-03-08-dca523%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.112.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->