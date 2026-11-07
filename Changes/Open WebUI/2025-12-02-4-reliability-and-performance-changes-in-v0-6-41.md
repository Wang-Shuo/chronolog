---
card_id: open-webui-2025-12-02-4fe3fd
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Reliability and Performance: 4 changes in
  v0.6.41 — \U0001F3D7️ Knowledge base file management was rebuilt with a dedicated
  database table…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2570
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5e94b84a5254f85db06e8d46eabf0db4439923472c445c7a04b5860fe659a6ad
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-4fe3fd
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 4 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F3D7️ Knowledge base file management was rebuilt with a dedicated
      database table replacing the previous JSON array storage, enabling pagination
      support for large knowledge bases, significantly faster file listing performance,
      and more reliable file-knowledge base relationship tracking. [Commit](https://github.com/open-webui/open-webui/commit/d19023288e2ca40f86e2dc3fd9f230540f3e70d7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F680 Milvus multitenancy vector database performance was improved
      by removing manual flush calls after upsert operations, eliminating rate limit
      errors and reducing load on etcd and MinIO/S3 storage by allowing Milvus to
      manage segment persistence automatically via its WAL and auto-flush policies.
      [#19680](https://github.com/open-webui/open-webui/pull/19680)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: ✨ Various improvements were implemented across the frontend and backend
      to enhance performance, stability, and security.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4DE Redundant API calls on the admin user overview page were eliminated
      by consolidating reactive statements, reducing four duplicate requests to a
      single efficient call and significantly improving page load performance. [#19509](https://github.com/open-webui/open-webui/issues/19509),
      [Commit](https://github.com/open-webui/open-webui/commit/9f89cc5e9f7e1c6c9e2bc91177e08df7c79f66f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-reliability-and-performance-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: reliability-performance
  title: 4 Reliability and Performance changes in v0.6.41
  type: change
related_changes:
- '[[Changes/HeyGen/2025-11-29-speed-mode-provides-fast-reliable-translation-in-175-languages-accents-and-diale|Speed
  Mode provides fast, reliable translation in 175+ languages, accents, and dialects]]'
- '[[Changes/HeyGen/2025-11-29-if-you-re-scaling-content-globally-you-now-have-clear-options-speed-when-you-nee|If
  you''re scaling content globally, you now have clear options]]'
- '[[Changes/HeyGen/2025-12-01-a-faster-cleaner-editing-experience|A faster, cleaner
  editing experience]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: reliability-performance
title: 4 Reliability and Performance changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Reliability and Performance changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏗️ Knowledge base file management was rebuilt with a dedicated database table replacing the previous JSON array storage, enabling pagination support for large knowledge bases, significantly faster file listing performance, and more reliable file-knowledge base relationship tracking. [Commit](https://github.com/open-webui/open-webui/commit/d19023288e2ca40f86e2dc3fd9f230540f3e70d7)

> 🚀 Milvus multitenancy vector database performance was improved by removing manual flush calls after upsert operations, eliminating rate limit errors and reducing load on etcd and MinIO/S3 storage by allowing Milvus to manage segment persistence automatically via its WAL and auto-flush policies. [#19680](https://github.com/open-webui/open-webui/pull/19680)

> ✨ Various improvements were implemented across the frontend and backend to enhance performance, stability, and security.

> 📞 Redundant API calls on the admin user overview page were eliminated by consolidating reactive statements, reducing four duplicate requests to a single efficient call and significantly improving page load performance. [#19509](https://github.com/open-webui/open-webui/issues/19509), [Commit](https://github.com/open-webui/open-webui/commit/9f89cc5e9f7e1c6c9e2bc91177e08df7c79f66f9)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-12-01 · HeyGen · [[Changes/HeyGen/2025-12-01-a-faster-cleaner-editing-experience|A faster, cleaner editing experience]]
- Later: 2025-12-04 · Codex CLI · [[Changes/Codex CLI/2025-12-04-2-reliability-and-performance-changes-in-rust-v0-65-0|2 Reliability and Performance changes in rust-v0.65.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-4fe3fd&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-4-reliability-and-performance-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-4fe3fd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->