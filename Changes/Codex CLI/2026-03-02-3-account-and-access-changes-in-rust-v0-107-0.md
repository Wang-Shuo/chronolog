---
card_id: codex-cli-2026-03-02-40dee8
date: '2026-03-02'
description: 'Codex CLI · 2026-03-02 · Account and Access: 3 changes in 0.107.0 —
  ChatGPT accounts that arrive without plan info now handle account reads correctly
  instead…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1068
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9ddd49cc6ad6159c8aecba2059722e632862b28979aed931f9d9762b2e0d34cc
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-02-40dee8
  comparison: ''
  date: '2026-03-02'
  description: 'Codex CLI — 0.107.0: 3 Account and Access changes'
  evidence:
  - quote: ChatGPT accounts that arrive without plan info now handle account reads
      correctly instead of triggering repeated login issues. (#13072)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: MCP OAuth login flows now forward configured `oauth_resource` values correctly
      for servers that require a `resource` parameter. (#12866)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12866 Add oauth_resource handling for MCP login flows @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-account-and-access-changes-in-rust-v0-107-0
  source_release: codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in rust-v0.107.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-02-27-3-account-and-access-changes-in-v0-31-0|3 Account
  and Access changes in v0.31.0]]'
- '[[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added
  manual URL paste fallback during MCP OAuth authentication]]'
- '[[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account
  and Access changes in v0.8.6]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in rust-v0.107.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in rust-v0.107.0

**Codex CLI** · 2026-03-02 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.107.0) · from [[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ChatGPT accounts that arrive without plan info now handle account reads correctly instead of triggering repeated login issues. (#13072)

> MCP OAuth login flows now forward configured `oauth_resource` values correctly for servers that require a `resource` parameter. (#12866)

> #12866 Add oauth_resource handling for MCP login flows @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.107.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-02-2-multimodal-input-changes-in-rust-v0-107-0|2 Multimodal Input changes in rust-v0.107.0]] · Multimodal Input
- [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0|3 Apps and Integrations changes in rust-v0.107.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Model Support
- [[Changes/Codex CLI/2026-03-02-3-editor-experience-changes-in-rust-v0-107-0|3 Editor Experience changes in rust-v0.107.0]] · Editor Experience
- [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-02-5-voice-and-audio-changes-in-rust-v0-107-0|5 Voice and Audio changes in rust-v0.107.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-02-24-other-changes-in-rust-v0-107-0|24 other changes in rust-v0.107.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-01 · Open WebUI · [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]]
- Later: 2026-03-03 · OpenCode · [[Changes/OpenCode/2026-03-03-normalize-trailing-slashes-in-auth-login-urls|Normalize trailing slashes in auth login URLs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-02-40dee8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-02-3-account-and-access-changes-in-rust-v0-107-0.md%0ACard%20ID%3A%20codex-cli-2026-03-02-40dee8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.107.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->