---
card_id: claude-code-2026-04-08-cfa4a0
date: '2026-04-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1117
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 226a903a90e6cf08b01869143b130290b1dffccf6a776126e9aebcdb061c7685
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-08-cfa4a0
  comparison: ''
  date: '2026-04-08'
  description: 'Claude Code — v2.1.97: Added `workspace.git_worktree` to the status
    line JSON input, set when the current directory is inside a linked git worktree'
  evidence:
  - quote: Added `workspace.git_worktree` to the status line JSON input, set when
      the current directory is inside a linked git worktree
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-workspace-git-worktree-to-the-status-line-json-input-set-when-the-current
  source_release: claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - status line
    score: 60
    theme: interface-experience
  - matched_terms:
    - worktree
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: Added `workspace.git_worktree` to the status line JSON input, set when the
    current…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]'
- '[[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|claude-code-2026-03-27-358253]]'
- '[[Changes/Cursor/2026-04-02-the-new-cursor-interface-allows-you-to-run-many-agents-in-parallel-across-repos|cursor-2026-04-02-57045c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33|claude-code-2026-04-08-v2-1-97-github-306811434-0f57bf33]]'
source_type: github_releases
theme: developer-workflow
title: Added workspace.git_worktree to the status line JSON input, set when the current…
type: change
---

# Added `workspace.git_worktree` to the status line JSON input, set when the current…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.97: Added `workspace.git_worktree` to the status line JSON input, set when the current directory is inside a linked git worktree
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `workspace.git_worktree` to the status line JSON input, set when the current directory is inside a linked git worktree
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.97
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
- Lag Days: 1117
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes