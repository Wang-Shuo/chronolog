from _scripts.analyze_a import analyze_products


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
    assert len(cursor["eras"]) >= 2
    assert result["evolves_from"]["cursor-2025-06-01-bbbbbb"] == [
        "cursor-2025-01-01-aaaaaa"
    ]
