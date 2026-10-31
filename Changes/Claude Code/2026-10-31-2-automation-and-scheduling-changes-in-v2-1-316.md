---
card_id: claude-code-2026-10-31-214d4d
date: '2026-10-31'
description: 'Claude Code · 2026-10-31 · Automation and Scheduling: 2 changes in v2.1.316
  — Added `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP` to keep system…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2025-12-17-tasks-let-you-set-up-automated-prompts-that-chatgpt-can-run-for-you-you-can-now-b3f799|Tasks
    let you set up automated prompts that ChatGPT can run for you]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 318
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9ca1d5b1c7a38f953b99428f4ed8430859aee809342bdb630eef136a5a8ef65e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-31-214d4d
  comparison: ''
  date: '2026-10-31'
  description: 'Claude Code — v2.1.316: 2 Automation and Scheduling changes'
  evidence:
  - quote: Added `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP` to keep system cross-certificates
      that certify each other in a loop, for servers whose private CA needs one
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  - quote: Changed auto mode so that an `autoMode.allow` list without `"$defaults"`
      no longer removes the built-in rule on scheduled-task prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-automation-and-scheduling-changes-in-v2-1-316
  source_release: claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9
  source_type: github_releases
  theme: automation-scheduling
  title: 2 Automation and Scheduling changes in v2.1.316
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed
  Ctrl+C at the idle prompt of an attached background session to leave…]]'
- '[[Changes/Cursor/2026-10-20-channels|Channels]]'
- '[[Changes/ChatGPT/2026-10-27-icloud-users-can-now-connect-mail-and-calendar-to-chatgpt-to-find-emails-catch-u|iCloud
  users can now connect Mail and Calendar to ChatGPT to find emails, catch up…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9|claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9]]'
source_type: github_releases
theme: automation-scheduling
title: 2 Automation and Scheduling changes in v2.1.316
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Automation and Scheduling changes in v2.1.316

**Claude Code** · 2026-10-31 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) · from [[Releases/Claude Code/claude-code-2026-10-31-v2-1-316-github-429617179-a30f32c9|v2.1.316]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP` to keep system cross-certificates that certify each other in a loop, for servers whose private CA needs one

> Changed auto mode so that an `autoMode.allow` list without `"$defaults"` no longer removes the built-in rule on scheduled-task prompts

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.316
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-31-7-apps-and-integrations-changes-in-v2-1-316|7 Apps and Integrations changes in v2.1.316]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-31-2-developer-workflow-changes-in-v2-1-316|2 Developer Workflow changes in v2.1.316]] · Developer Workflow
- [[Changes/Claude Code/2026-10-31-vscode-added-sign-in-to-a-claude-apps-gateway-from-the-chat-panel-with-no-termin|VSCode Added sign-in to a Claude apps gateway from the chat panel, with no…]] · Account and Access
- [[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated fast mode for Opus 4.8 as of October 30, 2026]] · Model Support
- [[Changes/Claude Code/2026-10-31-2-agent-mode-changes-in-v2-1-316|2 Agent Mode changes in v2.1.316]] · Agent Mode
- [[Changes/Claude Code/2026-10-31-2-editor-experience-changes-in-v2-1-316|2 Editor Experience changes in v2.1.316]] · Editor Experience
- [[Changes/Claude Code/2026-10-31-2-enterprise-and-administration-changes-in-v2-1-316|2 Enterprise and Administration changes in v2.1.316]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-31-2-other-changes-in-v2-1-316|2 other changes in v2.1.316]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-27 · ChatGPT · [[Changes/ChatGPT/2026-10-27-icloud-users-can-now-connect-mail-and-calendar-to-chatgpt-to-find-emails-catch-u|iCloud users can now connect Mail and Calendar to ChatGPT to find emails, catch up…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2025-12-17 · ChatGPT · [[Changes/ChatGPT/2025-12-17-tasks-let-you-set-up-automated-prompts-that-chatgpt-can-run-for-you-you-can-now-b3f799|Tasks let you set up automated prompts that ChatGPT can run for you]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-31-214d4d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-31-2-automation-and-scheduling-changes-in-v2-1-316.md%0ACard%20ID%3A%20claude-code-2026-10-31-214d4d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.316%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->