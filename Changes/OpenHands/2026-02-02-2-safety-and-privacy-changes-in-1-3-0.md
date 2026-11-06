---
card_id: openhands-2026-02-02-6d242b
date: '2026-02-02'
description: 'OpenHands · 2026-02-02 · Safety and Privacy: 2 changes in 1.3.0 - 2026-02-02
  — Added CORS support to Docker sandbox service for remote browser access. Users…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1023
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 25597578e23823a4dc86da20f1e94fe2b39689ee85974e84e7b803d6311b58d3
product: openhands
product_name: OpenHands
record:
  card_id: openhands-2026-02-02-6d242b
  comparison: ''
  date: '2026-02-02'
  description: 'OpenHands — 1.3.0 - 2026-02-02: 2 Safety and Privacy changes'
  evidence:
  - quote: Added CORS support to Docker sandbox service for remote browser access.
      Users running OpenHands on remote servers should set `WEB_HOST` environment
      variable (e.g., WEB_HOST=192.168.1.100:3000) along with `SANDBOX_CONTAINER_URL_PATTERN`
      for proper remote access configuration by @tofarr in https://github.com/OpenHands/OpenHands/pull/12489
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.3.0
  - quote: Added support for host networking mode via `OH_SANDBOX_USE_HOST_NETWORK=true`.
      This enables reverse proxy setups to access user-launched applications on any
      port, not just the predefined worker ports by @MkDev11 in https://github.com/OpenHands/OpenHands/pull/12445
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.3.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openhands
  product_name: OpenHands
  slug: 2-safety-and-privacy-changes-in-1-3-0
  source_release: openhands-2026-02-02-1-3-0-github-282330882-2979c249
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in 1.3.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions
  now respect content-level ask over tool-level allow]]'
- '[[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP
  server support permission flags: --yolo, --allow-all, etc. and permissions config]]'
- '[[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety
  and Privacy changes in rust-v0.93.0]]'
source_release: '[[Releases/OpenHands/openhands-2026-02-02-1-3-0-github-282330882-2979c249|openhands-2026-02-02-1-3-0-github-282330882-2979c249]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in 1.3.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in 1.3.0

**OpenHands** · 2026-02-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/OpenHands/OpenHands/releases/tag/1.3.0) · from [[Releases/OpenHands/openhands-2026-02-02-1-3-0-github-282330882-2979c249|1.3.0 - 2026-02-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added CORS support to Docker sandbox service for remote browser access. Users running OpenHands on remote servers should set `WEB_HOST` environment variable (e.g., WEB_HOST=192.168.1.100:3000) along with `SANDBOX_CONTAINER_URL_PATTERN` for proper remote access configuration by @tofarr in https://github.com/OpenHands/OpenHands/pull/12489

> Added support for host networking mode via `OH_SANDBOX_USE_HOST_NETWORK=true`. This enables reverse proxy setups to access user-launched applications on any port, not just the predefined worker ports by @MkDev11 in https://github.com/OpenHands/OpenHands/pull/12445

Source: https://github.com/OpenHands/OpenHands/releases/tag/1.3.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-31 · Codex CLI · [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]]
- Later: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openhands-2026-02-02-6d242b&body=Card%3A%20Changes%2FOpenHands%2F2026-02-02-2-safety-and-privacy-changes-in-1-3-0.md%0ACard%20ID%3A%20openhands-2026-02-02-6d242b%0ASource%3A%20https%3A%2F%2Fgithub.com%2FOpenHands%2FOpenHands%2Freleases%2Ftag%2F1.3.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->