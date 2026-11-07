---
card_id: openclaw-2026-09-01-510121
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Safety and Privacy: 7 changes in v2026.8.2 —
  On iPhone, model, effort, permission, context, attachment, skill, connector, and
  tool…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1234
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: edbb6681b6578739177d4a3a334cbd1ba6b3e3d9bd0e826bdfd0121e6449a12f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-510121
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 7 Safety and Privacy changes'
  evidence:
  - quote: On iPhone, model, effort, permission, context, attachment, skill, connector,
      and tool controls now live in the composer when the connected Gateway and operator
      access support them. Queued messages stay bound to the settings that were reviewed
      before sending, older or stale queue entries stop for review, and Control UI
      prompts keep one visible identity through preparation, completion, and reload.
      Selecting text can open an editable side-chat draft without adding the side
      question to the main history.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Browser Talk now waits for microphone permission before opening its connection
      and explains what it is waiting for instead of appearing stuck. Once the conversation
      begins, spoken questions and answers stay in order when transcription arrives
      late, a transcription failure can be shown without closing the call, and interrupting
      a Google Live response no longer ends the next turn by mistake.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Skill Workshop can also reject or quarantine a malformed proposal without
      trusting its draft, while actions that would revise, evaluate, or apply that
      content still fail closed. That makes disposal possible when a proposal is missing,
      altered, oversized, or linked somewhere unsafe without turning the recovery
      path into permission to use it.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Longer-running work is easier to steer without losing track of who owns
      it. Supported active tasks can accept permission changes, human approvals and
      corrections move ahead of agent-to-agent traffic, Stop catches more selected
      child work, and scheduled jobs report the outcome that actually settled instead
      of treating dispatch alone as success.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Supported native and Codex work can now take a permission change from the
      Control UI while it is active. The interface shows that the change is being
      applied, closes old approvals, and keeps the conversation in place instead of
      making you manually stop and continue the task.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Browser control can stay available through a paired local relay on supported
      macOS and Linux builds even when the Gateway is not running, while managed pages
      expose useful controls sooner. Cloud and remote work can reuse prepared projects,
      stop and clean up more deliberately, recover edits after a restart, and report
      failed sandbox or worker stages more clearly.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Remote sandboxes running on supported Python 3.9 environments now preserve
      complete file and attachment bytes, while guarded HTTP 308 redirects from Codex
      sandbox requests keep their request body and the existing destination checks.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-safety-and-privacy-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed
  remote and scheduled sessions failing…]]'
- '[[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety
  and Privacy changes in v2.1.257]]'
- '[[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227
  Use compatible PowerShell for elevated Windows sandbox commands @copyberry]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 7 Safety and Privacy changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On iPhone, model, effort, permission, context, attachment, skill, connector, and tool controls now live in the composer when the connected Gateway and operator access support them. Queued messages stay bound to the settings that were reviewed before sending, older or stale queue entries stop for review, and Control UI prompts keep one visible identity through preparation, completion, and reload. Selecting text can open an editable side-chat draft without adding the side question to the main history.

> Browser Talk now waits for microphone permission before opening its connection and explains what it is waiting for instead of appearing stuck. Once the conversation begins, spoken questions and answers stay in order when transcription arrives late, a transcription failure can be shown without closing the call, and interrupting a Google Live response no longer ends the next turn by mistake.

> Skill Workshop can also reject or quarantine a malformed proposal without trusting its draft, while actions that would revise, evaluate, or apply that content still fail closed. That makes disposal possible when a proposal is missing, altered, oversized, or linked somewhere unsafe without turning the recovery path into permission to use it.

> Longer-running work is easier to steer without losing track of who owns it. Supported active tasks can accept permission changes, human approvals and corrections move ahead of agent-to-agent traffic, Stop catches more selected child work, and scheduled jobs report the outcome that actually settled instead of treating dispatch alone as success.

> Supported native and Codex work can now take a permission change from the Control UI while it is active. The interface shows that the change is being applied, closes old approvals, and keeps the conversation in place instead of making you manually stop and continue the task.

> Browser control can stay available through a paired local relay on supported macOS and Linux builds even when the Gateway is not running, while managed pages expose useful controls sooner. Cloud and remote work can reuse prepared projects, stop and clean up more deliberately, recover edits after a restart, and report failed sandbox or worker stages more clearly.

> Remote sandboxes running on supported Python 3.9 environments now preserve complete file and attachment bytes, while guarded HTTP 308 redirects from Codex sandbox requests keep their request body and the existing destination checks.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
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
## Nearby in Safety and Privacy

- Earlier: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]]
- Later: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-core-apply-patch-no-longer-emits-an-empty-move-path-in-permission-metadata|Core apply_patch no longer emits an empty move path in permission metadata]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-510121&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-510121%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->