# Product expansion to 37 — 2026-11-07

ChronoLog now tracks **37 products**, with **5,076 releases**
and **18,201 Change Cards**. Eight additions contribute
**1,083 official release records** and **2,392 published cards**.

| Added product | Releases | Cards | Archived publication dates | Source |
| --- | ---: | ---: | --- | --- |
| Descript | 534 | 794 | 2018-07-07 → 2026-11-06 | [Official source](https://feedback.descript.com/changelog) |
| HeyGen | 47 | 247 | 2025-11-29 → 2026-10-28 | [Official source](https://heygen.noticeable.news/) |
| Synthesia | 202 | 101 | 2020-10-13 → 2026-10-27 | [Official source](https://www.synthesia.io/updates) |
| Qoder | 26 | 92 | 2026-08-27 → 2026-11-06 | [Official source](https://changelog.qoder.com/app) |
| Kimi Code | 91 | 379 | 2026-05-26 → 2026-11-06 | [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) |
| Microsoft 365 Copilot | 21 | 235 | 2026-01-13 → 2026-11-04 | [Official source](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes) |
| Notion | 154 | 527 | 2020-01-09 → 2026-10-19 | [Official source](https://www.notion.com/releases) |
| Z.ai API | 8 | 17 | 2025-09-30 → 2026-08-26 | [Official source](https://docs.z.ai/release-notes/new-released) |

## Selection and source scope

This expansion adds established video and workspace products alongside additional
coding and model tools. Every source was checked against its official public
history. It is a curated catalog expansion, not a popularity ranking or a claim
that all products were recently launched.

- Descript traverses all three update types exposed by its public Canny page:
  new, improved and fixed. This avoids the unfiltered API's 50-page limit. Each
  type must reach its terminal page; overlapping records must agree exactly.
  Older empty or media-only posts retain only their official descriptive title.
  No video/image content is inferred. Drafts and deleted posts are rejected.
- HeyGen traverses the public Noticeable archive and checks each article's title
  and publication timestamp against its index. Reactions and feedback forms are removed.
- Synthesia records dated summaries across all index pages. Separate featured hero
  announcements have no dates and are explicitly outside this source's scope.
  Full linked article bodies are not represented as collected.
- Qoder covers the unified app's current version history. Separate IDE, CLI and
  legacy QoderWork histories are not combined as duplicate products.
- Kimi Code uses dated versions from its official English repository changelog.
  Same-day versions retain distinct identities. Unreleased drafts are excluded;
  category headings such as Polish and Refactors do not become feature launches.
- Microsoft 365 Copilot uses the current Microsoft Learn all-features tab, which
  covers 2026. Platform tabs repeat the same batches and are excluded. Feature
  titles, app scope and first change summaries are retained; nested setup steps
  and impact boilerplate are omitted. Rollouts may be gradual. The linked public
  GitHub Markdown was older than the rendered Learn page, so Learn is authoritative
  for this acquisition. The separate consumer Copilot app is outside this source.
- Notion traverses every release archive page and covers both AI and general
  workspace changes. Explicit coming-soon blocks remain in source records but do
  not become shipped-change cards; hidden video-player errors are removed.
- Z.ai API records dated model announcements in its New Released notes. It does
  not claim full consumer-app coverage or independent verification of benchmark claims.
- Grok API and Kimi API candidates were deferred because their current changelogs
  provide month-level dates. Mistral and Perplexity sources could not be reliably
  fetched. No publication day or unavailable release text was invented.
- Existing **29-product** history retains all **3,993 release records** and original
  acquisition coverage, plus all **15,809 existing card records**. Source ranges indicate available endpoint coverage, not launch dates.
- **2,229 candidates remain pending review** (781 additional).
  They remain excluded from publication. New product eras have no editorial review;
  existing research summaries keep their original stated scope.

## Verification

Run: `more-products-2026-11-07-r2`, **candidate-applied**, **18,406 files** applied.

- **623 tests passed**, including pagination, type partitions, duplicate content,
  malformed dates, title-only records, source scope, roadmap filtering and the larger catalog.
- Literal inline code such as `[[hooks]]` is preserved as source text, while real
  links and relation targets remain validated. Regression tests cover both cases.
- Vault validation checked **24,804 Markdown files** and
  **391,248 links** with zero errors. The applied vault matches
  the validated candidate byte for byte.
- Quartz and publication checks passed: **23,445 active indexed pages**,
  **23,571 HTML pages**, **799,366 links**,
  and **30 RSS entries**. No broken graph edges or leaked review candidates.
- Site output: **894.7 MiB**; content index: **65.9 MiB**.
- Chrome verified all 37 homepage product links, all eight added product pages,
  and the final Model Support timeline filter (v0). Document width matches
  the viewport at 1440px and 390px; the comparison table scrolls internally.
  Console output and screenshots are retained in the evidence directory.
- **167 saved public HTTP responses** passed SHA-256 validation.
  Acquisition timestamps come from saved responses, not the later parser or generation time.

## Evidence and replay

The [evidence manifest](more-products-37-evidence/sha256.json) covers the normalized
collection, quality reports, HTTP manifest, preservation checks and browser evidence.
Original response bodies remain in the ignored local acquisition directory.

Sources were fetched on November 7, 2026. Generation replays that saved acquisition
and is labeled `replay`; it does not count as a scheduled live collection.

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id more-products-37-replay-unique \
  --output _pipeline/more-products-37-replay-unique \
  --collection docs/acceptance/more-products-37-evidence/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog
```

Publication follows the existing delivery PR, required Quality check and protected
main deployment workflow. Branch protection is unchanged.
