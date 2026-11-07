---
card_id: github-copilot-cli-2026-05-23-2c424f
date: '2026-05-23'
description: 'GitHub Copilot CLI · 2026-05-23 · Account and Access: 2 changes in 1.0.52
  — Legacy nested `oauth.clientId` and `oauth.callbackPort` keys in MCP server configs…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1150
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dd0739e814e3e2252e1d2b142e0653f2be8dfa9e4021c93fa3efa034a3a3ef06
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-23-2c424f
  comparison: ''
  date: '2026-05-23'
  description: 'GitHub Copilot CLI — 1.0.52: 2 Account and Access changes'
  evidence:
  - quote: Legacy nested `oauth.clientId` and `oauth.callbackPort` keys in MCP server
      configs are now migrated to the supported `oauthClientId` and `auth.redirectPort`
      keys instead of being silently dropped
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: MCP OAuth re-authentication honors the configured redirectPort
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-account-and-access-changes-in-v1-0-52
  source_release: github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v1.0.52
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-21-2-account-and-access-changes-in-v1-15-7|2 Account
  and Access changes in v1.15.7]]'
- '[[Changes/OpenCode/2026-05-21-added-grok-oauth-sign-in|Added Grok OAuth sign-in]]'
- '[[Changes/OpenCode/2026-05-22-core-let-mcp-oauth-configs-set-a-callback-port-and-include-configured-scopes-in|Core
  Let MCP OAuth configs set a callback port and include configured scopes…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v1.0.52
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v1.0.52

**GitHub Copilot CLI** · 2026-05-23 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.52) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|1.0.52]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Legacy nested `oauth.clientId` and `oauth.callbackPort` keys in MCP server configs are now migrated to the supported `oauthClientId` and `auth.redirectPort` keys instead of being silently dropped

> MCP OAuth re-authentication honors the configured redirectPort

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.52
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-23-automatically-prune-old-process-log-files-from-copilot-logs-at-startup-to-preven|Automatically prune old process log files from ~/.copilot/logs/ at startup…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-2-mobile-and-desktop-changes-in-v1-0-52|2 Mobile and Desktop changes in v1.0.52]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-23-6-interface-experience-changes-in-v1-0-52|6 Interface Experience changes in v1.0.52]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-general-purpose-subagents-use-gpt-5-4-or-gpt-5-5-when-available|General-purpose subagents use GPT-5.4 or GPT-5.5 when available]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-23-2-apps-and-integrations-changes-in-v1-0-52|2 Apps and Integrations changes in v1.0.52]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-23-3-pricing-model-changes-in-v1-0-52|3 Pricing Model changes in v1.0.52]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-23-4-context-window-changes-in-v1-0-52|4 Context Window changes in v1.0.52]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2 Safety and Privacy changes in v1.0.52]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-23-6-other-changes-in-v1-0-52|6 other changes in v1.0.52]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-05-22 · OpenCode · [[Changes/OpenCode/2026-05-22-core-let-mcp-oauth-configs-set-a-callback-port-and-include-configured-scopes-in|Core Let MCP OAuth configs set a callback port and include configured scopes…]]
- Later: 2026-05-26 · Codex CLI · [[Changes/Codex CLI/2026-05-26-2-account-and-access-changes-in-rust-v0-134-0|2 Account and Access changes in rust-v0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-23-2c424f&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-23-2-account-and-access-changes-in-v1-0-52.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-23-2c424f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.52%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->