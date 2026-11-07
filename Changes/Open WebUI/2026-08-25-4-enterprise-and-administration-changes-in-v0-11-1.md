---
card_id: open-webui-2026-08-25-cc13df
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Enterprise and Administration: 4 changes in
  v0.11.1 — \U0001F4EF **Group changes from single sign-on.** Group memberships added
  or removed…"
diffusion:
  first_in_tracked: '[[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access
    for Google Workspace accounts]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 07c63d1995a64d974223cf4ba8bed94e27ea3ee7ce025712fd3ca6772f0d58cc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-cc13df
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 4 Enterprise and Administration changes'
  evidence:
  - quote: "\U0001F4EF **Group changes from single sign-on.** Group memberships added
      or removed when someone signs in through an identity provider, and groups created
      automatically along the way, now raise the same events as the equivalent change
      made by an administrator or over directory sync. [#27657](https://github.com/open-webui/open-webui/pull/27657)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⛓ **Deleting one knowledge base removing a shared connection.** Deleting
      an external knowledge base now leaves its connection in place while other knowledge
      bases still use it, and only an administrator removing the last one clears it,
      where any user deleting theirs took the connection away from everyone. [#28113](https://github.com/open-webui/open-webui/pull/28113)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F648 **Needless request from the model picker.** Opening the model
      picker as a non-administrator no longer fires a request to an administrator-only
      settings endpoint that was always refused. [Commit](https://github.com/open-webui/open-webui/commit/b4738d1a2e6af1ce20adb322fc6d2aa2c9407901)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3F7 **Tags on a chat shared with you.** Opening a chat shared with
      you, or one in a shared folder, no longer fails to load its tags, and an administrator
      opening someone else's chat now sees the tags that chat actually carries. [Commit](https://github.com/open-webui/open-webui/commit/7d4747dfd73d7629227b10ae63c6854cc7543bee),
      [#28767](https://github.com/open-webui/open-webui/issues/28767)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-enterprise-and-administration-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: enterprise-admin
  title: 4 Enterprise and Administration changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Runway/2026-08-24-org-admins-can-now-set-a-default-sso-configuration-that-automatically-applies-to|Default
  SSO for New Workspaces]]'
- '[[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise
  and Administration changes in 1.17.0]]'
- '[[Changes/Lovable/2026-08-25-only-free-and-pro-projects-are-eligible-for-linkedin-skills|Only
  Free and Pro projects are eligible for LinkedIn skills]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: enterprise-admin
title: 4 Enterprise and Administration changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Enterprise and Administration changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📯 **Group changes from single sign-on.** Group memberships added or removed when someone signs in through an identity provider, and groups created automatically along the way, now raise the same events as the equivalent change made by an administrator or over directory sync. [#27657](https://github.com/open-webui/open-webui/pull/27657)

> ⛓ **Deleting one knowledge base removing a shared connection.** Deleting an external knowledge base now leaves its connection in place while other knowledge bases still use it, and only an administrator removing the last one clears it, where any user deleting theirs took the connection away from everyone. [#28113](https://github.com/open-webui/open-webui/pull/28113)

> 🙈 **Needless request from the model picker.** Opening the model picker as a non-administrator no longer fires a request to an administrator-only settings endpoint that was always refused. [Commit](https://github.com/open-webui/open-webui/commit/b4738d1a2e6af1ce20adb322fc6d2aa2c9407901)

> 🏷 **Tags on a chat shared with you.** Opening a chat shared with you, or one in a shared folder, no longer fails to load its tags, and an administrator opening someone else's chat now sees the tags that chat actually carries. [Commit](https://github.com/open-webui/open-webui/commit/7d4747dfd73d7629227b10ae63c6854cc7543bee), [#28767](https://github.com/open-webui/open-webui/issues/28767)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-08-25 · Lovable · [[Changes/Lovable/2026-08-25-only-free-and-pro-projects-are-eligible-for-linkedin-skills|Only Free and Pro projects are eligible for LinkedIn skills]]
- Later: 2026-08-26 · Lovable · [[Changes/Lovable/2026-08-26-record-who-is-behind-each-commit-lovable-pushes|Record who is behind each commit Lovable pushes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-05 · Gemini · [[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access for Google Workspace accounts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-cc13df&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-cc13df%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->