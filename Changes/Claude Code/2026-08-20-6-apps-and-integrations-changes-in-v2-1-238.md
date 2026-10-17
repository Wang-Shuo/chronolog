---
card_id: claude-code-2026-08-20-0f55a4
date: '2026-08-20'
description: 'Claude Code · 2026-08-20 · Apps and Integrations: 6 changes in v2.1.238
  — Plugin marketplaces: `headersHelper` on a url marketplace or a catalog entry runs
  a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 576f7803e8677bb00bbf1cc46e1615a5faa53816ffc7111aa2a56848f5c3904d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-20-0f55a4
  comparison: ''
  date: '2026-08-20'
  description: 'Claude Code — v2.1.238: 6 Apps and Integrations changes'
  evidence:
  - quote: 'Plugin marketplaces: `headersHelper` on a url marketplace or a catalog
      entry runs a command that mints HTTP headers (e.g. a short-lived token) for
      catalog and same-origin archive fetches'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: A catalog entry's `headersHelper` runs only when you install or update
      that plugin, after its command is shown; `claude plugin install/update` ask
      `[y/N]` (or pass `-y`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: 'Improved Remote Control connection resilience: brief HTTP 403 refusals
      from a network edge, VPN, or proxy are now tolerated for up to 3 minutes, with
      the refusing party named when a block persists'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: Changed `claude mcp list` and `claude mcp get` to show disabled servers
      as `⊘ Disabled` instead of connecting to them for a health check
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: MCP `headersHelper` in a project `.mcp.json`, and inline MCP servers in
      project or `--add-dir` agent files, now require that folder's trust dialog to
      have been accepted (also under `claude -p`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: MCP `headersHelper` from a project `.mcp.json`, plugin, or agent file runs
      without inherited credential env vars; user, managed and claude.ai-scope helpers
      now run from the Claude config dir
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-238
  source_release: claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.238
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-17-settings|Settings]]'
- '[[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM
  in print/SDK mode no longer records an interrupted turn or synthetic tool…]]'
- '[[Changes/ChatGPT/2026-08-20-use-apple-messages-from-codex-and-chatgpt-work-on-apple-silicon-macs-the-apple-m|Use
  Apple Messages from Codex and ChatGPT Work]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.238
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.238

**Claude Code** · 2026-08-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) · from [[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|v2.1.238]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin marketplaces: `headersHelper` on a url marketplace or a catalog entry runs a command that mints HTTP headers (e.g. a short-lived token) for catalog and same-origin archive fetches

> A catalog entry's `headersHelper` runs only when you install or update that plugin, after its command is shown; `claude plugin install/update` ask `[y/N]` (or pass `-y`)

> Improved Remote Control connection resilience: brief HTTP 403 refusals from a network edge, VPN, or proxy are now tolerated for up to 3 minutes, with the refusing party named when a block persists

> Changed `claude mcp list` and `claude mcp get` to show disabled servers as `⊘ Disabled` instead of connecting to them for a health check

> MCP `headersHelper` in a project `.mcp.json`, and inline MCP servers in project or `--add-dir` agent files, now require that folder's trust dialog to have been accepted (also under `claude -p`)

> MCP `headersHelper` from a project `.mcp.json`, plugin, or agent file runs without inherited credential env vars; user, managed and claude.ai-scope helpers now run from the Claude config dir

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-20-updated-the-bundled-claude-api-skill-for-the-managed-agents-aug-19-release-web-s|Updated the bundled claude-api skill for the Managed Agents Aug 19 release]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer Workflow changes in v2.1.238]] · Developer Workflow
- [[Changes/Claude Code/2026-08-20-improved-startup-bare-claude-starts-sooner-on-macos|Improved startup: bare claude starts sooner on macOS]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-20-improved-startup-responsiveness-the-automatic-update-check-now-runs-about-10-sec|Improved startup responsiveness]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-20-changed-ctrl-l-and-cmd-k-in-fullscreen-to-always-just-repaint-the-double-press-c|Changed Ctrl+L and Cmd+K in fullscreen to always just repaint]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-20 · ChatGPT · [[Changes/ChatGPT/2026-08-20-use-apple-messages-from-codex-and-chatgpt-work-on-apple-silicon-macs-the-apple-m|Use Apple Messages from Codex and ChatGPT Work]]
- Later: 2026-08-21 · ChatGPT · [[Changes/ChatGPT/2026-08-21-updated-plugin-recommendations-make-it-easier-to-find-tools-people-continue-to-u|Updated plugin recommendations make it easier to find tools people continue to use]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-20-0f55a4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-20-6-apps-and-integrations-changes-in-v2-1-238.md%0ACard%20ID%3A%20claude-code-2026-08-20-0f55a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.238%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->