---
card_id: codex-cli-2026-10-08-bc568a
date: '2026-10-08'
description: 'Codex CLI · 2026-10-08 · Model Support: 11 changes in 0.162.0 — Configure
  live web access and remote compaction capabilities for custom Responses-compatible…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1368
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4d3bc6af96128b319c28e0dccf268eb34e726cb21cbbf5453c77627f3c7aae85
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-08-bc568a
  comparison: ''
  date: '2026-10-08'
  description: 'Codex CLI — 0.162.0: 11 Model Support changes'
  evidence:
  - quote: Configure live web access and remote compaction capabilities for custom
      Responses-compatible model providers. (#50459)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: 'Respect server model and reasoning-summary defaults for new TUI threads
      while retaining explicit launch overrides. (#50013, #50811, #50913)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50013 Honor server model defaults when starting fresh TUI threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50128 Expose the model selected for a running turn''s next step @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50459 Add capability overrides for custom model providers @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50472 Enable Ultrafast service tiers for Amazon Bedrock Astra models
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50727 Show model and reasoning effort near the top of task details @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50811 Honor server reasoning summary defaults in new TUI threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50913 Use server model defaults for connected TUI fresh starts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51157 Enforce required environment skills before model inference @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51235 Remove default model labels from TUI model pickers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-model-support-changes-in-rust-v0-162-0
  source_release: codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in rust-v0.162.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model
  Support changes in rust-v0.161.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-07-model-picker-updates-the-recommended-list-to-prioritize-gpt-6-1-sol-gpt-6-astra|Model
  picker updates the recommended list to prioritize GPT-6.1 Sol, GPT-6…]]'
- '[[Changes/Claude Code/2026-10-08-3-model-support-changes-in-v2-1-295|3 Model Support
  changes in v2.1.295]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in rust-v0.162.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in rust-v0.162.0

**Codex CLI** · 2026-10-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.162.0) · from [[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|0.162.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configure live web access and remote compaction capabilities for custom Responses-compatible model providers. (#50459)

> Respect server model and reasoning-summary defaults for new TUI threads while retaining explicit launch overrides. (#50013, #50811, #50913)

> #50013 Honor server model defaults when starting fresh TUI threads @etraut-openai

> #50128 Expose the model selected for a running turn's next step @sayan-oai

> #50459 Add capability overrides for custom model providers @celia-oai

> #50472 Enable Ultrafast service tiers for Amazon Bedrock Astra models @celia-oai

> #50727 Show model and reasoning effort near the top of task details @etraut-openai

> #50811 Honor server reasoning summary defaults in new TUI threads @etraut-openai

> #50913 Use server model defaults for connected TUI fresh starts @etraut-openai

> #51157 Enforce required environment skills before model inference @anp-oai

> #51235 Remove default model labels from TUI model pickers @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.162.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-08-3-reliability-and-performance-changes-in-rust-v0-162-0|3 Reliability and Performance changes in rust-v0.162.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Context Window
- [[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216 Use the shared text editor for command-center task renaming @bc-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-08-8-interface-experience-changes-in-rust-v0-162-0|8 Interface Experience changes in rust-v0.162.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12 Developer Workflow changes in rust-v0.162.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-08-137-other-changes-in-rust-v0-162-0|137 other changes in rust-v0.162.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-3-model-support-changes-in-v2-1-295|3 Model Support changes in v2.1.295]]
- Later: 2026-10-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-08-add-claude-haiku-5-5-to-model-selection-and-model-completions|Add Claude Haiku 5.5 to model selection and --model completions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-08-bc568a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-08-11-model-support-changes-in-rust-v0-162-0.md%0ACard%20ID%3A%20codex-cli-2026-10-08-bc568a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.162.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->