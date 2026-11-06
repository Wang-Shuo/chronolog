---
card_id: open-webui-2025-08-21-a2a461
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Other changes: 23 changes in v0.6.23 — \U0001F4AC
  **Language-Aware Follow-Up Suggestions**: Enhanced the AI's follow-up question generation
  to…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ab692f1f72452ef5e88fcfc5c50d14399c17f6a8e05db08ad034fd661201f55b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-a2a461
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 23 other changes'
  evidence:
  - quote: "\U0001F4AC **Language-Aware Follow-Up Suggestions**: Enhanced the AI's
      follow-up question generation to dynamically adapt to the primary language of
      the current chat. Follow-up prompts will now be suggested in the same language
      the user and AI are conversing in, ensuring more natural and contextually relevant
      interactions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved Settings UI Reactivity and Visibility**: Resolved
      an issue where settings tabs for 'Connections' and 'Tools' did not dynamically
      update their visibility based on global administrative feature flags (e.g.,
      'enable_direct_connections'). The UI now reactively shows or hides these sections,
      ensuring a consistent and clear experience when administrators control feature
      availability."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4E6 **Fixed Stale Ollama Version in Docker Images**: Resolved an
      issue where the Ollama installation within Docker images could become stale
      due to caching during the build process. The Dockerfile now includes a mechanism
      to invalidate the build cache for the Ollama installation step, ensuring that
      the latest version of Ollama is always installed."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5C4️ **Improved Milvus Query Handling for Large Datasets**: Fixed
      a \"MilvusException\" that occurred when attempting to query more than 16384
      entries from a Milvus collection. The query logic has been refactored to use
      \"query_iterator()\", enabling efficient fetching of larger result sets in batches
      and resolving the previous limitation on the number of entries that could be
      retrieved."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4AC **Resolved Streaming Interruption for Kimi-Dev Models**: Fixed
      an issue where streaming responses from Kimi-Dev models would halt prematurely
      upon encountering specific 'thinking' tokens (◁think▷, ◁/think▷). The system
      now correctly processes these tokens, ensuring uninterrupted streaming and proper
      handling of hidden or collapsible thinking sections."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F50D **Enhanced Knowledge Base Search Functionality**: Improved
      the search capability within the 'Knowledge' section of the Workspace. Previously,
      searching for knowledge bases required exact term matches or starting with the
      first letter. Now, the search algorithm has been refined to allow broader, less
      exact matches, making it easier and more intuitive to find relevant knowledge
      bases."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F3A8 **Resolved Icon Overlap in 'Her' Theme**: Fixed a visual glitch
      in the 'Her' theme where icons would overlap on the loading screen and certain
      icons appeared incongruous. The display has been corrected to ensure proper
      visual presentation and theme consistency."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F50D **Resolved DDGS Concurrent Request Configuration**: Fixed an
      issue where the configured number of concurrent requests was not being honored
      for the DDGS (Dux Distributed Global Search) metasearch engine. The system now
      correctly applies the specified concurrency setting, improving efficiency for
      web searches."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Resolved Duplicate Tool Name Collision**: Fixed an issue
      where tools with identical names from different external servers were silently
      removed, preventing their simultaneous use. The system now correctly handles
      tool name collisions by internally prefixing tools with their server identifier,
      allowing multiple instances of similarly named tools from different servers
      to be active and usable by LLMs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5C4️ **Resolved S3 Vector Upload Limitations**: Fixed an issue
      that prevented uploading more than 500 vectors to S3 Vector buckets due to API
      limitations, which resulted in a \"ValidationException\". S3 vector uploads
      are now batched in groups of 500, ensuring successful processing of larger datasets."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Fixed Tool Installation Error During Startup**: Resolved
      a \"NoneType\" error that occurred during tool installation at startup when
      'tool.user' was unexpectedly null. The system now includes a check to ensure
      'tool.user' exists before attempting to access its properties, preventing crashes
      and ensuring robust tool initialization."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5BC️ **Resolved S3-Compatible Storage Upload Failures**: Fixed
      an issue where uploads to S3-compatible storage providers would fail with an
      \"XAmzContentSHA256Mismatch\" error. The system now correctly handles checksum
      calculations, ensuring reliable file and image uploads to S3-compatible services."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F3A8 **Resolved Banner Dismissal Issue with Iteration IDs**: Fixed
      a bug where dismissing banners could lead to unintended multiple banner dismissals
      or other incorrect behavior, especially when banners lacked unique iteration
      IDs. Unique IDs are now assigned during banner iteration, ensuring proper individual
      dismissal and consistent display behavior."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5C2️ **Core Directory Path Resolution Updated**: The internal mechanism
      for resolving core application directory paths (\"OPEN_WEBUI_DIR\", \"BACKEND_DIR\",
      \"BASE_DIR\") has been updated to use canonical resolution via \"Path().resolve()\".
      This change improves path reliability but may require adjustments for any external
      scripts or configurations that previously relied on specific non-canonical path
      interpretations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '@timovanasten, @mahenning, @olivier-lacroix, @FukkenShit, @PeterDaveHello,
      @BoFFire, @adamoutler, @silentoplayz, @Classic298, @koflerm, @Gyarbij, @expruc,
      @decent-engineer-decent-datascientist, @kahghi, @Kylapaallikko, @athoik, @rgaricano,
      @Rain6435, @ShirasawaSama, @0xThresh, @SebastienLentzAM, @tremlin, @tcx4c70,
      @joaoback'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '**Tailscale** <a href="https://tailscale.com/blog/self-host-a-local-ai-stack/?utm_source=OpenWebUI&utm_medium=paid-ad-placement&utm_campaign=OpenWebUI-Docs"
      target="_blank">'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '<img src="https://docs.openwebui.com/sponsors/banners/tailscale-banner.png"
      alt="tailscale" style="width: 8rem; height: 8rem; border-radius: .75rem;" />'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '**Warp** <a href="https://warp.dev/open-webui" target="_blank">'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '<img src="https://docs.openwebui.com/sponsors/banners/warp-banner.png"
      alt="warp" style="width: 8rem; height: 8rem; border-radius: .75rem;" />'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '@amd, @agency-agency, @roosi-gmbh, @feddersen-group, @SRKConsulting, @mushmax,
      @rndmcnlly, @icanbwell, @Krambu-Travis, @loitragg, @GenieDev101, @CubicleGangster,
      @GitDatamind, @TOWaB, @TheZigGroup, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz,
      @JrdnHans, @hkosm, @VeroFess'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 23-other-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: uncategorized
  title: 23 other changes in v0.6.23
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: uncategorized
title: 23 other changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 23 other changes in v0.6.23

**Open WebUI** · 2025-08-21 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💬 **Language-Aware Follow-Up Suggestions**: Enhanced the AI's follow-up question generation to dynamically adapt to the primary language of the current chat. Follow-up prompts will now be suggested in the same language the user and AI are conversing in, ensuring more natural and contextually relevant interactions.

> 🛠️ **Improved Settings UI Reactivity and Visibility**: Resolved an issue where settings tabs for 'Connections' and 'Tools' did not dynamically update their visibility based on global administrative feature flags (e.g., 'enable_direct_connections'). The UI now reactively shows or hides these sections, ensuring a consistent and clear experience when administrators control feature availability.

> 📦 **Fixed Stale Ollama Version in Docker Images**: Resolved an issue where the Ollama installation within Docker images could become stale due to caching during the build process. The Dockerfile now includes a mechanism to invalidate the build cache for the Ollama installation step, ensuring that the latest version of Ollama is always installed.

> 🗄️ **Improved Milvus Query Handling for Large Datasets**: Fixed a "MilvusException" that occurred when attempting to query more than 16384 entries from a Milvus collection. The query logic has been refactored to use "query_iterator()", enabling efficient fetching of larger result sets in batches and resolving the previous limitation on the number of entries that could be retrieved.

> 💬 **Resolved Streaming Interruption for Kimi-Dev Models**: Fixed an issue where streaming responses from Kimi-Dev models would halt prematurely upon encountering specific 'thinking' tokens (◁think▷, ◁/think▷). The system now correctly processes these tokens, ensuring uninterrupted streaming and proper handling of hidden or collapsible thinking sections.

> 🔍 **Enhanced Knowledge Base Search Functionality**: Improved the search capability within the 'Knowledge' section of the Workspace. Previously, searching for knowledge bases required exact term matches or starting with the first letter. Now, the search algorithm has been refined to allow broader, less exact matches, making it easier and more intuitive to find relevant knowledge bases.

> 🎨 **Resolved Icon Overlap in 'Her' Theme**: Fixed a visual glitch in the 'Her' theme where icons would overlap on the loading screen and certain icons appeared incongruous. The display has been corrected to ensure proper visual presentation and theme consistency.

> 🔍 **Resolved DDGS Concurrent Request Configuration**: Fixed an issue where the configured number of concurrent requests was not being honored for the DDGS (Dux Distributed Global Search) metasearch engine. The system now correctly applies the specified concurrency setting, improving efficiency for web searches.

> 🛠️ **Resolved Duplicate Tool Name Collision**: Fixed an issue where tools with identical names from different external servers were silently removed, preventing their simultaneous use. The system now correctly handles tool name collisions by internally prefixing tools with their server identifier, allowing multiple instances of similarly named tools from different servers to be active and usable by LLMs.

> 🗄️ **Resolved S3 Vector Upload Limitations**: Fixed an issue that prevented uploading more than 500 vectors to S3 Vector buckets due to API limitations, which resulted in a "ValidationException". S3 vector uploads are now batched in groups of 500, ensuring successful processing of larger datasets.

> 🛠️ **Fixed Tool Installation Error During Startup**: Resolved a "NoneType" error that occurred during tool installation at startup when 'tool.user' was unexpectedly null. The system now includes a check to ensure 'tool.user' exists before attempting to access its properties, preventing crashes and ensuring robust tool initialization.

> 🖼️ **Resolved S3-Compatible Storage Upload Failures**: Fixed an issue where uploads to S3-compatible storage providers would fail with an "XAmzContentSHA256Mismatch" error. The system now correctly handles checksum calculations, ensuring reliable file and image uploads to S3-compatible services.

> 🎨 **Resolved Banner Dismissal Issue with Iteration IDs**: Fixed a bug where dismissing banners could lead to unintended multiple banner dismissals or other incorrect behavior, especially when banners lacked unique iteration IDs. Unique IDs are now assigned during banner iteration, ensuring proper individual dismissal and consistent display behavior.

> 🗂️ **Core Directory Path Resolution Updated**: The internal mechanism for resolving core application directory paths ("OPEN_WEBUI_DIR", "BACKEND_DIR", "BASE_DIR") has been updated to use canonical resolution via "Path().resolve()". This change improves path reliability but may require adjustments for any external scripts or configurations that previously relied on specific non-canonical path interpretations.

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @timovanasten, @mahenning, @olivier-lacroix, @FukkenShit, @PeterDaveHello, @BoFFire, @adamoutler, @silentoplayz, @Classic298, @koflerm, @Gyarbij, @expruc, @decent-engineer-decent-datascientist, @kahghi, @Kylapaallikko, @athoik, @rgaricano, @Rain6435, @ShirasawaSama, @0xThresh, @SebastienLentzAM, @tremlin, @tcx4c70, @joaoback

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> **Tailscale** \<a href="https://tailscale.com/blog/self-host-a-local-ai-stack/?utm_source=OpenWebUI&utm_medium=paid-ad-placement&utm_campaign=OpenWebUI-Docs" target="_blank">

> \<img src="https://docs.openwebui.com/sponsors/banners/tailscale-banner.png" alt="tailscale" style="width: 8rem; height: 8rem; border-radius: .75rem;" />

> **Warp** \<a href="https://warp.dev/open-webui" target="_blank">

> \<img src="https://docs.openwebui.com/sponsors/banners/warp-banner.png" alt="warp" style="width: 8rem; height: 8rem; border-radius: .75rem;" />

> @amd, @agency-agency, @roosi-gmbh, @feddersen-group, @SRKConsulting, @mushmax, @rndmcnlly, @icanbwell, @Krambu-Travis, @loitragg, @GenieDev101, @CubicleGangster, @GitDatamind, @TOWaB, @TheZigGroup, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-a2a461&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-23-other-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-a2a461%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->