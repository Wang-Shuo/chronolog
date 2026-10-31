---
card_id: claude-code-2026-08-18-b3a982
date: '2026-08-18'
description: 'Claude Code · 2026-08-18 · Reliability and Performance: 2 changes in
  v2.1.235 — Improved memory and CPU usage while cloud sessions such as `/ultrareview`
  or…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1342
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f849581cd14c62c0c80b096f24a2a4020dd6c1ccdab69c29853ceb2bf3d51e4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-18-b3a982
  comparison: ''
  date: '2026-08-18'
  description: 'Claude Code — v2.1.235: 2 Reliability and Performance changes'
  evidence:
  - quote: Improved memory and CPU usage while cloud sessions such as `/ultrareview`
      or `/autofix-pr` run in the background — their event streams are no longer re-scanned
      and re-rendered on every update
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.235
  - quote: 'Improved the embedded `grep` in native macOS/Linux builds: pathological
      patterns now fail fast instead of exhausting memory, and `-m N` with `-A/-C`
      prints correct context'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.235
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-235
  source_release: claude-code-2026-08-18-v2-1-235-github-372521030-3c3fae7f
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.235
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-10-improved-performance-fewer-event-loop-stalls-on-file-not-found-suggestions-and-a|Improved
  performance: fewer event-loop stalls on file-not-found suggestions…]]'
- '[[Changes/Cursor/2026-08-13-faster-starts|Faster starts]]'
- '[[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added
  opt-in memory cgroup support for Bash tool commands on Linux…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-18-v2-1-235-github-372521030-3c3fae7f|claude-code-2026-08-18-v2-1-235-github-372521030-3c3fae7f]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.235
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.235

**Claude Code** · 2026-08-18 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.235) · from [[Releases/Claude Code/claude-code-2026-08-18-v2-1-235-github-372521030-3c3fae7f|v2.1.235]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved memory and CPU usage while cloud sessions such as `/ultrareview` or `/autofix-pr` run in the background — their event streams are no longer re-scanned and re-rendered on every update

> Improved the embedded `grep` in native macOS/Linux builds: pathological patterns now fail fast instead of exhausting memory, and `-m N` with `-A/-C` prints correct context

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.235
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-18-improved-the-context-limit-error-to-say-when-auto-compact-is-off-and-point-to-co|Improved the context-limit error to say when auto-compact is off and point…]] · Context Window
- [[Changes/Claude Code/2026-08-18-remote-control-claude-rc-now-applies-the-same-enterprise-gateway-availability-ch|Remote Control: claude rc now applies the same enterprise-gateway availability…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-18-4-other-changes-in-v2-1-235|4 other changes in v2.1.235]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-08-14 · Claude Code · [[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added opt-in memory cgroup support for Bash tool commands on Linux…]]
- Later: 2026-08-19 · Claude Code · [[Changes/Claude Code/2026-08-19-improved-startup-performance-the-session-counter-is-now-written-in-the-backgroun|Improved startup performance: the session counter is now written in the background]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-18-b3a982&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-18-2-reliability-and-performance-changes-in-v2-1-235.md%0ACard%20ID%3A%20claude-code-2026-08-18-b3a982%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.235%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->