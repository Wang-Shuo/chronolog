---
card_id: claude-code-2026-07-21-5131b9
date: '2026-07-21'
description: 'Claude Code · 2026-07-21 · Reliability and Performance: Added warnings
  when transcript writes are failing (e.g. disk full) or when session saving is off
  due to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1314
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: e5ae50dde747ff4648af233abc7fbfba033828b36ab47270a0268b3ab2dc85fa
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-21-5131b9
  comparison: ''
  date: '2026-07-21'
  description: 'Claude Code — v2.1.217: Added warnings when transcript writes are
    failing (e.g. disk full) or when session saving is off due to an inherited environment
    variable, instead of losing transcripts silently'
  evidence:
  - quote: Added warnings when transcript writes are failing (e.g. disk full) or when
      session saving is off due to an inherited environment variable, instead of losing
      transcripts silently
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session
  source_release: claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added warnings when transcript writes are failing (e.g. disk full) or when
    session…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-08-auto-update-binary-downloads-now-stream-to-disk-instead-of-buffering-in-memory-c|Auto-update
  binary downloads now stream to disk instead of buffering in memory…]]'
- '[[Changes/Claude Code/2026-07-14-3-reliability-and-performance-changes-in-v2-1-208|3
  Reliability and Performance changes in v2.1.208]]'
- '[[Changes/Claude Code/2026-07-18-added-a-periodic-progress-heartbeat-for-long-running-tool-calls-that-previously|Added
  a periodic progress heartbeat for long-running tool calls that previously went…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
source_type: github_releases
theme: reliability-performance
title: Added warnings when transcript writes are failing (e.g. disk full) or when
  session…
type: change
---

<!-- chronolog:begin region="header" -->
# Added warnings when transcript writes are failing (e.g. disk full) or when session…

**Claude Code** · 2026-07-21 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.217) · from [[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|v2.1.217]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added warnings when transcript writes are failing (e.g. disk full) or when session saving is off due to an inherited environment variable, instead of losing transcripts silently
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-21-changed-the-login-expiry-warning-to-appear-3-days-before-expiry-instead-of-5|Changed the login-expiry warning to appear 3 days before expiry instead of 5]] · Account and Access
- [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|Improved footer PR badge links to be clickable hyperlinks even when terminal support…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-21-2-agent-mode-changes-in-v2-1-217|2 Agent Mode changes in v2.1.217]] · Agent Mode
- [[Changes/Claude Code/2026-07-21-added-emoji-shortcode-autocomplete-in-the-prompt-input-type-heart-to-insert-or-h|Added emoji shortcode autocomplete in the prompt input]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-a-periodic-progress-heartbeat-for-long-running-tool-calls-that-previously|Added a periodic progress heartbeat for long-running tool calls that previously went…]]
- Later: 2026-08-10 · Claude Code · [[Changes/Claude Code/2026-08-10-improved-performance-fewer-event-loop-stalls-on-file-not-found-suggestions-and-a|Improved performance: fewer event-loop stalls on file-not-found suggestions…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-21-5131b9&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-21-added-warnings-when-transcript-writes-are-failing-e-g-disk-full-or-when-session.md%0ACard%20ID%3A%20claude-code-2026-07-21-5131b9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.217%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->