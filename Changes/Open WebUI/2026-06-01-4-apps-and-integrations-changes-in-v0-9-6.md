---
card_id: open-webui-2026-06-01-ced557
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Apps and Integrations: 4 changes in v0.9.6
  — \U0001F4D1 **MinerU file type configuration.** Administrators can now configure
  which file types…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 12af8c6ccee04fccc6c69908174bb1e4de87468ef3262486760d1b32cc95ecbc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-ced557
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 4 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F4D1 **MinerU file type configuration.** Administrators can now
      configure which file types are processed by the MinerU document loader, via
      the new \"MINERU_FILE_EXTENSIONS\" setting, extending it beyond PDF to formats
      like DOCX, PPTX, and XLSX. [Commit](https://github.com/open-webui/open-webui/commit/d4030a8aa5d48c2a1cb06c461566844aca2530ab)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: ⏱️ **Configurable MCP connection timeout.** The timeout for the initial
      handshake with an MCP tool server is now configurable via the new "MCP_INITIALIZE_TIMEOUT"
      setting, so servers that are slow to start or expose many tools can finish connecting
      instead of timing out. [#25011](https://github.com/open-webui/open-webui/pull/25011),
      [Commit](https://github.com/open-webui/open-webui/commit/4297c02b121180e239a61c483ac8477cc557d4ef)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6D1 **Stream termination for pipe functions.** Streamed responses
      from pipe functions now always send the standard end-of-stream marker, so chat
      clients and external integrations reliably detect when a response is complete
      instead of waiting on streams that already finished. [#24763](https://github.com/open-webui/open-webui/pull/24763)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F517 **Placeholders in MCP connection headers.** Custom header templates
      configured on MCP server connections now have their \"{{USER_ID}}\", \"{{USER_NAME}}\",
      \"{{USER_EMAIL}}\", \"{{USER_ROLE}}\", \"{{CHAT_ID}}\", and \"{{MESSAGE_ID}}\"
      placeholders interpolated at request time, matching how custom headers already
      work for direct connections and tool servers. [#24822](https://github.com/open-webui/open-webui/pull/24822)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-apps-and-integrations-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v0.9.6
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-01-elevenagents|ElevenAgents]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5
  Apps and Integrations changes in v1.0.57]]'
- '[[Changes/Lovable/2026-06-01-app-connector-salesforce|App connector: Salesforce]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📑 **MinerU file type configuration.** Administrators can now configure which file types are processed by the MinerU document loader, via the new "MINERU_FILE_EXTENSIONS" setting, extending it beyond PDF to formats like DOCX, PPTX, and XLSX. [Commit](https://github.com/open-webui/open-webui/commit/d4030a8aa5d48c2a1cb06c461566844aca2530ab)

> ⏱️ **Configurable MCP connection timeout.** The timeout for the initial handshake with an MCP tool server is now configurable via the new "MCP_INITIALIZE_TIMEOUT" setting, so servers that are slow to start or expose many tools can finish connecting instead of timing out. [#25011](https://github.com/open-webui/open-webui/pull/25011), [Commit](https://github.com/open-webui/open-webui/commit/4297c02b121180e239a61c483ac8477cc557d4ef)

> 🛑 **Stream termination for pipe functions.** Streamed responses from pipe functions now always send the standard end-of-stream marker, so chat clients and external integrations reliably detect when a response is complete instead of waiting on streams that already finished. [#24763](https://github.com/open-webui/open-webui/pull/24763)

> 🔗 **Placeholders in MCP connection headers.** Custom header templates configured on MCP server connections now have their "{{USER_ID}}", "{{USER_NAME}}", "{{USER_EMAIL}}", "{{USER_ROLE}}", "{{CHAT_ID}}", and "{{MESSAGE_ID}}" placeholders interpolated at request time, matching how custom headers already work for direct connections and tool servers. [#24822](https://github.com/open-webui/open-webui/pull/24822)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-01 · Lovable · [[Changes/Lovable/2026-06-01-app-connector-salesforce|App connector: Salesforce]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp now collapses claude.ai connectors you've never signed in to behind…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-ced557&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-4-apps-and-integrations-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-ced557%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->