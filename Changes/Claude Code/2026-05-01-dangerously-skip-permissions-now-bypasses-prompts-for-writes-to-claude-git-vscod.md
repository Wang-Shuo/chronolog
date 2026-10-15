---
card_id: claude-code-2026-05-01-92258f
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1111
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 9d88c737852eedf6ad572101c8c0b098ff97127eb163899f5e4bebb83557da82
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-01-92258f
  comparison: ''
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: `--dangerously-skip-permissions` now bypasses
    prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and
    other previously-protected paths (catastrophic removal commands still prompt as
    a safety net)'
  evidence:
  - quote: '`--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`,
      `.git/`, `.vscode/`, shell config files, and other previously-protected paths
      (catastrophic removal commands still prompt as a safety net)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: dangerously-skip-permissions-now-bypasses-prompts-for-writes-to-claude-git-vscod
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: safety-privacy
  title: '`--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`…'
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-30-vulnerability-scanner-runs-scheduled-scans-of-your-codebase-to-check-for-known-v|cursor-2026-04-30-67f1e8]]'
- '[[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|cursor-2026-04-30-701a64]]'
- '[[Changes/Cursor/2026-04-30-customize-cursor-managed-security-agents-by-adjusting-triggers-adding-your-own-i|cursor-2026-04-30-bbeb40]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: safety-privacy
title: --dangerously-skip-permissions now bypasses prompts for writes to .claude/…
type: change
---

# `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.126: `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
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
- Lag Days: 1111
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes