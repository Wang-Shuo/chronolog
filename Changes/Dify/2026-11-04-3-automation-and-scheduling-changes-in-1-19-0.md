---
card_id: dify-2026-11-04-9e68e1
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Automation and Scheduling: 3 changes in v1.19.0
  - Trace Your Workflows, Layer by Layer — This release also makes Workflow Tools
  portable…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2604
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ca0f2e3d262bec4671cbf10b9b7e9d0f376594eea9328aa7f7dd194c8ed48b7
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-9e68e1
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 3 Automation
    and Scheduling changes'
  evidence:
  - quote: This release also makes Workflow Tools portable with App packages, adds
      Skill Hub automation, and makes Agent files easier to upload and preview. The
      bundled plugin daemon is upgraded to **0.6.14-local**.
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Rebuild the web application and restart API, worker, scheduler, and Agent
      services from the same release. Refresh the standalone Agent Backend's locked
      `server` dependencies when deploying it separately.
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Install the matching 1.19.0 client and use `difyctl help` to discover the
      current server catalog. Refresh installed agent skills with `difyctl install
      skills <dir>`. Workflow and Chatflow automation should use the revised `stop.run`
      operation; message-based apps use `stop.task`.
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-automation-and-scheduling-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: automation-scheduling
  title: 3 Automation and Scheduling changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-11-03-2-automation-and-scheduling-changes-in-v0-13-0|2
  Automation and Scheduling changes in v0.13.0]]'
- '[[Changes/OpenClaw/2026-11-03-4-automation-and-scheduling-changes-in-v2026-10-10|4
  Automation and Scheduling changes in v2026.10.10]]'
- '[[Changes/OpenHands/2026-11-03-6-automation-and-scheduling-changes-in-v1-35-0|6
  Automation and Scheduling changes in v1.35.0]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: automation-scheduling
title: 3 Automation and Scheduling changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Automation and Scheduling changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This release also makes Workflow Tools portable with App packages, adds Skill Hub automation, and makes Agent files easier to upload and preview. The bundled plugin daemon is upgraded to **0.6.14-local**.

> Rebuild the web application and restart API, worker, scheduler, and Agent services from the same release. Refresh the standalone Agent Backend's locked `server` dependencies when deploying it separately.

> Install the matching 1.19.0 client and use `difyctl help` to discover the current server catalog. Refresh installed agent skills with `difyctl install skills <dir>`. Workflow and Chatflow automation should use the revised `stop.run` operation; message-based apps use `stop.task`.

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Apps and Integrations
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-6-files-and-data-changes-in-1-19-0|6 Files and Data changes in 1.19.0]] · Files and Data
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-6-automation-and-scheduling-changes-in-v1-35-0|6 Automation and Scheduling changes in v1.35.0]]
- Later: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-keeps-the-windows-scheduled-task-available-during-update-recovery-until-the-gate|Keeps the Windows scheduled task available during update recovery until the Gateway…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-9e68e1&body=Card%3A%20Changes%2FDify%2F2026-11-04-3-automation-and-scheduling-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-9e68e1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->