---
card_id: codex-cli-2026-07-21-d9e704
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Account and Access: 9 changes in 0.145.0 —
  Prevented slow or conflicting MCP startup and authentication flows by enforcing
  startup…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1209
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6da29ae6365792ff6499397bfd8728bacff394e0347eee106555327df8b38526
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-d9e704
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 9 Account and Access changes'
  evidence:
  - quote: 'Prevented slow or conflicting MCP startup and authentication flows by
      enforcing startup timeouts, avoiding blocking OAuth discovery, serializing refreshes,
      and reusing tool catalogs safely. (#32229, #32781, #32825, #33184, #33297)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31637 login: route raw auth flows through HTTP client @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#30293 Resolve and pin MCP OAuth credential stores @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31327 feat: add managed Bedrock login API @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32229 Serialize MCP OAuth credential refreshes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32801 Refactor OAuth store lock contention tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32825 Avoid blocking thread startup on MCP OAuth discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33040 Send plugin analytics with API key authentication @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33170 Support Amazon Bedrock login in the app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-account-and-access-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: account-access
  title: 9 Account and Access changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-16-server-mode-reconnects-oauth-mcp-servers-from-cached-tokens|Server
  mode reconnects OAuth MCP servers from cached tokens]]'
- '[[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated
  the auth status panel title from "Cloud authentication" to "Authentication"]]'
- '[[Changes/Claude Code/2026-07-21-changed-the-login-expiry-warning-to-appear-3-days-before-expiry-instead-of-5|Changed
  the login-expiry warning to appear 3 days before expiry instead of 5]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: account-access
title: 9 Account and Access changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Account and Access changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Prevented slow or conflicting MCP startup and authentication flows by enforcing startup timeouts, avoiding blocking OAuth discovery, serializing refreshes, and reusing tool catalogs safely. (#32229, #32781, #32825, #33184, #33297)

> #31637 login: route raw auth flows through HTTP client @bolinfest

> #30293 Resolve and pin MCP OAuth credential stores @stevenlee-oai

> #31327 feat: add managed Bedrock login API @celia-oai

> #32229 Serialize MCP OAuth credential refreshes @copyberry

> #32801 Refactor OAuth store lock contention tests @copyberry

> #32825 Avoid blocking thread startup on MCP OAuth discovery @copyberry

> #33040 Send plugin analytics with API key authentication @copyberry

> #33170 Support Amazon Bedrock login in the app server @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Model Support
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-changed-the-login-expiry-warning-to-appear-3-days-before-expiry-instead-of-5|Changed the login-expiry warning to appear 3 days before expiry instead of 5]]
- Later: 2026-07-29 · Codex CLI · [[Changes/Codex CLI/2026-07-29-34643-migrate-login-http-construction-to-httpclient-copyberry|♯34643 Migrate login HTTP construction to HttpClient @copyberry]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-d9e704&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-9-account-and-access-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-d9e704%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->