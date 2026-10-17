---
card_id: claude-code-2026-09-01-4e1cbc
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Developer Workflow: 3 changes in v2.1.257
  — Improved `/code-review --comment` to post findings on GitLab merge requests via
  `glab mr…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 804899ec1aa590ccfd4002183f1ad0838dc8fddf6f40a87e1b7b73572590de3e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-4e1cbc
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: 3 Developer Workflow changes'
  evidence:
  - quote: Improved `/code-review --comment` to post findings on GitLab merge requests
      via `glab mr note` instead of reporting the target as unsupported
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: Improved `claude self-hosted-runner --configure-git` to also enable git
      push negotiation, so the first push of a new branch from a stale clone uploads
      only the new commits instead of the whole tree
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  - quote: 'Improved `/fork` to keep the original conversation''s prompt cache in
      the new background session: its worktree briefing now arrives as a message instead
      of a system-prompt change'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-257
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.257
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed
  terminal hyperlinks in rendered markdown]]'
- '[[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed
  Anthropic telemetry export failures to log at debug level…]]'
- '[[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer
  Workflow changes in v2.1.251]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.257
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.257

**Claude Code** · 2026-09-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/code-review --comment` to post findings on GitLab merge requests via `glab mr note` instead of reporting the target as unsupported

> Improved `claude self-hosted-runner --configure-git` to also enable git push negotiation, so the first push of a new branch from a stale clone uploads only the new commits instead of the whole tree

> Improved `/fork` to keep the original conversation's prompt cache in the new background session: its worktree briefing now arrives as a message instead of a system-prompt change

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
- [[Changes/Claude Code/2026-09-01-7-other-changes-in-v2-1-257|7 other changes in v2.1.257]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]]
- Later: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-improved-terminal-resize-and-first-render-performance-for-long-responses-by-reus|Improved terminal resize and first-render performance for long responses by reusing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-4e1cbc&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-3-developer-workflow-changes-in-v2-1-257.md%0ACard%20ID%3A%20claude-code-2026-09-01-4e1cbc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->