---
card_id: dify-2026-11-04-bd62f1
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Voice and Audio: 2 changes in v1.19.0 - Trace Your
  Workflows, Layer by Layer — The PHP SDK serializes empty app inputs as JSON objects…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3040
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 58965ddc1f6f04bf0cb1c19e5014a7ec970a01d117e86cb80275d0fc772fd066
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-bd62f1
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 2 Voice and
    Audio changes'
  evidence:
  - quote: 'The PHP SDK serializes empty app inputs as JSON objects, avoids buffering
      streaming Workflow and text-to-audio responses, and sends `last_id` for conversation
      pagination while preserving its public method signature. (#44675, #44271, #44659)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Preserve annotation editor drafts and voice-input focus, and add the Simplified
      Chinese account-deletion success email template. (#44810, #44825, #45169, #43504)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-voice-and-audio-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: voice
  title: 2 Voice and Audio changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-11-03-voice-mode-remote-agents-redesigned-automations-and-jupyter-notebook-viewer|Voice
  mode, remote agents, redesigned Automations, and Jupyter notebook viewer]]'
- '[[Changes/Open WebUI/2026-11-03-4-voice-and-audio-changes-in-v0-13-0|4 Voice and
  Audio changes in v0.13.0]]'
- '[[Changes/OpenClaw/2026-11-03-6-voice-and-audio-changes-in-v2026-10-10|6 Voice
  and Audio changes in v2026.10.10]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: voice
title: 2 Voice and Audio changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Voice and Audio changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The PHP SDK serializes empty app inputs as JSON objects, avoids buffering streaming Workflow and text-to-audio responses, and sends `last_id` for conversation pagination while preserving its public method signature. (#44675, #44271, #44659)

> Preserve annotation editor drafts and voice-input focus, and add the Simplified Chinese account-deletion success email template. (#44810, #44825, #45169, #43504)

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
## Nearby in Voice and Audio

- Earlier: 2026-11-03 · OpenClaw · [[Changes/OpenClaw/2026-11-03-6-voice-and-audio-changes-in-v2026-10-10|6 Voice and Audio changes in v2026.10.10]]
- Later: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-7-voice-and-audio-changes-in-v2026-11-1|7 Voice and Audio changes in v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-bd62f1&body=Card%3A%20Changes%2FDify%2F2026-11-04-2-voice-and-audio-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-bd62f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->