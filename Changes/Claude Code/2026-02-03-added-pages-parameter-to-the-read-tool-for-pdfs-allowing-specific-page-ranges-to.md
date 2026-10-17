---
card_id: claude-code-2026-02-03-618c1b
date: '2026-02-03'
description: 'Claude Code · 2026-02-03 · Context Window: Added `pages` parameter to
  the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages:
  "1-5"`)…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1006
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ad42b299b81d85d3cfed7b8f53ade3183ae51f791d2a1c7a4fa98ec478959b2d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-03-618c1b
  comparison: ''
  date: '2026-02-03'
  description: 'Claude Code — v2.1.30: Added `pages` parameter to the Read tool for
    PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs
    (>10 pages) now return a lightweight reference when `@` mentioned instead of being
    inlined into context.'
  evidence:
  - quote: 'Added `pages` parameter to the Read tool for PDFs, allowing specific page
      ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return
      a lightweight reference when `@` mentioned instead of being inlined into context.'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to
  source_release: claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2
  source_type: github_releases
  theme: context-window
  title: Added `pages` parameter to the Read tool for PDFs, allowing specific page
    ranges…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-14-enabled-mcp-tool-search-auto-mode-by-default-for-all-users-when-mcp-tool-descrip|Enabled
  MCP tool search auto mode by default for all users]]'
- '[[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|Added
  auto:N syntax for configuring the MCP tool search auto-enable threshold…]]'
- '[[Changes/Cursor/2026-01-22-agents-can-now-read-pdfs-which-you-can-attach-in-chats-as-context|Agents
  can now read PDFs, which you can attach in chats as context]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
source_type: github_releases
theme: context-window
title: Added pages parameter to the Read tool for PDFs, allowing specific page ranges…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges…

**Claude Code** · 2026-02-03 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.30) · from [[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|v2.1.30]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|Added pre-configured OAuth client credentials for MCP servers that don't support…]] · Account and Access
- [[Changes/Claude Code/2026-02-03-2-developer-workflow-changes-in-v2-1-30|2 Developer Workflow changes in v2.1.30]] · Developer Workflow
- [[Changes/Claude Code/2026-02-03-improved-memory-usage-for-resume-68-reduction-for-users-with-many-sessions-by-re|Improved memory usage for --resume (68% reduction for users with many sessions)…]] · Reliability and Performance
- [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]] · Agent Mode
- [[Changes/Claude Code/2026-02-03-changed-model-to-execute-immediately-instead-of-being-queued|Changed /model to execute immediately instead of being queued]] · Model Support
- [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-03-added-debug-for-claude-to-help-troubleshoot-the-current-session|Added /debug for Claude to help troubleshoot the current session]] · Developer Workflow
- [[Changes/Claude Code/2026-02-03-2-other-changes-in-v2-1-30|2 other changes in v2.1.30]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-01-22 · Cursor · [[Changes/Cursor/2026-01-22-agents-can-now-read-pdfs-which-you-can-attach-in-chats-as-context|Agents can now read PDFs, which you can attach in chats as context]]
- Later: 2026-02-05 · Claude Code · [[Changes/Claude Code/2026-02-05-2-context-window-changes-in-v2-1-32|2 Context Window changes in v2.1.32]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-03-618c1b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to.md%0ACard%20ID%3A%20claude-code-2026-02-03-618c1b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.30%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->