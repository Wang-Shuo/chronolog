---
card_id: claude-code-2026-03-20-d05f5d
date: '2026-03-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1098
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 90c9b99ab98cfc611ba86538ed167c9dbf1f685c53b257bf843b1e2b34569f1b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-20-d05f5d
  comparison: ''
  date: '2026-03-20'
  description: 'Claude Code — v2.1.81: Added `--bare` flag for scripted `-p` calls
    — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY`
    or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory
    fully disabled'
  evidence:
  - quote: Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin
      sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper`
      via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc
  source_release: claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - plugin
    score: 50
    theme: apps-integrations
  - matched_terms:
    - lsp
    score: 50
    theme: developer-workflow
  theme_resolution: manual-backfill-review-v1
  title: Added `--bare` flag for scripted `-p` calls
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|claude-code-2026-03-14-d75873]]'
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|claude-code-2026-03-17-feecd4]]'
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe]]'
source_type: github_releases
theme: developer-workflow
title: Added --bare flag for scripted -p calls
type: change
---

# Added `--bare` flag for scripted `-p` calls

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.81: Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1098
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes