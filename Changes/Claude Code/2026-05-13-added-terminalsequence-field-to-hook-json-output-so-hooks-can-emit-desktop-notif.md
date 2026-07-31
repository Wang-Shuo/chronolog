---
card_id: claude-code-2026-05-13-df56c4
date: '2026-05-13'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1147
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|claude-code-2026-05-12-abb705]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c688672aef4e40450f14003d2f26cbc4ed10d8d092f7fd44cbbffe6a515d79c0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|claude-code-2026-05-11-368eed]]'
- '[[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|cursor-2026-05-11-df0e2b]]'
- '[[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|claude-code-2026-05-12-abb705]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
theme: apps-integrations
type: change
---

# Added `terminalSequence` field to hook JSON output so hooks can emit desktop not

<!-- chronolog:begin region="description" -->
Added `terminalSequence` field to hook JSON output so hooks can emit desktop notifications, window titles, and bells without a controlling terminal
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `terminalSequence` field to hook JSON output so hooks can emit desktop notifications, window titles, and bells without a controlling terminal
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-12-plugins-now-warn-when-a-default-component-folder-e-g-commands-is-silently-ignore|claude-code-2026-05-12-abb705]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1147
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes