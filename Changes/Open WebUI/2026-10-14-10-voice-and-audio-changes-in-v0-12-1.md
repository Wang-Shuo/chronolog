---
card_id: open-webui-2026-10-14-f7e822
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Voice and Audio: 10 changes in v0.12.1 — \U0001F3AD
  **Avatars in Standard voice calls.** A model's avatar now also appears in voice
  calls that…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1192
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 60a77b0a1f59a99092ac61b54d2f8a091bd1dc38a4ecb600f3de41ad6f1c60c8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-f7e822
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 10 Voice and Audio changes'
  evidence:
  - quote: "\U0001F3AD **Avatars in Standard voice calls.** A model's avatar now also
      appears in voice calls that use the Standard call mode, moves with the spoken
      reply and can play the model's gestures when the model uses native function
      calling, where avatars and gestures only worked in Realtime calls; the Voice
      avatar setting in the model editor is now shown even when Realtime is off. [Commit](https://github.com/open-webui/open-webui/commit/78613d86f7564d1927ebf5f11292419fdeadb18c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F3A0 **Turn and zoom the voice avatar.** In voice calls and in the
      model editor preview, the voice avatar can now be turned by dragging, panned
      with a right drag, Shift drag or two fingers, zoomed with the mouse wheel or
      a pinch and reset with a double click. [#32378](https://github.com/open-webui/open-webui/pull/32378)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F506 **Screen on during calls.** The screen now stays on during
      Realtime voice calls as well as Standard ones and is allowed to turn off again
      once the call ends, where Realtime calls let it go dark and Standard calls kept
      it on after closing the call. [Commit](https://github.com/open-webui/open-webui/commit/a9227421d847eb51d7c59ec336420bbb20dfbcc8),
      [#32251](https://github.com/open-webui/open-webui/issues/32251)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F39A️ **Realtime input parameters.** Administrators can now add
      extra settings for the audio input of Realtime voice calls as JSON under Input
      Parameters in the Voice calls section of Audio settings, such as noise reduction,
      or with the \"AUDIO_REALTIME_INPUT_PARAMS\" environment variable. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F513 **Skill editor and more over plain HTTP.** When Open WebUI
      is opened over plain HTTP at a network address, the skill editor, adding options
      to model controls, adding gestures to a voice avatar, Realtime voice calls and
      the Playground chat now work, where they failed with \"crypto.randomUUID is
      not a function\" and the skill editor stayed disabled. [Commit](https://github.com/open-webui/open-webui/commit/d786ed56c98e9b0fd4c8af111e1c95d4e00c7789),
      [Commit](https://github.com/open-webui/open-webui/commit/2eb77fc27f08924252d0abf5fe19182532075511),
      [#32238](https://github.com/open-webui/open-webui/issues/32238)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4F5 **No voice calls in shared chats.** The Voice mode button no
      longer shows in a shared chat you can reply in, and a call that was open closes
      when you switch to one. [Commit](https://github.com/open-webui/open-webui/commit/3a54306c50f351e5d6e89e296cb32518535712ee)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F646 **VRM 0.x avatar rest pose.** Voice avatars made in the older
      VRM 0.x format now rest with their arms down and breathe and sway the right
      way, where their arms were raised and their idle motion was mirrored. [#32270](https://github.com/open-webui/open-webui/pull/32270),
      [#32269](https://github.com/open-webui/open-webui/issues/32269)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F5E3️ **Kokoro voice in calls.** Voice calls now speak replies with
      the Kokoro.js (Browser) voice chosen in your settings when the administrator
      has no server speech engine set, where the browser's own voice was used instead.
      [Commit](https://github.com/open-webui/open-webui/commit/78613d86f7564d1927ebf5f11292419fdeadb18c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F3F7️ **Titles for voice call chats.** Chats started with a Realtime
      voice call now get a generated title and tags as soon as the chat is created,
      following the Automatic title and tag settings, where they stayed named \"New
      Chat\". [Commit](https://github.com/open-webui/open-webui/commit/8ea808850deabb4709391602417b0aa00f2857cf),
      [#32258](https://github.com/open-webui/open-webui/issues/32258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F32C️ **Background noise in Realtime calls.** Wind or background
      noise no longer cuts off the model mid-sentence in Realtime voice calls, since
      its spoken reply now only pauses until speech is confirmed and resumes after
      noise, and noise that is not understood as speech is also removed from the voice
      model's conversation so it no longer confuses later answers. [Commit](https://github.com/open-webui/open-webui/commit/a70e96525d88f9cb362b6451e5451c9b72618a92),
      [#32248](https://github.com/open-webui/open-webui/issues/32248), [#32250](https://github.com/open-webui/open-webui/issues/32250)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-voice-and-audio-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: voice
  title: 10 Voice and Audio changes in v0.12.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-12-dictation-holding-the-microphone-and-releasing-it-no-longer-stops-recording-prem|Dictation.
  Holding the microphone and releasing it no longer stops recording prematurely]]'
- '[[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude
  Tag Added support for Slack voice clips in Claude in Slack]]'
- "[[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|\U0001F4F1
  Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: voice
title: 10 Voice and Audio changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Voice and Audio changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎭 **Avatars in Standard voice calls.** A model's avatar now also appears in voice calls that use the Standard call mode, moves with the spoken reply and can play the model's gestures when the model uses native function calling, where avatars and gestures only worked in Realtime calls; the Voice avatar setting in the model editor is now shown even when Realtime is off. [Commit](https://github.com/open-webui/open-webui/commit/78613d86f7564d1927ebf5f11292419fdeadb18c)

> 🎠 **Turn and zoom the voice avatar.** In voice calls and in the model editor preview, the voice avatar can now be turned by dragging, panned with a right drag, Shift drag or two fingers, zoomed with the mouse wheel or a pinch and reset with a double click. [#32378](https://github.com/open-webui/open-webui/pull/32378)

> 🔆 **Screen on during calls.** The screen now stays on during Realtime voice calls as well as Standard ones and is allowed to turn off again once the call ends, where Realtime calls let it go dark and Standard calls kept it on after closing the call. [Commit](https://github.com/open-webui/open-webui/commit/a9227421d847eb51d7c59ec336420bbb20dfbcc8), [#32251](https://github.com/open-webui/open-webui/issues/32251)

> 🎚️ **Realtime input parameters.** Administrators can now add extra settings for the audio input of Realtime voice calls as JSON under Input Parameters in the Voice calls section of Audio settings, such as noise reduction, or with the "AUDIO_REALTIME_INPUT_PARAMS" environment variable. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b)

> 🔓 **Skill editor and more over plain HTTP.** When Open WebUI is opened over plain HTTP at a network address, the skill editor, adding options to model controls, adding gestures to a voice avatar, Realtime voice calls and the Playground chat now work, where they failed with "crypto.randomUUID is not a function" and the skill editor stayed disabled. [Commit](https://github.com/open-webui/open-webui/commit/d786ed56c98e9b0fd4c8af111e1c95d4e00c7789), [Commit](https://github.com/open-webui/open-webui/commit/2eb77fc27f08924252d0abf5fe19182532075511), [#32238](https://github.com/open-webui/open-webui/issues/32238)

> 📵 **No voice calls in shared chats.** The Voice mode button no longer shows in a shared chat you can reply in, and a call that was open closes when you switch to one. [Commit](https://github.com/open-webui/open-webui/commit/3a54306c50f351e5d6e89e296cb32518535712ee)

> 🙆 **VRM 0.x avatar rest pose.** Voice avatars made in the older VRM 0.x format now rest with their arms down and breathe and sway the right way, where their arms were raised and their idle motion was mirrored. [#32270](https://github.com/open-webui/open-webui/pull/32270), [#32269](https://github.com/open-webui/open-webui/issues/32269)

> 🗣️ **Kokoro voice in calls.** Voice calls now speak replies with the Kokoro.js (Browser) voice chosen in your settings when the administrator has no server speech engine set, where the browser's own voice was used instead. [Commit](https://github.com/open-webui/open-webui/commit/78613d86f7564d1927ebf5f11292419fdeadb18c)

> 🏷️ **Titles for voice call chats.** Chats started with a Realtime voice call now get a generated title and tags as soon as the chat is created, following the Automatic title and tag settings, where they stayed named "New Chat". [Commit](https://github.com/open-webui/open-webui/commit/8ea808850deabb4709391602417b0aa00f2857cf), [#32258](https://github.com/open-webui/open-webui/issues/32258)

> 🌬️ **Background noise in Realtime calls.** Wind or background noise no longer cuts off the model mid-sentence in Realtime voice calls, since its spoken reply now only pauses until speech is confirmed and resumes after noise, and noise that is not understood as speech is also removed from the voice model's conversation so it no longer confuses later answers. [Commit](https://github.com/open-webui/open-webui/commit/a70e96525d88f9cb362b6451e5451c9b72618a92), [#32248](https://github.com/open-webui/open-webui/issues/32248), [#32250](https://github.com/open-webui/open-webui/issues/32250)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-2-context-window-changes-in-v0-12-1|2 Context Window changes in v0.12.1]] · Context Window
- [[Changes/Open WebUI/2026-10-14-3-account-and-access-changes-in-v0-12-1|3 Account and Access changes in v0.12.1]] · Account and Access
- [[Changes/Open WebUI/2026-10-14-save-hidden-on-others-messages-in-a-chat-shared-with-allow-replies-editing-a-mes|💾 Save hidden on others' messages. In a chat shared with Allow replies, editing…]] · Collaboration
- [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]] · Model Support
- [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|📱 Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]]
- Later: 2026-10-14 · Runway · [[Changes/Runway/2026-10-14-fish-audio-drama-3-is-now-available-in-runway-mcp-turn-scripts-into-expressive-v|Fish Audio Drama 3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-f7e822&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-10-voice-and-audio-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-f7e822%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->