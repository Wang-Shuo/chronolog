---
card_id: claude-code-2026-09-17-96198c
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Developer Workflow: 7 changes in v2.1.274
  — Improved Artifact tool errors: when you are not signed in to claude.ai the terminal
  now…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1279
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ccea7713165a812fa733c472314dddf3ac938226a497b2b4eeb7f9623c4c482f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-96198c
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: 7 Developer Workflow changes'
  evidence:
  - quote: 'Improved Artifact tool errors: when you are not signed in to claude.ai
      the terminal now says so on the first attempt, and Claude is told to stop retrying
      a rejected call sooner'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Improved safety checks before removing an agent worktree that contains
      submodule checkouts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Changed `/code-review` to use leaner inline review prompts for every model
      that has no tuned settings of its own, instead of spawning many review subagents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Changed self-hosted runners to skip a read-only repository the git host
      refuses at the access check instead of failing the session start
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[VSCode] Changed the default global gitignore file to `$XDG_CONFIG_HOME/git/ignore`
      when `XDG_CONFIG_HOME` is an absolute path'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[Code Review] Improved how Code Review words each posted finding: short
      plain sentences that say who is affected, where the code goes wrong, and the
      fix up front'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[Code Review] Improved the check-run card and PR comment when a review
      is skipped because of an organization limit: each cause now links the admin
      page that fixes it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-developer-workflow-changes-in-v2-1-274
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in v2.1.274
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code
  Review Added a note under the still-open findings list in follow-up reviews]]'
- '[[Changes/Claude Code/2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi|Added
  OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events…]]'
- '[[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer
  Workflow changes in v2.1.273]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in v2.1.274
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in v2.1.274

**Claude Code** · 2026-09-17 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved Artifact tool errors: when you are not signed in to claude.ai the terminal now says so on the first attempt, and Claude is told to stop retrying a rejected call sooner

> Improved safety checks before removing an agent worktree that contains submodule checkouts

> Changed `/code-review` to use leaner inline review prompts for every model that has no tuned settings of its own, instead of spawning many review subagents

> Changed self-hosted runners to skip a read-only repository the git host refuses at the access check instead of failing the session start

> [VSCode] Changed the default global gitignore file to `$XDG_CONFIG_HOME/git/ignore` when `XDG_CONFIG_HOME` is an absolute path

> [Code Review] Improved how Code Review words each posted finding: short plain sentences that say who is affected, where the code goes wrong, and the fix up front

> [Code Review] Improved the check-run card and PR comment when a review is skipped because of an organization limit: each cause now links the admin page that fixes it

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
- [[Changes/Claude Code/2026-09-17-vscode-added-a-claudecode-lockeditorgroups-setting-to-stop-claude-from-locking-t|VSCode Added a claudeCode.lockEditorGroups setting to stop Claude from locking…]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]] · Files and Data
- [[Changes/Claude Code/2026-09-17-2-interface-experience-changes-in-v2-1-274|2 Interface Experience changes in v2.1.274]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-17-8-other-changes-in-v2-1-274|8 other changes in v2.1.274]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer Workflow changes in v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-96198c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-7-developer-workflow-changes-in-v2-1-274.md%0ACard%20ID%3A%20claude-code-2026-09-17-96198c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->