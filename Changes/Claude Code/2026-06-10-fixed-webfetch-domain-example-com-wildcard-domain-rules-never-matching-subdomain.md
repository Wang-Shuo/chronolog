---
card_id: claude-code-2026-06-10-c26bef
date: '2026-06-10'
description: 'Claude Code · 2026-06-10 · Safety and Privacy: Fixed `WebFetch(domain:*.example.com)`
  wildcard domain rules never matching subdomains in allow, deny, and ask…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1151
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 6e69974d979e23d0ed8430894807679134623ef370659514498b344b1f121c40
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
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain
  source_release: claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened
  cross-session messaging]]'
- '[[Changes/Claude Code/2026-06-08-added-safe-mode-flag-and-claude-code-safe-mode-to-start-claude-code-with-all-cus|Added
  --safe-mode flag (and CLAUDE_CODE_SAFE_MODE) to start Claude Code with all…]]'
- '[[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|Fixed
  stale permission and dialog prompts reappearing every time you reattached…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c]]'
source_type: github_releases
superseded: true
theme: safety-privacy
title: Fixed WebFetch(domain:.example.com) wildcard domain rules never matching…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching…

**Claude Code** · 2026-06-10 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) · from [[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|v2.1.172]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-10-added-a-search-bar-when-browsing-a-marketplace-s-plugins-in-plugin|Added a search bar when browsing a marketplace's plugins in /plugin]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|Added model attribute to the claude_code.lines_of_code.count OTEL metric]] · Model Support
- [[Changes/Claude Code/2026-06-10-amazon-bedrock-now-reads-the-aws-region-from-aws-config-files-when-aws-region-is|Amazon Bedrock now reads the AWS region from ~/.aws config files when AWS_REGION…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-fixed-stale-permission-and-dialog-prompts-reappearing-every-time-you-reattached|Fixed stale permission and dialog prompts reappearing every time you reattached…]]
- Later: 2026-06-10 · Cursor · [[Changes/Cursor/2026-06-10-you-can-now-run-bugbot-and-security-review-with-review-before-pushing-code-revie|Run Bugbot and Security Review with /review before pushing code]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-10-c26bef&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-10-fixed-webfetch-domain-example-com-wildcard-domain-rules-never-matching-subdomain.md%0ACard%20ID%3A%20claude-code-2026-06-10-c26bef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.172%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->