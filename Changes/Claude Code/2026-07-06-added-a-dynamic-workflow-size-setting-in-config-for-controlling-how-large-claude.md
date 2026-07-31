---
card_id: claude-code-2026-07-06-9942eb
date: '2026-07-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1096
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|claude-code-2026-07-01-4d022c]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 0f4c8ad6cf7be539fc27fc8e751338a69063a134000c8352811da5dfecf33bac
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-29-cloud-agents-run-in-isolated-virtual-machines-with-full-development-environments|cursor-2026-06-29-40b244]]'
- '[[Changes/Claude Code/2026-07-01-subagents-now-run-in-the-background-by-default-so-claude-keeps-working-while-the|claude-code-2026-07-01-0bd143]]'
- '[[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|claude-code-2026-07-01-4d022c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8|claude-code-2026-07-06-v2-1-202-github-349856235-58e6d3e8]]'
theme: agent-mode
type: change
---

# Added a "Dynamic workflow size" setting in `/config` for controlling how large C

<!-- chronolog:begin region="description" -->
Added a "Dynamic workflow size" setting in `/config` for controlling how large Claude generally makes dynamic workflows (small/medium/large agent counts) — an advisory guideline, not an enforced cap
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a "Dynamic workflow size" setting in `/config` for controlling how large Claude generally makes dynamic workflows (small/medium/large agent counts) — an advisory guideline, not an enforced cap
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.202
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-01-added-background-agent-notifications-in-claude-agents-sessions-that-need-input-o|claude-code-2026-07-01-4d022c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1096
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes