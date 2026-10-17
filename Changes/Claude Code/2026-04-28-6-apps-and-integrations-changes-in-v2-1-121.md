---
card_id: claude-code-2026-04-28-de37ff
date: '2026-04-28'
description: 'Claude Code · 2026-04-28 · Apps and Integrations: 6 changes in v2.1.121
  — Added `alwaysLoad` option to MCP server config — when `true`, all tools from that…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f8c145f2fad2cefa83712585034c31656ed86d9eed7abaf63ce9acb7c27a7672
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-28-de37ff
  comparison: ''
  date: '2026-04-28'
  description: 'Claude Code — v2.1.121: 6 Apps and Integrations changes'
  evidence:
  - quote: Added `alwaysLoad` option to MCP server config — when `true`, all tools
      from that server skip tool-search deferral and are always available
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: Added `claude plugin prune` to remove orphaned auto-installed plugin dependencies;
      `plugin uninstall --prune` cascades
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: PostToolUse hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput`
      (previously MCP-only)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: MCP servers that hit a transient error during startup now auto-retry up
      to 3 times instead of staying disconnected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: Claude.ai connectors with the same upstream URL are now deduplicated instead
      of appearing as duplicates
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: 'SDK: `mcp_authenticate` now supports `redirectUri` for custom scheme completion
      and claude.ai connectors'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-121
  source_release: claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.121
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3
  Apps and Integrations changes in v2.1.119]]'
- '[[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5
  Apps and Integrations changes in v2.1.118]]'
- '[[Changes/Claude Code/2026-04-28-2-apps-and-integrations-changes-in-v2-1-122|2
  Apps and Integrations changes in v2.1.122]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.121
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.121

**Claude Code** · 2026-04-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.121) · from [[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|v2.1.121]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `alwaysLoad` option to MCP server config — when `true`, all tools from that server skip tool-search deferral and are always available

> Added `claude plugin prune` to remove orphaned auto-installed plugin dependencies; `plugin uninstall --prune` cascades

> PostToolUse hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput` (previously MCP-only)

> MCP servers that hit a transient error during startup now auto-retry up to 3 times instead of staying disconnected

> Claude.ai connectors with the same upstream URL are now deduplicated instead of appearing as duplicates

> SDK: `mcp_authenticate` now supports `redirectUri` for custom scheme completion and claude.ai connectors

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-28-faster-startup-after-upgrading-removed-the-recent-activity-panel-from-the-releas|Faster startup after upgrading]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-28-2-agent-mode-changes-in-v2-1-121|2 Agent Mode changes in v2.1.121]] · Agent Mode
- [[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry: added stop_reason, gen_ai.response.finish_reasons…]] · Model Support
- [[Changes/Claude Code/2026-04-28-vscode-voice-dictation-now-respects-the-accessibility-voice-speechlanguage-setti|VSCode Voice dictation now respects the accessibility.voice.speechLanguage…]] · Voice and Audio
- [[Changes/Claude Code/2026-04-28-4-developer-workflow-changes-in-v2-1-121|4 Developer Workflow changes in v2.1.121]] · Developer Workflow
- [[Changes/Claude Code/2026-04-28-4-interface-experience-changes-in-v2-1-121|4 Interface Experience changes in v2.1.121]] · Interface Experience
- [[Changes/Claude Code/2026-04-28-vscode-context-now-opens-a-native-token-usage-dialog|VSCode /context now opens a native token usage dialog]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-2-apps-and-integrations-changes-in-v2-1-122|2 Apps and Integrations changes in v2.1.122]]
- Later: 2026-04-29 · Cursor · [[Changes/Cursor/2026-04-29-we-re-introducing-the-cursor-sdk-so-you-can-build-agents-with-the-same-runtime-h|Cursor introduces the Cursor SDK so you can build agents with the same runtime…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-28-de37ff&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-28-6-apps-and-integrations-changes-in-v2-1-121.md%0ACard%20ID%3A%20claude-code-2026-04-28-de37ff%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.121%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->