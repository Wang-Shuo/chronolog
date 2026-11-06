---
card_id: open-webui-2026-10-10-2c3b1e
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Voice and Audio: 12 changes in v0.12.0 — \U0001F57A
  **Animated avatars in Realtime voice calls.** A model can now show a 3D character
  instead…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1188
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39bf4f2da63786f6bf1e2b284a55b9ec6ed63a6b9e43c67cb6210c44c7bc6517
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-2c3b1e
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 12 Voice and Audio changes'
  evidence:
  - quote: "\U0001F57A **Animated avatars in Realtime voice calls.** A model can now
      show a 3D character instead of the voice orb during Realtime calls: in the model
      editor, upload a rigged VRM avatar of up to 25 MiB, preview it, optionally give
      it VRMA clips of up to 10 MiB for its idle, listening and speaking states, and
      add up to 16 named gestures with a description, which the voice model plays
      on its own when the conversation fits or when asked, such as a wave or a clap,
      while the avatar's mouth follows the spoken answer. [Commit](https://github.com/open-webui/open-webui/commit/7401f41630e53999afd6c4efba06816e7c05cdb7),
      [Commit](https://github.com/open-webui/open-webui/commit/e56f85f43260ed528bdf20a8afa635a963b84b78)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4FB **OpenAI Realtime models for text-to-speech.** Administrators
      can now pick OpenAI Realtime as the text-to-speech engine in Audio settings,
      which uses the gpt-realtime-2.1 or gpt-realtime-2.1-mini model with voices such
      as Marin and Cedar only to turn text into a finished audio clip rather than
      for a live voice conversation, and the instructions that keep it reading text
      aloud word for word can be replaced under Prompt Template or with the \"REALTIME_TTS_PROMPT_TEMPLATE\"
      environment variable. [Commit](https://github.com/open-webui/open-webui/commit/b8738494cfab53f7e3f3849e8856c26263bd45fa),
      [Commit](https://github.com/open-webui/open-webui/commit/b0bcd945199c3b6884ef6526fb4edd6636cd06ba)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A3 **Links no longer act on your behalf without asking.** Opening
      Open WebUI from a link, including from another website or a hidden frame, can
      no longer act in your name unseen: a prompt given with \"?q=\" is only filled
      into the message box instead of being sent, loading web pages or videos with
      \"load-url\" or \"youtube\" and starting a voice call with \"call=true\" or
      \"voice=true\" now ask for confirmation first, and links that create a note
      with a title and content now ask before creating it. [Commit](https://github.com/open-webui/open-webui/commit/91853205e817b0234fb3038f06cddf669ec7d335),
      [Commit](https://github.com/open-webui/open-webui/commit/0ffd86967fd2e5a537f69934b13c899b7f5c6f32)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4BD **Leaner storage of MCP media.** Images and audio returned
      by MCP tools are no longer saved a second time inside the database, which kept
      growing it with every such result. [#30419](https://github.com/open-webui/open-webui/pull/30419),
      [#30411](https://github.com/open-webui/open-webui/issues/30411)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F399️ **Voice calls recover from speech failures.** When the text-to-speech
      provider fails during a voice call, the call now shows the provider's error
      once and goes back to listening, where it previously hung in \"speaking\" with
      no sound until tapped. [#30372](https://github.com/open-webui/open-webui/pull/30372),
      [#30052](https://github.com/open-webui/open-webui/issues/30052)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A7 **Read Aloud on iPhone and iPad.** Replies read aloud automatically
      and voice calls now play sound on iOS and iPadOS, and a failed playback returns
      the speaker button to idle with an error message, where it previously stayed
      stuck in \"speaking\". [#30373](https://github.com/open-webui/open-webui/pull/30373),
      [#30262](https://github.com/open-webui/open-webui/issues/30262)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A4 **Voice mode stops when leaving the chat.** Leaving a chat
      with voice mode active, for example to open the workspace or notes, now turns
      the microphone off, where it previously kept listening and sending what you
      said as prompts. [#30417](https://github.com/open-webui/open-webui/pull/30417),
      [#30405](https://github.com/open-webui/open-webui/issues/30405)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F507 **Mute shortcut during voice calls.** Pressing M during a voice
      call mutes the microphone after every turn again, where it previously typed
      an \"m\" into the chat box. [#30421](https://github.com/open-webui/open-webui/pull/30421),
      [#30406](https://github.com/open-webui/open-webui/issues/30406)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F50A **Kokoro voice in Voice Mode from links and shortcuts.** Voice
      Mode opened with \"?call=true\" or a desktop shortcut now speaks replies when
      the speech engine is Kokoro.js (Browser), where only opening it with the Voice
      mode button set up the voice. [#31829](https://github.com/open-webui/open-webui/pull/31829),
      [#31828](https://github.com/open-webui/open-webui/issues/31828)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A4 **Web API dictation keeps listening.** With the Web API speech-to-text
      engine, dictation now only stops after two seconds of silence, where it could
      stop mid-sentence after a short pause. [#31891](https://github.com/open-webui/open-webui/pull/31891),
      [#19727](https://github.com/open-webui/open-webui/issues/19727)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F507 **Interrupting Voice mode stops the reply.** Interrupting Voice
      mode while it speaks now stops the rest of the reply instead of reading out
      the sentences that were already queued. [#31877](https://github.com/open-webui/open-webui/pull/31877),
      [#31876](https://github.com/open-webui/open-webui/issues/31876)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F508 **Read Aloud after a Voice mode call.** Read Aloud now plays
      with sound after a Voice mode call has ended, where it stayed muted until the
      chat was closed and opened again. [#31875](https://github.com/open-webui/open-webui/pull/31875),
      [#31874](https://github.com/open-webui/open-webui/issues/31874)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-voice-and-audio-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: voice
  title: 12 Voice and Audio changes in v0.12.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-06-feat-chat-add-optional-voice-dictation-to-the-chat-input-by-vascosch92-in-https|feat(chat):
  add optional voice dictation to the chat input]]'
- '[[Changes/Codex CLI/2026-10-07-4-voice-and-audio-changes-in-rust-v0-161-0|4 Voice
  and Audio changes in rust-v0.161.0]]'
- '[[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice
  and Audio changes in rust-v0.162.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: voice
title: 12 Voice and Audio changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Voice and Audio changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🕺 **Animated avatars in Realtime voice calls.** A model can now show a 3D character instead of the voice orb during Realtime calls: in the model editor, upload a rigged VRM avatar of up to 25 MiB, preview it, optionally give it VRMA clips of up to 10 MiB for its idle, listening and speaking states, and add up to 16 named gestures with a description, which the voice model plays on its own when the conversation fits or when asked, such as a wave or a clap, while the avatar's mouth follows the spoken answer. [Commit](https://github.com/open-webui/open-webui/commit/7401f41630e53999afd6c4efba06816e7c05cdb7), [Commit](https://github.com/open-webui/open-webui/commit/e56f85f43260ed528bdf20a8afa635a963b84b78)

> 📻 **OpenAI Realtime models for text-to-speech.** Administrators can now pick OpenAI Realtime as the text-to-speech engine in Audio settings, which uses the gpt-realtime-2.1 or gpt-realtime-2.1-mini model with voices such as Marin and Cedar only to turn text into a finished audio clip rather than for a live voice conversation, and the instructions that keep it reading text aloud word for word can be replaced under Prompt Template or with the "REALTIME_TTS_PROMPT_TEMPLATE" environment variable. [Commit](https://github.com/open-webui/open-webui/commit/b8738494cfab53f7e3f3849e8856c26263bd45fa), [Commit](https://github.com/open-webui/open-webui/commit/b0bcd945199c3b6884ef6526fb4edd6636cd06ba)

> 🎣 **Links no longer act on your behalf without asking.** Opening Open WebUI from a link, including from another website or a hidden frame, can no longer act in your name unseen: a prompt given with "?q=" is only filled into the message box instead of being sent, loading web pages or videos with "load-url" or "youtube" and starting a voice call with "call=true" or "voice=true" now ask for confirmation first, and links that create a note with a title and content now ask before creating it. [Commit](https://github.com/open-webui/open-webui/commit/91853205e817b0234fb3038f06cddf669ec7d335), [Commit](https://github.com/open-webui/open-webui/commit/0ffd86967fd2e5a537f69934b13c899b7f5c6f32)

> 💽 **Leaner storage of MCP media.** Images and audio returned by MCP tools are no longer saved a second time inside the database, which kept growing it with every such result. [#30419](https://github.com/open-webui/open-webui/pull/30419), [#30411](https://github.com/open-webui/open-webui/issues/30411)

> 🎙️ **Voice calls recover from speech failures.** When the text-to-speech provider fails during a voice call, the call now shows the provider's error once and goes back to listening, where it previously hung in "speaking" with no sound until tapped. [#30372](https://github.com/open-webui/open-webui/pull/30372), [#30052](https://github.com/open-webui/open-webui/issues/30052)

> 🎧 **Read Aloud on iPhone and iPad.** Replies read aloud automatically and voice calls now play sound on iOS and iPadOS, and a failed playback returns the speaker button to idle with an error message, where it previously stayed stuck in "speaking". [#30373](https://github.com/open-webui/open-webui/pull/30373), [#30262](https://github.com/open-webui/open-webui/issues/30262)

> 🎤 **Voice mode stops when leaving the chat.** Leaving a chat with voice mode active, for example to open the workspace or notes, now turns the microphone off, where it previously kept listening and sending what you said as prompts. [#30417](https://github.com/open-webui/open-webui/pull/30417), [#30405](https://github.com/open-webui/open-webui/issues/30405)

> 🔇 **Mute shortcut during voice calls.** Pressing M during a voice call mutes the microphone after every turn again, where it previously typed an "m" into the chat box. [#30421](https://github.com/open-webui/open-webui/pull/30421), [#30406](https://github.com/open-webui/open-webui/issues/30406)

> 🔊 **Kokoro voice in Voice Mode from links and shortcuts.** Voice Mode opened with "?call=true" or a desktop shortcut now speaks replies when the speech engine is Kokoro.js (Browser), where only opening it with the Voice mode button set up the voice. [#31829](https://github.com/open-webui/open-webui/pull/31829), [#31828](https://github.com/open-webui/open-webui/issues/31828)

> 🎤 **Web API dictation keeps listening.** With the Web API speech-to-text engine, dictation now only stops after two seconds of silence, where it could stop mid-sentence after a short pause. [#31891](https://github.com/open-webui/open-webui/pull/31891), [#19727](https://github.com/open-webui/open-webui/issues/19727)

> 🔇 **Interrupting Voice mode stops the reply.** Interrupting Voice mode while it speaks now stops the rest of the reply instead of reading out the sentences that were already queued. [#31877](https://github.com/open-webui/open-webui/pull/31877), [#31876](https://github.com/open-webui/open-webui/issues/31876)

> 🔈 **Read Aloud after a Voice mode call.** Read Aloud now plays with sound after a Voice mode call has ended, where it stayed muted until the chat was closed and opened again. [#31875](https://github.com/open-webui/open-webui/pull/31875), [#31874](https://github.com/open-webui/open-webui/issues/31874)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
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
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]]
- Later: 2026-10-12 · ElevenLabs · [[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-2c3b1e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-12-voice-and-audio-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-2c3b1e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->