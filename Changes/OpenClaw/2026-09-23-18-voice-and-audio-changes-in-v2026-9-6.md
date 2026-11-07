---
card_id: openclaw-2026-09-23-244485
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Voice and Audio: 18 changes in v2026.9.6 — Attachments
  marked as voice notes now play inside chat with compact play, seek, time and…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5951843e1fe841494fa0846fd9017f120dd98d1ea8d28fb51f935e29ca05474d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-244485
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 18 Voice and Audio changes'
  evidence:
  - quote: Attachments marked as voice notes now play inside chat with compact play,
      seek, time and mute controls and a waveform measured from the audio, without
      file headers or opening a side panel. Ordinary audio files keep their metadata
      and expansion controls. If a voice note cannot preview, its available download
      opens separately so the conversation stays in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Routine model and voice logs are quieter, with detail available at debug
      level while errors, slow responses and secret-egress audits remain visible.
      Invalid directory log paths now show an error and keep the last records visibly
      stale. Routine structured log records can omit _meta.path , which matters if
      your log-processing tools expect that field.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Discord videos and images with duration metadata also keep their visual
      media type instead of being mistaken for voice notes, while genuine waveform-bearing
      voice notes remain audio. Video understanding still depends on the configured
      provider's capabilities.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Speakers already authorized to talk to the agent can ask to list or change
      the current Discord call voice without also being configured as command owners.
      A change affects everyone in the shared call, while saved defaults and other
      owner-only permissions stay in place. That voice access ends with the call or
      turn, cancellation, or revoked access.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Established Discord and GPT Live playback can continue while other Gateway
      work is busy, reducing stutters caused by that work. Changing voices keeps speech
      that has not started without replaying speech already underway. Speaker admission,
      microphone forwarding, agent work, and transcripts can still wait on the Gateway,
      so this does not remove every source of voice delay.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: During realtime Talk, the phone leaves automatic local read-aloud silent,
      including replies started from another client, so consultation answers are not
      spoken twice. Text remains visible, and native Talk and explicit read-aloud
      remain available. Reconnecting to the same Gateway also keeps the selected agent
      in memory, while new Android voice messages send the recognized words without
      the app's former added instructions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Talk keeps valid consultation answers when speech transcription finishes
      late and shows each new answer once in Chat. Your spoken request remains readable
      while generated instructions for handing work to the agent stay out of the visible
      conversation. On supported interruptible relay calls, interrupting a reply also
      lets you continue speaking without immediately losing the call when the provider
      is slow to confirm the stop.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Long watch replies now offer Read full reply, with scrolling, part navigation,
      and retry controls beyond the compact preview. Update both the watch app and
      phone companion; Chat also needs a Gateway that supports full-message retrieval.
      Voice status and microphone guidance fit small watches more comfortably, and
      context selections expose their selected state to accessibility services. Live
      Chat stays a preview until a stored reply is available, and older Talk text
      can become unavailable after its session data is retired.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Canvas widgets can play direct HTTPS audio and video in inline previews,
      dashboards, and native panels. Update both the Mac app and Gateway, then update
      or recreate older saved widgets to receive the new media policy. Browser format
      support and autoplay rules still apply, so playback controls remain useful.
      Media requests can reach HTTPS hosts beyond a widget's separately granted API
      connections; the widget media guide explains the distinction.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Audio and document attachments can be read through equivalent macOS paths
      such as /tmp and /private/tmp . The opened file must still be inside a permitted
      folder, so this fixes path handling without extending access to neighboring
      folders or shared workspaces.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Native iOS chat now offers Download file on assistant-generated documents,
      handing the downloaded file to the system share sheet with Save to Files and
      other apps available. Shared native Mac chat adds a save panel for those documents.
      Downloads need current Gateway access and stay within the existing 100 MiB limit;
      expired or removed files need to be regenerated. Images, audio, and video keep
      their separate controls.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Deepgram prerecorded transcription now retains speech from later audio
      channels, including recordings whose first track is silent. It uses the best
      alternative from each channel in the provider's order; it does not interleave
      the tracks chronologically or add speaker labels.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Doctor can identify missing commands or arguments in CLI media-tool setup,
      and transcription rejects those incomplete commands before launching them while
      retaining model fallback. It provides guidance without rewriting your settings.
      Audio discovery also skips Whisper model scans when whisper-cli is not installed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can follow meeting notes while capture continues, with updates about
      every five minutes when new speech arrives and final notes when capture ends.
      This works with captured voice and Google Meet, Microsoft Teams, and Zoom meetings
      . The Meetings page refreshes automatically and keeps the complete saved transcript
      in its own tab, so you can move between the notes and what was said. Users with
      write access can also generate missing notes. Transcription can lag the conversation,
      and model-generated notes use your configured model, with normal usage charges
      and existing summary input limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Leaving a meeting now waits for audio startup already in progress and shutdown
      of the resulting audio runtime before reporting success. Rejoining the same
      meeting waits for that cleanup, while other meetings remain independent. Failed
      joins stay reachable while another leave attempt is needed to finish cleanup.
      Audio cleanup and leaving the browser meeting are separate, and a cleanup failure
      can still require a retry before replacement proceeds.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The optional FaceTime plugin adds one-to-one audio conversations with your
      configured agent, including spoken answers to requests that need its tools or
      memory. It is experimental, disabled by default, and needs a dedicated Apple
      Silicon Mac running macOS 14.4 or later, OpenClaw 2026.9.6, matching signed
      native helpers, configured audio devices, and realtime-provider credentials.
      Matching plugin and native distribution availability remains unconfirmed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Local speech commands preserve intentionally empty quoted arguments, preventing
      later options from shifting into the wrong position. Ordinary replies also skip
      unnecessary Markdown parsing when OpenClaw checks whether they should be spoken,
      without changing speech policy or synthesis limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Media handling and browser snapshot processing reuse information already
      prepared during the same operation. Shared parsing and formatting helpers retain
      existing attachment selection, transcription requests and browser output.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 18-voice-and-audio-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: voice
  title: 18 Voice and Audio changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice
  and Audio changes in rust-v0.156.0]]'
- '[[Changes/Google Antigravity/2026-09-22-right-clicking-an-image-caption-or-an-enlarged-image-no-longer-pops-open-the-thu|Right-clicking
  an image caption or an enlarged image no longer pops open…]]'
- '[[Changes/ChatGPT/2026-09-23-live-now-supports-plugins-on-web-ios-and-android-you-can-use-the-plugins-and-con-88a242|Use
  plugins in Voice and get work done by speaking]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: voice
title: 18 Voice and Audio changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Voice and Audio changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Attachments marked as voice notes now play inside chat with compact play, seek, time and mute controls and a waveform measured from the audio, without file headers or opening a side panel. Ordinary audio files keep their metadata and expansion controls. If a voice note cannot preview, its available download opens separately so the conversation stays in place.

> Routine model and voice logs are quieter, with detail available at debug level while errors, slow responses and secret-egress audits remain visible. Invalid directory log paths now show an error and keep the last records visibly stale. Routine structured log records can omit _meta.path , which matters if your log-processing tools expect that field.

> Discord videos and images with duration metadata also keep their visual media type instead of being mistaken for voice notes, while genuine waveform-bearing voice notes remain audio. Video understanding still depends on the configured provider's capabilities.

> Speakers already authorized to talk to the agent can ask to list or change the current Discord call voice without also being configured as command owners. A change affects everyone in the shared call, while saved defaults and other owner-only permissions stay in place. That voice access ends with the call or turn, cancellation, or revoked access.

> Established Discord and GPT Live playback can continue while other Gateway work is busy, reducing stutters caused by that work. Changing voices keeps speech that has not started without replaying speech already underway. Speaker admission, microphone forwarding, agent work, and transcripts can still wait on the Gateway, so this does not remove every source of voice delay.

> During realtime Talk, the phone leaves automatic local read-aloud silent, including replies started from another client, so consultation answers are not spoken twice. Text remains visible, and native Talk and explicit read-aloud remain available. Reconnecting to the same Gateway also keeps the selected agent in memory, while new Android voice messages send the recognized words without the app's former added instructions.

> Talk keeps valid consultation answers when speech transcription finishes late and shows each new answer once in Chat. Your spoken request remains readable while generated instructions for handing work to the agent stay out of the visible conversation. On supported interruptible relay calls, interrupting a reply also lets you continue speaking without immediately losing the call when the provider is slow to confirm the stop.

> Long watch replies now offer Read full reply, with scrolling, part navigation, and retry controls beyond the compact preview. Update both the watch app and phone companion; Chat also needs a Gateway that supports full-message retrieval. Voice status and microphone guidance fit small watches more comfortably, and context selections expose their selected state to accessibility services. Live Chat stays a preview until a stored reply is available, and older Talk text can become unavailable after its session data is retired.

> Canvas widgets can play direct HTTPS audio and video in inline previews, dashboards, and native panels. Update both the Mac app and Gateway, then update or recreate older saved widgets to receive the new media policy. Browser format support and autoplay rules still apply, so playback controls remain useful. Media requests can reach HTTPS hosts beyond a widget's separately granted API connections; the widget media guide explains the distinction.

> Audio and document attachments can be read through equivalent macOS paths such as /tmp and /private/tmp . The opened file must still be inside a permitted folder, so this fixes path handling without extending access to neighboring folders or shared workspaces.

> Native iOS chat now offers Download file on assistant-generated documents, handing the downloaded file to the system share sheet with Save to Files and other apps available. Shared native Mac chat adds a save panel for those documents. Downloads need current Gateway access and stay within the existing 100 MiB limit; expired or removed files need to be regenerated. Images, audio, and video keep their separate controls.

> Deepgram prerecorded transcription now retains speech from later audio channels, including recordings whose first track is silent. It uses the best alternative from each channel in the provider's order; it does not interleave the tracks chronologically or add speaker labels.

> Doctor can identify missing commands or arguments in CLI media-tool setup, and transcription rejects those incomplete commands before launching them while retaining model fallback. It provides guidance without rewriting your settings. Audio discovery also skips Whisper model scans when whisper-cli is not installed.

> You can follow meeting notes while capture continues, with updates about every five minutes when new speech arrives and final notes when capture ends. This works with captured voice and Google Meet, Microsoft Teams, and Zoom meetings . The Meetings page refreshes automatically and keeps the complete saved transcript in its own tab, so you can move between the notes and what was said. Users with write access can also generate missing notes. Transcription can lag the conversation, and model-generated notes use your configured model, with normal usage charges and existing summary input limits.

> Leaving a meeting now waits for audio startup already in progress and shutdown of the resulting audio runtime before reporting success. Rejoining the same meeting waits for that cleanup, while other meetings remain independent. Failed joins stay reachable while another leave attempt is needed to finish cleanup. Audio cleanup and leaving the browser meeting are separate, and a cleanup failure can still require a retry before replacement proceeds.

> The optional FaceTime plugin adds one-to-one audio conversations with your configured agent, including spoken answers to requests that need its tools or memory. It is experimental, disabled by default, and needs a dedicated Apple Silicon Mac running macOS 14.4 or later, OpenClaw 2026.9.6, matching signed native helpers, configured audio devices, and realtime-provider credentials. Matching plugin and native distribution availability remains unconfirmed.

> Local speech commands preserve intentionally empty quoted arguments, preventing later options from shifting into the wrong position. Ordinary replies also skip unnecessary Markdown parsing when OpenClaw checks whether they should be spoken, without changing speech policy or synthesis limits.

> Media handling and browser snapshot processing reuse information already prepared during the same operation. Shared parsing and formatting helpers retain existing attachment selection, transcription requests and browser output.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-23 · ChatGPT · [[Changes/ChatGPT/2026-09-23-live-now-supports-plugins-on-web-ios-and-android-you-can-use-the-plugins-and-con-88a242|Use plugins in Voice and get work done by speaking]]
- Later: 2026-09-25 · Codex CLI · [[Changes/Codex CLI/2026-09-25-5-voice-and-audio-changes-in-rust-v0-157-0|5 Voice and Audio changes in rust-v0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-244485&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-18-voice-and-audio-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-244485%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->