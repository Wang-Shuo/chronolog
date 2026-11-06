---
card_id: github-copilot-cli-2026-09-22-f104e8
date: '2026-09-22'
description: 'GitHub Copilot CLI · 2026-09-22 · Apps and Integrations: 6 changes in
  1.0.88 — Deferred MCP tools whose registered name needed sanitizing or shortening
  are now…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1279
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 711aa2cfc03a33f10eeea78a07d346972e4dbaf1eb2686d43304710799c1449d
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-22-f104e8
  comparison: ''
  date: '2026-09-22'
  description: 'GitHub Copilot CLI — 1.0.88: 6 Apps and Integrations changes'
  evidence:
  - quote: Deferred MCP tools whose registered name needed sanitizing or shortening
      are now listed under that name, so tool search can find them, and deferred MCP
      tools with no resolvable server name are now listed with the other tools instead
      of being left out of the reminder
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Agents from a plugin mounted with --plugin-dir now appear in server-mode
      sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Session and subagent start hooks combine successful additional-context
      contributions within the hook-output limit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Cached MCP tools stay scoped to environment-resolved server addresses and
      headers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: MCP and plugin views show server display names and plugin descriptions
      for clearer status.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: Prompt to update GitHub authorization when Connectors need reauthorization
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-apps-and-integrations-changes-in-v1-0-88
  source_release: github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v1.0.88
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8
  Apps and Integrations changes in v1.0.87]]'
- '[[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8
  Apps and Integrations changes in v2.1.280]]'
- '[[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42
  Apps and Integrations changes in rust-v0.156.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v1.0.88
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v1.0.88

**GitHub Copilot CLI** · 2026-09-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.88) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Deferred MCP tools whose registered name needed sanitizing or shortening are now listed under that name, so tool search can find them, and deferred MCP tools with no resolvable server name are now listed with the other tools instead of being left out of the reminder

> Agents from a plugin mounted with --plugin-dir now appear in server-mode sessions

> Session and subagent start hooks combine successful additional-context contributions within the hook-output limit

> Cached MCP tools stay scoped to environment-resolved server addresses and headers

> MCP and plugin views show server display names and plugin descriptions for clearer status.

> Prompt to update GitHub authorization when Connectors need reauthorization

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.88
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-22-in-the-sessions-tab-rows-you-can-dismiss-now-take-x-then-x-again-to-confirm-a-lo|In the Sessions tab, rows you can dismiss now take x then x again to confirm]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-22-2-agent-mode-changes-in-v1-0-88|2 Agent Mode changes in v1.0.88]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-22-add-optional-osc-777-terminal-notifications-for-direct-ghostty-and-wezterm-sessi|Add optional OSC 777 terminal notifications for direct Ghostty and WezTerm sessions]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-22-3-account-and-access-changes-in-v1-0-88|3 Account and Access changes in v1.0.88]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-22-session-resume-preserves-pending-conversation-events-when-saving-fails-and-expla|Session resume preserves pending conversation events when saving fails and explains…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-22-8-other-changes-in-v1-0-88|8 other changes in v1.0.88]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]]
- Later: 2026-09-22 · OpenHands · [[Changes/OpenHands/2026-09-22-test-cover-mcp-config-utilities-by-aivong-openhands-in-https-github-com-openhand|test: cover MCP config utilities]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-22-f104e8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-22-6-apps-and-integrations-changes-in-v1-0-88.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-22-f104e8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.88%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->