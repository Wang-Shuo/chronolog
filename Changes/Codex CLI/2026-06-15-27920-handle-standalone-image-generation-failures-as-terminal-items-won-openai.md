---
card_id: codex-cli-2026-06-15-8189e9
date: '2026-06-15'
description: 'Codex CLI · 2026-06-15 · Image Generation: #27920 Handle standalone
  image generation failures as terminal items @won-openai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2024-08-08-we-re-rolling-out-the-ability-for-chatgpt-free-users-to-create-up-to-two-images-2c505c|DALL·E
    3 for ChatGPT Free users]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 676
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ac399e420feecefefee291bb3ef5970ce9417f24fe54bb67e27d0c5f849ec61e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-15-8189e9
  comparison: ''
  date: '2026-06-15'
  description: 'Codex CLI — 0.140.0: #27920 Handle standalone image generation failures
    as terminal items @won-openai'
  evidence:
  - quote: '#27920 Handle standalone image generation failures as terminal items @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: 27920-handle-standalone-image-generation-failures-as-terminal-items-won-openai
  source_release: codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb
  source_type: github_releases
  theme: image-generation
  theme_matches:
  - matched_terms:
    - image generation
    score: 120
    theme: image-generation
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  title: '#27920 Handle standalone image generation failures as terminal items @won-openai'
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image
  Generation changes in rust-v0.136.0]]'
- '[[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image
  Generation changes in rust-v0.137.0]]'
- '[[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image
  Generation changes in rust-v0.138.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb]]'
source_type: github_releases
theme: image-generation
title: ♯27920 Handle standalone image generation failures as terminal items @won-openai
type: change
---

<!-- chronolog:begin region="header" -->
# #27920 Handle standalone image generation failures as terminal items @won-openai

**Codex CLI** · 2026-06-15 · [[Themes/image-generation|Image Generation]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.140.0) · from [[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|0.140.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> #27920 Handle standalone image generation failures as terminal items @won-openai
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.140.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-15-27245-image-add-shared-data-url-preparation-utilities-fjord-oai|♯27245 image: add shared data URL preparation utilities @fjord-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-15-27501-codex-expand-hosted-web-search-citation-guidance-yuning-oai|♯27501 codex Expand hosted web search citation guidance @yuning-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-15-3-reliability-and-performance-changes-in-rust-v0-140-0|3 Reliability and Performance changes in rust-v0.140.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-15-2-editor-experience-changes-in-rust-v0-140-0|2 Editor Experience changes in rust-v0.140.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-15-7-context-window-changes-in-rust-v0-140-0|7 Context Window changes in rust-v0.140.0]] · Context Window
- [[Changes/Codex CLI/2026-06-15-added-import-for-selectively-importing-setup-project-configuration-and-recent-ch|Added /import for selectively importing setup, project configuration, and recent…]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-27129-feat-use-provider-defaults-for-memory-models-celia-oai|♯27129 feat: use provider defaults for memory models @celia-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-15-3-interface-experience-changes-in-rust-v0-140-0|3 Interface Experience changes in rust-v0.140.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-35-apps-and-integrations-changes-in-rust-v0-140-0|35 Apps and Integrations changes in rust-v0.140.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-15-5-account-and-access-changes-in-rust-v0-140-0|5 Account and Access changes in rust-v0.140.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]] · Model Support
- [[Changes/Codex CLI/2026-06-15-clarified-contributor-guidance-around-keeping-crate-apis-narrow-and-supporting-l|Clarified contributor guidance around keeping crate APIs narrow and supporting…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-15-6-developer-workflow-changes-in-rust-v0-140-0|6 Developer Workflow changes in rust-v0.140.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-15-2-voice-and-audio-changes-in-rust-v0-140-0|2 Voice and Audio changes in rust-v0.140.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-06-15-121-other-changes-in-rust-v0-140-0|121 other changes in rust-v0.140.0]] · Other changes
- [[Changes/Codex CLI/2026-06-15-added-usage-views-for-daily-weekly-and-cumulative-account-token-activity-27925|Added /usage views for daily, weekly, and cumulative account token activity]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-06-08 · Codex CLI · [[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image Generation changes in rust-v0.138.0]]
- Later: 2026-07-08 · Codex CLI · [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-08-08 · ChatGPT · [[Changes/ChatGPT/2024-08-08-we-re-rolling-out-the-ability-for-chatgpt-free-users-to-create-up-to-two-images-2c505c|DALL·E 3 for ChatGPT Free users]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-15-8189e9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-15-27920-handle-standalone-image-generation-failures-as-terminal-items-won-openai.md%0ACard%20ID%3A%20codex-cli-2026-06-15-8189e9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.140.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->