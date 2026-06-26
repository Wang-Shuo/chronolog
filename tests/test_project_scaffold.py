from pathlib import Path
import json
import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_project_configs_and_fixture_are_present():
    sources = yaml.safe_load((ROOT / "_scripts" / "sources.yaml").read_text())
    themes = yaml.safe_load((ROOT / "_scripts" / "themes.yaml").read_text())
    fixture = json.loads((ROOT / "tests" / "fixtures" / "releases.json").read_text())

    assert len(sources["products"]) >= 5
    assert {product["feed_type"] for product in sources["products"]} <= {
        "github_releases",
        "blog_rss",
    }
    assert {"agent-mode", "context-window", "pricing-model"} <= {
        theme["slug"] for theme in themes["themes"]
    }
    assert len(fixture["releases"]) >= 10
    assert fixture["releases"][0]["product"]
