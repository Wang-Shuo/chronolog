---
card_id: claude-code-2026-08-26-336f51
date: '2026-08-26'
description: 'Claude Code · 2026-08-26 · Other changes: 4 changes in v2.1.247 — Added
  the `SendFeedback` tool: when something goes wrong in a session, Claude can draft
  a…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 57d91af1df6f47ee8781e5caa50b1daabde5e96e50d5840ce62b9d23e95485e7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-26-336f51
  comparison: ''
  date: '2026-08-26'
  description: 'Claude Code — v2.1.247: 4 other changes'
  evidence:
  - quote: 'Added the `SendFeedback` tool: when something goes wrong in a session,
      Claude can draft a feedback report for you to review and send from `/feedback`
      (turn off with the `feedbackDrafts` setting)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Added `{id, text, cooldownSessions, priority}` entries, `tipsFile`, and
      `label` to `spinnerTipsOverride`, so organizations can rotate their own tips
      alongside the built-in ones
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Updated the `/claude-api` skill with Admin API coverage (organization members,
      invites, workspaces, API keys, rate limit reports, workload identity federation,
      CMEK)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: 'Changed cross-session peer messages to collapse by default to a one-line
      `Message from @<sender>: <first line>` preview; Ctrl+O expands the full body'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-other-changes-in-v2-1-247
  source_release: claude-code-2026-08-26-v2-1-247-github-377320078-fc507178
  source_type: github_releases
  theme: uncategorized
  title: 4 other changes in v2.1.247
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|claude-code-2026-08-26-v2-1-247-github-377320078-fc507178]]'
source_type: github_releases
theme: uncategorized
title: 4 other changes in v2.1.247
type: change
---

<!-- chronolog:begin region="header" -->
# 4 other changes in v2.1.247

**Claude Code** · 2026-08-26 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) · from [[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the `SendFeedback` tool: when something goes wrong in a session, Claude can draft a feedback report for you to review and send from `/feedback` (turn off with the `feedbackDrafts` setting)

> Added `{id, text, cooldownSessions, priority}` entries, `tipsFile`, and `label` to `spinnerTipsOverride`, so organizations can rotate their own tips alongside the built-in ones

> Updated the `/claude-api` skill with Admin API coverage (organization members, invites, workspaces, API keys, rate limit reports, workload identity federation, CMEK)

> Changed cross-session peer messages to collapse by default to a one-line `Message from @<sender>: <first line>` preview; Ctrl+O expands the full body

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] · Model Support
- [[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed terminal hyperlinks in rendered markdown]] · Developer Workflow
- [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-26-3-account-and-access-changes-in-v2-1-247|3 Account and Access changes in v2.1.247]] · Account and Access
- [[Changes/Claude Code/2026-08-26-changed-the-prompt-footer-pr-badge-to-skip-its-github-re-check-on-terminal-refoc|Changed the prompt-footer PR badge to skip its GitHub re-check on terminal refocus…]] · Interface Experience
- [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-26-336f51&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-26-4-other-changes-in-v2-1-247.md%0ACard%20ID%3A%20claude-code-2026-08-26-336f51%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.247%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->