---
card_id: claude-code-2026-05-07-6fb4d0
date: '2026-05-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 49954f6728e7315d8a55c8eaacc0d2196bee9451da6a3a7f8c649ad45ff39b83
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-05-07-6fb4d0
  comparison: ''
  confidence: low
  date: '2026-05-07'
  description: 'Claude Code — v2.1.133: Added `worktree.baseRef` setting (`fresh`
    | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation
    worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default
    `fresh` changes `EnterWorktree`''s base back to `origin/<default>` (it has been
    local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed
    commits in new worktrees'
  evidence:
  - quote: 'Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether
      `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>`
      or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`''s base
      back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef:
      "head"` to keep unpushed commits in new worktrees'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr
  source_release: claude-code-2026-05-07-v2-1-133-github-319164825-08653677
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - worktree
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-added-prurltemplate-setting-to-point-the-footer-pr-badge-at-a-custom-code-review|claude-code-2026-04-23-cf1efd]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|claude-code-2026-04-28-33dc91]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|claude-code-2026-05-06-3f1ca0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
source_type: github_releases
theme: developer-workflow
title: Added worktree.baseRef setting (fresh  /  head) to choose whether --worktree…
type: change
---

# Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.133: Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
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
- Lag Days: 1146
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes