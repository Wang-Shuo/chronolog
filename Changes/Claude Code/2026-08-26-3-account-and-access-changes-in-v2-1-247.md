---
card_id: claude-code-2026-08-26-c699bd
date: '2026-08-26'
description: 'Claude Code · 2026-08-26 · Account and Access: 3 changes in v2.1.247
  — Changed analytics to stay off from startup, not only after login, when managed
  settings…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2220
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3711bb47de518623b9e6e4115884e5497e6848b01638f837cab9c81be8304463
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-26-c699bd
  comparison: ''
  date: '2026-08-26'
  description: 'Claude Code — v2.1.247: 3 Account and Access changes'
  evidence:
  - quote: Changed analytics to stay off from startup, not only after login, when
      managed settings force gateway login or a custom OAuth deployment is configured
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Changed Claude apps gateway sign-in requests to identify Claude Code (a
      `surface=claude_code` device-authorization parameter and a `claude-code/<version>`
      User-Agent)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Changed organization sign-in enforcement to exit at start when the administrator's
      managed settings cannot be read, even if host-supplied or per-user Windows registry
      settings exist
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-account-and-access-changes-in-v2-1-247
  source_release: claude-code-2026-08-26-v2-1-247-github-377320078-fc507178
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v2.1.247
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account
  and Access changes in v0.11.1]]'
- '[[Changes/Raycast/2026-08-25-mcp-added-loopback-oauth-redirects-so-mcp-providers-that-reject-custom-url-schem|MCP
  : Added loopback OAuth redirects so MCP providers that reject custom URL…]]'
- '[[Changes/Raycast/2026-08-25-mcp-added-loopback-oauth-redirects-so-mcp-providers-that-reject-custom-url-schem-c73eec|MCP
  : Added loopback OAuth redirects so MCP providers that reject custom URL…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|claude-code-2026-08-26-v2-1-247-github-377320078-fc507178]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v2.1.247
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v2.1.247

**Claude Code** · 2026-08-26 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) · from [[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed analytics to stay off from startup, not only after login, when managed settings force gateway login or a custom OAuth deployment is configured

> Changed Claude apps gateway sign-in requests to identify Claude Code (a `surface=claude_code` device-authorization parameter and a `claude-code/<version>` User-Agent)

> Changed organization sign-in enforcement to exit at start when the administrator's managed settings cannot be read, even if host-supplied or per-user Windows registry settings exist

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] · Model Support
- [[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed terminal hyperlinks in rendered markdown]] · Developer Workflow
- [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-26-changed-the-prompt-footer-pr-badge-to-skip-its-github-re-check-on-terminal-refoc|Changed the prompt-footer PR badge to skip its GitHub re-check on terminal refocus…]] · Interface Experience
- [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]] · Context Window
- [[Changes/Claude Code/2026-08-26-4-other-changes-in-v2-1-247|4 other changes in v2.1.247]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-25 · Raycast · [[Changes/Raycast/2026-08-25-mcp-added-loopback-oauth-redirects-so-mcp-providers-that-reject-custom-url-schem-c73eec|MCP : Added loopback OAuth redirects so MCP providers that reject custom URL…]]
- Later: 2026-08-26 · Codex CLI · [[Changes/Codex CLI/2026-08-26-2-account-and-access-changes-in-rust-v0-150-0|2 Account and Access changes in rust-v0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-26-c699bd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-26-3-account-and-access-changes-in-v2-1-247.md%0ACard%20ID%3A%20claude-code-2026-08-26-c699bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.247%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->