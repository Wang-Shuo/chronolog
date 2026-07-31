---
card_id: claude-code-2026-04-09-cbd468
date: '2026-04-09'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1122
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-08-added-focus-view-toggle-ctrl-o-in-no-flicker-mode-showing-prompt-one-line-tool-s|claude-code-2026-04-08-e9c02e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: dfc9627d3555be36a3eed91a4ed5b52b82c2d2b14389d6d253e2f5c9b775a3ca
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-02-you-can-switch-back-to-the-ide-anytime-or-have-both-open-simultaneously|cursor-2026-04-02-ed78a6]]'
- '[[Changes/Claude Code/2026-04-08-added-syntax-highlighting-for-cedar-policy-files-cedar-cedarpolicy|claude-code-2026-04-08-dcfaa4]]'
- '[[Changes/Claude Code/2026-04-08-added-focus-view-toggle-ctrl-o-in-no-flicker-mode-showing-prompt-one-line-tool-s|claude-code-2026-04-08-e9c02e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
theme: editor-experience
type: change
---

# Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fai

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-08-added-focus-view-toggle-ctrl-o-in-no-flicker-mode-showing-prompt-one-line-tool-s|claude-code-2026-04-08-e9c02e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1122
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes