from _scripts.silence_monitor import detect_silence


def test_silence_monitor_marks_sparse_history_pending():
    releases = [{"product": "cursor", "date": "2026-06-01"}]
    source = {"name": "cursor", "display_name": "Cursor", "track_silence": True, "silence_periods": 2}

    result = detect_silence(releases, [source], today="2026-06-26")

    assert result["alerts"] == []
    assert result["pending"][0]["product"] == "cursor"


def test_silence_monitor_alerts_for_configured_silence():
    releases = [
        {"product": "cursor", "date": "2025-01-01"},
        {"product": "cursor", "date": "2025-02-01"},
        {"product": "cursor", "date": "2025-03-01"},
        {"product": "cursor", "date": "2025-04-01"},
    ]
    source = {
        "name": "cursor",
        "display_name": "Cursor",
        "track_silence": True,
        "silence_window": "month",
        "silence_periods": 2,
        "silence_baseline_factor": 0.5,
    }

    result = detect_silence(releases, [source], today="2026-06-26")

    assert result["alerts"][0]["type"] == "silence"
    assert result["alerts"][0]["product"] == "cursor"


def test_historical_replay_ignores_future_releases_in_same_month():
    releases = [
        {"product": "cursor", "date": f"2025-0{month}-01"}
        for month in range(1, 5)
    ]
    releases.append({"product": "cursor", "date": "2025-06-30"})
    source = {"name": "cursor", "track_silence": True, "silence_periods": 2}
    result = detect_silence(releases, [source], today="2025-06-01")
    assert result["alerts"][0]["product"] == "cursor"


# --- W2 PR 3: cadence panel ------------------------------------------------------------

from _scripts.silence_monitor import cadence_anchor, cadence_summary

TRACKED = {"name": "cursor", "display_name": "Cursor", "track_silence": True,
           "silence_periods": 2, "silence_baseline_factor": 0.5}


def releases_on(*days, product="cursor"):
    return [{"product": product, "date": day} for day in days]


def test_cadence_anchor_is_the_newest_release_not_after_today():
    releases = releases_on("2026-09-30", "2026-10-14", "2026-11-02")
    assert cadence_anchor(releases, "2026-10-17") == "2026-10-14"
    assert cadence_anchor(releases, "2026-10-14") == "2026-10-14"
    assert cadence_anchor([], "2026-10-17") == "2026-10-17"


def test_cadence_counts_months_and_the_90_day_window_ending_at_today():
    # Two releases a month from 2025-07 through 2026-10, one of them after today.
    days = [f"{year}-{month:02d}-{day:02d}" for year, months in ((2025, range(7, 13)), (2026, range(1, 11)))
            for month in months for day in (5, 20)]
    summary = cadence_summary(releases_on(*days), [TRACKED], "2026-10-14")["cursor"]

    assert summary["as_of"] == "2026-10-14"
    assert summary["last_release_date"] == "2026-10-05"  # 2026-10-20 is after today
    assert summary["days_since_last_release"] == 9
    assert [item["month"] for item in summary["monthly_counts"]] == (
        [f"2025-{month:02d}" for month in range(11, 13)] + [f"2026-{month:02d}" for month in range(1, 11)])
    assert [item["count"] for item in summary["monthly_counts"]] == [2] * 11 + [1]
    assert all(item["archived"] for item in summary["monthly_counts"])
    # 2026-07-17 .. 2026-10-14: 07-20, 08-05, 08-20, 09-05, 09-20, 10-05.
    assert summary["releases_90d"] == 6
    # 30 releases in the 15 full months 2025-07 .. 2026-09.
    assert summary["baseline_monthly_releases"] == 2.0
    assert summary["status"] == "normal"


def test_cadence_status_quiet_silent_and_not_tracked():
    busy = [f"2026-{month:02d}-{day:02d}" for month in range(1, 9) for day in range(1, 11)]
    # Ten releases a month, then two in September and one in October: quiet.
    quiet = cadence_summary(releases_on(*busy, "2026-09-03", "2026-09-04", "2026-10-02"),
                            [TRACKED], "2026-10-14")["cursor"]
    assert quiet["baseline_monthly_releases"] == 9.11  # 82 releases over 9 full months
    assert quiet["status"] == "quiet"
    # September back to normal: one quiet month is not enough.
    recovering = cadence_summary(releases_on(*busy, *(f"2026-09-{day:02d}" for day in range(1, 9))),
                                 [TRACKED], "2026-10-14")["cursor"]
    assert recovering["status"] == "normal"
    # No release in September or October: the monitor's alert fires.
    silent = cadence_summary(releases_on(*busy), [TRACKED], "2026-10-14")["cursor"]
    assert silent["status"] == "silent"
    # An alert of the run (measured on the clock) also counts.
    flagged = cadence_summary(releases_on(*busy, "2026-10-01"), [TRACKED], "2026-10-14",
                              alerts=[{"product": "cursor"}])["cursor"]
    assert flagged["status"] == "silent"
    # Fewer than four releases, silence tracking off, or no source: not tracked.
    assert cadence_summary(releases_on("2026-10-01"), [TRACKED], "2026-10-14")["cursor"]["status"] == "not-tracked"
    untracked = {**TRACKED, "track_silence": False}
    assert cadence_summary(releases_on(*busy), [untracked], "2026-10-14")["cursor"]["status"] == "not-tracked"
    other = cadence_summary(releases_on(*busy, product="aider"), [TRACKED], "2026-10-14")
    assert other["aider"]["status"] == "not-tracked"
    assert other["cursor"]["last_release_date"] is None and other["cursor"]["releases_90d"] == 0
    # Months before the first archived release are flagged, not counted as silence.
    late = cadence_summary(releases_on(*busy[40:]), [TRACKED], "2026-10-14")["cursor"]
    assert [item["month"] for item in late["monthly_counts"] if not item["archived"]] == [
        "2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04"]
