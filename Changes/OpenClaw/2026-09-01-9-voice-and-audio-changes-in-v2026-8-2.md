---
card_id: openclaw-2026-09-01-1a83bd
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Voice and Audio: 9 changes in v2026.8.2 — v2026.8.2
  adds a Home button to the Control UI that opens your personal Home agent beside…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2976
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad1539ff102d32075f3696cf6f27170bb7492c0ec0f579a8d4c447d676cac895
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-1a83bd
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 9 Voice and Audio changes'
  evidence:
  - quote: v2026.8.2 adds a Home button to the Control UI that opens your personal
      Home agent beside whatever you are working on, instead of making you leave it
      to start another conversation. It also brings a Linux desktop companion, background
      sessions you can start without switching pages, browser control that can stay
      available without a running Gateway, four new looks for the Control UI, and
      a long tail of fixes for replies, voice, updates, and recovery.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Doctor can now take explicit ownership of more offline repair work by stopping
      the matching managed Gateway, completing supported repairs, checking the result,
      and restarting the same service. It can recover supported legacy approvals and
      databases, preserve valid scheduled jobs and current Voice Call settings during
      migration, and explain which original material remains available when a repair
      cannot finish.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Voice, media, and channel conversations now do a better job of reaching
      a clear ending and staying with the person and chat that started them. Spoken
      replies survive more delivery handoffs, calls and Browser Talk keep turns in
      order, attachments and plain text retain their intended shape, and account-specific
      failures no longer have to take every healthy channel down with them.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Spoken replies now make it through more of the places where successful
      synthesis could previously disappear or be mistaken for an unfinished answer.
      Private Discord and Telegram replies can deliver one permitted built-in TTS
      voice note while keeping private final text hidden, long replies leave internal
      reasoning and known tool-status text out of the audio, and delivered speech
      can finish the turn without a misleading warning or an unnecessary second request.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Speech created during Code Mode, Tool Search, or Codex work also has a
      clearer path into the final reply, while audio that finishes only after the
      request has timed out stays withheld.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Voice Call now drops an obsolete automatic answer when the caller starts
      speaking again, and an old call stream can no longer disrupt the current reply.
      Late provider updates stay attached to the original call with its transcript,
      duration, and agent, while a failed first save no longer dials or consumes the
      only call slot, so restoring storage access is enough to try again.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Affected AVI video and ASF or WMA audio also return to their existing playback-conversion
      paths instead of falling back as unsupported.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Voice and transcription settings now reach the service they were meant
      for more consistently. OpenRouter and DeepInfra speech honor the configured
      voice, Voice Call and Talk can find eligible configured providers, Talk clients
      can use advertised transcription models, and TTS personas can use credentials
      stored through SecretRefs without borrowing another provider's key.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: For multilingual voice notes, leaving the language unset now uses automatic
      language detection without inserting an English instruction into the transcript.
      xAI transcription can accept silence as an empty result and continue to a configured
      fallback, while private or self-hosted xAI setups can use their configured address
      for voice discovery and buffered speech.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-voice-and-audio-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: voice
  title: 9 Voice and Audio changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-08-31-2-voice-and-audio-changes-in-v2026-8-1|2 Voice and
  Audio changes in v2026.8.1]]'
- '[[Changes/Raycast/2026-08-31-dictation-improved-connection-reliability-automatically-stops-when-leaving-a-cha|Dictation
  : Improved connection reliability, automatically stops when leaving…]]'
- '[[Changes/Krea/2026-09-01-reference-to-video-for-minimax-h3-max|Reference-to-video
  for MiniMax H3 Max]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: voice
title: 9 Voice and Audio changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Voice and Audio changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> v2026.8.2 adds a Home button to the Control UI that opens your personal Home agent beside whatever you are working on, instead of making you leave it to start another conversation. It also brings a Linux desktop companion, background sessions you can start without switching pages, browser control that can stay available without a running Gateway, four new looks for the Control UI, and a long tail of fixes for replies, voice, updates, and recovery.

> Doctor can now take explicit ownership of more offline repair work by stopping the matching managed Gateway, completing supported repairs, checking the result, and restarting the same service. It can recover supported legacy approvals and databases, preserve valid scheduled jobs and current Voice Call settings during migration, and explain which original material remains available when a repair cannot finish.

> Voice, media, and channel conversations now do a better job of reaching a clear ending and staying with the person and chat that started them. Spoken replies survive more delivery handoffs, calls and Browser Talk keep turns in order, attachments and plain text retain their intended shape, and account-specific failures no longer have to take every healthy channel down with them.

> Spoken replies now make it through more of the places where successful synthesis could previously disappear or be mistaken for an unfinished answer. Private Discord and Telegram replies can deliver one permitted built-in TTS voice note while keeping private final text hidden, long replies leave internal reasoning and known tool-status text out of the audio, and delivered speech can finish the turn without a misleading warning or an unnecessary second request.

> Speech created during Code Mode, Tool Search, or Codex work also has a clearer path into the final reply, while audio that finishes only after the request has timed out stays withheld.

> Voice Call now drops an obsolete automatic answer when the caller starts speaking again, and an old call stream can no longer disrupt the current reply. Late provider updates stay attached to the original call with its transcript, duration, and agent, while a failed first save no longer dials or consumes the only call slot, so restoring storage access is enough to try again.

> Affected AVI video and ASF or WMA audio also return to their existing playback-conversion paths instead of falling back as unsupported.

> Voice and transcription settings now reach the service they were meant for more consistently. OpenRouter and DeepInfra speech honor the configured voice, Voice Call and Talk can find eligible configured providers, Talk clients can use advertised transcription models, and TTS personas can use credentials stored through SecretRefs without borrowing another provider's key.

> For multilingual voice notes, leaving the language unset now uses automatic language detection without inserting an English instruction into the transcript. xAI transcription can accept silence as an empty result and continue to a configured fallback, while private or self-hosted xAI setups can use their configured address for voice discovery and buffered speech.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-01 · Krea · [[Changes/Krea/2026-09-01-reference-to-video-for-minimax-h3-max|Reference-to-video for MiniMax H3 Max]]
- Later: 2026-09-01 · Synthesia · [[Changes/Synthesia/2026-09-01-browse-featured-voices-filter-by-language-or-accent-and-preview-instantly-all-in|Find the right voice faster with the refreshed voice picker]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-1a83bd&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-9-voice-and-audio-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-1a83bd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->