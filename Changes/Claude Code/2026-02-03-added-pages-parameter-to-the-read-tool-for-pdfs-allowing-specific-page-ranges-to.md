---
card_id: claude-code-2026-02-03-618c1b
date: '2026-02-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1006
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 4cf7c645f99d5e628e1f98f42dded3f086ef07a39fe0c0807df70368dcf38bd3
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
  extractor_version: fallback-v4
  impact: incremental
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
- '[[Changes/Claude Code/2026-01-13-added-context-window-used-percentage-and-context-window-remaining-percentage-fie|claude-code-2026-01-13-00ffe3]]'
- '[[Changes/Claude Code/2026-01-16-added-auto-n-syntax-for-configuring-the-mcp-tool-search-auto-enable-threshold-wh|claude-code-2026-01-16-35ca77]]'
- '[[Changes/Cursor/2026-01-22-the-result-is-faster-overall-execution-more-focused-context-in-your-main-convers|cursor-2026-01-22-ab1b65]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
source_type: github_releases
theme: context-window
title: Added pages parameter to the Read tool for PDFs, allowing specific page ranges…
type: change
---

# Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.30: Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1006
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes