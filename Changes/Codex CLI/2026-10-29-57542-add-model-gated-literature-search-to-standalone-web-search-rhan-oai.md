---
card_id: codex-cli-2026-10-29-9f0c99
date: '2026-10-29'
description: 'Codex CLI · 2026-10-29 · Search and Browsing: #57542 Add model-gated
  literature search to standalone web search @rhan-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1316
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 9e2a63d53fcf80d37a5213a0c3fc7af562886fc7fb6a4cc92d2f9d9c42a887e5
product: codex-cli
product_name: Codex CLI
record:
  ai_generated: true
  card_id: codex-cli-2026-10-29-9f0c99
  comparison: ''
  confidence: low
  date: '2026-10-29'
  description: 'Codex CLI — 0.166.0: #57542 Add model-gated literature search to standalone
    web search @rhan-oai'
  evidence:
  - quote: '#57542 Add model-gated literature search to standalone web search @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: 57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai
  source_release: codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a
  source_type: github_releases
  theme: search-browsing
  theme_matches:
  - matched_terms:
    - web search
    score: 60
    theme: search-browsing
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: '#57542 Add model-gated literature search to standalone web search @rhan-oai'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed
  the interactive session''s WebSearch budget to refill over time (100 calls/hour]]'
- '[[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3
  Search and Browsing changes in rust-v0.161.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-19-2-search-and-browsing-changes-in-v1-0-100|2
  Search and Browsing changes in v1.0.100]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a]]'
source_type: github_releases
theme: search-browsing
title: ♯57542 Add model-gated literature search to standalone web search @rhan-oai
type: change
---

<!-- chronolog:begin region="header" -->
# #57542 Add model-gated literature search to standalone web search @rhan-oai

**Codex CLI** · 2026-10-29 · [[Themes/search-browsing|Search and Browsing]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.166.0) · from [[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> #57542 Add model-gated literature search to standalone web search @rhan-oai
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.166.0
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
## Nearby in Search and Browsing

- Earlier: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-2-search-and-browsing-changes-in-v1-0-100|2 Search and Browsing changes in v1.0.100]]
- Later: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-3-search-and-browsing-changes-in-rust-v0-167-0|3 Search and Browsing changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-29-9f0c99&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-29-57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai.md%0ACard%20ID%3A%20codex-cli-2026-10-29-9f0c99%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.166.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->