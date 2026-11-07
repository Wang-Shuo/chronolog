---
card_id: openclaw-2026-06-30-48bc8f
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Collaboration: 5 changes in v2026.6.11 — When
  people switch between Telegram and another OpenClaw client in a shared direct…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2727
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35e1a4537bd99c9ad71860e8d5a058e5b25656861803b638b1126d6ce785b243
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-48bc8f
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 5 Collaboration changes'
  evidence:
  - quote: 'When people switch between Telegram and another OpenClaw client in a shared
      direct conversation, short Telegram replies now follow the latest conversation
      instead of responding to an older, unrelated Telegram proposal. #95390 Related
      #95378 . Thanks @maiduy708, @mikasa0818, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Nextcloud Talk bots now ignore ordinary file-share and lifecycle events
      without logging them as bot errors or risking disabled delivery, while malformed
      chat payloads still return an error. #96243 Related #81566 . Thanks @arkyu2077,
      @rafaelmgbh, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Gateway status, doctor, and restart diagnostics now retain recent restart
      details in OpenClaw's shared state database, while expired or malformed records
      are still discarded. a39a3b7 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: OpenClaw now keeps config recovery markers, last-known-good snapshots,
      and suspicious-read history in its shared state through migration, without leaving
      a separate config-health log file behind. 6daabd2 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Moves session and runtime internals behind shared maintenance boundaries.
      #89912 , #90439 , #96182 , #96191 , #96193 , #96195 , #96204 , #96206 , #96213
      , #96218 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 5-collaboration-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: collaboration
  title: 5 Collaboration changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-30-marketplace-access-by-organization-group-a2cf9b|Marketplace
  access by organization group]]'
- '[[Changes/Cursor/2026-06-30-we-ve-expanded-team-marketplaces-to-support-team-mcps-and-organization-groups|Cursor
  expands team marketplaces to support Team MCPs and organization groups]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration
  changes in v1.0.66]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: collaboration
title: 5 Collaboration changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Collaboration changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> When people switch between Telegram and another OpenClaw client in a shared direct conversation, short Telegram replies now follow the latest conversation instead of responding to an older, unrelated Telegram proposal. #95390 Related #95378 . Thanks @maiduy708, @mikasa0818, @obviyus.

> Nextcloud Talk bots now ignore ordinary file-share and lifecycle events without logging them as bot errors or risking disabled delivery, while malformed chat payloads still return an error. #96243 Related #81566 . Thanks @arkyu2077, @rafaelmgbh, @vincentkoc.

> Gateway status, doctor, and restart diagnostics now retain recent restart details in OpenClaw's shared state database, while expired or malformed records are still discarded. a39a3b7 Thanks @vincentkoc.

> OpenClaw now keeps config recovery markers, last-known-good snapshots, and suspicious-read history in its shared state through migration, without leaving a separate config-health log file behind. 6daabd2 Thanks @vincentkoc.

> Moves session and runtime internals behind shared maintenance boundaries. #89912 , #90439 , #96182 , #96191 , #96193 , #96195 , #96204 , #96206 , #96213 , #96218 Thanks @jalehman.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]]
- Later: 2026-07-01 · Notion · [[Changes/Notion/2026-07-01-your-agents-shouldn-t-be-stuck-in-one-off-chats-now-you-can-bring-multiple-agent|Your agents shouldn’t be stuck in one-off chats]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-48bc8f&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-5-collaboration-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-48bc8f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->