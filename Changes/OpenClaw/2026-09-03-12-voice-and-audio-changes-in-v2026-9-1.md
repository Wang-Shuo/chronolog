---
card_id: openclaw-2026-09-03-0dcb0a
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Voice and Audio: 12 changes in v2026.9.1 — The
  composer is less fragile around the edges of an active turn. You can begin the next…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2978
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 361ee6b8e17a72355e0a17a331961db2f2a9792e968a9fa642efb76876566342
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-0dcb0a
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 12 Voice and Audio changes'
  evidence:
  - quote: The composer is less fragile around the edges of an active turn. You can
      begin the next prompt immediately after sending, remove queued input without
      a false storage warning, keep late dictation after pressing Stop, and reply
      to attachment-only messages with a useful reference. Sent images remain visible
      while history takes ownership of them, Office attachment failures no longer
      wedge later turns through known display blocks, and silent command failures
      or plugin-delayed final replies still leave timely, visible progress or warning
      text.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Messaging in channels is less about whether a reply was technically sent
      and more about whether it arrived in the right conversation with its context,
      controls, and final outcome intact. This release carries that work across approvals,
      thread routing, rich replies, queues, restarts, voice, and the failure paths
      that used to leave either the person or the operator guessing.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Discord follows the same final-outcome discipline in several focused paths.
      Cancelled voice consults remain quiet, model-picker choices report their real
      result, and ambient or message-tool-only work does not leak a session-busy warning
      that its reply policy said to suppress.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Discord voice capture now has one owner per speaker and stops oversized
      batch utterances with an actionable warning instead of accumulating memory or
      sending a partial transcript. For inbound WhatsApp voice notes, Codex dynamic
      replies can once again return voice when automatic inbound TTS is enabled, while
      later text-only turns remain text and the audio decision stays attached to the
      reply that received it.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The native apps take two visible steps forward in this release. Android
      gets a much fuller everyday workspace for chat, sessions, navigation, and appearance,
      while Android, iPhone and iPad , and macOS can turn Mermaid source into readable
      diagrams inside the conversation. Around those larger changes, reconnects hold
      on to accepted work, voice stays with the turn that started it, and several
      platform-specific setup and helper paths handle failure more cleanly.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Talk and realtime voice now carry the acknowledged agent, run, and reply
      through the clients involved in the conversation, which keeps a consult on the
      intended agent, prevents an unrelated newer chat reply from being read back,
      and makes Stop target the work that actually started. Host cancellation is also
      reported as cancellation instead of a tool failure while the voice call remains
      open.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: On Apple Watch, dictated messages, spoken replies, playback, and retries
      remain attached to their original chat, and a spoken reply that outlasts the
      Watch’s wait points the user back to Chat on iPhone. Android offers an explicit
      voice-note recording path when on-device dictation is unavailable without discarding
      the draft, while macOS reuses a compatible speech recognizer, keeps the Talk
      overlay visible through a quick toggle, and packages the resources required
      by local MLX speech. The recognizer change removes one source of avoidable churn,
      but it does not establish that the broader open Apple speech-service memory
      report is fully fixed.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: macOS onboarding now brings failed AI setup, rejected-key details, and
      the retry action back into view instead of leaving someone stranded between
      setup and chat. Once inside chat, a cleaner two-row composer keeps context,
      model, effort, voice, send, attachment, branch, and verbosity controls reachable
      in narrow windows without duplicating model and usage details in the toolbar.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Provider choice now carries more cleanly into the tools around a conversation.
      Native Model Studio and Qwen routes honor prompt-cache retention, a selected
      web-fetch provider no longer trips over credentials for providers it never intended
      to use, and Local CLI speech generation follows the request timeout. Corrupted
      Volcengine speech responses fail clearly, while eligible OpenAI OAuth accounts
      can again transcribe inbound voice notes and configured batch audio without
      a separate API key. OAuth entitlement and quota are still account-specific,
      and custom Model Studio proxies remain opt-in for cache markers.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Voice Call setup now catches a missing response owner before telephony
      resources start on a multi-agent installation and points directly to plugins.entries.voice-call.config.agentId
      . Single-agent and explicitly owned setups keep their existing behavior, while
      affected multi-agent operators need to rerun setup and restart the Gateway after
      choosing the owner.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Voice Call diagnostic commands now stream large custom logs with backpressure,
      follow rotation and truncation more carefully, and honor whether SQLite history
      should start with retained records or only new ones. Feishu document actions
      also stop counting rejected access grants or image replacements as successes,
      while retaining a document that was created successfully and continuing with
      later images after one replacement fails.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Optional command implementations for memory-wiki, policy, QA Lab, and Voice
      Call now load only when their command is selected, while bundled web-search
      providers keep executable runtime code unloaded until OpenClaw chooses one.
      Activation planning reuses prepared alias work as well, but those component
      improvements do not establish a universal or end-to-end Gateway startup speedup.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-voice-and-audio-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: voice
  title: 12 Voice and Audio changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-02-you-can-now-send-a-message-with-the-send-button-while-dictation-is-still-running|Send
  a message with the send button while dictation is still running, instead…]]'
- '[[Changes/Ollama/2026-09-02-gemma4-now-supports-images-and-audio-on-mlx-engine|gemma4
  now supports images and audio on MLX engine]]'
- '[[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice
  and Audio changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: voice
title: 12 Voice and Audio changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Voice and Audio changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The composer is less fragile around the edges of an active turn. You can begin the next prompt immediately after sending, remove queued input without a false storage warning, keep late dictation after pressing Stop, and reply to attachment-only messages with a useful reference. Sent images remain visible while history takes ownership of them, Office attachment failures no longer wedge later turns through known display blocks, and silent command failures or plugin-delayed final replies still leave timely, visible progress or warning text.

> Messaging in channels is less about whether a reply was technically sent and more about whether it arrived in the right conversation with its context, controls, and final outcome intact. This release carries that work across approvals, thread routing, rich replies, queues, restarts, voice, and the failure paths that used to leave either the person or the operator guessing.

> Discord follows the same final-outcome discipline in several focused paths. Cancelled voice consults remain quiet, model-picker choices report their real result, and ambient or message-tool-only work does not leak a session-busy warning that its reply policy said to suppress.

> Discord voice capture now has one owner per speaker and stops oversized batch utterances with an actionable warning instead of accumulating memory or sending a partial transcript. For inbound WhatsApp voice notes, Codex dynamic replies can once again return voice when automatic inbound TTS is enabled, while later text-only turns remain text and the audio decision stays attached to the reply that received it.

> The native apps take two visible steps forward in this release. Android gets a much fuller everyday workspace for chat, sessions, navigation, and appearance, while Android, iPhone and iPad , and macOS can turn Mermaid source into readable diagrams inside the conversation. Around those larger changes, reconnects hold on to accepted work, voice stays with the turn that started it, and several platform-specific setup and helper paths handle failure more cleanly.

> Talk and realtime voice now carry the acknowledged agent, run, and reply through the clients involved in the conversation, which keeps a consult on the intended agent, prevents an unrelated newer chat reply from being read back, and makes Stop target the work that actually started. Host cancellation is also reported as cancellation instead of a tool failure while the voice call remains open.

> On Apple Watch, dictated messages, spoken replies, playback, and retries remain attached to their original chat, and a spoken reply that outlasts the Watch’s wait points the user back to Chat on iPhone. Android offers an explicit voice-note recording path when on-device dictation is unavailable without discarding the draft, while macOS reuses a compatible speech recognizer, keeps the Talk overlay visible through a quick toggle, and packages the resources required by local MLX speech. The recognizer change removes one source of avoidable churn, but it does not establish that the broader open Apple speech-service memory report is fully fixed.

> macOS onboarding now brings failed AI setup, rejected-key details, and the retry action back into view instead of leaving someone stranded between setup and chat. Once inside chat, a cleaner two-row composer keeps context, model, effort, voice, send, attachment, branch, and verbosity controls reachable in narrow windows without duplicating model and usage details in the toolbar.

> Provider choice now carries more cleanly into the tools around a conversation. Native Model Studio and Qwen routes honor prompt-cache retention, a selected web-fetch provider no longer trips over credentials for providers it never intended to use, and Local CLI speech generation follows the request timeout. Corrupted Volcengine speech responses fail clearly, while eligible OpenAI OAuth accounts can again transcribe inbound voice notes and configured batch audio without a separate API key. OAuth entitlement and quota are still account-specific, and custom Model Studio proxies remain opt-in for cache markers.

> Voice Call setup now catches a missing response owner before telephony resources start on a multi-agent installation and points directly to plugins.entries.voice-call.config.agentId . Single-agent and explicitly owned setups keep their existing behavior, while affected multi-agent operators need to rerun setup and restart the Gateway after choosing the owner.

> Voice Call diagnostic commands now stream large custom logs with backpressure, follow rotation and truncation more carefully, and honor whether SQLite history should start with retained records or only new ones. Feishu document actions also stop counting rejected access grants or image replacements as successes, while retaining a document that was created successfully and continuing with later images after one replacement fails.

> Optional command implementations for memory-wiki, policy, QA Lab, and Voice Call now load only when their command is selected, while bundled web-search providers keep executable runtime code unloaded until OpenClaw chooses one. Activation planning reuses prepared alias work as well, but those component improvements do not establish a universal or end-to-end Gateway startup speedup.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-5-voice-and-audio-changes-in-rust-v0-153-0|5 Voice and Audio changes in rust-v0.153.0]]
- Later: 2026-09-04 · HeyGen · [[Changes/HeyGen/2026-09-04-template-controls|Template controls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-0dcb0a&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-12-voice-and-audio-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-0dcb0a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->