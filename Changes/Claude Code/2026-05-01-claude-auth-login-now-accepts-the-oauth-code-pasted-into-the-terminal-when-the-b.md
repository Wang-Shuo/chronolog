---
card_id: claude-code-2026-05-01-a5bb2e
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 26a34e02f3d53506f8a54d4c7b6c9afc98526705ec02d22ac9d63741bf3cf4a3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-01-a5bb2e
  comparison: ''
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: `claude auth login` now accepts the OAuth
    code pasted into the terminal when the browser callback can''t reach localhost
    (WSL2, SSH, containers)'
  evidence:
  - quote: '`claude auth login` now accepts the OAuth code pasted into the terminal
      when the browser callback can''t reach localhost (WSL2, SSH, containers)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - login
    - oauth
    score: 100
    theme: account-access
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  title: '`claude auth login` now accepts the OAuth code pasted into the terminal
    when the'
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|chatgpt-2026-04-22-432031]]'
- '[[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]'
- '[[Changes/ChatGPT/2026-04-30-we-re-rolling-out-advanced-account-security-an-optional-setting-for-personal-cha|chatgpt-2026-04-30-139382]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: account-access
title: claude auth login now accepts the OAuth code pasted into the terminal when
  the
type: change
---

# `claude auth login` now accepts the OAuth code pasted into the terminal when the

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.126: `claude auth login` now accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `claude auth login` now accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
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
- Lag Days: 1128
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes