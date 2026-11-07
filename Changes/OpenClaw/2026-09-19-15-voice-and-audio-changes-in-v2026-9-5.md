---
card_id: openclaw-2026-09-19-d77e44
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Voice and Audio: 15 changes in v2026.9.5 — The
  bundled tool refresh preserves chat scroll position during streaming and dock changes…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2994
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59c99e2d5015bbbfe7d6d44ca9cf7996ab8898c0d491cd6f9c3d16c202d693dc
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-d77e44
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 15 Voice and Audio changes'
  evidence:
  - quote: The bundled tool refresh preserves chat scroll position during streaming
      and dock changes, fixes cleanup after an unused iOS voice capture is canceled,
      and keeps hidden Mac Dashboard and chat windows hidden. MCP app discovery, themes,
      and command-line selections also retain compatibility with their updated dependencies.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Configured GPT-Live conversations in Discord can play short and subsequent
      replies, preserve pauses, and hear you interrupt while the agent speaks. Uneven
      audio arrives with fewer playback gaps, using up to 120 ms of initial buffering,
      and silence no longer interrupts the reply. Buttons, forms, model menus, and
      Activity launches also keep their actions tied to the intended choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'For GPT-Live, remove requireWakeName: true and consultPolicy: "always"
      , or choose gpt-realtime-2.1 for host-controlled turns. The separate opt-in
      alternate Discord endpoint applies across accounts, takes precedence over explicit
      proxy and custom-fetch choices, blocks off-origin media, has no silent fallback
      to public Discord, and does not support interactive voice.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When you cancel local MLX speech on your Mac, audio arriving late is discarded
      before playback and cannot interfere with a newer Talk request. Microphone tests
      finish cleaning up before you can start another, and camera capture ends before
      the recording is exported.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Accepted Type or Dictate input from Voice now opens Chat to show the reply
      or error. Canceled, empty or locally rejected input leaves you on the current
      page, and active Live Talk stays in Voice. You can also tap a failed-reply notification
      to open the watch app; its Reply action still retries through the original phone
      and conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Android and iOS now show what is happening while dictation starts, listens
      and finishes, with recognized words visible before they enter your draft. Android's
      Stop finishes listening, Cancel discards a starting or transcribing attempt,
      and only final text is inserted. iOS adds a live waveform and offers Done to
      add the transcript or Cancel to discard it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Both show attachment-preparation progress. Android distinguishes local
      message queuing from delivery, while iOS also shows attachment sending and asks
      you to select an unavailable photo or video again. Dictation errors give retry
      guidance without silently leaving you waiting.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Android Talk now sends spoken turns that previously stopped after recognition
      and honors an explicit stt-tts choice using your configured speech provider
      and voice. Idle recognition beeps, visible fixed Talk instructions and setup
      readiness without a realtime provider remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Translations across 21 existing native-app locales now cover more Gateway
      setup, pending questions and approvals, dictation and attachment feedback. Android
      also gains translated QR-scanning and Talk voice-change guidance, while Mac
      onboarding gains translated setup and utility-model labels.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Live is audio-only, so choose gpt-realtime-2.1 when you need a camera.
      Configured Platform credentials take precedence over ChatGPT subscription access
      and use the Platform billing route. For meetings, update both Gateway and paired
      node and use supported isolated audio capture; remove a custom audioInputCommand
      before selecting Live. Live does not support Voice Call custom functions or
      host-controlled wake-name and forced-consult modes. On Apple clients, Stop ends
      the Live session. Headphones help prevent speaker feedback.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Conceptual illustration: A voice for the work in front of you.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can ask the assistant to change its speaking voice during supported
      Talk calls , or use the browser's voice picker. Supported Discord calls also
      offer in-call switching, now including Google Live's prebuilt voices. The call
      briefly reconnects while keeping the conversation and unfinished work, and your
      saved defaults stay unchanged. Speech already submitted to Google may be interrupted
      and is not replayed. Discord still requires an authorized voice turn with agent
      delegation and tool access.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Deepgram Flux preserves voice-note audio beyond 20 minutes instead of silently
      dropping the end, within your configured size and timeout limits. The speech
      CLI also rejects an unsupported remote Gateway --output request before synthesis
      starts, avoiding provider usage for a file it cannot save locally. Audio transcription
      commands now identify the provider and model used when that information is available.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Generated music attachments now use the saved audio filename, including
      a name you supplied, so immediate results and background completion messages
      identify the same file. Generated images and saved videos also keep readable
      filenames in their results and completion messages while retaining their unique
      storage paths. Videos returned only as links keep their existing names.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Find past meetings by words in saved notes or transcripts, then read long
      summaries with their headings and lists intact. The wider meeting timeline gives
      those notes more room, with clear loading feedback on desktop and mobile. Larger
      saved transcript libraries and voice-call histories also avoid repeated database
      work when you reopen them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-voice-and-audio-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: voice
  title: 15 Voice and Audio changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Descript/2026-09-17-how-to-find-it-537bc8|How to find it]]'
