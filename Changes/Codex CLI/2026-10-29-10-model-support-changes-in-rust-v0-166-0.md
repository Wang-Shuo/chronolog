---
card_id: codex-cli-2026-10-29-7237a7
date: '2026-10-29'
description: 'Codex CLI · 2026-10-29 · Model Support: 10 changes in 0.166.0 — Added
  GPT-6.1 Terra to the bundled, Vertex AI, and Amazon Bedrock model catalogs. (#57293)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1389
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 62a8cd26132fa48662676812d26788e5c53351e4012caa85c4891f90e68226fa
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-29-7237a7
  comparison: ''
  date: '2026-10-29'
  description: 'Codex CLI — 0.166.0: 10 Model Support changes'
  evidence:
  - quote: Added GPT-6.1 Terra to the bundled, Vertex AI, and Amazon Bedrock model
      catalogs. (#57293)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56525 Remove the 1 MiB response limit for explicit model catalogs @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57293 Add GPT-6.1 Terra to model catalogs @BOZHANG-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57325 Add model catalog fields for granular approval templates @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57553 Allow replacing dynamic tools between model steps @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57581 Allow model catalogs to customize approval instruction headings
      @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57585 Replace unavailable image references in model requests @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57770 Respect model catalog origins when selecting Guardian reviewers
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57789 Refresh the model catalog once when Guardian''s default reviewer
      is missing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57839 Preserve reasoning token accounting across resume and fork @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-model-support-changes-in-rust-v0-166-0
  source_release: codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in rust-v0.166.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-10-27-13-model-support-changes-in-v2-2-0|13 Model Support
  changes in v2.2.0]]'
- '[[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add
  configurable prompt cache TTLs per provider/model]]'
- '[[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings):
  use existing model-profile theme aliases]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in rust-v0.166.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in rust-v0.166.0

**Codex CLI** · 2026-10-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.166.0) · from [[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added GPT-6.1 Terra to the bundled, Vertex AI, and Amazon Bedrock model catalogs. (#57293)

> #56525 Remove the 1 MiB response limit for explicit model catalogs @eternal-openai

> #57293 Add GPT-6.1 Terra to model catalogs @BOZHANG-OAI

> #57325 Add model catalog fields for granular approval templates @goodman-oai

> #57553 Allow replacing dynamic tools between model steps @sdcoffey

> #57581 Allow model catalogs to customize approval instruction headings @goodman-oai

> #57585 Replace unavailable image references in model requests @kchainani-oai

> #57770 Respect model catalog origins when selecting Guardian reviewers @ioanbudea-OAI

> #57789 Refresh the model catalog once when Guardian's default reviewer is missing @jif-oai

> #57839 Preserve reasoning token accounting across resume and fork @andrewgu-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.166.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-29-57503-fix-macos-standalone-release-pruning-etraut-openai|♯57503 Fix macOS standalone release pruning @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-29-3-image-generation-changes-in-rust-v0-166-0|3 Image Generation changes in rust-v0.166.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-29-10-developer-workflow-changes-in-rust-v0-166-0|10 Developer Workflow changes in rust-v0.166.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-29-22-apps-and-integrations-changes-in-rust-v0-166-0|22 Apps and Integrations changes in rust-v0.166.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-29-57342-separate-tui-session-resume-preparation-from-activation-bc-openai|♯57342 Separate TUI session resume preparation from activation @bc-openai]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-10-29-12-interface-experience-changes-in-rust-v0-166-0|12 Interface Experience changes in rust-v0.166.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-29-3-editor-experience-changes-in-rust-v0-166-0|3 Editor Experience changes in rust-v0.166.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-29-57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai|♯57542 Add model-gated literature search to standalone web search @rhan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0|10 Safety and Privacy changes in rust-v0.166.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-29-57226-allow-nfs-database-migration-with-shared-file-permissions-dkovalenko-oai|♯57226 Allow NFS database migration with shared file permissions @dkovalenko-oai]] · Collaboration
- [[Changes/Codex CLI/2026-10-29-8-account-and-access-changes-in-rust-v0-166-0|8 Account and Access changes in rust-v0.166.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495 Add paginated channel subscription queries to the local message board @felixxia-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-29-13-context-window-changes-in-rust-v0-166-0|13 Context Window changes in rust-v0.166.0]] · Context Window
- [[Changes/Codex CLI/2026-10-29-173-other-changes-in-rust-v0-166-0|173 other changes in rust-v0.166.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings): use existing model-profile theme aliases]]
- Later: 2026-10-29 · Open WebUI · [[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support changes in v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-29-7237a7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-29-10-model-support-changes-in-rust-v0-166-0.md%0ACard%20ID%3A%20codex-cli-2026-10-29-7237a7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.166.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->