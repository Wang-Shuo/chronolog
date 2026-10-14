---
card_id: claude-code-2026-02-03-1c4ec2
date: '2026-02-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: significant
machine_hash: 037936f1101c5a7c4b4668967ecf148b5496e844f8753d481ec2eb6c022dabaa
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
  extractor_version: fallback-v3
  impact: significant
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
    support
  type: change
related_changes:
- '[[Changes/Cursor/2023-09-01-you-should-now-be-able-to-sign-in-with-github-again|cursor-2023-09-01-272a25]]'
- '[[Changes/ChatGPT/2024-04-01-we-re-making-it-easier-for-people-to-experience-the-benefits-of-ai-without-needi|chatgpt-2024-04-01-9d75a2]]'
- '[[Changes/Claude Code/2026-01-22-vscode-added-ability-for-oauth-users-to-browse-and-resume-remote-claude-sessions|claude-code-2026-01-22-5b6a2e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
source_type: github_releases
theme: account-access
title: Added pre-configured OAuth client credentials for MCP servers that don't support
type: change
---

# Added pre-configured OAuth client credentials for MCP servers that don't support

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.30: Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
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
- Lag Days: 1041
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes