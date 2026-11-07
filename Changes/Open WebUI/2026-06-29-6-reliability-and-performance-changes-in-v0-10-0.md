---
card_id: open-webui-2026-06-29-6c5c55
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Reliability and Performance: 6 changes in
  v0.10.0 — \U0001F680 **Much faster hybrid search on large knowledge bases.** Hybrid
  search now runs…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2779
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fce91d7cb81865acf36058a249e453d7893cc257a002d79ada4a4d3d20995c10
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-6c5c55
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 6 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F680 **Much faster hybrid search on large knowledge bases.** Hybrid
      search now runs natively in the database on pgvector setups instead of loading
      an entire collection into memory, so querying large knowledge bases is dramatically
      faster. [Commit](https://github.com/open-webui/open-webui/commit/223f484ded01d092979693341dc03351a9fa17fa),
      [#20737](https://github.com/open-webui/open-webui/discussions/20737)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Faster math rendering.** Rendered math is now cached and reused, so
      messages with repeated or unchanged math expressions render more efficiently.
      [#25847](https://github.com/open-webui/open-webui/pull/25847)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Snappier read-only code blocks.** Read-only code blocks now skip language
      auto-detection, so they render faster. [#25824](https://github.com/open-webui/open-webui/pull/25824)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Lighter, faster file search on large knowledge bases.** Listing and
      searching files no longer returns each file's full extracted text by default,
      and content matching is now length-bounded, so these requests are far lighter
      and searching across very large knowledge bases is dramatically faster. [Commit](https://github.com/open-webui/open-webui/commit/36d08fa2a7),
      [Commit](https://github.com/open-webui/open-webui/commit/46c1d6591badb6ab567ba1b8fae23475d5da105a),
      [Commit](https://github.com/open-webui/open-webui/commit/ab84bbf08c5935f1a19044ef581986f83311da8b),
      [#25774](https://github.com/open-webui/open-webui/pull/25774), [#25741](https://github.com/open-webui/open-webui/issues/25741),
      [#26145](https://github.com/open-webui/open-webui/pull/26145), [#25867](https://github.com/open-webui/open-webui/issues/25867)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Faster password hashing and bulk user import.** Password hashing and
      verification no longer block the server, and importing users from a CSV is now
      processed in a single batch, keeping large imports and sign-ins responsive.
      [Commit](https://github.com/open-webui/open-webui/commit/6fdf9b4340), [#25804](https://github.com/open-webui/open-webui/pull/25804),
      [#25805](https://github.com/open-webui/open-webui/pull/25805)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-reliability-and-performance-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: reliability-performance
  title: 6 Reliability and Performance changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-06-25-optimized-file-watching-notifications-to-prevent-visual-flickering-and-improve-p|Optimized
  file watching notifications to prevent visual flickering and improve…]]'
- '[[Changes/Ollama/2026-06-25-llm-size-mmproj-offload-by-projector-memory-by-dhiltgen-in-https-github-com-olla|llm:
  size mmproj offload by projector memory]]'
- '[[Changes/Kimi Code/2026-06-29-upgrade-web-markdown-renderer-dependencies-katex-markstream-vue-shiki-for-bug-fi|Upgrade
  web markdown renderer dependencies (katex, markstream-vue, shiki) for bug…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: reliability-performance
title: 6 Reliability and Performance changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Reliability and Performance changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚀 **Much faster hybrid search on large knowledge bases.** Hybrid search now runs natively in the database on pgvector setups instead of loading an entire collection into memory, so querying large knowledge bases is dramatically faster. [Commit](https://github.com/open-webui/open-webui/commit/223f484ded01d092979693341dc03351a9fa17fa), [#20737](https://github.com/open-webui/open-webui/discussions/20737)

> ⚡ **Faster math rendering.** Rendered math is now cached and reused, so messages with repeated or unchanged math expressions render more efficiently. [#25847](https://github.com/open-webui/open-webui/pull/25847)

> ⚡ **Snappier read-only code blocks.** Read-only code blocks now skip language auto-detection, so they render faster. [#25824](https://github.com/open-webui/open-webui/pull/25824)

> ⚡ **Lighter, faster file search on large knowledge bases.** Listing and searching files no longer returns each file's full extracted text by default, and content matching is now length-bounded, so these requests are far lighter and searching across very large knowledge bases is dramatically faster. [Commit](https://github.com/open-webui/open-webui/commit/36d08fa2a7), [Commit](https://github.com/open-webui/open-webui/commit/46c1d6591badb6ab567ba1b8fae23475d5da105a), [Commit](https://github.com/open-webui/open-webui/commit/ab84bbf08c5935f1a19044ef581986f83311da8b), [#25774](https://github.com/open-webui/open-webui/pull/25774), [#25741](https://github.com/open-webui/open-webui/issues/25741), [#26145](https://github.com/open-webui/open-webui/pull/26145), [#25867](https://github.com/open-webui/open-webui/issues/25867)

> ⚡ **Faster password hashing and bulk user import.** Password hashing and verification no longer block the server, and importing users from a CSV is now processed in a single batch, keeping large imports and sign-ins responsive. [Commit](https://github.com/open-webui/open-webui/commit/6fdf9b4340), [#25804](https://github.com/open-webui/open-webui/pull/25804), [#25805](https://github.com/open-webui/open-webui/pull/25805)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-06-29 · Kimi Code · [[Changes/Kimi Code/2026-06-29-upgrade-web-markdown-renderer-dependencies-katex-markstream-vue-shiki-for-bug-fi|Upgrade web markdown renderer dependencies (katex, markstream-vue, shiki) for bug…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-6c5c55&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-6-reliability-and-performance-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-6c5c55%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->