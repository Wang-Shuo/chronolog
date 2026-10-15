---
card_id: claude-code-2026-02-19-e831c2
date: '2026-02-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 66ef14d169189ea62d55fc24e3cb4eb7d317e50fef1ca9d17a5a04704e8964f4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-19-e831c2
  comparison: ''
  date: '2026-02-19'
  description: 'Claude Code — v2.1.49: Improved performance by caching authentication
    failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to
    servers requiring auth'
  evidence:
  - quote: Improved performance by caching authentication failures for HTTP and SSE
      MCP servers, avoiding repeated connection attempts to servers requiring auth
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.49
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: improved-performance-by-caching-authentication-failures-for-http-and-sse-mcp-ser
  source_release: claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - authentication
    score: 50
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  - matched_terms:
    - performance
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Improved performance by caching authentication failures for HTTP and SSE
    MCP…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]'
- '[[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|claude-code-2026-02-03-1c4ec2]]'
- '[[Changes/Claude Code/2026-02-13-added-claude-auth-login-claude-auth-status-and-claude-auth-logout-cli-subcommand|claude-code-2026-02-13-19875c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140|claude-code-2026-02-19-v2-1-49-github-288498923-7c27a140]]'
source_type: github_releases
theme: account-access
title: Improved performance by caching authentication failures for HTTP and SSE MCP…
type: change
---

# Improved performance by caching authentication failures for HTTP and SSE MCP…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.49: Improved performance by caching authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to servers requiring auth
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved performance by caching authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to servers requiring auth
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.49
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1057
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes