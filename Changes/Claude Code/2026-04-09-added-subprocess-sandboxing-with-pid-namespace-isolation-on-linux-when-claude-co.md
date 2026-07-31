---
card_id: claude-code-2026-04-09-5db0ee
date: '2026-04-09'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1089
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 630dd811ea5a2c7deb8bc039b4fdd6be3002245664e2bd7bf6ed8c134d75617e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]'
- '[[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]'
- '[[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
theme: safety-privacy
type: change
---

# Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_C

<!-- chronolog:begin region="description" -->
Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1089
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes