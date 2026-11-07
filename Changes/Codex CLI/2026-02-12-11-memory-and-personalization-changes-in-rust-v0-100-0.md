---
card_id: codex-cli-2026-02-12-44d93e
date: '2026-02-12'
description: 'Codex CLI · 2026-02-12 · Memory and Personalization: 11 changes in 0.100.0
  — Added memory management slash commands in the TUI (`/m_update`, `/m_drop`) and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 938
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee53e3f0fa9eee174f868df58477f04b5b3625a3ac25abac658287d43e29f456
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-12-44d93e
  comparison: ''
  date: '2026-02-12'
  description: 'Codex CLI — 0.100.0: 11 Memory and Personalization changes'
  evidence:
  - quote: 'Added memory management slash commands in the TUI (`/m_update`, `/m_drop`)
      and expanded memory-read/metrics plumbing. (#11569, #11459, #11593)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11439 feat: new memory prompts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11452 nit: increase max raw memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11454 fix: optional schema of memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11449 feat: set policy for phase 2 memory @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11462 clean: memory rollout recorder @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11459 feat: memory read path @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11471 chore: clean rollout extraction in memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11479 nit: memory truncation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11546 fix: update memory writing prompt @zuxin-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11593 feat: metrics to memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-memory-and-personalization-changes-in-rust-v0-100-0
  source_release: codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6
  source_type: github_releases
  theme: memory
  title: 11 Memory and Personalization changes in rust-v0.100.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-09-we-re-beginning-to-roll-out-a-test-for-ads-in-chatgpt-in-the-u-s-for-logged-in-a|Testing
  ads in ChatGPT (Free, Go)]]'
- '[[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7
  Memory and Personalization changes in rust-v0.99.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-11-add-instructions-command-to-view-and-toggle-custom-instruction-files|Add
  /instructions command to view and toggle custom instruction files]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6]]'
source_type: github_releases
theme: memory
title: 11 Memory and Personalization changes in rust-v0.100.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Memory and Personalization changes in rust-v0.100.0

**Codex CLI** · 2026-02-12 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.100.0) · from [[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|0.100.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added memory management slash commands in the TUI (`/m_update`, `/m_drop`) and expanded memory-read/metrics plumbing. (#11569, #11459, #11593)

> #11439 feat: new memory prompts @jif-oai

> #11452 nit: increase max raw memories @jif-oai

> #11454 fix: optional schema of memories @jif-oai

> #11449 feat: set policy for phase 2 memory @jif-oai

> #11462 clean: memory rollout recorder @jif-oai

> #11459 feat: memory read path @jif-oai

> #11471 chore: clean rollout extraction in memories @jif-oai

> #11479 nit: memory truncation @jif-oai

> #11546 fix: update memory writing prompt @zuxin-oai

> #11593 feat: metrics to memories @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.100.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-12-11412-tui-show-non-file-layer-content-in-debug-config-bolinfest|♯11412 tui: show non-file layer content in /debug-config @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-12-11521-test-app-server-stabilize-app-list-thread-feature-flag-test-by-using-file|♯11521 test(app-server): stabilize app/list thread feature-flag test by using…]] · Account and Access
- [[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context Window changes in rust-v0.100.0]] · Context Window
- [[Changes/Codex CLI/2026-02-12-improved-websocket-session-stability-by-continuing-ping-handling-when-idle-and-s|Improved websocket session stability by continuing ping handling when idle…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-12-2-agent-mode-changes-in-rust-v0-100-0|2 Agent Mode changes in rust-v0.100.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-12-4-mobile-and-desktop-changes-in-rust-v0-100-0|4 Mobile and Desktop changes in rust-v0.100.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0|5 Safety and Privacy changes in rust-v0.100.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-12-4-model-support-changes-in-rust-v0-100-0|4 Model Support changes in rust-v0.100.0]] · Model Support
- [[Changes/Codex CLI/2026-02-12-reduced-repeated-skill-parse-error-spam-during-active-edits-by-increasing-file-w|Reduced repeated skill parse-error spam during active edits by increasing…]] · Editor Experience
- [[Changes/Codex CLI/2026-02-12-5-apps-and-integrations-changes-in-rust-v0-100-0|5 Apps and Integrations changes in rust-v0.100.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-12-59-other-changes-in-rust-v0-100-0|59 other changes in rust-v0.100.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-02-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-11-add-instructions-command-to-view-and-toggle-custom-instruction-files|Add /instructions command to view and toggle custom instruction files]]
- Later: 2026-02-12 · Codex CLI · [[Changes/Codex CLI/2026-02-12-6-memory-and-personalization-changes-in-rust-v0-101-0|6 Memory and Personalization changes in rust-v0.101.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-12-44d93e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0.md%0ACard%20ID%3A%20codex-cli-2026-02-12-44d93e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.100.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->