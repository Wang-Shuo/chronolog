---
card_id: open-webui-2025-04-01-b56bc7
date: '2025-04-01'
description: "Open WebUI · 2025-04-01 · Other changes: 17 changes in v0.6.0 — \U0001F4E8
  **/messages Chat API Endpoint Support**: For power users building external AI systems,
  new…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ac3a162c03977c0699e16fe2316aba0bc3d49da89241130e796eab2756690500
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-04-01-b56bc7
  comparison: ''
  date: '2025-04-01'
  description: 'Open WebUI — v0.6.0: 17 other changes'
  evidence:
  - quote: "\U0001F4E8 **/messages Chat API Endpoint Support**: For power users building
      external AI systems, new endpoints allow precise control of messages asynchronously—feed
      long-running external responses into Open WebUI chats without coupling with
      the frontend."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F4E6 **Custom pip Options for Tools/Functions**: You can now specify
      custom pip installation options with \"PIP_OPTIONS\", \"PIP_PACKAGE_INDEX_OPTIONS\"
      environment variables—improving compatibility, support for private indexes,
      and better control over Python environments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F522 **Editable Message Counter**: You can now double-click the
      message count number and jump straight to editing the index—quickly navigate
      complex chats or regenerate specific messages precisely."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F5C3️ **Redis Sentinel Support Added**: Enhance deployment redundancy
      with support for Redis Sentinel for highly available, failover-safe Redis-based
      caching or pub/sub."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F5C2️ **Auto-Focus + Enter Submit for Folder Name**: When creating
      a new folder, the system automatically enters rename mode with name preselected—simplifying
      your org workflow."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F4CB **Cleaner UI for Tool Call Display**: Optimized the visual
      layout of called tools inside chat messages for better clarity and reduced visual
      clutter."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F9D1\U0001F4BB **Firefox Input Height Bug**: Text input in Firefox
      now maintains proper height, ensuring message boxes look consistent and behave
      predictably."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F9FE **Tika Blank Line Bug**: PDFs processed with Apache Tika 3.1.0.0
      no longer introduce excessive blank lines—improving RAG output quality and visual
      cleanliness."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F9EA **CSV Loader Encoding Issues**: CSV files with unknown encodings
      now automatically detect character sets, resolving import errors in non-UTF-8
      datasets."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F4E5 **File Deletion in Bypass Mode**: Resolved issue where files
      couldn’t be deleted from knowledge when “bypass embedding” mode was enabled."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F9FE **Normalize Citation Numbering**: Source citations now properly
      begin from \"1\" instead of \"0\"—improving consistency and professional presentation
      in AI outputs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F9FE **ENABLE_AUDIT_LOGS Setting Removed**: Deprecated setting “ENABLE_AUDIT_LOGS”
      has been fully removed—now controlled via “AUDIT_LOG_LEVEL” instead."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, **Long-Term Support (LTS) versions**,
      and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: '@JunaidPinjari, @melroy89, @Ithanil, @mahenning, @diwakar-s-maurya, @nikes,
      @panda44312, @softue, @philipp-horstenkamp, @tcgumus, @yak1ex, @foraxe, @ibaldonl,
      @hurxxxx, @taylorwilsdon, @TiancongLx, @PeterDaveHello, @FarisHijazi, @SadmL,
      @genjuro214, @kaytwo, @binxn, @djismgaming, @MaxJa4, @rgaricano, @jfbloom22,
      @shirayu, @Espinaydelfin, @aleixdorca, @OriginalSimon, @Alluuu, @Phlogi'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!):"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  - quote: '@ModonHolding, @agency-agency, @roosi-gmbh, @Unsupervisedcom, @feddersen-group,
      @SRKConsulting, @mushmax, @rndmcnlly, @icanbwell, @blogic-cz, @Krambu-Travis,
      @GenieDev101, @PortlandKyGuy, @sushibait, @CubicleGangster, @GitDatamind, @TOWaB,
      @TheZigGroup, @Classic298, @comet-ml'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 17-other-changes-in-v0-6-0
  source_release: open-webui-2025-04-01-v0-6-0-github-209478336-af8a2de0
  source_type: github_releases
  theme: uncategorized
  title: 17 other changes in v0.6.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-04-01-v0-6-0-github-209478336-af8a2de0|open-webui-2025-04-01-v0-6-0-github-209478336-af8a2de0]]'
source_type: github_releases
theme: uncategorized
title: 17 other changes in v0.6.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 other changes in v0.6.0

