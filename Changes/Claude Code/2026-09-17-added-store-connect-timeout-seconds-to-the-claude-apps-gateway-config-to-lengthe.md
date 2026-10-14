---
card_id: claude-code-2026-09-17-494f3b
date: '2026-09-17'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|chatgpt-2023-03-23-872ff0]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: dd5ea3772e96e62995aaf7e0232ee96992fbd66c1dbdd49ff9ea853fbae95181
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-494f3b
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: Added `store.connect_timeout_seconds` to the
    Claude apps gateway config to lengthen the Postgres connect timeout (default 5
    seconds), and improved the boot error when the database is unreachable to point
    to `store.postgres_url` and the configured timeout'
  evidence:
  - quote: Added `store.connect_timeout_seconds` to the Claude apps gateway config
      to lengthen the Postgres connect timeout (default 5 seconds), and improved the
      boot error when the database is unreachable to point to `store.postgres_url`
      and the configured timeout
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-store-connect-timeout-seconds-to-the-claude-apps-gateway-config-to-lengthe
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: apps-integrations
  title: Added `store.connect_timeout_seconds` to the Claude apps gateway config to
    lengt
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|chatgpt-2026-09-14-d001f0]]'
- '[[Changes/Claude Code/2026-09-15-added-forking-a-session-started-with-claude-remote-control-or-remote-control-fro|claude-code-2026-09-15-58687b]]'
- '[[Changes/Claude Code/2026-09-15-added-a-notification-when-an-mcp-server-disconnects-mid-session-and-automatic-re|claude-code-2026-09-15-d5fb1c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: apps-integrations
title: Added store.connect_timeout_seconds to the Claude apps gateway config to lengt
type: change
---

# Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengt

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.274: Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengthen the Postgres connect timeout (default 5 seconds), and improved the boot error when the database is unreachable to point to `store.postgres_url` and the configured timeout
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengthen the Postgres connect timeout (default 5 seconds), and improved the boot error when the database is unreachable to point to `store.postgres_url` and the configured timeout
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
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
- Lag Days: 1274
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes