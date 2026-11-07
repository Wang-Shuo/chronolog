---
card_id: codex-cli-2026-04-20-081633
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Developer Workflow: 6 changes in 0.122.0 —
  The TUI can open `/side` conversations for quick side questions, and queued input
  now…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2778
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ae64b4202613fa4b6cfb070a04c68595342739425c4b0f0bcc642d43e9ac2426
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-081633
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 6 Developer Workflow changes'
  evidence:
  - quote: 'The TUI can open `/side` conversations for quick side questions, and queued
      input now supports slash commands and `!` shell prompts while work is running
      (#18190, #18542).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17999 [codex] Make command exec delta tests chunk tolerant @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18135 debug: windows flake @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18261 fix(tui): use BEL for terminal title updates @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17752 [codex] Add marketplace remove command and shared logic @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18542 Queue slash and shell prompts in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-developer-workflow-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-17-2-developer-workflow-changes-in-v1-4-10|2 Developer
  Workflow changes in v1.4.10]]'
- '[[Changes/OpenCode/2026-04-17-3-developer-workflow-changes-in-v1-4-8|3 Developer
  Workflow changes in v1.4.8]]'
- '[[Changes/OpenCode/2026-04-19-terminal-add-a-full-session-option-when-forking-from-the-session-dialog|Terminal
  Add a full-session option when forking from the session dialog]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI can open `/side` conversations for quick side questions, and queued input now supports slash commands and `!` shell prompts while work is running (#18190, #18542).

> #17999 [codex] Make command exec delta tests chunk tolerant @euroelessar

> #18135 debug: windows flake @jif-oai

> #18261 fix(tui): use BEL for terminal title updates @etraut-openai

> #17752 [codex] Add marketplace remove command and shared logic @xli-oai

> #18542 Queue slash and shell prompts in the TUI @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-19 · OpenCode · [[Changes/OpenCode/2026-04-19-terminal-add-a-full-session-option-when-forking-from-the-session-dialog|Terminal Add a full-session option when forking from the session dialog]]
- Later: 2026-04-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-20-2-developer-workflow-changes-in-v1-0-33|2 Developer Workflow changes in v1.0.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-081633&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-081633%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->