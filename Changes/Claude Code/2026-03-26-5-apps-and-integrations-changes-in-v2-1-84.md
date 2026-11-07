---
card_id: claude-code-2026-03-26-37e3b9
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Apps and Integrations: 5 changes in v2.1.84
  — MCP tool descriptions and server instructions are now capped at 2KB to prevent…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2659
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 191e886e3fb8a1b47a65984a9d6c3c0fb97545a6cc86a2ae2ba48a39f42beb22
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-37e3b9
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: 5 Apps and Integrations changes'
  evidence:
  - quote: MCP tool descriptions and server instructions are now capped at 2KB to
      prevent OpenAPI-generated servers from bloating context
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: MCP servers configured both locally and via claude.ai connectors are now
      deduplicated — the local config wins
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Global system-prompt caching now works when `ToolSearch` is enabled, including
      for users with MCP tools configured
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Improved startup for `claude "prompt"` with MCP servers — the REPL now
      renders immediately instead of blocking until all servers connect
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Improved Remote Control to show a specific reason when blocked instead
      of a generic "not yet enabled" message
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-84
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.84
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-03-25-linux-sandboxing-and-mcp-improvements|Linux
  Sandboxing and MCP Improvements]]'
- '[[Changes/Ollama/2026-03-25-openclaw-integration-improvements-for-gateway-checks|OpenClaw
  integration improvements for gateway checks]]'
- '[[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps
  and Integrations changes in v0.8.11]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.84
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.84

**Claude Code** · 2026-03-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tool descriptions and server instructions are now capped at 2KB to prevent OpenAPI-generated servers from bloating context

> MCP servers configured both locally and via claude.ai connectors are now deduplicated — the local config wins

> Global system-prompt caching now works when `ToolSearch` is enabled, including for users with MCP tools configured

> Improved startup for `claude "prompt"` with MCP servers — the REPL now renders immediately instead of blocking until all servers connect

> Improved Remote Control to show a specific reason when blocked instead of a generic "not yet enabled" message

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-26-2-reliability-and-performance-changes-in-v2-1-84|2 Reliability and Performance changes in v2.1.84]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-allowedchannelplugins-managed-setting-for-team-enterprise-admins-to-define|Added allowedChannelPlugins managed setting for team/enterprise admins to define…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Model Support
- [[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash commands unavailable for the current auth setup…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Context Window
- [[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer Workflow changes in v2.1.84]] · Developer Workflow
- [[Changes/Claude Code/2026-03-26-6-other-changes-in-v2-1-84|6 other changes in v2.1.84]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-25 · Open WebUI · [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps and Integrations changes in v2.1.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-37e3b9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-5-apps-and-integrations-changes-in-v2-1-84.md%0ACard%20ID%3A%20claude-code-2026-03-26-37e3b9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->