---
card_id: open-webui-2026-07-27-96d98c
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Search and Browsing: 7 changes in v0.11.0
  — \U0001F4DC **Client certificates for SearXNG.** Web search can now present a client
  certificate to…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1222
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c51be95188343b508a2320c1ae8ffad7e4f5f2bb26cec77dbbd3e88565e4d28e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-96d98c
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 7 Search and Browsing changes'
  evidence:
  - quote: "\U0001F4DC **Client certificates for SearXNG.** Web search can now present
      a client certificate to a SearXNG instance that requires one, through new \"SEARXNG_CLIENT_CERT_FILE\"
      and \"SEARXNG_CLIENT_KEY_FILE\" settings. [Commit](https://github.com/open-webui/open-webui/commit/def26ce266c2e1d80e31b3ad12099db61a674832),
      [#26992](https://github.com/open-webui/open-webui/issues/26992)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F52D **OpenSERP web search.** Web search can now run against a self-hosted
      OpenSERP instance, which returns results from several major search engines without
      any API key, configured through a new \"OPENSERP_BASE_URL\" setting. [#27437](https://github.com/open-webui/open-webui/pull/27437),
      [#27438](https://github.com/open-webui/open-webui/issues/27438)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F96C **Faster web page parsing.** Pages pulled in by web search
      and web retrieval are now read with a faster parser, cutting roughly a tenth
      off the time spent on a ten result search. [#27439](https://github.com/open-webui/open-webui/pull/27439)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9ED **No pointless lookups when filtering search results.** Filtering
      web search results against a domain list no longer resolves every result to
      an address first, which had turned a three second search into half a minute
      wherever the resolver was slow or a name did not resolve. [Commit](https://github.com/open-webui/open-webui/commit/42ea8a5a2f04b6a57ccb47a61611a62479b60b78),
      [#26920](https://github.com/open-webui/open-webui/issues/26920)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAD7 **Web search results scoped to you.** The temporary collections
      holding a web search's pages are now tied to the person who ran the search,
      closing the one place where that scoping was not applied. [#26706](https://github.com/open-webui/open-webui/pull/26706)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6AB **Disabled terminal servers are refused.** A terminal connection
      an administrator has turned off can no longer be reached by browsing its files,
      opening a session, or calling its tools, rather than only disappearing from
      the interface. [Commit](https://github.com/open-webui/open-webui/commit/7537989235675ac84a40bf70c91ec3e16fc0d8db)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E2 **Web search failures explained.** When a search finds pages
      but cannot store them, the chat now says what went wrong and points at the document
      settings, instead of reporting sites searched and then no sources found. [#26883](https://github.com/open-webui/open-webui/pull/26883)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-search-and-browsing-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: search-browsing
  title: 7 Search and Browsing changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3
  Search and Browsing changes in rust-v0.145.0]]'
- '[[Changes/Claude Code/2026-07-22-changed-deep-research-to-start-only-when-invoked-manually-claude-no-longer-launc|Changed
  /deep-research to start only when invoked manually]]'
- '[[Changes/OpenCode/2026-07-24-core-preserve-grep-symlink-paths-in-search-results|Core
  Preserve grep symlink paths in search results]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: search-browsing
title: 7 Search and Browsing changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Search and Browsing changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📜 **Client certificates for SearXNG.** Web search can now present a client certificate to a SearXNG instance that requires one, through new "SEARXNG_CLIENT_CERT_FILE" and "SEARXNG_CLIENT_KEY_FILE" settings. [Commit](https://github.com/open-webui/open-webui/commit/def26ce266c2e1d80e31b3ad12099db61a674832), [#26992](https://github.com/open-webui/open-webui/issues/26992)

> 🔭 **OpenSERP web search.** Web search can now run against a self-hosted OpenSERP instance, which returns results from several major search engines without any API key, configured through a new "OPENSERP_BASE_URL" setting. [#27437](https://github.com/open-webui/open-webui/pull/27437), [#27438](https://github.com/open-webui/open-webui/issues/27438)

> 🥬 **Faster web page parsing.** Pages pulled in by web search and web retrieval are now read with a faster parser, cutting roughly a tenth off the time spent on a ten result search. [#27439](https://github.com/open-webui/open-webui/pull/27439)

> 🧭 **No pointless lookups when filtering search results.** Filtering web search results against a domain list no longer resolves every result to an address first, which had turned a three second search into half a minute wherever the resolver was slow or a name did not resolve. [Commit](https://github.com/open-webui/open-webui/commit/42ea8a5a2f04b6a57ccb47a61611a62479b60b78), [#26920](https://github.com/open-webui/open-webui/issues/26920)

> 🫗 **Web search results scoped to you.** The temporary collections holding a web search's pages are now tied to the person who ran the search, closing the one place where that scoping was not applied. [#26706](https://github.com/open-webui/open-webui/pull/26706)

> 🚫 **Disabled terminal servers are refused.** A terminal connection an administrator has turned off can no longer be reached by browsing its files, opening a session, or calling its tools, rather than only disappearing from the interface. [Commit](https://github.com/open-webui/open-webui/commit/7537989235675ac84a40bf70c91ec3e16fc0d8db)

> 📢 **Web search failures explained.** When a search finds pages but cannot store them, the chat now says what went wrong and points at the document settings, instead of reporting sites searched and then no sources found. [#26883](https://github.com/open-webui/open-webui/pull/26883)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-07-24 · OpenCode · [[Changes/OpenCode/2026-07-24-core-preserve-grep-symlink-paths-in-search-results|Core Preserve grep symlink paths in search results]]
- Later: 2026-07-29 · Codex CLI · [[Changes/Codex CLI/2026-07-29-2-search-and-browsing-changes-in-rust-v0-146-0|2 Search and Browsing changes in rust-v0.146.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-96d98c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-7-search-and-browsing-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-96d98c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->