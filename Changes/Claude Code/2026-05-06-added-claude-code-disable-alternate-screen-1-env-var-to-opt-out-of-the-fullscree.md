---
card_id: claude-code-2026-05-06-6aaf8f
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1213
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-added-claude-code-force-sync-output-1-env-var-to-force-enable-synchronized-outpu|claude-code-2026-05-06-652aeb]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 6802d26d6c3b9ffe1cfa38a517e5dade78490d39d6dde706c1c732e167b48240
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-28-fullscreen-mode-typing-into-the-prompt-no-longer-jumps-scroll-back-to-the-bottom|claude-code-2026-04-28-8a2fb3]]'
- '[[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|claude-code-2026-05-04-7e0d02]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-force-sync-output-1-env-var-to-force-enable-synchronized-outpu|claude-code-2026-05-06-652aeb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664|claude-code-2026-05-06-v2-1-132-github-318578987-ed60d664]]'
theme: interface-experience
type: change
---

# Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscr

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscreen alternate-screen renderer and keep the conversation in the terminal's native scrollback
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscreen alternate-screen renderer and keep the conversation in the terminal's native scrollback
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.132
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-added-claude-code-force-sync-output-1-env-var-to-force-enable-synchronized-outpu|claude-code-2026-05-06-652aeb]]
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