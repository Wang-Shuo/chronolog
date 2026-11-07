---
card_id: openclaw-2026-10-10-bc6dc2
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Voice and Audio: 8 changes in v2026.10.1 — Assistant
  replies can show playable YouTube cards , with start times and an external watch…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3015
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6bd812b0105e960692419f09af56fb59d9bc53ade47b4c0c36069da6db426a2b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-bc6dc2
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 8 Voice and Audio changes'
  evidence:
  - quote: Assistant replies can show playable YouTube cards , with start times and
      an external watch link when inline playback is unavailable. Thumbnails contact
      Google before you press Play. The Control UI also supports inline playback and
      seeking for allowed native local audio and video up to 4 GiB, subject to browser
      format support. Remote-workspace and channel limits stay unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Compatible memory plugins can bring their stored records into recall, Memory
      Wiki and realtime voice. With a native provider selected, OpenClaw checks access
      to private or conversation-specific memory, including what spawned agents inherit.
      Resetting or replacing the parent ends that inherited access, and status reports
      the selected provider's health separately from Memory Core.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Very old configurations and saved-data formats may need an intermediate
      release before this upgrade can proceed; refusals preserve the old files. Back
      up complete configuration, state and queue-owned media first. The documented
      configuration forms need 2026.9.5 Doctor ; Matrix's five retired files also
      need Matrix started once, and older flat layouts first need 2026.6 Doctor and
      Gateway startup . Retired outgoing/session JSON queues, cron files, encrypted
      OAuth sidecars, Voice Call logs and nested workspace setup files need 2026.9.7
      on the original host, then Doctor . Do not rename migrated queue artifacts to
      replay messages. Supported July routing aliases, supported JSON imports and
      current SQLite state remain supported. Follow state migrations , Matrix migrations
      and incoming-queue migration for the affected format.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Doctor gives eligible single-file Talk configurations their own saved provider
      settings, so later Voice Call edits do not change Talk. Configurations split
      across included files can lose inherited settings and need separate correction;
      see Talk migration . Supported command-approval policies also receive repair
      with a private original copy, but ordinary pre-Doctor exports can omit old command
      permissions or MCP grants. Run Doctor against the correct state directory before
      relying on an older-format export. Retired embedded session settings and shortcuts
      require backed-up manual correction; current Doctor does not repair them. Follow
      session-setting migrations .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Allowing a Discord parent channel lets the agent discover its active threads
      without a server-wide wildcard; explicit thread denies remain effective. Long
      model IDs retain the full selection through Submit; reopen /models if the catalog
      no longer resolves it. Voice joins and playback use elapsed time, so changing
      the system clock does not stretch or cut short that allowance.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Upgrading very old channel settings or data can require a bridge release.
      Keep a complete pre-update backup and follow the old-version upgrade guide .
      Retired Nextcloud Talk replay caches, Discord JSON preferences/bindings, Telegram
      sidecars and selected Matrix/Slack settings require the 2026.9.5 bridge. Retired
      Discord voice-TTS and guild-channel settings require 2026.9.7 Doctor. Migrate
      old Matrix JSON state before updating, and never run an older release against
      an already upgraded shared database. Very old Mattermost allowPrivateNetwork
      aliases lose their Doctor conversion; preserve the original configuration because
      a confirmed recovery path remains unresolved.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Background work and older files. Stopping or replacing a service cancels
      pending callbacks and waits for work already admitted after owner cleanup. Before
      this upgrade, migrate old Device Pair notify files, Discord model/thread files
      and iMessage reply, sent-echo or catchup files through 2026.9.5 and Doctor;
      Voice Call calls.jsonl needs 2026.9.7. Verify migration before backing up or
      moving the preserved originals and retrying. Standalone Voice Call keeps its
      webhook serving after printing a result; SIGINT or SIGTERM ends it and finishes
      cleanup.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Voice Call preserves recorded ownership and leaves old unowned active
      calls for provider-side hangup and a fresh call. #163118 . Thanks @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-voice-and-audio-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: voice
  title: 8 Voice and Audio changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Raycast/2026-10-09-2-voice-and-audio-changes-in-raycast-windows-2-7|2
  Voice and Audio changes in Raycast windows 2.7]]'
- '[[Changes/Wispr Flow/2026-10-09-meeting-recordings-recover-from-save-and-upload-errors-notetaker|Meeting
  recordings recover from save and upload errors (Notetaker)]]'
- '[[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice
  and Audio changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: voice
title: 8 Voice and Audio changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Voice and Audio changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Assistant replies can show playable YouTube cards , with start times and an external watch link when inline playback is unavailable. Thumbnails contact Google before you press Play. The Control UI also supports inline playback and seeking for allowed native local audio and video up to 4 GiB, subject to browser format support. Remote-workspace and channel limits stay unchanged.

> Compatible memory plugins can bring their stored records into recall, Memory Wiki and realtime voice. With a native provider selected, OpenClaw checks access to private or conversation-specific memory, including what spawned agents inherit. Resetting or replacing the parent ends that inherited access, and status reports the selected provider's health separately from Memory Core.

> Very old configurations and saved-data formats may need an intermediate release before this upgrade can proceed; refusals preserve the old files. Back up complete configuration, state and queue-owned media first. The documented configuration forms need 2026.9.5 Doctor ; Matrix's five retired files also need Matrix started once, and older flat layouts first need 2026.6 Doctor and Gateway startup . Retired outgoing/session JSON queues, cron files, encrypted OAuth sidecars, Voice Call logs and nested workspace setup files need 2026.9.7 on the original host, then Doctor . Do not rename migrated queue artifacts to replay messages. Supported July routing aliases, supported JSON imports and current SQLite state remain supported. Follow state migrations , Matrix migrations and incoming-queue migration for the affected format.

> Doctor gives eligible single-file Talk configurations their own saved provider settings, so later Voice Call edits do not change Talk. Configurations split across included files can lose inherited settings and need separate correction; see Talk migration . Supported command-approval policies also receive repair with a private original copy, but ordinary pre-Doctor exports can omit old command permissions or MCP grants. Run Doctor against the correct state directory before relying on an older-format export. Retired embedded session settings and shortcuts require backed-up manual correction; current Doctor does not repair them. Follow session-setting migrations .

> Allowing a Discord parent channel lets the agent discover its active threads without a server-wide wildcard; explicit thread denies remain effective. Long model IDs retain the full selection through Submit; reopen /models if the catalog no longer resolves it. Voice joins and playback use elapsed time, so changing the system clock does not stretch or cut short that allowance.

> Upgrading very old channel settings or data can require a bridge release. Keep a complete pre-update backup and follow the old-version upgrade guide . Retired Nextcloud Talk replay caches, Discord JSON preferences/bindings, Telegram sidecars and selected Matrix/Slack settings require the 2026.9.5 bridge. Retired Discord voice-TTS and guild-channel settings require 2026.9.7 Doctor. Migrate old Matrix JSON state before updating, and never run an older release against an already upgraded shared database. Very old Mattermost allowPrivateNetwork aliases lose their Doctor conversion; preserve the original configuration because a confirmed recovery path remains unresolved.

> Background work and older files. Stopping or replacing a service cancels pending callbacks and waits for work already admitted after owner cleanup. Before this upgrade, migrate old Device Pair notify files, Discord model/thread files and iMessage reply, sent-echo or catchup files through 2026.9.5 and Doctor; Voice Call calls.jsonl needs 2026.9.7. Verify migration before backing up or moving the preserved originals and retrying. Standalone Voice Call keeps its webhook serving after printing a result; SIGINT or SIGTERM ends it and finishes cleanup.

> Voice Call preserves recorded ownership and leaves old unowned active calls for provider-side hangup and a fresh call. #163118 . Thanks @steipete .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]]
- Later: 2026-10-12 · ElevenLabs · [[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-bc6dc2&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-8-voice-and-audio-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-bc6dc2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->