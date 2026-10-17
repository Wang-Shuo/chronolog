from _scripts.analyze_a import analyze_products
from _scripts.analyze_b import analyze_themes


def test_analyze_products_creates_eras_and_evolves_from():
    cards = [
        {
            "card_id": "cursor-2025-01-01-aaaaaa",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-01-01",
            "theme": "editor-experience",
            "source_release": "r1",
        },
        {
            "card_id": "cursor-2025-06-01-bbbbbb",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-06-01",
            "theme": "editor-experience",
            "source_release": "r2",
        },
        {
            "card_id": "cursor-2026-01-01-cccccc",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2026-01-01",
            "theme": "agent-mode",
            "source_release": "r3",
        },
    ]

    result = analyze_products(cards)

    cursor = result["products"]["cursor"]
    assert cursor["verbosity_baseline"] == 1.0
    assert cursor["eras"] == []
    assert result["evolves_from"] == {}


def test_analyze_products_never_splits_one_release_across_eras():
    cards = [
        {
            "card_id": f"cursor-2025-01-01-{suffix}",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-01-01",
            "theme": theme,
            "source_release": "cursor-2025-01-01-v1",
        }
        for suffix, theme in [
            ("aaaaaa", "agent-mode"),
            ("bbbbbb", "context-window"),
            ("cccccc", "model-support"),
        ]
    ]
    cards.append(
        {
            "card_id": "cursor-2026-01-01-dddddd",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2026-01-01",
            "theme": "collaboration",
            "source_release": "cursor-2026-01-01-v2",
        }
    )

    eras = analyze_products(cards)["products"]["cursor"]["eras"]

    assert eras == []  # no unsupported eras, including no split of a release


def test_analyze_themes_creates_related_changes_and_diffusion():
    cards = [
        {
            "card_id": "aider-2025-01-01-aaaaaa",
            "product": "aider",
            "product_name": "Aider",
            "date": "2025-01-01",
            "theme": "agent-mode",
        },
        {
            "card_id": "cursor-2025-02-01-bbbbbb",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-02-01",
            "theme": "agent-mode",
        },
        {
            "card_id": "tabby-2025-03-01-cccccc",
            "product": "tabby",
            "product_name": "Tabby",
            "date": "2025-03-01",
            "theme": "editor-experience",
        },
    ]

    result = analyze_themes(cards)

    cursor = result["cards"]["cursor-2025-02-01-bbbbbb"]
    assert cursor["related_changes"] == ["aider-2025-01-01-aaaaaa"]
    assert cursor["diffusion"]["scope"] == "tracked-products-only"
    assert cursor["diffusion"]["role"] == "later-observed"
    assert cursor["diffusion"]["lag_days"] == 31


def test_holding_theme_cards_have_no_chronology_and_rank_among_no_themes():
    base = {"product": "cursor", "product_name": "Cursor"}
    cards = [
        {**base, "card_id": "cursor-2025-01-01-aaaaaa", "date": "2025-01-01",
         "theme": "agent-mode", "source_release": "r1"},
        {**base, "card_id": "cursor-2025-01-01-bbbbbb", "date": "2025-01-01",
         "theme": "uncategorized", "source_release": "r1"},
        {**base, "card_id": "cursor-2025-02-01-cccccc", "date": "2025-02-01",
         "theme": "uncategorized", "source_release": "r2"},
    ]

    cursor = analyze_products(cards)["products"]["cursor"]
    assert cursor["top_themes"] == ["agent-mode"]
    # Holding cards are published cards, so the baseline still counts them.
    assert cursor["verbosity_baseline"] == 1.5

    themes = analyze_themes(cards)
    assert list(themes["themes"]) == ["agent-mode"]
    assert list(themes["cards"]) == ["cursor-2025-01-01-aaaaaa"]
    assert themes["cards"]["cursor-2025-01-01-aaaaaa"]["diffusion"]["role"] == "first-observed"
