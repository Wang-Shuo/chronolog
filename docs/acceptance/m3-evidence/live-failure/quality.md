# ChronoLog quality report

Run: `m3-live-manual` · **failed**

Mode: generate; input: live; base: `997692de8a9c23d8de09bbbaad2633b2c03c669c`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | success | browser-snapshot | 2026-10-13T10:59:17Z | 2022-12-15 → 2026-10-07 |
| claude-code | failed | none | unknown | None → None |
| cursor | success | http | 2026-10-13T12:30:42Z | 2023-03-14 → 2026-10-06 |

## Changes

{}

Pending themes: not assessed; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |

## Failure

ValueError: collection failed: [{&#x27;product&#x27;: &#x27;claude-code&#x27;, &#x27;error&#x27;: &quot;Client error &#x27;403 rate limit exceeded&#x27; for url &#x27;https://api.github.com/repos/anthropics/claude-code/releases?per_page=100&amp;page=2&#x27;\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403&quot;}]

Source claude-code: Client error &#x27;403 rate limit exceeded&#x27; for url &#x27;https://api.github.com/repos/anthropics/claude-code/releases?per_page=100&amp;page=2&#x27; For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
