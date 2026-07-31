---
card_id: claude-code-2026-03-07-85bd62
date: '2026-03-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1056
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-24-fixed-a-security-issue-where-statusline-and-filesuggestion-hook-commands-could-e|claude-code-2026-02-24-b4a332]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 314dc37a0310db1e4a0223dbd366680360d83e87c2e5b9d533e31f976daa8fd9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-19-permission-suggestions-are-now-populated-when-safety-checks-trigger-an-ask-respo|claude-code-2026-02-19-e3327d]]'
- '[[Changes/Claude Code/2026-02-24-fixed-a-security-issue-where-statusline-and-filesuggestion-hook-commands-could-e|claude-code-2026-02-24-b4a332]]'
- '[[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|cursor-2026-03-05-9c8870]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0|claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0]]'
theme: safety-privacy
type: change
---

# Fixed false-positive permission prompts for compound bash commands containing he

<!-- chronolog:begin region="description" -->
Fixed false-positive permission prompts for compound bash commands containing heredoc commit messages
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed false-positive permission prompts for compound bash commands containing heredoc commit messages
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-24-fixed-a-security-issue-where-statusline-and-filesuggestion-hook-commands-could-e|claude-code-2026-02-24-b4a332]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1056
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes