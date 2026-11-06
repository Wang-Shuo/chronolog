---
card_id: dify-2026-11-04-7a56da
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Collaboration: 4 changes in v1.19.0 - Trace Your
  Workflows, Layer by Layer — **Existing `shared.env` files remain supported.** Common
  API…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1260
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eec4e16bccade3b73cdeed587e3b255508e8f561477c124af2bbbeb7af2574eb
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-7a56da
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 4 Collaboration
    changes'
  evidence:
  - quote: '**Existing `shared.env` files remain supported.** Common API, worker,
      and Beat customizations now belong in `docker/envs/core-services/api-worker.env`.
      Compose still reads legacy `docker/envs/core-services/shared.env` first, then
      `api-worker.env`, so `api-worker.env` wins when both set conflicting values.
      Root `docker/.env` takes precedence over both. An unchanged copy of `api-worker.defaults`
      preserves existing `shared.env` customizations. See the [Docker configuration
      guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.19.0/docker/README.md#review-configuration-after-an-upgrade).
      (#45376)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: Consolidate delivery through the shared provider interface for Langfuse,
      LangSmith, Opik, Weave, Arize, Phoenix, Aliyun, MLflow, Databricks, and Tencent.
      Retryable exports resend the same trace unit with deterministic identifiers.
      (#44673)
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Tracing secrets and egress:** configuration reads no longer return saved
      credentials, destination changes require secret re-entry, and provider traffic
      uses the shared outbound policy. (#44673)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'For Docker, use `envs/core-services/api-worker.defaults` as the reference
      for common API/worker/Beat settings and `api-worker.env` for new overrides.
      Existing `shared.env` remains compatible. Tracked defaults load automatically;
      root `.env` and explicit service overrides still take precedence. Review the
      [service-specific references](https://github.com/langgenius/dify/tree/laipz8200/release-1.19.0/docker/envs)
      rather than replacing local files with fresh templates. (#45359, #45376)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-collaboration-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: collaboration
  title: 4 Collaboration changes in 1.19.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-30-see-progress-and-next-steps-when-you-publish|See progress
  and next steps when you publish]]'
- "[[Changes/Open WebUI/2026-11-03-new-chats-stay-in-sync-a-chat-started-from-the-home-page-keeps-syncing-with-the|\U0001F503
  New chats stay in sync. A chat started from the home page keeps syncing…]]"
- '[[Changes/OpenHands/2026-11-03-2-collaboration-changes-in-v1-35-0|2 Collaboration
  changes in v1.35.0]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: collaboration
title: 4 Collaboration changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Collaboration changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Existing `shared.env` files remain supported.** Common API, worker, and Beat customizations now belong in `docker/envs/core-services/api-worker.env`. Compose still reads legacy `docker/envs/core-services/shared.env` first, then `api-worker.env`, so `api-worker.env` wins when both set conflicting values. Root `docker/.env` takes precedence over both. An unchanged copy of `api-worker.defaults` preserves existing `shared.env` customizations. See the [Docker configuration guide](https://github.com/langgenius/dify/blob/laipz8200/release-1.19.0/docker/README.md#review-configuration-after-an-upgrade). (#45376)

> Consolidate delivery through the shared provider interface for Langfuse, LangSmith, Opik, Weave, Arize, Phoenix, Aliyun, MLflow, Databricks, and Tencent. Retryable exports resend the same trace unit with deterministic identifiers. (#44673)

> **Tracing secrets and egress:** configuration reads no longer return saved credentials, destination changes require secret re-entry, and provider traffic uses the shared outbound policy. (#44673)

> For Docker, use `envs/core-services/api-worker.defaults` as the reference for common API/worker/Beat settings and `api-worker.env` for new overrides. Existing `shared.env` remains compatible. Tracked defaults load automatically; root `.env` and explicit service overrides still take precedence. Review the [service-specific references](https://github.com/langgenius/dify/tree/laipz8200/release-1.19.0/docker/envs) rather than replacing local files with fresh templates. (#45359, #45376)

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
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
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-2-collaboration-changes-in-v1-35-0|2 Collaboration changes in v1.35.0]]
- Later: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-7a56da&body=Card%3A%20Changes%2FDify%2F2026-11-04-4-collaboration-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-7a56da%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->