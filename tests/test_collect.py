from pathlib import Path

from _scripts.collect import collect_fixture, load_sources


def test_load_sources_returns_enabled_products():
    products = load_sources(Path("_scripts/sources.yaml"))
    assert len(products) >= 5
    assert all(product["feed_type"] in {"github_releases", "blog_rss"} for product in products)


def test_collect_fixture_writes_normalized_releases(tmp_path: Path):
    output = tmp_path / "releases.json"
    releases = collect_fixture(Path("tests/fixtures/releases.json"), output)

    assert output.exists()
    assert len(releases["releases"]) >= 10
    assert {"product", "product_name", "date", "title", "body", "source_url"} <= set(
        releases["releases"][0]
    )
