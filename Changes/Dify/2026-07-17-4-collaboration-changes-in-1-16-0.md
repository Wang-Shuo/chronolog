---
card_id: dify-2026-07-17-58f474
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Collaboration: 4 changes in v1.16.0 — | `API_WEBSOCKET_WORKER_AMOUNT`
  | `1` | `docker/envs/core-services/shared.env.example` | Number of…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1150
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aa1312ba49b6764200610c950dca1b38de9a04e4ca0097e7de9801d918c7c154
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-58f474
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 4 Collaboration changes'
  evidence:
  - quote: '| `API_WEBSOCKET_WORKER_AMOUNT` | `1` | `docker/envs/core-services/shared.env.example`
      | Number of WebSocket API workers |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `WORKFLOW_GENERATION_TIMEOUT_MS` | `180000` | `docker/envs/core-services/shared.env.example`
      | Timeout for AI workflow generation |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: replace logger mock with caplog in workflow collaboration test by
      @ojasarora77 in https://github.com/langgenius/dify/pull/37971'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'refactor(tests): use caplog in workflow collaboration service tests (#37468)
      by @hikariming in https://github.com/langgenius/dify/pull/37991'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-collaboration-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: collaboration
  title: 4 Collaboration changes in 1.16.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-13-workspaces|Workspaces]]'
- '[[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration
  changes in v2026.7.1]]'
- '[[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration
  changes in v1.0.71]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: collaboration
title: 4 Collaboration changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Collaboration changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> | `API_WEBSOCKET_WORKER_AMOUNT` | `1` | `docker/envs/core-services/shared.env.example` | Number of WebSocket API workers |

> | `WORKFLOW_GENERATION_TIMEOUT_MS` | `180000` | `docker/envs/core-services/shared.env.example` | Timeout for AI workflow generation |

> test: replace logger mock with caplog in workflow collaboration test by @ojasarora77 in https://github.com/langgenius/dify/pull/37971

> refactor(tests): use caplog in workflow collaboration service tests (#37468) by @hikariming in https://github.com/langgenius/dify/pull/37991

Source: https://github.com/langgenius/dify/releases/tag/1.16.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-17-20-safety-and-privacy-changes-in-1-16-0|20 Safety and Privacy changes in 1.16.0]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-16-context-window-changes-in-1-16-0|16 Context Window changes in 1.16.0]] · Context Window
- [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Memory and Personalization
- [[Changes/Dify/2026-07-17-8-account-and-access-changes-in-1-16-0|8 Account and Access changes in 1.16.0]] · Account and Access
- [[Changes/Dify/2026-07-17-4-editor-experience-changes-in-1-16-0|4 Editor Experience changes in 1.16.0]] · Editor Experience
- [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]] · Voice and Audio
- [[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow changes in 1.16.0]] · Developer Workflow
- [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Apps and Integrations
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-12-model-support-changes-in-1-16-0|12 Model Support changes in 1.16.0]] · Model Support
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Agent Mode
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration changes in v1.0.71]]
- Later: 2026-07-21 · Codex CLI · [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-58f474&body=Card%3A%20Changes%2FDify%2F2026-07-17-4-collaboration-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-58f474%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->