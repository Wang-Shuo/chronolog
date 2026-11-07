---
card_id: openclaw-2026-10-22-0e73af
date: '2026-10-22'
description: 'OpenClaw · 2026-10-22 · Automation and Scheduling: 5 changes in v2026.10.6
  — Updates now stop if they can’t confirm which Gateway is running. Stop it through…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2591
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7a4a1ed35d369b401147ec5529f58b761ab7736f332dbba09f03b777d7ebdd91
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-22-0e73af
  comparison: ''
  date: '2026-10-22'
  description: 'OpenClaw — v2026.10.6: 5 Automation and Scheduling changes'
  evidence:
  - quote: Updates now stop if they can’t confirm which Gateway is running. Stop it
      through Task Scheduler, the terminal you started it from, or openclaw gateway
      stop , then retry. See update commands .
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Local-model automations now alert you after two skipped runs instead of
      silently staying unavailable. Existing opt-outs still apply.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: IMAP automations now move on to later mail when one message can’t be read.
      The unreadable message is kept. See IMAP automations .
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: To clear a scheduled job’s pinned Gateway target, an operator can run openclaw
      cron edit <id> --tools exec . This replaces the whole tool list, so include
      every tool the job still needs. See scheduled-command target recovery .
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: /btw , /side , and /loop now keep multiline input. Loop names stay on one
      line.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 5-automation-and-scheduling-changes-in-v2026-10-6
  source_release: openclaw-2026-10-22-v2026-10-6-56379f53
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 5 Automation and Scheduling changes in v2026.10.6
  type: change
related_changes:
- '[[Changes/Cursor/2026-10-20-channels|Channels]]'
- '[[Changes/OpenHands/2026-10-20-feat-home-dismiss-recommended-automations-rail-from-home-and-application-setting|feat(home):
  dismiss recommended automations rail from Home and Application settings]]'
- '[[Changes/Google Antigravity/2026-10-22-the-conversations-palette-cmd-p-on-macos-ctrl-p-on-windows-and-linux-now-include|The
  Conversations palette (Cmd+P on macOS, Ctrl+P on Windows and Linux) now includes…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|openclaw-2026-10-22-v2026-10-6-56379f53]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 5 Automation and Scheduling changes in v2026.10.6
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Automation and Scheduling changes in v2026.10.6

**OpenClaw** · 2026-10-22 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.6) · from [[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|v2026.10.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Updates now stop if they can’t confirm which Gateway is running. Stop it through Task Scheduler, the terminal you started it from, or openclaw gateway stop , then retry. See update commands .

> Local-model automations now alert you after two skipped runs instead of silently staying unavailable. Existing opt-outs still apply.

> IMAP automations now move on to later mail when one message can’t be read. The unreadable message is kept. See IMAP automations .

> To clear a scheduled job’s pinned Gateway target, an operator can run openclaw cron edit \<id> --tools exec . This replaces the whole tool list, so include every tool the job still needs. See scheduled-command target recovery .

> /btw , /side , and /loop now keep multiline input. Loop names stay on one line.

Source: https://docs.openclaw.ai/releases/2026.10.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-22-shell-completion-now-finds-global-flags-after-subcommands-regenerate-your-saved|Shell completion now finds global flags after subcommands]] · Editor Experience
- [[Changes/OpenClaw/2026-10-22-3-agent-mode-changes-in-v2026-10-6|3 Agent Mode changes in v2026.10.6]] · Agent Mode
- [[Changes/OpenClaw/2026-10-22-4-model-support-changes-in-v2026-10-6|4 Model Support changes in v2026.10.6]] · Model Support
- [[Changes/OpenClaw/2026-10-22-security-release-v2026-10-6-adds-remediations-for-the-emudhra-certificate-compro|Security release: v2026.10.6 adds remediations for the eMudhra certificate compromise]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-22-restarting-the-same-official-docker-container-no-longer-copies-all-its-saved-sta|Restarting the same official Docker container no longer copies all its saved state…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-22-7-developer-workflow-changes-in-v2026-10-6|7 Developer Workflow changes in v2026.10.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-22-linux-camera-discovery-now-reports-an-unreadable-device-folder-as-an-error-inste|Linux camera discovery now reports an unreadable device folder as an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-22-web-search-timeout-errors-now-tell-you-the-request-s-actual-time-limit-see-web-t|Web search timeout errors now tell you the request’s actual time limit]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-22-3-voice-and-audio-changes-in-v2026-10-6|3 Voice and Audio changes in v2026.10.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-22-session-share-now-shows-an-error-when-it-can-t-discover-receivers-instead-of-an|Session Share now shows an error when it can’t discover receivers, instead…]] · Collaboration
- [[Changes/OpenClaw/2026-10-22-2-mobile-and-desktop-changes-in-v2026-10-6|2 Mobile and Desktop changes in v2026.10.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-22-10-apps-and-integrations-changes-in-v2026-10-6|10 Apps and Integrations changes in v2026.10.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-22-2-enterprise-and-administration-changes-in-v2026-10-6|2 Enterprise and Administration changes in v2026.10.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context Window changes in v2026.10.6]] · Context Window
- [[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP sign-in errors now give a safe reason and tell you how to sign in or fix…]] · Account and Access
- [[Changes/OpenClaw/2026-10-22-4-memory-and-personalization-changes-in-v2026-10-6|4 Memory and Personalization changes in v2026.10.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-22-you-can-now-stop-a-gateway-that-has-been-stuck-starting-for-more-than-five-minut|Stop a Gateway that has been stuck starting for more than five minutes without ever…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-you-can-now-find-a-claude-code-conversation-by-its-exact-session-id-even-when-th|Find a Claude Code conversation by its exact session ID even when the normal search…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-60-other-changes-in-v2026-10-6|60 other changes in v2026.10.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-22 · Google Antigravity · [[Changes/Google Antigravity/2026-10-22-the-conversations-palette-cmd-p-on-macos-ctrl-p-on-windows-and-linux-now-include|The Conversations palette (Cmd+P on macOS, Ctrl+P on Windows and Linux) now includes…]]
- Later: 2026-10-22 · OpenHands · [[Changes/OpenHands/2026-10-22-refactor-automations-express-the-activity-track-height-in-css-by-enyst-in-https|refactor(automations): express the activity track height in CSS]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-22-0e73af&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-22-5-automation-and-scheduling-changes-in-v2026-10-6.md%0ACard%20ID%3A%20openclaw-2026-10-22-0e73af%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->