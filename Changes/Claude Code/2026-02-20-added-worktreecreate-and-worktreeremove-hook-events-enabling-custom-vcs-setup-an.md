---
card_id: claude-code-2026-02-20-648196
date: '2026-02-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1070
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-10-improved-heredoc-delimiter-parsing-to-prevent-command-smuggling|claude-code-2026-02-10-ac3a58]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: ee78b757be5746563697eef1b659257e0571a530bfe74d0df74f75a8652839ef
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-10-improved-heredoc-delimiter-parsing-to-prevent-command-smuggling|claude-code-2026-02-10-ac3a58]]'
- '[[Changes/Cursor/2026-02-18-mermaid-ascii-diagrams-in-cli|cursor-2026-02-18-185f96]]'
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|chatgpt-2026-02-19-97cccf]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-20-v2-1-50-github-288920711-09694b82|claude-code-2026-02-20-v2-1-50-github-288920711-09694b82]]'
theme: developer-workflow
type: change
---

# Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS set

<!-- chronolog:begin region="description" -->
Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.50
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-10-improved-heredoc-delimiter-parsing-to-prevent-command-smuggling|claude-code-2026-02-10-ac3a58]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1070
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes