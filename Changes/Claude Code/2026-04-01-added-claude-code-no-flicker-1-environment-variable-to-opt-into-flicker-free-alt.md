---
card_id: claude-code-2026-04-01-b9ce60
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1178
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-19-added-rate-limits-field-to-statusline-scripts-for-displaying-claude-ai-rate-limi|claude-code-2026-03-19-5110e3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 65c73b41fe87c5f0c7d2078e14e906fa75272b358ea55d2edc226e3b6dbee5d0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-17-response-text-now-streams-line-by-line-as-it-s-generated|claude-code-2026-03-17-cd3956]]'
- '[[Changes/Claude Code/2026-03-18-added-show-turn-duration-toggle-to-the-config-menu|claude-code-2026-03-18-dd12a8]]'
- '[[Changes/Claude Code/2026-03-19-added-rate-limits-field-to-statusline-scripts-for-displaying-claude-ai-rate-limi|claude-code-2026-03-19-5110e3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
theme: interface-experience
type: change
---

# Added `CLAUDE_CODE_NO_FLICKER=1` environment variable to opt into flicker-free a

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_NO_FLICKER=1` environment variable to opt into flicker-free alt-screen rendering with virtualized scrollback
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_NO_FLICKER=1` environment variable to opt into flicker-free alt-screen rendering with virtualized scrollback
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-19-added-rate-limits-field-to-statusline-scripts-for-displaying-claude-ai-rate-limi|claude-code-2026-03-19-5110e3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1178
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes