from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.collect import load_sources
from _scripts.common import PipelinePaths, read_json, write_json


def month_index(value: date) -> int:
    return value.year * 12 + value.month


def detect_silence(
    releases: list[dict[str, Any]],
    sources: list[dict[str, Any]],
    today: str,
) -> dict[str, Any]:
    today_date = date.fromisoformat(today)
    by_product: dict[str, list[date]] = defaultdict(list)
    for release in releases:
        release_day = date.fromisoformat(release["date"])
        if release_day <= today_date:
            by_product[release["product"]].append(release_day)

    alerts = []
    pending = []
    current_month = month_index(today_date)
    for source in sources:
        if not source.get("track_silence", False):
            continue
        product = source["name"]
        dates = sorted(by_product.get(product, []))
        if len(dates) < 4:
            pending.append(
                {
                    "product": product,
                    "silence_tracking": "pending",
                    "reason": "insufficient history",
                }
            )
            continue
        active_months = {month_index(day) for day in dates}
        first_month = month_index(dates[0])
        months_observed = max(current_month - first_month, 1)
        baseline = len(active_months) / months_observed
        periods = int(source.get("silence_periods", 2))
        recent_count = sum(1 for offset in range(periods) if current_month - offset in active_months)
        threshold = baseline * float(source.get("silence_baseline_factor", 0.5))
        recent_months_are_empty = all(
            current_month - offset not in active_months for offset in range(periods)
        )
        if recent_count < threshold and recent_months_are_empty:
            alerts.append(
                {
                    "type": "silence",
                    "product": product,
                    "product_name": source.get("display_name", product),
                    "date": today,
                    "silence_periods": periods,
                    "baseline_monthly_releases": round(baseline, 2),
                    "recent_releases": recent_count,
                    "message": (
                        f"{source.get('display_name', product)} has no releases "
                        f"in the last {periods} month windows."
                    ),
                }
            )
    return {"alerts": alerts, "pending": pending}


def monitor_run(run_id: str, today: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    releases = read_json(paths.collected)["releases"]
    sources = load_sources(paths.root / "_scripts" / "sources.yaml")
    result = detect_silence(releases, sources, today)
    write_json(paths.silence, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--today", default=date.today().isoformat())
    args = parser.parse_args()
    monitor_run(args.run_id, args.today)


if __name__ == "__main__":
    main()
