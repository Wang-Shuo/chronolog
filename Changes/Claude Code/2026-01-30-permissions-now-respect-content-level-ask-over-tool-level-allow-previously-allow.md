---
card_id: claude-code-2026-01-30-3cd8a3
date: '2026-01-30'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1020
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: e0e4fb0f58e4e800249027d138abc9f56366f8298532f73323760e26dcdef60a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-01-30-3cd8a3
  comparison: ''
  date: '2026-01-30'
  description: 'Claude Code — v2.1.27: Permissions now respect content-level `ask`
    over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed
    all bash commands, but will now permission prompt for `rm`.'
  evidence:
  - quote: 'Permissions now respect content-level `ask` over tool-level `allow`. Previously
      `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now
      permission prompt for `rm`.'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.27
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow
  source_release: claude-code-2026-01-30-v2-1-27-github-281663155-d003937d
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Permissions now respect content-level `ask` over tool-level `allow`. Previously
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-14-added-ability-to-provide-feedback-when-accepting-permission-prompts|claude-code-2026-01-14-835bd2]]'
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-30-v2-1-27-github-281663155-d003937d|claude-code-2026-01-30-v2-1-27-github-281663155-d003937d]]'
source_type: github_releases
theme: safety-privacy
title: Permissions now respect content-level ask over tool-level allow. Previously
type: change
---

# Permissions now respect content-level `ask` over tool-level `allow`. Previously

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.27: Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.27
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
- Lag Days: 1020
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes