---
card_id: open-webui-2025-12-21-caa362
date: '2025-12-21'
description: 'Open WebUI · 2025-12-21 · Other changes: 28 changes in v0.6.42 — > [!CAUTION]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 244a95d78f41728662eed20799dd6102bf7ce60cc820a6219c83bb8177fccafa
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-caa362
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 28 other changes'
  evidence:
  - quote: '> [!CAUTION]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: '> This release includes database schema changes; multi-worker, multi-server,
      or load-balanced deployments must update all instances simultaneously rather
      than performing rolling updates, as running mixed versions will cause application
      failures due to schema incompatibility between old and new instances.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: '> [!WARNING]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F30D The \"SEARXNG_LANGUAGE\" environment variable now allows configuring
      search language for SearXNG queries, replacing the hardcoded \"en-US\" default
      with a configurable setting that defaults to \"all\". [#19909](https://github.com/open-webui/open-webui/pull/19909)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F527 The \"RAG_EXTERNAL_RERANKER_TIMEOUT\" environment variable
      now allows configuring request timeouts for external reranker operations. [#20049](https://github.com/open-webui/open-webui/pull/20049),
      [#19900](https://github.com/open-webui/open-webui/issues/19900)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: ⏱️ The "WEB_LOADER_TIMEOUT" environment variable now allows configuring
      request timeouts for SafeWebBaseLoader operations. [#19804](https://github.com/open-webui/open-webui/pull/19804),
      [#19734](https://github.com/open-webui/open-webui/issues/19734)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F310 Translations for German, Danish, Finnish, Korean, Portuguese
      (Brazil), Simplified Chinese, Traditional Chinese, Catalan, and Spanish were
      enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4AD Text loss in the explanation feature when using the \"CHAT_STREAM_RESPONSE_CHUNK_MAX_BUFFER_SIZE\"
      environment variable was resolved by correcting newline handling in streaming
      responses. [#19829](https://github.com/open-webui/open-webui/pull/19829)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4DA Knowledge base batch file addition failures caused by Pydantic
      validation errors are now prevented by making the meta field optional in file
      metadata responses, allowing files without metadata to be processed correctly.
      [#20022](https://github.com/open-webui/open-webui/pull/20022), [#14220](https://github.com/open-webui/open-webui/issues/14220)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F39B️ Rate limiting errors (HTTP 429) with Brave Search free tier
      when generating multiple queries are now prevented through asyncio.Semaphore-based
      concurrency control applied globally to all search engines. [#20070](https://github.com/open-webui/open-webui/pull/20070),
      [#20003](https://github.com/open-webui/open-webui/issues/20003), [#14107](https://github.com/open-webui/open-webui/issues/14107),
      [#15134](https://github.com/open-webui/open-webui/issues/15134)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F6AB Channel API endpoint access is now correctly blocked when channels
      are globally disabled, preventing users with channel permissions from accessing
      channel data via API requests when the feature is turned off in admin settings.
      [#19957](https://github.com/open-webui/open-webui/pull/19957), [#19914](https://github.com/open-webui/open-webui/issues/19914)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F527 Pipeline settings save failures when valve properties contain
      null values are now handled correctly. [#19791](https://github.com/open-webui/open-webui/pull/19791)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F6E1️ Invalid PASSWORD_VALIDATION_REGEX_PATTERN configurations no
      longer cause startup warnings, with automatic fallback to the default pattern
      when regex compilation fails. [#20058](https://github.com/open-webui/open-webui/pull/20058)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4CB Log truncation issues in Docker deployments during application
      crashes were resolved by disabling Python stdio buffering, ensuring complete
      diagnostic output is captured. [#19844](https://github.com/open-webui/open-webui/issues/19844)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F524 File attachment container layout issues when using RTL languages
      were resolved by applying chat direction settings to file containers across
      all message types. [#19891](https://github.com/open-webui/open-webui/pull/19891),
      [#19742](https://github.com/open-webui/open-webui/issues/19742)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F39B️ Chat functionality failures caused by empty logit_bias parameter
      values are now prevented by properly handling empty strings in the parameter
      parsing middleware. [#19982](https://github.com/open-webui/open-webui/issues/19982)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4BE Cloned prompts and tools now correctly preserve their access
      control settings instead of being reset to null, preventing unintended visibility
      changes when duplicating private or restricted items. [#19960](https://github.com/open-webui/open-webui/pull/19960),
      [#19360](https://github.com/open-webui/open-webui/issues/19360)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F39A️ Text scale adjustment buttons in Interface Settings were fixed
      to correctly increment and decrement the scale value. [#19699](https://github.com/open-webui/open-webui/pull/19699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F3AD Group channel invite button text visibility in light theme
      was corrected to display properly against dark backgrounds. [#19828](https://github.com/open-webui/open-webui/issues/19828)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4C1 The move button is now hidden when no folders exist, preventing
      display of non-functional controls. [#19705](https://github.com/open-webui/open-webui/pull/19705)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4E6 Qdrant client dependency was updated to resolve startup version
      incompatibility warnings. [#19757](https://github.com/open-webui/open-webui/pull/19757)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F9EE The \"ENABLE_ASYNC_EMBEDDING\" environment variable is now
      correctly applied to embedding operations when configured exclusively via environment
      variables. [#19748](https://github.com/open-webui/open-webui/pull/19748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4BE SQLCipher absolute path handling was fixed to properly support
      absolute database paths (e.g., \"/app/data.db\") instead of incorrectly stripping
      leading slashes and converting them to relative paths; this restores functionality
      for Docker volume mounts and explicit absolute path configurations while maintaining
      backward compatibility with relative paths. [#20074](https://github.com/open-webui/open-webui/pull/20074)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: '@rgaricano, @jekuaitk, @borisboc, @ascodeasice, @westbrook-ai, @Cyp9715,
      @joaoback, @aleixdorca, @taylorwilsdon, @Ithanil, @Zyfax, @okamototk, @ndrsfel,
      @kim-seokjin, @michi-onl, @ShirasawaSama, @broskees, @silentoplayz, @zengxy,
      @jolow99, @bitsofinfo, @Kylapaallikko, @Classic298'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @loitragg, @haka4githu6, @silenceroom, @crizCraig, @GenieDev101,
      @CubicleGangster, @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz,
      @JrdnHans, @hkosm, @VeroFess, @joaoback, @LuxTronic'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 28-other-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: uncategorized
  title: 28 other changes in v0.6.42
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: uncategorized
title: 28 other changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 28 other changes in v0.6.42

**Open WebUI** · 2025-12-21 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!CAUTION]

> > This release includes database schema changes; multi-worker, multi-server, or load-balanced deployments must update all instances simultaneously rather than performing rolling updates, as running mixed versions will cause application failures due to schema incompatibility between old and new instances.

> > [!WARNING]

> 🌍 The "SEARXNG_LANGUAGE" environment variable now allows configuring search language for SearXNG queries, replacing the hardcoded "en-US" default with a configurable setting that defaults to "all". [#19909](https://github.com/open-webui/open-webui/pull/19909)

> 🔧 The "RAG_EXTERNAL_RERANKER_TIMEOUT" environment variable now allows configuring request timeouts for external reranker operations. [#20049](https://github.com/open-webui/open-webui/pull/20049), [#19900](https://github.com/open-webui/open-webui/issues/19900)

> ⏱️ The "WEB_LOADER_TIMEOUT" environment variable now allows configuring request timeouts for SafeWebBaseLoader operations. [#19804](https://github.com/open-webui/open-webui/pull/19804), [#19734](https://github.com/open-webui/open-webui/issues/19734)

> 🌐 Translations for German, Danish, Finnish, Korean, Portuguese (Brazil), Simplified Chinese, Traditional Chinese, Catalan, and Spanish were enhanced and expanded.

> 💭 Text loss in the explanation feature when using the "CHAT_STREAM_RESPONSE_CHUNK_MAX_BUFFER_SIZE" environment variable was resolved by correcting newline handling in streaming responses. [#19829](https://github.com/open-webui/open-webui/pull/19829)

> 📚 Knowledge base batch file addition failures caused by Pydantic validation errors are now prevented by making the meta field optional in file metadata responses, allowing files without metadata to be processed correctly. [#20022](https://github.com/open-webui/open-webui/pull/20022), [#14220](https://github.com/open-webui/open-webui/issues/14220)

> 🎛️ Rate limiting errors (HTTP 429) with Brave Search free tier when generating multiple queries are now prevented through asyncio.Semaphore-based concurrency control applied globally to all search engines. [#20070](https://github.com/open-webui/open-webui/pull/20070), [#20003](https://github.com/open-webui/open-webui/issues/20003), [#14107](https://github.com/open-webui/open-webui/issues/14107), [#15134](https://github.com/open-webui/open-webui/issues/15134)

> 🚫 Channel API endpoint access is now correctly blocked when channels are globally disabled, preventing users with channel permissions from accessing channel data via API requests when the feature is turned off in admin settings. [#19957](https://github.com/open-webui/open-webui/pull/19957), [#19914](https://github.com/open-webui/open-webui/issues/19914)

> 🔧 Pipeline settings save failures when valve properties contain null values are now handled correctly. [#19791](https://github.com/open-webui/open-webui/pull/19791)

> 🛡️ Invalid PASSWORD_VALIDATION_REGEX_PATTERN configurations no longer cause startup warnings, with automatic fallback to the default pattern when regex compilation fails. [#20058](https://github.com/open-webui/open-webui/pull/20058)

> 📋 Log truncation issues in Docker deployments during application crashes were resolved by disabling Python stdio buffering, ensuring complete diagnostic output is captured. [#19844](https://github.com/open-webui/open-webui/issues/19844)

> 🔤 File attachment container layout issues when using RTL languages were resolved by applying chat direction settings to file containers across all message types. [#19891](https://github.com/open-webui/open-webui/pull/19891), [#19742](https://github.com/open-webui/open-webui/issues/19742)

> 🎛️ Chat functionality failures caused by empty logit_bias parameter values are now prevented by properly handling empty strings in the parameter parsing middleware. [#19982](https://github.com/open-webui/open-webui/issues/19982)

> 💾 Cloned prompts and tools now correctly preserve their access control settings instead of being reset to null, preventing unintended visibility changes when duplicating private or restricted items. [#19960](https://github.com/open-webui/open-webui/pull/19960), [#19360](https://github.com/open-webui/open-webui/issues/19360)

> 🎚️ Text scale adjustment buttons in Interface Settings were fixed to correctly increment and decrement the scale value. [#19699](https://github.com/open-webui/open-webui/pull/19699)

> 🎭 Group channel invite button text visibility in light theme was corrected to display properly against dark backgrounds. [#19828](https://github.com/open-webui/open-webui/issues/19828)

> 📁 The move button is now hidden when no folders exist, preventing display of non-functional controls. [#19705](https://github.com/open-webui/open-webui/pull/19705)

> 📦 Qdrant client dependency was updated to resolve startup version incompatibility warnings. [#19757](https://github.com/open-webui/open-webui/pull/19757)

> 🧮 The "ENABLE_ASYNC_EMBEDDING" environment variable is now correctly applied to embedding operations when configured exclusively via environment variables. [#19748](https://github.com/open-webui/open-webui/pull/19748)

> 💾 SQLCipher absolute path handling was fixed to properly support absolute database paths (e.g., "/app/data.db") instead of incorrectly stripping leading slashes and converting them to relative paths; this restores functionality for Docker volume mounts and explicit absolute path configurations while maintaining backward compatibility with relative paths. [#20074](https://github.com/open-webui/open-webui/pull/20074)

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @rgaricano, @jekuaitk, @borisboc, @ascodeasice, @westbrook-ai, @Cyp9715, @joaoback, @aleixdorca, @taylorwilsdon, @Ithanil, @Zyfax, @okamototk, @ndrsfel, @kim-seokjin, @michi-onl, @ShirasawaSama, @broskees, @silentoplayz, @zengxy, @jolow99, @bitsofinfo, @Kylapaallikko, @Classic298

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @loitragg, @haka4githu6, @silenceroom, @crizCraig, @GenieDev101, @CubicleGangster, @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess, @joaoback, @LuxTronic

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-caa362&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-28-other-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-caa362%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->