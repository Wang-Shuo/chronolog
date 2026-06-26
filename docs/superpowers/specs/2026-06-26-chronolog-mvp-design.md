# ChronoLog MVP Design

## Background

ChronoLog is an Obsidian-first product changelog archive. The PRD defines a broad roadmap, but the approved MVP scope for this implementation is **Phase 1: Core Validation** from `docs/chronolog-prd.md`.

The repository currently starts from the PRD only. This design initializes the minimum product system needed to prove the Phase 1 value claims:

- A product page can show readable product evolution eras instead of a flat release list.
- A theme page can aggregate related change cards across products and show a Mermaid comparison timeline.
- Backfilled tier-1 sources can produce enough historical depth to make trend exploration meaningful.

## Scope

The MVP includes:

- Standard Obsidian Vault directories at the repository root.
- Python scripts under `_scripts/` for collection, extraction, validation, analysis, silence detection, and Markdown rendering.
- Tier-1 data source support for GitHub Releases and RSS feeds.
- Historical backfill via `collect.py --backfill`.
- Controlled theme vocabulary in `_scripts/themes.yaml`.
- Deterministic fallback extraction so the pipeline can run without LLM credentials.
- Stable `card_id` generation from product, release date, and normalized evidence quote hash.
- JSON schema validation and DLQ isolation for invalid extracted records.
- Minimal Analyzer-A output: eras, product-local `evolves_from`, and `verbosity_baseline`.
- Minimal Analyzer-B output: related cards and tracked-products-only diffusion metadata by theme.
- Pure Python silence detection based on per-product release frequency.
- Writer ownership model with machine regions, machine frontmatter fields, preserved human regions, and `machine_hash`.
- Theme MOC rendering with Mermaid timeline blocks.
- Basic Quartz configuration so the Vault can be previewed locally.
- Pytest coverage for the pipeline behaviors that protect data integrity.

The MVP excludes:

- GitHub Actions PR gate, metrics reports, signal generation, evals, public deployment, newsletter, custom Quartz theme, interactive React timelines, Canvas rendering, user accounts, paid features, tier-2/tier-3 sources, and social/media sources.
- Claims of industry-wide originator status. Diffusion roles are only within the currently tracked product set.
- Automatic publication without human review.

## Architecture

The repository root is the Obsidian Vault and the static-site content source. Generated Markdown is the single source of truth for durable content; JSON under `_pipeline/` is an intermediate artifact that can be regenerated.

Directory layout:

```text
.
├── _scripts/
│   ├── analyze_a.py
│   ├── analyze_b.py
│   ├── collect.py
│   ├── common.py
│   ├── extract.py
│   ├── pipeline.py
│   ├── run_pipeline.py
│   ├── silence_monitor.py
│   ├── sources.yaml
│   ├── themes.yaml
│   ├── validate.py
│   └── writer.py
├── _pipeline/
│   ├── dlq/
│   └── <run-id>/
├── _templates/
├── Alerts/
├── Changes/
├── Products/
├── Releases/
├── Themes/
├── docs/
├── tests/
├── index.md
├── package.json
├── pyproject.toml
└── quartz.config.ts
```

Each script has a narrow responsibility and can be run independently. `run_pipeline.py` coordinates the Phase 1 local path.

## Data Flow

1. `collect.py` reads `_scripts/sources.yaml` and fetches configured tier-1 sources.
2. Collected releases are written to `_pipeline/<run-id>/01-collected/releases.json`.
3. `extract.py` reads collected releases and `_scripts/themes.yaml`, then writes Change Card JSON to `_pipeline/<run-id>/02-extracted/change_cards.json`.
4. `validate.py --round 1` validates extracted JSON. Valid records are written to `_pipeline/<run-id>/02-extracted/valid_change_cards.json`; invalid records are copied to `_pipeline/dlq/`.
5. `analyze_a.py` groups valid cards by product and writes eras, `evolves_from` patches, and `verbosity_baseline`.
6. `analyze_b.py` groups valid cards by theme and writes `related_changes` and `diffusion` patches.
7. `silence_monitor.py` computes update-frequency alerts from collected releases and source configuration.
8. `writer.py` renders Products, Releases, Changes, Themes, Alerts, and `index.md`.
9. Quartz builds the Markdown Vault into a local static site.

## Data Sources

The MVP ships with 5-8 AI coding assistant sources where GitHub Releases or RSS feeds are available. A source may be disabled if the upstream endpoint is unavailable during local development, but the script must report that failure without crashing the whole run.

Supported source types:

- `github_releases`: uses the public GitHub releases API.
- `blog_rss`: uses RSS/Atom feed parsing.

Backfill behavior:

- `backfill: full` fetches all available entries up to a configurable cap for local practicality.
- `backfill: {since: YYYY-MM-DD}` fetches entries on or after that date.
- `backfill: none` skips historical fetch and only collects current feed/API entries.

## Extraction

The extraction boundary follows the PRD's fact-layer rule. `extract.py` does not generate cross-product claims.

Each card includes:

- `type`
- `card_id`
- `product`
- `product_name`
- `source_release`
- `date`
- `title`
- `slug`
- `theme`
- `impact`
- `description`
- `comparison`
- `evidence`
- `extractor_version`
- optional `theme_suggestion`
- optional `ai_generated` and `confidence` only for significant or paradigm-shift cards

`card_id` format:

```text
{product-slug}-{release-date}-{hash6}
```

