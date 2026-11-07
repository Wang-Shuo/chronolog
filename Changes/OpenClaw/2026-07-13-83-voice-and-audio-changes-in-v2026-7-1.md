---
card_id: openclaw-2026-07-13-ad8430
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Voice and Audio: 83 changes in v2026.7.1 — Responsive
  layouts keep chat history and controls usable on phones, tablets, short landscape…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2926
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 61b89637c322506c004cf374758de7e5708945710e2474c25c60e0de1bd9c758
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-ad8430
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 83 Voice and Audio changes'
  evidence:
  - quote: Responsive layouts keep chat history and controls usable on phones, tablets,
      short landscape screens, and large desktops. Keyboard and focus behavior, contrast,
      assistive labels, copying, scrolling, and touch targets are more consistent,
      while navigation, pairing, voice, schedule, and status text reaches more supported
      languages.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WebChat stays on the newest reply when assistant audio or video finishes
      loading, while respecting readers who intentionally scrolled upward. #97575
      Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Control UI microphone-access warning for realtime voice input now appears
      in the user's selected language. 68c85ef
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Voice, Model, and Sensitivity controls in Control UI Talk settings
      now align consistently in one row without duplicate selected-value text disturbing
      the layout. #96925 Thanks @evan-ym.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI microphone button is now visually quieter while idle and
      more distinct while recording, making the current voice state easier to recognize.
      #101843'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Discord improves reply visibility, attachments, voice sessions, progress,
      reconnects, and multi-account behavior. Completed replies produce more useful
      unread cues, brief Gateway reconnects are less likely to lose outbound messages,
      and repeated session-resume failures can recover without taking the whole Gateway
      down.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Multiple Discord bot accounts in one server now keep independent voice
      sessions, and configured voice auto-join works even when Discord becomes ready
      before voice startup completes. #87530 Thanks @geekhuashan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When a Discord voice-note reply fails, users now receive the assistant''s
      answer as a threaded text fallback without duplicating text that was already
      delivered. #89962 Thanks @danhayman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Checking a Discord member who is not in voice now reports them as disconnected
      instead of raising a misleading command or gateway failure. #90969 Thanks @asock.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord PluralKit lookups and voice-upload setup now stop unexpectedly
      large JSON responses before they can exhaust memory. #97706 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Discord voice conversations in stt-tts mode now retain earlier spoken context
      across turns instead of starting over after each reply. 6cc534b Thanks @karabaralex,
      @sanjays2402.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord voice playback now turns broken ffmpeg output pipes into a normal
      playback error instead of an uncaught Gateway-level exception. #101088 Thanks
      @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'LINE file uploads now retain recognizable audio extensions such as .m4a
      , allowing valid recordings to reach transcription instead of being treated
      as unknown files. #96403 Thanks @tancolo, @zaidazmi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Meet and direct Voice Call sessions now keep the identity, workspace,
      routing, and transcript attribution of the agent that started the call instead
      of silently switching to the default agent. #77763 Thanks @quangtran88.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Callers using realtime OpenAI or Google voice calls can now interrupt
      assistant speech and have buffered phone audio stop promptly, while other providers
      keep the existing local fallback. #90749 Thanks @moellenbeck.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Voice callers now hear a completed answer without waiting for post-turn
      compaction, and a successful early playback is no longer repeated. #94015 Thanks
      @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Twilio voice-call operators can select US1, IE1, or AU1 so call control
      and records use the intended Region, with US1 remaining the default. #95832
      Thanks @jodok.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'QQBot speech-to-text now returns an early, labelled error when an OpenAI-compatible
      transcription endpoint sends an oversized response instead of buffering the
      full body in memory. #96968 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Inbound Telnyx-style and Plivo voice conversations can now continue after
      the caller''s first response instead of falling silent before OpenClaw speaks
      again. #100255 Thanks @dvy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated voice-call webhook deliveries are now acknowledged without repeating
      call or transcript side effects within the replay window. #100263 Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Twilio voice-call provider now rejects unsupported API hostnames before
      sending a request and accepts only OpenClaw's supported Twilio regional hosts.
      094c0d4 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw now recognizes .m2a recordings as audio, allowing them to move
      through attachment, transcription, memory, and chat display workflows without
      conversion. #92167 Thanks @llljjjwww333.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MP3 speech from Piper, Kokoro, and other OpenAI-compatible TTS endpoints
      now arrives in Telegram as a native voice note rather than a filename-style
      audio attachment. #100715 Thanks @hemantsudarshan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord voice replies now keep their accompanying text and extra media
      attached to the original message even when single-use reply mode is enabled.
      #95978 Thanks @nxmxbbd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord voice playback now cleans up ffmpeg after output-pipe failures,
      reducing both Gateway crashes and leftover transcoder processes. #101124'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord voice playback failures now produce a readable error within the
      8,192-byte limit, including when ffmpeg output contains non-English text or
      emoji. #104230 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'An accepted voice message that arrives while OpenClaw is already replying
      can still receive a voice response when tts.auto: "inbound" is configured. #95596
      Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Realtime voice prompts now remain readable when long agent names or injected
      context containing emoji must be shortened. #101304 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'QQBot previews, errors, commands, speech-to-text messages, media diagnostics,
      and logs now remain valid when emoji-containing text reaches a length limit.
      #101516 Thanks @vincentkoc, @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Meet local audio bridges now shut down cleanly and log a warning
      when a capture or playback command pipe fails, rather than crashing on an unhandled
      stream error. #101596 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI Realtime voice and transcription sessions now start behind Clash,
      Surge, sing-box, and similar TUN proxy setups that resolve api.openai.com into
      fake-IP ranges. #86526 Thanks @shushushv.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Realtime voice sessions now omit an individual custom tool with an invalid
      provider-specific name and warn about it instead of letting that tool break
      the entire OpenAI, Azure, or Google session. #89175 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI Realtime voice in Talk, Voice Call, and Discord was announced with
      a Codex/OpenAI OAuth fallback in #100671 . Correction: public Codex OAuth accounts
      do not have a supported realtime transport, so current builds require an OpenAI
      Platform API key. Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Inworld text-to-speech and voice-list requests now fail safely on oversized,
      malformed, or never-ending responses instead of hanging or consuming unbounded
      Gateway memory. #95416 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Configured Voice Call transcription providers such as xAI remain selectable
      when another provider registry is active, allowing Talk sessions to start normally.
      #97170 Thanks @solavrc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Missing official media providers now produce errors with the exact recovery
      commands needed to restore transcription and other media workflows. #97484 Thanks
      @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Live voice sessions can now register and call OpenClaw tools instead
      of rejecting their declarations before a tool-backed turn begins. #100260'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI realtime voice sessions now default to gpt-realtime-2.1 when no
      model is specified, while explicit model pins continue to work. #101390 Thanks
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Short non-English audio now keeps the configured language hint without
      an unrelated English prompt, reducing accidental translation when users expect
      a transcript in the spoken language. #99023 Thanks @flyveryhigh, @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS voice notes now stay with the intended chat and recover more reliably
      across offline queues, app recreation, uncertain sends, and competing microphone
      use. #101236'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Voice Call history now stays with the correct configured agent across
      Gateway restarts and upgrades, while ambiguous legacy state is left untouched
      with actionable warnings. #89884 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Experimental local-model lean mode now offers a smaller default tool menu
      for constrained models, while operators can explicitly retain media, voice,
      or PDF tools through allowlists. #88881 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Edge-case fixes now preserve literal memory text and valid Unicode, improve
      voice-call cleanup and port checks, report Claude models and context limits
      accurately, and retain useful ClickClack connection errors. #100204 Thanks @cxbasdev,
      @harjothkhara, @lilan0125, @lin-hongkuan, @liuhao1024, @mikasa0818, @pandah97,
      @sunlit-deng, @zoowh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shortened web, media, TTS, status, transport, and voice-call text now
      preserves complete Unicode characters instead of producing replacement symbols
      or malformed downstream content. #101355 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Voice-call webhook setup through ngrok or Tailscale now fails cleanly
      on tunnel stream errors instead of crashing the Gateway, and shutdown avoids
      waiting on an already-ended tunnel. #101394 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Non-admin Telegram and Discord users can no longer change the Gateway''s
      Talk voice, though they can still view the current and available voices. #97874
      Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Read-only voice-call status now omits phone numbers, transcripts, routing
      details, processed event IDs, and raw metadata. #97870 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Across first-party client surfaces, conversation lists, command palettes,
      notifications, media, connection state, and file or diff views behave more consistently.
      The TUI stays open with useful errors, Diffs controls remain scoped to the comparison
      on screen, and shared keyboard, path, status, Talk, and voice behavior is less
      likely to drift between clients.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The official apps share broader native localization, voice-message workflows,
      multiple Gateway profiles, cached conversations, and clearer connection state
      when people switch between installations.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: iOS adds refreshed navigation and chat, voice notes, workspace files, safer
      setup recovery, multiple Gateway profiles, and Apple Watch dictation and quick
      replies.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Android improves first-run setup, navigation, chat and session tools, voice,
      permissions, notifications, scheduled work, localization, multiple Gateway profiles,
      and connection recovery.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can record and send a voice note of up to three minutes from
      the chat composer, optionally add text, and see the recording''s duration in
      chat. #100946'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can record and send a voice note of up to three minutes
      from the chat composer without entering live Talk mode. #101193'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now reports Realtime Talk and Dictation readiness separately,
      opens setup only for the mode that needs it, and keeps useful provider failure
      details visible. #98269 Related #98268 . Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Back navigation now returns users from Gateway or Talk settings,
      Sessions, and Providers to the Voice, Chat, or command-palette tab where they
      started. #98914 Thanks @lokimorty.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Talk and Dictation now use a connected Bluetooth headset microphone
      for hands-free capture and fall back cleanly when it disconnects. #99259 Related
      #96241 . Thanks @gwtaylor.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android push-to-talk now cleans up backgrounded, cancelled, or retried
      captures without reopening the microphone or stopping a newer voice session,
      and overlapping requests return busy. #100552 Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Talk, dictation, speech-provider setup, readiness, and failure
      guidance now use the selected language across the translations in this release.
      Sources: c785196 , 9edb906 , da67520 , 88f13ca , e878efe , 662d127 , 5002a0e
      , fe57718 , ebcf8dc , 4e7ca8e , 9863ceb , 768da09 , ff5d986 , 005ebd1 , 2824796
      , 4eaec93 , f99fdc9 , 555f601 , d2af689 , 81e92de , 8ed6c78 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native prompts for starting work, checking status, using phone and voice
      controls, pairing, and returning to Chat now use the selected language across
      the translations in this release. Sources: dd050bc , db72ffd , 4997802 , 2dc7bd1
      , 4381c29 , 9eb1a05 , 7838bc8 , 4352eaf , 43fe5cc , 6bd1a4b , 531af42 , 305715c
      , 8f9e163 , 2abad57 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Talk''s Gateway Default now uses the configured Gateway speech provider,
      and stopping a reply prevents delayed audio from leaking into later turns. #98376
      Related #98153 . Thanks @jraxworthy, @tony-ooo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS Talk fallback banner now opens Voice & Talk settings directly
      instead of sending users to unrelated Gateway settings. #98602 Related #98593
      . Thanks @pollybot13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iPhone app now presents a compact Talk control bar, a cleaner Appearance
      picker, and a properly aligned realtime-audio button beside the resting Chat
      composer. #98736'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users who open Gateway, Voice, or Notifications settings from another
      screen now return to the Chat, Talk, Agent, Control, or Approvals screen they
      came from. #98898 Thanks @lokimorty.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Voice Wake on iOS can now pause while Talk, camera audio, or another feature
      uses the microphone and resume without crashing the app. #99137 Thanks @pollybot13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android voice features now speak only chat events explicitly identified
      as assistant replies, preventing user, tool, system, or role-less text from
      being read aloud. #99123 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Talk now applies supported directive values even when generated
      or dictated JSON uses different capitalization for keys such as Voice or Language_Code
      . #99592 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android node commands now honor common boolean values such as yes , no
      , 1 , and 0 for app filters and camera audio options. #99873 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Voice and Talk setup text now truncates cleanly on narrow screens
      and at larger accessibility font sizes instead of appearing clipped. #100060
      Thanks @iwhatsskill, @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Android Voice tab now gives Realtime Talk and Dictation text and controls
      enough room to remain readable on phones and at larger font sizes. #100491 Thanks
      @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Meet sessions launched through a paired macOS Chrome node now open
      the intended URL with the configured Chrome profile and audio tools, while unsupported
      actions and executable overrides are rejected before reaching the node. #96908
      Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed Voice Call status remains available through the Gateway, tool,
      and CLI after restart or eviction instead of incorrectly appearing missing.
      #99797 Thanks @darren2030.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Several edge cases now preserve transcript and voice text, surface MCP
      failures, bound oversized responses, show current session time, choose the right
      Linux package manager, and use port 443 for secure Gateway links without an
      explicit port. #100258 Thanks @connermo, @cxbasdev, @gfaerny, @hailory, @harjothkhara,
      @ly85206559, @mushuiyu886, @simon-xydt, @sunlit-deng, @uditdewan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A set of failure-path fixes now keeps commands and maintenance tasks running
      through isolated errors, preserves terminal and model text, improves skill and
      approval diagnostics, and stops Android voice sessions cleanly after microphone
      loss. #100440 Thanks @cxbasdev, @lavyatandel, @nankingjing, @nianjiuzst, @tzy-17,
      @wendy-chsy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Modernized Voice Call''s internal session handling without changing replies
      or call behavior. #96539 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized session migration testing while preserving focused coverage
      for Voice Call session handling. #97370 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added stronger runtime coverage for voice, media, scheduling, browser
      cleanup, and telemetry workflows. #99737 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated Voice Call route handling while preserving webhook and realtime
      matching. #99766 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented iOS startup failures when Voice Wake is disabled, including
      in Simulator development builds. #100370'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed the release record and contributor credit for three already-landed
      voice fixes. #100473'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved the consistency of compact Android voice and screen captures
      used for release review. #100895 Thanks @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced accidental internal interfaces in the Discord plugin without changing
      messaging or voice behavior. #101945 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept voice-call implementation details private while preserving the plugin''s
      existing behavior. #102059 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept Discord voice error details bounded and readable when failures contain
      multibyte text. #104684 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 83-voice-and-audio-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: voice
  title: 83 Voice and Audio changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-08-we-re-rolling-out-a-new-chatgpt-voice-experience-chatgpt-voice-is-now-powered-by|Introducing
  GPT-Live-1 in ChatGPT Voice]]'
- '[[Changes/Synthesia/2026-07-09-explore-stock-voices-by-language-preview-with-your-own-script-and-download-audio|Explore
  the new Voices page]]'
- '[[Changes/ChatGPT/2026-07-13-chatgpt-is-available-again-on-whatsapp-in-the-european-economic-area-eea-you-can-f60c71|ChatGPT
  returns to WhatsApp in the EEA]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: voice
title: 83 Voice and Audio changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 83 Voice and Audio changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Responsive layouts keep chat history and controls usable on phones, tablets, short landscape screens, and large desktops. Keyboard and focus behavior, contrast, assistive labels, copying, scrolling, and touch targets are more consistent, while navigation, pairing, voice, schedule, and status text reaches more supported languages.

> WebChat stays on the newest reply when assistant audio or video finishes loading, while respecting readers who intentionally scrolled upward. #97575 Thanks @turbotheturtle.

> The Control UI microphone-access warning for realtime voice input now appears in the user's selected language. 68c85ef

> The Voice, Model, and Sensitivity controls in Control UI Talk settings now align consistently in one row without duplicate selected-value text disturbing the layout. #96925 Thanks @evan-ym.

> The Control UI microphone button is now visually quieter while idle and more distinct while recording, making the current voice state easier to recognize. #101843

