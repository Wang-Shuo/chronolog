from pathlib import Path
from datetime import date
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
        "chatgpt_changelog",
        "cursor_changelog",
    }
    assert {"agent-mode", "context-window", "pricing-model"} <= {
        theme["slug"] for theme in themes["themes"]
    }
    assert len(fixture["releases"]) >= 10
    assert all(release.get("product") for release in fixture["releases"])


def test_fixture_products_have_two_year_history_depth():
    fixture = json.loads((ROOT / "tests" / "fixtures" / "releases.json").read_text())
    dates_by_product: dict[str, list[date]] = {}
    for release in fixture["releases"]:
        dates_by_product.setdefault(release["product"], []).append(date.fromisoformat(release["date"]))

    assert dates_by_product
    for product, dates in dates_by_product.items():
        assert (max(dates) - min(dates)).days >= 730, product
