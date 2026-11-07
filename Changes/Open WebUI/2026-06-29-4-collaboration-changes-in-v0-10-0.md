---
card_id: open-webui-2026-06-29-21cdcd
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Collaboration: 4 changes in v0.10.0 — \U0001F9F9
  **Unshare all shared chats at once.** The Shared Chats dialog now has a button to
  stop…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2726
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f2ca24381567409861ce67fc720fe3ae60668f4911063b30fb70695c95900ded
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-21cdcd
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 4 Collaboration changes'
  evidence:
  - quote: "\U0001F9F9 **Unshare all shared chats at once.** The Shared Chats dialog
      now has a button to stop sharing every shared chat in one action. [#25848](https://github.com/open-webui/open-webui/pull/25848)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F47B **Collaborative notes reject unauthenticated presence events.**
      The remaining real-time note-collaboration events now require an authenticated
      session, so presence and cursors can no longer be spoofed by someone who only
      knows a note's ID. [#25946](https://github.com/open-webui/open-webui/pull/25946)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5D1️ **Unsharing cleans up orphaned rows.** Unsharing a chat now
      handles leftover shared-chat records, avoiding stale entries. [#25632](https://github.com/open-webui/open-webui/pull/25632)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F517 **Model share link updated.** Sharing a model now opens the
      current community post page, fixing the link that pointed at the old endpoint.
      [#25801](https://github.com/open-webui/open-webui/pull/25801)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-collaboration-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: collaboration
  title: 4 Collaboration changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-26-comments-in-shared-app-previews|Comments in shared
  app previews]]'
- '[[Changes/v0/2026-06-26-snowflake-gets-fewer-first-deploy-failures-creates-a-missing-snowflake-yml-for-y|Snowflake
  gets fewer first deploy failures, creates a missing snowflake.yml for you…]]'
- '[[Changes/Kimi Code/2026-06-29-scope-the-web-composer-s-up-down-input-history-to-the-current-session-instead-of|Scope
  the web composer''s up/down input history to the current session instead…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: collaboration
title: 4 Collaboration changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Collaboration changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧹 **Unshare all shared chats at once.** The Shared Chats dialog now has a button to stop sharing every shared chat in one action. [#25848](https://github.com/open-webui/open-webui/pull/25848)

> 👻 **Collaborative notes reject unauthenticated presence events.** The remaining real-time note-collaboration events now require an authenticated session, so presence and cursors can no longer be spoofed by someone who only knows a note's ID. [#25946](https://github.com/open-webui/open-webui/pull/25946)

> 🗑️ **Unsharing cleans up orphaned rows.** Unsharing a chat now handles leftover shared-chat records, avoiding stale entries. [#25632](https://github.com/open-webui/open-webui/pull/25632)

> 🔗 **Model share link updated.** Sharing a model now opens the current community post page, fixing the link that pointed at the old endpoint. [#25801](https://github.com/open-webui/open-webui/pull/25801)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
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
## Nearby in Collaboration

- Earlier: 2026-06-29 · Kimi Code · [[Changes/Kimi Code/2026-06-29-scope-the-web-composer-s-up-down-input-history-to-the-current-session-instead-of|Scope the web composer's up/down input history to the current session instead…]]
- Later: 2026-06-30 · Cursor · [[Changes/Cursor/2026-06-30-team-mcps-in-team-marketplaces-27f9ef|Team MCPs in team marketplaces]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-21cdcd&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-4-collaboration-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-21cdcd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->