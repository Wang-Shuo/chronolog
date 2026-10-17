from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.collect import load_sources
from _scripts.common import PipelinePaths, read_json, write_json


CADENCE_MONTHS = 12
CADENCE_WINDOW_DAYS = 90
CADENCE_STATUSES = ("normal", "quiet", "silent", "not-tracked")


def month_index(value: date) -> int:
    return value.year * 12 + value.month


def month_label(index: int) -> str:
    """``YYYY-MM`` of a ``month_index`` value."""
    year, month = divmod(index - 1, 12)
    return f"{year:04d}-{month + 1:02d}"


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


def cadence_anchor(releases: list[dict[str, Any]], today: str) -> str:
    """Newest archived release date on or before ``today`` (``today`` without releases).

    Cadence is measured to this archive date rather than the clock, so a rerun of the
    same archive on a later day renders the same cadence."""
    dates = [str(release["date"]) for release in releases if str(release["date"]) <= today]
    return max(dates, default=today)


def cadence_summary(
    releases: list[dict[str, Any]],
    sources: list[dict[str, Any]],
    today: str,
    alerts: list[dict[str, Any]] | None = None,
) -> dict[str, dict[str, Any]]:
    """Release cadence per product, measured to ``today`` (the pipeline passes the
    ``cadence_anchor``).

    - ``monthly_counts``: releases in each of the 12 calendar months ending at ``today``'s
      month (that month is partial); ``archived`` is false for months before the
      product's first archived release, whose zero is a coverage gap, not silence.
    - ``releases_90d``: releases in the 90 days ending at (and including) ``today``.
    - ``baseline_monthly_releases``: mean releases per full month over the monitor's
      observation window (the first release month up to, not including, ``today``'s
      month). ``detect_silence`` keeps its own active-month ratio for alerts.
    - ``status``: ``not-tracked`` (no ``track_silence`` or fewer than four releases, the
      monitor's pending case); ``silent`` (a silence alert fires at ``today`` or is listed
      in ``alerts``, the run's own alerts); ``quiet`` (each of the last
      ``silence_periods`` month windows, the monitor's windows, had fewer releases than
      baseline × ``silence_baseline_factor``); otherwise ``normal``.
    """
    today_date = date.fromisoformat(today)
    by_product: dict[str, list[date]] = defaultdict(list)
    for release in releases:
        release_day = date.fromisoformat(release["date"])
        if release_day <= today_date:
            by_product[release["product"]].append(release_day)
    monitor = detect_silence(releases, sources, today)
    silent = {alert["product"] for alert in [*monitor["alerts"], *(alerts or [])]}
    pending = {item["product"] for item in monitor["pending"]}
    sources_by_name = {source["name"]: source for source in sources}
    current_month = month_index(today_date)
    window_start = today_date - timedelta(days=CADENCE_WINDOW_DAYS - 1)
    summary = {}
    for product in sorted(set(by_product) | set(sources_by_name)):
        source = sources_by_name.get(product, {})
        dates = sorted(by_product.get(product, []))
        per_month = Counter(month_index(day) for day in dates)
        first_month = month_index(dates[0]) if dates else current_month
        months_observed = max(current_month - first_month, 1)
        before_current = sum(count for month, count in per_month.items() if month < current_month)
        baseline = before_current / months_observed
        periods = int(source.get("silence_periods", 2))
        threshold = baseline * float(source.get("silence_baseline_factor", 0.5))
        if not source.get("track_silence", False) or product in pending or not dates:
            status = "not-tracked"
        elif product in silent:
            status = "silent"
        elif all(per_month.get(current_month - offset, 0) < threshold for offset in range(periods)):
            status = "quiet"
        else:
            status = "normal"
        summary[product] = {
            "product_name": source.get("display_name", product),
            "as_of": today,
            "last_release_date": dates[-1].isoformat() if dates else None,
            "days_since_last_release": (today_date - dates[-1]).days if dates else None,
            "releases_90d": sum(window_start <= day <= today_date for day in dates),
            "monthly_counts": [
                {"month": month_label(month), "count": per_month.get(month, 0),
                 "archived": month >= first_month}
                for month in range(current_month - CADENCE_MONTHS + 1, current_month + 1)
            ],
            "baseline_monthly_releases": round(baseline, 2),
            "status": status,
        }
    return summary


def monitor_run(run_id: str, today: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    releases = read_json(paths.collected)["releases"]
    sources = load_sources(paths.root / "_scripts" / "sources.yaml")
    result = detect_silence(releases, sources, today)
    result["cadence"] = cadence_summary(
        releases, sources, cadence_anchor(releases, today), result["alerts"]
    )
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
