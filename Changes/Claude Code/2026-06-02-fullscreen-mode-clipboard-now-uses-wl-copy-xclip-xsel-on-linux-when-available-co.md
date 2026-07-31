---
card_id: claude-code-2026-06-02-fb9f22
date: '2026-06-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1240
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|claude-code-2026-05-28-40dca9]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: e36514cf3b66a16178375c238d9fc2d085c42a597ccc23b925022a493bf045d9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-21-prompt-history-no-longer-records-consecutive-duplicate-entries-recalling-a-promp|claude-code-2026-05-21-a1a371]]'
- '[[Changes/Claude Code/2026-05-22-markdown-output-now-renders-gfm-task-list-checkboxes-todo-x-done-instead-of-plai|claude-code-2026-05-22-222993]]'
- '[[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|claude-code-2026-05-28-40dca9]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa|claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa]]'
theme: interface-experience
type: change
---

# Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when avail

<!-- chronolog:begin region="description" -->
Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when available, copies to both the clipboard and PRIMARY selection for middle-click paste, and the "hold {key} for native selection" hint now shows the correct key per terminal
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when available, copies to both the clipboard and PRIMARY selection for middle-click paste, and the "hold {key} for native selection" hint now shows the correct key per terminal
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.161
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|claude-code-2026-05-28-40dca9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1240
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes