---
card_id: claude-code-2026-04-01-210067
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|chatgpt-2023-03-23-872ff0]]'
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
machine_hash: e660f1182d202508962909ad04e9717ca32a3c45e67c974f42cc3a57e395f50b
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
- '[[Changes/Claude Code/2026-03-26-deep-link-queries-claude-cli-open-q-now-support-up-to-5-000-characters-with-a-sc|claude-code-2026-03-26-7f4ed1]]'
- '[[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|chatgpt-2026-03-27-9f6ee9]]'
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: apps-integrations
title: Added MCP_CONNECTION_NONBLOCKING=true for -p mode to skip the MCP connection…
type: change
---

# Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.89: Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|chatgpt-2023-03-23-872ff0]]
- Lag Days: 1105
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes