---
card_id: claude-code-2026-04-01-210067
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Apps and Integrations: Added `MCP_CONNECTION_NONBLOCKING=true`
  for `-p` mode to skip the MCP connection wait entirely, and bounded…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You
    can join the waitlist to try plugins here]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 39c5d0b9f61165117f44f7063d2ab5624783245f7c69949f42d20695736a2745
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-210067
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: Added `MCP_CONNECTION_NONBLOCKING=true` for
    `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config`
    server connections at 5s instead of blocking on the slowest server'
  evidence:
  - quote: Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection
      wait entirely, and bounded `--mcp-config` server connections at 5s instead of
      blocking on the slowest server
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: apps-integrations
  title: Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-deep-link-queries-claude-cli-open-q-now-support-up-to-5-000-characters-with-a-sc|Deep
  link queries (claude-cli://open?q=…) now support up to 5,000 characters…]]'
- '[[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|ChatGPT
  rolls out updated Box, Notion, Linear, and Dropbox apps]]'
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced
  startup event-loop stalls when many claude.ai MCP connectors are configured…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: apps-integrations
title: Added MCP_CONNECTION_NONBLOCKING=true for -p mode to skip the MCP connection…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection…

**Claude Code** · 2026-04-01 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|Added "defer" permission decision to PreToolUse hooks]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-added-permissiondenied-hook-that-fires-after-auto-mode-classifier-denials-return|Added PermissionDenied hook that fires after auto mode classifier denials]] · Agent Mode
- [[Changes/Claude Code/2026-04-01-added-named-subagents-to-mention-typeahead-suggestions|Added named subagents to @ mention typeahead suggestions]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|Added CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE env var to keep the existing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You can join the waitlist to try plugins here]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-210067&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait.md%0ACard%20ID%3A%20claude-code-2026-04-01-210067%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->