---
card_id: open-webui-2026-05-10-8b907a
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Interface Experience: 2 changes in v0.9.5
  — \U0001F39B️ **Granular markdown rendering controls.** Users can now independently
  disable Markdown…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1217
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ca2ab2c00be5fd35e08bb182e9310f20ca46ccd52db7e67335363fe79a4479f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-8b907a
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 2 Interface Experience changes'
  evidence:
  - quote: "\U0001F39B️ **Granular markdown rendering controls.** Users can now independently
      disable Markdown rendering for user messages and assistant responses from Interface
      settings, preventing unintended formatting when pasting text that contains Markdown-sensitive
      characters. [Commit](https://github.com/open-webui/open-webui/commit/4a1064cefd6f48a8b3b02cd31f77838c8802b635)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F9F5 **Legacy chat history self-healing.** Loading legacy conversations
      now automatically detects broken parent-link graphs in migrated message records,
      merges missing messages from the embedded JSON history, and backfills them to
      the normalized table so future loads use the fast path without data loss. [Commit](https://github.com/open-webui/open-webui/commit/1388f4568b8f508c26542673dd01f1fa049e798a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-interface-experience-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: interface-experience
  title: 2 Interface Experience changes in v0.9.5
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-08-20665-make-environment-providers-own-default-selection-starr-openai|♯20665
  Make environment providers own default selection @starr-openai]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-project-info-remains-visible-in-slash-command-picker-when-no-results-match|Project
  info remains visible in slash command picker when no results match]]'
- '[[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface
  Experience changes in v0.9.3]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: interface-experience
title: 2 Interface Experience changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Interface Experience changes in v0.9.5

**Open WebUI** · 2026-05-10 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎛️ **Granular markdown rendering controls.** Users can now independently disable Markdown rendering for user messages and assistant responses from Interface settings, preventing unintended formatting when pasting text that contains Markdown-sensitive characters. [Commit](https://github.com/open-webui/open-webui/commit/4a1064cefd6f48a8b3b02cd31f77838c8802b635)

> 🧵 **Legacy chat history self-healing.** Loading legacy conversations now automatically detects broken parent-link graphs in migrated message records, merges missing messages from the embedded JSON history, and backfills them to the normalized table so future loads use the fast path without data loss. [Commit](https://github.com/open-webui/open-webui/commit/1388f4568b8f508c26542673dd01f1fa049e798a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-05-09 · Open WebUI · [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-8b907a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-2-interface-experience-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-8b907a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->