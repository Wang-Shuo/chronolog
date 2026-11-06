---
card_id: open-webui-2026-02-12-d50a21
date: '2026-02-12'
description: 'Open WebUI · 2026-02-12 · Other changes: 29 changes in v0.8.0 — > [!CAUTION]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5efd8cc16c544bbb3f6afaaff51219edaff624bc0bf0050b18ffe62a8a155c0a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-d50a21
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 29 other changes'
  evidence:
  - quote: '> [!CAUTION]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '> ⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '> [!WARNING]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '> ⚠️ **Long-Running Database Migration**: This release includes a migration
      for the `chat_message` table that can take a significant amount of time to complete,
      especially in larger deployments with extensive chat histories. Please plan
      for adequate downtime and allow the migration to finish completely without interruption.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F465 **Redesigned access control UI.** The access control UI was
      redesigned with a more intuitive interface that makes it easier to add multiple
      groups at once. [#21277](https://github.com/open-webui/open-webui/pull/21277)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F3F7️ **Prompt tags.** Prompts can now be organized with tags, and
      users can filter the prompt workspace by tag to quickly find related prompts
      across large collections. [#20945](https://github.com/open-webui/open-webui/pull/20945)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4A1 **Null chat title fallback.** Notifications without chat titles
      now display \"New Chat\" instead of showing null. [#21292](https://github.com/open-webui/open-webui/pull/21292)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4E7 **USER_EMAIL template variable.** Users can now reference their
      email address in prompts and system messages using the \"{{USER_EMAIL}}\" template
      variable. [#20881](https://github.com/open-webui/open-webui/pull/20881)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F510 **Custom password hints.** Administrators can now provide custom
      password requirement hints to users via the \"PASSWORD_VALIDATION_HINT\" environment
      variable, making it clearer what password criteria must be met during signup
      or password changes. [#20647](https://github.com/open-webui/open-webui/issues/20647),
      [#20650](https://github.com/open-webui/open-webui/pull/20650)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5C4️ **Weaviate custom endpoints.** Administrators can now connect
      to self-hosted Weaviate deployments with separate HTTP and gRPC endpoints via
      new environment variables. [#20620](https://github.com/open-webui/open-webui/pull/20620)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5C3️ **Redis Sentinel reconnection delay.** Administrators using
      Redis Sentinel can now configure a reconnection delay via \"REDIS_RECONNECT_DELAY\"
      to prevent retry exhaustion during failover elections. [#21021](https://github.com/open-webui/open-webui/pull/21021)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F310 **Translation updates.** Translations for Catalan, Finnish,
      Irish, French, German, Japanese, Latvian, Polish, Portuguese (Brazil), Simplified
      Chinese, Slovak, Spanish, and Traditional Chinese were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6AA **Channel notification access control.** Users without channel
      permissions can no longer access channels through notifications, properly enforcing
      access controls across all channel entry points. [#20883](https://github.com/open-webui/open-webui/pull/20883),
      [#20789](https://github.com/open-webui/open-webui/discussions/20789)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ♻️ **Streaming connection cleanup.** Streaming responses now properly clean
      up network connections when interrupted, preventing "Unclosed client session"
      errors from accumulating over time. [#20889](https://github.com/open-webui/open-webui/pull/20889),
      [#17058](https://github.com/open-webui/open-webui/issues/17058)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DA **Knowledge base reindex fix.** Reindexing knowledge base files
      now works correctly instead of failing with duplicate content errors. [#20854](https://github.com/open-webui/open-webui/issues/20854),
      [#20857](https://github.com/open-webui/open-webui/pull/20857)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BB **MATLAB syntax highlighting.** MATLAB code blocks now display
      with proper syntax highlighting in chat messages. [#20719](https://github.com/open-webui/open-webui/issues/20719),
      [#20773](https://github.com/open-webui/open-webui/pull/20773)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4CA **CSV export HTML entity decoding.** Exporting tables to CSV
      now properly decodes HTML entities, ensuring special characters display correctly
      in the exported file. [#20688](https://github.com/open-webui/open-webui/pull/20688)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F433 **Docker Ollama update fix.** Ollama can now be updated within
      Docker containers after adding a missing zstd dependency. [#20994](https://github.com/open-webui/open-webui/issues/20994),
      [#21052](https://github.com/open-webui/open-webui/pull/21052)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4E1 **OpenTelemetry Redis cluster fix.** OpenTelemetry instrumentation
      now works correctly with Redis cluster mode deployments. [#21129](https://github.com/open-webui/open-webui/pull/21129)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4E6 **Tool call expand/collapse fix.** Tool call results in chat
      can now be expanded and collapsed again after a recent refactor disabled this
      behavior. [#21205](https://github.com/open-webui/open-webui/pull/21205)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001FA9B **Disabled API endpoint bypass fix.** Fixed Ollama/OpenAI API
      endpoints bypassing 'ENABLE_OLLAMA_API' and 'ENABLE_OPENAI_API' flags when the
      'url_idx' parameter was provided. Endpoints now properly return a 503 error
      with a clear \"API is disabled\" message instead of attempting to connect and
      logging confusing connection errors."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4CE **Citation parsing error fix.** Citation parsing no longer
      crashes when builtin tools return error responses, fixing AttributeError issues
      when tools like search_web fail. [#21071](https://github.com/open-webui/open-webui/pull/21071)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ‼️ **Database Migration Required** — This release includes database schema
      changes; multi-worker, multi-server, or load-balanced deployments must update
      all instances simultaneously rather than performing rolling updates, as running
      mixed versions will cause application failures due to schema incompatibility
      between old and new instances.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ⚠️ **Chat Message Table Migration** — This release includes a new chat
      message table migration that can take a significant amount of time to complete
      in larger deployments with extensive chat histories. Administrators should plan
      for adequate maintenance windows and allow the migration to complete fully without
      interruption. Running the migration with insufficient time or resources may
      result in data integrity issues.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '@aindriu80, @Edgaras0x4E, @tomasloksa, @ctolon, @ShirasawaSama, @sjhddh,
      @PeterDaveHello, @schneider-f, @joaoback, @silentoplayz, @tremlin, @aleixdorca,
      @veeceey, @Algorithm5838, @jannikstdl, @Th3Un1q3, @EntropyYue, @Classic298,
      @pelmennoteam, @mickeytheseal, @hsienz'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @Classic298, @loitragg, @haka4githu6, @silenceroom, @walsermedia,
      @crizCraig, @GenieDev101, @CubicleGangster, @TOWaB, @comet-ml, @catalyst-net-nz,
      @JrdnHans, @hkosm, @joaoback, @LuxTronic'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 29-other-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: uncategorized
  title: 29 other changes in v0.8.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: uncategorized
title: 29 other changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 29 other changes in v0.8.0

**Open WebUI** · 2026-02-12 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!CAUTION]

> > ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> > [!WARNING]

> > ⚠️ **Long-Running Database Migration**: This release includes a migration for the `chat_message` table that can take a significant amount of time to complete, especially in larger deployments with extensive chat histories. Please plan for adequate downtime and allow the migration to finish completely without interruption.

> 👥 **Redesigned access control UI.** The access control UI was redesigned with a more intuitive interface that makes it easier to add multiple groups at once. [#21277](https://github.com/open-webui/open-webui/pull/21277)

> 🏷️ **Prompt tags.** Prompts can now be organized with tags, and users can filter the prompt workspace by tag to quickly find related prompts across large collections. [#20945](https://github.com/open-webui/open-webui/pull/20945)

> 💡 **Null chat title fallback.** Notifications without chat titles now display "New Chat" instead of showing null. [#21292](https://github.com/open-webui/open-webui/pull/21292)

> 📧 **USER_EMAIL template variable.** Users can now reference their email address in prompts and system messages using the "{{USER_EMAIL}}" template variable. [#20881](https://github.com/open-webui/open-webui/pull/20881)

> 🔐 **Custom password hints.** Administrators can now provide custom password requirement hints to users via the "PASSWORD_VALIDATION_HINT" environment variable, making it clearer what password criteria must be met during signup or password changes. [#20647](https://github.com/open-webui/open-webui/issues/20647), [#20650](https://github.com/open-webui/open-webui/pull/20650)

> 🗄️ **Weaviate custom endpoints.** Administrators can now connect to self-hosted Weaviate deployments with separate HTTP and gRPC endpoints via new environment variables. [#20620](https://github.com/open-webui/open-webui/pull/20620)

> 🗃️ **Redis Sentinel reconnection delay.** Administrators using Redis Sentinel can now configure a reconnection delay via "REDIS_RECONNECT_DELAY" to prevent retry exhaustion during failover elections. [#21021](https://github.com/open-webui/open-webui/pull/21021)

> 🌐 **Translation updates.** Translations for Catalan, Finnish, Irish, French, German, Japanese, Latvian, Polish, Portuguese (Brazil), Simplified Chinese, Slovak, Spanish, and Traditional Chinese were enhanced and expanded.

> 🚪 **Channel notification access control.** Users without channel permissions can no longer access channels through notifications, properly enforcing access controls across all channel entry points. [#20883](https://github.com/open-webui/open-webui/pull/20883), [#20789](https://github.com/open-webui/open-webui/discussions/20789)

> ♻️ **Streaming connection cleanup.** Streaming responses now properly clean up network connections when interrupted, preventing "Unclosed client session" errors from accumulating over time. [#20889](https://github.com/open-webui/open-webui/pull/20889), [#17058](https://github.com/open-webui/open-webui/issues/17058)

> 📚 **Knowledge base reindex fix.** Reindexing knowledge base files now works correctly instead of failing with duplicate content errors. [#20854](https://github.com/open-webui/open-webui/issues/20854), [#20857](https://github.com/open-webui/open-webui/pull/20857)

> 💻 **MATLAB syntax highlighting.** MATLAB code blocks now display with proper syntax highlighting in chat messages. [#20719](https://github.com/open-webui/open-webui/issues/20719), [#20773](https://github.com/open-webui/open-webui/pull/20773)

> 📊 **CSV export HTML entity decoding.** Exporting tables to CSV now properly decodes HTML entities, ensuring special characters display correctly in the exported file. [#20688](https://github.com/open-webui/open-webui/pull/20688)

> 🐳 **Docker Ollama update fix.** Ollama can now be updated within Docker containers after adding a missing zstd dependency. [#20994](https://github.com/open-webui/open-webui/issues/20994), [#21052](https://github.com/open-webui/open-webui/pull/21052)

> 📡 **OpenTelemetry Redis cluster fix.** OpenTelemetry instrumentation now works correctly with Redis cluster mode deployments. [#21129](https://github.com/open-webui/open-webui/pull/21129)

> 📦 **Tool call expand/collapse fix.** Tool call results in chat can now be expanded and collapsed again after a recent refactor disabled this behavior. [#21205](https://github.com/open-webui/open-webui/pull/21205)

> 🪛 **Disabled API endpoint bypass fix.** Fixed Ollama/OpenAI API endpoints bypassing 'ENABLE_OLLAMA_API' and 'ENABLE_OPENAI_API' flags when the 'url_idx' parameter was provided. Endpoints now properly return a 503 error with a clear "API is disabled" message instead of attempting to connect and logging confusing connection errors.

> 📎 **Citation parsing error fix.** Citation parsing no longer crashes when builtin tools return error responses, fixing AttributeError issues when tools like search_web fail. [#21071](https://github.com/open-webui/open-webui/pull/21071)

> ‼️ **Database Migration Required** — This release includes database schema changes; multi-worker, multi-server, or load-balanced deployments must update all instances simultaneously rather than performing rolling updates, as running mixed versions will cause application failures due to schema incompatibility between old and new instances.

> ⚠️ **Chat Message Table Migration** — This release includes a new chat message table migration that can take a significant amount of time to complete in larger deployments with extensive chat histories. Administrators should plan for adequate maintenance windows and allow the migration to complete fully without interruption. Running the migration with insufficient time or resources may result in data integrity issues.

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @aindriu80, @Edgaras0x4E, @tomasloksa, @ctolon, @ShirasawaSama, @sjhddh, @PeterDaveHello, @schneider-f, @joaoback, @silentoplayz, @tremlin, @aleixdorca, @veeceey, @Algorithm5838, @jannikstdl, @Th3Un1q3, @EntropyYue, @Classic298, @pelmennoteam, @mickeytheseal, @hsienz

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @Classic298, @loitragg, @haka4githu6, @silenceroom, @walsermedia, @crizCraig, @GenieDev101, @CubicleGangster, @TOWaB, @comet-ml, @catalyst-net-nz, @JrdnHans, @hkosm, @joaoback, @LuxTronic

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
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-d50a21&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-29-other-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-d50a21%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->