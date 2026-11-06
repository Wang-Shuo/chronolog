---
card_id: codex-cli-2026-04-20-761e29
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Model Support: 6 changes in 0.122.0 — Removed
  the stale core `models.json` and updated release preparation to refresh the active
  model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3dad788e39a244cf9b7869579385850f4a6a5b275895627b08b201f79165aa43
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-761e29
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 6 Model Support changes'
  evidence:
  - quote: Removed the stale core `models.json` and updated release preparation to
      refresh the active model catalog (#18585).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18154 fix: model menu pop @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#12640 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18373 Show default reasoning in /status @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18585 Remove unused models.json @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18625 Add `codex debug models` to show model catalog @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-model-support-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-16-gemma-4-on-mlx-added-support-for-running-gemma-4-via-mlx-on-apple-silicon-includ|Gemma
  4 on MLX. Added support for running Gemma 4 via MLX on Apple Silicon…]]'
- '[[Changes/Claude/2026-04-17-claude-design-by-anthropic-labs|Claude Design by Anthropic
  Labs]]'
- '[[Changes/Replit/2026-04-17-claude-opus-4-7-powers-power-mode|Claude Opus 4.7 powers
  Power mode]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Removed the stale core `models.json` and updated release preparation to refresh the active model catalog (#18585).

> #18154 fix: model menu pop @jif-oai

> #12640 Update models.json @github-actions

> #18373 Show default reasoning in /status @aibrahim-oai

> #18585 Remove unused models.json @aibrahim-oai

> #18625 Add `codex debug models` to show model catalog @andmis

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
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
## Nearby in Model Support

- Earlier: 2026-04-17 · Replit · [[Changes/Replit/2026-04-17-claude-opus-4-7-powers-power-mode|Claude Opus 4.7 powers Power mode]]
- Later: 2026-04-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-20-ctrl-t-to-toggle-reasoning-display-is-now-listed-in-the-help-and-overlay|ctrl+t to toggle reasoning display is now listed in the /help and ? overlay]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-761e29&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-6-model-support-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-761e29%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->