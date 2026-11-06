---
card_id: codex-cli-2026-09-28-30f6f2
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Account and Access: 8 changes in 0.158.0 —
  Connect to MCP servers that require pre-registered OAuth client secrets, including
  through…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d2129def3f094342e8aef6920f8c1ad4db73df03c6b7be21fcf331b046ba6604
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-30f6f2
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 8 Account and Access changes'
  evidence:
  - quote: Connect to MCP servers that require pre-registered OAuth client secrets,
      including through `codex mcp add --oauth-client-secret`. (#47891)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47447 Extract WebSocket authentication into `codex-websocket-auth` @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47601 Add opt-in WebSocket authentication to exec-server @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47828 Wait for login completion in recommended plugin tests @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47861 Avoid nested read locking when rendering browser sign-in @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47891 Support client secrets for pre-registered MCP OAuth clients @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47927 Use `127.0.0.1` for local login redirects @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48004 Respect configured authentication in the thread manager sample
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-account-and-access-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: account-access
  title: 8 Account and Access changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-25-5-account-and-access-changes-in-rust-v0-157-0|5
  Account and Access changes in rust-v0.157.0]]'
- '[[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added
  /mcp reconnect all in the interactive terminal to retry every MCP server…]]'
- '[[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account
  and Access changes in v2.1.284]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: account-access
title: 8 Account and Access changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Account and Access changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Connect to MCP servers that require pre-registered OAuth client secrets, including through `codex mcp add --oauth-client-secret`. (#47891)

> #47447 Extract WebSocket authentication into `codex-websocket-auth` @euroelessar

> #47601 Add opt-in WebSocket authentication to exec-server @euroelessar

> #47828 Wait for login completion in recommended plugin tests @felixxia-oai

> #47861 Avoid nested read locking when rendering browser sign-in @jif-oai

> #47891 Support client secrets for pre-registered MCP OAuth clients @willwang-openai

> #47927 Use `127.0.0.1` for local login redirects @willwang-openai

> #48004 Respect configured authentication in the thread manager sample @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]]
- Later: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-elevenlabs-cli|ElevenLabs CLI]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-30f6f2&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-8-account-and-access-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-30f6f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->