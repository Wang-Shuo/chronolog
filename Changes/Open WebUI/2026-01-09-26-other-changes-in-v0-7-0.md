---
card_id: open-webui-2026-01-09-e35d18
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Other changes: 26 changes in v0.7.0 — \U0001F4DD
  Users can now view read-only prompts in the workspace prompts list, with clear \"Read
  Only\"…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e055056d5ca9e5fe9bba63bb24ce3ee3d7d84389ef87df1d09eff95c94a7c83
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-e35d18
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 26 other changes'
  evidence:
  - quote: "\U0001F4DD Users can now view read-only prompts in the workspace prompts
      list, with clear \"Read Only\" badges indicating when editing is restricted.
      [#20368](https://github.com/open-webui/open-webui/pull/20368)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F527 Users can now view read-only tools in the workspace tools list,
      with clear \"Read Only\" badges indicating when editing is restricted. [#20243](https://github.com/open-webui/open-webui/issues/20243),
      [#20370](https://github.com/open-webui/open-webui/pull/20370)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: ⭐ Action Function developers can now update message favorite status using
      the new "chat:message:favorite" event, enabling the development of pin/unpin
      message actions without race conditions from frontend auto-save. [#20375](https://github.com/open-webui/open-webui/pull/20375)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4F0 Users can now dismiss the \"What's New\" changelog modal permanently
      using the X button, matching the behavior of the \"Okay, Let's Go!\" button.
      [#20258](https://github.com/open-webui/open-webui/pull/20258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4E7 Administrators can now configure the admin contact email displayed
      in the Account Pending overlay directly from the Admin Panel instead of only
      through environment variables. [#12500](https://github.com/open-webui/open-webui/issues/12500),
      [#20260](https://github.com/open-webui/open-webui/pull/20260)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F6E1️ Administrators can now restrict non-admin user access to Interface
      Settings through per-user or per-group permissions. [#20424](https://github.com/open-webui/open-webui/pull/20424)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F7E2 Administrators can now globally enable or disable user status
      visibility through the \"ENABLE_USER_STATUS\" setting in Admin Settings. [#20488](https://github.com/open-webui/open-webui/pull/20488)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F310 Translations for German, Portuguese (Brazil), Spanish, Simplified
      Chinese, Traditional Chinese, and Polish were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4AC Users can now export chats, use the Ask/Explain popup, and
      view chat lists correctly again after these features were broken by recent refactoring
      changes that caused 500 and 400 server errors. [#20146](https://github.com/open-webui/open-webui/issues/20146),
      [#20205](https://github.com/open-webui/open-webui/issues/20205), [#20206](https://github.com/open-webui/open-webui/issues/20206),
      [#20212](https://github.com/open-webui/open-webui/pull/20212)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4CE Users no longer encounter TypeError crashes when viewing messages
      with file attachments that have undefined URL properties. [#20343](https://github.com/open-webui/open-webui/pull/20343)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4C2 Users now see the correct Knowledge Base name when hovering
      over # file references in chat input instead of \"undefined\". [#20329](https://github.com/open-webui/open-webui/issues/20329),
      [#20333](https://github.com/open-webui/open-webui/pull/20333)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4C1 Users now see the Knowledge Selector dropdown correctly displayed
      above the Create Folder modal instead of being hidden behind it. [#20219](https://github.com/open-webui/open-webui/issues/20219),
      [#20213](https://github.com/open-webui/open-webui/pull/20213)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F305 Users now see profile images in non-PNG formats like SVG, JPEG,
      and GIF displayed correctly instead of appearing broken. [#20171](https://github.com/open-webui/open-webui/pull/20171)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4D7 Administrators with bypass access control enabled now correctly
      have write access to all knowledge bases. [#20371](https://github.com/open-webui/open-webui/pull/20371)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F3A8 Users with ComfyUI workflows now see only the intended final
      output images in chat instead of duplicate images from intermediate processing
      nodes like masks, crops, or segmentation previews. [#20158](https://github.com/open-webui/open-webui/issues/20158),
      [#20182](https://github.com/open-webui/open-webui/pull/20182)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F5C4️ Administrators with Redis Sentinel deployments no longer experience
      crashes during websocket disconnections due to improper async-generator handling
      in the YDocManager. [#20142](https://github.com/open-webui/open-webui/issues/20142),
      [#20145](https://github.com/open-webui/open-webui/pull/20145)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F510 Administrators using SCIM group management no longer encounter
      500 errors when working with groups that have no members. [#20187](https://github.com/open-webui/open-webui/pull/20187)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F578️ Administrators can now successfully save WebSearch settings
      without encountering validation errors for domain filter lists, YouTube language
      settings, or timeout values. [#20422](https://github.com/open-webui/open-webui/pull/20422)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4E6 Administrators installing with the uv package manager now experience
      successful installation after deprecated dependencies that were causing conflicts
      were removed. [#20177](https://github.com/open-webui/open-webui/issues/20177),
      [#20192](https://github.com/open-webui/open-webui/pull/20192)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: ⚠️ This release includes a major overhaul of database connection handling
      in the backend that requires all instances in multi-worker, multi-server, or
      load-balanced deployments to be updated simultaneously; running mixed versions
      will cause failures due to incompatible database connection management between
      old and new instances.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F517 Administrators will find the Admin Evaluations page at the
      new URL \"/admin/evaluations/feedback\" instead of \"/admin/evaluations/feedbacks\"
      to use the correct uncountable form of the word. [#20296](https://github.com/open-webui/open-webui/pull/20296)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: '@ShirasawaSama, @BLACKTHOMAS, @imsamurai, @jannikstdl, @silentoplayz,
      @joaoback, @rgaricano, @silentoplayz, @Classic298, @majiayu000, @Ithanil, @vincentsunx,
      @landerrosette, @BarerRocket2678, @rgaricano'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @loitragg, @haka4githu6, @silenceroom, @crizCraig, @GenieDev101,
      @CubicleGangster, @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz,
      @JrdnHans, @hkosm, @VeroFess, @joaoback, @walsermedia, @LuxTronic'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 26-other-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: uncategorized
  title: 26 other changes in v0.7.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: uncategorized
title: 26 other changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 26 other changes in v0.7.0

**Open WebUI** · 2026-01-09 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📝 Users can now view read-only prompts in the workspace prompts list, with clear "Read Only" badges indicating when editing is restricted. [#20368](https://github.com/open-webui/open-webui/pull/20368)

> 🔧 Users can now view read-only tools in the workspace tools list, with clear "Read Only" badges indicating when editing is restricted. [#20243](https://github.com/open-webui/open-webui/issues/20243), [#20370](https://github.com/open-webui/open-webui/pull/20370)

> ⭐ Action Function developers can now update message favorite status using the new "chat:message:favorite" event, enabling the development of pin/unpin message actions without race conditions from frontend auto-save. [#20375](https://github.com/open-webui/open-webui/pull/20375)

> 📰 Users can now dismiss the "What's New" changelog modal permanently using the X button, matching the behavior of the "Okay, Let's Go!" button. [#20258](https://github.com/open-webui/open-webui/pull/20258)

> 📧 Administrators can now configure the admin contact email displayed in the Account Pending overlay directly from the Admin Panel instead of only through environment variables. [#12500](https://github.com/open-webui/open-webui/issues/12500), [#20260](https://github.com/open-webui/open-webui/pull/20260)

> 🛡️ Administrators can now restrict non-admin user access to Interface Settings through per-user or per-group permissions. [#20424](https://github.com/open-webui/open-webui/pull/20424)

> 🟢 Administrators can now globally enable or disable user status visibility through the "ENABLE_USER_STATUS" setting in Admin Settings. [#20488](https://github.com/open-webui/open-webui/pull/20488)

> 🌐 Translations for German, Portuguese (Brazil), Spanish, Simplified Chinese, Traditional Chinese, and Polish were enhanced and expanded.

> 💬 Users can now export chats, use the Ask/Explain popup, and view chat lists correctly again after these features were broken by recent refactoring changes that caused 500 and 400 server errors. [#20146](https://github.com/open-webui/open-webui/issues/20146), [#20205](https://github.com/open-webui/open-webui/issues/20205), [#20206](https://github.com/open-webui/open-webui/issues/20206), [#20212](https://github.com/open-webui/open-webui/pull/20212)

> 📎 Users no longer encounter TypeError crashes when viewing messages with file attachments that have undefined URL properties. [#20343](https://github.com/open-webui/open-webui/pull/20343)

> 📂 Users now see the correct Knowledge Base name when hovering over # file references in chat input instead of "undefined". [#20329](https://github.com/open-webui/open-webui/issues/20329), [#20333](https://github.com/open-webui/open-webui/pull/20333)

> 📁 Users now see the Knowledge Selector dropdown correctly displayed above the Create Folder modal instead of being hidden behind it. [#20219](https://github.com/open-webui/open-webui/issues/20219), [#20213](https://github.com/open-webui/open-webui/pull/20213)

> 🌅 Users now see profile images in non-PNG formats like SVG, JPEG, and GIF displayed correctly instead of appearing broken. [#20171](https://github.com/open-webui/open-webui/pull/20171)

> 📗 Administrators with bypass access control enabled now correctly have write access to all knowledge bases. [#20371](https://github.com/open-webui/open-webui/pull/20371)

> 🎨 Users with ComfyUI workflows now see only the intended final output images in chat instead of duplicate images from intermediate processing nodes like masks, crops, or segmentation previews. [#20158](https://github.com/open-webui/open-webui/issues/20158), [#20182](https://github.com/open-webui/open-webui/pull/20182)

> 🗄️ Administrators with Redis Sentinel deployments no longer experience crashes during websocket disconnections due to improper async-generator handling in the YDocManager. [#20142](https://github.com/open-webui/open-webui/issues/20142), [#20145](https://github.com/open-webui/open-webui/pull/20145)

> 🔐 Administrators using SCIM group management no longer encounter 500 errors when working with groups that have no members. [#20187](https://github.com/open-webui/open-webui/pull/20187)

> 🕸️ Administrators can now successfully save WebSearch settings without encountering validation errors for domain filter lists, YouTube language settings, or timeout values. [#20422](https://github.com/open-webui/open-webui/pull/20422)

> 📦 Administrators installing with the uv package manager now experience successful installation after deprecated dependencies that were causing conflicts were removed. [#20177](https://github.com/open-webui/open-webui/issues/20177), [#20192](https://github.com/open-webui/open-webui/pull/20192)

> ⚠️ This release includes a major overhaul of database connection handling in the backend that requires all instances in multi-worker, multi-server, or load-balanced deployments to be updated simultaneously; running mixed versions will cause failures due to incompatible database connection management between old and new instances.

> 🔗 Administrators will find the Admin Evaluations page at the new URL "/admin/evaluations/feedback" instead of "/admin/evaluations/feedbacks" to use the correct uncountable form of the word. [#20296](https://github.com/open-webui/open-webui/pull/20296)

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @ShirasawaSama, @BLACKTHOMAS, @imsamurai, @jannikstdl, @silentoplayz, @joaoback, @rgaricano, @silentoplayz, @Classic298, @majiayu000, @Ithanil, @vincentsunx, @landerrosette, @BarerRocket2678, @rgaricano

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @loitragg, @haka4githu6, @silenceroom, @crizCraig, @GenieDev101, @CubicleGangster, @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess, @joaoback, @walsermedia, @LuxTronic

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-e35d18&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-26-other-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-e35d18%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->