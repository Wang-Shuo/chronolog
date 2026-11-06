---
card_id: codex-cli-2026-09-17-e32c02
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Account and Access: 6 changes in 0.155.0 —
  Amazon Bedrock can now obtain AWS credentials from configured commands, with caching…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1267
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eaa3bb40b10545ff3aede27c37e5c9460fee276e8192e68ac2e74033e71b34b5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-e32c02
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 6 Account and Access changes'
  evidence:
  - quote: Amazon Bedrock can now obtain AWS credentials from configured commands,
      with caching, expiration-based refresh, and authentication recovery. (#44028)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: 'MCP servers now report expired OAuth credentials accurately and provide
      reconnect guidance when token refresh fails. (#43947, #44359)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43844 Add staged enterprise OIDC login and coordinated logout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43947 Surface MCP reconnect signals when expired OAuth tokens cannot
      refresh @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44341 Bind remote-control sessions to their authentication owner @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44359 Report OAuth authentication failures in MCP status snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-account-and-access-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-16-2-account-and-access-changes-in-v1-19-0|2 Account
  and Access changes in v1.19.0]]'
- '[[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved
  Claude apps gateway sign-in rate limit errors]]'
- '[[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added
  the signed-in account to Claude apps gateway sign-in]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Amazon Bedrock can now obtain AWS credentials from configured commands, with caching, expiration-based refresh, and authentication recovery. (#44028)

> MCP servers now report expired OAuth credentials accurately and provide reconnect guidance when token refresh fails. (#43947, #44359)

> #43844 Add staged enterprise OIDC login and coordinated logout @copyberry

> #43947 Surface MCP reconnect signals when expired OAuth tokens cannot refresh @copyberry

> #44341 Bind remote-control sessions to their authentication owner @copyberry

> #44359 Report OAuth authentication failures in MCP status snapshots @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Context Window
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-17-96-other-changes-in-rust-v0-155-0|96 other changes in rust-v0.155.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added the signed-in account to Claude apps gateway sign-in]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed plugin commands load organization marketplace policy with environment…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-e32c02&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-6-account-and-access-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-e32c02%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->