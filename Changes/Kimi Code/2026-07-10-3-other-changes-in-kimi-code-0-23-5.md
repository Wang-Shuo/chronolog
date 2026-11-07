---
card_id: kimi-code-2026-07-10-af004e
date: '2026-07-10'
description: 'Kimi Code · 2026-07-10 · Other changes: 3 changes in Kimi Code 0.23.5
  (2026-07-10) — Retry provider 429, overload, and other transient errors more reliably…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c869b4a2841d1cbe178fbc190aecc6ed4c92d62b21720fc0e80edb7c312ac939
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-10-af004e
  comparison: ''
  date: '2026-07-10'
  description: 'Kimi Code — Kimi Code 0.23.5 (2026-07-10): 3 other changes'
  evidence:
  - quote: Retry provider 429, overload, and other transient errors more reliably,
      honoring the server Retry-After delay, and surface retries in `-p --output-format
      stream-json`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Stop unsupported image formats (AVIF, BMP, TIFF, ICO, …) from breaking
      sessions at every entry point — including remote image URLs and images mislabeled
      by a tool — and recover an already-stuck session by dropping the offending image
      and retrying, so one such image can no longer make every later request fail.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Hide the internal image-compression note so it no longer renders
      as user message text.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 3-other-changes-in-kimi-code-0-23-5
  source_release: kimi-code-2026-07-10-0-23-5-ae6a667a
  source_type: kimi_code_changelog
  theme: uncategorized
  title: 3 other changes in Kimi Code 0.23.5
  type: change
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-10-0-23-5-ae6a667a|kimi-code-2026-07-10-0-23-5-ae6a667a]]'
source_type: kimi_code_changelog
theme: uncategorized
title: 3 other changes in Kimi Code 0.23.5
type: change
---

<!-- chronolog:begin region="header" -->
# 3 other changes in Kimi Code 0.23.5

**Kimi Code** · 2026-07-10 · Other changes · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-10-0-23-5-ae6a667a|Kimi Code 0.23.5 (2026-07-10)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Retry provider 429, overload, and other transient errors more reliably, honoring the server Retry-After delay, and surface retries in `-p --output-format stream-json`.

> Stop unsupported image formats (AVIF, BMP, TIFF, ICO, …) from breaking sessions at every entry point — including remote image URLs and images mislabeled by a tool — and recover an already-stuck session by dropping the offending image and retrying, so one such image can no longer make every later request fail.

> web: Hide the internal image-compression note so it no longer renders as user message text.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-10-af004e&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-10-3-other-changes-in-kimi-code-0-23-5.md%0ACard%20ID%3A%20kimi-code-2026-07-10-af004e%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->