- '[[Changes/Descript/2026-09-17-give-a-recording-a-different-voice|Give a recording
  a different voice]]'
- '[[Changes/Qoder/2026-09-18-voice-input-press-and-hold-the-mouse-button-in-the-chat-input-box-to-dictate-rel|Voice
  input: Press and hold the mouse button in the chat input box to dictate]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: voice
title: 15 Voice and Audio changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Voice and Audio changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The bundled tool refresh preserves chat scroll position during streaming and dock changes, fixes cleanup after an unused iOS voice capture is canceled, and keeps hidden Mac Dashboard and chat windows hidden. MCP app discovery, themes, and command-line selections also retain compatibility with their updated dependencies.

> Configured GPT-Live conversations in Discord can play short and subsequent replies, preserve pauses, and hear you interrupt while the agent speaks. Uneven audio arrives with fewer playback gaps, using up to 120 ms of initial buffering, and silence no longer interrupts the reply. Buttons, forms, model menus, and Activity launches also keep their actions tied to the intended choice.

> For GPT-Live, remove requireWakeName: true and consultPolicy: "always" , or choose gpt-realtime-2.1 for host-controlled turns. The separate opt-in alternate Discord endpoint applies across accounts, takes precedence over explicit proxy and custom-fetch choices, blocks off-origin media, has no silent fallback to public Discord, and does not support interactive voice.

> When you cancel local MLX speech on your Mac, audio arriving late is discarded before playback and cannot interfere with a newer Talk request. Microphone tests finish cleaning up before you can start another, and camera capture ends before the recording is exported.

> Accepted Type or Dictate input from Voice now opens Chat to show the reply or error. Canceled, empty or locally rejected input leaves you on the current page, and active Live Talk stays in Voice. You can also tap a failed-reply notification to open the watch app; its Reply action still retries through the original phone and conversation.

> Android and iOS now show what is happening while dictation starts, listens and finishes, with recognized words visible before they enter your draft. Android's Stop finishes listening, Cancel discards a starting or transcribing attempt, and only final text is inserted. iOS adds a live waveform and offers Done to add the transcript or Cancel to discard it.

> Both show attachment-preparation progress. Android distinguishes local message queuing from delivery, while iOS also shows attachment sending and asks you to select an unavailable photo or video again. Dictation errors give retry guidance without silently leaving you waiting.

> Android Talk now sends spoken turns that previously stopped after recognition and honors an explicit stt-tts choice using your configured speech provider and voice. Idle recognition beeps, visible fixed Talk instructions and setup readiness without a realtime provider remain unchanged.

> Translations across 21 existing native-app locales now cover more Gateway setup, pending questions and approvals, dictation and attachment feedback. Android also gains translated QR-scanning and Talk voice-change guidance, while Mac onboarding gains translated setup and utility-model labels.

> Live is audio-only, so choose gpt-realtime-2.1 when you need a camera. Configured Platform credentials take precedence over ChatGPT subscription access and use the Platform billing route. For meetings, update both Gateway and paired node and use supported isolated audio capture; remove a custom audioInputCommand before selecting Live. Live does not support Voice Call custom functions or host-controlled wake-name and forced-consult modes. On Apple clients, Stop ends the Live session. Headphones help prevent speaker feedback.

> Conceptual illustration: A voice for the work in front of you.

> You can ask the assistant to change its speaking voice during supported Talk calls , or use the browser's voice picker. Supported Discord calls also offer in-call switching, now including Google Live's prebuilt voices. The call briefly reconnects while keeping the conversation and unfinished work, and your saved defaults stay unchanged. Speech already submitted to Google may be interrupted and is not replayed. Discord still requires an authorized voice turn with agent delegation and tool access.

> Deepgram Flux preserves voice-note audio beyond 20 minutes instead of silently dropping the end, within your configured size and timeout limits. The speech CLI also rejects an unsupported remote Gateway --output request before synthesis starts, avoiding provider usage for a file it cannot save locally. Audio transcription commands now identify the provider and model used when that information is available.

> Generated music attachments now use the saved audio filename, including a name you supplied, so immediate results and background completion messages identify the same file. Generated images and saved videos also keep readable filenames in their results and completion messages while retaining their unique storage paths. Videos returned only as links keep their existing names.

> Find past meetings by words in saved notes or transcripts, then read long summaries with their headings and lists intact. The wider meeting timeline gives those notes more room, with clear loading feedback on desktop and mobile. Larger saved transcript libraries and voice-call histories also avoid repeated database work when you reopen them.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-18 · Qoder · [[Changes/Qoder/2026-09-18-voice-input-press-and-hold-the-mouse-button-in-the-chat-input-box-to-dictate-rel|Voice input: Press and hold the mouse button in the chat input box to dictate]]
- Later: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-d77e44&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-15-voice-and-audio-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-d77e44%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->