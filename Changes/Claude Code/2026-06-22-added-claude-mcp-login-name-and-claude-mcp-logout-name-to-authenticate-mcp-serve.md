---
card_id: claude-code-2026-06-22-27079a
date: '2026-06-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: significant
machine_hash: 125e7cb1875fc0b14b3460fc73614db49c405c6bcf0663a8bf9014b04c748f82
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-06-22-27079a
  comparison: ''
  confidence: low
  date: '2026-06-22'
  description: 'Claude Code — v2.1.186: Added `claude mcp login <name>` and `claude
    mcp logout <name>` to authenticate MCP servers from the CLI without opening the
    interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing
    over SSH'
  evidence:
  - quote: Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate
      MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser`
      stdin redirect support for completing over SSH
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
  extractor_version: fallback-v3
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-claude-mcp-login-name-and-claude-mcp-logout-name-to-authenticate-mcp-serve
  source_release: claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - login
    score: 50
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  - matched_terms:
    - menu
    score: 50
    theme: interface-experience
  theme_resolution: manual-semantic-rule-v1
  title: Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate
    M
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-02-active-sessions-shows-sessions-known-through-session-management-including-chatgp|chatgpt-2026-06-02-4822a8]]'
- '[[Changes/ChatGPT/2026-06-02-log-out-of-individual-sessions-or-all-sessions-from-active-sessions|chatgpt-2026-06-02-a6ea70]]'
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b|claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b]]'
source_type: github_releases
theme: account-access
title: Added claude mcp login name and claude mcp logout name to authenticate M
type: change
---

# Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate M

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.186: Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing over SSH
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing over SSH
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
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
- Lag Days: 1180
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes