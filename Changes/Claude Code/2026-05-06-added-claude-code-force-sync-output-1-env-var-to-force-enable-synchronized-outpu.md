---
card_id: claude-code-2026-05-06-652aeb
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1213
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|claude-code-2026-05-04-7e0d02]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ebed449565fb3fa7ce1afc6df6384dee52017b47b439b0ec775dee16a8477ec3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-28-added-a-type-to-filter-search-box-to-skills-so-you-can-find-a-skill-in-long-list|claude-code-2026-04-28-185430]]'
- '[[Changes/Claude Code/2026-04-28-fullscreen-mode-typing-into-the-prompt-no-longer-jumps-scroll-back-to-the-bottom|claude-code-2026-04-28-8a2fb3]]'
- '[[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|claude-code-2026-05-04-7e0d02]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f]]'
theme: interface-experience
type: change
---

# Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized out

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized output on terminals that auto-detection misses (e.g. Emacs `eat`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized output on terminals that auto-detection misses (e.g. Emacs `eat`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|claude-code-2026-05-04-7e0d02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1213
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes