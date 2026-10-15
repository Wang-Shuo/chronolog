---
card_id: claude-code-2026-03-27-358253
date: '2026-03-27'
description: 'Claude Code · 2026-03-27 · Developer Workflow: Added `X-Claude-Code-Session-Id`
  header to API requests so proxies can aggregate requests by session without…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: d5cde02c66f2ce5e1cab440556547237dff8ce58859bf28e485ec349616226f4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-27-358253
  comparison: ''
  date: '2026-03-27'
  description: 'Claude Code — v2.1.86: Added `X-Claude-Code-Session-Id` header to
    API requests so proxies can aggregate requests by session without parsing the
    body'
  evidence:
  - quote: Added `X-Claude-Code-Session-Id` header to API requests so proxies can
      aggregate requests by session without parsing the body
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r
  source_release: claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|Resuming
  a session that was in a worktree now switches back to that worktree]]'
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|Added
  --bare flag for scripted -p calls]]'
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|Added
  WorktreeCreate hook support for type: "http"]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
source_type: github_releases
theme: developer-workflow
title: Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate…

**Claude Code** · 2026-03-27 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.86) · from [[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|v2.1.86]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|Reduced token overhead when mentioning files with @]] · Context Window
- [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|Added .jj and .sl to VCS directory exclusion lists so Grep and file autocomplete…]] · Editor Experience
- [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|Added WorktreeCreate hook support for type: "http"]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-the-new-cursor-interface-allows-you-to-run-many-agents-in-parallel-across-repos|The new Cursor interface allows you to run many agents in parallel across repos…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-27-358253&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r.md%0ACard%20ID%3A%20claude-code-2026-03-27-358253%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.86%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->