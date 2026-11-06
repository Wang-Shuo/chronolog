---
card_id: github-copilot-cli-2026-06-30-1190d0
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Account and Access: MCP OAuth against
  Microsoft Entra servers behind a tenant vanity domain (e.g. Copilot Studio) no longer…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 8ff29cad12e06b25207d59c1941b1b34771194bc8e86fc7eecef9f7354c599d0
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-1190d0
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.67: MCP OAuth against Microsoft Entra servers
    behind a tenant vanity domain (e.g. Copilot Studio) no longer fails to refresh
    or re-authenticate (AADSTS9010010 / AADSTS90023)'
  evidence:
  - quote: MCP OAuth against Microsoft Entra servers behind a tenant vanity domain
      (e.g. Copilot Studio) no longer fails to refresh or re-authenticate (AADSTS9010010
      / AADSTS90023)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.67
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: mcp-oauth-against-microsoft-entra-servers-behind-a-tenant-vanity-domain-e-g-copi
  source_release: github-copilot-cli-2026-06-30-v1-0-67-github-347129452-cdc0d10f
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: MCP OAuth against Microsoft Entra servers behind a tenant vanity domain…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-25-added-a-startup-notice-when-mcp-servers-need-authentication-pointing-at-mcp|Added
  a startup notice when MCP servers need authentication, pointing at /mcp]]'
- '[[Changes/Codex CLI/2026-06-25-macos-authentication-clients-can-honor-system-proxy-pac-and-wpad-settings-when-r|macOS
  authentication clients can honor system proxy, PAC, and WPAD settings…]]'
- '[[Changes/Codex CLI/2026-06-25-added-opt-in-windows-system-proxy-support-for-authentication-including-pac-wpad|Added
  opt-in Windows system proxy support for authentication, including PAC, WPAD…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-67-github-347129452-cdc0d10f|github-copilot-cli-2026-06-30-v1-0-67-github-347129452-cdc0d10f]]'
source_type: github_releases
theme: account-access
title: MCP OAuth against Microsoft Entra servers behind a tenant vanity domain…
type: change
---

<!-- chronolog:begin region="header" -->
# MCP OAuth against Microsoft Entra servers behind a tenant vanity domain…

**GitHub Copilot CLI** · 2026-06-30 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.67) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-67-github-347129452-cdc0d10f|1.0.67]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> MCP OAuth against Microsoft Entra servers behind a tenant vanity domain (e.g. Copilot Studio) no longer fails to refresh or re-authenticate (AADSTS9010010 / AADSTS90023)
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.67
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-add-claude-sonnet-5-as-a-supported-model|Add Claude Sonnet 5 as a supported model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-30-ctrl-q-now-enqueues-the-highlighted-slash-command-argument-completion|Ctrl+Q now enqueues the highlighted slash-command argument completion]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling the sandbox for the rest of the session now takes effect immediately…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent Mode changes in v1.0.67]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-30-allow-tool-calls-to-continue-when-hooks-time-out|Allow tool calls to continue when hooks time out]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-require-session-limits-to-be-at-least-30-ai-credits|Require session limits to be at least 30 AI credits]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-prompt-mode-exit-summary-shows-a-resume-hint-to-continue-the-session|Prompt mode exit summary shows a resume hint to continue the session]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-added-opt-in-windows-system-proxy-support-for-authentication-including-pac-wpad|Added opt-in Windows system proxy support for authentication, including PAC, WPAD…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-6-account-and-access-changes-in-v1-0-66|6 Account and Access changes in v1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-1190d0&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-mcp-oauth-against-microsoft-entra-servers-behind-a-tenant-vanity-domain-e-g-copi.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-1190d0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.67%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->