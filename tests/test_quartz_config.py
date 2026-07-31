from pathlib import Path
import json


def test_quartz_files_define_build_command():
    package = json.loads(Path("package.json").read_text())
    assert package["scripts"]["build"] == "quartz build"
    assert "quartz" in package["dependencies"]
    assert Path("quartz.config.ts").exists()


def test_quartz_mirror_is_ignored_because_vault_root_is_the_source_of_truth():
    ignored = Path(".gitignore").read_text(encoding="utf-8").splitlines()
    wrapper = Path("_scripts/quartz_build_wrapper.mjs").read_text(encoding="utf-8")
    config = Path("quartz.config.ts").read_text(encoding="utf-8")

    assert "content/" in ignored
    assert 'args.splice(1, 0, "--directory", ".")' in wrapper
    assert 'path.join(root, "quartz", "bootstrap-cli.mjs")' in wrapper
    assert '"content"' in config
