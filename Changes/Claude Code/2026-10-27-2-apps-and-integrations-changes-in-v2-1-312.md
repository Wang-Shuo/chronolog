---
card_id: claude-code-2026-10-27-8b6936
date: '2026-10-27'
description: 'Claude Code · 2026-10-27 · Apps and Integrations: 2 changes in v2.1.312
  — Added `oidc.user_id_claim` to the Claude apps gateway, to identify people by an…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1314
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a9321b878b2b34ae283b78e89d543661ed0fb88da1f963411580661968688553
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-27-8b6936
  comparison: ''
  date: '2026-10-27'
  description: 'Claude Code — v2.1.312: 2 Apps and Integrations changes'
  evidence:
  - quote: Added `oidc.user_id_claim` to the Claude apps gateway, to identify people
      by an id_token claim other than `sub`, such as Microsoft Entra ID's `oid`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
  - quote: Changed OpenTelemetry `mcp_server.name` to report the real name of fixed-URL
      remote MCP servers declared by plugins from the official Anthropic marketplace,
      instead of `custom`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-312
  source_release: claude-code-2026-10-27-v2-1-312-github-425846009-439d063a
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.312
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-22-2-apps-and-integrations-changes-in-v2-1-309|2
  Apps and Integrations changes in v2.1.309]]'
- '[[Changes/Claude Code/2026-10-23-2-apps-and-integrations-changes-in-v2-1-310|2
  Apps and Integrations changes in v2.1.310]]'
- '[[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3
  Apps and Integrations changes in v2.1.311]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-27-v2-1-312-github-425846009-439d063a|claude-code-2026-10-27-v2-1-312-github-425846009-439d063a]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.312
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.312

**Claude Code** · 2026-10-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.312) · from [[Releases/Claude Code/claude-code-2026-10-27-v2-1-312-github-425846009-439d063a|v2.1.312]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `oidc.user_id_claim` to the Claude apps gateway, to identify people by an id_token claim other than `sub`, such as Microsoft Entra ID's `oid`

> Changed OpenTelemetry `mcp_server.name` to report the real name of fixed-URL remote MCP servers declared by plugins from the official Anthropic marketplace, instead of `custom`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode changes in v2.1.312]] · Agent Mode
- [[Changes/Claude Code/2026-10-27-cloud-sessions-added-a-bash-editor-with-colors-line-numbers-and-a-copy-button-to|Cloud sessions Added a Bash editor with colors, line numbers and a Copy button…]] · Editor Experience
- [[Changes/Claude Code/2026-10-27-2-interface-experience-changes-in-v2-1-312|2 Interface Experience changes in v2.1.312]] · Interface Experience
- [[Changes/Claude Code/2026-10-27-changed-claude-code-to-stop-sending-the-claude-code-safety-event-opentelemetry-e|Changed Claude Code to stop sending the claude_code.safety_event OpenTelemetry event]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-27-changed-a-subagent-s-autocompactwindow-to-lower-the-window-set-by-claude-code-au|Changed a subagent's autoCompactWindow to lower the window set…]] · Context Window
- [[Changes/Claude Code/2026-10-27-3-model-support-changes-in-v2-1-312|3 Model Support changes in v2.1.312]] · Model Support
- [[Changes/Claude Code/2026-10-27-5-other-changes-in-v2-1-312|5 other changes in v2.1.312]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]]
- Later: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-27-8b6936&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-27-2-apps-and-integrations-changes-in-v2-1-312.md%0ACard%20ID%3A%20claude-code-2026-10-27-8b6936%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.312%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->