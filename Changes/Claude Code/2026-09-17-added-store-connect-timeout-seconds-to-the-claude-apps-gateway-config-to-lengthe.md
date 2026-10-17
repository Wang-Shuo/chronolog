---
card_id: claude-code-2026-09-17-494f3b
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Apps and Integrations: Added `store.connect_timeout_seconds`
  to the Claude apps gateway config to lengthen the Postgres connect…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You
    can join the waitlist to try plugins here]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: f0bbf4e5f6132896f0d1d3c6675f60e9df035ece148ace8e41ca05207239198f
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
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-store-connect-timeout-seconds-to-the-claude-apps-gateway-config-to-lengthe
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: apps-integrations
  title: Added `store.connect_timeout_seconds` to the Claude apps gateway config to
    lengthen…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You
  can change your Health permissions anytime in Settings → Plugins → Health]]'
- '[[Changes/Claude Code/2026-09-15-added-forking-a-session-started-with-claude-remote-control-or-remote-control-fro|Added
  forking a session started with claude --remote-control or /remote-control…]]'
- '[[Changes/Claude Code/2026-09-15-added-a-notification-when-an-mcp-server-disconnects-mid-session-and-automatic-re|Added
  a notification when an MCP server disconnects mid-session and automatic…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
superseded: true
theme: apps-integrations
title: Added store.connect_timeout_seconds to the Claude apps gateway config to lengthen…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengthen…

**Claude Code** · 2026-09-17 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengthen the Postgres connect timeout (default 5 seconds), and improved the boot error when the database is unreachable to point to `store.postgres_url` and the configured timeout
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-added-claude-code-mcp-startup-wait-ms-to-bound-how-long-the-first-non-interactiv|Added CLAUDE_CODE_MCP_STARTUP_WAIT_MS to bound how long the first non-interactive…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-added-effort-attribute-to-the-claude-code-llm-request-opentelemetry-trace-span-m|Added effort attribute to the claude_code.llm_request OpenTelemetry trace span…]] · Model Support
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-added-a-notification-when-an-mcp-server-disconnects-mid-session-and-automatic-re|Added a notification when an MCP server disconnects mid-session and automatic…]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You can join the waitlist to try plugins here]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-494f3b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-added-store-connect-timeout-seconds-to-the-claude-apps-gateway-config-to-lengthe.md%0ACard%20ID%3A%20claude-code-2026-09-17-494f3b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->