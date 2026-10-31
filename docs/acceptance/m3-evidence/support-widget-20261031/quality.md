# ChronoLog quality report

Run: `support-widget-fix-20261031` · **candidate-applied**

Mode: generate; input: replay; base: `de2c71f33cbcd3d2c075300348e1510168465251`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | success | browser-snapshot | 2026-10-31T04:08:55Z | 2022-12-15 → 2026-10-30 |
| claude-code | success | http | 2026-10-31T04:08:35Z | 2025-12-19 → 2026-10-31 |
| cursor | success | http | 2026-10-31T04:08:46Z | 2023-03-14 → 2026-10-20 |

## Changes

{"acquisition_only": 0, "added": 12, "modified": 26, "removed": 0, "retired": 0}

Pending themes: 63; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
