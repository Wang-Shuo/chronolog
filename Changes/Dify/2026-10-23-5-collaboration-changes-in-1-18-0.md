---
card_id: dify-2026-10-23-eac2ac
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Collaboration: 5 changes in v1.18.0 — Smarter Agent
  Routing, Portable Apps, Deeper Workflow Visibility — **Upgrade the Agent components…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2842
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e9c029c888fda4af3b165a299085bd082f98af3612bfdbaf1f1d44304ee1833e
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-eac2ac
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 5 Collaboration changes'
  evidence:
  - quote: '**Upgrade the Agent components together.** `/runs` now accepts composition
      v2 and rejects v1 requests. Existing session snapshots are converted on read
      and saved as v2; old runtimes cannot read newly saved v2 snapshots. Direct Agent
      Backend integrations must update their request format. The old Agent-specific
      AskHuman tool and deferred resume path are removed: historical Agent forms no
      longer resume execution, while shared Workflow Human Input nodes remain supported.
      (#43833)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Retire old workflow consumers before admitting new-version traffic.**
      Let in-flight runs finish, then replace legacy workers/resume consumers so they
      cannot process the shared queue without the new cancellation guards. Legacy
      paused task IDs can be recovered from valid saved invocation snapshots within
      the existing access scope; missing or invalid snapshots require separate recovery.
      Nested usage totals retain the limitation noted above. (#40277)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Review the proxy boundary.** Bundled Nginx replaces `X-Forwarded-For`
      with its resolved client address, and Compose enables forwarded-header handling.
      Keep direct API access restricted to trusted callers. If a load balancer or
      Cloudflare sits before Nginx, configure trusted real-IP handling there; otherwise
      visitors may share the proxy’s rate-limit bucket. See [client IP and trusted
      proxies](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/docker/README.md#client-ip-and-trusted-proxies).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Knowledge sharing defaults:** in RBAC-enabled deployments, new knowledge
      bases no longer automatically include every workspace member. (#42430)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Preserve LLM prompt/model changes during collaboration and synchronize
      imported graphs correctly. Code generation retains input bindings for surviving
      parameter names, understands multiline/destructured signatures and Python parameters
      containing commas, and preserves literal `{{inputs}}` text in user code. (#42124,
      #42817, #44075, #44046, #44337, #43438)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-collaboration-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: collaboration
  title: 5 Collaboration changes in 1.18.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-19-feat-verify-openhands-adopt-the-shared-known-bug-contract-by-enyst-in-https-gith|feat(verify-openhands):
  adopt the shared known-bug contract]]'
- '[[Changes/OpenClaw/2026-10-22-session-share-now-shows-an-error-when-it-can-t-discover-receivers-instead-of-an|Session
  Share now shows an error when it can’t discover receivers, instead…]]'
- '[[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration
  changes in rust-v0.164.0]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: collaboration
title: 5 Collaboration changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Collaboration changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Upgrade the Agent components together.** `/runs` now accepts composition v2 and rejects v1 requests. Existing session snapshots are converted on read and saved as v2; old runtimes cannot read newly saved v2 snapshots. Direct Agent Backend integrations must update their request format. The old Agent-specific AskHuman tool and deferred resume path are removed: historical Agent forms no longer resume execution, while shared Workflow Human Input nodes remain supported. (#43833)

> **Retire old workflow consumers before admitting new-version traffic.** Let in-flight runs finish, then replace legacy workers/resume consumers so they cannot process the shared queue without the new cancellation guards. Legacy paused task IDs can be recovered from valid saved invocation snapshots within the existing access scope; missing or invalid snapshots require separate recovery. Nested usage totals retain the limitation noted above. (#40277)

> **Review the proxy boundary.** Bundled Nginx replaces `X-Forwarded-For` with its resolved client address, and Compose enables forwarded-header handling. Keep direct API access restricted to trusted callers. If a load balancer or Cloudflare sits before Nginx, configure trusted real-IP handling there; otherwise visitors may share the proxy’s rate-limit bucket. See [client IP and trusted proxies](https://github.com/langgenius/dify/blob/laipz8200/release-1.18.0/docker/README.md#client-ip-and-trusted-proxies).

> **Knowledge sharing defaults:** in RBAC-enabled deployments, new knowledge bases no longer automatically include every workspace member. (#42430)

> Preserve LLM prompt/model changes during collaboration and synchronize imported graphs correctly. Code generation retains input bindings for surviving parameter names, understands multiline/destructured signatures and Python parameters containing commas, and preserves literal `{{inputs}}` text in user code. (#42124, #42817, #44075, #44046, #44337, #43438)

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]]
- Later: 2026-10-23 · Replit · [[Changes/Replit/2026-10-23-chat-and-asset-sharing|Chat and asset sharing]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-eac2ac&body=Card%3A%20Changes%2FDify%2F2026-10-23-5-collaboration-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-eac2ac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->