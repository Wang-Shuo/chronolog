---
card_id: claude-code-2026-10-05-969d5d
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Search and Browsing: Changed the interactive
  session''s WebSearch budget to refill over time (100 calls/hour…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 8f07e2bcecf7b586b5116d59240677b843be8502069c80150a2cba471622cbf7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-969d5d
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: Changed the interactive session''s WebSearch
    budget to refill over time (100 calls/hour; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR`
    sets the rate, 0 turns it off) instead of ending after 200 calls'
  evidence:
  - quote: Changed the interactive session's WebSearch budget to refill over time
      (100 calls/hour; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` sets the rate, 0
      turns it off) instead of ending after 200 calls
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: search-browsing
  title: Changed the interactive session's WebSearch budget to refill over time (100
    calls/hour
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-10-box-dropbox-and-sharepoint-now-join-google-drive-in-chatgpt-library-once-connect|Box,
  Dropbox, and SharePoint now join Google Drive in ChatGPT Library]]'
- '[[Changes/Claude Code/2026-09-23-improved-deep-research-reliability-on-long-research-briefs-by-removing-unused-re|Improved
  /deep-research reliability on long research briefs by removing unused…]]'
- '[[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved
  SDK sessions so a message sent with priority "now" no longer cancels…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: search-browsing
title: Changed the interactive session's WebSearch budget to refill over time (100
  calls/hour
type: change
---

<!-- chronolog:begin region="header" -->
# Changed the interactive session's WebSearch budget to refill over time (100 calls/hour

**Claude Code** · 2026-10-05 · [[Themes/search-browsing|Search and Browsing]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed the interactive session's WebSearch budget to refill over time (100 calls/hour; `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` sets the rate, 0 turns it off) instead of ending after 200 calls
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-2-model-support-changes-in-v2-1-290|2 Model Support changes in v2.1.290]] · Model Support
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-05-18-other-changes-in-v2-1-290|18 other changes in v2.1.290]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-969d5d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls.md%0ACard%20ID%3A%20claude-code-2026-10-05-969d5d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->