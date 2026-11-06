---
card_id: open-webui-2026-05-09-ee9fea
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Safety and Privacy: 3 changes in v0.9.3 —
  \U0001F510 **Public chat sharing permission control.** Administrators can now control
  whether users…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1119
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f6ee3cdc1a7aa259132e889b54689597efd32eb22f7c7df7fb0aafcb93f03c2a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-ee9fea
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 3 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F510 **Public chat sharing permission control.** Administrators
      can now control whether users are allowed to create publicly shareable chats
      through a dedicated permission setting. [Commit](https://github.com/open-webui/open-webui/commit/ef6d4f2d6c4b79c7e12e864a4fcb6a57ee84e5d4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ⚡ **Faster prompt tag loading.** Prompt tag filters now load much faster
      for non-admin users by fetching only accessible tags directly, avoiding per-prompt
      permission checks and unnecessary prompt data loading. [#24287](https://github.com/open-webui/open-webui/pull/24287),
      [#24258](https://github.com/open-webui/open-webui/discussions/24258)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4C5 **Calendar event permission checks.** Calendar event update
      and delete actions now handle ownership and access checks more reliably, returning
      clean access-denied results when appropriate. [Commit](https://github.com/open-webui/open-webui/commit/2977910ffd9d2369dfa504aa6ab12745b3dbd19a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-safety-and-privacy-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-08-2-safety-and-privacy-changes-in-rust-v0-130-0|2
  Safety and Privacy changes in rust-v0.130.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-pressing-ctrl-c-while-a-permission-prompt-is-pending-no-longer-causes-the-cli-to|Pressing
  Ctrl+C while a permission prompt is pending no longer causes the CLI to hang]]'
- '[[Changes/Replit/2026-05-08-workspace-security-center-2-0|Workspace Security Center
  2.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Public chat sharing permission control.** Administrators can now control whether users are allowed to create publicly shareable chats through a dedicated permission setting. [Commit](https://github.com/open-webui/open-webui/commit/ef6d4f2d6c4b79c7e12e864a4fcb6a57ee84e5d4)

> ⚡ **Faster prompt tag loading.** Prompt tag filters now load much faster for non-admin users by fetching only accessible tags directly, avoiding per-prompt permission checks and unnecessary prompt data loading. [#24287](https://github.com/open-webui/open-webui/pull/24287), [#24258](https://github.com/open-webui/open-webui/discussions/24258)

> 📅 **Calendar event permission checks.** Calendar event update and delete actions now handle ownership and access checks more reliably, returning clean access-denied results when appropriate. [Commit](https://github.com/open-webui/open-webui/commit/2977910ffd9d2369dfa504aa6ab12745b3dbd19a)

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
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-08 · Replit · [[Changes/Replit/2026-05-08-workspace-security-center-2-0|Workspace Security Center 2.0]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-ee9fea&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-3-safety-and-privacy-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-ee9fea%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->