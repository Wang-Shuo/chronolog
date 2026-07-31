# ChronoLog

ChronoLog turns official product release histories into an Obsidian/Quartz vault of
Release pages, normalized Change Cards, product timelines, and cross-product themes.

## Official sources

- ChatGPT: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Claude Code: [anthropics/claude-code releases](https://github.com/anthropics/claude-code/releases)
- Cursor: [Cursor changelog](https://cursor.com/changelog)

## Full historical backfill

Run all three enabled sources and reconcile the generated vault against the complete
collected history:

```bash
python _scripts/run_pipeline.py \
  --run-id full-backfill-YYYY-MM-DD \
  --backfill chatgpt,claude-code,cursor \
  --today YYYY-MM-DD \
  --reconcile
```

The ChatGPT Help Center may return a Cloudflare `403` to non-browser clients. Save a
browser-rendered copy of the official page and pass it as an explicit source override:

```bash
python _scripts/run_pipeline.py \
  --run-id full-backfill-YYYY-MM-DD \
  --backfill chatgpt,claude-code,cursor \
  --snapshot chatgpt=/absolute/path/chatgpt-release-notes.html \
  --today YYYY-MM-DD \
  --reconcile
```

`--snapshot PRODUCT=PATH` replaces network collection only for that product; the
other requested products still use their official live sources. Keep the input under
`_pipeline/<run-id>/00-snapshots/` when its bytes and provenance need to remain
auditable with the run.

Theme classification is local and reproducible. Deterministic vocabulary rules handle
clear cases, `_scripts/backfill_review.yaml` records stable-ID semantic dispositions,
and unresolved items remain in
`_pipeline/<run-id>/02-extracted/theme_candidates.json` instead of being published.
Semantic review is performed with Codex reasoning; the pipeline does not call an
external LLM API.

## Development and fixture pipeline

Run the local MVP fixture pipeline:

```bash
python -m pytest
python _scripts/run_pipeline.py --fixture --run-id demo --today 2026-06-26 --reconcile
```

The pipeline runs both validation rounds. Candidate or ambiguous themes are held in
`_pipeline/<run-id>/02-extracted/theme_candidates.json` and are not published until
they are promoted into `_scripts/themes.yaml`. `--reconcile` is intended for a complete
fixture/backfill scope: missing historical cards are preserved in place and marked
`superseded: true`.

Collect recent live releases without reconciling historical cards:

```bash
python _scripts/run_pipeline.py --run-id live
```

Build the Quartz site:

```bash
npm install
npx quartz build
```

Quartz reads the Vault directories at the repository root directly. The ignored
`content/` directory is a disposable artifact from older builds and is not a source of
truth.

Preview locally:

```bash
npx quartz build --serve
```
