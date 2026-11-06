# ChronoLog quality report

Run: `product-expansion-20-2026-11-06-r5` · **candidate-applied**

Mode: generate; input: replay; base: `5d9ba8bd67f1586b5714f00cf6850410a1499e45`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| claude | success | http | 2026-11-06T13:12:59Z | 2025-08-01 → 2026-11-05 |
| gemini | success | http | 2026-11-06T13:13:00Z | 2023-04-10 → 2026-10-13 |
| deepseek-api | success | http | 2026-11-06T13:13:00Z | 2024-05-17 → 2026-10-17 |
| elevenlabs | success | http | 2026-11-06T13:13:19Z | 2024-10-13 → 2026-11-02 |
| lovable | success | http | 2026-11-06T13:13:19Z | 2024-12-03 → 2026-11-04 |
| v0 | success | http | 2026-11-06T13:13:20Z | 2025-10-01 → 2026-10-19 |
| ollama | success | http | 2026-11-06T13:13:38Z | 2023-07-08 → 2026-11-03 |
| dify | success | http | 2026-11-06T13:13:44Z | 2023-05-15 → 2026-11-04 |
| open-webui | success | http | 2026-11-06T13:13:51Z | 2024-02-23 → 2026-11-03 |
| replit | success | http | 2026-11-06T13:15:09Z | 2024-12-13 → 2026-10-30 |

## Changes

{"acquisition_only": 0, "added": 7602, "modified": 6908, "removed": 0, "retired": 0}

Pending themes: 1055; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |
| tests | passed | tests.log |
| vault | passed | vault-validation.json |
| build | passed | build.log |
| publication | passed | publication.json |

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
