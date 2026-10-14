"""Offline M1 acceptance against an existing real vault in a NEW disposable directory.

Run from the repository root with its Python environment. Never writes source vault.
The historical collection is replay evidence, not a fresh fetch from official sources.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

import frontmatter

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from _scripts.collect import source_result
from _scripts.common import PipelinePaths, read_json, write_json
from _scripts.pipeline import run_pipeline
from _scripts.transaction import DIRECTORIES, snapshot


def envelope(releases, mode):
    products = sorted({r["product"] for r in releases})
    return {
        "source": "replay", "mode": mode, "releases": releases, "errors": [],
        "sources": [source_result(product, [r for r in releases if r["product"] == product],
                                  complete=mode == "full", coverage="historical-snapshot")
                    for product in products],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collection", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="New disposable directory")
    args = parser.parse_args()
    destination = args.output.resolve()
    if destination.exists():
        parser.error("output must not already exist")
    if destination.is_relative_to(ROOT):
        parser.error("output must be outside the source repository")
    baseline = snapshot(ROOT)
    releases = read_json(args.collection)["releases"]
    products = sorted({r["product"] for r in releases})
    destination.mkdir(parents=True)
    vault = destination / "vault"
    shutil.copytree(ROOT / "_scripts", vault / "_scripts", ignore=shutil.ignore_patterns("__pycache__"))
    for name in DIRECTORIES:
        if (ROOT / name).exists():
            shutil.copytree(ROOT / name, vault / name)
    shutil.copy2(ROOT / "index.md", vault / "index.md")
    results = {
        "input_sha256": hashlib.sha256(args.collection.read_bytes()).hexdigest(),
        "input_release_count": len(releases), "products": products,
        "execution": "offline historical replay; no live source freshness claim",
        "code_sha256": {
            p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((ROOT / "_scripts").glob("*.py"))
        },
        "steps": [],
    }

    def record(run_id, payload, **kwargs):
        result = run_pipeline(vault, run_id, collection=payload, today="2026-08-01", **kwargs)
        evidence = destination / "evidence" / run_id
        evidence.mkdir(parents=True)
        paths = PipelinePaths(run_id, vault)
        shutil.copy2(paths.run_dir / "manifest.json", evidence / "manifest.json")
        shutil.copy2(paths.validation_round2, evidence / "validation.json")
        summary = {key: result[key] for key in (
            "run_id", "status", "changed_files", "merged_releases", "merged_cards", "pending_theme_review"
        )}
        report = read_json(paths.validation_round2)
        summary.update(validation_errors=len(report["errors"]), links_checked=report["links_checked"])
        results["steps"].append(summary)
        print(json.dumps(summary), flush=True)
        return result

    record("full", envelope(releases, "full"), reconcile=True)
    path = next((vault / "Changes/ChatGPT").glob("*.md"))
    post = frontmatter.load(path)
    post["human_overrides"] = {"review_note": "M1 acceptance preservation check"}
    post.content += "\n\nM1 acceptance: human-owned note."
    path.write_text(frontmatter.dumps(post))
    # Prove that history does not depend on the previous run's intermediates.
    shutil.rmtree(vault / "_pipeline")
    latest = [max((r for r in releases if r["product"] == p),
                  key=lambda r: (r["date"], r["release_id"])) for p in products]
    before_incremental = snapshot(vault)
    incremental = record("incremental", envelope(latest, "incremental"))
    assert incremental["merged_releases"] == len(releases)
    assert snapshot(vault) == before_incremental
    before_repeat = snapshot(vault)
    repeat = record("repeat", envelope(latest, "incremental"))
    assert repeat["status"] == "no-change" and snapshot(vault) == before_repeat

    writes = []
    def fail(index, name):
        writes.append(name)
        if index == 2:
            raise OSError("M1 acceptance injected write failure")
    try:
        # Advance the evaluation date to create staged alerts on this historical
        # snapshot, ensuring the fault occurs during actual publication writes.
        run_pipeline(vault, "failure", collection=envelope(latest, "incremental"),
                     today="2026-10-13", after_write=fail)
    except OSError as exc:
        assert "injected write failure" in str(exc)
    else:
        raise AssertionError("fault injection did not execute")
    assert len(writes) == 3 and snapshot(vault) == before_repeat
    assert not (vault / "_pipeline/transaction.json").exists()
    failed_manifest = read_json(vault / "_pipeline/failure/manifest.json")
    results["fault"] = {"writes_before_failure": len(writes), "vault_restored": True,
                        "manifest_status": failed_manifest["status"]}
    write_json(destination / "evidence/failure/manifest.json", failed_manifest)
    record("recovered", envelope(latest, "incremental"))
    assert frontmatter.load(path)["human_overrides"]["review_note"] == "M1 acceptance preservation check"
    assert "M1 acceptance: human-owned note." in path.read_text()
    assert snapshot(ROOT) == baseline
    results.update(human_edits_preserved=True, prior_run_json_removed=True,
                   source_vault_unchanged=True, passed=True)
    write_json(destination / "results.json", results)
    print(f"Evidence: {destination / 'results.json'}", flush=True)


if __name__ == "__main__":
    main()
