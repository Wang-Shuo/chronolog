---
card_id: codex-cli-2026-07-09-5bf987
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Apps and Integrations: 11 changes in 0.144.0
  — Long-running app sessions now refresh expired authentication for the hosted…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1204
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 09b788331137439774e94b23d8991a14a3ecdaa5b18aac626ab27e935e27cee8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-5bf987
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 11 Apps and Integrations changes'
  evidence:
  - quote: Long-running app sessions now refresh expired authentication for the hosted
      `codex_apps` connector. (#31486)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: Reduced plugin skill-loading time on remote executors by resolving namespaces
      once per root. (#31348)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31369 test(skills): cover plugin namespace loading @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31319 [codex] add connector runtime latency metrics @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31348 perf(skills): resolve plugin namespaces per root @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31518 Log plugin install failure subtypes @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31612 Round MCP timeout durations in error messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31622 websocket-client: add proxy-aware connector @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31292 Reuse MCP tool snapshot within a sampling request @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31330 [codex-apps] Omit internal fields from file payloads @jacobzhou-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31486 [connectors] Refresh codex_apps /ps/mcp auth @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.144.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-07-08-chore-bump-sdk-packages-to-v1-33-0-by-all-hands-bot-in-https-github-com-openhand|chore:
  bump SDK packages to v1.33.0]]'
- '[[Changes/ChatGPT/2026-07-09-we-re-also-replacing-the-app-directory-with-the-plugin-directory-existing-app-co|We’re
  also replacing the App Directory with the Plugin Directory]]'
- '[[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills
  are now generally available]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Long-running app sessions now refresh expired authentication for the hosted `codex_apps` connector. (#31486)

> Reduced plugin skill-loading time on remote executors by resolving namespaces once per root. (#31348)

> #31369 test(skills): cover plugin namespace loading @anp-oai

> #31319 [codex] add connector runtime latency metrics @mzeng-openai

> #31348 perf(skills): resolve plugin namespaces per root @anp-oai

> #31518 Log plugin install failure subtypes @charlesgong-openai

> #31612 Round MCP timeout durations in error messages @jif-oai

> #31622 websocket-client: add proxy-aware connector @bolinfest

> #31292 Reuse MCP tool snapshot within a sampling request @sayan-oai

> #31330 [codex-apps] Omit internal fields from file payloads @jacobzhou-oai

> #31486 [connectors] Refresh codex_apps /ps/mcp auth @stevenlee-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s|Responses WebSockets continue using the low-latency transport while respecting…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Model Support
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-09-43-other-changes-in-rust-v0-144-0|43 other changes in rust-v0.144.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-09 · ChatGPT · [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills are now generally available]]
- Later: 2026-07-09 · Lovable · [[Changes/Lovable/2026-07-09-app-connectors-dbt-semantic-layer-and-clickhouse|App connectors: dbt Semantic Layer and ClickHouse]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-5bf987&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-5bf987%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->