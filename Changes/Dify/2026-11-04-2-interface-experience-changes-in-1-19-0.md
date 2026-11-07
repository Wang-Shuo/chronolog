---
card_id: dify-2026-11-04-df14ef
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Interface Experience: 2 changes in v1.19.0 - Trace
  Your Workflows, Layer by Layer — Keep newly created, user-maintained apps visible
  in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2761
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3863b64ec74fb4aeef1b03de7f8c56060ad02aca30ea7ffe0b53c8ff075df80d
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-df14ef
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 2 Interface
    Experience changes'
  evidence:
  - quote: 'Keep newly created, user-maintained apps visible in Studio and preserve
      primary navigation across Console routes. Calculate log-period boundaries from
      the current date. (#44929, #44633, #45360)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: For Workflow and Chatflow OpenAPI calls, use **`POST /openapi/v1/apps/{app_id}/runs/{run_id}:stop`**
      (`stop.run`) and **`GET /openapi/v1/apps/{app_id}/runs/{run_id}/events`** (`get.run.event`).
      Chat, Agent Chat, and Completion retain the task-ID stop route under `stop.task`.
      (#44587)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-interface-experience-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: interface-experience
  title: 2 Interface Experience changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-11-03-4-interface-experience-changes-in-v0-13-0|4 Interface
  Experience changes in v0.13.0]]'
- '[[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13
  Interface Experience changes in v2026.10.10]]'
- '[[Changes/OpenHands/2026-11-03-12-interface-experience-changes-in-v1-35-0|12 Interface
  Experience changes in v1.35.0]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: interface-experience
title: 2 Interface Experience changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Interface Experience changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Keep newly created, user-maintained apps visible in Studio and preserve primary navigation across Console routes. Calculate log-period boundaries from the current date. (#44929, #44633, #45360)

> For Workflow and Chatflow OpenAPI calls, use **`POST /openapi/v1/apps/{app_id}/runs/{run_id}:stop`** (`stop.run`) and **`GET /openapi/v1/apps/{app_id}/runs/{run_id}/events`** (`get.run.event`). Chat, Agent Chat, and Completion retain the task-ID stop route under `stop.task`. (#44587)

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Apps and Integrations
- [[Changes/Dify/2026-11-04-3-automation-and-scheduling-changes-in-1-19-0|3 Automation and Scheduling changes in 1.19.0]] · Automation and Scheduling
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-6-files-and-data-changes-in-1-19-0|6 Files and Data changes in 1.19.0]] · Files and Data
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-12-interface-experience-changes-in-v1-35-0|12 Interface Experience changes in v1.35.0]]
- Later: 2026-11-04 · Raycast · [[Changes/Raycast/2026-11-04-tip-assign-a-hotkey-like-alt-a-to-dictate-to-ai-for-even-quicker-access|Tip: Assign a hotkey like Alt + A to Dictate to AI for even quicker access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-df14ef&body=Card%3A%20Changes%2FDify%2F2026-11-04-2-interface-experience-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-df14ef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->