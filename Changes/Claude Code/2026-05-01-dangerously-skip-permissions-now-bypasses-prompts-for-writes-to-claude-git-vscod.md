---
card_id: claude-code-2026-05-01-92258f
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1111
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|claude-code-2026-04-18-f53068]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 8800afdde1ab610e61c1e09baa96b493fb58cca98286dd42eb3502f365db0291
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-04-30-vulnerability-scanner-runs-scheduled-scans-of-your-codebase-to-check-for-known-v|cursor-2026-04-30-67f1e8]]'
- '[[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|cursor-2026-04-30-701a64]]'
- '[[Changes/Cursor/2026-04-30-vulnerability-scanner|cursor-2026-04-30-7bb8a5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
theme: safety-privacy
type: change
---

# `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`,

<!-- chronolog:begin region="description" -->
`--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|claude-code-2026-04-18-f53068]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1111
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes