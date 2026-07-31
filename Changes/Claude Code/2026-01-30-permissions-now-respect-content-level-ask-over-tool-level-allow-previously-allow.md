---
card_id: claude-code-2026-01-30-3cd8a3
date: '2026-01-30'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1020
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c01fa456488ca5dfc1cb351a82a8d8ffb25a1b4c5addb5dfc7d45b3f867d4a1f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-14-added-ability-to-provide-feedback-when-accepting-permission-prompts|claude-code-2026-01-14-835bd2]]'
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-30-v2-1-27-github-281663155-d003937d|claude-code-2026-01-30-v2-1-27-github-281663155-d003937d]]'
theme: safety-privacy
type: change
---

# Permissions now respect content-level `ask` over tool-level `allow`. Previously

<!-- chronolog:begin region="description" -->
Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.27
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1020
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes