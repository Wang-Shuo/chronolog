# ChronoLog quality report

Run: `recovery-20261030-preflight` · **ready**

Mode: generate; input: live; base: `80911db89ed10923205d471fd756a47d5b45a16f`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | success | browser-snapshot | 2026-10-30T12:40:58.527Z | 2022-12-15 → 2026-10-28 |
| claude-code | success | http | 2026-10-30T12:41:57Z | 2025-12-19 → 2026-10-30 |
| cursor | success | http | 2026-10-30T12:42:45Z | 2023-03-14 → 2026-10-20 |

## Changes

{"acquisition_only": 0, "added": 62, "modified": 45, "removed": 0, "retired": 0}

Pending themes: 63; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
