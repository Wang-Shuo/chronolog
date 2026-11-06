---
card_id: codex-cli-2026-11-06-6e044d
date: '2026-11-06'
description: 'Codex CLI · 2026-11-06 · Model Support: 7 changes in 0.167.0 — Saved
  chats stay visible after you switch model providers. If a chat can’t resume, you
  can read…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1397
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f070baa9220d4999c4c4de72fb3487b0096a703d9822ea1c2cf463f9dc7d5eda
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-11-06-6e044d
  comparison: ''
  date: '2026-11-06'
  description: 'Codex CLI — 0.167.0: 7 Model Support changes'
  evidence:
  - quote: Saved chats stay visible after you switch model providers. If a chat can’t
      resume, you can read its transcript and prepare an editable prompt to continue
      in a new chat (#58202).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: The `openai-docs` skill recommends the documented replacement when migrating
      away from a deprecated model (#58134).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58134 Prefer documented replacements for deprecation-driven model migrations
      @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58202 Keep chats accessible across model provider changes @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58361 Preserve model metadata origin through runtime resolution @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58405 Add an option to suppress incremental model change announcements
      @chetan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58441 Preserve Apps usage instructions in model catalog messages @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-model-support-changes-in-rust-v0-167-0
  source_release: codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in rust-v0.167.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support
  changes in v0.13.0]]'
- '[[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes
  in 1.19.0]]'
- '[[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli):
  add models command and --list-models flag for model discovery]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in rust-v0.167.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in rust-v0.167.0

**Codex CLI** · 2026-11-06 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.167.0) · from [[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Saved chats stay visible after you switch model providers. If a chat can’t resume, you can read its transcript and prepare an editable prompt to continue in a new chat (#58202).

> The `openai-docs` skill recommends the documented replacement when migrating away from a deprecated model (#58134).

> #58134 Prefer documented replacements for deprecation-driven model migrations @kkahadze-oai

> #58202 Keep chats accessible across model provider changes @abhinav-oai

> #58361 Preserve model metadata origin through runtime resolution @ioanbudea-OAI

> #58405 Add an option to suppress incremental model change announcements @chetan-oai

> #58441 Preserve Apps usage instructions in model catalog messages @goodman-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.167.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-11-06-2-editor-experience-changes-in-rust-v0-167-0|2 Editor Experience changes in rust-v0.167.0]] · Editor Experience
- [[Changes/Codex CLI/2026-11-06-3-search-and-browsing-changes-in-rust-v0-167-0|3 Search and Browsing changes in rust-v0.167.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context Window changes in rust-v0.167.0]] · Context Window
- [[Changes/Codex CLI/2026-11-06-6-developer-workflow-changes-in-rust-v0-167-0|6 Developer Workflow changes in rust-v0.167.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-11-06-4-voice-and-audio-changes-in-rust-v0-167-0|4 Voice and Audio changes in rust-v0.167.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2 Mobile and Desktop changes in rust-v0.167.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5 Account and Access changes in rust-v0.167.0]] · Account and Access
- [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Agent Mode
- [[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13 Interface Experience changes in rust-v0.167.0]] · Interface Experience
- [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0|12 Apps and Integrations changes in rust-v0.167.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-11-06-65-other-changes-in-rust-v0-167-0|65 other changes in rust-v0.167.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-04 · Gemini CLI · [[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli): add models command and --list-models flag for model discovery]]
- Later: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-11-06-6e044d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-11-06-7-model-support-changes-in-rust-v0-167-0.md%0ACard%20ID%3A%20codex-cli-2026-11-06-6e044d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.167.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->