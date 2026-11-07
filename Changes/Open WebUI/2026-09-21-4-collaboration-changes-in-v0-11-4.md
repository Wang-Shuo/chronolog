---
card_id: open-webui-2026-09-21-375538
date: '2026-09-21'
description: 'Open WebUI · 2026-09-21 · Collaboration: 4 changes in v0.11.4 — ✴️ **Lighter
  shared note editing.** Notes written by several people at once no longer echo…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2810
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1fb65c4cf502132e26c10f0a1463ce2981019cd190a6b4bf0270cab172da5c13
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-375538
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 4 Collaboration changes'
  evidence:
  - quote: ✴️ **Lighter shared note editing.** Notes written by several people at
      once no longer echo every keystroke back to the server once per watcher; the
      traffic between editors falls by half with two of them and keeps falling as
      more join, so shared notes stay smooth as the room grows. [#28185](https://github.com/open-webui/open-webui/pull/28185)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F91D **Note sharing survives a save.** Saving a note you had been
      given access to took that sharing away, so the note went private and everyone
      else lost it. [#30175](https://github.com/open-webui/open-webui/pull/30175)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6D1 **Complete chat stop.** Where a chat had more than one task
      in flight, stopping it, deleting it, or closing a note being worked on could
      stop the first and leave the rest running to the end, both because a task that
      had already finished ended the round early and because the list being worked
      through was rewritten underneath it as each one was cleared away; every task
      is now stopped in turn, so a reply that was calling tools stops calling them
      rather than running on to its own limit, though instances sharing their state
      through Redis were not affected. [Commit](https://github.com/open-webui/open-webui/commit/e35b907f737e625b900b3a03d61890f67ab0c4b0),
      [#29844](https://github.com/open-webui/open-webui/pull/29844), [#29816](https://github.com/open-webui/open-webui/issues/29816)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F52D **Knowledge base search recall.** Where many knowledge bases
      are stored together, a search of one holding a small share of what is stored
      found only a small share of its matches, and the shortfall grew as the store
      did; the search now keeps looking until it has enough from the knowledge base
      you asked for, and \"PGVECTOR_ITERATIVE_SCAN\" switches that off or makes it
      strict. [#30142](https://github.com/open-webui/open-webui/pull/30142), [#30135](https://github.com/open-webui/open-webui/issues/30135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-collaboration-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: collaboration
  title: 4 Collaboration changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Descript/2026-09-17-captions-redesigned|Captions, redesigned]]'
- '[[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed
  /ultrareview in non-interactive sessions to refuse when the repository has…]]'
- '[[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration
  changes in v2026.9.5]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: collaboration
title: 4 Collaboration changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Collaboration changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✴️ **Lighter shared note editing.** Notes written by several people at once no longer echo every keystroke back to the server once per watcher; the traffic between editors falls by half with two of them and keeps falling as more join, so shared notes stay smooth as the room grows. [#28185](https://github.com/open-webui/open-webui/pull/28185)

> 🤝 **Note sharing survives a save.** Saving a note you had been given access to took that sharing away, so the note went private and everyone else lost it. [#30175](https://github.com/open-webui/open-webui/pull/30175)

> 🛑 **Complete chat stop.** Where a chat had more than one task in flight, stopping it, deleting it, or closing a note being worked on could stop the first and leave the rest running to the end, both because a task that had already finished ended the round early and because the list being worked through was rewritten underneath it as each one was cleared away; every task is now stopped in turn, so a reply that was calling tools stops calling them rather than running on to its own limit, though instances sharing their state through Redis were not affected. [Commit](https://github.com/open-webui/open-webui/commit/e35b907f737e625b900b3a03d61890f67ab0c4b0), [#29844](https://github.com/open-webui/open-webui/pull/29844), [#29816](https://github.com/open-webui/open-webui/issues/29816)

> 🔭 **Knowledge base search recall.** Where many knowledge bases are stored together, a search of one holding a small share of what is stored found only a small share of its matches, and the shortfall grew as the store did; the search now keeps looking until it has enough from the knowledge base you asked for, and "PGVECTOR_ITERATIVE_SCAN" switches that off or makes it strict. [#30142](https://github.com/open-webui/open-webui/pull/30142), [#30135](https://github.com/open-webui/open-webui/issues/30135)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-19 · OpenClaw · [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-375538&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-4-collaboration-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-375538%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->