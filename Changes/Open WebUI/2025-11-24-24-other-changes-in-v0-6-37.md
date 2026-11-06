---
card_id: open-webui-2025-11-24-18b471
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Other changes: 24 changes in v0.6.37 — \U0001F510
  SSRF protection was implemented with a configurable URL blocklist that prevents
  access to…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf8a31f85270c1394cfcf0afdc2657e673210fb1487ddf2d1b22879f6fe66949
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-18b471
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 24 other changes'
  evidence:
  - quote: "\U0001F510 SSRF protection was implemented with a configurable URL blocklist
      that prevents access to cloud metadata endpoints and private networks, with
      default protections for AWS, Google Cloud, Azure, and Alibaba Cloud metadata
      services, customizable via \"WEB_FETCH_FILTER_LIST\" environment variable. [#19201](https://github.com/open-webui/open-webui/pull/19201)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CA Audit log file path is now configurable via \"AUDIT_LOGS_FILE_PATH\"
      environment variable, enabling storage in separate volumes or custom locations.
      [#19173](https://github.com/open-webui/open-webui/pull/19173)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CB Tables in chat messages now include a copy button that appears
      on hover, enabling quick copying of table content alongside the existing CSV
      export functionality. [#19162](https://github.com/open-webui/open-webui/issues/19162)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F310 Translations for Simplified Chinese, Traditional Chinese, Portuguese
      (Brazil), Catalan, Spanish (Spain), Finnish, Irish, Farsi, Swedish, Danish,
      German, Korean, and Thai were improved and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F5BC️ Multiple input images for image editing and generation are
      now correctly passed as an array using the \"image[]\" parameter syntax, enabling
      proper multi-image reference functionality with models like GPT Image 1. [#19339](https://github.com/open-webui/open-webui/issues/19339)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F50D Chat search now works correctly with PostgreSQL when chat data
      contains null bytes, with comprehensive sanitization preventing null bytes during
      data writes, cleaning existing data on read, and stripping null bytes during
      search queries to ensure reliable search functionality. [#15616](https://github.com/open-webui/open-webui/issues/15616)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F50D Hybrid search with reranking now correctly handles attribute
      validation, preventing errors when collection results lack expected structure.
      [#19025](https://github.com/open-webui/open-webui/pull/19025), [#17046](https://github.com/open-webui/open-webui/issues/17046)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F50E Reranking functionality now works correctly after recent refactoring,
      resolving crashes caused by incorrect function argument handling. [#19270](https://github.com/open-webui/open-webui/pull/19270)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C5 Date formatting in chat search and admin user chat search now
      correctly respects the \"DEFAULT_LOCALE\" environment variable, displaying dates
      according to the configured locale instead of always using MM/DD/YYYY format.
      [#19305](https://github.com/open-webui/open-webui/pull/19305), [#19020](https://github.com/open-webui/open-webui/issues/19020)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C4 RAG template prompt duplication was eliminated by removing
      redundant user query section from the default template. [#19099](https://github.com/open-webui/open-webui/pull/19099),
      [#19098](https://github.com/open-webui/open-webui/issues/19098)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CB MinerU local mode configuration no longer incorrectly requires
      an API key, allowing proper use of local content extraction without external
      API credentials. [#19258](https://github.com/open-webui/open-webui/issues/19258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CA Excel file uploads now work correctly with the addition of
      the missing msoffcrypto-tool dependency, resolving import errors introduced
      by the unstructured package upgrade. [#19153](https://github.com/open-webui/open-webui/issues/19153)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4D1 Docling parameters now properly handle JSON serialization,
      preventing exceptions and ensuring configuration changes are saved correctly.
      [#19072](https://github.com/open-webui/open-webui/pull/19072)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F6E0️ UserValves configuration now correctly isolates settings per
      tool, preventing configuration contamination when multiple tools with UserValves
      are used simultaneously. [#19185](https://github.com/open-webui/open-webui/pull/19185),
      [#15569](https://github.com/open-webui/open-webui/issues/15569)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C1 Archived chats now have their folder associations automatically
      removed to prevent unintended deletion when their previous folder is deleted.
      [#14578](https://github.com/open-webui/open-webui/issues/14578)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F510 ElevenLabs API key is now properly obfuscated in the admin
      settings page, preventing plain text exposure of sensitive credentials. [#19262](https://github.com/open-webui/open-webui/pull/19262),
      [#19260](https://github.com/open-webui/open-webui/issues/19260)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F512 API key endpoint restrictions now properly enforce access controls
      for all endpoints including SCIM, preventing unintended access when \"API_KEY_ALLOWED_ENDPOINTS\"
      is configured. [#19168](https://github.com/open-webui/open-webui/issues/19168)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CB Text copied from chat responses in Chrome now pastes without
      background formatting, improving readability when pasting into word processors.
      [#19083](https://github.com/open-webui/open-webui/issues/19083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4C4 MinerU parameter handling was refactored to pass parameters
      directly to the API, improving flexibility and fixing VLM backend configuration.
      [#19105](https://github.com/open-webui/open-webui/pull/19105), [#18446](https://github.com/open-webui/open-webui/discussions/18446)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: '@Davixk, @podden, @ShirasawaSama, @jekuaitk, @sanglt, @shargyle, @aindriu80,
      @krishna-medapati, @lazariv, @FlorentMair80, @mikkeschiren, @joaoback, @Cyp9715,
      @aleixdorca, @silentoplayz, @gerhardj-b, @siwadon-jay, @jmleksan, @dannyl1u,
      @rgaricano, @Kylapaallikko, @Classic298, @expruc, @tomhaynes, @diwakar-s-maurya,
      @xqqp, @logan-hcg, @BlakeTnr, @siavashvj, @Oleg52, @sihyeonn, @davecrab, @matiboux,
      @adam-skalicky'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @agency-agency, @Classic298, @loitragg, @haka4githu6, @silenceroom,
      @GenieDev101, @CubicleGangster, @TOWaB, @comet-ml, @FominVO, @catalyst-net-nz,
      @JrdnHans, @hkosm, @VeroFess, @joaoback, @walsermedia, @LuxTronic'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 24-other-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in v0.6.37
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in v0.6.37

**Open WebUI** · 2025-11-24 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 SSRF protection was implemented with a configurable URL blocklist that prevents access to cloud metadata endpoints and private networks, with default protections for AWS, Google Cloud, Azure, and Alibaba Cloud metadata services, customizable via "WEB_FETCH_FILTER_LIST" environment variable. [#19201](https://github.com/open-webui/open-webui/pull/19201)

> 📊 Audit log file path is now configurable via "AUDIT_LOGS_FILE_PATH" environment variable, enabling storage in separate volumes or custom locations. [#19173](https://github.com/open-webui/open-webui/pull/19173)

> 📋 Tables in chat messages now include a copy button that appears on hover, enabling quick copying of table content alongside the existing CSV export functionality. [#19162](https://github.com/open-webui/open-webui/issues/19162)

> 🌐 Translations for Simplified Chinese, Traditional Chinese, Portuguese (Brazil), Catalan, Spanish (Spain), Finnish, Irish, Farsi, Swedish, Danish, German, Korean, and Thai were improved and expanded.

> 🖼️ Multiple input images for image editing and generation are now correctly passed as an array using the "image[]" parameter syntax, enabling proper multi-image reference functionality with models like GPT Image 1. [#19339](https://github.com/open-webui/open-webui/issues/19339)

> 🔍 Chat search now works correctly with PostgreSQL when chat data contains null bytes, with comprehensive sanitization preventing null bytes during data writes, cleaning existing data on read, and stripping null bytes during search queries to ensure reliable search functionality. [#15616](https://github.com/open-webui/open-webui/issues/15616)

> 🔍 Hybrid search with reranking now correctly handles attribute validation, preventing errors when collection results lack expected structure. [#19025](https://github.com/open-webui/open-webui/pull/19025), [#17046](https://github.com/open-webui/open-webui/issues/17046)

> 🔎 Reranking functionality now works correctly after recent refactoring, resolving crashes caused by incorrect function argument handling. [#19270](https://github.com/open-webui/open-webui/pull/19270)

> 📅 Date formatting in chat search and admin user chat search now correctly respects the "DEFAULT_LOCALE" environment variable, displaying dates according to the configured locale instead of always using MM/DD/YYYY format. [#19305](https://github.com/open-webui/open-webui/pull/19305), [#19020](https://github.com/open-webui/open-webui/issues/19020)

> 📄 RAG template prompt duplication was eliminated by removing redundant user query section from the default template. [#19099](https://github.com/open-webui/open-webui/pull/19099), [#19098](https://github.com/open-webui/open-webui/issues/19098)

> 📋 MinerU local mode configuration no longer incorrectly requires an API key, allowing proper use of local content extraction without external API credentials. [#19258](https://github.com/open-webui/open-webui/issues/19258)

> 📊 Excel file uploads now work correctly with the addition of the missing msoffcrypto-tool dependency, resolving import errors introduced by the unstructured package upgrade. [#19153](https://github.com/open-webui/open-webui/issues/19153)

> 📑 Docling parameters now properly handle JSON serialization, preventing exceptions and ensuring configuration changes are saved correctly. [#19072](https://github.com/open-webui/open-webui/pull/19072)

> 🛠️ UserValves configuration now correctly isolates settings per tool, preventing configuration contamination when multiple tools with UserValves are used simultaneously. [#19185](https://github.com/open-webui/open-webui/pull/19185), [#15569](https://github.com/open-webui/open-webui/issues/15569)

> 📁 Archived chats now have their folder associations automatically removed to prevent unintended deletion when their previous folder is deleted. [#14578](https://github.com/open-webui/open-webui/issues/14578)

> 🔐 ElevenLabs API key is now properly obfuscated in the admin settings page, preventing plain text exposure of sensitive credentials. [#19262](https://github.com/open-webui/open-webui/pull/19262), [#19260](https://github.com/open-webui/open-webui/issues/19260)

> 🔒 API key endpoint restrictions now properly enforce access controls for all endpoints including SCIM, preventing unintended access when "API_KEY_ALLOWED_ENDPOINTS" is configured. [#19168](https://github.com/open-webui/open-webui/issues/19168)

> 📋 Text copied from chat responses in Chrome now pastes without background formatting, improving readability when pasting into word processors. [#19083](https://github.com/open-webui/open-webui/issues/19083)

> 📄 MinerU parameter handling was refactored to pass parameters directly to the API, improving flexibility and fixing VLM backend configuration. [#19105](https://github.com/open-webui/open-webui/pull/19105), [#18446](https://github.com/open-webui/open-webui/discussions/18446)

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @Davixk, @podden, @ShirasawaSama, @jekuaitk, @sanglt, @shargyle, @aindriu80, @krishna-medapati, @lazariv, @FlorentMair80, @mikkeschiren, @joaoback, @Cyp9715, @aleixdorca, @silentoplayz, @gerhardj-b, @siwadon-jay, @jmleksan, @dannyl1u, @rgaricano, @Kylapaallikko, @Classic298, @expruc, @tomhaynes, @diwakar-s-maurya, @xqqp, @logan-hcg, @BlakeTnr, @siavashvj, @Oleg52, @sihyeonn, @davecrab, @matiboux, @adam-skalicky

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @agency-agency, @Classic298, @loitragg, @haka4githu6, @silenceroom, @GenieDev101, @CubicleGangster, @TOWaB, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess, @joaoback, @walsermedia, @LuxTronic

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-5-interface-experience-changes-in-v0-6-37|5 Interface Experience changes in v0.6.37]] · Interface Experience
- [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-prompt-autocompletion-is-now-available-independently-of-the-rich-text-input-sett|✍️ Prompt autocompletion is now available independently of the rich text input…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-rag-template-query-placeholder-escaping-logic-was-corrected-to-prevent-unintende|📝 RAG template query placeholder escaping logic was corrected to prevent unintended…]] · Context Window
- [[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|👥 Default group assignment is now available for new users, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-2-voice-and-audio-changes-in-v0-6-37|2 Voice and Audio changes in v0.6.37]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-24-7-account-and-access-changes-in-v0-6-37|7 Account and Access changes in v0.6.37]] · Account and Access
- [[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-24-ui-scale-adjustment-is-now-available-in-interface-settings-allowing-users-to-inc|🎨 UI scale adjustment is now available in interface settings, allowing users…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and Data changes in v0.6.37]] · Files and Data
- [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-4-image-generation-changes-in-v0-6-37|4 Image Generation changes in v0.6.37]] · Image Generation
- [[Changes/Open WebUI/2025-11-24-websocket-and-redis-configuration-options-are-now-available-including-debug-logg|🔧 WebSocket and Redis configuration options are now available including debug…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-24-pwa-installations-on-ios-now-properly-refresh-after-server-container-restarts-re|📱 PWA installations on iOS now properly refresh after server container restarts…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-24-11-model-support-changes-in-v0-6-37|11 Model Support changes in v0.6.37]] · Model Support
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-18b471&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-24-other-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-18b471%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->