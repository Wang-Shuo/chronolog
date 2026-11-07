---
card_id: claude-code-2026-09-01-eab202
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Account and Access: 2 changes in v2.1.257
  — Improved MCP connection and OAuth debug/error logs so credentials carried in a
  server''s…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2226
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f452f93edb2842fad75a452391d082ca97f3d052cb87af771cf26414be544577
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-eab202
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 2 Account and Access changes'
  evidence:
  - quote: Improved MCP connection and OAuth debug/error logs so credentials carried
      in a server's URL or request headers are redacted
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Changed Claude apps gateway sign-in and token refresh requests to verify
      the gateway's pinned TLS certificate, as the managed settings fetch already
      does
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-account-and-access-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v2.1.257
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-08-29-show-the-specific-authentication-failure-such-as-401-bad-credentials-instead-of|Show
  the specific authentication failure (such as 401 Bad credentials) instead…]]'
- "[[Changes/Open WebUI/2026-08-31-disconnect-oauth-only-where-there-is-oauth-the-disconnect-control-on-a-tool-serv|\U0001F50C
  Disconnect OAuth only where there is OAuth. The disconnect control on a tool…]]"
- '[[Changes/Raycast/2026-08-31-mcp-support-for-servers-that-use-https-redirects-during-oauth|MCP
  : Support for servers that use HTTPS redirects during OAuth]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2.1.257

**Claude Code** · 2026-09-01 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved MCP connection and OAuth debug/error logs so credentials carried in a server's URL or request headers are redacted

> Changed Claude apps gateway sign-in and token refresh requests to verify the gateway's pinned TLS certificate, as the managed settings fetch already does

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
- [[Changes/Claude Code/2026-09-01-7-other-changes-in-v2-1-257|7 other changes in v2.1.257]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-31 · Raycast · [[Changes/Raycast/2026-08-31-mcp-support-for-servers-that-use-https-redirects-during-oauth|MCP : Support for servers that use HTTPS redirects during OAuth]]
- Later: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2 Account and Access changes in rust-v0.152.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-eab202&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-2-account-and-access-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-eab202%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->