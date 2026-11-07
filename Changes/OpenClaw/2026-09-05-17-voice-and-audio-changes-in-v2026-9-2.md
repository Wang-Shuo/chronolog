---
card_id: openclaw-2026-09-05-b1f199
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Voice and Audio: 17 changes in v2026.9.2 — You
  can configure a listen-only bot to take Discord meeting notes when people enter
  a voice…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1153
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ec482b106b05c358888dd5d1d6ba1c0f99c26c5fa3cbab392a1c608f9b5fcf85
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-b1f199
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 17 Voice and Audio changes'
  evidence:
  - quote: You can configure a listen-only bot to take Discord meeting notes when
      people enter a voice room, then return to the overview, decisions, action items,
      and speaker-labeled transcript from the Meetings page . Agents can also read
      permitted saved meetings, so the conversation can continue from what was discussed
      without you having to paste the notes into a new chat.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Occupancy capture is opt-in and needs Discord voice and speech-to-text
      setup. Tell participants that transcripts will be captured and stored before
      enabling it, and configure at most one room per account and guild. The bot waits
      30 seconds after everyone leaves, and a meeting can reopen with its existing
      transcript within 10 minutes, including after a restart. Continuous capture
      remains the default for existing setups and now retains its capture identity
      through temporary startup failures.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: In a shared Discord voice room, a delayed request keeps the identity and
      permissions of the person who spoke it, while spoken answers queue in order
      instead of replacing one another. One speaker’s failed connection can recover
      when they speak again without disconnecting everyone else, and OpenAI agent-proxy
      early wake acknowledgments require the name at the start of the utterance instead
      of matching an unfinished ordinary word.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenAI and xAI voice replies also handle interruptions against the answer
      currently playing when another answer is queued, and later replies can continue
      after cancellation. The follow-up playback repair keeps a partial audio frame
      from ending the conversation during a provider pause. Direct voice-model history
      remains separate for each speaker while agent consultations share the room conversation;
      a room retains at most eight speaker connections, subject to the provider’s
      own limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: New M4A and audio WebM uploads stay in the audio workflow, staged recordings
      can use their original URL to recover the file type, and portrait video frames
      use display orientation when that information is available. Allowed local macro-enabled
      Excel workbooks can also be sent as attachments, preserving extension capitalization
      when staging uses the original extension. This handles the workbook as a file;
      it does not run or certify its macros, and audio transcription still needs its
      own setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Experimental Talk on Watch lets you start a voice conversation directly
      from your wrist, with the iPhone used for setup rather than relaying the call.
      The companion messaging path gets its own recovery screen, while iPhone and
      Android conversations become easier to read, copy, and follow through longer
      tasks. On Mac, personal browser sign-in brings your own account into shared
      Gateways, and clearer approval panels make it easier to see what you are allowing.
      Linux companion work addresses specific AppImage startup failures.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Talk on Watch is a new experimental way to speak with your Claw without
      the paired iPhone carrying the audio or relaying each message. Enable Standalone
      Voice under iPhone Settings → Apple Watch, then open Talk on Watch and tap Start.
      You can choose an agent, read the recent transcript, mute the microphone, and
      end the call from the Watch; simply opening the screen does not start recording,
      and each call has its own conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Setup requires an administrator connection on the iPhone, a trusted secure
      Gateway address the Watch can reach independently, and a compatible realtime
      provider using ICE-lite and UDP. The Watch receives its own limited read and
      Talk credentials, while permanent provider credentials stay on the Gateway.
      There is no TURN relay or TCP/WebSocket audio fallback, so a network that blocks
      the required UDP connection cannot use this path. Talk configuration explains
      the supported combinations.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The existing iPhone-relayed Watch chat now saves pending messages and completed
      replies on both devices, allowing a restart or reconnect to recover work without
      automatically repeating a send whose outcome is uncertain. Queued messages retain
      their original conversation even if you switch chats on the phone, and a saved
      reply can still be read after the spoken-reply wait has ended.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On eligible Android audio setups, Talk can keep listening while it speaks,
      so an interruption stops queued speech even after the provider has finished
      generating the reply. This requires active native echo cancellation and Android
      communication audio; other setups keep taking turns between listening and playback.
      Thinking, Listening, and Speaking now follow the current response and playback
      more closely, and new successful spoken answers appear once in Chat while errors
      and interrupted partial replies stay visible.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The native speech loop also sends recognized phrases and resumes listening
      after the answer, keeps capture running when reply audio is muted, and respects
      Stop or a switch to push-to-talk. Around that conversation, Disconnect stays
      disconnected, failed settings loads are shown as errors rather than empty data,
      and unresolved sends remain visible for recovery. Android guidance explains
      the native Talk path, while Talk mode covers the audio requirements.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Dashboard Settings gains a This Mac group for app behavior, device capabilities,
      permissions, and local Talk and update controls when a supporting Mac app exposes
      the native bridge. These controls remain owned by the Mac and appear only where
      that bridge supports them. Voice Wake trigger words belong to the connected
      Gateway, so their editor also works in an ordinary browser when the Gateway
      advertises the required methods.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When browsing native Codex or Claude sessions on connected computers, slow
      hosts can now add their results after the initial partial list arrives, subject
      to the viewer's current access. Internal voice consultations also stop producing
      false prompt-mirroring warnings when their hidden input was already saved.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Talk now checks for an unambiguous agent owner before loading providers,
      and voice-choice discovery can load provider catalogs without starting each
      full plugin. Compatible video-description services also honor their configured
      API-key or no-auth mode, with credentials reflected in service errors removed
      from diagnostics.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Documentation section links have been repaired across setup, troubleshooting,
      permissions, transcription, and skill-trust guidance. Computer-use and Podman
      instructions point to their intended sections, and maturity pages have unique
      jump targets without changing their recorded scores or implying a new QA run.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Several narrower changes remove work that no longer needs to be retained.
      Code Mode can release completed calls' inputs while slower calls continue, compute
      workers no longer require the parent process to hold their input copies throughout
      execution, and session-list refreshes can let go of obsolete cached pages. Long-conversation
      preparation avoids repeated validation and unnecessary copies, while voice processing
      skips debug-capture filesystem checks when capture is disabled. These changes
      reduce specific processing and retention costs; total history loading can still
      be dominated by database reads.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On Apple clients, Talk relay playback now follows the audio player's actual
      completion. The speaking state, playback acknowledgments, and microphone echo
      suppression stay active until queued audio finishes, while pause, interruption,
      and cancellation can still stop playback earlier.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 17-voice-and-audio-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: voice
  title: 17 Voice and Audio changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Ollama/2026-09-02-gemma4-now-supports-images-and-audio-on-mlx-engine|gemma4
  now supports images and audio on MLX engine]]'
