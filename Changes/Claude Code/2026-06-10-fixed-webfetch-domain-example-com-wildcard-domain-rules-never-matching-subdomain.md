---
card_id: claude-code-2026-06-10-c26bef
date: '2026-06-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1151
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 7577bdecf9f7425902ab06391381664412c8dce10696dc11161fd0c64d05fdeb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-10-c26bef
  comparison: ''
  date: '2026-06-10'
  description: 'Claude Code — v2.1.172: Fixed `WebFetch(domain:*.example.com)` wildcard
    domain rules never matching subdomains in allow, deny, and ask position, and file
    permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`)
    being rejected at startup'
  evidence:
  - quote: Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching
      subdomains in allow, deny, and ask position, and file permission rules with
      mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at
      startup
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain
  source_release: claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching
    subd
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]'
- '[[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|claude-code-2026-06-08-55bad2]]'
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|claude-code-2026-06-08-d4c97e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c]]'
source_type: github_releases
theme: safety-privacy
title: Fixed WebFetch(domain:.example.com) wildcard domain rules never matching subd
type: change
---

# Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subd

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.172: Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
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
- Lag Days: 1151
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes