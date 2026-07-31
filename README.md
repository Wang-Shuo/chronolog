# ChronoLog

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
