---
card_id: claude-code-2026-04-09-97b58a
date: '2026-04-09'
description: 'Claude Code · 2026-04-09 · Developer Workflow: 6 changes in v2.1.98
  — Added `workspace.git_worktree` to the status line JSON input, set whenever the
  current…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1118
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d30253527294b7e7a404e73c0cf36558cb9685e1f3d3aa033f5b4de800303863
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-09-97b58a
  comparison: ''
  date: '2026-04-09'
  description: 'Claude Code — v2.1.98: 6 Developer Workflow changes'
  evidence:
  - quote: Added `workspace.git_worktree` to the status line JSON input, set whenever
      the current directory is inside a linked git worktree
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Added W3C `TRACEPARENT` env var to Bash tool subprocesses when OTEL tracing
      is enabled, so child-process spans correctly parent to Claude Code's trace tree
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: 'LSP: Claude Code now identifies itself to language servers via `clientInfo`
      in the initialize request'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Improved `/resume` filter hint labels and added project/worktree/branch
      names in the filter indicator
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Improved footer indicators (Focus, notifications) to stay on the mode-indicator
      row instead of wrapping at narrow terminal widths
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Improved hook errors in the transcript to include the first line of stderr
      for self-diagnosis without `--debug`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-developer-workflow-changes-in-v2-1-98
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v2.1.98
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-04-removed-tag-command|Removed /tag command]]'
- '[[Changes/Claude Code/2026-04-08-3-developer-workflow-changes-in-v2-1-97|3 Developer
  Workflow changes in v2.1.97]]'
- '[[Changes/Cursor/2026-04-08-bugbot-learned-rules-9e5cac|Bugbot Learned Rules]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v2.1.98
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v2.1.98

**Claude Code** · 2026-04-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.98) · from [[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `workspace.git_worktree` to the status line JSON input, set whenever the current directory is inside a linked git worktree

> Added W3C `TRACEPARENT` env var to Bash tool subprocesses when OTEL tracing is enabled, so child-process spans correctly parent to Claude Code's trace tree

> LSP: Claude Code now identifies itself to language servers via `clientInfo` in the initialize request

> Improved `/resume` filter hint labels and added project/worktree/branch names in the filter indicator

> Improved footer indicators (Focus, notifications) to stay on the mode-indicator row instead of wrapping at narrow terminal widths

> Improved hook errors in the transcript to include the first line of stderr for self-diagnosis without `--debug`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-09-fixed-false-bash-permission-prompts-for-cut-d-paste-d-column-s-awk-print-1-file|Fixed false Bash permission prompts for cut -d /, paste -d /, column -s /…]] · Pricing Model
- [[Changes/Claude Code/2026-04-09-6-safety-and-privacy-changes-in-v2-1-98|6 Safety and Privacy changes in v2.1.98]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-09-2-editor-experience-changes-in-v2-1-98|2 Editor Experience changes in v2.1.98]] · Editor Experience
- [[Changes/Claude Code/2026-04-09-fixed-a-memory-leak-where-remote-control-permission-handler-entries-were-retaine|Fixed a memory leak where Remote Control permission handler entries were retained…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|Added interactive Google Vertex AI setup wizard accessible from the login screen…]] · Account and Access
- [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Agent Mode
- [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-08 · Cursor · [[Changes/Cursor/2026-04-08-bugbot-learned-rules-9e5cac|Bugbot Learned Rules]]
- Later: 2026-04-13 · Claude Code · [[Changes/Claude Code/2026-04-13-2-developer-workflow-changes-in-v2-1-105|2 Developer Workflow changes in v2.1.105]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-09-97b58a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-09-6-developer-workflow-changes-in-v2-1-98.md%0ACard%20ID%3A%20claude-code-2026-04-09-97b58a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.98%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->