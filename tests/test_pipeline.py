from pathlib import Path
import subprocess
import sys


def test_fixture_pipeline_generates_vault_content():
    subprocess.run(
        [
            sys.executable,
            "_scripts/run_pipeline.py",
            "--fixture",
            "--run-id",
            "test-demo",
            "--today",
            "2026-06-26",
        ],
        check=True,
    )

    assert Path("Products").exists()
    assert Path("Changes").exists()
    assert Path("Releases").exists()
    assert Path("Themes").exists()
    assert Path("Alerts").exists()
    assert Path("index.md").exists()
    assert any(Path("Themes").glob("*.md"))
    assert "```mermaid" in next(Path("Themes").glob("*.md")).read_text()
