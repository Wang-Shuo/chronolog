---
card_id: claude-code-2026-04-17-cd5737
date: '2026-04-17'
description: 'Claude Code · 2026-04-17 · Safety and Privacy: 6 changes in v2.1.113
  — Added `sandbox.network.deniedDomains` setting to block specific domains even when
  a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1097
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6255751235530d534d2f551c7eb094afdce6580f1c391972d95ca3d3d1868594
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-17-cd5737
  comparison: ''
  date: '2026-04-17'
  description: 'Claude Code — v2.1.113: 6 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.network.deniedDomains` setting to block specific domains
      even when a broader `allowedDomains` wildcard would otherwise permit them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: Running `cd <current-directory> && git …` no longer triggers a permission
      prompt when the `cd` is a no-op
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: 'Security: on macOS, `/private/{etc,var,tmp,home}` paths are now treated
      as dangerous removal targets under `Bash(rm:*)` allow rules'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: 'Security: Bash deny rules now match commands wrapped in `env`/`sudo`/`watch`/`ionice`/`setsid`
      and similar exec wrappers'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: 'Security: `Bash(find:*)` allow rules no longer auto-approve `find -exec`/`-delete`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  - quote: Fixed Bash `dangerouslyDisableSandbox` running commands outside the sandbox
      without a permission prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-113
  source_release: claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.113
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety
  and Privacy changes in v2.1.108]]'
- '[[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added
  /less-permission-prompts skill]]'
- '[[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety
  and Privacy changes in v2.1.111]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba|claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.113
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.113

**Claude Code** · 2026-04-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.113) · from [[Releases/Claude Code/claude-code-2026-04-17-v2-1-113-github-310525785-1b5293ba|v2.1.113]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.network.deniedDomains` setting to block specific domains even when a broader `allowedDomains` wildcard would otherwise permit them

> Running `cd <current-directory> && git …` no longer triggers a permission prompt when the `cd` is a no-op

> Security: on macOS, `/private/{etc,var,tmp,home}` paths are now treated as dangerous removal targets under `Bash(rm:*)` allow rules

> Security: Bash deny rules now match commands wrapped in `env`/`sudo`/`watch`/`ionice`/`setsid` and similar exec wrappers

> Security: `Bash(find:*)` allow rules no longer auto-approve `find -exec`/`-delete`

> Fixed Bash `dangerouslyDisableSandbox` running commands outside the sandbox without a permission prompt

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.113
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-17-3-developer-workflow-changes-in-v2-1-113|3 Developer Workflow changes in v2.1.113]] · Developer Workflow
- [[Changes/Claude Code/2026-04-17-remote-control-clients-can-now-query-file-autocomplete-suggestions|Remote Control clients can now query @-file autocomplete suggestions]] · Editor Experience
- [[Changes/Claude Code/2026-04-17-improved-loop-pressing-esc-now-cancels-pending-wakeups-and-wakeups-display-as-cl|Improved /loop: pressing Esc now cancels pending wakeups, and wakeups display…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-04-17-3-interface-experience-changes-in-v2-1-113|3 Interface Experience changes in v2.1.113]] · Interface Experience
- [[Changes/Claude Code/2026-04-17-extra-usage-now-works-from-remote-control-mobile-web-clients|/extra-usage now works from Remote Control (mobile/web) clients]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-17-improved-ultrareview-faster-launch-with-parallelized-checks-diffstat-in-the-laun|Improved /ultrareview: faster launch with parallelized checks, diffstat…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-17-subagents-that-stall-mid-stream-now-fail-with-a-clear-error-after-10-minutes-ins|Subagents that stall mid-stream now fail with a clear error after 10 minutes instead…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-16 · Claude Code · [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]]
- Later: 2026-04-18 · Claude Code · [[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed a crash in the permission dialog when an agent teams teammate requested tool…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-17-cd5737&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-17-6-safety-and-privacy-changes-in-v2-1-113.md%0ACard%20ID%3A%20claude-code-2026-04-17-cd5737%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.113%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->