---
card_id: open-webui-2026-09-21-1271a7
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Context Window: 3 changes in v0.11.4 — \U0001F511
  **Tokens stay out of logs.** A failure part way through signing in with an identity
  provider…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2560
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9e28cdb632d43b1c4b5dfe71b6091ec4fa1a0edbcc8d7b9c1f680846771ab2c4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-1271a7
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 3 Context Window changes'
  evidence:
  - quote: "\U0001F511 **Tokens stay out of logs.** A failure part way through signing
      in with an identity provider no longer writes the credentials it was handed
      into the application log, recording the provider and the error it reported instead.
      [#29709](https://github.com/open-webui/open-webui/pull/29709)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⏳ **Session expiry accuracy.** A session with an identity provider now
      expires with the token it actually calls with, rather than whichever of its
      two tokens ran out first, which renewed it early and dropped it whenever that
      failed. [Commit](https://github.com/open-webui/open-webui/commit/aaaf26fb8ede28854dd660b11b85ba6bafe64007)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F39A **Compaction threshold saves.** The context compaction threshold
      set in general settings now reaches the model parameters, where the value never
      left the page. [#30270](https://github.com/open-webui/open-webui/pull/30270),
      [#30269](https://github.com/open-webui/open-webui/issues/30269)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-context-window-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-18-type-or-to-add-context-and-skills-where-you-type|Type
  @ or / to add context and skills where you type]]'
- '[[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context
  Window changes in v2026.9.5]]'
- '[[Changes/Devin/2026-09-21-rotate-bitbucket-data-center-tokens|Rotate Bitbucket
  Data Center Tokens]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔑 **Tokens stay out of logs.** A failure part way through signing in with an identity provider no longer writes the credentials it was handed into the application log, recording the provider and the error it reported instead. [#29709](https://github.com/open-webui/open-webui/pull/29709)

> ⏳ **Session expiry accuracy.** A session with an identity provider now expires with the token it actually calls with, rather than whichever of its two tokens ran out first, which renewed it early and dropped it whenever that failed. [Commit](https://github.com/open-webui/open-webui/commit/aaaf26fb8ede28854dd660b11b85ba6bafe64007)

> 🎚 **Compaction threshold saves.** The context compaction threshold set in general settings now reaches the model parameters, where the value never left the page. [#30270](https://github.com/open-webui/open-webui/pull/30270), [#30269](https://github.com/open-webui/open-webui/issues/30269)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-21 · Devin · [[Changes/Devin/2026-09-21-rotate-bitbucket-data-center-tokens|Rotate Bitbucket Data Center Tokens]]
- Later: 2026-09-22 · Cline · [[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window changes in v4.1.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-1271a7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-3-context-window-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-1271a7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->