from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import signal
import sys
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.collect import parse_snapshot_args, positive_int
from _scripts.common import read_json
from _scripts.pipeline import run_pipeline
from _scripts.transaction import recover, vault_lock


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT, help="Vault with _scripts configuration")
    parser.add_argument("--run-id", default=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid4().hex[:8])
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--backfill", nargs="?", const="all")
    parser.add_argument("--limit", type=positive_int)
    parser.add_argument("--snapshot", action="append", default=[])
    parser.add_argument("--collection", type=Path, help="Replay collected JSON including source status/completeness")
    parser.add_argument("--today", help="Explicit YYYY-MM-DD for historical replay")
    parser.add_argument("--timezone", default="Asia/Shanghai")
    parser.add_argument("--reconcile", action="store_true")
    parser.add_argument("--recover-only", action="store_true")
    args = parser.parse_args()
    if args.collection and (args.fixture or args.backfill or args.snapshot or args.limit):
        parser.error("--collection cannot be combined with live/fixture collection options")
    if args.fixture and (args.backfill or args.snapshot or args.limit):
        parser.error("--fixture cannot be combined with live collection options")

    def interrupted(_signal, _frame):
        raise KeyboardInterrupt("pipeline interrupted")

    signal.signal(signal.SIGTERM, interrupted)
    try:
        if args.recover_only:
            with vault_lock(args.root.resolve()):
                recovered = recover(args.root.resolve())
            print(f"Recovered: {recovered or 'no pending transaction'}")
            return
        result = run_pipeline(
            args.root, args.run_id, fixture=args.fixture, backfill=args.backfill,
            limit=args.limit, snapshot_paths=parse_snapshot_args(args.snapshot),
            today=args.today, timezone=args.timezone, reconcile=args.reconcile,
            collection=read_json(args.collection) if args.collection else None,
        )
        print(f"{result['status']}: {args.run_id}; changed files: {result['changed_files']}")
    except (Exception, KeyboardInterrupt) as exc:
        print(f"Pipeline failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
