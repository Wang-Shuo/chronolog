---
card_id: codex-cli-2026-04-15-a20bd0
date: '2026-04-15'
description: 'Codex CLI · 2026-04-15 · Memory and Personalization: 9 changes in 0.121.0
  — Added TUI and app-server controls for memory mode, memory reset/deletion, and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9823179ed2121f4a264fc66b12405fbf8703078e97046f14234fa9036e522855
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-15-a20bd0
  comparison: ''
  date: '2026-04-15'
  description: 'Codex CLI — 0.121.0: 9 Memory and Personalization changes'
  evidence:
  - quote: 'Added TUI and app-server controls for memory mode, memory reset/deletion,
      and memory-extension cleanup (#17632, #17626, #17913, #17937, #17844).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Updated app-server docs for new MCP, marketplace, turn injection, memory
      reset, filesystem metadata, external-agent migration, and websocket token-hash
      APIs (#17364, #17717, #17703, #17913, #17719, #17855, #17871).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: Added memory pipeline documentation for extension cleanup (#17844).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17626 feat: disable memory endpoint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17913 feat: add endpoint to delete memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17844 feat: cleaning of memories extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17919 chore: do not disable memories for past rollouts on reset @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17632 feat: memories menu @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17937 feat: reset memories button @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-memory-and-personalization-changes-in-rust-v0-121-0
  source_release: codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03
  source_type: github_releases
  theme: memory
  title: 9 Memory and Personalization changes in rust-v0.121.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-10-agent-no-longer-hangs-on-the-first-turn-when-the-memory-backend-is-unavailable|Agent
  no longer hangs on the first turn when the memory backend is unavailable]]'
- '[[Changes/GitHub Copilot CLI/2026-04-13-custom-instruction-files-preserve-special-characters-like-and-placeholders|Custom
  instruction files preserve special characters like & and placeholders]]'
- '[[Changes/Gemini CLI/2026-04-14-2-memory-and-personalization-changes-in-v0-38-0|2
  Memory and Personalization changes in v0.38.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03]]'
source_type: github_releases
theme: memory
title: 9 Memory and Personalization changes in rust-v0.121.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Memory and Personalization changes in rust-v0.121.0

**Codex CLI** · 2026-04-15 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.121.0) · from [[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|0.121.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added TUI and app-server controls for memory mode, memory reset/deletion, and memory-extension cleanup (#17632, #17626, #17913, #17937, #17844).

> Updated app-server docs for new MCP, marketplace, turn injection, memory reset, filesystem metadata, external-agent migration, and websocket token-hash APIs (#17364, #17717, #17703, #17913, #17719, #17855, #17871).

> Added memory pipeline documentation for extension cleanup (#17844).

> #17626 feat: disable memory endpoint @jif-oai

> #17913 feat: add endpoint to delete memories @jif-oai

> #17844 feat: cleaning of memories extension @jif-oai

> #17919 chore: do not disable memories for past rollouts on reset @jif-oai

> #17632 feat: memories menu @jif-oai

> #17937 feat: reset memories button @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.121.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-15-3-model-support-changes-in-rust-v0-121-0|3 Model Support changes in rust-v0.121.0]] · Model Support
- [[Changes/Codex CLI/2026-04-15-17684-adjust-default-tool-search-result-caps-malone-oai|♯17684 Adjust default tool search result caps @malone-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-15-9-apps-and-integrations-changes-in-rust-v0-121-0|9 Apps and Integrations changes in rust-v0.121.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context Window changes in rust-v0.121.0]] · Context Window
- [[Changes/Codex CLI/2026-04-15-7-agent-mode-changes-in-rust-v0-121-0|7 Agent Mode changes in rust-v0.121.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-15-4-developer-workflow-changes-in-rust-v0-121-0|4 Developer Workflow changes in rust-v0.121.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-15-17640-fix-stability-exec-server-jif-oai|♯17640 fix: stability exec server @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-15-added-realtime-and-app-server-apis-for-output-modality-transcript-completion-eve|Added realtime and app-server APIs for output modality, transcript completion…]] · Editor Experience
- [[Changes/Codex CLI/2026-04-15-17414-fix-thread-list-cwd-filtering-for-windows-verbatim-paths-etraut-openai|♯17414 Fix thread/list cwd filtering for Windows verbatim paths @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0|10 Safety and Privacy changes in rust-v0.121.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-15-17717-codex-refactor-marketplace-add-into-shared-core-flow-xli-oai|♯17717 codex Refactor marketplace add into shared core flow @xli-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-15-99-other-changes-in-rust-v0-121-0|99 other changes in rust-v0.121.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-14 · Gemini CLI · [[Changes/Gemini CLI/2026-04-14-2-memory-and-personalization-changes-in-v0-38-0|2 Memory and Personalization changes in v0.38.0]]
- Later: 2026-04-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-16-custom-instructions-and-skills-refresh-from-disk-after-clear-or-new|Custom instructions and skills refresh from disk after /clear or /new]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-15-a20bd0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0.md%0ACard%20ID%3A%20codex-cli-2026-04-15-a20bd0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.121.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->