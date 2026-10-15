# ChronoLog quality report

Run: `w1-site-20261015` · **candidate-applied**

Mode: generate; input: replay; base: `72fc8523837c920865dfdbaf94d155627e6ebe18`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | success | browser-snapshot | 2026-10-14T23:26:11+0800 | 2022-12-15 → 2026-10-07 |
| claude-code | success | http | 2026-10-15T01:55:15Z | 2025-12-19 → 2026-10-14 |
| cursor | success | http | 2026-10-15T01:55:30Z | 2023-03-14 → 2026-10-13 |

## Changes

{"acquisition_only": 0, "added": 1, "modified": 4, "removed": 0, "retired": 0}

Pending themes: 149; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
