---
card_id: cline-2026-08-13-a59347
date: '2026-08-13'
description: 'Cline · 2026-08-13 · Other changes: 6 changes in v4.1.9 — Switch the
  interface to Inter and Geist Mono.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0443cf574d1a762bed3da657a2d6f949a1896c9f2272b2e168680a219b44c2ee
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-13-a59347
  comparison: ''
  date: '2026-08-13'
  description: 'Cline — v4.1.9: 6 other changes'
  evidence:
  - quote: Switch the interface to Inter and Geist Mono.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  - quote: Don't discard a successfully refreshed Cline token when the old one was
      already past expiry, which made the first request after a long idle period fail
      despite valid credentials.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  - quote: Stop the legacy-task migration backlog from spamming telemetry, and record
      a migration outcome only once the seeded session actually persists, so a failed
      migration is no longer reported as a success.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  - quote: Report involuntary Cline logouts (a rejected refresh token) instead of
      clearing credentials silently.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  - quote: Reject truncated tool-call JSON instead of silently "repairing" it into
      wrong arguments.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  - quote: Report disjoint per-request token buckets instead of re-counting the whole
      cached conversation on every request, which inflated per-task totals roughly
      5x on cache-heavy sessions.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 6-other-changes-in-v4-1-9
  source_release: cline-2026-08-13-v4-1-9-github-369742457-b48c0c59
  source_type: github_releases
  theme: uncategorized
  title: 6 other changes in v4.1.9
  type: change
source_release: '[[Releases/Cline/cline-2026-08-13-v4-1-9-github-369742457-b48c0c59|cline-2026-08-13-v4-1-9-github-369742457-b48c0c59]]'
source_type: github_releases
theme: uncategorized
title: 6 other changes in v4.1.9
type: change
---

<!-- chronolog:begin region="header" -->
# 6 other changes in v4.1.9

**Cline** · 2026-08-13 · Other changes · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.9) · from [[Releases/Cline/cline-2026-08-13-v4-1-9-github-369742457-b48c0c59|v4.1.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Switch the interface to Inter and Geist Mono.

> Don't discard a successfully refreshed Cline token when the old one was already past expiry, which made the first request after a long idle period fail despite valid credentials.

> Stop the legacy-task migration backlog from spamming telemetry, and record a migration outcome only once the seeded session actually persists, so a failed migration is no longer reported as a success.

> Report involuntary Cline logouts (a rejected refresh token) instead of clearing credentials silently.

> Reject truncated tool-call JSON instead of silently "repairing" it into wrong arguments.

> Report disjoint per-request token buckets instead of re-counting the whole cached conversation on every request, which inflated per-task totals roughly 5x on cache-heavy sessions.

Source: https://github.com/cline/cline/releases/tag/v4.1.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-13-these-land-through-sdk-v0-0-74-and-therefore-apply-to-windows-running-the-sdk-bu|These land through SDK v0.0.74 and therefore apply to windows running the SDK…]] · Apps and Integrations
- [[Changes/Cline/2026-08-13-use-the-editor-s-foreground-color-for-diff-block-text-so-diffs-stay-legible-in-t|Use the editor's foreground color for diff block text, so diffs stay legible…]] · Editor Experience
- [[Changes/Cline/2026-08-13-fix-the-claude-code-provider-being-unusable-for-agentic-work-it-now-runs-its-own|Fix the Claude Code provider being unusable for agentic work]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-13-a59347&body=Card%3A%20Changes%2FCline%2F2026-08-13-6-other-changes-in-v4-1-9.md%0ACard%20ID%3A%20cline-2026-08-13-a59347%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->