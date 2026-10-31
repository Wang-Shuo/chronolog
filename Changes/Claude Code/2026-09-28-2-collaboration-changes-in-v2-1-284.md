---
card_id: claude-code-2026-09-28-6b0356
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Collaboration: 2 changes in v2.1.284 — Changed
  retries after a dropped connection mid-response to share one budget with the rest
  of…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1223
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39df8efcae8c9144ca1ff63fd2c925492fc43fb210bf3dad906a9b414308465f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-6b0356
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 2 Collaboration changes'
  evidence:
  - quote: Changed retries after a dropped connection mid-response to share one budget
      with the rest of the request's retries, so a failing request gives up sooner
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed artifact publishing to refuse a file on a network share (a `\\host\share`
      path or a `/net` automount) unless it is on a mapped network drive added with
      `--add-dir`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-collaboration-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: collaboration
  title: 2 Collaboration changes in v2.1.284
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-09-library-sharing-lets-you-share-files-and-folders-in-chatgpt-choose-who-can-acces|Library
  sharing lets you share files and folders in ChatGPT, choose who can access…]]'
- '[[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed
  /ultrareview in non-interactive sessions to refuse when the repository has…]]'
- '[[Changes/Cursor/2026-09-23-team-rules|Team rules]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: collaboration
title: 2 Collaboration changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Collaboration changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed retries after a dropped connection mid-response to share one budget with the rest of the request's retries, so a failing request gives up sooner

> Changed artifact publishing to refuse a file on a network share (a `\\host\share` path or a `/net` automount) unless it is on a mapped network drive added with `--add-dir`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Agent Mode
- [[Changes/Claude Code/2026-09-28-claude-tag-improved-notify-members-now-in-admin-settings-one-press-reaches-every|Claude Tag Improved "Notify members now" in admin settings]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-28-added-effortslider-decreaseeffort-increaseeffort-and-toggleultracode-keybinding|Added effortSlider:decreaseEffort, increaseEffort and toggleUltracode…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-improved-auto-memory-loading-invisible-characters-and-tags-that-imitate-claude-c|Improved auto-memory loading]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]] · Pricing Model
- [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]] · Account and Access
- [[Changes/Claude Code/2026-09-28-improved-startup-time-and-memory-use-by-building-only-the-parts-of-the-settings|Improved startup time and memory use by building only the parts of the settings…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-team-rules|Team rules]]
- Later: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-your-chatgpt-profile-now-brings-together-your-bio-activity-and-sites-you-choose-09d5dd|Share your profile and showcase your Sites]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-6b0356&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-2-collaboration-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-6b0356%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->