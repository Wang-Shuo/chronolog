---
card_id: open-webui-2026-06-01-74b2a0
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Search and Browsing: 9 changes in v0.9.6 —
  \U0001F9F0 **Filesystem tool for knowledge bases.** A new built-in tool, enabled
  via the…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2195
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d30cf4f258211d5d03c5ba193d9fbb3348cfc09c014ae96862c9597e63330e9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-74b2a0
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 9 Search and Browsing changes'
  evidence:
  - quote: "\U0001F9F0 **Filesystem tool for knowledge bases.** A new built-in tool,
      enabled via the \"ENABLE_KB_EXEC\" environment variable, lets AI models browse
      and search knowledge base contents using familiar filesystem commands such as
      'ls', 'cat', 'grep', 'find', 'head', 'tail', and 'sed', including pipes between
      them. [Commit](https://github.com/open-webui/open-webui/commit/5b125c24d4eae925d3287efa626595bab29d5c33),
      [Commit](https://github.com/open-webui/open-webui/commit/ecec86dd32aa396dd5a383e9be5b0f16c4346c48),
      [Commit](https://github.com/open-webui/open-webui/commit/9ef579ce4be5b82f9281b085a621fed5b04e0d26),
      [Commit](https://github.com/open-webui/open-webui/commit/2f642754ac6b8c430228a7fc289357a6c6652235),
      [Commit](https://github.com/open-webui/open-webui/commit/3b00e5721a60518ea317c4fd61a6d0d182961a2f),
      [Commit](https://github.com/open-webui/open-webui/commit/4e78b355efe0611f27fddef591c69f7c1259a9f6),
      [Commit](https://github.com/open-webui/open-webui/commit/74f95a9b0d6b89b241701422170d54e21e701baa),
      [Commit](https://github.com/open-webui/open-webui/commit/cc16e06c32de48bdf464db5814483a49f3527b63),
      [Commit](https://github.com/open-webui/open-webui/commit/1ea54c3217f487990b6a4c0f0d8ea675a479b6e1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F600 **Emoji picker in message input.** A new emoji button in the
      rich text formatting toolbar lets you browse and insert emojis directly into
      your messages. [#24704](https://github.com/open-webui/open-webui/pull/24704)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F3CE️ **More responsive web search under load.** Web search through
      SearXNG, Google PSE, Brave, Serper, and Serpstack now uses non-blocking network
      calls, so the server stays responsive to other users while a search is in flight,
      and concurrent multi-query searches complete faster. [Commit](https://github.com/open-webui/open-webui/commit/b94245d2ee191e8ef118bf9de1ff7539503bfec9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F30E **Linkup web search provider.** Administrators can now select
      Linkup as the web search provider from the admin settings, with options to configure
      the API key and search depth. [#24752](https://github.com/open-webui/open-webui/pull/24752),
      [Commit](https://github.com/open-webui/open-webui/commit/56c0d00e13c74d665124ec9f1cae78e83ca60b6a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F50D **Web search reliability.** Web search again fetches page content
      reliably with the default web loader engine, a new \"USER_AGENT\" environment
      variable lets administrators set a real browser user-agent so fetches aren't
      blocked by Cloudflare, Wikipedia, and other bot-detection systems, and the startup
      script no longer fails to launch when these new environment variables are unset.
      [#24560](https://github.com/open-webui/open-webui/issues/24560), [#24793](https://github.com/open-webui/open-webui/issues/24793),
      [#24683](https://github.com/open-webui/open-webui/pull/24683), [Commit](https://github.com/open-webui/open-webui/commit/f60733758272c4532cd032e518c9cd73f648043a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F525 **Firecrawl web search results.** Web search using Firecrawl
      now returns results correctly regardless of which response format the Firecrawl
      version uses. [#24712](https://github.com/open-webui/open-webui/pull/24712)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9EE **Message search and analytics consistency.** Edits, deletions,
      and branch changes made in a chat are now reflected in message search results
      and analytics counts instead of leaving stale entries behind. [#25205](https://github.com/open-webui/open-webui/pull/25205),
      [Commit](https://github.com/open-webui/open-webui/commit/aa06200f789a4c3fc54ea9a141cd347d76cda4c5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FA79 **Graceful handling of in-chat task failures.** When web search
      query generation, image prompt generation, or a tool call fails or references
      a missing tool, the chat now falls back or surfaces a clear error instead of
      breaking partway through the response. [#25038](https://github.com/open-webui/open-webui/issues/25038),
      [#25144](https://github.com/open-webui/open-webui/issues/25144), [Commit](https://github.com/open-webui/open-webui/commit/b64fd988f02b8a4295193892b24b00bdf635a4dc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001FA9F **Bing search CLI smoke test.** Running the Bing web-search
      module from the command line for a quick connectivity check no longer raises
      an error about missing arguments. [#24765](https://github.com/open-webui/open-webui/issues/24765),
      [#24768](https://github.com/open-webui/open-webui/pull/24768)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-search-and-browsing-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: search-browsing
  title: 9 Search and Browsing changes in v0.9.6
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-01-chatgpt-can-now-help-with-more-of-the-job-search-process-from-finding-relevant-l|Find
  live jobs and format your resume in ChatGPT]]'
- '[[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3
  Search and Browsing changes in rust-v0.136.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-2-search-and-browsing-changes-in-v1-0-57|2
  Search and Browsing changes in v1.0.57]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: search-browsing
title: 9 Search and Browsing changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Search and Browsing changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧰 **Filesystem tool for knowledge bases.** A new built-in tool, enabled via the "ENABLE_KB_EXEC" environment variable, lets AI models browse and search knowledge base contents using familiar filesystem commands such as 'ls', 'cat', 'grep', 'find', 'head', 'tail', and 'sed', including pipes between them. [Commit](https://github.com/open-webui/open-webui/commit/5b125c24d4eae925d3287efa626595bab29d5c33), [Commit](https://github.com/open-webui/open-webui/commit/ecec86dd32aa396dd5a383e9be5b0f16c4346c48), [Commit](https://github.com/open-webui/open-webui/commit/9ef579ce4be5b82f9281b085a621fed5b04e0d26), [Commit](https://github.com/open-webui/open-webui/commit/2f642754ac6b8c430228a7fc289357a6c6652235), [Commit](https://github.com/open-webui/open-webui/commit/3b00e5721a60518ea317c4fd61a6d0d182961a2f), [Commit](https://github.com/open-webui/open-webui/commit/4e78b355efe0611f27fddef591c69f7c1259a9f6), [Commit](https://github.com/open-webui/open-webui/commit/74f95a9b0d6b89b241701422170d54e21e701baa), [Commit](https://github.com/open-webui/open-webui/commit/cc16e06c32de48bdf464db5814483a49f3527b63), [Commit](https://github.com/open-webui/open-webui/commit/1ea54c3217f487990b6a4c0f0d8ea675a479b6e1)

> 😀 **Emoji picker in message input.** A new emoji button in the rich text formatting toolbar lets you browse and insert emojis directly into your messages. [#24704](https://github.com/open-webui/open-webui/pull/24704)

> 🏎️ **More responsive web search under load.** Web search through SearXNG, Google PSE, Brave, Serper, and Serpstack now uses non-blocking network calls, so the server stays responsive to other users while a search is in flight, and concurrent multi-query searches complete faster. [Commit](https://github.com/open-webui/open-webui/commit/b94245d2ee191e8ef118bf9de1ff7539503bfec9)

> 🌎 **Linkup web search provider.** Administrators can now select Linkup as the web search provider from the admin settings, with options to configure the API key and search depth. [#24752](https://github.com/open-webui/open-webui/pull/24752), [Commit](https://github.com/open-webui/open-webui/commit/56c0d00e13c74d665124ec9f1cae78e83ca60b6a)

> 🔍 **Web search reliability.** Web search again fetches page content reliably with the default web loader engine, a new "USER_AGENT" environment variable lets administrators set a real browser user-agent so fetches aren't blocked by Cloudflare, Wikipedia, and other bot-detection systems, and the startup script no longer fails to launch when these new environment variables are unset. [#24560](https://github.com/open-webui/open-webui/issues/24560), [#24793](https://github.com/open-webui/open-webui/issues/24793), [#24683](https://github.com/open-webui/open-webui/pull/24683), [Commit](https://github.com/open-webui/open-webui/commit/f60733758272c4532cd032e518c9cd73f648043a)

> 🔥 **Firecrawl web search results.** Web search using Firecrawl now returns results correctly regardless of which response format the Firecrawl version uses. [#24712](https://github.com/open-webui/open-webui/pull/24712)

> 🧮 **Message search and analytics consistency.** Edits, deletions, and branch changes made in a chat are now reflected in message search results and analytics counts instead of leaving stale entries behind. [#25205](https://github.com/open-webui/open-webui/pull/25205), [Commit](https://github.com/open-webui/open-webui/commit/aa06200f789a4c3fc54ea9a141cd347d76cda4c5)

> 🩹 **Graceful handling of in-chat task failures.** When web search query generation, image prompt generation, or a tool call fails or references a missing tool, the chat now falls back or surfaces a clear error instead of breaking partway through the response. [#25038](https://github.com/open-webui/open-webui/issues/25038), [#25144](https://github.com/open-webui/open-webui/issues/25144), [Commit](https://github.com/open-webui/open-webui/commit/b64fd988f02b8a4295193892b24b00bdf635a4dc)

> 🪟 **Bing search CLI smoke test.** Running the Bing web-search module from the command line for a quick connectivity check no longer raises an error about missing arguments. [#24765](https://github.com/open-webui/open-webui/issues/24765), [#24768](https://github.com/open-webui/open-webui/pull/24768)

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
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-2-search-and-browsing-changes-in-v1-0-57|2 Search and Browsing changes in v1.0.57]]
- Later: 2026-06-03 · Ollama · [[Changes/Ollama/2026-06-03-pi-web-search-setup-now-updates-only-when-a-newer-package-is-available|Pi web search setup now updates only when a newer package is available]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-74b2a0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-9-search-and-browsing-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-74b2a0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->