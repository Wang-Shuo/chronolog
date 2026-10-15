---
card_id: claude-code-2026-03-20-d05f5d
date: '2026-03-20'
description: 'Claude Code · 2026-03-20 · Developer Workflow: Added `--bare` flag for
  scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks;
  requires…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1098
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 0b4a982184451335371dd3194173f8890a0d23139d607f77d6d9a6c473f42b92
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-20-d05f5d
  comparison: ''
  date: '2026-03-20'
  description: 'Claude Code — v2.1.81: Added `--bare` flag for scripted `-p` calls
    — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY`
    or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory
    fully disabled'
  evidence:
  - quote: Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin
      sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper`
      via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc
  source_release: claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - plugin
    score: 50
    theme: apps-integrations
  - matched_terms:
    - lsp
    score: 50
    theme: developer-workflow
  theme_resolution: manual-backfill-review-v1
  title: Added `--bare` flag for scripted `-p` calls
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|Added
  worktree.sparsePaths setting for claude --worktree in large monorepos…]]'
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal
  notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]'
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|Resuming
  a session that was in a worktree now switches back to that worktree]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe]]'
source_type: github_releases
theme: developer-workflow
title: Added --bare flag for scripted -p calls
type: change
---

<!-- chronolog:begin region="header" -->
# Added `--bare` flag for scripted `-p` calls

**Claude Code** · 2026-03-20 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.81) · from [[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|v2.1.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-20-added-channels-permission-relay-channel-servers-that-declare-the-permission-capa|Added --channels permission relay]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-20-improved-mcp-read-search-tool-calls-to-collapse-into-a-single-queried-server-lin|Improved MCP read/search tool calls to collapse into a single…]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|Fixed unnecessary permission prompts for Bash commands containing dashes in strings]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|Resuming a session that was in a worktree now switches back to that worktree]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|Added WorktreeCreate hook support for type: "http"]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-20-d05f5d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc.md%0ACard%20ID%3A%20claude-code-2026-03-20-d05f5d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->