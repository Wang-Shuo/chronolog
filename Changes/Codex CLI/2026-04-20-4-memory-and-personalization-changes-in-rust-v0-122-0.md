---
card_id: codex-cli-2026-04-20-95900a
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Memory and Personalization: 4 changes in 0.122.0
  — Several TUI rough edges were fixed, including fatal skills-list failures, invalid…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1005
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e6230c105e235fe2369b2557ef265bc534e06982af9a9014bd4a80625bf9b9b7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-95900a
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 4 Memory and Personalization changes'
  evidence:
  - quote: 'Several TUI rough edges were fixed, including fatal skills-list failures,
      invalid resume hints, duplicate context statusline entries, `/model` menu loops,
      redundant memory notices, and terminal title quoting in iTerm2 (#18061, #18059,
      #18054, #18154, #18580, #18261).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18137 nit: add min values for memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18134 chore: unify memory drop endpoints @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18580 Avoid redundant memory enable notice @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-memory-and-personalization-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: memory
  title: 4 Memory and Personalization changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0|9
  Memory and Personalization changes in rust-v0.121.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-custom-instructions-and-skills-refresh-from-disk-after-clear-or-new|Custom
  instructions and skills refresh from disk after /clear or /new]]'
- '[[Changes/OpenCode/2026-04-16-core-the-bash-tool-uses-less-memory-on-large-command-output|Core
  The bash tool uses less memory on large command output]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: memory
title: 4 Memory and Personalization changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Several TUI rough edges were fixed, including fatal skills-list failures, invalid resume hints, duplicate context statusline entries, `/model` menu loops, redundant memory notices, and terminal title quoting in iTerm2 (#18061, #18059, #18054, #18154, #18580, #18261).

> #18137 nit: add min values for memories @jif-oai

> #18134 chore: unify memory drop endpoints @jif-oai

> #18580 Avoid redundant memory enable notice @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-16 · OpenCode · [[Changes/OpenCode/2026-04-16-core-the-bash-tool-uses-less-memory-on-large-command-output|Core The bash tool uses less memory on large command output]]
- Later: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-95900a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-95900a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->