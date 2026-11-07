---
card_id: open-webui-2026-08-25-1bc92c
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Safety and Privacy: 7 changes in v0.11.1 —
  \U0001F4C7 **Faster permission checks on large instances.** Working out which groups
  you belong to…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e9379bd2b8e456ef8ed1584e57a9d43b0a5836cb019ff138d61b9bd14ca6e6ef
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-1bc92c
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 7 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F4C7 **Faster permission checks on large instances.** Working out
      which groups you belong to is now a direct lookup rather than a scan of every
      membership on the server, so chats and the admin user list stay quick as an
      organization grows. [#27822](https://github.com/open-webui/open-webui/pull/27822)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6F0 **Less overhead on every request.** The layers each request
      passes through before it is handled are now one instead of five, which also
      removes a quarter of that cost from every piece of a streamed reply on instances
      that set security headers. [Commit](https://github.com/open-webui/open-webui/commit/b96d2b12dae5e953e520bec03f74e9b85b955dc7),
      [#28171](https://github.com/open-webui/open-webui/issues/28171)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section. Some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6D1 **Memory permission being respected.** Taking away someone's
      memory permission now also stops their stored memories being added to the context
      of their conversations, which one path had continued doing regardless. [#27668](https://github.com/open-webui/open-webui/pull/27668)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⚖️ **Sharing defaults matching what was configured.** On instances upgraded
      from older versions, public sharing of tools and notes no longer shows as switched
      on in the admin panel, and saving any unrelated permission no longer grants
      everyone a capability that was never enabled. [#27716](https://github.com/open-webui/open-webui/pull/27716),
      [#27715](https://github.com/open-webui/open-webui/issues/27715)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F374 **Fork offered only when allowed.** The fork action and the
      fork command no longer appear for people whose chat import permission is turned
      off, where using them produced an access denied error. [#27711](https://github.com/open-webui/open-webui/pull/27711),
      [#27692](https://github.com/open-webui/open-webui/issues/27692)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F513 **Turning on open sharing.** The open sharing permission can
      now be switched on in the default user permissions, where saving appeared to
      work but the setting was discarded and came back off. [#27609](https://github.com/open-webui/open-webui/pull/27609),
      [#27607](https://github.com/open-webui/open-webui/issues/27607)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-safety-and-privacy-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety
  and Privacy changes in v2.1.246]]'
- '[[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and
  Privacy changes in 1.17.0]]'
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR
  Agent Issue Fix (26120): Clarify privacy notice wording and selection options]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📇 **Faster permission checks on large instances.** Working out which groups you belong to is now a direct lookup rather than a scan of every membership on the server, so chats and the admin user list stay quick as an organization grows. [#27822](https://github.com/open-webui/open-webui/pull/27822)

> 🛰 **Less overhead on every request.** The layers each request passes through before it is handled are now one instead of five, which also removes a quarter of that cost from every piece of a streamed reply on instances that set security headers. [Commit](https://github.com/open-webui/open-webui/commit/b96d2b12dae5e953e520bec03f74e9b85b955dc7), [#28171](https://github.com/open-webui/open-webui/issues/28171)

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section. Some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 🛑 **Memory permission being respected.** Taking away someone's memory permission now also stops their stored memories being added to the context of their conversations, which one path had continued doing regardless. [#27668](https://github.com/open-webui/open-webui/pull/27668)

> ⚖️ **Sharing defaults matching what was configured.** On instances upgraded from older versions, public sharing of tools and notes no longer shows as switched on in the admin panel, and saving any unrelated permission no longer grants everyone a capability that was never enabled. [#27716](https://github.com/open-webui/open-webui/pull/27716), [#27715](https://github.com/open-webui/open-webui/issues/27715)

> 🍴 **Fork offered only when allowed.** The fork action and the fork command no longer appear for people whose chat import permission is turned off, where using them produced an access denied error. [#27711](https://github.com/open-webui/open-webui/pull/27711), [#27692](https://github.com/open-webui/open-webui/issues/27692)

> 🔓 **Turning on open sharing.** The open sharing permission can now be switched on in the default user permissions, where saving appeared to work but the setting was discarded and came back off. [#27609](https://github.com/open-webui/open-webui/pull/27609), [#27607](https://github.com/open-webui/open-webui/issues/27607)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
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
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR Agent Issue Fix (26120): Clarify privacy notice wording and selection options]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-1bc92c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-7-safety-and-privacy-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-1bc92c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->