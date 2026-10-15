"""Locked, journaled vault publication with rollback and restart recovery.

Each file replacement is atomic. The vault as a whole is not a filesystem snapshot:
readers should consume the built site, and builds must run after this command exits.
An interrupted multi-file commit is rolled back before the next run can start.
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
from contextlib import contextmanager
from pathlib import Path
import shutil
from typing import Callable

from _scripts.common import PipelinePaths, utc_timestamp
from _scripts.validate import ROOT_PAGES, VAULT_DIRECTORIES

DIRECTORIES = (*VAULT_DIRECTORIES, "_review")


def files(root: Path) -> dict[str, Path]:
    paths = [root / name for name in ROOT_PAGES if (root / name).exists()]
    for directory in DIRECTORIES:
        paths.extend((root / directory).rglob("*.md"))
    if any(p.is_symlink() or not p.resolve().is_relative_to(root.resolve()) for p in paths):
        raise ValueError("vault paths must be regular files inside the vault")
    return {p.relative_to(root).as_posix(): p for p in sorted(paths)}


def copy_pages(source: Path, destination: Path, *, create_missing: bool = False) -> None:
    """Copy every Vault directory and root page from ``source`` into ``destination``."""
    for directory in DIRECTORIES:
        if (source / directory).exists():
            shutil.copytree(source / directory, destination / directory)
        elif create_missing:
            (destination / directory).mkdir()
    for name in ROOT_PAGES:
        if (source / name).exists():
            shutil.copy2(source / name, destination / name)


def digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def snapshot(root: Path) -> dict[str, str | None]:
    return {name: digest(path) for name, path in files(root).items()}


def sync_directory(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.chronolog-tmp")
    try:
        with temporary.open("wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        sync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def vault_lock(root: Path):
    directory = root / "_pipeline"
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "vault.lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("another pipeline run holds the vault lock") from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def recover(root: Path) -> str | None:
    journal_path = root / "_pipeline/transaction.json"
    if not journal_path.exists():
        return None
    journal = json.loads(journal_path.read_text())
    backup = root / "_pipeline/transaction-backup"
    if journal["status"] != "committed":
        # Inspect everything first: do not silently overwrite edits made after a crash.
        for entry in journal["files"]:
            relative = Path(entry["path"])
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError("invalid transaction path")
            target = root / relative
            if target.is_symlink() or not target.resolve().is_relative_to(root.resolve()):
                raise ValueError("transaction path escapes vault")
            if digest(target) not in {entry["before"], entry["after"]}:
                raise RuntimeError(f"recovery conflict; preserve and inspect {target}")
            if entry["before"] is not None and digest(backup / relative) != entry["before"]:
                raise RuntimeError(f"missing/corrupt recovery backup: {relative}")
        for entry in journal["files"]:
            target = root / entry["path"]
            if entry["before"] is None:
                target.unlink(missing_ok=True)
            else:
                atomic_write(target, (backup / entry["path"]).read_bytes())
        for name in journal.get("new_directories", []):
            path = root / name
            if path.exists() and not any(path.iterdir()):
                path.rmdir()
    manifest_path = PipelinePaths(journal["run_id"], root).run_dir / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        manifest.update(
            status="published" if journal["status"] == "committed" else "recovered",
            recovery="commit-cleanup" if journal["status"] == "committed" else "rolled-back",
            completed_at=utc_timestamp(),
        )
        atomic_write(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2).encode())
    journal_path.unlink()
    sync_directory(journal_path.parent)
    shutil.rmtree(backup, ignore_errors=True)
    return journal["run_id"]


def publish(
    root: Path, stage: Path, before: dict[str, str | None], run_id: str,
    after_write: Callable[[int, str], None] | None = None,
) -> int:
    if snapshot(root) != before:
        raise RuntimeError("vault changed during preparation; refusing to overwrite concurrent edits")
    staged = files(stage)
    after = snapshot(stage)
    changes = [
        {"path": name, "before": before.get(name), "after": after.get(name)}
        for name in sorted(before.keys() | after.keys()) if before.get(name) != after.get(name)
    ]
    if not changes:
        return 0
    backup = root / "_pipeline/transaction-backup"
    if (root / "_pipeline/transaction.json").exists():
        raise RuntimeError("recover the previous transaction before publishing")
    shutil.rmtree(backup, ignore_errors=True)
    new_dirs = {name for name in DIRECTORIES if not (root / name).exists()}
    for entry in changes:
        target = root / entry["path"]
        if entry["before"] is not None:
            atomic_write(backup / entry["path"], target.read_bytes())
        parent = target.parent
        while parent != root and not parent.exists():
            new_dirs.add(parent.relative_to(root).as_posix())
            parent = parent.parent
    journal = {"run_id": run_id, "status": "applying", "files": changes,
               "new_directories": sorted(new_dirs, key=lambda p: len(Path(p).parts), reverse=True)}
    journal_path = root / "_pipeline/transaction.json"
    atomic_write(journal_path, json.dumps(journal).encode())
    try:
        for directory in DIRECTORIES:
            (root / directory).mkdir(exist_ok=True)
        for index, entry in enumerate(changes):
            target = root / entry["path"]
            if digest(target) != entry["before"]:
                raise RuntimeError(f"vault changed during commit: {entry['path']}")
            if entry["after"] is None:
                target.unlink()
                sync_directory(target.parent)
            else:
                atomic_write(target, staged[entry["path"]].read_bytes())
            if after_write:
                after_write(index, entry["path"])
        journal["status"] = "committed"
        atomic_write(journal_path, json.dumps(journal).encode())
    except BaseException:
        recover(root)
        raise
    recover(root)  # A committed journal only needs cleanup, not rollback.
    return len(changes)