> Discord improves reply visibility, attachments, voice sessions, progress, reconnects, and multi-account behavior. Completed replies produce more useful unread cues, brief Gateway reconnects are less likely to lose outbound messages, and repeated session-resume failures can recover without taking the whole Gateway down.

> Multiple Discord bot accounts in one server now keep independent voice sessions, and configured voice auto-join works even when Discord becomes ready before voice startup completes. #87530 Thanks @geekhuashan.

> When a Discord voice-note reply fails, users now receive the assistant's answer as a threaded text fallback without duplicating text that was already delivered. #89962 Thanks @danhayman.

> Checking a Discord member who is not in voice now reports them as disconnected instead of raising a misleading command or gateway failure. #90969 Thanks @asock.

> Discord PluralKit lookups and voice-upload setup now stop unexpectedly large JSON responses before they can exhaust memory. #97706 Thanks @cxbasdev.

> Discord voice conversations in stt-tts mode now retain earlier spoken context across turns instead of starting over after each reply. 6cc534b Thanks @karabaralex, @sanjays2402.

> Discord voice playback now turns broken ffmpeg output pipes into a normal playback error instead of an uncaught Gateway-level exception. #101088 Thanks @masatohoshino.

> LINE file uploads now retain recognizable audio extensions such as .m4a , allowing valid recordings to reach transcription instead of being treated as unknown files. #96403 Thanks @tancolo, @zaidazmi.

> Google Meet and direct Voice Call sessions now keep the identity, workspace, routing, and transcript attribution of the agent that started the call instead of silently switching to the default agent. #77763 Thanks @quangtran88.

> Callers using realtime OpenAI or Google voice calls can now interrupt assistant speech and have buffered phone audio stop promptly, while other providers keep the existing local fallback. #90749 Thanks @moellenbeck.

> Voice callers now hear a completed answer without waiting for post-turn compaction, and a successful early playback is no longer repeated. #94015 Thanks @xialonglee.

> Twilio voice-call operators can select US1, IE1, or AU1 so call control and records use the intended Region, with US1 remaining the default. #95832 Thanks @jodok.

> QQBot speech-to-text now returns an early, labelled error when an OpenAI-compatible transcription endpoint sends an oversized response instead of buffering the full body in memory. #96968 Thanks @mushuiyu886.

> Inbound Telnyx-style and Plivo voice conversations can now continue after the caller's first response instead of falling silent before OpenClaw speaks again. #100255 Thanks @dvy.

> Repeated voice-call webhook deliveries are now acknowledged without repeating call or transcript side effects within the replay window. #100263 Thanks @xialonglee.

> The Twilio voice-call provider now rejects unsupported API hostnames before sending a request and accepts only OpenClaw's supported Twilio regional hosts. 094c0d4 Thanks @vincentkoc.

> OpenClaw now recognizes .m2a recordings as audio, allowing them to move through attachment, transcription, memory, and chat display workflows without conversion. #92167 Thanks @llljjjwww333.

> MP3 speech from Piper, Kokoro, and other OpenAI-compatible TTS endpoints now arrives in Telegram as a native voice note rather than a filename-style audio attachment. #100715 Thanks @hemantsudarshan.

> Discord voice replies now keep their accompanying text and extra media attached to the original message even when single-use reply mode is enabled. #95978 Thanks @nxmxbbd.

> Discord voice playback now cleans up ffmpeg after output-pipe failures, reducing both Gateway crashes and leftover transcoder processes. #101124

> Discord voice playback failures now produce a readable error within the 8,192-byte limit, including when ffmpeg output contains non-English text or emoji. #104230 Thanks @qingminglong.

> An accepted voice message that arrives while OpenClaw is already replying can still receive a voice response when tts.auto: "inbound" is configured. #95596 Thanks @mcaxtr.

> Realtime voice prompts now remain readable when long agent names or injected context containing emoji must be shortened. #101304 Thanks @alix-007.

> QQBot previews, errors, commands, speech-to-text messages, media diagnostics, and logs now remain valid when emoji-containing text reaches a length limit. #101516 Thanks @vincentkoc, @wangmiao0668000666.

> Google Meet local audio bridges now shut down cleanly and log a warning when a capture or playback command pipe fails, rather than crashing on an unhandled stream error. #101596 Thanks @alix-007.

> OpenAI Realtime voice and transcription sessions now start behind Clash, Surge, sing-box, and similar TUN proxy setups that resolve api.openai.com into fake-IP ranges. #86526 Thanks @shushushv.

> Realtime voice sessions now omit an individual custom tool with an invalid provider-specific name and warn about it instead of letting that tool break the entire OpenAI, Azure, or Google session. #89175 Thanks @vincentkoc.

> OpenAI Realtime voice in Talk, Voice Call, and Discord was announced with a Codex/OpenAI OAuth fallback in #100671 . Correction: public Codex OAuth accounts do not have a supported realtime transport, so current builds require an OpenAI Platform API key. Thanks @steipete-oai.

> Inworld text-to-speech and voice-list requests now fail safely on oversized, malformed, or never-ending responses instead of hanging or consuming unbounded Gateway memory. #95416 Thanks @alix-007, @vincentkoc.

> Configured Voice Call transcription providers such as xAI remain selectable when another provider registry is active, allowing Talk sessions to start normally. #97170 Thanks @solavrc.

> Missing official media providers now produce errors with the exact recovery commands needed to restore transcription and other media workflows. #97484 Thanks @wangmiao0668000666.

> Google Live voice sessions can now register and call OpenClaw tools instead of rejecting their declarations before a tool-backed turn begins. #100260

> OpenAI realtime voice sessions now default to gpt-realtime-2.1 when no model is specified, while explicit model pins continue to work. #101390 Thanks @vincentkoc.

> Short non-English audio now keeps the configured language hint without an unrelated English prompt, reducing accidental translation when users expect a transcript in the spoken language. #99023 Thanks @flyveryhigh, @nianjiuzst.

> iOS voice notes now stay with the intended chat and recover more reliably across offline queues, app recreation, uncertain sends, and competing microphone use. #101236

> Voice Call history now stays with the correct configured agent across Gateway restarts and upgrades, while ambiguous legacy state is left untouched with actionable warnings. #89884 Thanks @mushuiyu886.

> Experimental local-model lean mode now offers a smaller default tool menu for constrained models, while operators can explicitly retain media, voice, or PDF tools through allowlists. #88881 Thanks @vincentkoc.

> Edge-case fixes now preserve literal memory text and valid Unicode, improve voice-call cleanup and port checks, report Claude models and context limits accurately, and retain useful ClickClack connection errors. #100204 Thanks @cxbasdev, @harjothkhara, @lilan0125, @lin-hongkuan, @liuhao1024, @mikasa0818, @pandah97, @sunlit-deng, @zoowh.

> Shortened web, media, TTS, status, transport, and voice-call text now preserves complete Unicode characters instead of producing replacement symbols or malformed downstream content. #101355 Thanks @alix-007, @vincentkoc.

> Voice-call webhook setup through ngrok or Tailscale now fails cleanly on tunnel stream errors instead of crashing the Gateway, and shutdown avoids waiting on an already-ended tunnel. #101394 Thanks @cxbasdev.

> Non-admin Telegram and Discord users can no longer change the Gateway's Talk voice, though they can still view the current and available voices. #97874 Thanks @eleqtrizit.

> Read-only voice-call status now omits phone numbers, transcripts, routing details, processed event IDs, and raw metadata. #97870 Thanks @eleqtrizit.

> Across first-party client surfaces, conversation lists, command palettes, notifications, media, connection state, and file or diff views behave more consistently. The TUI stays open with useful errors, Diffs controls remain scoped to the comparison on screen, and shared keyboard, path, status, Talk, and voice behavior is less likely to drift between clients.

> The official apps share broader native localization, voice-message workflows, multiple Gateway profiles, cached conversations, and clearer connection state when people switch between installations.

> iOS adds refreshed navigation and chat, voice notes, workspace files, safer setup recovery, multiple Gateway profiles, and Apple Watch dictation and quick replies.

> Android improves first-run setup, navigation, chat and session tools, voice, permissions, notifications, scheduled work, localization, multiple Gateway profiles, and connection recovery.

> iOS users can record and send a voice note of up to three minutes from the chat composer, optionally add text, and see the recording's duration in chat. #100946

> Android users can record and send a voice note of up to three minutes from the chat composer without entering live Talk mode. #101193

> Android now reports Realtime Talk and Dictation readiness separately, opens setup only for the mode that needs it, and keeps useful provider failure details visible. #98269 Related #98268 . Thanks @solvely-colin.

> Android Back navigation now returns users from Gateway or Talk settings, Sessions, and Providers to the Voice, Chat, or command-palette tab where they started. #98914 Thanks @lokimorty.

> Android Talk and Dictation now use a connected Bluetooth headset microphone for hands-free capture and fall back cleanly when it disconnects. #99259 Related #96241 . Thanks @gwtaylor.

> Android push-to-talk now cleans up backgrounded, cancelled, or retried captures without reopening the microphone or stopping a newer voice session, and overlapping requests return busy. #100552 Thanks @xialonglee.

> Android Talk, dictation, speech-provider setup, readiness, and failure guidance now use the selected language across the translations in this release. Sources: c785196 , 9edb906 , da67520 , 88f13ca , e878efe , 662d127 , 5002a0e , fe57718 , ebcf8dc , 4e7ca8e , 9863ceb , 768da09 , ff5d986 , 005ebd1 , 2824796 , 4eaec93 , f99fdc9 , 555f601 , d2af689 , 81e92de , 8ed6c78 .

> Native prompts for starting work, checking status, using phone and voice controls, pairing, and returning to Chat now use the selected language across the translations in this release. Sources: dd050bc , db72ffd , 4997802 , 2dc7bd1 , 4381c29 , 9eb1a05 , 7838bc8 , 4352eaf , 43fe5cc , 6bd1a4b , 531af42 , 305715c , 8f9e163 , 2abad57 .

> iOS Talk's Gateway Default now uses the configured Gateway speech provider, and stopping a reply prevents delayed audio from leaking into later turns. #98376 Related #98153 . Thanks @jraxworthy, @tony-ooo.

> The iOS Talk fallback banner now opens Voice & Talk settings directly instead of sending users to unrelated Gateway settings. #98602 Related #98593 . Thanks @pollybot13.

> The iPhone app now presents a compact Talk control bar, a cleaner Appearance picker, and a properly aligned realtime-audio button beside the resting Chat composer. #98736

> iOS users who open Gateway, Voice, or Notifications settings from another screen now return to the Chat, Talk, Agent, Control, or Approvals screen they came from. #98898 Thanks @lokimorty.

> Voice Wake on iOS can now pause while Talk, camera audio, or another feature uses the microphone and resume without crashing the app. #99137 Thanks @pollybot13.

> Android voice features now speak only chat events explicitly identified as assistant replies, preventing user, tool, system, or role-less text from being read aloud. #99123 Thanks @ly85206559.

> Android Talk now applies supported directive values even when generated or dictated JSON uses different capitalization for keys such as Voice or Language_Code . #99592 Thanks @ly85206559.

> Android node commands now honor common boolean values such as yes , no , 1 , and 0 for app filters and camera audio options. #99873 Thanks @ly85206559.

> Android Voice and Talk setup text now truncates cleanly on narrow screens and at larger accessibility font sizes instead of appearing clipped. #100060 Thanks @iwhatsskill, @solvely-colin.

> The Android Voice tab now gives Realtime Talk and Dictation text and controls enough room to remain readable on phones and at larger font sizes. #100491 Thanks @iwhatsskill.

> Google Meet sessions launched through a paired macOS Chrome node now open the intended URL with the configured Chrome profile and audio tools, while unsupported actions and executable overrides are rejected before reaching the node. #96908 Thanks @joshavant.

> Completed Voice Call status remains available through the Gateway, tool, and CLI after restart or eviction instead of incorrectly appearing missing. #99797 Thanks @darren2030.

> Several edge cases now preserve transcript and voice text, surface MCP failures, bound oversized responses, show current session time, choose the right Linux package manager, and use port 443 for secure Gateway links without an explicit port. #100258 Thanks @connermo, @cxbasdev, @gfaerny, @hailory, @harjothkhara, @ly85206559, @mushuiyu886, @simon-xydt, @sunlit-deng, @uditdewan.

> A set of failure-path fixes now keeps commands and maintenance tasks running through isolated errors, preserves terminal and model text, improves skill and approval diagnostics, and stops Android voice sessions cleanly after microphone loss. #100440 Thanks @cxbasdev, @lavyatandel, @nankingjing, @nianjiuzst, @tzy-17, @wendy-chsy.

> Modernized Voice Call's internal session handling without changing replies or call behavior. #96539 Thanks @jalehman.

> Stabilized session migration testing while preserving focused coverage for Voice Call session handling. #97370 Thanks @romneyda.

> Added stronger runtime coverage for voice, media, scheduling, browser cleanup, and telemetry workflows. #99737 Thanks @romneyda.

> Consolidated Voice Call route handling while preserving webhook and realtime matching. #99766 Thanks @romneyda.

> Prevented iOS startup failures when Voice Wake is disabled, including in Simulator development builds. #100370

> Completed the release record and contributor credit for three already-landed voice fixes. #100473

> Improved the consistency of compact Android voice and screen captures used for release review. #100895 Thanks @iwhatsskill.

> Reduced accidental internal interfaces in the Discord plugin without changing messaging or voice behavior. #101945 Thanks @vincentkoc.

> Kept voice-call implementation details private while preserving the plugin's existing behavior. #102059 Thanks @vincentkoc.

> Kept Discord voice error details bounded and readable when failures contain multibyte text. #104684 Thanks @qingminglong.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-07-13 · ChatGPT · [[Changes/ChatGPT/2026-07-13-chatgpt-is-available-again-on-whatsapp-in-the-european-economic-area-eea-you-can-f60c71|ChatGPT returns to WhatsApp in the EEA]]
- Later: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-add-voice-devices-to-choose-and-persist-the-microphone-for-voice-mode|Add /voice devices to choose and persist the microphone for voice mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-ad8430&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-83-voice-and-audio-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-ad8430%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->