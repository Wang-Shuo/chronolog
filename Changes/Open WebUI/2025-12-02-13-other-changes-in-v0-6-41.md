---
card_id: open-webui-2025-12-02-d834a6
date: '2025-12-02'
description: 'Open WebUI · 2025-12-02 · Other changes: 13 changes in v0.6.41 — > [!CAUTION]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 61b373c8c52417e245377b5687db8638a1271de4dea85dc23dac369e34086f6d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-d834a6
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 13 other changes'
  evidence:
  - quote: '> [!CAUTION]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: '> ⚠️ **IMPORTANT for Multi-Instance Deployments**: This release includes
      database schema changes; multi-worker, multi-server, or load-balanced deployments
      must update all instances simultaneously rather than performing rolling updates,
      as running mixed versions will cause application failures due to schema incompatibility
      between old and new instances.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4C2 Administrators can now globally disable the folders feature
      and control user-level folder permissions through the admin panel, enabling
      minimalist interface configurations for deployments that don't require workspace
      organization features. [#19529](https://github.com/open-webui/open-webui/pull/19529),
      [#19210](https://github.com/open-webui/open-webui/discussions/19210), [#18459](https://github.com/open-webui/open-webui/discussions/18459),
      [#18299](https://github.com/open-webui/open-webui/discussions/18299)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F30D Translations for German, French, Portuguese (Brazil), Catalan,
      Simplified Chinese, and Traditional Chinese were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F512 Redis TLS connection failures were resolved by updating the
      python-socketio dependency to version 5.15.0, restoring support for the \"rediss://\"
      URL schema. [#19480](https://github.com/open-webui/open-webui/issues/19480),
      [#19488](https://github.com/open-webui/open-webui/pull/19488)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F319 Dark mode select dropdown styling was corrected to use proper
      background colors, fixing an issue where dropdown borders and hover states appeared
      white instead of matching the dark theme. [#19693](https://github.com/open-webui/open-webui/pull/19693),
      [#19442](https://github.com/open-webui/open-webui/issues/19442)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F50D Milvus vector database query filtering was fixed by correcting
      string quote handling in filter expressions and using the proper parameter name
      for queries, resolving false \"duplicate content detected\" errors that prevented
      uploading multiple files to knowledge bases. [#19602](https://github.com/open-webui/open-webui/pull/19602),
      [#18119](https://github.com/open-webui/open-webui/issues/18119), [#16345](https://github.com/open-webui/open-webui/issues/16345),
      [#17088](https://github.com/open-webui/open-webui/issues/17088), [#18485](https://github.com/open-webui/open-webui/issues/18485)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F199 Milvus multitenancy vector database was updated to use query_iterator()
      for improved robustness and consistency with the standard Milvus implementation,
      fixing the same false duplicate detection errors and improving handling of large
      result sets in multi-tenant deployments. [#19695](https://github.com/open-webui/open-webui/pull/19695)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: '@Classic298, @ShirasawaSama, @tobiasge, @RomualdYT, @joaoback, @kjpoccia,
      @gerhardj-b, @aleixdorca, @acwoo97, @matthew-kusz, @stevessr, @HennieLP'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: '@amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax,
      @icanbwell, @loitragg, @haka4githu6, @silenceroom, @GenieDev101, @CubicleGangster,
      @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm,
      @VeroFess, @joaoback, @walsermedia, @LuxTronic'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-other-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in v0.6.41
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in v0.6.41

**Open WebUI** · 2025-12-02 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!CAUTION]

> > ⚠️ **IMPORTANT for Multi-Instance Deployments**: This release includes database schema changes; multi-worker, multi-server, or load-balanced deployments must update all instances simultaneously rather than performing rolling updates, as running mixed versions will cause application failures due to schema incompatibility between old and new instances.

> 📂 Administrators can now globally disable the folders feature and control user-level folder permissions through the admin panel, enabling minimalist interface configurations for deployments that don't require workspace organization features. [#19529](https://github.com/open-webui/open-webui/pull/19529), [#19210](https://github.com/open-webui/open-webui/discussions/19210), [#18459](https://github.com/open-webui/open-webui/discussions/18459), [#18299](https://github.com/open-webui/open-webui/discussions/18299)

> 🌍 Translations for German, French, Portuguese (Brazil), Catalan, Simplified Chinese, and Traditional Chinese were enhanced and expanded.

> 🔒 Redis TLS connection failures were resolved by updating the python-socketio dependency to version 5.15.0, restoring support for the "rediss://" URL schema. [#19480](https://github.com/open-webui/open-webui/issues/19480), [#19488](https://github.com/open-webui/open-webui/pull/19488)

> 🌙 Dark mode select dropdown styling was corrected to use proper background colors, fixing an issue where dropdown borders and hover states appeared white instead of matching the dark theme. [#19693](https://github.com/open-webui/open-webui/pull/19693), [#19442](https://github.com/open-webui/open-webui/issues/19442)

> 🔍 Milvus vector database query filtering was fixed by correcting string quote handling in filter expressions and using the proper parameter name for queries, resolving false "duplicate content detected" errors that prevented uploading multiple files to knowledge bases. [#19602](https://github.com/open-webui/open-webui/pull/19602), [#18119](https://github.com/open-webui/open-webui/issues/18119), [#16345](https://github.com/open-webui/open-webui/issues/16345), [#17088](https://github.com/open-webui/open-webui/issues/17088), [#18485](https://github.com/open-webui/open-webui/issues/18485)

> 🆙 Milvus multitenancy vector database was updated to use query_iterator() for improved robustness and consistency with the standard Milvus implementation, fixing the same false duplicate detection errors and improving handling of large result sets in multi-tenant deployments. [#19695](https://github.com/open-webui/open-webui/pull/19695)

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @Classic298, @ShirasawaSama, @tobiasge, @RomualdYT, @joaoback, @kjpoccia, @gerhardj-b, @aleixdorca, @acwoo97, @matthew-kusz, @stevessr, @HennieLP

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> @amd, @roosi-gmbh, @rndmcnlly, @feddersen-group, @SRKConsulting, @mushmax, @icanbwell, @loitragg, @haka4githu6, @silenceroom, @GenieDev101, @CubicleGangster, @TOWaB, @Classic298, @comet-ml, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess, @joaoback, @walsermedia, @LuxTronic

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-11-interface-experience-changes-in-v0-6-41|11 Interface Experience changes in v0.6.41]] · Interface Experience
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-d834a6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-13-other-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-d834a6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->