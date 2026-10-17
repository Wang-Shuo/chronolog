---
card_id: claude-code-2026-09-17-218842
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Other changes: 8 changes in v2.1.274 — Added
  `claude_code.managed_settings_resolved` OTel event: managed-settings sources and
  policy…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0c6c0c3a90294367d06271e5066b7d83edcf213573372f3503d010114c150454
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-218842
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: 8 other changes'
  evidence:
  - quote: 'Added `claude_code.managed_settings_resolved` OTel event: managed-settings
      sources and policy helper state; redacted settings and digests with `OTEL_LOG_MANAGED_SETTINGS=1`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved artifact publishing: a publish built on an older version is stopped
      before it is sent, with the newer page to merge'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved `OTEL_LOG_RAW_API_BODIES=file:<dir>` output: a new `index.jsonl`
      and `request_body_id` / `message.id` event attributes link each response to
      its request file and transcript message'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Changed artifact watching in local sessions: a new version published elsewhere
      no longer starts a turn; Claude learns of it from a later Artifact tool result'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Changed the `/status` GitHub line to read "Cloud sessions", and `/web-setup`,
      `/ultrareview`, and teleport messages to say "cloud session" instead of "Claude
      Code on the web"
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[VSCode] Added continuation of the step a window reload interrupted, labeled
      in the chat, with a Claude Code: Continue After Reload setting to turn it off'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[Claude Code on the web] Changed routines to skip a run and retry for
      up to 72 hours when the owner''s GitHub connection is missing, instead of switching
      the routine off at the first failed check'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[Claude Tag] Added a Guests setting to the Add channel and Add workspace
      forms in Claude Tag admin settings, so owners can pick Inherit, Allow, Channel
      only or Restrict up front'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-other-changes-in-v2-1-274
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v2.1.274
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v2.1.274
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v2.1.274

**Claude Code** · 2026-09-17 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude_code.managed_settings_resolved` OTel event: managed-settings sources and policy helper state; redacted settings and digests with `OTEL_LOG_MANAGED_SETTINGS=1`

> Improved artifact publishing: a publish built on an older version is stopped before it is sent, with the newer page to merge

> Improved `OTEL_LOG_RAW_API_BODIES=file:<dir>` output: a new `index.jsonl` and `request_body_id` / `message.id` event attributes link each response to its request file and transcript message

> Changed artifact watching in local sessions: a new version published elsewhere no longer starts a turn; Claude learns of it from a later Artifact tool result

> Changed the `/status` GitHub line to read "Cloud sessions", and `/web-setup`, `/ultrareview`, and teleport messages to say "cloud session" instead of "Claude Code on the web"

> [VSCode] Added continuation of the step a window reload interrupted, labeled in the chat, with a Claude Code: Continue After Reload setting to turn it off

> [Claude Code on the web] Changed routines to skip a run and retry for up to 72 hours when the owner's GitHub connection is missing, instead of switching the routine off at the first failed check

> [Claude Tag] Added a Guests setting to the Add channel and Add workspace forms in Claude Tag admin settings, so owners can pick Inherit, Allow, Channel only or Restrict up front

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved Claude apps gateway sign-in rate limit errors]] · Account and Access
- [[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support changes in v2.1.274]] · Model Support
- [[Changes/Claude Code/2026-09-17-claude-code-on-the-web-changed-a-routine-s-on-hold-notice-when-your-subscription|Claude Code on the web Changed a routine's on-hold notice]] · Pricing Model
- [[Changes/Claude Code/2026-09-17-added-enduser-sub-the-idp-subject-to-the-telemetry-claude-desktop-and-cowork-sen|Added enduser.sub, the IdP subject, to the telemetry Claude Desktop and Cowork…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-vscode-improved-screen-reader-navigation-of-the-conversation-each-message-is-ann|VSCode Improved screen reader navigation of the conversation]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-17-7-developer-workflow-changes-in-v2-1-274|7 Developer Workflow changes in v2.1.274]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-vscode-added-a-claudecode-lockeditorgroups-setting-to-stop-claude-from-locking-t|VSCode Added a claudeCode.lockEditorGroups setting to stop Claude from locking…]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]] · Files and Data
- [[Changes/Claude Code/2026-09-17-2-interface-experience-changes-in-v2-1-274|2 Interface Experience changes in v2.1.274]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-218842&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-8-other-changes-in-v2-1-274.md%0ACard%20ID%3A%20claude-code-2026-09-17-218842%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->