**Open WebUI** · 2025-04-01 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.0) · from [[Releases/Open WebUI/open-webui-2025-04-01-v0-6-0-github-209478336-af8a2de0|v0.6.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📨 **/messages Chat API Endpoint Support**: For power users building external AI systems, new endpoints allow precise control of messages asynchronously—feed long-running external responses into Open WebUI chats without coupling with the frontend.

> 📦 **Custom pip Options for Tools/Functions**: You can now specify custom pip installation options with "PIP_OPTIONS", "PIP_PACKAGE_INDEX_OPTIONS" environment variables—improving compatibility, support for private indexes, and better control over Python environments.

> 🔢 **Editable Message Counter**: You can now double-click the message count number and jump straight to editing the index—quickly navigate complex chats or regenerate specific messages precisely.

> 🗃️ **Redis Sentinel Support Added**: Enhance deployment redundancy with support for Redis Sentinel for highly available, failover-safe Redis-based caching or pub/sub.

> 🗂️ **Auto-Focus + Enter Submit for Folder Name**: When creating a new folder, the system automatically enters rename mode with name preselected—simplifying your org workflow.

> 📋 **Cleaner UI for Tool Call Display**: Optimized the visual layout of called tools inside chat messages for better clarity and reduced visual clutter.

> 🧑💻 **Firefox Input Height Bug**: Text input in Firefox now maintains proper height, ensuring message boxes look consistent and behave predictably.

> 🧾 **Tika Blank Line Bug**: PDFs processed with Apache Tika 3.1.0.0 no longer introduce excessive blank lines—improving RAG output quality and visual cleanliness.

> 🧪 **CSV Loader Encoding Issues**: CSV files with unknown encodings now automatically detect character sets, resolving import errors in non-UTF-8 datasets.

> 📥 **File Deletion in Bypass Mode**: Resolved issue where files couldn’t be deleted from knowledge when “bypass embedding” mode was enabled.

> 🧾 **Normalize Citation Numbering**: Source citations now properly begin from "1" instead of "0"—improving consistency and professional presentation in AI outputs.

> 🧾 **ENABLE_AUDIT_LOGS Setting Removed**: Deprecated setting “ENABLE_AUDIT_LOGS” has been fully removed—now controlled via “AUDIT_LOG_LEVEL” instead.

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, **Long-Term Support (LTS) versions**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @JunaidPinjari, @melroy89, @Ithanil, @mahenning, @diwakar-s-maurya, @nikes, @panda44312, @softue, @philipp-horstenkamp, @tcgumus, @yak1ex, @foraxe, @ibaldonl, @hurxxxx, @taylorwilsdon, @TiancongLx, @PeterDaveHello, @FarisHijazi, @SadmL, @genjuro214, @kaytwo, @binxn, @djismgaming, @MaxJa4, @rgaricano, @jfbloom22, @shirayu, @Espinaydelfin, @aleixdorca, @OriginalSimon, @Alluuu, @Phlogi

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!):

> @ModonHolding, @agency-agency, @roosi-gmbh, @Unsupervisedcom, @feddersen-group, @SRKConsulting, @mushmax, @rndmcnlly, @icanbwell, @blogic-cz, @Krambu-Travis, @GenieDev101, @PortlandKyGuy, @sushibait, @CubicleGangster, @GitDatamind, @TOWaB, @TheZigGroup, @Classic298, @comet-ml

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-04-01-3-interface-experience-changes-in-v0-6-0|3 Interface Experience changes in v0.6.0]] · Interface Experience
- [[Changes/Open WebUI/2025-04-01-2-apps-and-integrations-changes-in-v0-6-0|2 Apps and Integrations changes in v0.6.0]] · Apps and Integrations
- [[Changes/Open WebUI/2025-04-01-3-model-support-changes-in-v0-6-0|3 Model Support changes in v0.6.0]] · Model Support
- [[Changes/Open WebUI/2025-04-01-improved-error-handling-from-pipelines-pipelines-now-show-the-actual-returned-er|📚 Improved Error Handling from Pipelines]] · Developer Workflow
- [[Changes/Open WebUI/2025-04-01-internationalization-language-support-updates-added-estonian-and-galician-langua|🌍 Internationalization Language Support Updates]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-04-01-4-files-and-data-changes-in-v0-6-0|4 Files and Data changes in v0.6.0]] · Files and Data
- [[Changes/Open WebUI/2025-04-01-3-reliability-and-performance-changes-in-v0-6-0|3 Reliability and Performance changes in v0.6.0]] · Reliability and Performance
- [[Changes/Open WebUI/2025-04-01-2-enterprise-and-administration-changes-in-v0-6-0|2 Enterprise and Administration changes in v0.6.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-04-01-prompt-autocompletion-disabled-by-default-autocomplete-suggestions-while-typing|🧠 Prompt Autocompletion Disabled By Default]] · Editor Experience
- [[Changes/Open WebUI/2025-04-01-2-safety-and-privacy-changes-in-v0-6-0|2 Safety and Privacy changes in v0.6.0]] · Safety and Privacy
- [[Changes/Open WebUI/2025-04-01-2-account-and-access-changes-in-v0-6-0|2 Account and Access changes in v0.6.0]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-04-01-b56bc7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-04-01-17-other-changes-in-v0-6-0.md%0ACard%20ID%3A%20open-webui-2025-04-01-b56bc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->