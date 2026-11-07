# Trending product expansion to 29 — 2026-11-07

ChronoLog now tracks **29 products**, with **3,993 releases**
and **15,809 Change Cards**. Nine additions contribute
**766 official release records** and **2,561 published cards**.

| Added product | Releases | Cards | Archived publication dates | Source |
| --- | ---: | ---: | --- | --- |
| Suno | 76 | 152 | 2023-12-23 → 2026-11-06 | [Official source](https://suno.com/release-notes) |
| Runway | 161 | 115 | 2024-01-08 → 2026-10-27 | [Official source](https://runway.com/changelog) |
| Midjourney | 96 | 212 | 2024-03-07 → 2026-10-08 | [Official source](https://updates.midjourney.com/) |
| Gamma | 78 | 93 | 2024-02-14 → 2026-10-26 | [Official source](https://ideas.gamma.app/changelog) |
| Granola | 25 | 18 | 2024-05-22 → 2026-09-02 | [Official source](https://www.granola.ai/updates) |
| Google Antigravity | 70 | 318 | 2025-11-18 → 2026-11-03 | [Official source](https://antigravity.google/docs/changelog) |
| Manus | 35 | 21 | 2025-05-11 → 2026-09-29 | [Official source](https://www.manus.im/updates) |
| OpenClaw | 24 | 442 | 2026-06-30 → 2026-11-05 | [Official source](https://docs.openclaw.ai/releases) |
| OpenCode | 201 | 1,190 | 2025-12-19 → 2026-11-06 | [Official source](https://opencode.ai/changelog) |

## Selection and source scope

The selection expands music, video, image creation, presentations, meetings and
agent workflows. Recent discovery used the [a16z October 2026 consumer AI report](https://a16z.com/100-gen-ai-apps-7/)
and [Torii October 2026 enterprise adoption report](https://www.toriihq.com/research/reports/ai-breakout-october-2026),
then checked each product's official public update history. These reports use
different traffic, spending and adoption measures; this is a curated expansion,
not a universal popularity ranking or a claim that every product was recently launched.

- Suno and Runway collect every dated entry currently rendered on their official
  release pages. Runway's same-day announcements retain separate identities.
- Midjourney traverses all 96 posts in its official sitemap, using article
  publication dates rather than sitemap modification dates or dates in titles.
  The source archive retains roadmap sections; these do not become shipped-change cards.
- Gamma traverses all cumulative public changelog pages with an explicit published
  filter. Manus follows the official public notification cursor and verifies the total;
  private notifications are excluded. Both collectors fail on repeated or incomplete pages.
- Granola records dated summaries from its official updates index, including launch
  and company announcements there; it does not claim full blog-body coverage.
- Antigravity covers the App (hub) and original IDE. Other editor extensions, SDK,
  CLI and undated model-launch cards are outside the stated scope. Surface and
  version jointly identify releases.
- OpenClaw traverses the complete curated documentation index. Publication dates
  come from matching stable GitHub tags: for example, v2026.11.1 was published on
  November 5, not November 1. Older technical histories outside this index are excluded.
- OpenCode follows all older-updates pages, preserving feature paragraphs even when
  a release is nested in an outer HTML list. Missing pages fail the whole source.
- Music generation, video generation, presentation creation and meeting notes now
  have dedicated themes. Existing twenty-product history retains its original
  identities, source text, dates and acquisition provenance.
- **1,448 candidates remain pending review** (393 additional).
  These remain excluded from publication. New product eras have no editorial review;
  existing research summaries keep their stated original scope.

## Verification

Run: `trending-products-2026-11-07-r2`, **candidate-applied**, **15,480 files** applied.

- **580 tests passed**; pagination, published-only filtering, malformed dates,
  source boundaries, same-day identities and filters at the 29-product catalog size are covered.
- Vault validation checked **21,273 Markdown files** and
  **343,154 links**, with zero errors. The applied vault matches
  the validated candidate byte for byte.
- Quartz and publication checks passed: **19,914 active indexed pages**,
  **20,016 HTML pages**, **689,774 links**,
  and **30 RSS entries**. No broken graph edges or leaked review candidates.
- Site output: **767.3 MiB**. The content index is **57.5 MiB**.
- Chrome verified all 29 homepage product links and the last Model Support timeline filter
  (v0, number 28; Granola has no Model Support cards).
  Document width matches the viewport at 1440px and 390px; the comparison table
  scrolls internally. All nine added product pages have correct titles and rendered
  content. Console: zero errors and warnings; output is retained in the evidence directory.
- **181 saved public HTTP responses** passed SHA-256 verification.
  Acquisition timestamps come from the recorded responses, including reparsed data;
  they are not reset to the later parser or generation time.

## Evidence and replay

The [evidence manifest](trending-products-29-evidence/sha256.json) covers the normalized
collection, quality reports, logs, HTTP manifest, history-preservation check and
browser checks/screenshots. Original response bodies remain in the ignored local
acquisition directory; per-response hashes and URLs are retained in this evidence.

Sources were fetched on November 7, 2026. Generation replays the saved acquisition
and is labeled `replay`; it does not count as a scheduled live collection.

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id trending-products-29-replay-unique \
  --output _pipeline/trending-products-29-replay-unique \
  --collection docs/acceptance/trending-products-29-evidence/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog
```

Publication follows the existing delivery PR, required Quality check and protected
main deployment workflow. Branch protection is unchanged.
