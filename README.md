# ChronoLog

Run the local MVP fixture pipeline:

```bash
python -m pytest
python _scripts/run_pipeline.py --fixture --run-id demo --today 2026-06-26
```

Build the Quartz site:

```bash
npm install
npx quartz build
```

Preview locally:

```bash
npx quartz build --serve
```
