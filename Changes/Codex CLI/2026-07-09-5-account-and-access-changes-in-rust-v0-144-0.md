---
card_id: codex-cli-2026-07-09-91b7a6
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Account and Access: 5 changes in 0.144.0 —
  MCP tools can now request authentication interactively without an experimental opt-in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 754fba51f1449c1938f58515cea9f095ce6400561de213f64a339e5d3d1f9a60
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-91b7a6
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 5 Account and Access changes'
  evidence:
  - quote: MCP tools can now request authentication interactively without an experimental
      opt-in. (#28772)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: 'App-server hosts can provide Codex authentication at runtime and redirect
      successful logins to a hosted page. (#28745, #31274)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: Device-code login warnings now explain how to recognize and stop phishing
      attempts. (#31648)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30292 Serialize shared MCP OAuth credential stores @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#28745 [login] support hosted success redirects @rafael-jac'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-account-and-access-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in rust-v0.144.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5
  Account and Access changes in rust-v0.143.0]]'
- '[[Changes/OpenHands/2026-07-08-feat-track-user-login-timestamps-by-saurya-in-https-github-com-openhands-openhan|feat:
  track user login timestamps]]'
- '[[Changes/ChatGPT/2026-07-09-we-re-deprecating-atlas-as-we-bring-browser-based-agentic-capabilities-into-chat|Retiring
  Atlas]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools can now request authentication interactively without an experimental opt-in. (#28772)

> App-server hosts can provide Codex authentication at runtime and redirect successful logins to a hosted page. (#28745, #31274)

> Device-code login warnings now explain how to recognize and stop phishing attempts. (#31648)

> #30292 Serialize shared MCP OAuth credential stores @stevenlee-oai

> #28745 [login] support hosted success redirects @rafael-jac

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
## Nearby in Account and Access

- Earlier: 2026-07-09 · ChatGPT · [[Changes/ChatGPT/2026-07-09-we-re-deprecating-atlas-as-we-bring-browser-based-agentic-capabilities-into-chat|Retiring Atlas]]
- Later: 2026-07-10 · Claude Code · [[Changes/Claude Code/2026-07-10-gateway-login-now-supports-anthropic-operated-public-gateway-endpoints|Gateway: /login now supports Anthropic-operated public gateway endpoints]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-91b7a6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-5-account-and-access-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-91b7a6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->