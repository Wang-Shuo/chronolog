---
card_id: claude-code-2026-02-20-648196
date: '2026-02-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1070
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 8643b07d42fe0e9965733b754238825b274dd66d9482258ce6c303da63c116d4
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-02-20-648196
  comparison: ''
  confidence: low
  date: '2026-02-20'
  description: 'Claude Code — v2.1.50: Added `WorktreeCreate` and `WorktreeRemove`
    hook events, enabling custom VCS setup and teardown when agent worktree isolation
    creates or removes worktrees.'
  evidence:
  - quote: Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom
      VCS setup and teardown when agent worktree isolation creates or removes worktrees.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.50
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-worktreecreate-and-worktreeremove-hook-events-enabling-custom-vcs-setup-an
  source_release: claude-code-2026-02-20-v2-1-50-github-288920711-09694b82
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
  title: Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom
    VCS setup…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-10-improved-heredoc-delimiter-parsing-to-prevent-command-smuggling|claude-code-2026-02-10-ac3a58]]'
- '[[Changes/Cursor/2026-02-18-mermaid-code-blocks-now-render-inline-as-ascii-diagrams-in-your-cli-conversation|cursor-2026-02-18-a06cbc]]'
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|chatgpt-2026-02-19-97cccf]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-20-v2-1-50-github-288920711-09694b82|claude-code-2026-02-20-v2-1-50-github-288920711-09694b82]]'
source_type: github_releases
theme: developer-workflow
title: Added WorktreeCreate and WorktreeRemove hook events, enabling custom VCS setup…
type: change
---

# Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.50: Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.50
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
- Lag Days: 1070
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes