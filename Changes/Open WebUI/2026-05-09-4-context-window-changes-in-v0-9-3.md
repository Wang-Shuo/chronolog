---
card_id: open-webui-2026-05-09-4cacae
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Context Window: 4 changes in v0.9.3 — \U0001F465
  **User group prompt variable.** System and template prompts now support the \"{{USER_GROUPS}}\"…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2425
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e397e8f3771dd8273759323650086f4c6f1e46092650cc1a220c423c412748cf
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-4cacae
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 4 Context Window changes'
  evidence:
  - quote: "\U0001F465 **User group prompt variable.** System and template prompts
      now support the \"{{USER_GROUPS}}\" variable, which expands to the user’s group
      memberships so prompts can adapt to role- or access-based context automatically.
      [Commit](https://github.com/open-webui/open-webui/commit/c1202a23277abb8e7080271a929dcc9d29b67e66),
      [#24462](https://github.com/open-webui/open-webui/issues/24462)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F3F7️ **Dynamic header template variables.** Administrators can
      now use chat, message, and user template variables in custom connection and
      tool server headers so each request can carry per-conversation context automatically.
      [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6),
      [#24164](https://github.com/open-webui/open-webui/pull/24164)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ✏️ **Assistant response editing and continuation.** You can now edit and
      restructure assistant output items — including reasoning blocks, tool calls,
      and text content — from a dedicated editor view, and continue generating from
      the edited state so the model receives full prior context.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4CE **Knowledge collection persistence.** Knowledge collections
      selected with the chat input selector now remain attached after reloads and
      chat switches, so attached context no longer disappears between sessions. [Commit](https://github.com/open-webui/open-webui/commit/7c398a625a8d51f79d80217f6d329fc30c72b782),
      [#24142](https://github.com/open-webui/open-webui/issues/24142)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-context-window-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v0.9.3
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-07-2-context-window-changes-in-v1-14-40|2 Context Window
  changes in v1.14.40]]'
- '[[Changes/Codex CLI/2026-05-08-2-context-window-changes-in-rust-v0-130-0|2 Context
  Window changes in rust-v0.130.0]]'
- '[[Changes/Replit/2026-05-08-external-access-tokens-for-private-deployments|External
  access tokens for Private Deployments]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👥 **User group prompt variable.** System and template prompts now support the "{{USER_GROUPS}}" variable, which expands to the user’s group memberships so prompts can adapt to role- or access-based context automatically. [Commit](https://github.com/open-webui/open-webui/commit/c1202a23277abb8e7080271a929dcc9d29b67e66), [#24462](https://github.com/open-webui/open-webui/issues/24462)

> 🏷️ **Dynamic header template variables.** Administrators can now use chat, message, and user template variables in custom connection and tool server headers so each request can carry per-conversation context automatically. [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6), [#24164](https://github.com/open-webui/open-webui/pull/24164)

> ✏️ **Assistant response editing and continuation.** You can now edit and restructure assistant output items — including reasoning blocks, tool calls, and text content — from a dedicated editor view, and continue generating from the edited state so the model receives full prior context.

> 📎 **Knowledge collection persistence.** Knowledge collections selected with the chat input selector now remain attached after reloads and chat switches, so attached context no longer disappears between sessions. [Commit](https://github.com/open-webui/open-webui/commit/7c398a625a8d51f79d80217f6d329fc30c72b782), [#24142](https://github.com/open-webui/open-webui/issues/24142)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
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
## Nearby in Context Window

- Earlier: 2026-05-08 · Replit · [[Changes/Replit/2026-05-08-external-access-tokens-for-private-deployments|External access tokens for Private Deployments]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-4cacae&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-4-context-window-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-4cacae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->