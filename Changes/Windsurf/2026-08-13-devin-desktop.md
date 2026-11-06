---
card_id: windsurf-2026-08-13-2968e5
date: '2026-08-13'
description: 'Windsurf · 2026-08-13 · Mobile and Desktop: Faster sidebar for users
  with thousands of cached sessions: filtering, space grouping, and sorting now only
  process…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1248
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 496c00a69456345d4e80a8fbf5a279a050b12a25ca7f472b24b6fa2366864b47
product: windsurf
product_name: Windsurf
record:
  card_id: windsurf-2026-08-13-2968e5
  comparison: ''
  date: '2026-08-13'
  description: 'Windsurf — v3.7.25: Faster sidebar for users with thousands of cached
    sessions: filtering, space grouping, and sorting now only process the sessions
    actually fetched for display, eliminating multi-second lag after "Reload Window"
    or while scrolling.'
  evidence:
  - quote: 'Faster sidebar for users with thousands of cached sessions: filtering,
      space grouping, and sorting now only process the sessions actually fetched for
      display, eliminating multi-second lag after "Reload Window" or while scrolling.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-25
  - quote: 'Sessions appear immediately on startup: the agent sidebar and the Sessions
      board and list views are pre-populated from a per-session cache while the first
      session list request is still in flight. Mode and model selections, per-turn
      stats footers, turn and Fast Context feedback indicators, and pending in-editor
      diff review state now refresh from the server instead of being restored across
      restarts.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-25
  - quote: Automation and scheduled sessions are filtered on the server when the connector
      supports it, and fall back to the local filter otherwise.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-25
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: devin-desktop
  source_release: windsurf-2026-08-13-v3-7-25-ed4fb4e7
  source_type: windsurf_changelog
  theme: mobile-desktop
  title: Devin Desktop
  type: change
related_changes:
- '[[Changes/Windsurf/2026-08-10-devin-desktop|Devin Desktop]]'
- '[[Changes/Claude Code/2026-08-12-changed-self-hosted-runner-windows-startup-to-require-an-explicit-base-dir-there|Changed
  self-hosted runner Windows startup to require an explicit --base-dir]]'
- '[[Changes/Claude Code/2026-08-13-gateway-the-desktop-overlay-now-accepts-every-released-desktop-setting-was-11-ha|Gateway:
  the desktop: overlay now accepts every released Desktop setting…]]'
source_release: '[[Releases/Windsurf/windsurf-2026-08-13-v3-7-25-ed4fb4e7|windsurf-2026-08-13-v3-7-25-ed4fb4e7]]'
source_type: windsurf_changelog
theme: mobile-desktop
title: Devin Desktop
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Desktop

**Windsurf** · 2026-08-13 · [[Themes/mobile-desktop|Mobile and Desktop]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v3-7-25) · from [[Releases/Windsurf/windsurf-2026-08-13-v3-7-25-ed4fb4e7|v3.7.25]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Faster sidebar for users with thousands of cached sessions: filtering, space grouping, and sorting now only process the sessions actually fetched for display, eliminating multi-second lag after "Reload Window" or while scrolling.
>
> Sessions appear immediately on startup: the agent sidebar and the Sessions board and list views are pre-populated from a per-session cache while the first session list request is still in flight. Mode and model selections, per-turn stats footers, turn and Fast Context feedback indicators, and pending in-editor diff review state now refresh from the server instead of being restored across restarts.
>
> Automation and scheduled sessions are filtered on the server when the connector supports it, and fall back to the local filter otherwise.
>
> Source: https://docs.devin.ai/desktop/changelog#v3-7-25
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2026-08-13-devin-local|Devin Local]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-13 · Claude Code · [[Changes/Claude Code/2026-08-13-gateway-the-desktop-overlay-now-accepts-every-released-desktop-setting-was-11-ha|Gateway: the desktop: overlay now accepts every released Desktop setting…]]
- Later: 2026-08-14 · ChatGPT · [[Changes/ChatGPT/2026-08-14-work-in-the-built-in-browser-or-chrome-browser-actions-are-available-in-the-linu|Work in the built-in browser or Chrome]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2026-08-13-2968e5&body=Card%3A%20Changes%2FWindsurf%2F2026-08-13-devin-desktop.md%0ACard%20ID%3A%20windsurf-2026-08-13-2968e5%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v3-7-25%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->