---
card_id: open-webui-2025-09-09-8a3bc7
date: '2025-09-09'
description: "Open WebUI · 2025-09-09 · Developer Workflow: 14 changes in v0.6.27
  — \U0001F4C1 Emoji folder icons were added, allowing users to personalize workspace
  organization…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2555
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2559b612e51a78cdba594129eab21ada7091d1038f66584ff54477db658a2909
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-09-8a3bc7
  comparison: ''
  date: '2025-09-09'
  description: 'Open WebUI — v0.6.27: 14 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4C1 Emoji folder icons were added, allowing users to personalize
      workspace organization with visual cues, including improved chevron display.
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/1588f42fe777ad5d807e3f2fc8dbbc47a8db87c0),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/b70c0f36c0f5bbfc2a767429984d6fba1a7bb26c),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/11dea8795bfce42aa5d8d58ef316ded05173bd87),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/c0a47169fa059154d5f5a9ea6b94f9a66d82f255)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4C1 The 'Search Collection' input field now dynamically displays
      the total number of files within the knowledge base. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/fbbe1117ae4c9c8fec6499d790eee275818eccc5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4DA The knowledge API now supports a \"delete_file\" query parameter,
      allowing configurable file deletion behavior. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/22c4ef4fb096498066b73befe993ae3a82f7a8e7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4CA Llama.cpp timing statistics are now integrated into the usage
      field for comprehensive model performance metrics. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/e830b4959ecd4b2795e29e53026984a58a7696a9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F5C4️ The PGVECTOR_CREATE_EXTENSION environment variable now allows
      control over automatic pgvector extension creation. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/c2b4976c82d335ed524bd80dc914b5e2f5bfbd9e),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/b45219c8b15b48d5ee3d42983e1107bbcefbab01),
      [Docs:#672](https://github.com/open-webui/docs/pull/672)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4AC A new setting was added to control whether clicking a suggested
      prompt automatically sends the message or only inserts the text. [#17192](https://github.com/open-webui/open-webui/issues/17192),
      [Commit](https://github.com/open-webui/open-webui/commit/e023a98f11fc52feb21e4065ec707cc98e50c7d3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F40D Code execution package detection precision is improved in Pyodide
      to prevent unnecessary package inclusions. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/bbe116795860a81a647d9567e0d9cb1950650095)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F6E0️ Tool message format API compliance is fixed by ensuring content
      fields in tool call responses contain valid string values instead of null. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/37bf0087e5b8a324009c9d06b304027df351ea6b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4BE Knowledge file save race conditions are prevented by serializing
      API calls and adding an \"isSaving\" guard. [#17137](https://github.com/open-webui/open-webui/pull/17137),
      [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/4ca936f0bf9813bee11ec8aea41d7e34fb6b16a9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F517 Web page and YouTube attachments are now correctly processed
      by setting their type as \"text\" and using collection names for accurate content
      retrieval. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/487979859a6ffcfd60468f523822cdf838fbef5b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4C1 Knowledge base update validation errors are resolved, ensuring
      seamless management via UI or API. [#17244](https://github.com/open-webui/open-webui/issues/17244),
      [Commit](https://github.com/open-webui/open-webui/commit/9aac1489080a5c9441e89b1a56de0d3a672bc5fb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F512 OIDC access denied errors are now displayed as user-friendly
      toast notifications instead of raw JSON. [#17208](https://github.com/open-webui/open-webui/issues/17208),
      [Commit](https://github.com/open-webui/open-webui/commit/3d6d050ad82d360adc42d6e9f42e8faf8d13c9f4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F4AC Chat exception handling is enhanced to prevent system instability
      during message generation and ensure graceful error recovery. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/f56889c5c7f0cf1a501c05d35dfa614e4f8b6958)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  - quote: "\U0001F6E0️ Renamed \"Tools\" to \"External Tools\" across the UI for
      clearer distinction between built-in and external functionalities. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/0bca4e230ef276bec468889e3be036242ad11086f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 14-developer-workflow-changes-in-v0-6-27
  source_release: open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819
  source_type: github_releases
  theme: developer-workflow
  title: 14 Developer Workflow changes in v0.6.27
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-05-3-developer-workflow-changes-in-rust-v0-30-0|3 Developer
  Workflow changes in rust-v0.30.0]]'
- '[[Changes/Codex CLI/2025-09-08-2-developer-workflow-changes-in-rust-v0-31-0|2 Developer
  Workflow changes in rust-v0.31.0]]'
- '[[Changes/Gemini CLI/2025-09-09-3-developer-workflow-changes-in-v0-4-0|3 Developer
  Workflow changes in v0.4.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819]]'
source_type: github_releases
theme: developer-workflow
title: 14 Developer Workflow changes in v0.6.27
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Developer Workflow changes in v0.6.27

**Open WebUI** · 2025-09-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.27) · from [[Releases/Open WebUI/open-webui-2025-09-09-v0-6-27-github-245869039-35ab9819|v0.6.27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📁 Emoji folder icons were added, allowing users to personalize workspace organization with visual cues, including improved chevron display. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/1588f42fe777ad5d807e3f2fc8dbbc47a8db87c0), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/b70c0f36c0f5bbfc2a767429984d6fba1a7bb26c), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/11dea8795bfce42aa5d8d58ef316ded05173bd87), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/c0a47169fa059154d5f5a9ea6b94f9a66d82f255)

