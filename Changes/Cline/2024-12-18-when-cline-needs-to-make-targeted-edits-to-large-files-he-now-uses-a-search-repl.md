---
card_id: cline-2024-12-18-69e1a5
date: '2024-12-18'
description: 'Cline · 2024-12-18 · Reliability and Performance: When Cline needs to
  make targeted edits to large files, he now uses a search & replace diff format where
  he…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 734
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: c5c0ed09b151ea364ca1441601c3b874fe3e2027ab7b001d16aaabe56a95d671
product: cline
product_name: Cline
record:
  card_id: cline-2024-12-18-69e1a5
  comparison: ''
  date: '2024-12-18'
  description: 'Cline — v3.0.0: When Cline needs to make targeted edits to large files,
    he now uses a search & replace diff format where he only has to output the content
    to replace, rather than the whole file. This allows for faster, more reliable
    edits and prevents code deletion issues where previously, unmodified sections
    of code might have been replaced with comments like `// rest of code here`. Cline
    can also fall back to whole file editing for when it makes sense, e.g. replacing
    boilerplate files, complete refactors, or when diff editing fails.'
  evidence:
  - quote: When Cline needs to make targeted edits to large files, he now uses a search
      & replace diff format where he only has to output the content to replace, rather
      than the whole file. This allows for faster, more reliable edits and prevents
      code deletion issues where previously, unmodified sections of code might have
      been replaced with comments like `// rest of code here`. Cline can also fall
      back to whole file editing for when it makes sense, e.g. replacing boilerplate
      files, complete refactors, or when diff editing fails.
    source_release: https://github.com/cline/cline/releases/tag/v3.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cline
  product_name: Cline
  slug: when-cline-needs-to-make-targeted-edits-to-large-files-he-now-uses-a-search-repl
  source_release: cline-2024-12-18-v3-0-0-github-191549962-04b25c94
  source_type: github_releases
  theme: reliability-performance
  title: When Cline needs to make targeted edits to large files, he now uses a search…
  type: change
related_changes:
- '[[Changes/Cursor/2024-11-24-several-performance-improvements|Several performance
  improvements]]'
- '[[Changes/Cursor/2024-12-17-cursor-starts-up-faster|Cursor starts up faster]]'
- '[[Changes/Cursor/2024-12-17-cheaper-and-faster-bug-finding-model|Cheaper and faster
  Bug Finding Model]]'
source_release: '[[Releases/Cline/cline-2024-12-18-v3-0-0-github-191549962-04b25c94|cline-2024-12-18-v3-0-0-github-191549962-04b25c94]]'
source_type: github_releases
theme: reliability-performance
title: When Cline needs to make targeted edits to large files, he now uses a search…
type: change
---

<!-- chronolog:begin region="header" -->
# When Cline needs to make targeted edits to large files, he now uses a search…

**Cline** · 2024-12-18 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/cline/cline/releases/tag/v3.0.0) · from [[Releases/Cline/cline-2024-12-18-v3-0-0-github-191549962-04b25c94|v3.0.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> When Cline needs to make targeted edits to large files, he now uses a search & replace diff format where he only has to output the content to replace, rather than the whole file. This allows for faster, more reliable edits and prevents code deletion issues where previously, unmodified sections of code might have been replaced with comments like `// rest of code here`. Cline can also fall back to whole file editing for when it makes sense, e.g. replacing boilerplate files, complete refactors, or when diff editing fails.
>
> Source: https://github.com/cline/cline/releases/tag/v3.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2024-12-18-you-can-now-specify-custom-instructions-for-your-project-by-adding-a-root-level|Specify custom instructions for your project by adding a root-level .clinerules file]] · Context Window
- [[Changes/Cline/2024-12-18-enable-or-disable-for-reading-files-directories-editing-files-executing-terminal|Enable or disable for]] · Apps and Integrations
- [[Changes/Cline/2024-12-18-cline-s-most-requested-feature-is-here-you-can-now-let-cline-work-more-autonomou|Cline's most requested feature is here 🎉 You can now let Cline work more…]] · Safety and Privacy
- [[Changes/Cline/2024-12-18-4-other-changes-in-v3-0-0|4 other changes in v3.0.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2024-12-17 · Cursor · [[Changes/Cursor/2024-12-17-cheaper-and-faster-bug-finding-model|Cheaper and faster Bug Finding Model]]
- Later: 2025-01-07 · OpenHands · [[Changes/OpenHands/2025-01-07-performance-improvement-of-ui-during-long-sessions-by-amanape-in-https-github-co|Performance improvement of UI during long sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2024-12-18-69e1a5&body=Card%3A%20Changes%2FCline%2F2024-12-18-when-cline-needs-to-make-targeted-edits-to-large-files-he-now-uses-a-search-repl.md%0ACard%20ID%3A%20cline-2024-12-18-69e1a5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv3.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->