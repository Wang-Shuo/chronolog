---
card_id: claude-code-2026-04-09-4cb6c4
date: '2026-04-09'
description: 'Claude Code · 2026-04-09 · Editor Experience: 2 changes in v2.1.98 —
  Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail
  on…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1122
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f9f8b47c599db14f77f429c4b3c99cbe8daa38bd05ff0b2671cbc1c848260f6a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-09-4cb6c4
  comparison: ''
  date: '2026-04-09'
  description: 'Claude Code — v2.1.98: 2 Editor Experience changes'
  evidence:
  - quote: 'Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit
      fail on read-only files with a `p4 edit` hint instead of silently overwriting
      them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Improved Accept Edits mode to auto-approve filesystem commands prefixed
      with safe env vars or process wrappers
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-editor-experience-changes-in-v2-1-98
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: editor-experience
  title: 2 Editor Experience changes in v2.1.98
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-02-agent-tabs-in-the-editor|Agent Tabs in the Editor]]'
- '[[Changes/Claude Code/2026-04-04-removed-vim-command-toggle-vim-mode-via-config-editor-mode|Removed
  /vim command (toggle vim mode via /config → Editor mode)]]'
- '[[Changes/Claude Code/2026-04-08-4-editor-experience-changes-in-v2-1-97|4 Editor
  Experience changes in v2.1.97]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
theme: editor-experience
title: 2 Editor Experience changes in v2.1.98
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Editor Experience changes in v2.1.98

**Claude Code** · 2026-04-09 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.98) · from [[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them

> Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe env vars or process wrappers

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-09-fixed-false-bash-permission-prompts-for-cut-d-paste-d-column-s-awk-print-1-file|Fixed false Bash permission prompts for cut -d /, paste -d /, column -s /…]] · Pricing Model
- [[Changes/Claude Code/2026-04-09-6-safety-and-privacy-changes-in-v2-1-98|6 Safety and Privacy changes in v2.1.98]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-09-fixed-a-memory-leak-where-remote-control-permission-handler-entries-were-retaine|Fixed a memory leak where Remote Control permission handler entries were retained…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-09-6-developer-workflow-changes-in-v2-1-98|6 Developer Workflow changes in v2.1.98]] · Developer Workflow
- [[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|Added interactive Google Vertex AI setup wizard accessible from the login screen…]] · Account and Access
- [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Agent Mode
- [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]] · Context Window
- [[Changes/Claude Code/2026-04-09-3-other-changes-in-v2-1-98|3 other changes in v2.1.98]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-04-08 · Claude Code · [[Changes/Claude Code/2026-04-08-4-editor-experience-changes-in-v2-1-97|4 Editor Experience changes in v2.1.97]]
- Later: 2026-04-13 · Cursor · [[Changes/Cursor/2026-04-13-3-editor-experience-changes-in-3-1|3 Editor Experience changes in 3.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-09-4cb6c4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-09-2-editor-experience-changes-in-v2-1-98.md%0ACard%20ID%3A%20claude-code-2026-04-09-4cb6c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.98%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->