---
card_id: claude-code-2026-09-17-f16d05
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Safety and Privacy: 3 changes in v2.1.274
  — Fixed `claude agents` losing `--model`, `--effort`, `--permission-mode`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1250
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 41c7399819ce314746619357f80b2b5599370c74f13cfb4f0e594309ca296d64
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-f16d05
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed `claude agents` losing `--model`, `--effort`, `--permission-mode`,
      `--allow-dangerously-skip-permissions` and `--agent` after an auto-update relaunch
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Fixed Bash permission checks for commands that loop over or assign certain
      special shell variables; these commands now ask for permission
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Fixed the Edit permission prompt preview sometimes showing a different
      location than the approved edit in files with multi-byte characters
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-274
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.274
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety
  and Privacy changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety
  and Privacy changes in v2.1.273]]'
- '[[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety
  and Privacy changes in v2.1.275]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.274
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.274

**Claude Code** · 2026-09-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `claude agents` losing `--model`, `--effort`, `--permission-mode`, `--allow-dangerously-skip-permissions` and `--agent` after an auto-update relaunch

> Fixed Bash permission checks for commands that loop over or assign certain special shell variables; these commands now ask for permission

> Fixed the Edit permission prompt preview sometimes showing a different location than the approved edit in files with multi-byte characters

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
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-17-8-other-changes-in-v2-1-274|8 other changes in v2.1.274]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]]
- Later: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety and Privacy changes in v2.1.277]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-f16d05&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-3-safety-and-privacy-changes-in-v2-1-274.md%0ACard%20ID%3A%20claude-code-2026-09-17-f16d05%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->