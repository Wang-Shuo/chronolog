---
card_id: claude-code-2026-02-28-0b3758
date: '2026-02-28'
description: 'Claude Code · 2026-02-28 · Account and Access: Added manual URL paste
  fallback during MCP OAuth authentication. If the automatic localhost redirect doesn''t…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f9e743f83fea732e723ab6dd609361d1e540f41bc1fcef2c34ebef587626bdf1
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-28-0b3758
  comparison: ''
  date: '2026-02-28'
  description: 'Claude Code — v2.1.63: Added manual URL paste fallback during MCP
    OAuth authentication. If the automatic localhost redirect doesn''t work, you can
    paste the callback URL to complete authentication.'
  evidence:
  - quote: Added manual URL paste fallback during MCP OAuth authentication. If the
      automatic localhost redirect doesn't work, you can paste the callback URL to
      complete authentication.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic
  source_release: claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - authentication
    - oauth
    score: 100
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  title: Added manual URL paste fallback during MCP OAuth authentication
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-06-vscode-added-support-for-remote-sessions-allowing-oauth-users-to-browse-and-resu|VSCode:
  Added support for remote sessions, allowing OAuth users to browse and resume…]]'
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|Added
  claude auth login, claude auth status, and claude auth logout CLI subcommands]]'
- '[[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved
  performance by caching authentication failures for HTTP and SSE MCP…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c]]'
source_type: github_releases
theme: account-access
title: Added manual URL paste fallback during MCP OAuth authentication
type: change
---

<!-- chronolog:begin region="header" -->
# Added manual URL paste fallback during MCP OAuth authentication

**Claude Code** · 2026-02-28 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.63) · from [[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|v2.1.63]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added manual URL paste fallback during MCP OAuth authentication. If the automatic localhost redirect doesn't work, you can paste the callback URL to complete authentication.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]] · Memory and Personalization
- [[Changes/Claude Code/2026-02-28-improved-model-command-to-show-the-currently-active-model-in-the-slash-command-m|Improved /model command to show the currently active model in the slash command menu]] · Developer Workflow
- [[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added "Always copy full response" option to the /copy picker]] · Interface Experience
- [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]] · Agent Mode
- [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres|Improved memory usage in long sessions with subagents by stripping heavy progress…]] · Reliability and Performance
- [[Changes/Claude Code/2026-02-28-added-simplify-and-batch-bundled-slash-commands|Added /simplify and /batch bundled slash commands]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-19 · Claude Code · [[Changes/Claude Code/2026-02-19-improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser|Improved performance by caching authentication failures for HTTP and SSE MCP…]]
- Later: 2026-03-05 · Claude Code · [[Changes/Claude Code/2026-03-05-2-account-and-access-changes-in-v2-1-69|2 Account and Access changes in v2.1.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-28-0b3758&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic.md%0ACard%20ID%3A%20claude-code-2026-02-28-0b3758%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.63%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->