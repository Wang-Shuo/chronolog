# ChronoLog quality report

Run: `recovery-20261027-auth-preflight` · **ready**

Mode: generate; input: live; base: `5dff1a70562ede05ba8426283040f46989e00dbf`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | success | http | 2026-10-27T02:37:46Z | 2022-12-15 → 2026-10-26 |
| claude-code | success | http | 2026-10-27T02:37:52Z | 2025-12-19 → 2026-10-26 |
| cursor | success | http | 2026-10-27T02:38:15Z | 2023-03-14 → 2026-10-20 |

## Changes

{"acquisition_only": 0, "added": 33, "modified": 861, "removed": 0, "retired": 0}

Pending themes: 63; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
