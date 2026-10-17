---
card_id: claude-code-2026-10-05-f5e097
date: '2026-10-05'
description: 'Claude Code · 2026-10-05 · Model Support: 2 changes in v2.1.290 — Changed
  `/code-review` at medium effort to also report cleanup and CLAUDE.md conventions…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1365
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4295b5a5db7ce7bdca91431db7ccfba21724cc523bada68c9eaa2ee092696ce0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-f5e097
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: 2 Model Support changes'
  evidence:
  - quote: Changed `/code-review` at medium effort to also report cleanup and CLAUDE.md
      conventions findings on models without tuned review settings, including Opus
      5.5 and Sonnet 5.5
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  - quote: '[Claude Tag] Added fast mode in Slack: mention Claude with `!fast` to
      switch a thread to fast mode, moving it to Opus if needed, and `!fast off` to
      switch back; replies show (fast) while it''s on'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-290
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.290
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed
  how failed API requests are retried]]'
- '[[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support
  changes in v2.1.287]]'
- '[[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed
  the client-side auto mode classifier to ignore…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.290
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.290

**Claude Code** · 2026-10-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.290) · from [[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|v2.1.290]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed `/code-review` at medium effort to also report cleanup and CLAUDE.md conventions findings on models without tuned review settings, including Opus 5.5 and Sonnet 5.5

> [Claude Tag] Added fast mode in Slack: mention Claude with `!fast` to switch a thread to fast mode, moving it to Opus if needed, and `!fast off` to switch back; replies show (fast) while it's on

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-05-changed-background-sessions-waiting-on-a-scheduled-wakeup-loop-they-are-now-left|Changed background sessions waiting on a scheduled wakeup (/loop)]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added /claude-api managed-agents-onboard quickstart-name to build a Console…]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-3-account-and-access-changes-in-v2-1-290|3 Account and Access changes in v2.1.290]] · Account and Access
- [[Changes/Claude Code/2026-10-05-vscode-added-a-screen-reader-announcement-message-queued-when-you-send-a-message|VSCode Added a screen reader announcement, "Message queued.", when you send…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]] · Search and Browsing
- [[Changes/Claude Code/2026-10-05-14-apps-and-integrations-changes-in-v2-1-290|14 Apps and Integrations changes in v2.1.290]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]] · Agent Mode
- [[Changes/Claude Code/2026-10-05-5-developer-workflow-changes-in-v2-1-290|5 Developer Workflow changes in v2.1.290]] · Developer Workflow
- [[Changes/Claude Code/2026-10-05-changed-background-sessions-whose-scheduled-task-is-gone-they-now-move-to-comple|Changed background sessions whose scheduled task is gone]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-05-improved-responsiveness-while-resuming-large-sessions-timers-input-and-rendering|Improved responsiveness while resuming large sessions]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-changed-the-client-side-auto-mode-classifier-to-ignore-an-anthropic-default-sonn|Changed the client-side auto mode classifier to ignore…]]
- Later: 2026-10-06 · Claude Code · [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-05-f5e097&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-05-2-model-support-changes-in-v2-1-290.md%0ACard%20ID%3A%20claude-code-2026-10-05-f5e097%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.290%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->