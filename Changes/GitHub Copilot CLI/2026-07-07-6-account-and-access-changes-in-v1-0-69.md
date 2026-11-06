---
card_id: github-copilot-cli-2026-07-07-79f891
date: '2026-07-07'
description: 'GitHub Copilot CLI · 2026-07-07 · Account and Access: 6 changes in 1.0.69
  — Require Copilot login before ACP authenticate returns success'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1195
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 548ac57d79d933646b902dce030de6c70957c24573dbf6f0f6b7e8ba8cbfd8a4
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-07-79f891
  comparison: ''
  date: '2026-07-07'
  description: 'GitHub Copilot CLI — 1.0.69: 6 Account and Access changes'
  evidence:
  - quote: Require Copilot login before ACP authenticate returns success
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Sign in to MCP servers through the CLI OAuth callback flow
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: OAuth-gated MCP servers now register their tools after reconnect
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Keep CLI authentication working in one-shot sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Show Authenticate for cancelled MCP OAuth requests
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Keep MCP servers in needs-auth after OAuth cancellation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-account-and-access-changes-in-v1-0-69
  source_release: github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v1.0.69
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-06-recover-access-when-an-sso-provider-is-removed|Recover
  access when an SSO provider is removed]]'
- '[[Changes/OpenHands/2026-07-06-3-account-and-access-changes-in-1-9-0|3 Account
  and Access changes in 1.9.0]]'
- '[[Changes/Claude Code/2026-07-07-added-a-warning-when-your-login-is-about-to-expire-so-you-can-re-authenticate-be|Added
  a warning when your login is about to expire, so you can re-authenticate…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v1.0.69
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v1.0.69

**GitHub Copilot CLI** · 2026-07-07 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.69) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|1.0.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Require Copilot login before ACP authenticate returns success

> Sign in to MCP servers through the CLI OAuth callback flow

> OAuth-gated MCP servers now register their tools after reconnect

> Keep CLI authentication working in one-shot sessions

> Show Authenticate for cancelled MCP OAuth requests

> Keep MCP servers in needs-auth after OAuth cancellation

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-07-8-safety-and-privacy-changes-in-v1-0-69|8 Safety and Privacy changes in v1.0.69]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-07-7-developer-workflow-changes-in-v1-0-69|7 Developer Workflow changes in v1.0.69]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-07-6-model-support-changes-in-v1-0-69|6 Model Support changes in v1.0.69]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-07-warn-when-static-context-uses-most-of-the-prompt-budget-and-block-requests-when|Warn when static context uses most of the prompt budget and block requests…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-07-5-reliability-and-performance-changes-in-v1-0-69|5 Reliability and Performance changes in v1.0.69]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-07-3-mobile-and-desktop-changes-in-v1-0-69|3 Mobile and Desktop changes in v1.0.69]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-07-07-2-editor-experience-changes-in-v1-0-69|2 Editor Experience changes in v1.0.69]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-keep-session-resume-working-when-token-timing-includes-fractional-milliseconds|Keep session resume working when token timing includes fractional milliseconds]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-07-07-improve-chronicle-cost-tips-with-more-precise-evidence-backed-recommendations|Improve /chronicle cost-tips with more precise evidence-backed recommendations]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-07-07-double-press-esc-now-interrupts-the-running-main-turn-flushing-queued-messages-o|Double-press Esc now interrupts the running main turn (flushing queued messages)…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-07-5-interface-experience-changes-in-v1-0-69|5 Interface Experience changes in v1.0.69]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-7-apps-and-integrations-changes-in-v1-0-69|7 Apps and Integrations changes in v1.0.69]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-07-24-other-changes-in-v1-0-69|24 other changes in v1.0.69]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-07 · Claude Code · [[Changes/Claude Code/2026-07-07-added-a-warning-when-your-login-is-about-to-expire-so-you-can-re-authenticate-be|Added a warning when your login is about to expire, so you can re-authenticate…]]
- Later: 2026-07-07 · Lovable · [[Changes/Lovable/2026-07-07-sign-in-with-sso-using-your-company-domain-or-provider-id|Sign in with SSO using your company domain or provider ID]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-07-79f891&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-07-6-account-and-access-changes-in-v1-0-69.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-07-79f891%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->