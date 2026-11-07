---
card_id: codex-cli-2026-07-09-db2e83
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Safety and Privacy: 4 changes in 0.144.0 —
  Windows sandbox sessions can delete files in writable roots and access the managed
  primary…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 82d0df8b1e212d5194be3764457950efff5e910f5928bdbb4eac87dc77b5add6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-db2e83
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 4 Safety and Privacy changes'
  evidence:
  - quote: 'Windows sandbox sessions can delete files in writable roots and access
      the managed primary runtime. (#31138, #31574)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30879 Handle mixed-case URLs in Windows command safety @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31138 fix(windows-sandbox): allow deletion in writable roots @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31574 [codex] Grant Windows sandbox access to primary runtime @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-safety-and-privacy-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in rust-v0.144.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background
  task notifications now explicitly state that no human input has occurred…]]'
- '[[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13
  Safety and Privacy changes in rust-v0.143.0]]'
- '[[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On
  desktop, Work can use local files and desktop apps with your permission]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows sandbox sessions can delete files in writable roots and access the managed primary runtime. (#31138, #31574)

> #30879 Handle mixed-case URLs in Windows command safety @charliemarsh-oai

> #31138 fix(windows-sandbox): allow deletion in writable roots @fcoury-oai

> #31574 [codex] Grant Windows sandbox access to primary runtime @abhinav-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s|Responses WebSockets continue using the low-latency transport while respecting…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Model Support
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-09-43-other-changes-in-rust-v0-144-0|43 other changes in rust-v0.144.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-09 · ChatGPT · [[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On desktop, Work can use local files and desktop apps with your permission]]
- Later: 2026-07-10 · Claude Code · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-db2e83&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-db2e83%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->