`hash6` is the first six hex characters of a SHA-256 digest of the normalized primary evidence quote.

LLM behavior:

- If an API key and model configuration are present, `extract.py` can call an LLM adapter.
- If no credentials are present, deterministic fallback extraction creates auditable cards from release titles, headings, bullets, and theme aliases.
- The fallback exists to keep Phase 1 locally runnable; it is not presented as final editorial quality.

## Validation And DLQ

`validate.py --round 1` checks:

- Required fields are present.
- `theme` is an official theme slug or `__candidate__` with `theme_suggestion`.
- `impact` is one of `incremental`, `significant`, or `paradigm-shift`.
- `evidence` contains at least one item with `source_release` and `quote`.
- `card_id` matches the deterministic identity format.
- `description` is non-empty.

Invalid records are written to `_pipeline/dlq/<run-id>-failed.json` with the original record and validation errors. Valid records continue through the pipeline.

## Analysis

Analyzer-A MVP:

- Groups cards by product.
- Computes `verbosity_baseline` as cards per release.
- Creates eras from time ranges and dominant themes. A product with enough history should render at least two eras; products with sparse data render one era with an explicit `data_sparse` marker.
- Adds simple `evolves_from` links between cards for the same product and theme ordered by date.

Analyzer-B MVP:

- Groups cards by theme.
- Adds `related_changes` links for cards sharing a theme across products.
- Computes diffusion metadata within the tracked product set:
  - `scope: tracked-products-only`
  - `role: originator`, `follower`, or `variant`
  - `first_in_tracked`
  - `lag_days`
  - `tracked_products_count`

## Silence Detection

`silence_monitor.py` is pure Python and does not call an LLM.

For each product with `track_silence: true`, it calculates release counts in configured windows and compares the current window with the historical baseline. If the product has insufficient history, it records `silence_tracking: pending` instead of producing an alarm.

When a product crosses the configured threshold, the script writes an alert JSON that `writer.py` renders to `Alerts/{date}-{product}-silence.md`.

## Writer Ownership Model

`writer.py` renders deterministic Markdown and preserves human-owned content.

Rules:

- Machine-generated body content is wrapped in `<!-- chronolog:begin region="..." -->` and `<!-- chronolog:end -->`.
- On update, only machine regions are replaced.
- Content outside machine regions is preserved.
- Human overrides can be stored in `human_overrides` frontmatter and are never written by the pipeline.
- `machine_hash` is computed from normalized machine fields and machine-region content, excluding `machine_hash` itself.
- If a current file's machine-region content does not match its stored `machine_hash`, the writer skips that file, preserves it, and records a merge conflict entry in DLQ.

Markdown output:

- Products: frontmatter, product summary, eras, change timeline.
- Releases: source summary and linked change cards.
- Changes: fact description, evidence, evolution links, diffusion, optional folded AI note.
- Themes: theme definition, Mermaid comparison timeline, cards by date, involved products.
- Alerts: silence signal details.
- `index.md`: product count, change count, theme count, links to product and theme pages.

## Quartz Preview

The MVP includes the minimum files needed to install and build Quartz v4 locally:

- `package.json`
- `quartz.config.ts`
- `quartz.layout.ts` if required by the installed Quartz version

The preview command is:

```bash
npm install
npx quartz build --serve
```

If Quartz package behavior changes, the implementation should keep the local static preview working and document the exact command in `README.md`.

## Testing

The implementation uses pytest and test fixtures that avoid network access by default.

Required tests:

- Stable `card_id` generation for repeated extraction of the same release.
- Theme alias normalization and candidate theme handling.
- Round-1 validation passes valid records and sends invalid records to DLQ.
- Analyzer-A creates eras and same-product `evolves_from` links.
- Analyzer-B creates tracked-products-only diffusion metadata.
- Silence monitor emits pending status for sparse history and alerts for configured silence.
- Writer preserves human content outside machine regions.
- Writer detects machine-region edits via `machine_hash`.
- Theme MOC contains a Mermaid timeline for cards across products.
- End-to-end fixture pipeline creates Products, Changes, Releases, Themes, Alerts, and `index.md`.

## Acceptance Criteria

The MVP is complete when these commands run successfully:

```bash
python -m pytest
python _scripts/run_pipeline.py --fixture --run-id demo
python _scripts/validate.py --round 1 --run-id demo
npm install
npx quartz build
```

The generated Vault must contain:

- At least five configured tier-1 products in `_scripts/sources.yaml`.
- Official themes in `_scripts/themes.yaml`.
- Product pages in `Products/`.
- Change Cards in `Changes/<Product>/`.
- Release pages in `Releases/<Product>/`.
- Theme MOCs in `Themes/` with Mermaid timelines.
- An `index.md` linking the generated archive.

Manual inspection must confirm:

- A product page shows eras, not only a release list.
- A theme page aggregates multiple products under one theme.
- The Mermaid timeline makes product ordering by date visible.
- Human-authored content outside machine regions survives a rerun.

## Implementation Notes

The implementation should prefer small, testable Python modules over large scripts. Shared parsing, slugging, hashing, frontmatter, and path helpers belong in `_scripts/common.py`. Network-facing collection code must have fixture-mode equivalents so tests and demos do not depend on live endpoints.

The first implementation can use deterministic analysis instead of LLM analysis as long as the data contracts match the PRD and the pipeline can adopt LLM-backed logic in a future phase without rewriting Writer or Validator.