> 📁 The 'Search Collection' input field now dynamically displays the total number of files within the knowledge base. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/fbbe1117ae4c9c8fec6499d790eee275818eccc5)

> 📚 The knowledge API now supports a "delete_file" query parameter, allowing configurable file deletion behavior. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/22c4ef4fb096498066b73befe993ae3a82f7a8e7)

> 📊 Llama.cpp timing statistics are now integrated into the usage field for comprehensive model performance metrics. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/e830b4959ecd4b2795e29e53026984a58a7696a9)

> 🗄️ The PGVECTOR_CREATE_EXTENSION environment variable now allows control over automatic pgvector extension creation. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/c2b4976c82d335ed524bd80dc914b5e2f5bfbd9e), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/b45219c8b15b48d5ee3d42983e1107bbcefbab01), [Docs:#672](https://github.com/open-webui/docs/pull/672)

> 💬 A new setting was added to control whether clicking a suggested prompt automatically sends the message or only inserts the text. [#17192](https://github.com/open-webui/open-webui/issues/17192), [Commit](https://github.com/open-webui/open-webui/commit/e023a98f11fc52feb21e4065ec707cc98e50c7d3)

> 🐍 Code execution package detection precision is improved in Pyodide to prevent unnecessary package inclusions. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/bbe116795860a81a647d9567e0d9cb1950650095)

> 🛠️ Tool message format API compliance is fixed by ensuring content fields in tool call responses contain valid string values instead of null. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/37bf0087e5b8a324009c9d06b304027df351ea6b)

> 💾 Knowledge file save race conditions are prevented by serializing API calls and adding an "isSaving" guard. [#17137](https://github.com/open-webui/open-webui/pull/17137), [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/4ca936f0bf9813bee11ec8aea41d7e34fb6b16a9)

> 🔗 Web page and YouTube attachments are now correctly processed by setting their type as "text" and using collection names for accurate content retrieval. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/487979859a6ffcfd60468f523822cdf838fbef5b)

> 📁 Knowledge base update validation errors are resolved, ensuring seamless management via UI or API. [#17244](https://github.com/open-webui/open-webui/issues/17244), [Commit](https://github.com/open-webui/open-webui/commit/9aac1489080a5c9441e89b1a56de0d3a672bc5fb)

> 🔒 OIDC access denied errors are now displayed as user-friendly toast notifications instead of raw JSON. [#17208](https://github.com/open-webui/open-webui/issues/17208), [Commit](https://github.com/open-webui/open-webui/commit/3d6d050ad82d360adc42d6e9f42e8faf8d13c9f4)

> 💬 Chat exception handling is enhanced to prevent system instability during message generation and ensure graceful error recovery. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/f56889c5c7f0cf1a501c05d35dfa614e4f8b6958)

> 🛠️ Renamed "Tools" to "External Tools" across the UI for clearer distinction between built-in and external functionalities. [Commit](https://github.com/open-webui/open-webui/pull/17070/commits/0bca4e230ef276bec468889e3be036242ad11086f)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-09-web-search-result-display-was-enhanced-to-include-titles-and-favicons-providing|💬 Web search result display was enhanced to include titles and favicons, providing…]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-09-6-account-and-access-changes-in-v0-6-27|6 Account and Access changes in v0.6.27]] · Account and Access
- [[Changes/Open WebUI/2025-09-09-unicode-filename-support-is-improved-for-external-document-loaders-by-properly-u|📁 Unicode filename support is improved for external document loaders by properly…]] · Files and Data
- [[Changes/Open WebUI/2025-09-09-rag-loop-error-with-gemma-3-1-2b-instruct-is-fixed-by-correctly-unwrapping-unexp|🧠 RAG Loop/Error with Gemma 3.1 2B Instruct is fixed by correctly unwrapping…]] · Model Support
- [[Changes/Open WebUI/2025-09-09-4-safety-and-privacy-changes-in-v0-6-27|4 Safety and Privacy changes in v0.6.27]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-09-a-provider-toggle-in-connection-settings-now-allows-users-to-manually-specify-az|☁️ A provider toggle in connection settings now allows users to manually specify…]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-09-follow-up-tooltip-duplication-is-removed-streamlining-the-user-interface-and-pre|💬 Follow-up tooltip duplication is removed, streamlining the user interface…]] · Interface Experience
- [[Changes/Open WebUI/2025-09-09-5-reliability-and-performance-changes-in-v0-6-27|5 Reliability and Performance changes in v0.6.27]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-09-azure-openai-image-generation-is-now-supported-with-configurations-for-images-op|🎨 Azure OpenAI image generation is now supported, with configurations…]] · Image Generation
- [[Changes/Open WebUI/2025-09-09-17-other-changes-in-v0-6-27|17 other changes in v0.6.27]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-09-09 · Gemini CLI · [[Changes/Gemini CLI/2025-09-09-3-developer-workflow-changes-in-v0-4-0|3 Developer Workflow changes in v0.4.0]]
- Later: 2025-09-10 · Codex CLI · [[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer Workflow changes in rust-v0.32.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-09-8a3bc7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-09-14-developer-workflow-changes-in-v0-6-27.md%0ACard%20ID%3A%20open-webui-2025-09-09-8a3bc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->