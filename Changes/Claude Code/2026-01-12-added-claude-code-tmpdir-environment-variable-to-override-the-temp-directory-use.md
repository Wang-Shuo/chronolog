---
card_id: claude-code-2026-01-12-1e8817
date: '2026-01-12'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1031
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-09-added-clickable-hyperlinks-for-file-paths-in-tool-output-in-terminals-that-suppo|claude-code-2026-01-09-a78ee5]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 3fa13ac1e8b6d77c7c24b21ee859e9a316bc5e770f23ca0ff0e700d2bcc2fed8
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-09-improved-slash-command-suggestion-readability-by-truncating-long-descriptions-to|claude-code-2026-01-09-4d3b66]]'
- '[[Changes/Claude Code/2026-01-09-added-source-path-metadata-to-images-dragged-onto-the-terminal-helping-claude-un|claude-code-2026-01-09-88f6ef]]'
- '[[Changes/Claude Code/2026-01-09-added-clickable-hyperlinks-for-file-paths-in-tool-output-in-terminals-that-suppo|claude-code-2026-01-09-a78ee5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-12-v2-1-5-github-276118083-94c73a96|claude-code-2026-01-12-v2-1-5-github-276118083-94c73a96]]'
theme: developer-workflow
type: change
---

# Added `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory u

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory used for internal temp files, useful for environments with custom temp directory requirements
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory used for internal temp files, useful for environments with custom temp directory requirements
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.5
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-09-added-clickable-hyperlinks-for-file-paths-in-tool-output-in-terminals-that-suppo|claude-code-2026-01-09-a78ee5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1031
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes