from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_fixture_pipeline_generates_vault_content(tmp_path: Path):
    project = tmp_path / "chronolog"
    shutil.copytree(ROOT / "_scripts", project / "_scripts")
    shutil.copytree(ROOT / "tests" / "fixtures", project / "tests" / "fixtures")

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
        cwd=project,
    )

    assert (project / "Products").exists()
    assert (project / "Changes").exists()
    assert (project / "Releases").exists()
    assert (project / "Themes").exists()
    assert (project / "Alerts").exists()
    assert (project / "index.md").exists()
    assert any((project / "Themes").glob("*.md"))
    assert "```mermaid" in next((project / "Themes").glob("*.md")).read_text()
