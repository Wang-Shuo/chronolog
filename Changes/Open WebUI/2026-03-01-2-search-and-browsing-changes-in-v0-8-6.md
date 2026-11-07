---
card_id: open-webui-2026-03-01-2f0f89
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Search and Browsing: 2 changes in v0.8.6 —
  \U0001F5A5️ **Open Terminal integration.** Users can now connect to [Open…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 44e18a34f0743f4754350c68e52b6c25e5831d5ec0f1b24cbd4356ab38e9c258
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-2f0f89
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 2 Search and Browsing changes'
  evidence:
  - quote: "\U0001F5A5️ **Open Terminal integration.** Users can now connect to [Open
      Terminal](https://github.com/open-webui/open-terminal) instances to browse,
      read, and upload files directly in chat, with the terminal acting as an always-on
      tool. File navigation includes folder browsing, image and PDF previews, drag-and-drop
      uploads, directory creation, and file deletion. The current working directory
      is automatically injected into tool descriptions for context-aware commands.
      [Commit](https://github.com/open-webui/open-webui/commit/636ab99ad8e5b71b32dd37ba7c62c32368585b2a),
      [Commit](https://github.com/open-webui/open-webui/commit/64ff15a5365e2c4122fccab582782669f06ec58d),
      [Commit](https://github.com/open-webui/open-webui/commit/4737e1f11847d057859ec78892fa89e24cbcd83b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F50D **Web search domain filter config.** The WEB_SEARCH_DOMAIN_FILTER_LIST
      environment variable is now correctly read and applied, fixing an issue where
      domain filtering for web searches always used an empty default value. [#21964](https://github.com/open-webui/open-webui/pull/21964),
      [#20186](https://github.com/open-webui/open-webui/issues/20186)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-search-and-browsing-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: search-browsing
  title: 2 Search and Browsing changes in v0.8.6
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-02-25-introduce-limits-for-search-results-by-gundermanc-in-https-github-com-google-gem|Introduce
  limits for search results]]'
- '[[Changes/GitHub Copilot CLI/2026-02-25-add-research-command-for-deep-research-with-exportable-reports|Add
  /research command for deep research with exportable reports]]'
- '[[Changes/ChatGPT/2026-02-27-open-search-results-in-a-new-tab-cmd-click-in-the-search-panel-now-opens-results|Open
  search results in a new tab]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: search-browsing
title: 2 Search and Browsing changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Search and Browsing changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖥️ **Open Terminal integration.** Users can now connect to [Open Terminal](https://github.com/open-webui/open-terminal) instances to browse, read, and upload files directly in chat, with the terminal acting as an always-on tool. File navigation includes folder browsing, image and PDF previews, drag-and-drop uploads, directory creation, and file deletion. The current working directory is automatically injected into tool descriptions for context-aware commands. [Commit](https://github.com/open-webui/open-webui/commit/636ab99ad8e5b71b32dd37ba7c62c32368585b2a), [Commit](https://github.com/open-webui/open-webui/commit/64ff15a5365e2c4122fccab582782669f06ec58d), [Commit](https://github.com/open-webui/open-webui/commit/4737e1f11847d057859ec78892fa89e24cbcd83b)

> 🔍 **Web search domain filter config.** The WEB_SEARCH_DOMAIN_FILTER_LIST environment variable is now correctly read and applied, fixing an issue where domain filtering for web searches always used an empty default value. [#21964](https://github.com/open-webui/open-webui/pull/21964), [#20186](https://github.com/open-webui/open-webui/issues/20186)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-02-27 · ChatGPT · [[Changes/ChatGPT/2026-02-27-open-search-results-in-a-new-tab-cmd-click-in-the-search-panel-now-opens-results|Open search results in a new tab]]
- Later: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-13538-chore-add-web-search-tool-type-for-image-support-sayan-oai|♯13538 chore: add web_search_tool_type for image support @sayan-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-2f0f89&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-2-search-and-browsing-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-2f0f89%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->