- '[[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice
  and Audio changes in rust-v0.153.0]]'
- '[[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice
  and Audio changes in v2026.9.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: voice
title: 17 Voice and Audio changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Voice and Audio changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> You can configure a listen-only bot to take Discord meeting notes when people enter a voice room, then return to the overview, decisions, action items, and speaker-labeled transcript from the Meetings page . Agents can also read permitted saved meetings, so the conversation can continue from what was discussed without you having to paste the notes into a new chat.

> Occupancy capture is opt-in and needs Discord voice and speech-to-text setup. Tell participants that transcripts will be captured and stored before enabling it, and configure at most one room per account and guild. The bot waits 30 seconds after everyone leaves, and a meeting can reopen with its existing transcript within 10 minutes, including after a restart. Continuous capture remains the default for existing setups and now retains its capture identity through temporary startup failures.

> In a shared Discord voice room, a delayed request keeps the identity and permissions of the person who spoke it, while spoken answers queue in order instead of replacing one another. One speaker’s failed connection can recover when they speak again without disconnecting everyone else, and OpenAI agent-proxy early wake acknowledgments require the name at the start of the utterance instead of matching an unfinished ordinary word.

> OpenAI and xAI voice replies also handle interruptions against the answer currently playing when another answer is queued, and later replies can continue after cancellation. The follow-up playback repair keeps a partial audio frame from ending the conversation during a provider pause. Direct voice-model history remains separate for each speaker while agent consultations share the room conversation; a room retains at most eight speaker connections, subject to the provider’s own limits.

