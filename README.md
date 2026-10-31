# ChronoLog

ChronoLog turns official product release histories into an Obsidian/Quartz vault of
Release pages, normalized Change Cards, product timelines, and cross-product themes.

Current implementation status, priorities, and acceptance criteria are tracked in the
[development plan (2026-10-13)](docs/development-plan-2026-10-13.md). Product, UI and
content design recommendations for the reader-facing site are in the
[design review (2026-10-15)](docs/design-review-2026-10-15.md); delivery progress is
summarised in the [progress record (2026-10-17)](docs/progress-2026-10-17.md).
The pipeline merges historical Markdown with each new batch, validates a staged vault,
and publishes through a recoverable transaction. Content-quality and public-release
acceptance remain separate milestones.

## Setup

Python 3.11+ and a POSIX environment (macOS/Linux) are required; the pipeline uses a
filesystem lock to serialize writes. Install the Python dependencies and run tests:

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
```

## Official sources

- ChatGPT: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Claude Code: [anthropics/claude-code releases](https://github.com/anthropics/claude-code/releases)
- Cursor: [Cursor changelog](https://cursor.com/changelog)

## Daily incremental updates

```bash
python _scripts/run_pipeline.py
```

By default each source collects its recent window (up to 30 releases). The pipeline
merges that batch with historical Release and Change records read directly from
Markdown, then rebuilds the full managed product/theme indexes and relations.
Missing items in a recent window are not retired. A successful identical run reports
`no-change`; an HTTP error or unexpected empty source response reports failure and
leaves the vault unchanged.

Dates default to the execution day in `Asia/Shanghai`. Use `--timezone UTC` to change
the clock or `--today YYYY-MM-DD` for a historical replay. Source fetch timestamps
are recorded separately in UTC. Silence analysis uses merged history only for
sources successfully observed in this run.

Run IDs are generated automatically. An explicit `--run-id NAME` must be unused;
retry with a fresh ID to preserve previous diagnostics. `--root /path/to/vault`
selects another vault containing `_scripts` configuration, independently of the
shell's current directory.

## Full historical backfill and reconciliation

```bash
python _scripts/run_pipeline.py \
  --backfill chatgpt,claude-code,cursor \
  --reconcile
```

`--backfill` without a product list selects all enabled sources. `--reconcile`
requires a successful, unlimited full collection for every selected source. Only
that selected scope is reconciled: missing identities are preserved as
`superseded: true`, while unselected sources and pending-review records are protected.
An RSS feed window is not proof of complete history and cannot authorize reconciliation.
“Complete” means the available endpoint was traversed, not proof of lifetime coverage.

Without `--reconcile`, even a full collection only adds or updates identities. Use a
rehearsal copy to inspect the effect of a first migration or intentional retirement
of records before applying it to your working archive.

The ChatGPT Help Center may return a Cloudflare `403`. Save a browser-rendered copy
of the official page outside the new run directory, then supply it explicitly:

```bash
python _scripts/run_pipeline.py \
  --backfill chatgpt,claude-code,cursor \
  --snapshot chatgpt=/absolute/path/chatgpt-release-notes.html \
  --reconcile
