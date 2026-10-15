---
card_id: claude-code-2026-02-24-30f423
date: '2026-02-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 72f750653a0e6932805193201611666a830aefe2eed23923ef4fa60540ec5e94
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-24-30f423
  comparison: ''
  date: '2026-02-24'
  description: 'Claude Code — v2.1.51: BashTool now skips login shell (`-l` flag)
    by default when a shell snapshot is available, improving command execution performance.
    Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.'
  evidence:
  - quote: BashTool now skips login shell (`-l` flag) by default when a shell snapshot
      is available, improving command execution performance. Previously this required
      setting `CLAUDE_BASH_NO_LOGIN=true`.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa
  source_release: claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - login
    score: 50
    theme: account-access
  - matched_terms:
    - performance
    score: 50
    theme: reliability-performance
  theme_resolution: manual-backfill-review-v1
  title: BashTool now skips login shell (`-l` flag) by default when a shell snapshot…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|chatgpt-2026-02-19-97cccf]]'
- '[[Changes/Claude Code/2026-02-20-added-worktreecreate-and-worktreeremove-hook-events-enabling-custom-vcs-setup-an|claude-code-2026-02-20-648196]]'
- '[[Changes/Claude Code/2026-02-20-added-support-for-startuptimeout-configuration-for-lsp-servers|claude-code-2026-02-20-aba95d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
source_type: github_releases
theme: developer-workflow
title: BashTool now skips login shell (-l flag) by default when a shell snapshot…
type: change
---

# BashTool now skips login shell (`-l` flag) by default when a shell snapshot…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.51: BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
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
- Lag Days: 1074
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes