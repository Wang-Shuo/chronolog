---
card_id: open-webui-2025-12-02-a68232
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Files and Data: \U0001F40D SentenceTransformers
  embedding initialization was fixed by updating the transformers dependency to version
  4.57.3…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 922
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 3f7ed5c8a1fc773fec3aee6c91c4dd8838836374764bf1155b11150197672f08
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-a68232
  comparison: ''
  date: '2025-12-02'
  description: "Open WebUI — v0.6.41: \U0001F40D SentenceTransformers embedding initialization
    was fixed by updating the transformers dependency to version 4.57.3, resolving
    a regression in v0.6.40 where document ingestion failed with \"'NoneType' object
    has no attribute 'encode'\" errors due to a bug in transformers 4.57.2. [#19512](https://github.com/open-webui/open-webui/issues/19512),
    [#19513](https://github.com/open-webui/open-webui/pull/19513)"
  evidence:
  - quote: "\U0001F40D SentenceTransformers embedding initialization was fixed by
      updating the transformers dependency to version 4.57.3, resolving a regression
      in v0.6.40 where document ingestion failed with \"'NoneType' object has no attribute
      'encode'\" errors due to a bug in transformers 4.57.2. [#19512](https://github.com/open-webui/open-webui/issues/19512),
      [#19513](https://github.com/open-webui/open-webui/pull/19513)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: file-data
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F40D SentenceTransformers embedding initialization was fixed by updating…"
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and
  Data changes in v0.6.37]]'
- '[[Changes/Dify/2025-11-26-3-files-and-data-changes-in-1-10-1|3 Files and Data changes
  in 1.10.1]]'
- '[[Changes/Cline/2025-11-27-docs-document-proxy-settings-by-dominiccooney-in-https-github-com-cline-cline-pu|docs:
  Document proxy settings]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: file-data
title: "\U0001F40D SentenceTransformers embedding initialization was fixed by updating…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🐍 SentenceTransformers embedding initialization was fixed by updating…

**Open WebUI** · 2025-12-02 · [[Themes/file-data|Files and Data]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🐍 SentenceTransformers embedding initialization was fixed by updating the transformers dependency to version 4.57.3, resolving a regression in v0.6.40 where document ingestion failed with "'NoneType' object has no attribute 'encode'" errors due to a bug in transformers 4.57.2. [#19512](https://github.com/open-webui/open-webui/issues/19512), [#19513](https://github.com/open-webui/open-webui/pull/19513)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
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
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2025-11-27 · Cline · [[Changes/Cline/2025-11-27-docs-document-proxy-settings-by-dominiccooney-in-https-github-com-cline-cline-pu|docs: Document proxy settings]]
- Later: 2025-12-11 · Dify · [[Changes/Dify/2025-12-11-5-files-and-data-changes-in-1-11-0|5 Files and Data changes in 1.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-a68232&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor.md%0ACard%20ID%3A%20open-webui-2025-12-02-a68232%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->