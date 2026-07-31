---
card_id: claude-code-2026-04-23-774df5
date: '2026-04-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1136
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-20-config-search-now-matches-option-values-e-g-searching-vim-finds-the-editor-mode|claude-code-2026-04-20-ae9196]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: eee0581819c6213b8f8afd99f5fe18f47a3f8dbab65c8028aa08b734c0e108e6
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-09-added-claude-code-perforce-mode-env-var-when-set-edit-write-notebookedit-fail-on|claude-code-2026-04-09-cbd468]]'
- '[[Changes/Cursor/2026-04-15-try-it-out-in-cursor-3-1-in-the-agents-window-or-the-editor-read-more-in-our-ann|cursor-2026-04-15-034e94]]'
- '[[Changes/Claude Code/2026-04-20-config-search-now-matches-option-values-e-g-searching-vim-finds-the-editor-mode|claude-code-2026-04-20-ae9196]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-23-v2-1-119-github-312949780-573724e7|claude-code-2026-04-23-v2-1-119-github-312949780-573724e7]]'
theme: editor-experience
type: change
---

# `/config` settings (theme, editor mode, verbose, etc.) now persist to `~/.claude

<!-- chronolog:begin region="description" -->
`/config` settings (theme, editor mode, verbose, etc.) now persist to `~/.claude/settings.json` and participate in project/local/policy override precedence
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `/config` settings (theme, editor mode, verbose, etc.) now persist to `~/.claude/settings.json` and participate in project/local/policy override precedence
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.119
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-20-config-search-now-matches-option-values-e-g-searching-vim-finds-the-editor-mode|claude-code-2026-04-20-ae9196]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1136
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes