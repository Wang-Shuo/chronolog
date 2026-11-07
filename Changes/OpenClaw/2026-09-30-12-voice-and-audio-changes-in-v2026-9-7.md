---
card_id: openclaw-2026-09-30-872554
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Voice and Audio: 12 changes in v2026.9.7 — You
  can steer active work even when an older message is waiting as a follow-up. People
  with…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 611c912be4a28ae5f3a3fc0047c6976e3e6be780162920f8a4a61567c65195b2
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-872554
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 12 Voice and Audio changes'
  evidence:
  - quote: You can steer active work even when an older message is waiting as a follow-up.
      People with the same permissions can also steer shared turns, including across
      devices using the same shared Owner token. Steering does not interrupt running
      tools and remains unavailable for Incognito and cloud-worker turns. A ready
      follow-up replaces Stop with Send, Queue, or Steer; clear the draft to bring
      Stop back. Stop remains available for drafts that cannot send, except during
      active dictation.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Browser Talk can continue through brief connection stalls and asks you
      to repeat speech if audio was dropped. The in-call voice dropdown has been removed.
      Set future-call defaults in Settings → Talk , or ask the assistant to change
      the current call’s voice. Native iOS and Android voice controls are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Talk, Discord, FaceTime, and Voice Call now guide the voice model to consult
      your agent about its other work when that option is available. This does not
      give the voice model direct access to other conversations. Talk also removes
      redundant confirmations for read-only Code Mode lookups, while keeping approvals
      for changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Voice Call's maxChars setting now limits profile files only, so total voice
      context can be longer.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Mac app brings the web conversation into its native window, while Apple
      chat adds document and audio attachments.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Apple chat can now attach documents and audio, including PDFs, Office files
      and ZIP archives. Use Attach , drag-and-drop or Finder paste on Mac, and + →
      File on iOS. Size limits still apply, and an oversized send keeps your draft.
      What the agent can read depends on the model.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Mac Voice Wake uses your edited transcript, and clearing the text cancels
      the request. Swabble now honors its configured minimum length and cooldown,
      so short commands may stop triggering hooks. The default minimum is 24 characters.
      An early partial transcript can trigger a hook and prevent its corrected final
      text from triggering another during the cooldown; manual test-hook remains exempt
      from the length limit.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: 'For dialogue, select a 3.8 speech model and configure exactly two voices
      , each with a distinct speaker name. Put the name and words on the same line,
      such as Puck: Hello , to choose that voice. Unrecognized labels are read aloud,
      and text without recognized labels uses the single-voice path.'
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Managed Linux desktop views now have an Unmute control for listening to
      application sound, including with view-only access. Audio starts muted, stops
      when you hide or disconnect the view, and stays muted after reconnecting. It
      carries no microphone audio, uses about 1.5 Mbit/s, and may not stay in sync
      with the picture.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If sound is unavailable, use the Audio unavailable control for setup help.
      Install pulseaudio and pulseaudio-utils , then restart the managed desktop.
      Successful setup replaces its existing PulseAudio route with a private output;
      failed setup leaves the old route in place without capturing it.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Meeting captions and saved transcripts can keep speaker labels and information
      about where each caption came from. Those labels help you follow the conversation
      but do not verify a speaker's identity. Transcript saving and lookup do less
      repeated work, and failed audio startup cleans up any output process it already
      started. The experimental Google Meet interface does not yet provide native
      chat, reactions, or hand raising.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Voice Call loads again on OpenClaw 2026.9.6. Optional identity and workspace
      context remains off unless you enable it on that version.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-voice-and-audio-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: voice
  title: 12 Voice and Audio changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Runway/2026-09-29-elevenlabs-v4-is-now-supported-in-runway-letting-you-generate-audio-with-the-lat|ElevenLabs
  V4]]'
- '[[Changes/Gemini/2026-09-30-let-skills-in-gemini-tackle-your-most-repetitive-tasks|Let
  skills in Gemini tackle your most repetitive tasks]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-holding-space-and-ctrl-x-v-explain-when-voice-mode-is-off-or-still-getting-ready|Holding
  Space and Ctrl+X V explain when voice mode is off or still getting ready]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: voice
title: 12 Voice and Audio changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Voice and Audio changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> You can steer active work even when an older message is waiting as a follow-up. People with the same permissions can also steer shared turns, including across devices using the same shared Owner token. Steering does not interrupt running tools and remains unavailable for Incognito and cloud-worker turns. A ready follow-up replaces Stop with Send, Queue, or Steer; clear the draft to bring Stop back. Stop remains available for drafts that cannot send, except during active dictation.

> Browser Talk can continue through brief connection stalls and asks you to repeat speech if audio was dropped. The in-call voice dropdown has been removed. Set future-call defaults in Settings → Talk , or ask the assistant to change the current call’s voice. Native iOS and Android voice controls are unchanged.

> Talk, Discord, FaceTime, and Voice Call now guide the voice model to consult your agent about its other work when that option is available. This does not give the voice model direct access to other conversations. Talk also removes redundant confirmations for read-only Code Mode lookups, while keeping approvals for changes.

> Voice Call's maxChars setting now limits profile files only, so total voice context can be longer.

> The Mac app brings the web conversation into its native window, while Apple chat adds document and audio attachments.

> Apple chat can now attach documents and audio, including PDFs, Office files and ZIP archives. Use Attach , drag-and-drop or Finder paste on Mac, and + → File on iOS. Size limits still apply, and an oversized send keeps your draft. What the agent can read depends on the model.

> Mac Voice Wake uses your edited transcript, and clearing the text cancels the request. Swabble now honors its configured minimum length and cooldown, so short commands may stop triggering hooks. The default minimum is 24 characters. An early partial transcript can trigger a hook and prevent its corrected final text from triggering another during the cooldown; manual test-hook remains exempt from the length limit.

> For dialogue, select a 3.8 speech model and configure exactly two voices , each with a distinct speaker name. Put the name and words on the same line, such as Puck: Hello , to choose that voice. Unrecognized labels are read aloud, and text without recognized labels uses the single-voice path.

> Managed Linux desktop views now have an Unmute control for listening to application sound, including with view-only access. Audio starts muted, stops when you hide or disconnect the view, and stays muted after reconnecting. It carries no microphone audio, uses about 1.5 Mbit/s, and may not stay in sync with the picture.

> If sound is unavailable, use the Audio unavailable control for setup help. Install pulseaudio and pulseaudio-utils , then restart the managed desktop. Successful setup replaces its existing PulseAudio route with a private output; failed setup leaves the old route in place without capturing it.

> Meeting captions and saved transcripts can keep speaker labels and information about where each caption came from. Those labels help you follow the conversation but do not verify a speaker's identity. Transcript saving and lookup do less repeated work, and failed audio startup cleans up any output process it already started. The experimental Google Meet interface does not yet provide native chat, reactions, or hand raising.

> Voice Call loads again on OpenClaw 2026.9.6. Optional identity and workspace context remains off unless you enable it on that version.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-holding-space-and-ctrl-x-v-explain-when-voice-mode-is-off-or-still-getting-ready|Holding Space and Ctrl+X V explain when voice mode is off or still getting ready]]
- Later: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-49073-surface-realtime-voice-catalog-failures-in-the-tui-etraut-openai|♯49073 Surface realtime voice catalog failures in the TUI @etraut-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-872554&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-12-voice-and-audio-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-872554%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->