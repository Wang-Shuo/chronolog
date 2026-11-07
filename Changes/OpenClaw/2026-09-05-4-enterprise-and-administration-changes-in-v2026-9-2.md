---
card_id: openclaw-2026-09-05-6cf1e2
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Enterprise and Administration: 4 changes in
  v2026.9.2 — Successfully generated images remain visible when a later tool fails,
  and saved…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2426
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 704fb8582f966e35a736422365604fa21ed133bae0b43d44ac92cd1d828d074c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-6cf1e2
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 4 Enterprise and Administration changes'
  evidence:
  - quote: Successfully generated images remain visible when a later tool fails, and
      saved media replies keep one caption after reload. Project screenshots now follow
      the conversation's filesystem permissions, so a screenshot the session is allowed
      to use can also appear in chat. For a blocked image outside those folders, an
      administrator can inspect its path and choose Allow image for that file alone,
      with an expiring allowance and current access checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: An update now leaves a report you can return to after the connection drops
      and OpenClaw comes back. The update dialog follows the saved attempt, Settings
      → Updates reopens its latest report, and the CLI and chat use the same recorded
      steps, outcome, and verification results. Successful updates keep that detail
      too, so you do not have to reconstruct what happened from a disappearing notification.
      The update history guide covers openclaw update status and administrator history
      queries.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Deployment controllers that pause new work before maintenance can now explicitly
      hand an unfinished wait over to restart recovery. An administrator arms gateway.suspend.handoff
      for the exact suspended process, then the controller sends SIGTERM and owns
      launching the replacement. This gives managed deployments a supported way to
      interrupt eligible conversation work after their maintenance waiting period,
      without having two owners trying to restart the same Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Pairing requests identify the device and its requested access, show administrator
      warnings, and distinguish a capability update from replacing a device token.
      You can inspect full IDs and versions in Details or use Copy ID. Command-Return
      approves the displayed request once, while Return alone does not; Not Now or
      Escape on pairing requests leaves them pending. Always Allow Here remains available
      only when the command policy permits it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-enterprise-and-administration-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: enterprise-admin
  title: 4 Enterprise and Administration changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/HeyGen/2026-09-04-governance-for-admins|Governance for admins]]'
- '[[Changes/Lovable/2026-09-04-manage-and-protect-your-preview-links|Manage and protect
  your preview links]]'
- '[[Changes/Wispr Flow/2026-09-04-for-teams-enterprise-desktop|For Teams & Enterprise
  (Desktop)]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: enterprise-admin
title: 4 Enterprise and Administration changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Enterprise and Administration changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Successfully generated images remain visible when a later tool fails, and saved media replies keep one caption after reload. Project screenshots now follow the conversation's filesystem permissions, so a screenshot the session is allowed to use can also appear in chat. For a blocked image outside those folders, an administrator can inspect its path and choose Allow image for that file alone, with an expiring allowance and current access checks.

> An update now leaves a report you can return to after the connection drops and OpenClaw comes back. The update dialog follows the saved attempt, Settings → Updates reopens its latest report, and the CLI and chat use the same recorded steps, outcome, and verification results. Successful updates keep that detail too, so you do not have to reconstruct what happened from a disappearing notification. The update history guide covers openclaw update status and administrator history queries.

> Deployment controllers that pause new work before maintenance can now explicitly hand an unfinished wait over to restart recovery. An administrator arms gateway.suspend.handoff for the exact suspended process, then the controller sends SIGTERM and owns launching the replacement. This gives managed deployments a supported way to interrupt eligible conversation work after their maintenance waiting period, without having two owners trying to restart the same Gateway.

> Pairing requests identify the device and its requested access, show administrator warnings, and distinguish a capability update from replacing a device token. You can inspect full IDs and versions in Details or use Copy ID. Command-Return approves the displayed request once, while Return alone does not; Not Now or Escape on pairing requests leaves them pending. Always Allow Here remains available only when the command policy permits it.

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
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-09-04 · Wispr Flow · [[Changes/Wispr Flow/2026-09-04-for-teams-enterprise-desktop|For Teams & Enterprise (Desktop)]]
- Later: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-6cf1e2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-6cf1e2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->