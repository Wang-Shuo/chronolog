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
