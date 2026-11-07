---
card_id: claude-code-2026-02-03-618c1b
date: '2026-02-03'
description: 'Claude Code · 2026-02-03 · Context Window: Added `pages` parameter to
  the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages:
  "1-5"`)…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f1e11942da39a1d6e4c71fd982ea146474d5622741d8f7b9e0e97cc160a02355
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
- '[[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context
  Window changes in rust-v0.93.0]]'
- '[[Changes/OpenCode/2026-01-31-core-add-copilot-specific-provider-to-properly-handle-reasoning-tokens|Core
  Add Copilot-specific provider to properly handle reasoning tokens]]'
- '[[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context
  Window changes in rust-v0.94.0]]'
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

- Earlier: 2026-02-02 · Codex CLI · [[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context Window changes in rust-v0.94.0]]
- Later: 2026-02-03 · Dify · [[Changes/Dify/2026-02-03-5-context-window-changes-in-1-12-0|5 Context Window changes in 1.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-03-618c1b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to.md%0ACard%20ID%3A%20claude-code-2026-02-03-618c1b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.30%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->