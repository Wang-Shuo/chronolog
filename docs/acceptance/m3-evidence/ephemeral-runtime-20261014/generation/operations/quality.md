# ChronoLog quality report

Run: `daily-38587902325-1` · **failed**

Mode: generate; input: live; base: `11f68b4d364b05a6281bd4cb3bb5289a01363f3c`.

| Source | Status | Acquisition | Acquired at | Release range |
| --- | --- | --- | --- | --- |
| chatgpt | failed | none | unknown | None → None |
| claude-code | success | http | 2026-10-14T15:17:08Z | 2025-12-19 → 2026-10-14 |
| cursor | success | http | 2026-10-14T15:17:24Z | 2023-03-14 → 2026-10-13 |

## Changes

{}

Pending themes: not assessed; DLQ: 0; conflicts: 0.

| Gate | Result | Evidence |
| --- | --- | --- |

## Failure

ValueError: collection failed: [{&#x27;product&#x27;: &#x27;chatgpt&#x27;, &#x27;error&#x27;: &#x27;ChatGPT Help Center blocked automated access; provide a browser-rendered snapshot with --snapshot chatgpt=/path/to/page.html&#x27;}]

Source chatgpt: ChatGPT Help Center blocked automated access; provide a browser-rendered snapshot with --snapshot chatgpt=/path/to/page.html; snapshot fallback rejected: [Errno 2] No such file or directory: &#x27;_inputs/chatgpt/capture.json&#x27;

Detailed changed paths, source coverage, validation results and input hashes are in `quality.json` and `evidence-sha256.json`.
Generated content requires PR review. A green engineering gate does not approve new semantic judgments.
