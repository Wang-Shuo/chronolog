---
card_id: codex-cli-2026-10-29-fdf53f
date: '2026-10-29'
description: 'Codex CLI · 2026-10-29 · Context Window: 13 changes in 0.166.0 — Preserved
  reasoning-token accounting across resume and fork to avoid premature compaction…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f84494e573c6f3eb16fecfca3b9d11b7bdbabae93ef5b7ab07762533b1fb4e6d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-29-fdf53f
  comparison: ''
  date: '2026-10-29'
  description: 'Codex CLI — 0.166.0: 13 Context Window changes'
  evidence:
  - quote: Preserved reasoning-token accounting across resume and fork to avoid premature
      compaction. (#57839)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56477 Move Guardian approval reason caps into context composition @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56493 Move Guardian tool description preparation into context composition
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56514 Preserve tracing context throughout tool dispatch @bkotsopoulos'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56559 Remove Guardian snapshot-specific context helpers @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57181 Add optional names to untrusted additional context @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57238 Exercise V2 spawning in subagent context inheritance tests @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57274 Defer REPL evidence rendering to synchronous context preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57279 Render untrusted additional context as named tool outputs @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57312 Centralize Guardian root context preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57425 Centralize Guardian root context preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57494 Centralize synchronous Guardian context preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57698 Move Guardian context policy and prompts into the reviewer extension
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-context-window-changes-in-rust-v0-166-0
  source_release: codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a
  source_type: github_releases
  theme: context-window
  title: 13 Context Window changes in rust-v0.166.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-27-2-context-window-changes-in-rust-v0-165-0|2 Context
  Window changes in rust-v0.165.0]]'
- '[[Changes/Ollama/2026-10-27-lfm3-https-ollama-com-library-lfm3-a-1-7b-text-model-with-a-256k-token-context-w|lfm3((source
  link) a 1.7B text model with a 256K-token context…]]'
- '[[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window
  changes in v2.2.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a]]'
source_type: github_releases
theme: context-window
title: 13 Context Window changes in rust-v0.166.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Context Window changes in rust-v0.166.0

**Codex CLI** · 2026-10-29 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.166.0) · from [[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preserved reasoning-token accounting across resume and fork to avoid premature compaction. (#57839)

> #56477 Move Guardian approval reason caps into context composition @ioanbudea-OAI

> #56493 Move Guardian tool description preparation into context composition @ioanbudea-OAI

> #56514 Preserve tracing context throughout tool dispatch @bkotsopoulos

> #56559 Remove Guardian snapshot-specific context helpers @felixxia-oai

> #57181 Add optional names to untrusted additional context @akira-oai

> #57238 Exercise V2 spawning in subagent context inheritance tests @tamird

> #57274 Defer REPL evidence rendering to synchronous context preparation @ioanbudea-OAI

> #57279 Render untrusted additional context as named tool outputs @akira-oai

> #57312 Centralize Guardian root context preparation @ioanbudea-OAI

> #57425 Centralize Guardian root context preparation @ioanbudea-OAI

> #57494 Centralize synchronous Guardian context preparation @ioanbudea-OAI

> #57698 Move Guardian context policy and prompts into the reviewer extension @jif-oai

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
- [[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model Support changes in rust-v0.166.0]] · Model Support
- [[Changes/Codex CLI/2026-10-29-57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai|♯57542 Add model-gated literature search to standalone web search @rhan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0|10 Safety and Privacy changes in rust-v0.166.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-29-57226-allow-nfs-database-migration-with-shared-file-permissions-dkovalenko-oai|♯57226 Allow NFS database migration with shared file permissions @dkovalenko-oai]] · Collaboration
- [[Changes/Codex CLI/2026-10-29-8-account-and-access-changes-in-rust-v0-166-0|8 Account and Access changes in rust-v0.166.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495 Add paginated channel subscription queries to the local message board @felixxia-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-29-173-other-changes-in-rust-v0-166-0|173 other changes in rust-v0.166.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-27 · OpenCode · [[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window changes in v2.2.0]]
- Later: 2026-10-29 · Open WebUI · [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-29-fdf53f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-29-13-context-window-changes-in-rust-v0-166-0.md%0ACard%20ID%3A%20codex-cli-2026-10-29-fdf53f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.166.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->