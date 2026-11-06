# Product expansion to 20 — 2026-11-06

ChronoLog now tracks **20 products**, with **3,227 releases**
and **13,248 Change Cards**. The ten additional products contribute
**1,229 official release records** and **5,419 cards**.

| Added product | Releases | Cards | Archived announcement dates | Source |
| --- | ---: | ---: | --- | --- |
| Claude | 63 | 75 | 2025-08-01 → 2026-11-05 | [Official source](https://support.claude.com/en/articles/12138966-release-notes) |
| Gemini | 96 | 126 | 2023-04-10 → 2026-10-13 | [Official source](https://gemini.google/us/release-notes/?hl=en) |
| DeepSeek API | 22 | 19 | 2024-05-17 → 2026-10-17 | [Official source](https://api-docs.deepseek.com/updates/) |
| ElevenLabs | 103 | 814 | 2024-10-13 → 2026-11-02 | [Official source](https://elevenlabs.io/docs/changelog) |
| Lovable | 156 | 592 | 2024-12-03 → 2026-11-04 | [Official source](https://docs.lovable.dev/changelog) |
| v0 | 92 | 234 | 2025-10-01 → 2026-10-19 | [Official source](https://v0.app/changelog) |
| Replit | 99 | 476 | 2024-12-13 → 2026-10-30 | [Official source](https://docs.replit.com/updates) |
| Ollama | 266 | 698 | 2023-07-08 → 2026-11-03 | [Official source](https://api.github.com/repos/ollama/ollama/releases) |
| Dify | 154 | 1,101 | 2023-05-15 → 2026-11-04 | [Official source](https://api.github.com/repos/langgenius/dify/releases) |
| Open WebUI | 178 | 1,284 | 2024-02-23 → 2026-11-03 | [Official source](https://api.github.com/repos/open-webui/open-webui/releases) |

## Scope and collection

- The product catalog drives collection, product pages, search, graph and timeline
  filters. Existing ten-product history is retained with its original source dates.
- Claude, Gemini, DeepSeek API and v0 use dated official HTML entries; Lovable uses
  its dated Markdown changelog. ElevenLabs traverses its complete dated changelog
  index rather than the default 20-entry window. Replit traverses dated weekly
  update URLs in the official sitemap and checks each page's heading date.
- Ollama, Dify and Open WebUI include stable versioned releases from their official
  GitHub repositories. Prereleases and separately versioned packages are excluded.
- Missing archive pages, invalid dates, duplicate identities and foreign index hosts
  fail collection. Navigation, documentation widgets and code examples are excluded.
  All 281 saved HTTP responses returned 200 and passed their SHA-256 checks.
- Coverage refers to the currently available official endpoints. Claude's current
  endpoint starts in August 2025. Gemini includes historical Bard entries. DeepSeek
  API is an API history, and Replit includes development-platform changes announced
  alongside Agent. Each product page states its specific scope and acquisition date.
- Gemini app mentions no longer imply model changes; versioned model names remain
  model signals. Ollama runtime memory is distinguished from saved user memory.
  Generic Misc./All changes groups and release-automation text do not become feature
  titles. Markdown formatting in source titles cannot split generated wiki links.
- **1,055 candidates remain pending review** (944 additional).
  These remain excluded from publication. New product eras are not editorially
  reviewed; existing research summaries retain their stated original scope.

## Verification

Final run: `product-expansion-20-2026-11-06-r5`, **candidate-applied**, with
**14,510 files** applied after all gates passed.

- **539 tests passed**, including archive traversal, date validation, failed-page
  handling, app-aware classification, wiki-label rendering and all 20 timeline filters.
- Vault audit checked **17,931 Markdown files** and
  **288,231 links**, with zero errors. The working vault matches
  the validated candidate byte for byte.
- Quartz built successfully. Publication audit checked **16,647
  HTML pages** and **572,436 links**, confirmed
  **16,572 active indexed pages**, no broken graph edges,
  and **30 valid RSS items**. Excluded pages remain absent.
- Final Chrome checks found all 20 products on the homepage and verified the 20th
  timeline filter (v0) at desktop and mobile sizes. Document width matches the
  viewport at 1440px and 390px; the wide comparison table scrolls internally.
  The Dify product page has no unrendered wiki links. Console: zero errors or warnings.

## Evidence and replay

The [evidence manifest](product-expansion-20-evidence/sha256.json) hashes the compressed
normalized collection, quality reports, raw test/build logs, HTTP response manifest,
vault comparison and final browser checks/screenshots. Original HTTP bodies remain
in the ignored local acquisition directory; their per-response hashes are retained.

Sources were fetched live on 2026-11-06. Generation replays that saved acquisition
and is correctly labeled `replay`; it does not count as a scheduled live run.

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id product-expansion-20-replay-unique \
  --output _pipeline/product-expansion-20-replay-unique \
  --collection docs/acceptance/product-expansion-20-evidence/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog
```

This command builds an isolated candidate. Publication uses the existing reviewed
PR workflow, its required Quality check, and the protected-main deployment workflow.
