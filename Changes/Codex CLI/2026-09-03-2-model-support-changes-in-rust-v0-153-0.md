---
card_id: codex-cli-2026-09-03-5637d5
date: '2026-09-03'
description: 'Codex CLI · 2026-09-03 · Model Support: 2 changes in 0.153.0 — App-server
  thread metadata includes nullable `model` and `reasoningEffort` fields. Structured…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1333
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0cf91e6e70dd931802139023d57a010addb13dbc4be3ca235fb6544e4b520de1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-03-5637d5
  comparison: ''
  date: '2026-09-03'
  description: 'Codex CLI — 0.153.0: 2 Model Support changes'
  evidence:
  - quote: App-server thread metadata includes nullable `model` and `reasoningEffort`
      fields. Structured asynchronous questions are supported through `request_user_input_async`
      when enabled by the model catalog. ([#42151](https://github.com/openai/codex/pull/42151),
      [#42178](https://github.com/openai/codex/pull/42178))
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  - quote: '[#42151](https://github.com/openai/codex/pull/42151) Expose model settings
      in app-server thread metadata'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.153.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-model-support-changes-in-rust-v0-153-0
  source_release: codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in rust-v0.153.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-09-02-honor-gguf-model-defined-default-parameters|Honor GGUF
  model defined default parameters]]'
- '[[Changes/ChatGPT/2026-09-03-today-we-re-introducing-gpt-6-astra-with-improvements-in-coding-research-compute-069f67|Introducing
  GPT-6 Astra]]'
- '[[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support
  changes in v2.1.260]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in rust-v0.153.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in rust-v0.153.0

**Codex CLI** · 2026-09-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.153.0) · from [[Releases/Codex CLI/codex-cli-2026-09-03-rust-v0-153-0-github-381669913-72d3437f|0.153.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server thread metadata includes nullable `model` and `reasoningEffort` fields. Structured asynchronous questions are supported through `request_user_input_async` when enabled by the model catalog. ([#42151](https://github.com/openai/codex/pull/42151), [#42178](https://github.com/openai/codex/pull/42178))

> [#42151](https://github.com/openai/codex/pull/42151) Expose model settings in app-server thread metadata

Source: https://github.com/openai/codex/releases/tag/rust-v0.153.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-03-42140-https-github-com-openai-codex-pull-42140-add-redo-support-to-vim-composer|♯42140((source link) Add redo support to Vim…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-03-3-interface-experience-changes-in-rust-v0-153-0|3 Interface Experience changes in rust-v0.153.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice and Audio changes in rust-v0.153.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source link) Prepare MCP connections…]] · Account and Access
- [[Changes/Codex CLI/2026-09-03-5-developer-workflow-changes-in-rust-v0-153-0|5 Developer Workflow changes in rust-v0.153.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source link) Emit turn cost telemetry…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context Window changes in rust-v0.153.0]] · Context Window
- [[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration changes in rust-v0.153.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source link) Detect standalone installs…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18 Apps and Integrations changes in rust-v0.153.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-03-50-other-changes-in-rust-v0-153-0|50 other changes in rust-v0.153.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-03 · Claude Code · [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]]
- Later: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-2-model-support-changes-in-rust-v0-153-1|2 Model Support changes in rust-v0.153.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-03-5637d5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-03-2-model-support-changes-in-rust-v0-153-0.md%0ACard%20ID%3A%20codex-cli-2026-09-03-5637d5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.153.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->