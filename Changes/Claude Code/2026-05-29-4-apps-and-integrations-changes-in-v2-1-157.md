---
card_id: claude-code-2026-05-29-bcbc85
date: '2026-05-29'
description: 'Claude Code · 2026-05-29 · Apps and Integrations: 4 changes in v2.1.157
  — Plugins in `.claude/skills` directories are now automatically loaded, no marketplace…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a348b855388bdca7bec0e0a08a7a560ab890ef234a0b9a9d5bb9e0493b148127
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-29-bcbc85
  comparison: ''
  date: '2026-05-29'
  description: 'Claude Code — v2.1.157: 4 Apps and Integrations changes'
  evidence:
  - quote: Plugins in `.claude/skills` directories are now automatically loaded, no
      marketplace required
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  - quote: Added `claude plugin init <name>` to scaffold a new plugin in `.claude/skills`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  - quote: 'Added autocomplete for `/plugin` arguments: subcommands, installed plugin
      names, and plugins from known marketplaces'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  - quote: '`tool_decision` telemetry events now include `tool_parameters` (bash commands,
      MCP/skill names) when `OTEL_LOG_TOOL_DETAILS=1`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-157
  source_release: claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.157
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-27-4-apps-and-integrations-changes-in-v2-1-152|4
  Apps and Integrations changes in v2.1.152]]'
- '[[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2
  Apps and Integrations changes in v2.1.153]]'
- '[[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4
  Apps and Integrations changes in v2.1.154]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8|claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.157
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.157

**Claude Code** · 2026-05-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.157) · from [[Releases/Claude Code/claude-code-2026-05-29-v2-1-157-github-331670634-f5eda9d8|v2.1.157]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugins in `.claude/skills` directories are now automatically loaded, no marketplace required

> Added `claude plugin init <name>` to scaffold a new plugin in `.claude/skills`

> Added autocomplete for `/plugin` arguments: subcommands, installed plugin names, and plugins from known marketplaces

> `tool_decision` telemetry events now include `tool_parameters` (bash commands, MCP/skill names) when `OTEL_LOG_TOOL_DETAILS=1`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.157
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-29-claude-agents-slash-command-autocomplete-in-the-dispatch-input-now-matches-subst|claude agents: slash-command autocomplete in the dispatch input now matches substrings]] · Interface Experience
- [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]] · Agent Mode
- [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-29-3-developer-workflow-changes-in-v2-1-157|3 Developer Workflow changes in v2.1.157]] · Developer Workflow
- [[Changes/Claude Code/2026-05-29-removed-the-ide-for-startup-hint-toast|Removed the "/ide for …" startup hint toast]] · Editor Experience
- [[Changes/Claude Code/2026-05-29-improved-performance-of-long-and-resumed-conversations-by-eliminating-redundant|Improved performance of long and resumed conversations by eliminating redundant…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4 Apps and Integrations changes in v2.1.154]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp now collapses claude.ai connectors you've never signed in to behind…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-29-bcbc85&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-29-4-apps-and-integrations-changes-in-v2-1-157.md%0ACard%20ID%3A%20claude-code-2026-05-29-bcbc85%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.157%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->