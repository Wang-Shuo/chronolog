---
card_id: open-webui-2026-09-21-bcd27d
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Search and Browsing: 6 changes in v0.11.4
  — \U0001F4CF **Exa result length cap.** Web search through Exa can be held to a
  number of characters…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added
    ability to batch delete/ignore search results]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2307
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d4cf8359e2ab81f4e82e12eb4b33544055263afe4f45b1e43db51fc78de0c6f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-bcd27d
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 6 Search and Browsing changes'
  evidence:
  - quote: "\U0001F4CF **Exa result length cap.** Web search through Exa can be held
      to a number of characters per result, set beside its key in the admin web search
      settings or as \"EXA_MAX_CONTENT_LENGTH\". [Commit](https://github.com/open-webui/open-webui/commit/12b14124b9376eccf2ba7cf3dba92bc145493703)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F1EA\U0001F1FA **European web search option.** Staan can now be
      picked as the web search provider, giving deployments that need search inside
      the EU an option they do not have to host themselves, configured from the admin
      web search settings or through \"STAAN_API_KEY\", \"STAAN_MARKET\" and \"STAAN_MAX_SNIPPETS\".
      [#30138](https://github.com/open-webui/open-webui/pull/30138), [#26006](https://github.com/open-webui/open-webui/discussions/26006),
      [#30303](https://github.com/open-webui/open-webui/pull/30303), [#30301](https://github.com/open-webui/open-webui/issues/30301)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4DA **Web results stop being cited.** Pages a web search only listed
      are no longer offered to the model as things to cite, which had it attaching
      a result id to text from a different result and the citations panel resolving
      that to a title that looked right. [#29631](https://github.com/open-webui/open-webui/pull/29631),
      [#29627](https://github.com/open-webui/open-webui/issues/29627)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F50E **SearchApi errors, news and links.** Web search through searchapi.io
      now reports a bad key instead of coming back empty, reads the news results it
      returns alongside its ordinary ones, and hands the web loader the resolved destination
      link, so citations stop pointing at a redirect page. [#30308](https://github.com/open-webui/open-webui/pull/30308),
      [#30305](https://github.com/open-webui/open-webui/issues/30305)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F50E **Slim leaves out DDGS.** DDGS, the metasearch provider that
      needs no key of its own, is not carried in the slim image, so web search there
      needs a provider with a key. [Commit](https://github.com/open-webui/open-webui/commit/0fa4dea5ff64ea663f162d07c9a1175c39e4aad0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F587️ **Link scheme rendering.** A link in a reply, a citation or
      a web search result is now rendered only where it points at a web address, a
      mail address, a telephone number or somewhere inside this instance; anything
      else, an \"ftp://\" address or an application link such as \"obsidian://\" or
      \"vscode://\" among them, is shown as the text it is. Two old oddities go with
      it: a source written as \"HTTP://\" now becomes a link, and a filename merely
      containing the letters http no longer becomes one that leads nowhere. [#29890](https://github.com/open-webui/open-webui/pull/29890)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-search-and-browsing-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: search-browsing
  title: 6 Search and Browsing changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-18-try-the-lovable-api-in-postman|Try the Lovable API
  in Postman]]'
- '[[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search
  and Browsing changes in v2026.9.5]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-consecutive-steering-prompts-in-the-same-mode-combine-into-one-pending-message-p|Consecutive
  steering prompts in the same mode combine into one pending message]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: search-browsing
title: 6 Search and Browsing changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Search and Browsing changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📏 **Exa result length cap.** Web search through Exa can be held to a number of characters per result, set beside its key in the admin web search settings or as "EXA_MAX_CONTENT_LENGTH". [Commit](https://github.com/open-webui/open-webui/commit/12b14124b9376eccf2ba7cf3dba92bc145493703)

> 🇪🇺 **European web search option.** Staan can now be picked as the web search provider, giving deployments that need search inside the EU an option they do not have to host themselves, configured from the admin web search settings or through "STAAN_API_KEY", "STAAN_MARKET" and "STAAN_MAX_SNIPPETS". [#30138](https://github.com/open-webui/open-webui/pull/30138), [#26006](https://github.com/open-webui/open-webui/discussions/26006), [#30303](https://github.com/open-webui/open-webui/pull/30303), [#30301](https://github.com/open-webui/open-webui/issues/30301)

> 📚 **Web results stop being cited.** Pages a web search only listed are no longer offered to the model as things to cite, which had it attaching a result id to text from a different result and the citations panel resolving that to a title that looked right. [#29631](https://github.com/open-webui/open-webui/pull/29631), [#29627](https://github.com/open-webui/open-webui/issues/29627)

> 🔎 **SearchApi errors, news and links.** Web search through searchapi.io now reports a bad key instead of coming back empty, reads the news results it returns alongside its ordinary ones, and hands the web loader the resolved destination link, so citations stop pointing at a redirect page. [#30308](https://github.com/open-webui/open-webui/pull/30308), [#30305](https://github.com/open-webui/open-webui/issues/30305)

> 🔎 **Slim leaves out DDGS.** DDGS, the metasearch provider that needs no key of its own, is not carried in the slim image, so web search there needs a provider with a key. [Commit](https://github.com/open-webui/open-webui/commit/0fa4dea5ff64ea663f162d07c9a1175c39e4aad0)

> 🖇️ **Link scheme rendering.** A link in a reply, a citation or a web search result is now rendered only where it points at a web address, a mail address, a telephone number or somewhere inside this instance; anything else, an "ftp://" address or an application link such as "obsidian://" or "vscode://" among them, is shown as the text it is. Two old oddities go with it: a source written as "HTTP://" now becomes a link, and a filename merely containing the letters http no longer becomes one that leads nowhere. [#29890](https://github.com/open-webui/open-webui/pull/29890)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-consecutive-steering-prompts-in-the-same-mode-combine-into-one-pending-message-p|Consecutive steering prompts in the same mode combine into one pending message]]
- Later: 2026-09-22 · AnythingLLM · [[Changes/AnythingLLM/2026-09-22-7-search-and-browsing-changes-in-v1-16-2|7 Search and Browsing changes in v1.16.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-05-28 · Descript · [[Changes/Descript/2020-05-28-added-ability-to-batch-delete-ignore-search-results|Added ability to batch delete/ignore search results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-bcd27d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-6-search-and-browsing-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-bcd27d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->