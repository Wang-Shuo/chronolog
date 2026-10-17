---
card_id: claude-code-2026-09-29-6b1e05
date: '2026-09-29'
description: 'Claude Code · 2026-09-29 · Apps and Integrations: 14 changes in v2.1.285
  — Added `claude plugin configure <plugin>` to show a plugin''s options and which
  are…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1286
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fcdad393f266392c05f4d4aa981ac67dc6f8dbd05cf5086c76c14f36e805dbb1
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-29-6b1e05
  comparison: ''
  date: '2026-09-29'
  description: 'Claude Code — v2.1.285: 14 Apps and Integrations changes'
  evidence:
  - quote: Added `claude plugin configure <plugin>` to show a plugin's options and
      which are unset, or save new values read from stdin with `--values-stdin`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Added `<server>.<key>=<value>` to `claude plugin install --config`, so
      a bundled `.mcpb` MCP server's own settings can be set at install time and it
      starts without visiting `/plugin` → Configure
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Improved plugin marketplace errors to name why a git address is refused
      instead of citing enterprise policy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Improved validation of git URLs for plugins, marketplaces and the current
      repository's remote
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: 'Improved pictures Claude sends as BMP, HEIC, HEIF, AVIF or TIFF files:
      the Claude apps now show a preview where Claude Code can convert them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: 'Improved SDK liveness during a non-streaming fallback request: with partial
      messages on, a `ping` stream event is now sent every 30 seconds on the Anthropic
      API, Claude Platform on AWS and gateways'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed MCP tools so a tool that sets its own `_meta['anthropic/alwaysLoad']`
      to false stays deferred when its `--mcp-config`, Agent SDK or plugin server
      is set to `alwaysLoad`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: 'Changed the MCP server name `widgets` to be reserved in cloud sessions
      and on self-hosted runners: your own server under it, or a close spelling such
      as `widgets_`, no longer loads, so rename it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `claude mcp get` to hide the command, arguments, and environment
      values of stdio MCP servers provided by plugins; variable names are still shown
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `/claude-api` so it can no longer be run from Remote Control clients
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: '[VSCode] Added a plugin options form to Manage plugins: installing a plugin
      that has options asks for the unset ones, and a gear on its row changes them
      later'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: '[VSCode] Improved the Manage plugins dialog: a failed plugin action now
      opens a popup that explains it and, where there is one, offers the fix'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: '[VSCode] Changed the Manage plugins dialog to ask before removing a marketplace
      or turning off a plugin that your project''s shared `.claude/settings.json`
      turns on'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: '[Cloud sessions] Changed `MCP_DISCOVERY_CACHE=1`, when set in your cloud
      environment''s variables rather than a settings file, to reuse your connectors''
      tool lists after a session restart; other MCP servers are no longer cached and
      connect at startup'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 14-apps-and-integrations-changes-in-v2-1-285
  source_release: claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in v2.1.285
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-plugins-can-now-include-interactive-panels-sidebar-views-and-viewers-or-editors-d0bd7e|Work
  with interactive plugin extensions]]'
- '[[Changes/ChatGPT/2026-09-29-we-re-making-it-easier-to-bring-meeting-context-into-chatgpt-so-you-can-act-on-n|We’re
  making it easier to bring meeting context into ChatGPT so you can act on next…]]'
- '[[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start
  automations from connected-app events]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in v2.1.285
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in v2.1.285

**Claude Code** · 2026-09-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) · from [[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude plugin configure <plugin>` to show a plugin's options and which are unset, or save new values read from stdin with `--values-stdin`

> Added `<server>.<key>=<value>` to `claude plugin install --config`, so a bundled `.mcpb` MCP server's own settings can be set at install time and it starts without visiting `/plugin` → Configure

> Improved plugin marketplace errors to name why a git address is refused instead of citing enterprise policy

> Improved validation of git URLs for plugins, marketplaces and the current repository's remote

> Improved pictures Claude sends as BMP, HEIC, HEIF, AVIF or TIFF files: the Claude apps now show a preview where Claude Code can convert them

> Improved SDK liveness during a non-streaming fallback request: with partial messages on, a `ping` stream event is now sent every 30 seconds on the Anthropic API, Claude Platform on AWS and gateways

> Changed MCP tools so a tool that sets its own `_meta['anthropic/alwaysLoad']` to false stays deferred when its `--mcp-config`, Agent SDK or plugin server is set to `alwaysLoad`

> Changed the MCP server name `widgets` to be reserved in cloud sessions and on self-hosted runners: your own server under it, or a close spelling such as `widgets_`, no longer loads, so rename it

> Changed `claude mcp get` to hide the command, arguments, and environment values of stdio MCP servers provided by plugins; variable names are still shown

> Changed `/claude-api` so it can no longer be run from Remote Control clients

> [VSCode] Added a plugin options form to Manage plugins: installing a plugin that has options asks for the unset ones, and a gear on its row changes them later

> [VSCode] Improved the Manage plugins dialog: a failed plugin action now opens a popup that explains it and, where there is one, offers the fix

> [VSCode] Changed the Manage plugins dialog to ask before removing a marketplace or turning off a plugin that your project's shared `.claude/settings.json` turns on

> [Cloud sessions] Changed `MCP_DISCOVERY_CACHE=1`, when set in your cloud environment's variables rather than a settings file, to reuse your connectors' tool lists after a session restart; other MCP servers are no longer cached and connect at startup

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Context Window
- [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-29-6-mobile-and-desktop-changes-in-v2-1-285|6 Mobile and Desktop changes in v2.1.285]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-29-improved-responsiveness-when-leaving-the-ctrl-o-transcript-view-in-long-sessions|Improved responsiveness when leaving the ctrl+o transcript view in long sessions…]] · Interface Experience
- [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Model Support
- [[Changes/Claude Code/2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac|Fixed the PowerShell tool's permission check skipping deny and ask rules…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]] · Account and Access
- [[Changes/Claude Code/2026-09-29-2-editor-experience-changes-in-v2-1-285|2 Editor Experience changes in v2.1.285]] · Editor Experience
- [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Agent Mode
- [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer Workflow changes in v2.1.285]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start automations from connected-app events]]
- Later: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11 Apps and Integrations changes in v2.1.286]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-29-6b1e05&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-29-14-apps-and-integrations-changes-in-v2-1-285.md%0ACard%20ID%3A%20claude-code-2026-09-29-6b1e05%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.285%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->