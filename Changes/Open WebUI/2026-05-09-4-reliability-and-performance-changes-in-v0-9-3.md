---
card_id: open-webui-2026-05-09-b7646b
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Reliability and Performance: 4 changes in
  v0.9.3 — \U0001F680 **Faster prompt list loading.** Prompt and prompt-tag pages
  now load much faster…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2728
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2049b1a2da27d462eb5b41ed4874c6b372c602edd39658db06a13ffa321f4427
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-b7646b
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 4 Reliability and Performance changes'
  evidence:
  - quote: "\U0001F680 **Faster prompt list loading.** Prompt and prompt-tag pages
      now load much faster for non-admin users, even with large prompt libraries,
      because accessible prompts are filtered efficiently in a single database query.
      [#24288](https://github.com/open-webui/open-webui/pull/24288), [#24258](https://github.com/open-webui/open-webui/discussions/24258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ⚡ **Faster chat history loading.** Chat history maps now load from normalized
      message records when available, reducing overhead for large conversations while
      preserving fallback behavior for legacy chats. [Commit](https://github.com/open-webui/open-webui/commit/485d689cfd1ef8b9e7f77cd7b535b8b8747dff1f),
      [#23159](https://github.com/open-webui/open-webui/pull/23159)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ⚡ **Health check responsiveness.** Health and readiness probes now avoid
      blocking database calls and skip sync session commit handling on probe paths,
      improving responsiveness and reducing false unready transitions during database
      pressure. [#24380](https://github.com/open-webui/open-webui/pull/24380), [#24384](https://github.com/open-webui/open-webui/pull/24384)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-reliability-and-performance-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: reliability-performance
  title: 4 Reliability and Performance changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Ollama/2026-05-07-api-show-responses-are-now-cached-improving-median-latency-by-6-7x-which-will-in|/api/show
  responses are now cached, improving median latency…]]'
- '[[Changes/Codex CLI/2026-05-08-added-a-faster-cargo-profiling-build-profile-and-disabled-empty-doctest-targets|Added
  a faster Cargo profiling build profile and disabled empty doctest targets…]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-faster-user-list-and-user-switch-for-multi-account-users|Faster
  /user list and /user switch for multi-account users]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: reliability-performance
title: 4 Reliability and Performance changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Reliability and Performance changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚀 **Faster prompt list loading.** Prompt and prompt-tag pages now load much faster for non-admin users, even with large prompt libraries, because accessible prompts are filtered efficiently in a single database query. [#24288](https://github.com/open-webui/open-webui/pull/24288), [#24258](https://github.com/open-webui/open-webui/discussions/24258)

> ⚡ **Faster chat history loading.** Chat history maps now load from normalized message records when available, reducing overhead for large conversations while preserving fallback behavior for legacy chats. [Commit](https://github.com/open-webui/open-webui/commit/485d689cfd1ef8b9e7f77cd7b535b8b8747dff1f), [#23159](https://github.com/open-webui/open-webui/pull/23159)

> ⚡ **Health check responsiveness.** Health and readiness probes now avoid blocking database calls and skip sync session commit handling on probe paths, improving responsiveness and reducing false unready transitions during database pressure. [#24380](https://github.com/open-webui/open-webui/pull/24380), [#24384](https://github.com/open-webui/open-webui/pull/24384)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-08-faster-user-list-and-user-switch-for-multi-account-users|Faster /user list and /user switch for multi-account users]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-added-scroll-speed-command-to-tune-mouse-wheel-scroll-speed-with-a-live-preview|Added /scroll-speed command to tune mouse wheel scroll speed with a live preview]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-b7646b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-4-reliability-and-performance-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-b7646b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->