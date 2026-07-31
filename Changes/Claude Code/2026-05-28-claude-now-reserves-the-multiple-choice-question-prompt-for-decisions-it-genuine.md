---
card_id: claude-code-2026-05-28-e3cabb
date: '2026-05-28'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1120
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|claude-code-2026-04-15-980a64]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 84412bb04638705e14878052dd2e92397da4a2ac2235033fbce68c8c8077cee8
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-11-cursor-automatically-picks-the-right-repository-and-model-based-on-your-prompt-a|cursor-2026-05-11-9965be]]'
- '[[Changes/Cursor/2026-05-18-fast-default-3-00-m-input-15-00-m-output-tokens|cursor-2026-05-18-1726b2]]'
- '[[Changes/Cursor/2026-05-18-standard-0-50-m-input-2-50-m-output-tokens|cursor-2026-05-18-5a9507]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9]]'
theme: context-window
type: change
---

# Claude now reserves the multiple-choice question prompt for decisions it genuine

<!-- chronolog:begin region="description" -->
Claude now reserves the multiple-choice question prompt for decisions it genuinely cannot make itself, instead of asking when it already has enough context to proceed
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Claude now reserves the multiple-choice question prompt for decisions it genuinely cannot make itself, instead of asking when it already has enough context to proceed
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|claude-code-2026-04-15-980a64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1120
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes