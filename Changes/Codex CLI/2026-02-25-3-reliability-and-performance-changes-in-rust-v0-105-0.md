---
card_id: codex-cli-2026-02-25-3824e5
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Reliability and Performance: 3 changes in 0.105.0
  — App-server websocket handling is more robust: thread listeners survive…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2655
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7a09fc1be5f6235b6f4d9f6247f1e352d3b3e8f3d83d435ae1af5c6ea17259e6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-3824e5
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 3 Reliability and Performance changes'
  evidence:
  - quote: 'App-server websocket handling is more robust: thread listeners survive
      disconnects, Ctrl-C waits for in-flight turns before restarting, and websocket
      clients that send `permessage-deflate` can connect successfully. (#12373, #12517,
      #12629)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12120 feat: memory usage metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12761 feat: record memory usage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-reliability-and-performance-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: reliability-performance
  title: 3 Reliability and Performance changes in rust-v0.105.0
  type: change
related_changes:
- '[[Changes/Cline/2026-02-24-preconnect-websocket-to-reduce-response-latency|Preconnect
  websocket to reduce response latency]]'
- '[[Changes/Ollama/2026-02-24-mlx-engine-now-has-improved-memory-usage|MLX engine
  now has improved memory usage]]'
- '[[Changes/OpenCode/2026-02-24-2-reliability-and-performance-changes-in-v1-2-11|2
  Reliability and Performance changes in v1.2.11]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: reliability-performance
title: 3 Reliability and Performance changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Reliability and Performance changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server websocket handling is more robust: thread listeners survive disconnects, Ctrl-C waits for in-flight turns before restarting, and websocket clients that send `permessage-deflate` can connect successfully. (#12373, #12517, #12629)

> #12120 feat: memory usage metrics @jif-oai

> #12761 feat: record memory usage @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.105.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-25-15-developer-workflow-changes-in-rust-v0-105-0|15 Developer Workflow changes in rust-v0.105.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-25-12028-remove-feature-flag-collaboration-modes-aibrahim-oai|♯12028 remove feature flag collaboration modes @aibrahim-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-25-9-memory-and-personalization-changes-in-rust-v0-105-0|9 Memory and Personalization changes in rust-v0.105.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-25-you-can-now-dictate-prompts-by-holding-the-spacebar-to-record-and-transcribe-voi|Dictate prompts by holding the spacebar to record and transcribe voice input…]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-3-account-and-access-changes-in-rust-v0-105-0|3 Account and Access changes in rust-v0.105.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-25-8-interface-experience-changes-in-rust-v0-105-0|8 Interface Experience changes in rust-v0.105.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-25-2-editor-experience-changes-in-rust-v0-105-0|2 Editor Experience changes in rust-v0.105.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-25-5-context-window-changes-in-rust-v0-105-0|5 Context Window changes in rust-v0.105.0]] · Context Window
- [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Model Support
- [[Changes/Codex CLI/2026-02-25-2-mobile-and-desktop-changes-in-rust-v0-105-0|2 Mobile and Desktop changes in rust-v0.105.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-25-2-voice-and-audio-changes-in-rust-v0-105-0|2 Voice and Audio changes in rust-v0.105.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-156-other-changes-in-rust-v0-105-0|156 other changes in rust-v0.105.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-24 · OpenCode · [[Changes/OpenCode/2026-02-24-2-reliability-and-performance-changes-in-v1-2-11|2 Reliability and Performance changes in v1.2.11]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-2-reliability-and-performance-changes-in-v0-30-0|2 Reliability and Performance changes in v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-3824e5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-3824e5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->