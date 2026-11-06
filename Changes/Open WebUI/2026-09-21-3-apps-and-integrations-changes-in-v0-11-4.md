---
card_id: open-webui-2026-09-21-9a5c6c
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Apps and Integrations: 3 changes in v0.11.4
  — \U0001F4D8 **Direct connection guidance.** The connections and integrations pages
  in the…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee4aaf5d038e400dcfee16540d3ec0daaa7aea5e91022593d9aea1ef81e4cd8a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-9a5c6c
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 3 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F4D8 **Direct connection guidance.** The connections and integrations
      pages in the personal settings now say plainly that a direct connection leans
      on your browser session to keep requests running, which suits testing and temporary
      use rather than everyday work. [Commit](https://github.com/open-webui/open-webui/commit/5d66dd6ad291db17894953714c01fd4303093e7e),
      [Commit](https://github.com/open-webui/open-webui/commit/15e2259a2ae1b7dec1f93a52078304dd3a79a14c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA9D **Responses API tool strictness.** A workspace tool, MCP server
      or OpenAPI server reaching a model on the Responses API was turned into a strict
      schema where it had never asked to be, so the model filled every optional field
      with empty strings, zeros and empty arrays, and search and filter tools were
      handed values where leaving them out was meant. [#30046](https://github.com/open-webui/open-webui/pull/30046),
      [#27750](https://github.com/open-webui/open-webui/issues/27750)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA9B **Paginated MCP tool lists.** A server that hands its tools
      back a page at a time had only the first page read, so the rest were never offered
      to a model; the whole list is now collected before the tools are built. [Commit](https://github.com/open-webui/open-webui/commit/ffae4116a8d58a820f1770c41c69dafe4d51c881)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-apps-and-integrations-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6
  Apps and Integrations changes in v2.1.277]]'
- '[[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8
  Apps and Integrations changes in v1.0.87]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📘 **Direct connection guidance.** The connections and integrations pages in the personal settings now say plainly that a direct connection leans on your browser session to keep requests running, which suits testing and temporary use rather than everyday work. [Commit](https://github.com/open-webui/open-webui/commit/5d66dd6ad291db17894953714c01fd4303093e7e), [Commit](https://github.com/open-webui/open-webui/commit/15e2259a2ae1b7dec1f93a52078304dd3a79a14c)

> 🪝 **Responses API tool strictness.** A workspace tool, MCP server or OpenAPI server reaching a model on the Responses API was turned into a strict schema where it had never asked to be, so the model filled every optional field with empty strings, zeros and empty arrays, and search and filter tools were handed values where leaving them out was meant. [#30046](https://github.com/open-webui/open-webui/pull/30046), [#27750](https://github.com/open-webui/open-webui/issues/27750)

> 🪛 **Paginated MCP tool lists.** A server that hands its tools back a page at a time had only the first page read, so the rest were never offered to a model; the whole list is now collected before the tools are built. [Commit](https://github.com/open-webui/open-webui/commit/ffae4116a8d58a820f1770c41c69dafe4d51c881)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
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
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8 Apps and Integrations changes in v1.0.87]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-9a5c6c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-3-apps-and-integrations-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-9a5c6c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->