```

The pipeline copies this input to the run's `00-snapshots/` directory and records its
hash, original path and file modification time. The modification time is not proof
of when the browser fetched the page; retain that provenance with the original input.
The override affects only ChatGPT; the other selected sources still use live endpoints.
A historical snapshot is not a fresh observation of the upstream site.

## Failure gates, review and recovery

Any requested source failure, invalid extracted card (Round 1 DLQ), machine-region
conflict, broken link or failed publication-set check blocks publication. Pending
theme candidates are normal review work, not validation failures.

Theme classification is local and reproducible. `_scripts/themes.yaml` defines the
vocabulary; `_scripts/backfill_review.yaml` records stable-ID decisions. The pipeline
does not call an external LLM API. Pending records persist as draft Markdown under
`_review/`, excluded from Quartz. Successful re-extraction after a vocabulary or
review-decision update promotes them; resolved review records and notes remain under
`_review/resolved/`. Published facts also persist in machine-owned `record` frontmatter,
so deleting completed run JSON does not remove historical inputs. Human regions,
custom frontmatter and `human_overrides` remain preserved.

Inspect `_pipeline/<run-id>/` for:

- `manifest.json`: source status, scope/completeness, evaluation date, phase and outcome.
- `01-collected/` and `02-extracted/`: the current batch and theme candidates.
- `03-merged/`: reconstructed historical inputs plus the new batch.
- `03a-analyzed-per/`, `03b-analyzed-cross/`, `03c-silence/`: merged analyses.
- `04-validated/`: full-vault link checks and any writer conflicts.
- `stage/`: unpublished or successfully verified staging output.

Invalid extracted cards are retained at `_pipeline/dlq/<run-id>-failed.json`.
On failure, fix the source/input or restore the intended machine-owned region and
rerun with a new run ID. Put editorial changes outside machine regions or in
`human_overrides` rather than removing `machine_hash` to bypass a conflict.

Publication journals `_pipeline/transaction.json` and its backup before replacing
files. Ordinary exceptions and handled interrupts trigger rollback. After process
termination, the next run recovers the unfinished transaction first. To recover
without collecting new data:

```bash
python _scripts/run_pipeline.py --recover-only
```

A journal already marked committed is cleaned up without reverting its content.
If a file was edited after interruption or a backup is corrupt, recovery stops and
identifies the conflict; preserve the journal and backups, save the conflicting edit,
and resolve it before retrying. Never delete `_pipeline/` while a run or transaction
is active. Keep acceptance evidence elsewhere before deleting completed runs.

Each file replacement is atomic; the entire multi-file vault is not a filesystem
snapshot. Run builds after the pipeline exits successfully. A second pipeline is
blocked by the vault lock, and edits detected during preparation prevent publication.

## Isolated fixture development

Fixture data must use a separate, initially empty vault. For example, from the
repository root:

```bash
fixture_root="$(mktemp -d /tmp/chronolog-fixture.XXXXXX)"
mkdir -p "$fixture_root/_scripts" "$fixture_root/tests"
cp _scripts/*.yaml "$fixture_root/_scripts/"
cp -R tests/fixtures "$fixture_root/tests/fixtures"
python _scripts/run_pipeline.py --root "$fixture_root" --fixture \
  --today 2026-06-26 --reconcile
```

The main pipeline rejects a fixture run against an archive containing live releases.
Individual stage scripts are debugging tools; calling `writer.py` directly bypasses
the transactional orchestrator and should only be done in disposable vaults.

## Offline replay and M1 verification

A saved collection from the new collector can be replayed without network access:

```bash
python _scripts/run_pipeline.py --root /absolute/path/to/disposable-vault \
  --collection /absolute/path/to/releases.json --today 2026-08-01
```

The file must include `mode`, per-source status, count, timestamp and completeness.
Old JSON without that metadata is rejected; it cannot silently authorize full
reconciliation. Replay source metadata is an explicit input contract, not an
independent audit of the upstream site's completeness.

For the M1 full → incremental → repeat → failure/recovery rehearsal on the historical
648-release snapshot, use the dedicated verification script. It copies the real
vault, removes prior run JSON between steps, and checks that source files stay unchanged:

```bash
python tests/manual/verify_m1_replay.py \
  --collection _pipeline/full-backfill-2026-08-01/01-collected/releases.json \
  --output /tmp/chronolog-m1-replay
```

The output directory must not exist. This historical input is ignored by Git and must
be supplied separately in another checkout; unit regressions remain fully offline.
Results and reports are saved under the output directory.

## Quartz site

```bash
npm install
npx quartz build
```

Quartz reads the repository-root vault. `content/` is an ignored, disposable artifact
from older builds. `_pipeline/`, `_review/`, `_scripts/`, tests and docs are not published.
The explicit three-product filter excludes legacy fixture products, fixture records
and superseded records from HTML, search, explorer and graph. Historical Markdown
remains available locally; there is no public archive route for retired records.

Preview locally:

```bash
npx quartz build --serve
```

## M2 content verification

The 2026-10-13 refresh contains 787 releases from ChatGPT, Claude Code and Cursor.
Source acquisition time and release date are separate on the home and product pages.
ChatGPT uses a dated official browser snapshot; Claude Code Releases starts at
v2.0.73 and is not a complete lifetime history. Rules extract at most five cards
per release; pending themes stay in `_review/`.

[Acceptance evidence](docs/acceptance/m2-2026-10-13.md) includes the compressed
source corpus, golden samples, actual publication checks and reproduction commands.
The user accepted the [human review packet](docs/acceptance/m2-review-packet.md) on
2026-10-13. M2 is complete; M3 operations remain pending. This acceptance covers
the fixed samples and three narratives, not every candidate in `_review/`.

Cited narratives live in `_scripts/editorial.yaml`; evidence IDs must exist in the
merged release set before product eras render. `m2_review.yaml` records specific
semantic corrections. Chronology does not automatically create `evolves_from` or
claim that one product adopted another's capability. Theme timelines are navigable
year lists, with two curated research summaries.


## M3 operations

[M3 runbook](docs/m3-operations.md) covers repository setup, the daily review PR,
automatic ChatGPT browser capture, source failure isolation, reviewed-commit deployment and evidence
retention. [Implementation evidence](docs/acceptance/m3-2026-10-13.md) separates
local checks from the seven real daily runs and public deployment still required.

The `Quality` workflow runs tests, golden samples, Vault validation, Quartz and
actual publication/RSS checks on every PR. `Generate review candidate` works in an
isolated copy and updates `codex/chronolog-updates` only after its gates pass.
Generation has read-only repository permissions. A separate publisher uses the
job-scoped `GITHUB_TOKEN` to push content, maintain a bot-authored PR and explicitly
dispatch Quality for its exact head. No bot account or long-lived PAT is required.
Timestamp-only acquisition changes produce a run report without opening a PR;
an existing PR still gets Quality dispatched to recover a previous trigger failure.
`Deploy reviewed site` accepts merged commits whose PR final head received human
approval; direct pushes do not deploy.

Local validation without changing the Vault:

```bash
.venv/bin/python -m _scripts.operations --mode check \
  --run-id local-quality-001 --output _pipeline/local-quality-001
```

Set `CHRONOLOG_BASE_URL=host/path` for the intended deployment. RSS is enabled and
checked against the active search index. The first reviewed Pages deployment is
live at https://wang-shuo.github.io/chronolog/. Repository permissions and branch
protection are configured. The temporary-credential workflow is enabled after reviewed PR #3 merged. Its
first live collection passed credential setup and collected Claude Code/Cursor;
Daily generation now tries an isolated Chromium browser when ChatGPT HTTP is blocked.
Captures are dated run artifacts, so they do not require a separate snapshot PR.
If a source remains unavailable, its existing archive is retained and marked delayed
while complete healthy sources continue; all-source failure or a missing historical
baseline still blocks generation. Content changes retain human review. Browser
access is not guaranteed, and seven real daily runs plus recovery/handoff acceptance
remain outstanding. See the
[M3 operations runbook](docs/m3-operations.md).
