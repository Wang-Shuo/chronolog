---
card_id: claude-code-2026-02-03-1c4ec2
date: '2026-02-03'
description: 'Claude Code · 2026-02-03 · Account and Access: Added pre-configured
  OAuth client credentials for MCP servers that don''t support Dynamic Client Registration…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: c7bd3940673da7787778207cb262019fb8f411f07f1a4fd939160c19660d9c56
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-02-03-1c4ec2
  comparison: ''
  confidence: low
  date: '2026-02-03'
  description: 'Claude Code — v2.1.30: Added pre-configured OAuth client credentials
    for MCP servers that don''t support Dynamic Client Registration (e.g., Slack).
    Use `--client-id` and `--client-secret` with `claude mcp add`.'
  evidence:
  - quote: Added pre-configured OAuth client credentials for MCP servers that don't
      support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret`
      with `claude mcp add`.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support
  source_release: claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: Added pre-configured OAuth client credentials for MCP servers that don't
    support…
  type: change
related_changes:
- '[[Changes/Cursor/2026-01-16-one-click-mcp-authentication|One-click MCP authentication]]'
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|VSCode
  Added ability for OAuth users to browse and resume remote Claude sessions…]]'
- '[[Changes/Cursor/2026-01-22-browser-can-now-request-local-network-permissions-fixing-authentication-flows-wi|Browser
  can now request local network permissions, fixing authentication flows…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
source_type: github_releases
theme: account-access
title: Added pre-configured OAuth client credentials for MCP servers that don't support…
type: change
---

<!-- chronolog:begin region="header" -->
# Added pre-configured OAuth client credentials for MCP servers that don't support…

**Claude Code** · 2026-02-03 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.30) · from [[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|v2.1.30]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-03-2-developer-workflow-changes-in-v2-1-30|2 Developer Workflow changes in v2.1.30]] · Developer Workflow
- [[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added pages parameter to the Read tool for PDFs, allowing specific page ranges…]] · Context Window
- [[Changes/Claude Code/2026-02-03-improved-memory-usage-for-resume-68-reduction-for-users-with-many-sessions-by-re|Improved memory usage for --resume (68% reduction for users with many sessions)…]] · Reliability and Performance
- [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]] · Agent Mode
- [[Changes/Claude Code/2026-02-03-changed-model-to-execute-immediately-instead-of-being-queued|Changed /model to execute immediately instead of being queued]] · Model Support
- [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-03-added-debug-for-claude-to-help-troubleshoot-the-current-session|Added /debug for Claude to help troubleshoot the current session]] · Developer Workflow
- [[Changes/Claude Code/2026-02-03-2-other-changes-in-v2-1-30|2 other changes in v2.1.30]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-01-22 · Cursor · [[Changes/Cursor/2026-01-22-browser-can-now-request-local-network-permissions-fixing-authentication-flows-wi|Browser can now request local network permissions, fixing authentication flows…]]
- Later: 2026-02-06 · Claude Code · [[Changes/Claude Code/2026-02-06-vscode-added-support-for-remote-sessions-allowing-oauth-users-to-browse-and-resu|VSCode: Added support for remote sessions, allowing OAuth users to browse and resume…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-03-1c4ec2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support.md%0ACard%20ID%3A%20claude-code-2026-02-03-1c4ec2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.30%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->