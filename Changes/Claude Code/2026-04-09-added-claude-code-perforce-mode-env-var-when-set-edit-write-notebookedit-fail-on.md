---
card_id: claude-code-2026-04-09-cbd468
date: '2026-04-09'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1122
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 90d11d6a1b96a44a79b4fbb1bf7d41a2a15a6b61cb3de4ab5437c97ed3395229
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
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-code-perforce-mode-env-var-when-set-edit-write-notebookedit-fail-on
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: editor-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: 'Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit
    fai'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|claude-code-2026-03-27-833a57]]'
- '[[Changes/Cursor/2026-04-02-you-can-switch-back-to-the-ide-anytime-or-have-both-open-simultaneously|cursor-2026-04-02-ed78a6]]'
- '[[Changes/Claude Code/2026-04-08-added-syntax-highlighting-for-cedar-policy-files-cedar-cedarpolicy|claude-code-2026-04-08-dcfaa4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
theme: editor-experience
title: 'Added CLAUDE_CODE_PERFORCE_MODE env var: when set, Edit/Write/NotebookEdit
  fai'
type: change
---

# Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fai

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.98: Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PERFORCE_MODE` env var: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1122
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes