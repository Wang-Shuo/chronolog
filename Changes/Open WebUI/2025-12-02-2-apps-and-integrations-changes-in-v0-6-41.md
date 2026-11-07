---
card_id: open-webui-2025-12-02-fd6c87
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Apps and Integrations: 2 changes in v0.6.41
  — \U0001F50C A new API endpoint was added to directly get or create a Direct Message
  channel with…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2545
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b6600d36f9dd8e642de384a733377e16ce6d5d28cf7b986c1d9dd5e82dab554f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-fd6c87
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 2 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F50C A new API endpoint was added to directly get or create a Direct
      Message channel with a specific user by their ID, streamlining programmatic
      DM channel creation for integrations and frontend workflows. [Commit](https://github.com/open-webui/open-webui/commit/f589b7c1895a6a77166c047891acfa21bc0936c4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4DD MCP tool server configuration was corrected to properly handle
      the \"Function Name Filter List\" as both string and list types, preventing
      AttributeError when the field is empty and ensuring backward compatibility.
      [#19486](https://github.com/open-webui/open-webui/issues/19486), [Commit](https://github.com/open-webui/open-webui/commit/c5b73d71843edc024325d4a6e625ec939a747279),
      [Commit](https://github.com/open-webui/open-webui/commit/477097c2e42985c14892301d0127314629d07df1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-apps-and-integrations-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Cline/2025-12-02-feat-cerebras-add-x-cerebras-3rd-party-integration-header-by-sebastiand-cerebras|feat(cerebras):
  add X-Cerebras-3rd-Party-Integration header]]'
- '[[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3
  Apps and Integrations changes in rust-v0.64.0]]'
- '[[Changes/Gemini CLI/2025-12-02-9-apps-and-integrations-changes-in-v0-19-0|9 Apps
  and Integrations changes in v0.19.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔌 A new API endpoint was added to directly get or create a Direct Message channel with a specific user by their ID, streamlining programmatic DM channel creation for integrations and frontend workflows. [Commit](https://github.com/open-webui/open-webui/commit/f589b7c1895a6a77166c047891acfa21bc0936c4)

> 📝 MCP tool server configuration was corrected to properly handle the "Function Name Filter List" as both string and list types, preventing AttributeError when the field is empty and ensuring backward compatibility. [#19486](https://github.com/open-webui/open-webui/issues/19486), [Commit](https://github.com/open-webui/open-webui/commit/c5b73d71843edc024325d4a6e625ec939a747279), [Commit](https://github.com/open-webui/open-webui/commit/477097c2e42985c14892301d0127314629d07df1)

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
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-9-apps-and-integrations-changes-in-v0-19-0|9 Apps and Integrations changes in v0.19.0]]
- Later: 2025-12-03 · v0 · [[Changes/v0/2025-12-03-you-can-now-bring-your-own-mcps-to-v0|Bring your own MCPs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-fd6c87&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-2-apps-and-integrations-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-fd6c87%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->