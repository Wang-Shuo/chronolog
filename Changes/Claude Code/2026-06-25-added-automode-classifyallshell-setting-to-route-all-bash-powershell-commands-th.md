---
card_id: claude-code-2026-06-25-f40f80
date: '2026-06-25'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1085
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-25-added-auto-mode-denial-reasons-to-the-transcript-the-denial-toast-and-permission|claude-code-2026-06-25-1a6f27]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ac3bafc8f47310f1a1229bd9b3bea789ebf2f8b291d4ecf4773622fc3b8a71e3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-22-added-teammatemode-iterm2-setting-with-a-warning-when-auto-mode-cannot-find-the|claude-code-2026-06-22-3c587e]]'
- '[[Changes/Claude Code/2026-06-22-added-status-filtering-press-f-to-the-workflows-agent-detail-view|claude-code-2026-06-22-f1d8a2]]'
- '[[Changes/Claude Code/2026-06-25-added-auto-mode-denial-reasons-to-the-transcript-the-denial-toast-and-permission|claude-code-2026-06-25-1a6f27]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
theme: agent-mode
type: change
---

# Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands

<!-- chronolog:begin region="description" -->
Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands through the auto-mode classifier instead of only arbitrary-code-execution patterns
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands through the auto-mode classifier instead of only arbitrary-code-execution patterns
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-25-added-auto-mode-denial-reasons-to-the-transcript-the-denial-toast-and-permission|claude-code-2026-06-25-1a6f27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1085
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes