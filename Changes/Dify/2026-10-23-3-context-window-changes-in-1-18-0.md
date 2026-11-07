---
card_id: dify-2026-10-23-43c9a5
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Context Window: 3 changes in v1.18.0 — Smarter Agent
  Routing, Portable Apps, Deeper Workflow Visibility — Workspace owners can create…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10708449f5dfc835cff561d5c7c5ff4ca15b04a4516c7d3e9959d5fd15fb182d
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-43c9a5
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 3 Context Window changes'
  evidence:
  - quote: 'Workspace owners can create resource access tokens bound to selected apps
      or knowledge bases. Tokens work with the supported Service API routes and app
      operations in difyctl; they do not grant workspace administration. The Settings
      entry is opt-in through `NEXT_PUBLIC_ENABLE_ACCESS_TOKEN`, which defaults to
      `false`. (#42293, #44422)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| Deployment-wide trajectories | `DIFY_AGENT_TRAJECTORY_ENABLED=false`,
      `DIFY_AGENT_TRAJECTORY_OTLP_TRACES_ENDPOINT`, `DIFY_AGENT_TRAJECTORY_OTLP_HEADERS`,
      and `DIFY_AGENT_TRAJECTORY_SERVICE_NAME`; content capture defaults to off and
      trace context defaults to `isolated`. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `a8c9e2f1b704` | Add resource access tokens and resource bindings. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-context-window-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in 1.18.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-10-22-ollama-launch-now-passes-cloud-models-context-lengths-and-capabilities-to-coding|ollama
  launch now passes cloud models'' context lengths and capabilities to coding…]]'
- '[[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context
  Window changes in v2026.10.6]]'
- '[[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context
  Window changes in rust-v0.164.0]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Workspace owners can create resource access tokens bound to selected apps or knowledge bases. Tokens work with the supported Service API routes and app operations in difyctl; they do not grant workspace administration. The Settings entry is opt-in through `NEXT_PUBLIC_ENABLE_ACCESS_TOKEN`, which defaults to `false`. (#42293, #44422)

> | Deployment-wide trajectories | `DIFY_AGENT_TRAJECTORY_ENABLED=false`, `DIFY_AGENT_TRAJECTORY_OTLP_TRACES_ENDPOINT`, `DIFY_AGENT_TRAJECTORY_OTLP_HEADERS`, and `DIFY_AGENT_TRAJECTORY_SERVICE_NAME`; content capture defaults to off and trace context defaults to `isolated`. |

> | `a8c9e2f1b704` | Add resource access tokens and resource bindings. |

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]]
- Later: 2026-10-23 · Ollama · [[Changes/Ollama/2026-10-23-nemotron-3-5-bolt-e4b-https-ollama-com-library-nemotron-3-5-bolt-is-nvidia-s-sma|Nemotron 3.5 Bolt E4B((source link) is NVIDIA’s…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-43c9a5&body=Card%3A%20Changes%2FDify%2F2026-10-23-3-context-window-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-43c9a5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->