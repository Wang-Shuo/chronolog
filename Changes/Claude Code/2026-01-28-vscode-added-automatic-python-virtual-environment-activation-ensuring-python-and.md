---
card_id: claude-code-2026-01-28-6a32ec
date: '2026-01-28'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1047
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-27-added-support-for-loading-claude-md-files-from-additional-directories-specified|claude-code-2026-01-27-c86065]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d4f9b6be70b635fd6c18e622e0635d00bd6cf5acd8686890d888b6134e5a038d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-23-changed-indexed-argument-syntax-from-arguments-0-to-arguments-0-bracket-syntax|claude-code-2026-01-23-48861a]]'
- '[[Changes/Claude Code/2026-01-23-added-shorthand-0-1-etc-for-accessing-individual-arguments-in-custom-commands|claude-code-2026-01-23-e3d862]]'
- '[[Changes/Claude Code/2026-01-27-added-support-for-loading-claude-md-files-from-additional-directories-specified|claude-code-2026-01-27-c86065]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-28-v2-1-21-github-280523920-bba74245|claude-code-2026-01-28-v2-1-21-github-280523920-bba74245]]'
theme: developer-workflow
type: change
---

# [VSCode] Added automatic Python virtual environment activation, ensuring `python

<!-- chronolog:begin region="description" -->
[VSCode] Added automatic Python virtual environment activation, ensuring `python` and `pip` commands use the correct interpreter (configurable via `claudeCode.usePythonEnvironment` setting)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [VSCode] Added automatic Python virtual environment activation, ensuring `python` and `pip` commands use the correct interpreter (configurable via `claudeCode.usePythonEnvironment` setting)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-27-added-support-for-loading-claude-md-files-from-additional-directories-specified|claude-code-2026-01-27-c86065]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1047
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes