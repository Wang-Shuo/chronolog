"""Transactional full/incremental pipeline. Markdown is the historical input."""
from __future__ import annotations

from datetime import datetime
import hashlib
from pathlib import Path
import shutil
from typing import Any, Callable
from zoneinfo import ZoneInfo

import frontmatter

from _scripts.analyze_a import analyze_products
from _scripts.analyze_b import analyze_themes
from _scripts.collect import collect_fixture, collect_live, load_sources
from _scripts.common import PipelinePaths, read_json, utc_timestamp, write_json
from _scripts.extract import extract_run
from _scripts.editorial import (attach_editorial, key_moments, load_editorial, source_coverage,
                                theme_narratives)
from _scripts.history import merge_history, read_history, write_pending
from _scripts.silence_monitor import cadence_anchor, cadence_summary, detect_silence
from _scripts.transaction import copy_pages, files, publish, recover, snapshot, vault_lock
from _scripts.validate import validate_cards_file, validate_vault_links
from _scripts.writer import content_machine_hash, write_run


def execution_date(timezone: str = "Asia/Shanghai") -> str:
    return datetime.now(ZoneInfo(timezone)).date().isoformat()


def check_collection(payload: dict[str, Any], reconcile: bool, allow_partial: bool = False) -> set[str]:
    sources = payload.get("sources", [])
    if not sources or (not allow_partial and (payload.get("errors") or any(s.get("status") != "success" for s in sources))):
        raise ValueError(f"collection failed: {payload.get('errors') or sources or 'no requested sources'}")
    if len({s['product'] for s in sources}) != len(sources):
        raise ValueError("duplicate source status")
    if any(s.get('status') not in {'success', 'failed'} for s in sources):
        raise ValueError('invalid source status')
    failed = {s['product'] for s in sources if s['status'] == 'failed'}
    if any(e.get('product') not in failed for e in payload.get('errors', [])):
        raise ValueError('unattributed collection error')
    requested = {s['product'] for s in sources if s['status'] == 'success'}
    if not requested:
        raise ValueError('collection failed: no successful sources')
    if payload.get("mode") not in {"full", "incremental"}:
        raise ValueError("collection must declare full or incremental mode")
    if reconcile and (payload["mode"] != "full" or any(not s.get("complete") for s in sources if s['product'] in requested)):
        raise ValueError("reconcile requires complete full collection for every requested source")
    releases = payload.get("releases", [])
    ids = set()
    for release in releases:
        for key in ("release_id", "product", "product_name", "date", "title", "source_url", "body"):
            if key not in release:
                raise ValueError(f"collected release missing {key}")
        if release["release_id"] in ids or release["product"] not in requested:
            raise ValueError("duplicate release identity or unexpected product")
        ids.add(release["release_id"])
        for key in ("product", "product_name", "release_id"):
            value = str(release[key])
            if value in {"", ".", ".."} or "/" in value or "\\" in value:
                raise ValueError(f"unsafe {key}: {value}")
    for source in sources:
        if source['product'] in failed:
            if source.get('count') != 0 or source.get('complete') or not source.get('error'):
                raise ValueError('failed source must contain no accepted data and explain its failure')
            continue
        count = sum(r["product"] == source["product"] for r in releases)
        if source.get("count") != count or not source.get("collected_at"):
            raise ValueError(f"source manifest count/time mismatch: {source['product']}")
        if not count and source.get("coverage") != "no-change":
            raise ValueError(f"unexpected empty collection for {source['product']}")
        if not count and reconcile:
            raise ValueError("empty no-change inputs cannot reconcile history")
    return requested


def check_machine_hashes(root: Path) -> None:
    for name, path in files(root).items():
        text = path.read_text()
        post = frontmatter.loads(text)
        if post.get("machine_hash") and content_machine_hash(text) != post["machine_hash"]:
            raise ValueError(f"machine_hash conflict: {name}")


def run_pipeline(
    root: Path, run_id: str, *, fixture: bool = False, backfill: str | None = None,
    limit: int | None = None, snapshot_paths: dict[str, Path] | None = None,
    today: str | None = None, timezone: str = "Asia/Shanghai", reconcile: bool = False,
    collection: dict[str, Any] | None = None,
    allow_partial: bool = False,
    after_write: Callable[[int, str], None] | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    paths = PipelinePaths(run_id, root)
    effective_today = today or execution_date(timezone)
    datetime.strptime(effective_today, "%Y-%m-%d")
    ZoneInfo(timezone)
    if limit is not None and limit <= 0:
        raise ValueError("limit must be positive")
    with vault_lock(root):
        recovered = recover(root)
        if paths.run_dir.exists():
            raise ValueError(f"run-id already exists; use a fresh id: {run_id}")
        manifest: dict[str, Any] = {
            "run_id": run_id, "started_at": utc_timestamp(), "today": effective_today,
            "timezone": timezone, "status": "preparing", "reconcile": reconcile,
            "recovered_run": recovered, "sources": [],
        }
        manifest_path = paths.run_dir / "manifest.json"
        write_json(manifest_path, manifest)
        before = snapshot(root)
        stage = paths.run_dir / "stage"
        try:
            sources = load_sources(root / "_scripts/sources.yaml")
            saved_snapshots = {}
            for product, path in (snapshot_paths or {}).items():
                if product not in {s["name"] for s in sources if s["feed_type"] == "chatgpt_changelog"}:
                    raise ValueError(f"unsupported snapshot source: {product}")
                saved = paths.run_dir / "00-snapshots" / f"{product}.html"
                saved.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, saved)
                saved_snapshots[product] = saved
                manifest.setdefault("snapshots", {})[product] = {
                    "original_path": str(path), "sha256": hashlib.sha256(saved.read_bytes()).hexdigest(),
                }
            if collection is None:
                if fixture:
                    collection = collect_fixture(root / "tests/fixtures/releases.json", paths.collected)
                else:
                    collection = collect_live(
                        root / "_scripts/sources.yaml", paths.collected,
                        limit if limit is not None else None if backfill else 30,
                        backfill, saved_snapshots,
                    )
            else:
                write_json(paths.collected, collection)
            manifest.update(mode=collection.get("mode"), sources=collection.get("sources", []),
                            collection_errors=collection.get("errors", []))
            write_json(manifest_path, manifest)
            requested = check_collection(collection, reconcile, allow_partial)
            configured = {s['name'] for s in sources}
            failed_products = {s['product'] for s in collection['sources'] if s['status'] == 'failed'}
            if failed_products - configured:
                raise ValueError('cannot retain an unknown failed source')
            if limit is not None and reconcile:
                raise ValueError("reconcile cannot use a limited collection")
            managed = requested | {source["name"] for source in sources}
            if collection.get("source") == "fixture":
                for path in (root / "Releases").rglob("*.md"):
                    if frontmatter.load(path).get("source_type") not in {None, "fixture"}:
                        raise ValueError("fixture runs require a separate vault from live data")
            check_machine_hashes(root)
            manifest["phase"] = "extraction"
            extract_run(run_id, root=root)
            round1 = validate_cards_file(paths.extracted, paths.valid_cards, paths.dlq,
                                         root / "_scripts/themes.yaml")
            manifest["round1"] = round1
            if round1["failed"]:
                raise ValueError("round 1 failed; inspect the DLQ; vault was not changed")
            batch = read_json(paths.valid_cards)
            history = read_history(root, managed)
            historical_products = {r["product"] for r in history[0]}
            if failed_products - historical_products:
                raise ValueError('failed source requires an existing historical source baseline')
            if any(s.get("coverage") == "no-change" and s["product"] not in historical_products
                   for s in collection["sources"]):
                raise ValueError("no-change requires an existing historical source baseline")
            reconcile_products = requested if reconcile else set()
            releases, cards, pending = merge_history(
                history, collection["releases"], batch["change_cards"],
                batch.get("pending_theme_review", []), reconcile_products,
            )
            manifest.update(requested_products=sorted(requested),
                            retained_products=sorted(failed_products),
                            collection_health='degraded' if failed_products else 'healthy',
                            reconcile_products=sorted(reconcile_products),
                            merged_releases=len(releases), merged_cards=len(cards),
                            pending_theme_review=len(pending), phase="staging")
            stage.mkdir()
            copy_pages(root, stage, create_missing=True)
            staged = PipelinePaths(run_id, stage)
            merged_payload = {"change_cards": cards, "pending_theme_review": pending}
            write_json(staged.collected, {"releases": releases})
            write_json(staged.valid_cards, merged_payload)
            write_json(paths.run_dir / "03-merged/releases.json", {"releases": releases})
            write_json(paths.run_dir / "03-merged/cards.json", merged_payload)
            analysis_a, analysis_b = analyze_products(cards), analyze_themes(cards)
            editorial = load_editorial(root)
            attach_editorial(analysis_a, releases, editorial)
            # Narratives citing a release missing from the run, and curated key moments
            # that are not active cards of their theme, are dropped and listed here.
            analysis_b['editorial'], narrative_warnings = theme_narratives(editorial, releases)
            analysis_b['key_moments'], moment_warnings = key_moments(editorial, cards)
            manifest['editorial_warnings'] = narrative_warnings + moment_warnings
            source_states = {s['product']: s for s in collection['sources']}
            for product, info in analysis_a['products'].items():
                page = root / 'Products' / f"{info['product_name']}.md"
                previous = frontmatter.load(page).get('coverage', {}) if page.exists() else {}
                info['coverage'] = source_coverage(source_states.get(product),
                    [r for r in releases if r['product'] == product], previous)
            silence = detect_silence(releases, [s for s in sources if s["name"] in requested], effective_today)
            silence['pending'].extend({'product': p, 'silence_tracking': 'collection-error',
                                       'reason': 'collection delayed; historical content retained'}
                                      for p in sorted(failed_products))
            # Cadence is measured to the newest archived release (not the clock), so the
            # same archive renders the same product pages on any day; alerts keep the clock.
            silence["cadence"] = cadence_summary(
                releases, sources, cadence_anchor(releases, effective_today), silence["alerts"]
            )
            for product in failed_products:
                if product in silence['cadence']:
                    silence['cadence'][product]['status'] = 'collection-delayed'
            for dest, value in ((staged.analyze_a, analysis_a), (staged.analyze_b, analysis_b),
                                (staged.silence, silence), (paths.analyze_a, analysis_a),
                                (paths.analyze_b, analysis_b), (paths.silence, silence)):
                write_json(dest, value)
            conflicts = write_run(run_id, root=stage, reconcile=reconcile,
                                  reconcile_products=reconcile_products, config_root=root)
            # Non-blocking list of pages kept on a legacy skeleton because of human text.
            migration_pending = staged.run_dir / "writer-migration-pending.json"
            manifest["writer_migration_pending"] = (
                len(read_json(migration_pending)) if migration_pending.exists() else 0
            )
            if migration_pending.exists():
                shutil.copy2(migration_pending, paths.run_dir / migration_pending.name)
            if conflicts:
                write_json(paths.run_dir / "04-validated/writer-conflicts.json", conflicts)
                raise ValueError("writer conflicts; staged changes were not published")
            write_pending(stage, pending, managed)
            report = validate_vault_links(stage, releases, cards, pending)
            write_json(paths.validation_round2, report)
            if report["errors"]:
                raise ValueError("round 2 failed; staged changes were not published")
            check_machine_hashes(stage)
            actual_releases, actual_cards, actual_pending = read_history(stage, managed)
            for actual, expected, key in ((actual_releases, releases, "release_id"),
                                          (actual_cards, cards, "card_id"),
                                          (actual_pending, pending, "card_id")):
                if {r[key] for r in actual} != {r[key] for r in expected}:
                    raise ValueError(f"staged publication set mismatch: {key}")
            manifest["phase"] = "publication"
            write_json(manifest_path, manifest)
            count = publish(root, stage, before, run_id, after_write=after_write)
            manifest.update(status="published" if count else "no-change", changed_files=count,
                            phase="complete", completed_at=utc_timestamp())
            write_json(manifest_path, manifest)
            return manifest
        except BaseException as exc:
            manifest.update(status="failed", error=f"{type(exc).__name__}: {exc}",
                            completed_at=utc_timestamp())
            if manifest.get("phase") in {None, "extraction"}:
                write_json(paths.silence, {"alerts": [], "pending": [
                    {"product": s.get("product"), "silence_tracking": "collection-error",
                     "reason": s.get("error") or "run did not pass collection gates"}
                    for s in manifest["sources"] if s.get("status") != "success"
                ]})
            write_json(manifest_path, manifest)
            raise
