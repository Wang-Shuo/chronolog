---
card_id: open-webui-2026-02-12-fbcbe3
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Apps and Integrations: 6 changes in v0.8.0
  — \U0001F6E1️ **MCP custom SSL certificates.** Administrators can now connect to
  MCP servers with…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2617
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3550f8a27977e8ce8a6d69d090a38552c99abf7f0695204a84918574090e19a2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-fbcbe3
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 6 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F6E1️ **MCP custom SSL certificates.** Administrators can now connect
      to MCP servers with self-signed or custom SSL certificates via the \"AIOHTTP_CLIENT_SESSION_TOOL_SERVER_SSL\"
      environment variable. [#20875](https://github.com/open-webui/open-webui/issues/20875),
      [Commit](https://github.com/open-webui/open-webui/commit/c7f996d593e4bb48103b91316204fe7e50e25b35)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F517 **Forward user info to tool servers.** User identity and chat
      context can now be forwarded to MCP servers and external tool servers when \"ENABLE_FORWARD_USER_INFO_HEADERS\"
      is enabled, allowing tool providers to implement per-user authorization, auditing,
      and rate limiting. [#21092](https://github.com/open-webui/open-webui/pull/21092),
      [Commit](https://github.com/open-webui/open-webui/commit/2c37daef86a058e370151ecead17f10078102307)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4EC **External tool event emitters.** External tools (OpenAPI/MCP)
      can now send tool events back to Open WebUI using the event emitter endpoint,
      as message ID is now forwarded alongside chat ID when \"ENABLE_FORWARD_USER_INFO_HEADERS\"
      is enabled. [#21214](https://github.com/open-webui/open-webui/pull/21214)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50C **MCP tools regression fix.** MCP tools now work reliably again
      after a regression in v0.7.2 that caused \"cannot pickle '_asyncio.Future' object\"
      errors when attempting to use MCP servers in chat. [#20629](https://github.com/open-webui/open-webui/issues/20629),
      [#20500](https://github.com/open-webui/open-webui/issues/20500), [Commit](https://github.com/open-webui/open-webui/commit/886c12c5664bc2dd73313330f61c2257169da6d1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5DD️ **SSL verification for embeddings.** SSL certificate verification
      now respects the \"AIOHTTP_CLIENT_SESSION_SSL\" setting for OpenAI and Azure
      OpenAI embedding requests, allowing connections to self-signed certificate endpoints
      when disabled. [Commit](https://github.com/open-webui/open-webui/commit/cd31b8301b38bfa86872608cfbd022ff74e3ae52)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F517 **Prompt ID-based URLs.** Prompts now use unique ID-based URLs
      instead of command-based URLs, allowing more flexible command renaming without
      breaking saved links or integrations. [#20945](https://github.com/open-webui/open-webui/pull/20945)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-apps-and-integrations-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-12-5-apps-and-integrations-changes-in-rust-v0-100-0|5
  Apps and Integrations changes in rust-v0.100.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-mcp-servers-respect-the-cwd-working-directory-property|MCP
  servers respect the cwd working directory property]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-2-apps-and-integrations-changes-in-v0-0-409|2
  Apps and Integrations changes in v0.0.409]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **MCP custom SSL certificates.** Administrators can now connect to MCP servers with self-signed or custom SSL certificates via the "AIOHTTP_CLIENT_SESSION_TOOL_SERVER_SSL" environment variable. [#20875](https://github.com/open-webui/open-webui/issues/20875), [Commit](https://github.com/open-webui/open-webui/commit/c7f996d593e4bb48103b91316204fe7e50e25b35)

> 🔗 **Forward user info to tool servers.** User identity and chat context can now be forwarded to MCP servers and external tool servers when "ENABLE_FORWARD_USER_INFO_HEADERS" is enabled, allowing tool providers to implement per-user authorization, auditing, and rate limiting. [#21092](https://github.com/open-webui/open-webui/pull/21092), [Commit](https://github.com/open-webui/open-webui/commit/2c37daef86a058e370151ecead17f10078102307)

> 📬 **External tool event emitters.** External tools (OpenAPI/MCP) can now send tool events back to Open WebUI using the event emitter endpoint, as message ID is now forwarded alongside chat ID when "ENABLE_FORWARD_USER_INFO_HEADERS" is enabled. [#21214](https://github.com/open-webui/open-webui/pull/21214)

> 🔌 **MCP tools regression fix.** MCP tools now work reliably again after a regression in v0.7.2 that caused "cannot pickle '_asyncio.Future' object" errors when attempting to use MCP servers in chat. [#20629](https://github.com/open-webui/open-webui/issues/20629), [#20500](https://github.com/open-webui/open-webui/issues/20500), [Commit](https://github.com/open-webui/open-webui/commit/886c12c5664bc2dd73313330f61c2257169da6d1)

> 🗝️ **SSL verification for embeddings.** SSL certificate verification now respects the "AIOHTTP_CLIENT_SESSION_SSL" setting for OpenAI and Azure OpenAI embedding requests, allowing connections to self-signed certificate endpoints when disabled. [Commit](https://github.com/open-webui/open-webui/commit/cd31b8301b38bfa86872608cfbd022ff74e3ae52)

> 🔗 **Prompt ID-based URLs.** Prompts now use unique ID-based URLs instead of command-based URLs, allowing more flexible command renaming without breaking saved links or integrations. [#20945](https://github.com/open-webui/open-webui/pull/20945)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-12-2-apps-and-integrations-changes-in-v0-0-409|2 Apps and Integrations changes in v0.0.409]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-core-use-promise-all-for-mcp-listtools-calls-to-improve-performance|Core Use Promise.all for MCP listTools calls to improve performance]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-fbcbe3&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-6-apps-and-integrations-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-fbcbe3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->