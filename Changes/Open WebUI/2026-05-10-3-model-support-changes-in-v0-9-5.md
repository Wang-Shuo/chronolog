---
card_id: open-webui-2026-05-10-e56222
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Model Support: 3 changes in v0.9.5 — \U0001F4DD
  **Notes create and open reliability.** Creating new notes and opening existing notes
  no longer…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1217
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8c5b26c9536cc8bb7e76cc62c76dc64e54bd3279053648baa9b6743c655de885
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-e56222
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 3 Model Support changes'
  evidence:
  - quote: "\U0001F4DD **Notes create and open reliability.** Creating new notes and
      opening existing notes no longer fails with a TypeError caused by `is_pinned`
      being passed to the SQLAlchemy model on create, and passed twice to `NoteResponse`
      on read. [#24484](https://github.com/open-webui/open-webui/issues/24484), [#24486](https://github.com/open-webui/open-webui/pull/24486)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Model params exposure for read-only users.** The per-model
      API endpoint now strips the `params` dict (including system prompts) from responses
      to callers without write access, preventing read-only users from viewing admin-curated
      model configuration. [#24525](https://github.com/open-webui/open-webui/pull/24525)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F39B️ **Filter selector reactivity.** Model filter checkboxes now
      derive state reactively from the current filter list and selected IDs instead
      of capturing a one-time snapshot at mount, so checkboxes update correctly when
      model contexts or filter configurations change at runtime. [Commit](https://github.com/open-webui/open-webui/commit/d1ef5382377f590f97a6dbaee88f369e6d7c5f6f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-model-support-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.9.5
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-08-3-model-support-changes-in-v1-0-44|3 Model
  Support changes in v1.0.44]]'
- '[[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support
  changes in v0.9.3]]'
- '[[Changes/OpenCode/2026-05-09-3-model-support-changes-in-v1-14-44-2|3 Model Support
  changes in v1.14.44 + 2]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.9.5

**Open WebUI** · 2026-05-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📝 **Notes create and open reliability.** Creating new notes and opening existing notes no longer fails with a TypeError caused by `is_pinned` being passed to the SQLAlchemy model on create, and passed twice to `NoteResponse` on read. [#24484](https://github.com/open-webui/open-webui/issues/24484), [#24486](https://github.com/open-webui/open-webui/pull/24486)

> 🔐 **Model params exposure for read-only users.** The per-model API endpoint now strips the `params` dict (including system prompts) from responses to callers without write access, preventing read-only users from viewing admin-curated model configuration. [#24525](https://github.com/open-webui/open-webui/pull/24525)

> 🎛️ **Filter selector reactivity.** Model filter checkboxes now derive state reactively from the current filter list and selected IDs instead of capturing a one-time snapshot at mount, so checkboxes update correctly when model contexts or filter configurations change at runtime. [Commit](https://github.com/open-webui/open-webui/commit/d1ef5382377f590f97a6dbaee88f369e6d7c5f6f)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-09 · OpenCode · [[Changes/OpenCode/2026-05-09-3-model-support-changes-in-v1-14-44-2|3 Model Support changes in v1.14.44 + 2]]
- Later: 2026-05-10 · OpenCode · [[Changes/OpenCode/2026-05-10-core-provider-configs-and-api-responses-now-accept-models-marked-as-active|Core Provider configs and API responses now accept models marked as active]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-e56222&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-3-model-support-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-e56222%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->