---
card_id: claude-code-2026-06-15-1d14c3
date: '2026-06-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1075
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|claude-code-2026-06-10-78521c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c0a23aad8914789a6a3f274df5fb54e2377c971532f164036195064c41b1e663
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-04-by-default-a-local-sdk-agent-runs-tool-calls-without-asking-for-approval-since-t|cursor-2026-06-04-ee9248]]'
- '[[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|cursor-2026-06-05-70abae]]'
- '[[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|claude-code-2026-06-10-78521c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
theme: agent-mode
type: change
---

# Improved auto mode: subagent spawns are now evaluated by the classifier before l

<!-- chronolog:begin region="description" -->
Improved auto mode: subagent spawns are now evaluated by the classifier before launch, closing a gap where a subagent could request a blocked action without review
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved auto mode: subagent spawns are now evaluated by the classifier before launch, closing a gap where a subagent could request a blocked action without review
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|claude-code-2026-06-10-78521c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1075
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes