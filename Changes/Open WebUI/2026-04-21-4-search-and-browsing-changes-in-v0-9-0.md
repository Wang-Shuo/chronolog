---
card_id: open-webui-2026-04-21-b1d34b
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Search and Browsing: 4 changes in v0.9.0 —
  \U0001F4CE **Attach previously uploaded files.** The chat input menu now includes
  a Files tab for…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 209f3b2b339a3bbb7ebe48a38df1872d195dd3f4d62d40809df5fc355239870f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-b1d34b
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 4 Search and Browsing changes'
  evidence:
  - quote: "\U0001F4CE **Attach previously uploaded files.** The chat input menu now
      includes a Files tab for browsing and attaching previously uploaded files, eliminating
      the need to re-upload files you have already shared. [Commit](https://github.com/open-webui/open-webui/commit/edb8971c7dbd974322c3207c4655ff66479c3ee2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F0 **Pipe tool access.** Pipe functions now receive built-in and
      MCP tools in **tools**, so tools like Web Search and code execution are available
      when enabled. [#23365](https://github.com/open-webui/open-webui/issues/23365)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F527 **Web search settings save reliability.** Saving web search
      configuration now works without server errors, so administrators can update
      \"WEB_FETCH_MAX_CONTENT_LENGTH\" and related retrieval settings successfully
      from the admin interface. [Commit](https://github.com/open-webui/open-webui/commit/36d02aa1477aa1b4e7fb59d022f99693ebfa8667),
      [#23127](https://github.com/open-webui/open-webui/issues/23127)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50D **Web search result count.** The built-in search_web tool now
      respects the admin-configured \"Search Result Count\" setting instead of always
      returning 5 results when using Native Function Calling mode. [#23488](https://github.com/open-webui/open-webui/pull/23488),
      [#23485](https://github.com/open-webui/open-webui/issues/23485)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-search-and-browsing-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: search-browsing
  title: 4 Search and Browsing changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-11-2-search-and-browsing-changes-in-rust-v0-120-0|2
  Search and Browsing changes in rust-v0.120.0]]'
- '[[Changes/Codex CLI/2026-04-15-17684-adjust-default-tool-search-result-caps-malone-oai|♯17684
  Adjust default tool search result caps @malone-oai]]'
- '[[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin
  workflows now include tabbed browsing, inline enable/disable toggles…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: search-browsing
title: 4 Search and Browsing changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📎 **Attach previously uploaded files.** The chat input menu now includes a Files tab for browsing and attaching previously uploaded files, eliminating the need to re-upload files you have already shared. [Commit](https://github.com/open-webui/open-webui/commit/edb8971c7dbd974322c3207c4655ff66479c3ee2)

> 🧰 **Pipe tool access.** Pipe functions now receive built-in and MCP tools in **tools**, so tools like Web Search and code execution are available when enabled. [#23365](https://github.com/open-webui/open-webui/issues/23365)

> 🔧 **Web search settings save reliability.** Saving web search configuration now works without server errors, so administrators can update "WEB_FETCH_MAX_CONTENT_LENGTH" and related retrieval settings successfully from the admin interface. [Commit](https://github.com/open-webui/open-webui/commit/36d02aa1477aa1b4e7fb59d022f99693ebfa8667), [#23127](https://github.com/open-webui/open-webui/issues/23127)

> 🔍 **Web search result count.** The built-in search_web tool now respects the admin-configured "Search Result Count" setting instead of always returning 5 results when using Native Function Calling mode. [#23488](https://github.com/open-webui/open-webui/pull/23488), [#23485](https://github.com/open-webui/open-webui/issues/23485)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-04-20 · Codex CLI · [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]]
- Later: 2026-05-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-01-research-uses-an-orchestrator-subagent-model-for-more-thorough-and-reliable-deep|/research uses an orchestrator/subagent model for more thorough and reliable deep…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-b1d34b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-4-search-and-browsing-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-b1d34b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->