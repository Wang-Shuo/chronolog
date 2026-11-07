---
card_id: open-webui-2025-12-02-7c12f8
date: '2025-12-02'
description: 'Open WebUI · 2025-12-02 · Model Support: 9 changes in v0.6.41 — ☁️ Azure
  Document Intelligence model selection was added, allowing administrators to specify…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1058
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bff4e4b1b535da333952b0b5d910d0ae6dafc7052ab8ad0d0108119f3263efa8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-7c12f8
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 9 Model Support changes'
  evidence:
  - quote: ☁️ Azure Document Intelligence model selection was added, allowing administrators
      to specify which model to use for document processing via the "DOCUMENT_INTELLIGENCE_MODEL"
      environment variable or admin UI setting, with "prebuilt-layout" as the default.
      [#19692](https://github.com/open-webui/open-webui/pull/19692), [Docs:#872](https://github.com/open-webui/docs/pull/872)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F9E0 Custom models based on Ollama or OpenAI now properly inherit
      the connection type from their base model, ensuring they appear correctly in
      the \"Local\" or \"External\" model selection tabs instead of only appearing
      under \"All\". [#19183](https://github.com/open-webui/open-webui/issues/19183),
      [Commit](https://github.com/open-webui/open-webui/commit/39f7575)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F526 Model list filtering in workspaces was corrected to properly
      include models shared with user groups, ensuring members can view models they
      have write access to through group permissions. [#19461](https://github.com/open-webui/open-webui/issues/19461),
      [Commit](https://github.com/open-webui/open-webui/commit/69722ba973768a5f689f2e2351bf583a8db9bba8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4BE Model allowlist persistence in multi-worker deployments was
      fixed by implementing Redis-based shared state for the internal models dictionary,
      ensuring configuration changes are consistently visible across all worker processes.
      [#19395](https://github.com/open-webui/open-webui/issues/19395), [Commit](https://github.com/open-webui/open-webui/commit/b5e5617d7f7ad3e4eec9f15f4cc7f07cb5afc2fa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F916 Embedding model auto-update functionality was fixed to properly
      respect the \"RAG_EMBEDDING_MODEL_AUTO_UPDATE\" setting by correctly passing
      the flag to the model path resolver, ensuring models update as expected when
      the auto-update option is enabled. [#19687](https://github.com/open-webui/open-webui/pull/19687)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F9F9 Duplicate API calls on the workspace models page were eliminated
      by removing redundant model list fetching, reducing two identical requests to
      a single call and improving page responsiveness. [#19517](https://github.com/open-webui/open-webui/issues/19517),
      [Commit](https://github.com/open-webui/open-webui/commit/d1bbf6be7a4d1d53fa8ad46ca4f62fc4b2e6a8cb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F518 The model valves button was corrected to prevent unintended
      form submission by adding explicit button type attribute, ensuring it no longer
      triggers message sending when the input area contains text. [#19534](https://github.com/open-webui/open-webui/pull/19534)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F5D1️ Ollama model deletion was fixed by correcting the request
      payload format and ensuring the model selector properly displays the placeholder
      option. [Commit](https://github.com/open-webui/open-webui/commit/0f3156651c64bc5af188a65fc2908bdcecf30c74)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F504 The knowledge base API was restructured to support the new
      file relationship model."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-model-support-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Cline/2025-12-02-skip-reasoning-details-on-microwave-model-by-canvrno-in-https-github-com-cline-c|Skip
  reasoning_details on microwave model]]'
- '[[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model
  Support changes in rust-v0.64.0]]'
- '[[Changes/Gemini CLI/2025-12-02-5-model-support-changes-in-v0-19-0|5 Model Support
  changes in v0.19.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ☁️ Azure Document Intelligence model selection was added, allowing administrators to specify which model to use for document processing via the "DOCUMENT_INTELLIGENCE_MODEL" environment variable or admin UI setting, with "prebuilt-layout" as the default. [#19692](https://github.com/open-webui/open-webui/pull/19692), [Docs:#872](https://github.com/open-webui/docs/pull/872)

> 🧠 Custom models based on Ollama or OpenAI now properly inherit the connection type from their base model, ensuring they appear correctly in the "Local" or "External" model selection tabs instead of only appearing under "All". [#19183](https://github.com/open-webui/open-webui/issues/19183), [Commit](https://github.com/open-webui/open-webui/commit/39f7575)

> 🔦 Model list filtering in workspaces was corrected to properly include models shared with user groups, ensuring members can view models they have write access to through group permissions. [#19461](https://github.com/open-webui/open-webui/issues/19461), [Commit](https://github.com/open-webui/open-webui/commit/69722ba973768a5f689f2e2351bf583a8db9bba8)

> 💾 Model allowlist persistence in multi-worker deployments was fixed by implementing Redis-based shared state for the internal models dictionary, ensuring configuration changes are consistently visible across all worker processes. [#19395](https://github.com/open-webui/open-webui/issues/19395), [Commit](https://github.com/open-webui/open-webui/commit/b5e5617d7f7ad3e4eec9f15f4cc7f07cb5afc2fa)

> 🤖 Embedding model auto-update functionality was fixed to properly respect the "RAG_EMBEDDING_MODEL_AUTO_UPDATE" setting by correctly passing the flag to the model path resolver, ensuring models update as expected when the auto-update option is enabled. [#19687](https://github.com/open-webui/open-webui/pull/19687)

> 🧹 Duplicate API calls on the workspace models page were eliminated by removing redundant model list fetching, reducing two identical requests to a single call and improving page responsiveness. [#19517](https://github.com/open-webui/open-webui/issues/19517), [Commit](https://github.com/open-webui/open-webui/commit/d1bbf6be7a4d1d53fa8ad46ca4f62fc4b2e6a8cb)

> 🔘 The model valves button was corrected to prevent unintended form submission by adding explicit button type attribute, ensuring it no longer triggers message sending when the input area contains text. [#19534](https://github.com/open-webui/open-webui/pull/19534)

> 🗑️ Ollama model deletion was fixed by correcting the request payload format and ensuring the model selector properly displays the placeholder option. [Commit](https://github.com/open-webui/open-webui/commit/0f3156651c64bc5af188a65fc2908bdcecf30c74)

> 🔄 The knowledge base API was restructured to support the new file relationship model.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-5-model-support-changes-in-v0-19-0|5 Model Support changes in v0.19.0]]
- Later: 2025-12-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-12-03-add-apply-patch-toolchain-for-openai-codex-models|Add apply_patch toolchain for OpenAI Codex models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-7c12f8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-9-model-support-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-7c12f8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->