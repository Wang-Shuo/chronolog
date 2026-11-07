---
card_id: open-webui-2026-08-25-bb243e
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Editor Experience: 12 changes in v0.11.1 —
  \U0001F4A4 **Far fewer writes just from being signed in.** Recording that someone
  is online now…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1260
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1271c1daf8cf7f3fdadddfff54149083c7614108ce2ea66645c5e248d090049a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-bb243e
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 12 Editor Experience changes'
  evidence:
  - quote: "\U0001F4A4 **Far fewer writes just from being signed in.** Recording that
      someone is online now writes at most once a minute for each person rather than
      on every single request, where an open tab alone caused two write transactions
      a minute before anyone touched anything. [#28177](https://github.com/open-webui/open-webui/pull/28177),
      [#28165](https://github.com/open-webui/open-webui/issues/28165)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ☑️ **Checkboxes beside their labels.** In the model editor and the admin
      model defaults, each capability, feature, and tool checkbox now sits directly
      in front of its own label instead of at the far edge of its column, where it
      could look like it belonged to the next one, and the label itself can be clicked
      to toggle it. [#27788](https://github.com/open-webui/open-webui/pull/27788),
      [#27771](https://github.com/open-webui/open-webui/issues/27771), [Commit](https://github.com/open-webui/open-webui/commit/1b39ff352a2fa3b57bd7815f44c50daf96937a14),
      [Commit](https://github.com/open-webui/open-webui/commit/0f821398ca9c9ddd8da521b5f9dcf103030202e8)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✒️ **Underlined text.** Underlined text now appears underlined in a reply
      instead of showing the markup around it, and underlining is kept when you edit
      in a rich text box rather than being dropped. [Commit](https://github.com/open-webui/open-webui/commit/11db926a7b471e9477595786ef451a916174cc18),
      [#26904](https://github.com/open-webui/open-webui/issues/26904)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F493 **Tunable heartbeat for live updates.** A new \"WEBSOCKET_HEARTBEAT_INTERVAL\"
      setting controls how often each open tab checks in with the server, where it
      was fixed at 30 seconds, so a large deployment can cut background traffic that
      no one asked for. [Commit](https://github.com/open-webui/open-webui/commit/3c1017f6c3ffc7194f074f2cfd2ea5f49943c575),
      [#28166](https://github.com/open-webui/open-webui/issues/28166)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⏳ **Analytics stuck loading.** Choosing a custom date range in analytics
      without picking dates yet no longer leaves the tab spinning forever, including
      after leaving and coming back to it. [#28125](https://github.com/open-webui/open-webui/issues/28125),
      [Commit](https://github.com/open-webui/open-webui/commit/629cdcb5303958c5b99ee437030ab80cc418bc2e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F516 **Skill identifiers that cannot be reached.** Creating a skill
      whose identifier contains a character that is not allowed in a web address is
      now refused outright, rather than accepted and then permanently impossible to
      open, edit, turn off, delete, or recreate. [#27660](https://github.com/open-webui/open-webui/pull/27660),
      [#27655](https://github.com/open-webui/open-webui/issues/27655)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F532 **Removing an item in the model editor.** Unticking a tool,
      skill, action, or filter no longer leaves the next one in the list looking unticked
      while it is still selected, needing two clicks to remove and passing the same
      confusion down the list each time. [#28837](https://github.com/open-webui/open-webui/pull/28837),
      [#28832](https://github.com/open-webui/open-webui/issues/28832)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5D2 **Editing a workflow from settings.** Opening the code editor
      for a ComfyUI workflow from the images settings now brings it to the front,
      where it opened behind the settings dialog and could not be reached at all.
      [#27648](https://github.com/open-webui/open-webui/pull/27648), [#27647](https://github.com/open-webui/open-webui/issues/27647)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FABA **Workspace counts left behind.** The number beside each workspace
      tab now follows its list, where creating, copying, importing, or deleting something
      left the old number in place until you moved to another tab or reloaded, and
      the tools count ignored its search entirely. [#28983](https://github.com/open-webui/open-webui/pull/28983),
      [#28981](https://github.com/open-webui/open-webui/issues/28981)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✒ **Note edits lost without warning.** Typing in a note now reaches the
      database, where a save already waiting could be cancelled without a replacement,
      leaving the editor showing text that was never stored and nothing to say so;
      this affected notes written by a model or through the API, and any instance
      without Redis after a restart. [#28669](https://github.com/open-webui/open-webui/pull/28669),
      [#28667](https://github.com/open-webui/open-webui/issues/28667)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⏱️ **Unanswered prompts in tools.** On deployments that set "WEBSOCKET_EVENT_CALLER_TIMEOUT",
      a question a tool asks you that goes unanswered now reports a timeout rather
      than an empty reply, and waiting too long no longer risks disconnecting a tab
      that is still open. [#28311](https://github.com/open-webui/open-webui/pull/28311)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39F️ **Connections whose tags were saved as plain text.** A connection
      with tags stored as plain text no longer breaks its editor panel or silently
      blanks the tags on every model coming from it. [Commit](https://github.com/open-webui/open-webui/commit/8be4c5fa6a849a9ff4a74f6a2870a115a836e68a),
      [#28749](https://github.com/open-webui/open-webui/issues/28749)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-editor-experience-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: editor-experience
  title: 12 Editor Experience changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-08-24-elevenlabs-cli|ElevenLabs CLI]]'
- '[[Changes/Claude Code/2026-08-25-added-the-turn-s-completion-time-to-the-end-of-turn-duration-line-e-g-saut-ed-fo|Added
  the turn''s completion time to the end-of-turn duration line…]]'
- '[[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience
  changes in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: editor-experience
title: 12 Editor Experience changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Editor Experience changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💤 **Far fewer writes just from being signed in.** Recording that someone is online now writes at most once a minute for each person rather than on every single request, where an open tab alone caused two write transactions a minute before anyone touched anything. [#28177](https://github.com/open-webui/open-webui/pull/28177), [#28165](https://github.com/open-webui/open-webui/issues/28165)

> ☑️ **Checkboxes beside their labels.** In the model editor and the admin model defaults, each capability, feature, and tool checkbox now sits directly in front of its own label instead of at the far edge of its column, where it could look like it belonged to the next one, and the label itself can be clicked to toggle it. [#27788](https://github.com/open-webui/open-webui/pull/27788), [#27771](https://github.com/open-webui/open-webui/issues/27771), [Commit](https://github.com/open-webui/open-webui/commit/1b39ff352a2fa3b57bd7815f44c50daf96937a14), [Commit](https://github.com/open-webui/open-webui/commit/0f821398ca9c9ddd8da521b5f9dcf103030202e8)

> ✒️ **Underlined text.** Underlined text now appears underlined in a reply instead of showing the markup around it, and underlining is kept when you edit in a rich text box rather than being dropped. [Commit](https://github.com/open-webui/open-webui/commit/11db926a7b471e9477595786ef451a916174cc18), [#26904](https://github.com/open-webui/open-webui/issues/26904)

> 💓 **Tunable heartbeat for live updates.** A new "WEBSOCKET_HEARTBEAT_INTERVAL" setting controls how often each open tab checks in with the server, where it was fixed at 30 seconds, so a large deployment can cut background traffic that no one asked for. [Commit](https://github.com/open-webui/open-webui/commit/3c1017f6c3ffc7194f074f2cfd2ea5f49943c575), [#28166](https://github.com/open-webui/open-webui/issues/28166)

> ⏳ **Analytics stuck loading.** Choosing a custom date range in analytics without picking dates yet no longer leaves the tab spinning forever, including after leaving and coming back to it. [#28125](https://github.com/open-webui/open-webui/issues/28125), [Commit](https://github.com/open-webui/open-webui/commit/629cdcb5303958c5b99ee437030ab80cc418bc2e)

> 🔖 **Skill identifiers that cannot be reached.** Creating a skill whose identifier contains a character that is not allowed in a web address is now refused outright, rather than accepted and then permanently impossible to open, edit, turn off, delete, or recreate. [#27660](https://github.com/open-webui/open-webui/pull/27660), [#27655](https://github.com/open-webui/open-webui/issues/27655)

> 🔲 **Removing an item in the model editor.** Unticking a tool, skill, action, or filter no longer leaves the next one in the list looking unticked while it is still selected, needing two clicks to remove and passing the same confusion down the list each time. [#28837](https://github.com/open-webui/open-webui/pull/28837), [#28832](https://github.com/open-webui/open-webui/issues/28832)

> 🗒 **Editing a workflow from settings.** Opening the code editor for a ComfyUI workflow from the images settings now brings it to the front, where it opened behind the settings dialog and could not be reached at all. [#27648](https://github.com/open-webui/open-webui/pull/27648), [#27647](https://github.com/open-webui/open-webui/issues/27647)

> 🪺 **Workspace counts left behind.** The number beside each workspace tab now follows its list, where creating, copying, importing, or deleting something left the old number in place until you moved to another tab or reloaded, and the tools count ignored its search entirely. [#28983](https://github.com/open-webui/open-webui/pull/28983), [#28981](https://github.com/open-webui/open-webui/issues/28981)

> ✒ **Note edits lost without warning.** Typing in a note now reaches the database, where a save already waiting could be cancelled without a replacement, leaving the editor showing text that was never stored and nothing to say so; this affected notes written by a model or through the API, and any instance without Redis after a restart. [#28669](https://github.com/open-webui/open-webui/pull/28669), [#28667](https://github.com/open-webui/open-webui/issues/28667)

> ⏱️ **Unanswered prompts in tools.** On deployments that set "WEBSOCKET_EVENT_CALLER_TIMEOUT", a question a tool asks you that goes unanswered now reports a timeout rather than an empty reply, and waiting too long no longer risks disconnecting a tab that is still open. [#28311](https://github.com/open-webui/open-webui/pull/28311)

> 🎟️ **Connections whose tags were saved as plain text.** A connection with tags stored as plain text no longer breaks its editor panel or silently blanks the tags on every model coming from it. [Commit](https://github.com/open-webui/open-webui/commit/8be4c5fa6a849a9ff4a74f6a2870a115a836e68a), [#28749](https://github.com/open-webui/open-webui/issues/28749)

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
## Nearby in Editor Experience

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]]
- Later: 2026-08-27 · Cursor · [[Changes/Cursor/2026-08-27-once-the-agent-s-build-is-to-your-liking-click-the-create-repo-button-to-save-yo|Turn it into a real repo, whenever you want]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-bb243e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-12-editor-experience-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-bb243e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->