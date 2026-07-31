---
card_id: claude-code-2026-06-15-f824ca
date: '2026-06-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1075
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|claude-code-2026-06-15-1d14c3]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: e6acc2e4120b50dba811bde2e82f70cfdd6ab55ae034bd6b9e5d59a5168eafba
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|cursor-2026-06-05-70abae]]'
- '[[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|claude-code-2026-06-10-78521c]]'
- '[[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|claude-code-2026-06-15-1d14c3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-15-v2-1-178-github-339741361-902bc427|claude-code-2026-06-15-v2-1-178-github-339741361-902bc427]]'
theme: agent-mode
type: change
---

# Nested `.claude/` directories: the agent, workflow, and output-style closest to

<!-- chronolog:begin region="description" -->
Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins when names collide; project-scope workflow saves now target the closest existing `.claude/workflows/`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Nested `.claude/` directories: the agent, workflow, and output-style closest to the working directory now wins when names collide; project-scope workflow saves now target the closest existing `.claude/workflows/`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.178
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-15-improved-auto-mode-subagent-spawns-are-now-evaluated-by-the-classifier-before-la|claude-code-2026-06-15-1d14c3]]
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