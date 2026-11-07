---
card_id: open-webui-2026-10-10-ad52e0
date: '2026-10-10'
description: 'Open WebUI · 2026-10-10 · Safety and Privacy: 6 changes in v0.12.0 —
  ☎️ **Realtime voice calls.** Administrators can now switch Call mode in the Voice
  calls…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3329c4d269385f80d3dc64bd63746b8405be16213582a711e5ec9e54937990d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-ad52e0
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 6 Safety and Privacy changes'
  evidence:
  - quote: ☎️ **Realtime voice calls.** Administrators can now switch Call mode in
      the Voice calls section of Audio settings from Standard to Realtime, so Voice
      mode talks through an OpenAI Realtime voice model (gpt-realtime-2.1-mini with
      the Marin voice by default) that handles small talk itself and hands real questions
      and tasks to the chat's selected model, with its conversation history and tools,
      before speaking the answer while the full reply appears in the chat. Approvals
      and questions from tools still have to be answered in the chat, calls need the
      Allow Call permission and end after an hour, models can set their own Realtime
      Voice in the model editor, and the settings can also be given with the "AUDIO_REALTIME_ENABLED",
      "AUDIO_REALTIME_OPENAI_API_BASE_URL", "AUDIO_REALTIME_OPENAI_API_KEY", "AUDIO_REALTIME_MODEL",
      "AUDIO_REALTIME_VOICE", "AUDIO_REALTIME_TRANSCRIPTION_MODEL" and "REALTIME_CALL_PROMPT_TEMPLATE"
      environment variables. [Commit](https://github.com/open-webui/open-webui/commit/093bfce2b6bd128731bae8075110898ae22a76e9),
      [Commit](https://github.com/open-webui/open-webui/commit/fa4c7fe5e8b5a26bcb9e4597d311a6b16aaf796a),
      [#5894](https://github.com/open-webui/open-webui/issues/5894)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section. Some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E1 **Channels permission for live messages and automations.**
      Users without the Channels permission no longer receive live channel messages,
      and an automation that posts into a channel no longer runs once its creator
      has lost that permission. [#31578](https://github.com/open-webui/open-webui/pull/31578),
      [#31577](https://github.com/open-webui/open-webui/pull/31577)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4DD **Notes permission for live note editing.** Opening a note
      for live collaborative editing now requires the Notes permission, like the rest
      of the Notes feature. [#31552](https://github.com/open-webui/open-webui/pull/31552)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4DE **Voice mode permission applies to call links.** Opening a
      chat with \"?call=true\" in the URL now respects the \"Allow Call\" permission
      and the same checks as the Voice mode button, so it no longer starts a voice
      call for users without that permission, with several models selected or with
      the Web API speech-to-text engine. [#31826](https://github.com/open-webui/open-webui/pull/31826),
      [#31825](https://github.com/open-webui/open-webui/issues/31825)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5D2️ **Notes switch applies to the notes API.** Turning Notes off
      with \"ENABLE_NOTES\" or in Admin Settings now also refuses every notes API
      request, where it only hid notes in the interface and anyone with the notes
      permission could still create, read, change and delete notes through the API.
      [Commit](https://github.com/open-webui/open-webui/commit/83acd08697d2985e3da03b20e3c8119c958d32d7),
      [#31414](https://github.com/open-webui/open-webui/issues/31414)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-safety-and-privacy-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.12.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows
  MXC sandbox]]'
- '[[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety
  and Privacy changes in v2.1.296]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-copilot-config-supports-sandbox-credential-injecthosts-keys-with-key-completion|copilot
  config supports sandbox credential injectHosts keys, with key completion…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ☎️ **Realtime voice calls.** Administrators can now switch Call mode in the Voice calls section of Audio settings from Standard to Realtime, so Voice mode talks through an OpenAI Realtime voice model (gpt-realtime-2.1-mini with the Marin voice by default) that handles small talk itself and hands real questions and tasks to the chat's selected model, with its conversation history and tools, before speaking the answer while the full reply appears in the chat. Approvals and questions from tools still have to be answered in the chat, calls need the Allow Call permission and end after an hour, models can set their own Realtime Voice in the model editor, and the settings can also be given with the "AUDIO_REALTIME_ENABLED", "AUDIO_REALTIME_OPENAI_API_BASE_URL", "AUDIO_REALTIME_OPENAI_API_KEY", "AUDIO_REALTIME_MODEL", "AUDIO_REALTIME_VOICE", "AUDIO_REALTIME_TRANSCRIPTION_MODEL" and "REALTIME_CALL_PROMPT_TEMPLATE" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/093bfce2b6bd128731bae8075110898ae22a76e9), [Commit](https://github.com/open-webui/open-webui/commit/fa4c7fe5e8b5a26bcb9e4597d311a6b16aaf796a), [#5894](https://github.com/open-webui/open-webui/issues/5894)

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section. Some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 📡 **Channels permission for live messages and automations.** Users without the Channels permission no longer receive live channel messages, and an automation that posts into a channel no longer runs once its creator has lost that permission. [#31578](https://github.com/open-webui/open-webui/pull/31578), [#31577](https://github.com/open-webui/open-webui/pull/31577)

> 📝 **Notes permission for live note editing.** Opening a note for live collaborative editing now requires the Notes permission, like the rest of the Notes feature. [#31552](https://github.com/open-webui/open-webui/pull/31552)

> 📞 **Voice mode permission applies to call links.** Opening a chat with "?call=true" in the URL now respects the "Allow Call" permission and the same checks as the Voice mode button, so it no longer starts a voice call for users without that permission, with several models selected or with the Web API speech-to-text engine. [#31826](https://github.com/open-webui/open-webui/pull/31826), [#31825](https://github.com/open-webui/open-webui/issues/31825)

> 🗒️ **Notes switch applies to the notes API.** Turning Notes off with "ENABLE_NOTES" or in Admin Settings now also refuses every notes API request, where it only hid notes in the interface and anyone with the notes permission could still create, read, change and delete notes through the API. [Commit](https://github.com/open-webui/open-webui/commit/83acd08697d2985e3da03b20e3c8119c958d32d7), [#31414](https://github.com/open-webui/open-webui/issues/31414)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-09-copilot-config-supports-sandbox-credential-injecthosts-keys-with-key-completion|copilot config supports sandbox credential injectHosts keys, with key completion…]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-ad52e0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-6-safety-and-privacy-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-ad52e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->