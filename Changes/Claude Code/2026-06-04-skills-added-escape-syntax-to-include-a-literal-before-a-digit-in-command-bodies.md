---
card_id: claude-code-2026-06-04-c16d8f
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1174
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-03-tools-explicitly-listing-grep-glob-now-provides-the-dedicated-search-tools-on-na|claude-code-2026-06-03-74afd0]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7fb7c9497563d8df7f437b5ddf64b78bb5bbbe8601f984fba1b7d7d3c0375e8f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-02-acceptedits-mode-now-prompts-before-writing-build-tool-config-files-that-grant-c|claude-code-2026-06-02-58d83f]]'
- '[[Changes/Claude Code/2026-06-02-parallel-tool-calls-a-failed-bash-command-no-longer-cancels-other-calls-in-the-s|claude-code-2026-06-02-ae28c1]]'
- '[[Changes/Claude Code/2026-06-03-tools-explicitly-listing-grep-glob-now-provides-the-dedicated-search-tools-on-na|claude-code-2026-06-03-74afd0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988|claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988]]'
theme: developer-workflow
type: change
---

# Skills: added `\$` escape syntax to include a literal `$` before a digit in comm

<!-- chronolog:begin region="description" -->
Skills: added `\$` escape syntax to include a literal `$` before a digit in command bodies
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Skills: added `\$` escape syntax to include a literal `$` before a digit in command bodies
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-03-tools-explicitly-listing-grep-glob-now-provides-the-dedicated-search-tools-on-na|claude-code-2026-06-03-74afd0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1174
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes