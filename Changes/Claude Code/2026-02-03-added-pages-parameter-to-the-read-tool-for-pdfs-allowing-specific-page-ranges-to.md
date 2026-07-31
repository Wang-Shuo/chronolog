---
card_id: claude-code-2026-02-03-618c1b
date: '2026-02-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1006
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|claude-code-2026-01-16-35ca77]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 056df29bfe4ae0ded49aafbcc61de7f4514b925ed515606ea9697652d0d7b08f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|claude-code-2026-01-13-00ffe3]]'
- '[[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|claude-code-2026-01-16-35ca77]]'
- '[[Changes/Cursor/2026-01-22-the-result-is-faster-overall-execution-more-focused-context-in-your-main-convers|cursor-2026-01-22-ab1b65]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
theme: context-window
type: change
---

# Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges

<!-- chronolog:begin region="description" -->
Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|claude-code-2026-01-16-35ca77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1006
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes