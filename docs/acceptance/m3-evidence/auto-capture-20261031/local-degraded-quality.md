# ChronoLog quality report

Run: `auto-recovery-live-20261031` · **ready**

Mode: generate; input: live; base: `fa92fbbef8099bcd7acb855a592e5f6a88f40691`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | failed | none | unknown | None → None |
| claude-code | success | http | 2026-10-31T02:14:11Z | 2025-12-19 → 2026-10-31 |
| cursor | success | http | 2026-10-31T02:14:58Z | 2023-03-14 → 2026-10-20 |

**Degraded collection:** failed sources retain their last reviewed content. Only successful sources are updated and reconciled. This is not a fully successful collection.

## Changes

{"acquisition_only": 0, "added": 10, "modified": 23, "removed": 0, "retired": 0}

Pending themes: 63; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Source chatgpt: ChatGPT Help Center blocked automated access; provide a browser-rendered snapshot with --snapshot chatgpt=/path/to/page.html; automatic browser capture failed: official browser capture did not become usable: empty or duplicate ChatGPT release identities

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
