---
card_id: claude-code-2026-07-17-690de7
date: '2026-07-17'
description: 'Claude Code · 2026-07-17 · Search and Browsing: 3 changes in v2.1.212
  — Added a session-wide limit on WebSearch tool calls (default 200, tunable via…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1212
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9ba1c6f44f48a29c717a44f4b44b97cace9c4b1a1d73c50ae4449ada643d64b4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-17-690de7
  comparison: ''
  date: '2026-07-17'
  description: 'Claude Code — v2.1.212: 3 Search and Browsing changes'
  evidence:
  - quote: Added a session-wide limit on WebSearch tool calls (default 200, tunable
      via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) to stop runaway search loops
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Improved web search and web fetch reliability by retrying 529 errors and
      rate-limited requests with bounded backoff
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  - quote: Changed bare `/btw` to reopen the side-question panel on your most recent
      exchange so you can browse earlier answers
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-search-and-browsing-changes-in-v2-1-212
  source_release: claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in v2.1.212
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-04-08-the-outlook-email-and-calendar-apps-for-chatgpt-can-now-help-with-delegated-or-s|Outlook
  shared mailboxes and calendars in ChatGPT]]'
- '[[Changes/Claude Code/2026-05-19-the-plugin-browse-and-discover-panes-now-show-when-a-plugin-was-last-updated|The
  /plugin browse and discover panes now show when a plugin was last updated]]'
- '[[Changes/ChatGPT/2026-06-01-chatgpt-can-now-help-with-more-of-the-job-search-process-from-finding-relevant-l|Find
  live jobs and format your resume in ChatGPT]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in v2.1.212
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v2.1.212

**Claude Code** · 2026-07-17 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) · from [[Releases/Claude Code/claude-code-2026-07-17-v2-1-212-github-355310036-d94b4e11|v2.1.212]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) to stop runaway search loops

> Improved web search and web fetch reliability by retrying 529 errors and rate-limited requests with bounded backoff

> Changed bare `/btw` to reopen the side-question panel on your most recent exchange so you can browse earlier answers

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.212
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]] · Agent Mode
- [[Changes/Claude Code/2026-07-17-typing-resume-in-the-agent-view-now-opens-a-picker-of-past-sessions-including-se|Typing /resume in the agent view now opens a picker of past sessions]] · Interface Experience
- [[Changes/Claude Code/2026-07-17-updated-the-auth-status-panel-title-from-cloud-authentication-to-authentication|Updated the auth status panel title from "Cloud authentication" to "Authentication"]] · Account and Access
- [[Changes/Claude Code/2026-07-17-2-apps-and-integrations-changes-in-v2-1-212|2 Apps and Integrations changes in v2.1.212]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]] · Model Support
- [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-17-corrected-an-earlier-release-note-2-1-200-tmux-through-the-3-6-series-lacks-sync|Corrected an earlier release note (2.1.200)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-06-01 · ChatGPT · [[Changes/ChatGPT/2026-06-01-chatgpt-can-now-help-with-more-of-the-job-search-process-from-finding-relevant-l|Find live jobs and format your resume in ChatGPT]]
- Later: 2026-07-22 · Claude Code · [[Changes/Claude Code/2026-07-22-changed-deep-research-to-start-only-when-invoked-manually-claude-no-longer-launc|Changed /deep-research to start only when invoked manually]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-17-690de7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-17-3-search-and-browsing-changes-in-v2-1-212.md%0ACard%20ID%3A%20claude-code-2026-07-17-690de7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.212%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->