> New M4A and audio WebM uploads stay in the audio workflow, staged recordings can use their original URL to recover the file type, and portrait video frames use display orientation when that information is available. Allowed local macro-enabled Excel workbooks can also be sent as attachments, preserving extension capitalization when staging uses the original extension. This handles the workbook as a file; it does not run or certify its macros, and audio transcription still needs its own setup.

> Experimental Talk on Watch lets you start a voice conversation directly from your wrist, with the iPhone used for setup rather than relaying the call. The companion messaging path gets its own recovery screen, while iPhone and Android conversations become easier to read, copy, and follow through longer tasks. On Mac, personal browser sign-in brings your own account into shared Gateways, and clearer approval panels make it easier to see what you are allowing. Linux companion work addresses specific AppImage startup failures.

> Talk on Watch is a new experimental way to speak with your Claw without the paired iPhone carrying the audio or relaying each message. Enable Standalone Voice under iPhone Settings → Apple Watch, then open Talk on Watch and tap Start. You can choose an agent, read the recent transcript, mute the microphone, and end the call from the Watch; simply opening the screen does not start recording, and each call has its own conversation.

> Setup requires an administrator connection on the iPhone, a trusted secure Gateway address the Watch can reach independently, and a compatible realtime provider using ICE-lite and UDP. The Watch receives its own limited read and Talk credentials, while permanent provider credentials stay on the Gateway. There is no TURN relay or TCP/WebSocket audio fallback, so a network that blocks the required UDP connection cannot use this path. Talk configuration explains the supported combinations.

> The existing iPhone-relayed Watch chat now saves pending messages and completed replies on both devices, allowing a restart or reconnect to recover work without automatically repeating a send whose outcome is uncertain. Queued messages retain their original conversation even if you switch chats on the phone, and a saved reply can still be read after the spoken-reply wait has ended.

> On eligible Android audio setups, Talk can keep listening while it speaks, so an interruption stops queued speech even after the provider has finished generating the reply. This requires active native echo cancellation and Android communication audio; other setups keep taking turns between listening and playback. Thinking, Listening, and Speaking now follow the current response and playback more closely, and new successful spoken answers appear once in Chat while errors and interrupted partial replies stay visible.

> The native speech loop also sends recognized phrases and resumes listening after the answer, keeps capture running when reply audio is muted, and respects Stop or a switch to push-to-talk. Around that conversation, Disconnect stays disconnected, failed settings loads are shown as errors rather than empty data, and unresolved sends remain visible for recovery. Android guidance explains the native Talk path, while Talk mode covers the audio requirements.

> Dashboard Settings gains a This Mac group for app behavior, device capabilities, permissions, and local Talk and update controls when a supporting Mac app exposes the native bridge. These controls remain owned by the Mac and appear only where that bridge supports them. Voice Wake trigger words belong to the connected Gateway, so their editor also works in an ordinary browser when the Gateway advertises the required methods.

> When browsing native Codex or Claude sessions on connected computers, slow hosts can now add their results after the initial partial list arrives, subject to the viewer's current access. Internal voice consultations also stop producing false prompt-mirroring warnings when their hidden input was already saved.

> Talk now checks for an unambiguous agent owner before loading providers, and voice-choice discovery can load provider catalogs without starting each full plugin. Compatible video-description services also honor their configured API-key or no-auth mode, with credentials reflected in service errors removed from diagnostics.

> Documentation section links have been repaired across setup, troubleshooting, permissions, transcription, and skill-trust guidance. Computer-use and Podman instructions point to their intended sections, and maturity pages have unique jump targets without changing their recorded scores or implying a new QA run.

> Several narrower changes remove work that no longer needs to be retained. Code Mode can release completed calls' inputs while slower calls continue, compute workers no longer require the parent process to hold their input copies throughout execution, and session-list refreshes can let go of obsolete cached pages. Long-conversation preparation avoids repeated validation and unnecessary copies, while voice processing skips debug-capture filesystem checks when capture is disabled. These changes reduce specific processing and retention costs; total history loading can still be dominated by database reads.

> On Apple clients, Talk relay playback now follows the audio player's actual completion. The speaking state, playback acknowledgments, and microphone echo suppression stay active until queued audio finishes, while pause, interruption, and cancellation can still stop playback earlier.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-03 · OpenClaw · [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]]
- Later: 2026-09-07 · ElevenLabs · [[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-b1f199&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-17-voice-and-audio-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-b1f199%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->