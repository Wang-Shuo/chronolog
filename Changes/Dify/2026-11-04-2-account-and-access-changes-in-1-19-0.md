---
card_id: dify-2026-11-04-fb3a95
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Account and Access: 2 changes in v1.19.0 - Trace
  Your Workflows, Layer by Layer — Persist refreshed OAuth credentials and serialize…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1315
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a9da32db8de09e5531e39825b1e6bcd5818b3352a81670eb5cc99d672dec3ab8
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-fb3a95
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 2 Account and
    Access changes'
  evidence:
  - quote: Persist refreshed OAuth credentials and serialize concurrent refreshes
      across tools and datasources, protecting rotating tokens and concurrent reauthorization.
      Temporary refresh failures return a temporary-unavailability response instead
      of incorrectly asking users to repair valid credentials. (#32195)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Report download HTTP failures instead of passing error pages to the plugin
      installer. Distinguish Squid-generated denial responses from upstream authentication
      errors, preserve GitHub import paths containing `blob`, and reject incompatible
      multipart file shapes consistently. (#44333, #44841, #44280, #44903)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-account-and-access-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in 1.19.0
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-11-03-saved-oauth-provider-settings-oauth-providers-now-load-their-saved-connection-se|\U0001F511
  Saved OAuth provider settings. OAuth providers now load their saved connection…]]"
- '[[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account
  and Access changes in v2026.10.10]]'
- '[[Changes/OpenHands/2026-11-03-ci-deps-bump-docker-login-action-from-4-6-0-to-4-7-0-in-the-actions-group-across|ci(deps):
  bump docker/login-action from 4.6.0 to 4.7.0 in the actions group across 1…]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Persist refreshed OAuth credentials and serialize concurrent refreshes across tools and datasources, protecting rotating tokens and concurrent reauthorization. Temporary refresh failures return a temporary-unavailability response instead of incorrectly asking users to repair valid credentials. (#32195)

> Report download HTTP failures instead of passing error pages to the plugin installer. Distinguish Squid-generated denial responses from upstream authentication errors, preserve GitHub import paths containing `blob`, and reject incompatible multipart file shapes consistently. (#44333, #44841, #44280, #44903)

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
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-ci-deps-bump-docker-login-action-from-4-6-0-to-4-7-0-in-the-actions-group-across|ci(deps): bump docker/login-action from 4.6.0 to 4.7.0 in the actions group across 1…]]
- Later: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-4-account-and-access-changes-in-v2026-11-1|4 Account and Access changes in v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-fb3a95&body=Card%3A%20Changes%2FDify%2F2026-11-04-2-account-and-access-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-fb3a95%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->