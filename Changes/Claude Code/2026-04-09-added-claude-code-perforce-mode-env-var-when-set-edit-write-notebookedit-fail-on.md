---
card_id: claude-code-2026-04-09-cbd468
date: '2026-04-09'
description: 'Claude Code · 2026-04-09 · Editor Experience: Added `CLAUDE_CODE_PERFORCE_MODE`
  env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|Instant
    fix all lint errors with AI 😎]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1122
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 9d28704999c3252cb81ebc129ee1dc3a7ff7ecd2e14660c89310c47c2634f7b0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-09-cbd468
  comparison: ''
  date: '2026-04-09'
  description: 'Claude Code — v2.1.98: Added `CLAUDE_CODE_PERFORCE_MODE` env var:
    when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint
    instead of silently overwriting them'
  evidence:
  - quote: 'Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit
      fail on read-only files with a `p4 edit` hint instead of silently overwriting
      them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-code-perforce-mode-env-var-when-set-edit-write-notebookedit-fail-on
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: editor-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Added `CLAUDE_CODE_PERFORCE_MODE` env var
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|Added
  .jj and .sl to VCS directory exclusion lists so Grep and file autocomplete…]]'
- '[[Changes/Cursor/2026-04-02-you-can-switch-back-to-the-ide-anytime-or-have-both-open-simultaneously|You
  can switch back to the IDE anytime, or have both open simultaneously]]'
- '[[Changes/Claude Code/2026-04-08-added-syntax-highlighting-for-cedar-policy-files-cedar-cedarpolicy|Added
  syntax highlighting for Cedar policy files (.cedar, .cedarpolicy)]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
theme: editor-experience
title: Added CLAUDE_CODE_PERFORCE_MODE env var
type: change
---

<!-- chronolog:begin region="header" -->
# Added `CLAUDE_CODE_PERFORCE_MODE` env var

**Claude Code** · 2026-04-09 · [[Themes/editor-experience|Editor Experience]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.98) · from [[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-09-added-monitor-tool-for-streaming-events-from-background-scripts|Added Monitor tool for streaming events from background scripts]] · Agent Mode
- [[Changes/Claude Code/2026-04-09-added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co|Added subprocess sandboxing with PID namespace isolation on Linux…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|Added interactive Google Vertex AI setup wizard accessible from the login screen…]] · Account and Access
- [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-04-08 · Claude Code · [[Changes/Claude Code/2026-04-08-added-syntax-highlighting-for-cedar-policy-files-cedar-cedarpolicy|Added syntax highlighting for Cedar policy files (.cedar, .cedarpolicy)]]
- Later: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-config-search-now-matches-option-values-e-g-searching-vim-finds-the-editor-mode|/config search now matches option values…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|Instant fix all lint errors with AI 😎]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-09-cbd468&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-09-added-claude-code-perforce-mode-env-var-when-set-edit-write-notebookedit-fail-on.md%0ACard%20ID%3A%20claude-code-2026-04-09-cbd468%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.98%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->