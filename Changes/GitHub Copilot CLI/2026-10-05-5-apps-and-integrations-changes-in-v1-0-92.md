---
card_id: github-copilot-cli-2026-10-05-f74e7c
date: '2026-10-05'
description: 'GitHub Copilot CLI · 2026-10-05 · Apps and Integrations: 5 changes in
  1.0.92 — Entra-protected MCP servers can silently renew access-token-only credentials.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d8bdd8da3e96c9ab0f56841714849496b3b7a95ff3bdcb88e2a5968fce7ed1c3
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-05-f74e7c
  comparison: ''
  date: '2026-10-05'
  description: 'GitHub Copilot CLI — 1.0.92: 5 Apps and Integrations changes'
  evidence:
  - quote: Entra-protected MCP servers can silently renew access-token-only credentials.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.92
  - quote: Legacy HTTP+SSE MCP connections no longer hang indefinitely when a message
      POST is never acknowledged; the acknowledgement is bounded by the server's configured
      timeout
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.92
  - quote: MCP tools recover within the same turn when server instructions change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.92
  - quote: Reconnect to remote MCP servers after idle Streamable HTTP sessions expire
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.92
  - quote: Improve startup responsiveness when connecting many MCP servers at once
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.92
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-apps-and-integrations-changes-in-v1-0-92
  source_release: github-copilot-cli-2026-10-05-v1-0-92-github-404054639-a6ba3455
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v1.0.92
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-03-2-apps-and-integrations-changes-in-v2-1-289|2
  Apps and Integrations changes in v2.1.289]]'
- '[[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14
  Apps and Integrations changes in v2.1.290]]'
- '[[Changes/Codex CLI/2026-10-05-2-apps-and-integrations-changes-in-rust-v0-160-1|2
  Apps and Integrations changes in rust-v0.160.1]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-05-v1-0-92-github-404054639-a6ba3455|github-copilot-cli-2026-10-05-v1-0-92-github-404054639-a6ba3455]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v1.0.92
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v1.0.92

**GitHub Copilot CLI** · 2026-10-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.92) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-05-v1-0-92-github-404054639-a6ba3455|1.0.92]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Entra-protected MCP servers can silently renew access-token-only credentials.

> Legacy HTTP+SSE MCP connections no longer hang indefinitely when a message POST is never acknowledged; the acknowledgement is bounded by the server's configured timeout

> MCP tools recover within the same turn when server instructions change

> Reconnect to remote MCP servers after idle Streamable HTTP sessions expire

> Improve startup responsiveness when connecting many MCP servers at once

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.92
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-05-4-safety-and-privacy-changes-in-v1-0-92|4 Safety and Privacy changes in v1.0.92]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-10-05-4-developer-workflow-changes-in-v1-0-92|4 Developer Workflow changes in v1.0.92]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-05-2-context-window-changes-in-v1-0-92|2 Context Window changes in v1.0.92]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-10-05-2-model-support-changes-in-v1-0-92|2 Model Support changes in v1.0.92]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-10-05-plan-usage-reflects-the-current-billing-period-after-quota-resets|Plan usage reflects the current billing period after quota resets]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-10-05-add-a-pre-conversation-ctrl-e-environment-picker-to-switch-between-local-and-clo|Add a pre-conversation Ctrl+E environment picker to switch between local and cloud runs]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-10-05-voice-runtime-install-errors-name-why-the-download-from-nuget-org-failed-not-onl|Voice runtime install errors name why the download from nuget.org failed, not only…]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-10-05-2-editor-experience-changes-in-v1-0-92|2 Editor Experience changes in v1.0.92]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-10-05-canvas-actions-can-now-return-images-to-the-model-in-invoke-canvas-action|Canvas actions can now return images to the model in invoke_canvas_action]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-10-05-remote-session-resume-now-uses-your-configured-github-auth-for-resume-and-connec|Remote session resume now uses your configured GitHub auth for --resume and --connect]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-10-05-3-account-and-access-changes-in-v1-0-92|3 Account and Access changes in v1.0.92]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-10-05-sandboxed-commands-on-windows-write-temporary-files-to-the-granted-temp-director|Sandboxed commands on Windows write temporary files to the granted temp directory…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-10-05-7-other-changes-in-v1-0-92|7 other changes in v1.0.92]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-05 · Codex CLI · [[Changes/Codex CLI/2026-10-05-2-apps-and-integrations-changes-in-rust-v0-160-1|2 Apps and Integrations changes in rust-v0.160.1]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-05-f74e7c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-05-5-apps-and-integrations-changes-in-v1-0-92.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-05-f74e7c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.92%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->