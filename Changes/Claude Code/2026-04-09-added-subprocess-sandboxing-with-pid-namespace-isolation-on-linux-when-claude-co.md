---
card_id: claude-code-2026-04-09-5db0ee
date: '2026-04-09'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 8d95c1b457fada51bdf227332ccb582f64dae74ad1af6107d081c4ddd1ebda25
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-09-5db0ee
  comparison: ''
  date: '2026-04-09'
  description: 'Claude Code — v2.1.98: Added subprocess sandboxing with PID namespace
    isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS`
    env var to limit per-session script invocations'
  evidence:
  - quote: Added subprocess sandboxing with PID namespace isolation on Linux when
      `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env
      var to limit per-session script invocations
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_C
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]'
- '[[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]'
- '[[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
theme: safety-privacy
title: Added subprocess sandboxing with PID namespace isolation on Linux when CLAUDE_C
type: change
---

# Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_C

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.98: Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1089
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes