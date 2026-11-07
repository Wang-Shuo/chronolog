---
card_id: openclaw-2026-10-12-10c54a
date: '2026-10-12'
description: 'OpenClaw · 2026-10-12 · Memory and Personalization: 4 changes in v2026.10.2
  — Leftover migration files. Doctor can archive old sender lists for removed channel…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 809bec331d7827d33eab19139d2343e9b87ff7a65899f705e8b83f3ce78b7ea6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-12-10c54a
  comparison: ''
  date: '2026-10-12'
  description: 'OpenClaw — v2026.10.2: 4 Memory and Personalization changes'
  evidence:
  - quote: 'Leftover migration files. Doctor can archive old sender lists for removed
      channel accounts and continue repairs. Memory-indexing lock files also stop
      triggering repeated recovery warnings for a healthy database. Damaged files
      for configured accounts and genuine recovery holds still need attention; see
      the migration guide . #167651 , #166517 , thanks to @steipete , @oshunter and
      @noelff .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Memory recall through Tool Search. Supported memory searches through Tool
      Search no longer fail when an agent asks for a score cutoff or a limit on results.
      #158632 , thanks to @masatohoshino , @obviyus and @he-yufeng .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Codex model discovery cleanup. Timed-out model discovery releases abandoned
      background processes while active sibling work can finish, preventing that source
      of accumulating memory use. Later work can start a replacement; see Codex recovery
      guidance . #168365 , thanks to @steipete and @609NFT .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'File and console logs. Masking secrets in file logs and JSON console output
      uses less temporary memory, with the same masking rules and output. #167943
      , thanks to @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-memory-and-personalization-changes-in-v2026-10-2
  source_release: openclaw-2026-10-12-v2026-10-2-9abf70fc
  source_type: openclaw_changelog
  theme: memory
  title: 4 Memory and Personalization changes in v2026.10.2
  type: change
related_changes:
- '[[Changes/Raycast/2026-10-09-2-memory-and-personalization-changes-in-raycast-macos-2-7|2
  Memory and Personalization changes in Raycast macos 2.7]]'
- '[[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2
  Memory and Personalization changes in v0.12.0]]'
- '[[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13
  Memory and Personalization changes in v2026.10.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|openclaw-2026-10-12-v2026-10-2-9abf70fc]]'
source_type: openclaw_changelog
theme: memory
title: 4 Memory and Personalization changes in v2026.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in v2026.10.2

**OpenClaw** · 2026-10-12 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.2) · from [[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|v2026.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Leftover migration files. Doctor can archive old sender lists for removed channel accounts and continue repairs. Memory-indexing lock files also stop triggering repeated recovery warnings for a healthy database. Damaged files for configured accounts and genuine recovery holds still need attention; see the migration guide . #167651 , #166517 , thanks to @steipete , @oshunter and @noelff .

> Memory recall through Tool Search. Supported memory searches through Tool Search no longer fail when an agent asks for a score cutoff or a limit on results. #158632 , thanks to @masatohoshino , @obviyus and @he-yufeng .

> Codex model discovery cleanup. Timed-out model discovery releases abandoned background processes while active sibling work can finish, preventing that source of accumulating memory use. Later work can start a replacement; see Codex recovery guidance . #168365 , thanks to @steipete and @609NFT .

> File and console logs. Masking secrets in file logs and JSON console output uses less temporary memory, with the same masking rules and output. #167943 , thanks to @steipete .

Source: https://docs.openclaw.ai/releases/2026.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-12-5-apps-and-integrations-changes-in-v2026-10-2|5 Apps and Integrations changes in v2026.10.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-12-older-session-history-doctor-can-continue-repairing-leftover-session-files-while|Older session history]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-12-2-pricing-model-changes-in-v2026-10-2|2 Pricing Model changes in v2026.10.2]] · Pricing Model
- [[Changes/OpenClaw/2026-10-12-9-model-support-changes-in-v2026-10-2|9 Model Support changes in v2026.10.2]] · Model Support
- [[Changes/OpenClaw/2026-10-12-4-context-window-changes-in-v2026-10-2|4 Context Window changes in v2026.10.2]] · Context Window
- [[Changes/OpenClaw/2026-10-12-dictation-holding-the-microphone-and-releasing-it-no-longer-stops-recording-prem|Dictation. Holding the microphone and releasing it no longer stops recording prematurely]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-12-managed-browser-tabs-at-the-shared-tab-limit-locally-managed-browser-cleanup-fav|Managed browser tabs]] · Editor Experience
- [[Changes/OpenClaw/2026-10-12-2-developer-workflow-changes-in-v2026-10-2|2 Developer Workflow changes in v2026.10.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-12-home-notifications-creating-many-chats-no-longer-fills-home-s-notification-queue|Home notifications]] · Collaboration
- [[Changes/OpenClaw/2026-10-12-manually-started-jobs-an-accepted-automation-can-keep-using-its-allowed-tools-af|Manually started jobs]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-12-5-agent-mode-changes-in-v2026-10-2|5 Agent Mode changes in v2026.10.2]] · Agent Mode
- [[Changes/OpenClaw/2026-10-12-2-mobile-and-desktop-changes-in-v2026-10-2|2 Mobile and Desktop changes in v2026.10.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin approval waits]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-12-summaries-before-completion-replies-when-a-long-conversation-needs-a-summary-ope|Summaries before completion replies]] · Interface Experience
- [[Changes/OpenClaw/2026-10-12-23-other-changes-in-v2026-10-2|23 other changes in v2026.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]]
- Later: 2026-10-12 · Raycast · [[Changes/Raycast/2026-10-12-cloud-sync-v2|Cloud Sync v2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-12-10c54a&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2.md%0ACard%20ID%3A%20openclaw-2026-10-12-10c54a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->