# Product expansion to 45 — 2026-11-07

ChronoLog now tracks **45 products**, with **6,008 releases**
and **21,692 published Change Cards**. Eight additions contribute
**932 official release records** and **3,491 published cards**.

| Added product | Releases | Cards | Archived publication dates | Source |
| --- | ---: | ---: | --- | --- |
| Krea | 47 | 116 | 2026-04-14 → 2026-11-04 | [Official source](https://www.krea.ai/docs/changelog) |
| Recraft | 77 | 108 | 2025-01-10 → 2026-11-05 | [Official source](https://feedback.recraft.ai/changelog) |
| Raycast | 263 | 1,305 | 2020-08-03 → 2026-11-06 | [Official source](https://www.raycast.com/changelog) |
| Devin | 129 | 951 | 2024-05-13 → 2026-11-02 | [Official source](https://docs.devin.ai/release-notes/overview) |
| LM Studio | 64 | 206 | 2024-10-22 → 2026-10-31 | [Official source](https://lmstudio.ai/changelog/lmstudio) |
| AnythingLLM | 39 | 284 | 2024-07-26 → 2026-10-26 | [Official source](https://api.github.com/repos/Mintplex-Labs/anything-llm/releases) |
| Superwhisper | 292 | 442 | 2023-08-03 → 2026-11-06 | [Official source](https://superwhisper.com/changelog) |
| Wispr Flow | 21 | 79 | 2026-03-31 → 2026-10-30 | [Official source](https://wisprflow.ai/whats-new) |

## Selection and coverage

This batch adds established creative, agent, local-model and voice products with
verifiable official dated archives. It is a curated expansion, not a popularity
ranking or a claim that every product recently launched.

- Krea preserves every dated announcement in its current documentation changelog;
  same-day announcements keep distinct identities. Earlier blog-only posts and
  media contents are outside this source's scope.
- Recraft exhausts its public Canny changelog. Empty or media-only posts retain
  their descriptive official title; drafts, deleted posts and media transcription
  are excluded.
- Raycast traverses every page of the macOS, legacy macOS V1, Windows and iOS
  archives. Platform-qualified identities prevent equal version numbers from
  merging. Both AI and general launcher/workspace changes are included.
- Devin discovers all annual archives through its recent-updates overview. Annual
  content is authoritative: the overview contained conflicting or older text.
  Every recent overview date must appear in the annual archives. Separate Desktop
  and CLI version histories are excluded; Windsurf already covers Desktop.
- LM Studio checks the stable API's offsets, unique versions and reported total.
  A version retains the builds grouped under it and the API's version release date;
  builds are not assigned invented dates. Bionic, previews and separate runtime/SDK
  histories are excluded.
- AnythingLLM uses stable versioned releases from the official application
  repository, including platform and Docker changes described there. Desktop-only
  distribution history and prereleases are outside this endpoint.
- Superwhisper checks all four official platform tabs and retains separate macOS,
  Windows, iOS and Android version identities. Missing older mobile history and
  Linux announcements without an archive tab are excluded.
- Wispr Flow records visible release dates and preserves Desktop, iOS, Android,
  Notetaker and All platforms scope. HTML anchor names are not treated as dates.
- Perplexity, Mistral and Poe were deferred because their sources could not be
  reliably fetched. Bolt's visible week ranges lacked years, and Ideogram's current
  endpoint did not establish a release archive. No unavailable dates were invented.

Existing **37-product** history retains all **5,076 release records**, **18,201
published card records**, **2,229 pending records** and original acquisition coverage.
Available-endpoint date ranges are not product launch dates or lifetime coverage.
There are now **2,834 pending candidates**, including
**605 new candidates**; none are published. New product eras remain unreviewed,
and existing research summaries retain their original scope.

## Collection and extraction checks

- **55 saved collection HTTP responses** passed SHA-256 checks. Normalized collections
  retain the earliest actual acquisition timestamp used for each source.
- Missing dates, incomplete pagination, wrong platform tabs, changing totals and
  duplicate release identities fail collection instead of authorizing partial reconciliation.
- Generic labels such as Build 1, Features & Improvements and Other no longer become
  feature launches. Concrete changes remain separate, and fixes-only builds create
  no artificial feature cards. Explicit Krea video generation is distinguished from video input.
- The first local gate caught two outdated catalog expectations in tests. They were
  updated to the 45-product contract; no checks were skipped. That failed run remains
  under the ignored `next-products-2026-11-07-r1` directory.
- The second gate caught a source-relative AnythingLLM link being treated as a
  vault edge. The official GitHub release HTML confirms its tagged-repository
  target. Evidence rendering now resolves relative paths in the source context
  while preserving raw quotes and card identities; inline code remains literal.
  The failed `r2` run is retained, and the final run repeats all gates.

## Site capacity and behavior

The previous 37-product output was **894.7 MiB**. Each page repeated 13,162 bytes of
identical callout/Mermaid CSS and JavaScript, leaving little room for more history.
The new wrapper emits those exact bytes once as content-hashed shared files.
Tests cover deduplication, nested deployment paths, partial emission, unchanged
source objects, script load/module/SPA flags and inline fallbacks for URL-dependent
resources. Browser checks confirm initial rendering, callout toggling and Mermaid
rendering after a real SPA navigation, with no console errors or warnings.

The prior CI run hit its 20-minute build budget before succeeding on an unchanged
rerun; deployment took approximately 25 minutes. The build command now has a
30-minute budget, Quality/deployment jobs 45 minutes, and scheduled generation
60 minutes. Test, link, publication and protected-review gates remain enforced.

## Acceptance

Run: `next-products-2026-11-07-r3`, **candidate-applied**, **21,341 files** applied.

- **651 automated tests passed**.
- Vault validation checked **29,235 Markdown files** and
  **459,518 links**, with no errors.
- The applied vault matches the validated candidate byte for byte; original
  records, pending records and acquisition coverage passed independent comparisons.
- Quartz and publication audits passed: **27,876 active indexed pages**,
  **28,026 HTML pages**, **945,318 HTML links**,
  and **30 RSS entries**. Review candidates and QA fixture pages are excluded.
- Output size is **714.8 MiB**, below 1 GiB; content index is
  **76.8 MiB**. Shared assets match the previous inline bytes exactly.
- Chrome verified all 45 homepage product links, all eight added pages, a new-product
  theme filter and the final v0 filter. Viewport/document widths match at 1440px and
  390px; the comparison table scrolls internally. All ten browser-checked pages
  match the final build byte for byte after the source-link correction.

## Evidence and replay

The [evidence manifest](next-products-45-evidence/sha256.json) covers the normalized
collection, quality reports, source-response manifest, preservation checks and
browser evidence. Copied build/console logs normalize terminal escapes and trailing
whitespace; original logs and raw HTTP bodies remain in the ignored local folders.
Generation replays the November 7 acquisition and is explicitly labeled `replay`.

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id next-products-45-replay-unique \
  --output _pipeline/next-products-45-replay-unique \
  --collection docs/acceptance/next-products-45-evidence/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog
```

Delivery follows the existing protected-main PR, Quality and deployment workflow.
