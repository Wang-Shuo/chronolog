---
card_id: claude-code-2026-09-28-dc51b2
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Other changes: 9 changes in v2.1.284 — Improved
  the "No such tool available" error for Claude in Chrome tools called without their…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 28fb5da19445b230c998d00cc8dff391898813b7274f34e94d3b0eb952250d01
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-dc51b2
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 9 other changes'
  evidence:
  - quote: 'Improved the "No such tool available" error for Claude in Chrome tools
      called without their prefix: it now names the tool to call'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Improved Monitor event rows to show what each event printed instead of
      repeating the description, and stopped repeating an unchanged "Waiting for N
      … to finish" line after every event
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved `/claude-api`: `hillclimb` no longer spends rounds on prompt
      rewordings too small for the eval to measure, and an extra page you ask for
      beside `report.html` is built as one local file that loads nothing from the
      network'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved artifact pages: Claude writes its design plan into the page instead
      of the reply, and uses the name you already gave something as the page title'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Improved the Artifact tool so that when Claude is given a claude.ai chat
      or project link, an artifact from a chat, or an artifact id on its own, it asks
      for the right link or the content instead of stopping
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[VSCode] Added an optional time above each prompt and response, with a
      date line where the day changes (Claude Code: Show Message Timestamps setting,
      off by default)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[VSCode] Changed `CLAUDE_CONFIG_DIR` in the `claudeCode.environmentVariables`
      setting to apply only when it is an absolute path, and passed it to terminals
      that continue the chat'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Added the spend that counts toward your organization-wide
      limit to the analytics spend projection chart, with how much of the limit is
      used'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Improved Claude''s wait notice on self-hosted environments
      with on-demand runners: it now says whether a runner is starting, a start will
      be retried, or no runner will start'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.284
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.284

**Claude Code** · 2026-09-28 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the "No such tool available" error for Claude in Chrome tools called without their prefix: it now names the tool to call

> Improved Monitor event rows to show what each event printed instead of repeating the description, and stopped repeating an unchanged "Waiting for N … to finish" line after every event

> Improved `/claude-api`: `hillclimb` no longer spends rounds on prompt rewordings too small for the eval to measure, and an extra page you ask for beside `report.html` is built as one local file that loads nothing from the network

> Improved artifact pages: Claude writes its design plan into the page instead of the reply, and uses the name you already gave something as the page title

> Improved the Artifact tool so that when Claude is given a claude.ai chat or project link, an artifact from a chat, or an artifact id on its own, it asks for the right link or the content instead of stopping

> [VSCode] Added an optional time above each prompt and response, with a date line where the day changes (Claude Code: Show Message Timestamps setting, off by default)

> [VSCode] Changed `CLAUDE_CONFIG_DIR` in the `claudeCode.environmentVariables` setting to apply only when it is an absolute path, and passed it to terminals that continue the chat

> [Claude Tag] Added the spend that counts toward your organization-wide limit to the analytics spend projection chart, with how much of the limit is used

> [Claude Tag] Improved Claude's wait notice on self-hosted environments with on-demand runners: it now says whether a runner is starting, a start will be retried, or no runner will start

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
- [[Changes/Claude Code/2026-09-28-2-collaboration-changes-in-v2-1-284|2 Collaboration changes in v2.1.284]] · Collaboration
- [[Changes/Claude Code/2026-09-28-improved-startup-time-and-memory-use-by-building-only-the-parts-of-the-settings|Improved startup time and memory use by building only the parts of the settings…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-dc51b2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-9-other-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-dc51b2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->