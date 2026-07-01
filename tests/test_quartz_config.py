from pathlib import Path
import json


def test_quartz_files_define_build_command():
    package = json.loads(Path("package.json").read_text())
    assert package["scripts"]["build"] == "quartz build"
    assert "quartz" in package["dependencies"]
    assert Path("quartz.config.ts").exists()
