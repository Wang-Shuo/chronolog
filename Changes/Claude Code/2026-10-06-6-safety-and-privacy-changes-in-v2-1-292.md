---
card_id: claude-code-2026-10-06-14eec8
date: '2026-10-06'
description: 'Claude Code · 2026-10-06 · Safety and Privacy: 6 changes in v2.1.292
  — Security: Fixed PreToolUse hook approvals and auto mode bypassing the permission
  prompt…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1269
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3f7554b02c3a3da4bfeab3dccf54083c20a15cdc257714e17863f63f5de1ebfa
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-06-14eec8
  comparison: ''
  date: '2026-10-06'
  description: 'Claude Code — v2.1.292: 6 Safety and Privacy changes'
  evidence:
  - quote: 'Security: Fixed PreToolUse hook approvals and auto mode bypassing the
      permission prompt for file reads from network (UNC) paths'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Fixed "instruction file not loaded" lines going stale or missing after
      `/cd` or a permission change, and added a transcript line when a nested one
      isn't loaded
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Fixed cloud sessions with a large transcript sometimes asking for a permission
      again after it was approved
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Fixed tool calls made while the plugin hooks worker restarts being answered
      without the plugins' permission hooks
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved sandbox auto-allow: with strict sandbox mode set in user, managed
      or --settings settings, an interpreter command with an env var prefix like `FOO=bar
      python3 app.py` runs unprompted'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: '[Claude Tag] Fixed a session hanging until interrupted when a permission
      prompt that can''t be answered from Slack was denied automatically'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-292
  source_release: claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.292
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety
  and Privacy changes in v2.1.287]]'
- '[[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety
  and Privacy changes in v2.1.288]]'
- '[[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety
  and Privacy changes in v2.1.290]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.292
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.292

**Claude Code** · 2026-10-06 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) · from [[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Security: Fixed PreToolUse hook approvals and auto mode bypassing the permission prompt for file reads from network (UNC) paths

> Fixed "instruction file not loaded" lines going stale or missing after `/cd` or a permission change, and added a transcript line when a nested one isn't loaded

> Fixed cloud sessions with a large transcript sometimes asking for a permission again after it was approved

> Fixed tool calls made while the plugin hooks worker restarts being answered without the plugins' permission hooks

> Improved sandbox auto-allow: with strict sandbox mode set in user, managed or --settings settings, an interpreter command with an env var prefix like `FOO=bar python3 app.py` runs unprompted

> [Claude Tag] Fixed a session hanging until interrupted when a permission prompt that can't be answered from Slack was denied automatically

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-06-improved-rendering-speed-of-long-bulleted-or-numbered-replies-they-stream-resize|Improved rendering speed of long bulleted or numbered replies]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-06-added-prompt-autocomplete-an-event-a-mod-hooks-to-add-its-own-rows-to-the-prompt|Added prompt.autocomplete, an event a mod hooks to add its own rows to the prompt…]] · Editor Experience
- [[Changes/Claude Code/2026-10-06-2-developer-workflow-changes-in-v2-1-292|2 Developer Workflow changes in v2.1.292]] · Developer Workflow
- [[Changes/Claude Code/2026-10-06-claude-tag-added-an-edit-button-to-the-allowed-domains-card-on-a-channel-s-confi|Claude Tag Added an Edit button to the Allowed domains card on a channel's…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-06-improved-the-focus-tip-it-now-invites-you-to-try-focus-view-mid-turn-and-shows-h|Improved the /focus tip]] · Interface Experience
- [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]] · Model Support
- [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Agent Mode
- [[Changes/Claude Code/2026-10-06-8-other-changes-in-v2-1-292|8 other changes in v2.1.292]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-06-14eec8&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-06-6-safety-and-privacy-changes-in-v2-1-292.md%0ACard%20ID%3A%20claude-code-2026-10-06-14eec8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.292%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->