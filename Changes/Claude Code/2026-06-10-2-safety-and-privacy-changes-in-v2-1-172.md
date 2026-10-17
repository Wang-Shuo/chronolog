---
card_id: claude-code-2026-06-10-30c00f
date: '2026-06-10'
description: 'Claude Code · 2026-06-10 · Safety and Privacy: 2 changes in v2.1.172
  — Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains…'
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
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bf389c533aefce2c4b750742b73dd5fc6d0deccb8ef91e86e036fcbf1f908eca
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-10-30c00f
  comparison: ''
  date: '2026-06-10'
  description: 'Claude Code — v2.1.172: 2 Safety and Privacy changes'
  evidence:
  - quote: Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching
      subdomains in allow, deny, and ask position, and file permission rules with
      mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at
      startup
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
  - quote: '[VSCode] Fixed PowerShell tool calls rendering as raw JSON instead of
      a proper command display and permission dialog, and stripped ANSI escape codes
      from displayed shell output'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-172
  source_release: claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.172
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]]'
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened
  cross-session messaging]]'
- '[[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety
  and Privacy changes in v2.1.169]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.172
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.172

**Claude Code** · 2026-06-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.172) · from [[Releases/Claude Code/claude-code-2026-06-10-v2-1-172-github-337412034-dc68562c|v2.1.172]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position, and file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup

> [VSCode] Fixed PowerShell tool calls rendering as raw JSON instead of a proper command display and permission dialog, and stripped ANSI escape codes from displayed shell output

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.172
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-10-2-developer-workflow-changes-in-v2-1-172|2 Developer Workflow changes in v2.1.172]] · Developer Workflow
- [[Changes/Claude Code/2026-06-10-3-apps-and-integrations-changes-in-v2-1-172|3 Apps and Integrations changes in v2.1.172]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-10-improved-performance-in-long-conversations-by-removing-redundant-message-normali|Improved performance in long conversations by removing redundant message…]] · Reliability and Performance
- [[Changes/Claude Code/2026-06-10-disable-mouse-tracking-on-windows-consoles-that-don-t-fully-support-it|Disable mouse tracking on Windows consoles that don't fully support it]] · Mobile and Desktop
- [[Changes/Claude Code/2026-06-10-sub-agents-can-now-spawn-their-own-sub-agents-up-to-5-levels-deep|Sub-agents can now spawn their own sub-agents (up to 5 levels deep)]] · Agent Mode
- [[Changes/Claude Code/2026-06-10-stopped-promoting-loop-in-remote-sessions-where-pending-loops-don-t-keep-the-con|Stopped promoting /loop in remote sessions, where pending loops don't keep…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-06-10-2-model-support-changes-in-v2-1-172|2 Model Support changes in v2.1.172]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety and Privacy changes in v2.1.169]]
- Later: 2026-06-10 · Cursor · [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before you push]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-10-30c00f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-10-2-safety-and-privacy-changes-in-v2-1-172.md%0ACard%20ID%3A%20claude-code-2026-06-10-30c00f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.172%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->