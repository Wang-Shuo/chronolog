---
card_id: claude-code-2026-02-28-b47b10
date: '2026-02-28'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 968
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-20-added-support-for-isolation-worktree-in-agent-definitions-allowing-agents-to-dec|claude-code-2026-02-20-33fd37]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: f6fa7532343490c513333ac6993b329649218f1d8494c28cd4ec551e12c79829
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-02-24-after-onboarding-onto-your-codebase-each-agent-runs-in-its-own-isolated-vm-with|cursor-2026-02-24-9f5dee]]'
- '[[Changes/Cursor/2026-02-24-get-started-at-cursor-com-onboard-to-watch-the-agent-configure-itself-and-record|cursor-2026-02-24-c94da5]]'
- '[[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|cursor-2026-02-26-ef0b88]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c]]'
theme: agent-mode
type: change
---

# Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of runni

<!-- chronolog:begin region="description" -->
Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running a shell command
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running a shell command
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-20-added-support-for-isolation-worktree-in-agent-definitions-allowing-agents-to-dec|claude-code-2026-02-20-33fd37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 968
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes