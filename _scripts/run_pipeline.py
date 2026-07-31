from __future__ import annotations

import argparse
import subprocess
import sys


def run_step(args: list[str]) -> None:
    subprocess.run([sys.executable, *args], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--backfill", nargs="?", const="all")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--snapshot", action="append", default=[])
    parser.add_argument("--today", default="2026-06-26")
    parser.add_argument("--reconcile", action="store_true")
    args = parser.parse_args()

    collect_args = ["_scripts/collect.py", "--run-id", args.run_id]
    if args.fixture:
        collect_args.append("--fixture")
    if args.backfill:
        collect_args.extend(["--backfill", args.backfill])
    if args.limit is not None:
        collect_args.extend(["--limit", str(args.limit)])
    for snapshot in args.snapshot:
        collect_args.extend(["--snapshot", snapshot])
    run_step(collect_args)
    run_step(["_scripts/extract.py", "--run-id", args.run_id])
    run_step(["_scripts/validate.py", "--round", "1", "--run-id", args.run_id])
    run_step(["_scripts/analyze_a.py", "--run-id", args.run_id])
    run_step(["_scripts/analyze_b.py", "--run-id", args.run_id])
    run_step(["_scripts/silence_monitor.py", "--run-id", args.run_id, "--today", args.today])
    writer_args = ["_scripts/writer.py", "--run-id", args.run_id]
    if args.reconcile:
        writer_args.append("--reconcile")
    run_step(writer_args)
    run_step(["_scripts/validate.py", "--round", "2", "--run-id", args.run_id])


if __name__ == "__main__":
    main()
