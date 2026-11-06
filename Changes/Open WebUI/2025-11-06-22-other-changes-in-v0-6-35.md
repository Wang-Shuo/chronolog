---
card_id: open-webui-2025-11-06-074840
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Other changes: 22 changes in v0.6.35 — \U0001F50A
  ELEVENLABS_API_BASE_URL environment variable now allows configuration of custom
  ElevenLabs…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a3dc6f2ca325d56390cc0db7ffa17bb95aa2da526ae45f1d98a78f126bcad3d1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-074840
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 22 other changes'
  evidence:
  - quote: "\U0001F50A ELEVENLABS_API_BASE_URL environment variable now allows configuration
      of custom ElevenLabs API endpoints, enabling support for EU residency API requirements.
      [#18402](https://github.com/open-webui/open-webui/issues/18402)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F319 Dark mode styles for select elements were added using Tailwind
      CSS classes, improving consistency across the interface. [#18636](https://github.com/open-webui/open-webui/pull/18636)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F310 Translations for Portuguese (Brazil), Greek, German, Traditional
      Chinese, Simplified Chinese, Spanish, Georgian, Danish, and Estonian were enhanced
      and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4AC Chat titles are now properly generated even when title auto-generation
      is disabled in interface settings, fixing an issue where chats would remain
      labeled as \"New chat\". [#18761](https://github.com/open-webui/open-webui/pull/18761),
      [#18717](https://github.com/open-webui/open-webui/issues/18717), [#6478](https://github.com/open-webui/open-webui/issues/6478)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F50D Chat query errors are prevented by properly validating and
      handling the \"order_by\" parameter to ensure requested columns exist. [#18400](https://github.com/open-webui/open-webui/pull/18400),
      [#18452](https://github.com/open-webui/open-webui/pull/18452)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F511 Self-hosted Marker instances can now be used without requiring
      an API key, while keeping it optional for datalab Marker service users. [#18617](https://github.com/open-webui/open-webui/issues/18617)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4C4 Docling RAG parameter configuration is now correctly saved
      in the admin UI by fixing the typo in the \"DOCLING_PARAMS\" parameter name.
      [#18390](https://github.com/open-webui/open-webui/pull/18390)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F6E0️ Functions page now updates immediately after deleting a function,
      removing the need for a manual page reload. [#18912](https://github.com/open-webui/open-webui/pull/18912),
      [#18908](https://github.com/open-webui/open-webui/issues/18908)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4CB Clipboard images pasted via the \"{{CLIPBOARD}}\" prompt variable
      are now correctly converted to base64 format before being sent to the backend,
      resolving base64 encoding errors. [#18432](https://github.com/open-webui/open-webui/pull/18432),
      [#18425](https://github.com/open-webui/open-webui/issues/18425)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4C1 Folder and channel creation now validates that names are not
      empty, preventing creation of folders or channels with no name and showing an
      error toast if attempted. [#18564](https://github.com/open-webui/open-webui/pull/18564)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F58A️ Rich text input no longer removes text between equals signs
      when pasting code with comparison operators. [#18551](https://github.com/open-webui/open-webui/issues/18551)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: ⌨️ Keyboard shortcuts now display the correct keys for international and
      non-QWERTY keyboard layouts by detecting the user's layout using the Keyboard
      API. [#18533](https://github.com/open-webui/open-webui/pull/18533)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F39A️ Divider no longer displays in the integrations menu when no
      integrations are enabled. [#18487](https://github.com/open-webui/open-webui/pull/18487)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F3A8 Artifacts view now automatically displays when opening an existing
      conversation containing artifacts, improving user experience. [#18215](https://github.com/open-webui/open-webui/pull/18215)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F58C️ Formatting toolbar is no longer hidden under images or code
      blocks in chat and now displays correctly above all message content."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4AC Duplicate prompt suggestions no longer cause the webpage to
      freeze or throw JavaScript errors by implementing proper key management with
      composite keys. [#18841](https://github.com/open-webui/open-webui/pull/18841),
      [#18566](https://github.com/open-webui/open-webui/issues/18566)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F6E1️ Duplicate crossorigin attribute in the manifest file was removed.
      [#18413](https://github.com/open-webui/open-webui/pull/18413)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: '@joaoback, @kaiwinut, @taylorwilsdon, @Classic298, @duncansmart, @silentoplayz,
      @sinejespersen, @acomarcho, @Davixk, @Ithanil, @zhsh-12, @athoik, @acomarcho,
      @wangweixuan, @ShirasawaSama, @acwoo97, @IllimarR, @rgaricano, @OAburub, @iPagar,
      @mkhludnev, @jmleksan, @attilaolah, @htulipe, @ricdikulous, @andrewbbaek, @Tsafaras,
      @Classic298, @ivanostanin, @wei840222'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @agency-agency, @Classic298, @loitragg, @haka4githu6, @GenieDev101,
      @CubicleGangster, @TOWaB, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans,
      @hkosm, @VeroFess, @joaoback'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 22-other-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: uncategorized
  title: 22 other changes in v0.6.35
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: uncategorized
title: 22 other changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 22 other changes in v0.6.35

**Open WebUI** · 2025-11-06 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔊 ELEVENLABS_API_BASE_URL environment variable now allows configuration of custom ElevenLabs API endpoints, enabling support for EU residency API requirements. [#18402](https://github.com/open-webui/open-webui/issues/18402)

> 🌙 Dark mode styles for select elements were added using Tailwind CSS classes, improving consistency across the interface. [#18636](https://github.com/open-webui/open-webui/pull/18636)

> 🌐 Translations for Portuguese (Brazil), Greek, German, Traditional Chinese, Simplified Chinese, Spanish, Georgian, Danish, and Estonian were enhanced and expanded.

> 💬 Chat titles are now properly generated even when title auto-generation is disabled in interface settings, fixing an issue where chats would remain labeled as "New chat". [#18761](https://github.com/open-webui/open-webui/pull/18761), [#18717](https://github.com/open-webui/open-webui/issues/18717), [#6478](https://github.com/open-webui/open-webui/issues/6478)

> 🔍 Chat query errors are prevented by properly validating and handling the "order_by" parameter to ensure requested columns exist. [#18400](https://github.com/open-webui/open-webui/pull/18400), [#18452](https://github.com/open-webui/open-webui/pull/18452)

> 🔑 Self-hosted Marker instances can now be used without requiring an API key, while keeping it optional for datalab Marker service users. [#18617](https://github.com/open-webui/open-webui/issues/18617)

> 📄 Docling RAG parameter configuration is now correctly saved in the admin UI by fixing the typo in the "DOCLING_PARAMS" parameter name. [#18390](https://github.com/open-webui/open-webui/pull/18390)

> 🛠️ Functions page now updates immediately after deleting a function, removing the need for a manual page reload. [#18912](https://github.com/open-webui/open-webui/pull/18912), [#18908](https://github.com/open-webui/open-webui/issues/18908)

> 📋 Clipboard images pasted via the "{{CLIPBOARD}}" prompt variable are now correctly converted to base64 format before being sent to the backend, resolving base64 encoding errors. [#18432](https://github.com/open-webui/open-webui/pull/18432), [#18425](https://github.com/open-webui/open-webui/issues/18425)

> 📁 Folder and channel creation now validates that names are not empty, preventing creation of folders or channels with no name and showing an error toast if attempted. [#18564](https://github.com/open-webui/open-webui/pull/18564)

> 🖊️ Rich text input no longer removes text between equals signs when pasting code with comparison operators. [#18551](https://github.com/open-webui/open-webui/issues/18551)

> ⌨️ Keyboard shortcuts now display the correct keys for international and non-QWERTY keyboard layouts by detecting the user's layout using the Keyboard API. [#18533](https://github.com/open-webui/open-webui/pull/18533)

> 🎚️ Divider no longer displays in the integrations menu when no integrations are enabled. [#18487](https://github.com/open-webui/open-webui/pull/18487)

> 🎨 Artifacts view now automatically displays when opening an existing conversation containing artifacts, improving user experience. [#18215](https://github.com/open-webui/open-webui/pull/18215)

> 🖌️ Formatting toolbar is no longer hidden under images or code blocks in chat and now displays correctly above all message content.

> 💬 Duplicate prompt suggestions no longer cause the webpage to freeze or throw JavaScript errors by implementing proper key management with composite keys. [#18841](https://github.com/open-webui/open-webui/pull/18841), [#18566](https://github.com/open-webui/open-webui/issues/18566)

> 🛡️ Duplicate crossorigin attribute in the manifest file was removed. [#18413](https://github.com/open-webui/open-webui/pull/18413)

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @joaoback, @kaiwinut, @taylorwilsdon, @Classic298, @duncansmart, @silentoplayz, @sinejespersen, @acomarcho, @Davixk, @Ithanil, @zhsh-12, @athoik, @acomarcho, @wangweixuan, @ShirasawaSama, @acwoo97, @IllimarR, @rgaricano, @OAburub, @iPagar, @mkhludnev, @jmleksan, @attilaolah, @htulipe, @ricdikulous, @andrewbbaek, @Tsafaras, @Classic298, @ivanostanin, @wei840222

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @agency-agency, @Classic298, @loitragg, @haka4githu6, @GenieDev101, @CubicleGangster, @TOWaB, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess, @joaoback

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
- [[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search and Browsing changes in v0.6.35]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-06-3-reliability-and-performance-changes-in-v0-6-35|3 Reliability and Performance changes in v0.6.35]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-06-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window changes in v0.6.35]] · Context Window
- [[Changes/Open WebUI/2025-11-06-edit-button-is-now-available-in-the-three-dot-menu-of-models-in-the-workspace-se|✏️ Edit button is now available in the three-dot menu of models in the workspace…]] · Model Support
- [[Changes/Open WebUI/2025-11-06-screen-reader-support-was-enhanced-by-wrapping-messages-in-semantic-elements-wit|♿ Screen reader support was enhanced by wrapping messages in semantic elements…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-06-external-document-loaders-can-now-optionally-forward-user-information-headers-wh|📄 External document loaders can now optionally forward user information headers…]] · Pricing Model
- [[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and Data changes in v0.6.35]] · Files and Data
- [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-06-5-account-and-access-changes-in-v0-6-35|5 Account and Access changes in v0.6.35]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-074840&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-22-other-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-074840%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->