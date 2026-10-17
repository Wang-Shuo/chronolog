---
card_id: claude-code-2026-09-08-7a773a
date: '2026-09-08'
description: 'Claude Code · 2026-09-08 · Apps and Integrations: 4 changes in v2.1.265
  — Added support for pointing `--plugin-dir` at a folder of plugins: each child folder…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d6ba2981676c009b72b876a3c0c641216bb64e799b3d552bdc28f49f7352918b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-08-7a773a
  comparison: ''
  date: '2026-09-08'
  description: 'Claude Code — v2.1.265: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Added support for pointing `--plugin-dir` at a folder of plugins: each
      child folder with a manifest loads, and children added or removed while running
      are picked up'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.265
  - quote: 'Improved slash commands typed mid-prompt: matches now show in a list (Tab
      opens it outside fullscreen) instead of a single suggestion, and a plugin skill
      is now found by its bare name'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.265
  - quote: Changed plugin display metadata to prefer the marketplace entry over `plugin.json`
      on the Installed tab and `claude plugin details`, filling gaps from `plugin.json`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.265
  - quote: Changed Claude apps gateway sessions to export OpenTelemetry directly to
      a collector the gateway's managed settings name in `OTEL_EXPORTER_OTLP_ENDPOINT`,
      instead of through the gateway's relay; sessions without a named collector still
      use the relay
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.265
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-265
  source_release: claude-code-2026-09-08-v2-1-265-github-384990084-dc34b405
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.265
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4
  Apps and Integrations changes in v2.1.260]]'
- '[[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added
  /reload-plugins to headless sessions, so it appears in the Claude Code…]]'
- '[[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode
  Added an Add server form and a Remove action to the MCP servers dialog…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-08-v2-1-265-github-384990084-dc34b405|claude-code-2026-09-08-v2-1-265-github-384990084-dc34b405]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.265
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.265

**Claude Code** · 2026-09-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.265) · from [[Releases/Claude Code/claude-code-2026-09-08-v2-1-265-github-384990084-dc34b405|v2.1.265]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added support for pointing `--plugin-dir` at a folder of plugins: each child folder with a manifest loads, and children added or removed while running are picked up

> Improved slash commands typed mid-prompt: matches now show in a list (Tab opens it outside fullscreen) instead of a single suggestion, and a plugin skill is now found by its bare name

> Changed plugin display metadata to prefer the marketplace entry over `plugin.json` on the Installed tab and `claude plugin details`, filling gaps from `plugin.json`

> Changed Claude apps gateway sessions to export OpenTelemetry directly to a collector the gateway's managed settings name in `OTEL_EXPORTER_OTLP_ENDPOINT`, instead of through the gateway's relay; sessions without a named collector still use the relay

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.265
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-08-added-user-email-and-user-groups-to-the-telemetry-claude-desktop-and-cowork-send|Added user.email and user.groups to the telemetry Claude Desktop and Cowork send…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety and Privacy changes in v2.1.265]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-08-improved-worktree-startup-on-large-repositories-the-new-worktree-is-now-checked|Improved --worktree startup on large repositories]] · Developer Workflow
- [[Changes/Claude Code/2026-09-08-2-account-and-access-changes-in-v2-1-265|2 Account and Access changes in v2.1.265]] · Account and Access
- [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-08-7a773a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-08-4-apps-and-integrations-changes-in-v2-1-265.md%0ACard%20ID%3A%20claude-code-2026-09-08-7a773a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.265%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->