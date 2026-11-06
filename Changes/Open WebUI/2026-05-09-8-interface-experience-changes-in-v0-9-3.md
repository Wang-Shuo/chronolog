---
card_id: open-webui-2026-05-09-43e985
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Interface Experience: 8 changes in v0.9.3
  — \U0001F4C5 **Calendar creation flow.** Users can now create calendars from a dedicated
  modal and a…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d720cbe0e1e267543a819bb24e1eafc8237c39e7298f87165c0b1348f5513871
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-43e985
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 8 Interface Experience changes'
  evidence:
  - quote: "\U0001F4C5 **Calendar creation flow.** Users can now create calendars
      from a dedicated modal and a quick-add action in the calendar sidebar, making
      calendar setup faster from the calendar workspace. [Commit](https://github.com/open-webui/open-webui/commit/34146ab60f5dc1a2f8bdda8e61ce02797233a25d),
      [Commit](https://github.com/open-webui/open-webui/commit/1baf73bdd56f4e5ded12a4bd3c168f4d2a70b840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9EE **LaTeX copy shortcut.** You can now click rendered LaTeX expressions
      to copy the raw formula to your clipboard, making it easier to reuse equations
      outside chat. [Commit](https://github.com/open-webui/open-webui/commit/064fdecb675c176a04b024c16ce179f4dda45236),
      [#24244](https://github.com/open-webui/open-webui/pull/24244)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ✨ **Smoother rich text editing.** The message composer now defers formatting
      toolbar refresh work to the next animation frame, reducing typing jank while
      formatting controls stay accurate. [Commit](https://github.com/open-webui/open-webui/commit/794b97025d4c56f91d49c9d1ec4775d2ea07b53a),
      [#24013](https://github.com/open-webui/open-webui/pull/24013)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F517 **HTTP share link copy fallback.** Copy Link now works reliably
      on HTTP deployments by using a selection-based fallback when secure clipboard
      APIs are unavailable. [Commit](https://github.com/open-webui/open-webui/commit/f70b0da1563ffa0a8daecbe71cbc30fd8cf834c4),
      [#24135](https://github.com/open-webui/open-webui/issues/24135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F5 **Regeneration loading lock recovery.** Chats no longer get
      stuck in a permanent loading state after failed regenerations because invalid
      message-tree references are repaired before rendering. [Commit](https://github.com/open-webui/open-webui/commit/ee3b82926b37843f2771c6a8d432781a557ea96a),
      [#24424](https://github.com/open-webui/open-webui/issues/24424)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F6E1️ **Safer image URL handling.** Untrusted external image URLs
      are now blocked in profile and rich-text image rendering paths, preventing unintended
      client-side requests to attacker-controlled domains. [#24420](https://github.com/open-webui/open-webui/pull/24420)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F5A5️ **Terminal sidebar auto-open guard.** The terminal sidebar
      no longer auto-opens on chat load when OpenTerminal is disabled, because stale
      terminal IDs saved on models or in localStorage are now validated against available
      terminal servers before use."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F5 **Reliable background task cleanup.** The chat task lifecycle
      now deregisters completed tasks before checking for remaining siblings, eliminating
      the off-by-one timing issue that could leave the stop button stuck or dismiss
      the sidebar activity spinner too early."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-interface-experience-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: interface-experience
  title: 8 Interface Experience changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065
  feat(tui): redesign session picker @fcoury-oai]]'
- '[[Changes/Codex CLI/2026-05-08-20665-make-environment-providers-own-default-selection-starr-openai|♯20665
  Make environment providers own default selection @starr-openai]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-project-info-remains-visible-in-slash-command-picker-when-no-results-match|Project
  info remains visible in slash command picker when no results match]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: interface-experience
title: 8 Interface Experience changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Interface Experience changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📅 **Calendar creation flow.** Users can now create calendars from a dedicated modal and a quick-add action in the calendar sidebar, making calendar setup faster from the calendar workspace. [Commit](https://github.com/open-webui/open-webui/commit/34146ab60f5dc1a2f8bdda8e61ce02797233a25d), [Commit](https://github.com/open-webui/open-webui/commit/1baf73bdd56f4e5ded12a4bd3c168f4d2a70b840)

> 🧮 **LaTeX copy shortcut.** You can now click rendered LaTeX expressions to copy the raw formula to your clipboard, making it easier to reuse equations outside chat. [Commit](https://github.com/open-webui/open-webui/commit/064fdecb675c176a04b024c16ce179f4dda45236), [#24244](https://github.com/open-webui/open-webui/pull/24244)

> ✨ **Smoother rich text editing.** The message composer now defers formatting toolbar refresh work to the next animation frame, reducing typing jank while formatting controls stay accurate. [Commit](https://github.com/open-webui/open-webui/commit/794b97025d4c56f91d49c9d1ec4775d2ea07b53a), [#24013](https://github.com/open-webui/open-webui/pull/24013)

> 🔗 **HTTP share link copy fallback.** Copy Link now works reliably on HTTP deployments by using a selection-based fallback when secure clipboard APIs are unavailable. [Commit](https://github.com/open-webui/open-webui/commit/f70b0da1563ffa0a8daecbe71cbc30fd8cf834c4), [#24135](https://github.com/open-webui/open-webui/issues/24135)

> 🧵 **Regeneration loading lock recovery.** Chats no longer get stuck in a permanent loading state after failed regenerations because invalid message-tree references are repaired before rendering. [Commit](https://github.com/open-webui/open-webui/commit/ee3b82926b37843f2771c6a8d432781a557ea96a), [#24424](https://github.com/open-webui/open-webui/issues/24424)

> 🛡️ **Safer image URL handling.** Untrusted external image URLs are now blocked in profile and rich-text image rendering paths, preventing unintended client-side requests to attacker-controlled domains. [#24420](https://github.com/open-webui/open-webui/pull/24420)

> 🖥️ **Terminal sidebar auto-open guard.** The terminal sidebar no longer auto-opens on chat load when OpenTerminal is disabled, because stale terminal IDs saved on models or in localStorage are now validated against available terminal servers before use.

> 🧵 **Reliable background task cleanup.** The chat task lifecycle now deregisters completed tasks before checking for remaining siblings, eliminating the off-by-one timing issue that could leave the stop button stuck or dismiss the sidebar activity spinner too early.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-05-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-08-project-info-remains-visible-in-slash-command-picker-when-no-results-match|Project info remains visible in slash command picker when no results match]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-43e985&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-8-interface-experience-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-43e985%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->