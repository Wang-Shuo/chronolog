---
card_id: claude-code-2026-09-29-fc2f9f
date: '2026-09-29'
description: 'Claude Code · 2026-09-29 · Developer Workflow: 3 changes in v2.1.285
  — Changed background Bash and PowerShell commands to stop after a time limit (their…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2940
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8bd1406d855733ff477ad5732c10f998bf41d580aa161c6de4369dab631b7bbd
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-29-fc2f9f
  comparison: ''
  date: '2026-09-29'
  description: 'Claude Code — v2.1.285: 3 Developer Workflow changes'
  evidence:
  - quote: Changed background Bash and PowerShell commands to stop after a time limit
      (their `timeout` with `run_in_background`, default 30 min, max 2 h); Claude
      is notified when one is stopped
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed Code Review's pull request reviews and `/ultrareview` to run when
      `disableWorkflows` is on, unless the machine running the review has it set by
      its own administrator (MDM or the managed-settings file)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: '[Code Review] Improved the Code Review check run to say when your repository''s
      REVIEW.md wasn''t applied, for example on a very large pull request or when
      REVIEW.md is a symbolic link'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-285
  source_release: claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.285
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-28-3-developer-workflow-changes-in-v1-0-89|3
  Developer Workflow changes in v1.0.89]]'
- '[[Changes/Google Antigravity/2026-09-28-terminal-command-steps-in-the-conversation-now-stay-collapsed-by-default-while-r|Terminal
  command steps in the conversation now stay collapsed by default…]]'
- '[[Changes/OpenCode/2026-09-28-core-debug-configuration-output-now-redacts-credentials-and-sensitive-headers|Core
  Debug configuration output now redacts credentials and sensitive headers]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.285
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.285

**Claude Code** · 2026-09-29 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) · from [[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed background Bash and PowerShell commands to stop after a time limit (their `timeout` with `run_in_background`, default 30 min, max 2 h); Claude is notified when one is stopped

> Changed Code Review's pull request reviews and `/ultrareview` to run when `disableWorkflows` is on, unless the machine running the review has it set by its own administrator (MDM or the managed-settings file)

> [Code Review] Improved the Code Review check run to say when your repository's REVIEW.md wasn't applied, for example on a very large pull request or when REVIEW.md is a symbolic link

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Context Window
- [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Pricing Model
- [[Changes/Claude Code/2026-09-29-6-mobile-and-desktop-changes-in-v2-1-285|6 Mobile and Desktop changes in v2.1.285]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-29-improved-responsiveness-when-leaving-the-ctrl-o-transcript-view-in-long-sessions|Improved responsiveness when leaving the ctrl+o transcript view in long sessions…]] · Interface Experience
- [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Model Support
- [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac|Fixed the PowerShell tool's permission check skipping deny and ask rules…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]] · Account and Access
- [[Changes/Claude Code/2026-09-29-2-editor-experience-changes-in-v2-1-285|2 Editor Experience changes in v2.1.285]] · Editor Experience
- [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Agent Mode
- [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-29-10-other-changes-in-v2-1-285|10 other changes in v2.1.285]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-28 · OpenCode · [[Changes/OpenCode/2026-09-28-core-debug-configuration-output-now-redacts-credentials-and-sensitive-headers|Core Debug configuration output now redacts credentials and sensitive headers]]
- Later: 2026-09-29 · Codex CLI · [[Changes/Codex CLI/2026-09-29-5-developer-workflow-changes-in-rust-v0-159-0|5 Developer Workflow changes in rust-v0.159.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-29-fc2f9f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-29-3-developer-workflow-changes-in-v2-1-285.md%0ACard%20ID%3A%20claude-code-2026-09-29-fc2f9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.285%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->