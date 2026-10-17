from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import frontmatter
import pytest

from _scripts.common import PipelinePaths, load_site, machine_hash, write_json
from _scripts.history import merge_history
from _scripts.quality import normalized_page
from _scripts.writer import (
    MIGRATION_PENDING_REASON,
    change_card_paths,
    counted,
    ensure_vault_dirs,
    extract_machine_regions,
    legacy_residue,
    machine_region,
    main,
    reconcile_missing_change_cards,
    relation_link,
    render_change_markdown,
    render_about_markdown,
    render_frontmatter,
    render_index_markdown,
    render_product_markdown,
    render_release_markdown,
    render_theme_markdown,
    replace_machine_region,
    write_markdown_file,
    write_run,
)

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/Wang-Shuo/chronolog"


def test_replace_machine_region_preserves_human_content():
    existing = """# Cursor

Human intro.

<!-- chronolog:begin region="eras" -->
old
<!-- chronolog:end -->

## Editor Notes
Keep this.
"""

    updated = replace_machine_region(existing, "eras", "new")

    assert "Human intro." in updated
    assert "Keep this." in updated
    assert "new" in updated
    assert "old" not in updated


def test_render_theme_markdown_contains_navigable_year_timeline(tmp_path: Path):
    cards = [
        {
            "card_id": "aider-2025-01-01-aaaaaa",
            "product": "aider",
            "product_name": "Aider",
            "date": "2025-01-01",
            "title": "Agent mode",
            "theme": "agent-mode",
            "slug": "agent-mode",
        },
        {
            "card_id": "cursor-2025-02-01-bbbbbb",
            "product": "cursor",
            "product_name": "Cursor",
            "date": "2025-02-01",
            "title": "Agent shell",
            "theme": "agent-mode",
            "slug": "agent-shell",
        },
    ]

    markdown = render_theme_markdown("agent-mode", cards)

    assert "### 2025" in markdown
    assert "same-theme chronology" in markdown
    assert "timeline" in markdown
    assert "Aider" in markdown
    assert "Cursor" in markdown


def test_render_theme_markdown_strips_trailing_timeline_whitespace():
    card = {**change_card(), "title": "Agent shell   "}

    markdown = render_theme_markdown("agent-mode", [card])

    assert not any(line.endswith(" ") for line in markdown.splitlines())


def test_write_markdown_file_detects_machine_region_edits(tmp_path: Path):
    target = tmp_path / "change.md"
    card = {
        "type": "change",
        "card_id": "cursor-2025-02-01-aaaaaa",
        "product": "cursor",
        "product_name": "Cursor",
        "source_release": "cursor-2025-02-01-v1",
        "date": "2025-02-01",
        "title": "Agent shell",
        "slug": "agent-shell",
        "theme": "agent-mode",
        "impact": "incremental",
        "description": "Agent can run shell commands.",
        "comparison": "",
        "evidence": [{"source_release": "https://example.com", "quote": "Agent can run shell commands."}],
        "extractor_version": "fallback-v1",
    }
    rendered = render_change_markdown(card, {"evolves_from": []}, {})
    write_markdown_file(target, rendered, [])

    target.write_text(
        target.read_text(encoding="utf-8").replace(
            "Agent can run shell commands.",
            "Edited machine text.",
        ),
        encoding="utf-8",
    )
    conflicts: list[dict[str, str]] = []

    wrote = write_markdown_file(target, rendered, conflicts)

    assert wrote is False
    assert conflicts[0]["file"] == str(target)
    assert "Edited machine text." in target.read_text(encoding="utf-8")


def test_write_markdown_file_preserves_custom_human_frontmatter(tmp_path: Path):
    target = tmp_path / "change.md"
    card = change_card()
    rendered = render_change_markdown(card, {"evolves_from": []}, {})
    write_markdown_file(target, rendered, [])
    post = frontmatter.load(target)
    post.metadata["research_note"] = "keep this"
    target.write_text(frontmatter.dumps(post), encoding="utf-8")

    wrote = write_markdown_file(target, rendered, [])

    assert wrote is True
    assert frontmatter.load(target).metadata["research_note"] == "keep this"


def _card_heading(path: Path) -> str:
    return next(line for line in frontmatter.load(path).content.splitlines() if line.startswith("# "))


def test_write_markdown_file_refreshes_generated_card_heading(tmp_path: Path):
    target = tmp_path / "change.md"
    legacy = {**change_card(), "title": "We're adding an agent shell so agents can run comma"}
    target.write_text(legacy_change_markdown(legacy, notes="Keep me."), encoding="utf-8")
    retitled = {**legacy, "title": "Cursor adds an agent shell so agents can run commands"}
    conflicts: list[dict[str, str]] = []

    wrote = write_markdown_file(
        target, render_change_markdown(retitled, {"evolves_from": []}, {}), conflicts, []
    )

    assert wrote is True and conflicts == []
    post = frontmatter.load(target)
    assert _card_heading(target) == "# Cursor adds an agent shell so agents can run commands"
    assert post["record"]["title"] == retitled["title"]
    assert post["title"] == retitled["title"]
    assert "Keep me." in post.content


def test_write_markdown_file_preserves_edited_card_heading(tmp_path: Path):
    target = tmp_path / "change.md"
    card = change_card()
    target.write_text(
        legacy_change_markdown(card).replace("# Agent shell\n", "# Curated agent shell\n"),
        encoding="utf-8",
    )
    retitled = {**card, "title": "Agent can run shell commands"}
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    wrote = write_markdown_file(
        target, render_change_markdown(retitled, {"evolves_from": []}, {}), conflicts, pending
    )

    # An edited legacy H1 is human text: the skeleton is kept for manual migration.
    assert wrote is True and conflicts == []
    assert _card_heading(target) == "# Curated agent shell"
    assert frontmatter.load(target)["record"]["title"] == "Agent can run shell commands"
    assert pending == [{"file": str(target), "reason": MIGRATION_PENDING_REASON}]


def test_new_card_heading_lives_in_a_machine_region(tmp_path: Path):
    target = tmp_path / "change.md"
    rendered = render_change_markdown(change_card(), {"evolves_from": []}, {})
    write_markdown_file(target, rendered, [])
    target.write_text(
        target.read_text(encoding="utf-8").replace("# Agent shell\n", "# Curated agent shell\n"),
        encoding="utf-8",
    )
    conflicts: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, conflicts) is False
    assert conflicts[0]["error"] == "machine_hash mismatch"


def test_change_card_paths_reuses_existing_path_for_stable_card_id(tmp_path: Path):
    target = tmp_path / "Changes" / "Cursor" / "2025-02-01-original-slug.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        render_change_markdown(change_card(), {"evolves_from": []}, {}),
        encoding="utf-8",
    )
    renamed_card = {**change_card(), "slug": "new-title-slug", "title": "A new title"}

    paths, duplicates = change_card_paths(tmp_path, [renamed_card])

    assert duplicates == []
    assert paths[renamed_card["card_id"]] == target


def test_change_card_paths_disambiguates_same_date_and_slug(tmp_path: Path):
    first = change_card()
    second = {**change_card(), "card_id": "cursor-2025-02-01-bbbbbb"}

    paths, duplicates = change_card_paths(tmp_path, [first, second])

    assert duplicates == []
    assert paths[first["card_id"]].name == "2025-02-01-agent-shell.md"
    assert paths[second["card_id"]].name == "2025-02-01-agent-shell-bbbbbb.md"
    assert len(set(paths.values())) == 2


def test_reconcile_missing_change_cards_marks_superseded_without_deleting(tmp_path: Path):
    target = tmp_path / "Changes" / "Cursor" / "2025-02-01-agent-shell.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        render_change_markdown(change_card(), {"evolves_from": []}, {}),
        encoding="utf-8",
    )
    conflicts: list[dict[str, str]] = []

    superseded = reconcile_missing_change_cards(
        tmp_path,
        active_card_ids=set(),
        reconcile_products={"cursor"},
        conflicts=conflicts,
    )

    assert superseded == [change_card()["card_id"]]
    assert conflicts == []
    assert target.exists()
    assert frontmatter.load(target).metadata["superseded"] is True


def test_writer_cli_returns_nonzero_when_machine_conflict_exists(monkeypatch):
    monkeypatch.setattr("_scripts.writer.write_run", lambda *_args, **_kwargs: [{"error": "conflict"}])
    monkeypatch.setattr("sys.argv", ["writer.py", "--run-id", "demo"])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 1


def test_ensure_vault_dirs_creates_empty_alerts_directory(tmp_path: Path):
    ensure_vault_dirs(tmp_path)

    assert (tmp_path / "Products").is_dir()
    assert (tmp_path / "Changes").is_dir()
    assert (tmp_path / "Releases").is_dir()
    assert (tmp_path / "Themes").is_dir()
    assert (tmp_path / "Alerts").is_dir()


def test_writer_creates_release_page_when_release_has_no_publishable_cards(tmp_path: Path):
    run_id = "zero-card-release"
    paths = PipelinePaths(run_id, root=tmp_path)
    release = {
        "release_id": "chatgpt-2023-01-09-updates-a1b2c3d4",
        "product": "chatgpt",
        "product_name": "ChatGPT",
        "date": "2023-01-09",
        "version": "Updates to ChatGPT",
        "title": "Updates to ChatGPT",
        "body": "Maintenance update.",
        "source_summary": "Maintenance update.",
        "source_url": "https://help.openai.com/release#update",
        "source_type": "chatgpt_changelog",
    }
    write_json(
        paths.valid_cards,
        {"change_cards": [], "pending_theme_review": []},
    )
    write_json(paths.analyze_a, {"products": {}, "evolves_from": {}})
    write_json(paths.analyze_b, {"themes": {}, "cards": {}})
    write_json(paths.silence, {"alerts": [], "pending": []})
    write_json(paths.collected, {"source": "fixture", "releases": [release]})

    conflicts = write_run(run_id, root=tmp_path)

    pages = list((tmp_path / "Releases" / "ChatGPT").glob("*.md"))
    assert conflicts == []
    assert len(pages) == 1
    post = frontmatter.load(pages[0])
    assert post.metadata["release_id"] == release["release_id"]
    assert post.metadata["changes_count"] == 0
    assert "No change cards extracted." in post.content


def change_card() -> dict[str, object]:
    return {
        "type": "change",
        "card_id": "cursor-2025-02-01-aaaaaa",
        "product": "cursor",
        "product_name": "Cursor",
        "source_release": "cursor-2025-02-01-v1",
        "date": "2025-02-01",
        "title": "Agent shell",
        "slug": "agent-shell",
        "theme": "agent-mode",
        "impact": "incremental",
        "description": "Agent can run shell commands.",
        "comparison": "",
        "evidence": [
            {"source_release": "https://example.com", "quote": "Agent can run shell commands."}
        ],
        "extractor_version": "fallback-v1",
    }


@pytest.mark.parametrize("source_title, visible_title", [
    ("Added `$.prompt.media` for managed mods", "Added $.prompt.media for managed mods"),
    ("Added `$.ui.view({ agentId })`", "Added $.ui.view({ agentId })"),
    ("Read `$SHELL`, `$1`, and `$(pwd)`", "Read $SHELL, $1, and $(pwd)"),
    ("Pricing: $0.10/$0.50 per Mtok", "Pricing: $0.10/$0.50 per Mtok"),
    ("Keep $$ and a trailing $", "Keep $$ and a trailing $"),
])
def test_dollar_symbols_survive_card_titles_and_navigation(source_title, visible_title):
    from _scripts.writer import card_link
    card = {**change_card(), "title": source_title}
    target = "Changes/Cursor/2025-02-01-agent-shell"
    targets = {card["card_id"]: target}
    post = frontmatter.loads(render_change_markdown(card, {}, {}, targets))
    assert post["title"] == visible_title
    assert post["record"]["title"] == source_title
    expected_link = f"[[{target}|{visible_title}]]"
    assert card_link(card, targets) == expected_link
    assert expected_link in render_theme_markdown("agent-mode", [card], card_targets=targets)
    release = {"release_id": "r", "product": "cursor", "product_name": "Cursor",
               "title": source_title, "date": card["date"],
               "source_url": "https://cursor.com/changelog/test", "cards": [card]}
    rendered_release = render_release_markdown(release, targets)
    assert frontmatter.loads(rendered_release)["title"] == "Cursor · " + visible_title
    assert f"# Cursor · {source_title}\n" in rendered_release
    assert expected_link in rendered_release


# --- W1 C2: Change Card, Release and Theme templates -------------------------------

THEME_LABELS = {"agent-mode": "Agent Mode", "model-support": "Model Support"}


def related_card(card_id, product_name, date, title, theme="agent-mode"):
    return {**change_card(), "card_id": card_id, "product": product_name.lower().replace(" ", "-"),
            "product_name": product_name, "date": date, "title": title,
            "slug": title.lower().replace(" ", "-").replace("`", ""), "theme": theme,
            "source_release": f"{product_name.lower()}-{date}-release"}


def legacy_change_markdown(card, notes: str = "") -> str:
    """A Change Card as the pre-W1 writer produced it."""
    metadata = {key: card[key] for key in (
        "type", "card_id", "product", "product_name", "source_release", "date", "theme",
        "impact", "extractor_version") if key in card}
    metadata.update(title=card["title"], record=dict(card), evolves_from=[])
    regions = {
        "description": card["description"],
        "evidence": "\n\n".join(f"> {item['quote']}\n>\n> Source: {item['source_release']}"
                                for item in card["evidence"]),
        "evolution": "No evidence-backed evolution relationship assigned.",
        "diffusion": "- Scope: tracked-products-only\n- Lag Days: 3",
    }
    metadata["machine_hash"] = machine_hash(metadata, regions)
    body = f"# {card['title']}\n\n" + "\n\n".join(
        machine_region(name, content) for name, content in regions.items()
    ) + "\n\n## Editor Notes\n" + (f"\n{notes}\n" if notes else "")
    return render_frontmatter(metadata, body)


def legacy_release_markdown(release, heading: str | None = None) -> str:
    regions = {
        "summary": f"{release['source_summary']}\n\n[Official release notes]({release['source_url']})\n\nTracked cards: 0",
        "cards": "No change cards extracted.",
    }
    fields = {
        "tags": ["release", release["product"]],
        "title": f"{release['product_name']} — {release['title']}",
        "record": {key: value for key, value in release.items() if key not in {"body", "cards"}},
        "release_id": release["release_id"], "product": release["product"],
        "product_name": release["product_name"], "source_release": release["title"],
        "version": release["title"], "source_url": release["source_url"],
        "source_type": release["source_type"], "changes_count": 0, "date": release["date"],
    }
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (f"# {heading or release['product_name'] + ' ' + release['title']}\n\n"
            f"## Summary\n{machine_region('summary', regions['summary'])}\n\n"
            f"## Change Cards\n{machine_region('cards', regions['cards'])}\n")
    return render_frontmatter(fields, body)


def legacy_theme_markdown(theme: str) -> str:
    regions = {"narrative": "Explore the dated evidence below.", "timeline": "Scope: tracked-products-only.",
               "cards": "No changes yet."}
    fields = {"tags": ["theme", "moc"], "title": theme.replace("-", " ").title(), "status": "official",
              "publication": "active", "theme": theme, "products_involved": []}
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (f"# Theme: {theme}\n\n"
            f"## Research summary\n{machine_region('narrative', regions['narrative'])}\n\n"
            f"## Cross-Product Timeline\n{machine_region('timeline', regions['timeline'])}\n\n"
            f"## Change Cards\n{machine_region('cards', regions['cards'])}\n")
    return render_frontmatter(fields, body)


def release_record(**overrides):
    release = {
        "release_id": "cursor-2025-02-01-v1", "product": "cursor", "product_name": "Cursor",
        "date": "2025-02-01", "title": "Cursor Projects", "version": "Cursor Projects",
        "source_summary": "What's changed", "source_url": "https://cursor.com/changelog/projects",
        "source_type": "cursor_changelog",
    }
    release.update(overrides)
    return release


def test_change_card_template_renders_every_section():
    card = change_card()
    sibling = related_card("cursor-2025-02-01-bbbbbb", "Cursor", "2025-02-01", "Model picker", "model-support")
    earlier = related_card("chatgpt-2025-01-15-cccccc", "ChatGPT", "2025-01-15", "ChatGPT agent")
    later = related_card("claude-code-2025-03-01-dddddd", "Claude Code", "2025-03-01", "Background `agents`")
    first = related_card("cursor-2023-07-06-eeeeee", "Cursor", "2023-07-06", "Agents arrive")
    evolved = related_card("cursor-2024-12-01-ffffff", "Cursor", "2024-12-01", "Agent preview")
    every = [card, sibling, earlier, later, first, evolved]
    targets = {c["card_id"]: f"Changes/{c['product_name']}/{c['date']}-{c['slug']}" for c in every}
    diffusion = {"theme": "agent-mode", "relation": "same-theme-chronology",
                 "inference": "No adoption, equivalence, or causation claim.",
                 "scope": "tracked-products-only", "role": "later-observed",
                 "first_in_tracked": first["card_id"], "lag_days": 575, "tracked_products_count": 3}

    post = frontmatter.loads(render_change_markdown(
        card, {"evolves_from": [evolved["card_id"]]},
        {"related_changes": [first["card_id"]], "diffusion": diffusion},
        targets, "Releases/Cursor/cursor-2025-02-01-v1", release_title="Cursor `0.45`",
        cards_by_id={c["card_id"]: c for c in every}, siblings=[sibling, card],
        earlier=earlier, later=later, theme_labels=THEME_LABELS, repository=REPOSITORY,
    ))

    assert list(extract_machine_regions(post.content)) == [
        "header", "evidence", "context", "nearby", "relations", "footer"]
    regions = extract_machine_regions(post.content)
    assert regions["header"] == (
        "# Agent shell\n\n**Cursor** · 2025-02-01 · [[Themes/agent-mode|Agent Mode]] · "
        "[Official source](https://example.com) · "
        "from [[Releases/Cursor/cursor-2025-02-01-v1|Cursor 0.45]]")
    assert regions["evidence"] == "> Agent can run shell commands.\n>\n> Source: https://example.com"
    assert regions["context"] == (
        "## Also in this release\n\n"
        "- [[Changes/Cursor/2025-02-01-model-picker|Model picker]] · Model Support")
    assert regions["nearby"] == (
        "## Nearby in Agent Mode\n\n"
        "- Earlier: 2025-01-15 · ChatGPT · [[Changes/ChatGPT/2025-01-15-chatgpt-agent|ChatGPT agent]]\n"
        "- Later: 2025-03-01 · Claude Code · "
        "[[Changes/Claude Code/2025-03-01-background-agents|Background agents]]")
    assert regions["relations"] == (
        "## Related\n\n"
        "- Builds on: [[Changes/Cursor/2024-12-01-agent-preview|Agent preview]]\n"
        "- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · "
        "[[Changes/Cursor/2023-07-06-agents-arrive|Agents arrive]]")
    assert regions["footer"].startswith(f"[Report an issue with this card]({REPOSITORY}/issues/new?")
    for removed in ("Editor Notes", "Lag Days", "Tracked Products Count", "Inference",
                    "No evidence-backed evolution"):
        assert removed not in post.content
    assert post["diffusion"] == {**diffusion,
                                 "first_in_tracked": "[[Changes/Cursor/2023-07-06-agents-arrive|Agents arrive]]"}
    assert post["evolves_from"] == ["[[Changes/Cursor/2024-12-01-agent-preview|Agent preview]]"]
    assert post["description"] == "Cursor · 2025-02-01 · Agent Mode: Agent can run shell commands."


def test_change_card_template_omits_empty_sections():
    post = frontmatter.loads(render_change_markdown(change_card(), {"evolves_from": []}, {}))

    regions = extract_machine_regions(post.content)
    assert list(regions) == ["header", "evidence", "context", "nearby", "relations", "footer"]
    assert {name: regions[name] for name in ("context", "nearby", "relations", "footer")} == {
        "context": "", "nearby": "", "relations": "", "footer": ""}
    # Without a known release target the "from" part is omitted.
    assert regions["header"] == (
        "# Agent shell\n\n**Cursor** · 2025-02-01 · [[Themes/agent-mode|Agent Mode]] · "
        "[Official source](https://example.com)")
    assert "## " not in post.content
    assert "description" not in regions and "evolution" not in regions and "diffusion" not in regions


def test_first_observed_card_states_its_tracked_scope():
    patch_b = {"diffusion": {"role": "first-observed", "first_in_tracked": "cursor-2025-02-01-aaaaaa",
                             "lag_days": 0, "tracked_products_count": 3}}
    regions = extract_machine_regions(frontmatter.loads(
        render_change_markdown(change_card(), {}, patch_b)).content)

    assert regions["relations"] == (
        "## Related\n\n- Earliest same-theme entry among the 3 tracked products.")


def test_later_observed_card_without_known_first_entry_has_no_relations_section():
    patch_b = {"diffusion": {"role": "later-observed", "first_in_tracked": "cursor-2023-01-01-zzzzzz"}}
    post = frontmatter.loads(render_change_markdown(change_card(), {}, patch_b))

    assert extract_machine_regions(post.content)["relations"] == ""
    assert post["diffusion"]["first_in_tracked"] == "cursor-2023-01-01-zzzzzz"


def test_change_description_is_capped_at_a_word_boundary():
    quote = ("Agents can now run long shell sessions in the cloud while you close your laptop, "
             "and they report progress back to the editor with detailed transcripts of every step taken")
    card = {**change_card(), "evidence": [{"source_release": "https://example.com", "quote": quote}]}

    description = frontmatter.loads(
        render_change_markdown(card, {}, {}, theme_labels=THEME_LABELS))["description"]

    assert len(description) <= 160
    assert description.endswith("…")
    prefix = description[:-1]
    assert prefix.startswith("Cursor · 2025-02-01 · Agent Mode: Agents can now run")
    assert f"Cursor · 2025-02-01 · Agent Mode: {quote}".startswith(prefix)
    assert f"Cursor · 2025-02-01 · Agent Mode: {quote}"[len(prefix)] == " "


def test_feedback_link_prefills_an_encoded_github_issue():
    card = {**change_card(), "evidence": [
        {"source_release": "https://cursor.com/changelog/1-0#a&b", "quote": "Agent shell"}]}
    targets = {card["card_id"]: "Changes/Claude Code/2025-02-01-agent-shell"}

    footer = extract_machine_regions(frontmatter.loads(render_change_markdown(
        card, {}, {}, targets, repository=REPOSITORY + "/")).content)["footer"]

    url = footer.removeprefix("[Report an issue with this card](").removesuffix(")")
    assert " " not in url and "(" not in url and ")" not in url
    parsed = urlsplit(url)
    assert f"{parsed.scheme}://{parsed.netloc}{parsed.path}" == f"{REPOSITORY}/issues/new"
    query = parse_qs(parsed.query)
    assert query["title"] == ["Card feedback: cursor-2025-02-01-aaaaaa"]
    body = query["body"][0]
    assert "Card: Changes/Claude Code/2025-02-01-agent-shell.md" in body
    assert "Card ID: cursor-2025-02-01-aaaaaa" in body
    assert "Source: https://cursor.com/changelog/1-0#a&b" in body


def test_site_repository_is_configured_and_optional(tmp_path: Path):
    assert load_site(ROOT / "_scripts/sources.yaml") == {"repository": REPOSITORY}
    assert load_site(tmp_path / "missing.yaml") == {}
    (tmp_path / "sources.yaml").write_text("products: []\n", encoding="utf-8")
    assert load_site(tmp_path / "sources.yaml") == {}


def test_relation_link_labels_targets_with_card_titles():
    targets = {"cursor-2025-02-01-aaaaaa": "Changes/Cursor/2025-02-01-agent-shell"}

    assert relation_link("cursor-2025-02-01-aaaaaa", targets, {"cursor-2025-02-01-aaaaaa": "Agent `shell`"}) == (
        "[[Changes/Cursor/2025-02-01-agent-shell|Agent shell]]")
    assert relation_link("cursor-2025-02-01-aaaaaa", targets) == (
        "[[Changes/Cursor/2025-02-01-agent-shell|cursor-2025-02-01-aaaaaa]]")
    assert relation_link("cursor-2025-02-01-bbbbbb", targets, {}) == "cursor-2025-02-01-bbbbbb"


def test_legacy_residue_ignores_generated_skeletons():
    assert legacy_residue(frontmatter.loads(legacy_change_markdown(change_card())).content, "change") == ""
    assert legacy_residue(frontmatter.loads(legacy_release_markdown(release_record())).content, "release") == ""
    assert legacy_residue(frontmatter.loads(legacy_theme_markdown("agent-mode")).content, "theme") == ""
    with_notes = frontmatter.loads(legacy_change_markdown(change_card(), notes="Keep me.")).content
    assert legacy_residue(with_notes, "change") == "Keep me."
    # Skeleton headings of another page type are human text.
    assert legacy_residue("# Title\n\n## Summary\n", "change") == "## Summary"
    # A heading written after the regions is not the generated H1.
    assert legacy_residue(machine_region("header", "# T") + "\n\n# Notes\n", "change") == "# Notes"


def test_migration_replaces_untouched_legacy_card_skeleton(tmp_path: Path):
    target = tmp_path / "change.md"
    target.write_text(legacy_change_markdown(change_card()), encoding="utf-8")
    rendered = render_change_markdown(change_card(), {"evolves_from": []}, {}, repository=REPOSITORY)
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, conflicts, pending) is True

    post = frontmatter.load(target)
    assert conflicts == [] and pending == []
    assert post.content == frontmatter.loads(rendered).content
    assert list(extract_machine_regions(post.content)) == [
        "header", "evidence", "context", "nearby", "relations", "footer"]
    assert "Editor Notes" not in post.content and "Lag Days" not in post.content
    assert post["description"].startswith("Cursor · 2025-02-01 · Agent Mode: ")


def test_migration_keeps_legacy_card_with_human_text_and_reports_it(tmp_path: Path):
    target = tmp_path / "change.md"
    target.write_text(legacy_change_markdown(change_card(), notes="Keep me."), encoding="utf-8")
    changed = {**change_card(), "evidence": [{"source_release": "https://example.com/new", "quote": "New quote."}]}
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(
        target, render_change_markdown(changed, {}, {}, repository=REPOSITORY), conflicts, pending) is True

    post = frontmatter.load(target)
    regions = extract_machine_regions(post.content)
    assert conflicts == []
    assert pending == [{"file": str(target), "reason": MIGRATION_PENDING_REASON}]
    assert list(regions) == ["description", "evidence", "evolution", "diffusion"]
    assert regions["evidence"] == "> New quote.\n>\n> Source: https://example.com/new"
    assert post.content.rstrip().endswith("## Editor Notes\n\nKeep me.")
    assert "Report an issue" not in post.content
    # The kept file is consistent: a later run is not blocked by a hash conflict.
    assert write_markdown_file(target, render_change_markdown(changed, {}, {}), conflicts, []) is True
    assert conflicts == []


def test_render_is_idempotent_on_migrated_files(tmp_path: Path):
    target = tmp_path / "change.md"
    target.write_text(legacy_change_markdown(change_card()), encoding="utf-8")
    rendered = render_change_markdown(change_card(), {}, {}, repository=REPOSITORY)
    write_markdown_file(target, rendered, [], [])
    migrated = target.read_bytes()

    write_markdown_file(target, rendered, [], [])
    assert target.read_bytes() == migrated

    fresh = tmp_path / "fresh.md"
    write_markdown_file(fresh, rendered, [], [])
    assert fresh.read_bytes() == migrated

    # Human notes after the last region survive repeated renders unchanged.
    target.write_text(target.read_text(encoding="utf-8") + "\n\nHuman research notes.", encoding="utf-8")
    noted = target.read_bytes()
    pending: list[dict[str, str]] = []
    write_markdown_file(target, rendered, [], pending)
    assert target.read_bytes() == noted and pending == []


def test_migration_rewrites_legacy_release_and_theme_pages(tmp_path: Path):
    release_path = tmp_path / "release.md"
    release_path.write_text(legacy_release_markdown(release_record()), encoding="utf-8")
    theme_path = tmp_path / "theme.md"
    theme_path.write_text(legacy_theme_markdown("mobile-desktop"), encoding="utf-8")
    pending: list[dict[str, str]] = []

    write_markdown_file(release_path, render_release_markdown(release_record()), [], pending)
    write_markdown_file(theme_path, render_theme_markdown(
        "mobile-desktop", [], theme_labels={"mobile-desktop": "Mobile and Desktop"}), [], pending)

    assert pending == []
    release = frontmatter.load(release_path)
    assert release.content.startswith('<!-- chronolog:begin region="header" -->\n# Cursor Projects\n')
    assert "Tracked cards" not in release.content and "Cursor Cursor Projects" not in release.content
    theme = frontmatter.load(theme_path)
    assert theme.content.startswith('<!-- chronolog:begin region="header" -->\n# Mobile and Desktop\n')
    assert theme["title"] == "Mobile and Desktop"
    assert "Theme: mobile-desktop" not in theme.content


def test_migration_rewrites_legacy_release_with_stale_heading(tmp_path: Path):
    # The pre-W1 writer never refreshed a Release H1, so it can lag the record title.
    target = tmp_path / "release.md"
    release = release_record(title="Microsoft SharePoint connector")
    target.write_text(legacy_release_markdown(release, heading="Cursor Microsoft Sharepoint connector"),
                      encoding="utf-8")
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, render_release_markdown(release), conflicts, pending) is True

    assert conflicts == [] and pending == []
    assert "# Cursor · Microsoft SharePoint connector\n" in target.read_text(encoding="utf-8")
    assert "Sharepoint" not in frontmatter.load(target).content


@pytest.mark.parametrize("product_name, title, heading", [
    ("Cursor", "Cursor Projects", "Cursor Projects"),
    ("Claude Code", "v2.1.300", "Claude Code · v2.1.300"),
    ("ChatGPT", "Introducing GPT-4o", "ChatGPT · Introducing GPT-4o"),
    ("ChatGPT", "chatgpt search", "chatgpt search"),
    ("Claude Code", "Ship `/agents` view", "Claude Code · Ship `/agents` view"),
])
def test_release_heading_names_the_product_once(product_name, title, heading):
    release = release_record(product_name=product_name, title=title)

    post = frontmatter.loads(render_release_markdown(release))

    regions = extract_machine_regions(post.content)
    assert regions["header"].split("\n")[0] == f"# {heading}"
    assert post["title"] == heading.replace("`", "")
    assert regions["header"].endswith(
        f"**{product_name}** · 2025-02-01 · [Official release notes](https://cursor.com/changelog/projects)")


def test_release_summary_counts_tracked_and_candidate_lines():
    cards = [
        {**change_card(), "card_id": "cursor-2025-02-01-aaaaaa"},
        {**change_card(), "card_id": "cursor-2025-02-01-bbbbbb", "theme": "model-support",
         "title": "Model picker", "slug": "model-picker"},
        {**change_card(), "card_id": "cursor-2025-02-01-cccccc", "title": "Agent tabs", "slug": "agent-tabs"},
    ]
    body = "## What's changed\n" + "\n".join(f"- Candidate change line {n}" for n in range(7))
    release = {**release_record(title="v1.2"), "body": body, "cards": cards}

    post = frontmatter.loads(render_release_markdown(release, theme_labels=THEME_LABELS))

    regions = extract_machine_regions(post.content)
    assert regions["summary"] == (
        "3 tracked changes across 2 themes: Agent Mode, Model Support.\n\n"
        "Tracked 3 cards from 7 candidate lines.")
    assert regions["cards"].splitlines()[0] == "- [[2025-02-01-agent-shell|Agent shell]] · Agent Mode"
    assert "Model picker]] · Model Support" in regions["cards"]
    assert post["record"]["candidate_line_count"] == 7
    assert "body" not in post["record"]
    assert post["description"] == (
        "Cursor release v1.2 on 2025-02-01: 3 tracked changes across Agent Mode, Model Support")


def test_release_summary_uses_informative_source_summary_and_omits_unknown_denominator():
    release = release_record(title="v1.2", source_summary="Agents now run in the cloud.")

    post = frontmatter.loads(render_release_markdown(release))

    assert extract_machine_regions(post.content)["summary"] == (
        "Agents now run in the cloud.\n\nTracked 0 cards.")
    assert "candidate_line_count" not in post["record"]
    for generic in ("What's changed", "#New Features", "Release notes", "v1.2"):
        summary = extract_machine_regions(frontmatter.loads(render_release_markdown(
            release_record(title="v1.2", source_summary=generic))).content)["summary"]
        assert summary == "No change cards extracted.\n\nTracked 0 cards."


def test_candidate_line_count_survives_history_reconstruction():
    collected = {**release_record(), "body": "- First candidate line here\n- Second candidate line here"}

    releases, _, _ = merge_history(([], [], []), [collected], [], [], set())
    assert releases == [{**release_record(), "candidate_line_count": 2}]

    # Incremental runs rebuild releases from the frontmatter record, without a body.
    record = frontmatter.loads(render_release_markdown({**collected, "cards": []}))["record"]
    assert record["candidate_line_count"] == 2
    summary = extract_machine_regions(frontmatter.loads(
        render_release_markdown({**record, "cards": []})).content)["summary"]
    assert summary.endswith("Tracked 0 cards from 2 candidate lines.")


def test_theme_display_names_label_theme_index_and_product_pages():
    card = {**change_card(), "theme": "mobile-desktop"}
    labels = {"mobile-desktop": "Mobile and Desktop", "agent-mode": "Agent Mode"}
    editorial = "**Research question: what changed on _desktop_?**\n\nSecond paragraph."

    theme = frontmatter.loads(render_theme_markdown("mobile-desktop", [card], editorial=editorial,
                                                    theme_labels=labels))
    assert theme["title"] == "Mobile and Desktop"
    assert extract_machine_regions(theme.content)["header"] == (
        "# Mobile and Desktop\n\n1 tracked change in Cursor · 2025-02-01 → 2025-02-01")
    assert theme["description"] == "Research question: what changed on desktop?"
    plain = frontmatter.loads(render_theme_markdown("mobile-desktop", [card], theme_labels=labels))
    assert plain["description"] == "Cross-product timeline of Mobile and Desktop changes in Cursor."
    # Without a vocabulary entry the slug is title-cased.
    assert frontmatter.loads(render_theme_markdown("file-data", []))["title"] == "File Data"

    index = render_index_markdown([card], {"products": {}}, {"themes": {"agent-mode": {}, "mobile-desktop": {}}},
                                  {}, theme_labels=labels)
    assert "**Other** · [[Themes/mobile-desktop|Mobile and Desktop]] (1)" in index
    assert "- [[Themes/agent-mode|Agent Mode]] — From assisted edits to delegated work" in index

    info = {"product_name": "Cursor", "verbosity_baseline": 1, "eras": [],
            "top_themes": ["mobile-desktop", "agent-mode"]}
    product = render_product_markdown("cursor", info, [card], {card["card_id"]: "Changes/Cursor/x"},
                                      theme_labels=labels)
    assert "- [[Themes/mobile-desktop|Mobile and Desktop]] · 1 card · " + "█" * 12 in product
    assert "> - 2025-02-01 · Mobile and Desktop: [[Changes/Cursor/x|Agent shell]]" in product


def write_run_inputs(root: Path, run_id: str, cards, releases, analysis_b=None) -> None:
    paths = PipelinePaths(run_id, root=root)
    write_json(paths.valid_cards, {"change_cards": cards, "pending_theme_review": []})
    write_json(paths.analyze_a, {"products": {}, "evolves_from": {}})
    write_json(paths.analyze_b, analysis_b or {"themes": {}, "cards": {}})
    write_json(paths.silence, {"alerts": [], "pending": []})
    write_json(paths.collected, {"releases": releases})


def test_write_run_links_card_context_with_vocabulary_and_repository(tmp_path: Path):
    config = tmp_path / "config"
    (config / "_scripts").mkdir(parents=True)
    for name in ("themes.yaml", "sources.yaml"):
        (config / "_scripts" / name).write_text((ROOT / "_scripts" / name).read_text())
    vault = tmp_path / "vault"
    release = {**release_record(), "body": "- Agent can run shell commands.\n- Mobile app can review agent runs."}
    first = change_card()
    second = {**change_card(), "card_id": "cursor-2025-02-01-bbbbbb", "theme": "mobile-desktop",
              "title": "Mobile review", "slug": "mobile-review"}
    write_run_inputs(vault, "context", [first, second], [release])

    assert write_run("context", root=vault, config_root=config) == []

    card = frontmatter.load(vault / "Changes/Cursor/2025-02-01-agent-shell.md")
    regions = extract_machine_regions(card.content)
    assert regions["header"].endswith(
        "from [[Releases/Cursor/cursor-2025-02-01-v1|Cursor Projects]]")
    assert regions["context"] == (
        "## Also in this release\n\n"
        "- [[Changes/Cursor/2025-02-01-mobile-review|Mobile review]] · Mobile and Desktop")
    assert regions["footer"].startswith(f"[Report an issue with this card]({REPOSITORY}/issues/new?")
    page = frontmatter.load(vault / "Releases/Cursor/cursor-2025-02-01-v1.md")
    assert extract_machine_regions(page.content)["summary"].endswith(
        "Tracked 2 cards from 2 candidate lines.")
    assert frontmatter.load(vault / "Themes/mobile-desktop.md")["title"] == "Mobile and Desktop"
    assert not (PipelinePaths("context", vault).run_dir / "writer-migration-pending.json").exists()


def test_nearby_skips_same_release_siblings_in_both_directions(tmp_path: Path):
    earlier = {**related_card("chatgpt-2025-01-15-cccccc", "ChatGPT", "2025-01-15", "ChatGPT agent"),
               "source_release": "chatgpt-2025-01-15-r"}
    siblings = [
        {**change_card(), "card_id": f"cursor-2025-02-01-{suffix * 6}", "title": title,
         "slug": title.lower().replace(" ", "-")}
        for suffix, title in (("a", "Agent shell"), ("b", "Agent tabs"), ("e", "Agent queue"))
    ]
    later = {**related_card("claude-code-2025-03-01-dddddd", "Claude Code", "2025-03-01", "Background agents"),
             "source_release": "claude-code-2025-03-01-r"}
    releases = [
        release_record(),
        release_record(release_id="chatgpt-2025-01-15-r", product="chatgpt", product_name="ChatGPT",
                       date="2025-01-15", title="Agents", source_url="https://example.com/chatgpt"),
        release_record(release_id="claude-code-2025-03-01-r", product="claude-code",
                       product_name="Claude Code", date="2025-03-01", title="v2.0",
                       source_url="https://example.com/claude"),
    ]
    write_run_inputs(tmp_path, "nearby", [earlier, *siblings, later], releases)

    assert write_run("nearby", root=tmp_path) == []

    # The immediate neighbours of the middle card are its siblings; Nearby skips them.
    middle = frontmatter.load(tmp_path / "Changes/Cursor/2025-02-01-agent-tabs.md")
    regions = extract_machine_regions(middle.content)
    assert regions["nearby"] == (
        "## Nearby in Agent Mode\n\n"
        "- Earlier: 2025-01-15 · ChatGPT · [[Changes/ChatGPT/2025-01-15-chatgpt-agent|ChatGPT agent]]\n"
        "- Later: 2025-03-01 · Claude Code · "
        "[[Changes/Claude Code/2025-03-01-background-agents|Background agents]]")
    assert "Agent shell" in regions["context"] and "Agent queue" in regions["context"]
    first = frontmatter.load(tmp_path / "Changes/ChatGPT/2025-01-15-chatgpt-agent.md")
    assert extract_machine_regions(first.content)["nearby"] == (
        "## Nearby in Agent Mode\n\n"
        "- Later: 2025-02-01 · Cursor · [[Changes/Cursor/2025-02-01-agent-shell|Agent shell]]")


def test_write_run_reports_legacy_pages_kept_for_manual_migration(tmp_path: Path):
    card = change_card()
    target = tmp_path / "Changes/Cursor/2025-02-01-agent-shell.md"
    target.parent.mkdir(parents=True)
    target.write_text(legacy_change_markdown(card, notes="Keep me."), encoding="utf-8")
    write_run_inputs(tmp_path, "pending", [card], [release_record()])

    assert write_run("pending", root=tmp_path) == []

    from _scripts.common import read_json
    pending = read_json(PipelinePaths("pending", tmp_path).run_dir / "writer-migration-pending.json")
    assert pending == [{"file": "Changes/Cursor/2025-02-01-agent-shell.md",
                        "reason": MIGRATION_PENDING_REASON}]
    assert "Keep me." in target.read_text(encoding="utf-8")


# --- W1 PR 3: reader home page and About page ----------------------------------------

HOME_VOCABULARY = {
    "agent-mode": {"display_name": "Agent Mode", "category": "paradigm"},
    "model-support": {"display_name": "Model Support", "category": "capability"},
    "context-window": {"display_name": "Context Window", "category": "capability"},
    "safety-privacy": {"display_name": "Safety and Privacy", "category": "trust"},
}
HOME_LABELS = {slug: theme["display_name"] for slug, theme in HOME_VOCABULARY.items()}


def home_card(product: str, product_name: str, date: str, theme: str, suffix: str) -> dict:
    return {**change_card(), "card_id": f"{product}-{date}-{suffix}", "product": product,
            "product_name": product_name, "date": date, "theme": theme,
            "title": f"{product_name} {suffix}", "slug": f"{theme}-{suffix}",
            "source_release": f"{product}-{date}-r"}


def home_release(product: str, product_name: str, date: str) -> dict:
    return {"release_id": f"{product}-{date}-r", "product": product,
            "product_name": product_name, "date": date}


HOME_COVERAGE = {
    "chatgpt": {"acquisition": "browser-snapshot", "snapshot_captured_at": "2026-10-14T23:26:11+0800",
                "earliest": "2025-01-01", "latest": "2026-10-01", "release_count": 3,
                "url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
                "known_gaps": "Codex-only entries excluded."},
    "claude-code": {"acquisition": "http", "last_successful_fetch": "2026-10-15T01:55:15Z",
                    "earliest": "2026-10-14", "latest": "2026-10-14", "release_count": 1,
                    "url": "https://api.github.com/repos/anthropics/claude-code/releases"},
    "cursor": {"acquisition": "http", "last_successful_fetch": "2026-10-15T01:55:30Z",
               "earliest": "2026-08-01", "latest": "2026-10-13", "release_count": 2,
               "url": "https://cursor.com/changelog"},
}


def home_inputs(coverage=None):
    """Three products whose newest card (2026-10-14) anchors a 2026-09-15 window."""
    coverage = coverage or HOME_COVERAGE
    products = {
        product: {"product_name": name, "coverage": coverage[product]}
        for product, name in (("chatgpt", "ChatGPT"), ("claude-code", "Claude Code"), ("cursor", "Cursor"))
    }
    cards = [home_card("chatgpt", "ChatGPT", "2026-01-01", "model-support", "aaaaaa")]
    cards += [home_card("cursor", "Cursor", f"2026-10-{day:02d}", "agent-mode", f"c{day:05d}")
              for day in range(1, 10)]
    cards += [home_card("cursor", "Cursor", "2026-08-01", "model-support", "cold00")]
    cards += [home_card("claude-code", "Claude Code", "2026-10-14", theme, suffix)
              for theme, suffix in (("safety-privacy", "bbbbb1"), ("context-window", "bbbbb2"),
                                    ("context-window", "bbbbb0"), ("mystery-theme", "bbbbb3"))]
    releases = {
        "chatgpt": [home_release("chatgpt", "ChatGPT", day)
                    for day in ("2025-01-01", "2026-07-20", "2026-10-01")],
        "claude-code": [home_release("claude-code", "Claude Code", "2026-10-14")],
        "cursor": [home_release("cursor", "Cursor", day) for day in ("2026-08-01", "2026-10-13")],
    }
    themes = {"themes": {theme: {} for theme in {card["theme"] for card in cards}}}
    return cards, {"products": products}, themes, releases


def render_home(silence=None, coverage=None):
    cards, analysis_a, analysis_b, releases = home_inputs(coverage)
    return render_index_markdown(
        cards, analysis_a, analysis_b, silence or {"alerts": []}, theme_labels=HOME_LABELS,
        releases_by_product=releases, vocabulary=HOME_VOCABULARY,
    )


def test_counted_groups_thousands_for_headline_numbers():
    assert counted(1949, "tracked change") == "1,949 tracked changes"
    assert counted(1, "product") == "1 product"


def test_home_page_leads_with_latest_changes_anchored_on_data():
    post = frontmatter.loads(render_home(
        {"alerts": [{"product_name": "ChatGPT", "message": "No release for two months."}]}))
    regions = extract_machine_regions(post.content)

    assert list(regions) == ["header", "recent", "featured", "products", "themes", "coverage"]
    assert [line for line in post.content.splitlines() if line.startswith("## ")] == [
        "## Latest changes", "## Start exploring", "## Products", "## Themes", "## About the data"]
    assert regions["header"] == (
        "# ChronoLog\n\nTracked changes in ChatGPT, Claude Code and Cursor, from official release "
        "notes. 3 products · 15 tracked changes · 5 themes · archive to 2026-10-14 · "
        "[[About|About the data]]")
    recent = regions["recent"].split("\n\n")
    assert recent[0] == "- ⚠ ChatGPT: No release for two months."
    # The window ends at the newest card (2026-10-14), not at today's date.
    assert recent[1] == "### ChatGPT\n- No changes archived between 2026-09-15 and 2026-10-14."
    # Same date: ordered by theme, then card_id.
    assert recent[2] == "\n".join([
        "### Claude Code",
        "- 2026-10-14 · Context Window: [[2026-10-14-context-window-bbbbb0|Claude Code bbbbb0]]",
        "- 2026-10-14 · Context Window: [[2026-10-14-context-window-bbbbb2|Claude Code bbbbb2]]",
        "- 2026-10-14 · Mystery Theme: [[2026-10-14-mystery-theme-bbbbb3|Claude Code bbbbb3]]",
        "- 2026-10-14 · Safety and Privacy: [[2026-10-14-safety-privacy-bbbbb1|Claude Code bbbbb1]]",
    ])
    cursor = recent[3].splitlines()
    assert cursor[0] == "### Cursor"
    assert [line.split(" · ")[0] for line in cursor[1:7]] == [
        f"- 2026-10-{day:02d}" for day in range(9, 3, -1)]
    # Nine Cursor cards fall in the window; the 2026-08-01 card does not.
    assert cursor[7:] == ["- 3 more in this window → [[Products/Cursor|Cursor]]"]


def test_home_page_products_themes_and_coverage_summary():
    post = frontmatter.loads(render_home())
    regions = extract_machine_regions(post.content)

    # Releases in the 90 days ending at the newest release of any product (2026-10-14).
    assert regions["products"] == "\n".join([
        "- [[Products/ChatGPT|ChatGPT]] · 3 releases · 2025-01-01 → 2026-10-01 · "
        "2 releases in the last 90 days",
        "- [[Products/Claude Code|Claude Code]] · 1 release · 2026-10-14 → 2026-10-14 · "
        "1 release in the last 90 days",
        "- [[Products/Cursor|Cursor]] · 2 releases · 2026-08-01 → 2026-10-13 · "
        "2 releases in the last 90 days",
    ])
    assert regions["themes"] == "\n\n".join([
        "**Paradigm** · [[Themes/agent-mode|Agent Mode]] (9)",
        "**Capability** · [[Themes/context-window|Context Window]] (2) · "
        "[[Themes/model-support|Model Support]] (2)",
        "**Trust** · [[Themes/safety-privacy|Safety and Privacy]] (1)",
        "**Other** · [[Themes/mystery-theme|Mystery Theme]] (1)",
    ])
    assert regions["coverage"] == "\n".join([
        "- ChatGPT · 3 releases · 2025-01-01 → 2026-10-01 · [official source]"
        "(https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · "
        "Codex-only entries excluded.",
        "- Claude Code · 1 release · 2026-10-14 → 2026-10-14 · [official source]"
        "(https://github.com/anthropics/claude-code/releases)",
        "- Cursor · 2 releases · 2026-08-01 → 2026-10-13 · [official source](https://cursor.com/changelog)",
        "",
        "Acquisition times, how cards are made, review status and glossary: [[About|About the data]].",
    ])
    assert "Agent Mode]] — From assisted edits to delegated work" in regions["featured"]
    # Review counts and acquisition timestamps live on the About page only.
    for text in ("Pending theme review", "Alert count", "Overview", "T01:55", "+0800", "fetch"):
        assert text not in post.content


def legacy_index_markdown(lead: str = "") -> str:
    """index.md as the pre-W1 writer left it (production has no lead paragraph)."""
    regions = {
        "coverage": "### Cursor\n\nArchived release dates: 2026-08-01 → 2026-10-13.\n\n"
                    "Last successful fetch: 2026-10-15T01:55:30Z.",
        "featured": "- [[Themes/agent-mode|Agent Mode]] — From assisted edits to delegated work",
        "overview": "Product count: 1\nChange count: 1\nTheme count: 1\nAlert count: 0\n"
                    "Pending theme review: 0",
        "products": "- [[Products/Cursor|Cursor]]",
        "themes": "- [[Themes/agent-mode|Agent Mode]]",
    }
    fields = {"tags": ["index"], "title": "ChronoLog", "publication": "active",
              "date": "2026-10-13", "created": "2026-08-01", "modified": "2026-10-13"}
    fields["machine_hash"] = machine_hash(fields, regions)
    sections = [("Source coverage", "coverage"), ("Start exploring", "featured"),
                ("Overview", "overview"), ("Products", "products"), ("Themes", "themes")]
    body = "# ChronoLog\n\n" + (f"{lead}\n\n" if lead else "") + "\n\n".join(
        f"## {heading}\n{machine_region(region, regions[region])}" for heading, region in sections
    ) + "\n"
    return render_frontmatter(fields, body)


PRE_W1_INDEX_LEAD = (
    "Research changes in ChatGPT, Claude Code, and Cursor through official release evidence. "
    "Counts cover accepted active records; fixtures, pending review, and superseded records are excluded.")


@pytest.mark.parametrize("lead", ["", PRE_W1_INDEX_LEAD])
def test_legacy_index_migrates_to_the_reader_home_skeleton(tmp_path: Path, lead: str):
    target = tmp_path / "index.md"
    target.write_text(legacy_index_markdown(lead), encoding="utf-8")
    rendered = render_home()
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, conflicts, pending) is True

    post = frontmatter.load(target)
    assert conflicts == [] and pending == []
    assert post.content == frontmatter.loads(rendered).content
    assert "## Overview" not in post.content and "Product count:" not in post.content
    assert "Research changes in" not in post.content
    migrated = target.read_bytes()
    write_markdown_file(target, rendered, conflicts, pending)
    assert target.read_bytes() == migrated and conflicts == [] and pending == []
    fresh = tmp_path / "fresh.md"
    write_markdown_file(fresh, rendered, [], [])
    assert fresh.read_bytes() == migrated


def test_legacy_index_with_human_text_keeps_its_structure_and_is_reported(tmp_path: Path):
    target = tmp_path / "index.md"
    target.write_text(legacy_index_markdown("A note a reviewer wrote."), encoding="utf-8")
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, render_home(), conflicts, pending) is True

    post = frontmatter.load(target)
    assert conflicts == []
    assert pending == [{"file": str(target), "reason": MIGRATION_PENDING_REASON}]
    assert "A note a reviewer wrote." in post.content and "## Overview" in post.content
    assert list(extract_machine_regions(post.content)) == [
        "coverage", "featured", "overview", "products", "themes"]
    assert "[[Products/Cursor|Cursor]] · 2 releases" in post.content
    # The kept file stays consistent, so the next run is not blocked by a hash conflict.
    assert write_markdown_file(target, render_home(), conflicts, []) is True and conflicts == []


def render_about(coverage=None, repository=REPOSITORY, pending=149):
    cards, analysis_a, _, releases = home_inputs(coverage)
    return render_about_markdown(cards, analysis_a["products"], releases, {"alerts": []},
                                 pending_theme_review=pending, repository=repository)


def test_about_page_documents_sources_method_status_and_feedback():
    post = frontmatter.loads(render_about(pending=1234))
    regions = extract_machine_regions(post.content)

    assert post["title"] == "About the data" and post["tags"] == ["about"]
    assert post["publication"] == "active" and len(post["description"]) <= 160
    assert post.content.startswith("# About the data\n\n")
    assert list(regions) == ["intro", "sources", "method", "status", "glossary", "feedback"]
    assert "three products: ChatGPT, Claude Code and Cursor" in regions["intro"]
    assert regions["sources"].split("\n\n")[0] == "\n".join([
        "### ChatGPT",
        "- Official source: [ChatGPT release notes]"
        "(https://help.openai.com/en/articles/6825453-chatgpt-release-notes)",
        "- Archived releases: 3, dated 2025-01-01 → 2026-10-01",
        "- Official browser snapshot captured: 2026-10-14T23:26:11+0800. "
        "Imported snapshot; this is not a successful automatic HTTP fetch.",
        "- Known gaps: Codex-only entries excluded.",
    ])
    assert ("- Official source: [Claude Code GitHub releases]"
            "(https://github.com/anthropics/claude-code/releases)") in regions["sources"]
    assert "- Last successful fetch: 2026-10-15T01:55:15Z." in regions["sources"]
    assert "At most" not in regions["method"] and "sampled" not in regions["method"]
    assert "digest card per release" in regions["method"]
    assert "Tracked N cards from M candidate lines" in regions["method"]
    assert regions["status"].startswith(
        "3 products · 6 archived releases · 15 tracked changes · 5 themes. "
        "Pending theme review: 1,234. Silence alerts: 0.")
    for term in ("Change Card", "Digest card", "Other changes", "Release", "Theme", "Era",
                 "Tracked products only", "Candidate line"):
        assert f"- **{term}**: " in regions["glossary"]
    assert regions["feedback"].endswith(f"open an issue at [{REPOSITORY}/issues]({REPOSITORY}/issues).")
    assert extract_machine_regions(render_about(repository=""))["feedback"] == ""


def test_acquisition_time_only_refresh_is_not_a_content_change(tmp_path: Path):
    later = {
        "chatgpt": {**HOME_COVERAGE["chatgpt"], "snapshot_captured_at": "2026-10-16T08:00:00+0800",
                    "acquired_at": "2026-10-16T08:00:00+0800"},
        "claude-code": {**HOME_COVERAGE["claude-code"], "last_successful_fetch": "2026-10-16T01:15:02Z"},
        "cursor": {**HOME_COVERAGE["cursor"], "last_successful_fetch": "2026-10-16T01:15:09Z"},
    }
    cards, analysis_a, _, releases = home_inputs()
    pages = {}
    for name, coverage in (("before", HOME_COVERAGE), ("after", later)):
        about = tmp_path / name / "About.md"
        about.parent.mkdir()
        about.write_text(render_about(coverage), encoding="utf-8")
        product = tmp_path / name / "ChatGPT.md"
        product.write_text(render_product_markdown(
            "chatgpt", {"product_name": "ChatGPT", "verbosity_baseline": 1, "coverage": coverage["chatgpt"]},
            [cards[0]], releases=releases["chatgpt"]), encoding="utf-8")
        pages[name] = (about, product)

    for before, after in zip(pages["before"], pages["after"]):
        assert before.read_text() != after.read_text()
        assert normalized_page(before) == normalized_page(after)
    # A changed source fact is still a content change.
    gaps = {**HOME_COVERAGE, "cursor": {**HOME_COVERAGE["cursor"], "known_gaps": "New gap."}}
    changed = tmp_path / "changed.md"
    changed.write_text(render_about(gaps), encoding="utf-8")
    assert normalized_page(changed) != normalized_page(pages["before"][0])


def test_product_coverage_region_is_a_one_line_summary_linking_about():
    info = {"product_name": "ChatGPT", "verbosity_baseline": 1, "coverage": HOME_COVERAGE["chatgpt"]}
    cards, _, _, releases = home_inputs()
    regions = extract_machine_regions(frontmatter.loads(
        render_product_markdown("chatgpt", info, [cards[0]], releases=releases["chatgpt"])).content)
    assert regions["coverage"] == (
        "3 releases · 2025-01-01 → 2026-10-01 · [official source]"
        "(https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · "
        "Codex-only entries excluded.\n\n"
        "Acquisition details, how cards are made and known gaps: [[About]].")


def digest_card() -> dict[str, object]:
    bullets = ["Added agent checkpoints", "Improved agent startup", "Changed the agent status line"]
    return {
        **change_card(), "card_id": "claude-code-2026-10-14-dddddd", "product": "claude-code",
        "product_name": "Claude Code", "source_release": "claude-code-2026-10-14-v2-1-300",
        "date": "2026-10-14", "title": "3 Agent Mode changes in v2.1.300",
        "slug": "3-agent-mode-changes-in-v2-1-300", "kind": "digest",
        "evidence": [{"source_release": "https://github.com/anthropics/claude-code/releases/tag/v2.1.300",
                      "quote": quote} for quote in bullets],
        "extractor_version": "fallback-v5",
    }


def test_digest_card_lists_each_change_and_names_the_release():
    card = digest_card()
    post = frontmatter.loads(render_change_markdown(
        card, {}, {}, {card["card_id"]: "Changes/Claude Code/x"},
        release_target="Releases/Claude Code/v2-1-300", release_title="v2.1.300",
        theme_labels=THEME_LABELS))
    regions = extract_machine_regions(post.content)

    assert regions["header"].splitlines()[2] == (
        "**Claude Code** · 2026-10-14 · [[Themes/agent-mode|Agent Mode]] · Digest · "
        "[Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · "
        "from [[Releases/Claude Code/v2-1-300|v2.1.300]]")
    assert regions["evidence"] == (
        "## Changes in this digest\n\n"
        "> Added agent checkpoints\n\n> Improved agent startup\n\n> Changed the agent status line\n\n"
        "Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300")
    assert post["kind"] == "digest"
    assert post["description"] == (
        "Claude Code · 2026-10-14 · Agent Mode: 3 changes in v2.1.300 — Added agent checkpoints")


def test_multi_paragraph_card_quotes_one_group_and_labels_kind_and_scope():
    card = {**change_card(), "kind": "launch", "scope": "iOS",
            "evidence": [{"source_release": "https://example.com", "quote": "First paragraph."},
                         {"source_release": "https://example.com", "quote": "Second paragraph."}]}
    regions = extract_machine_regions(frontmatter.loads(
        render_change_markdown(card, {}, {}, theme_labels=THEME_LABELS)).content)

    assert regions["evidence"] == (
        "> First paragraph.\n>\n> Second paragraph.\n>\n> Source: https://example.com")
    assert regions["header"].splitlines()[2] == (
        "**Cursor** · 2025-02-01 · [[Themes/agent-mode|Agent Mode]] · Launch · iOS · "
        "[Official source](https://example.com)")
    plain = extract_machine_regions(frontmatter.loads(
        render_change_markdown({**change_card(), "kind": "change"}, {}, {}, theme_labels=THEME_LABELS)
    ).content)
    assert plain["header"].splitlines()[2] == (
        "**Cursor** · 2025-02-01 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://example.com)")


def test_release_summary_reports_cards_candidate_lines_and_pending_lines():
    cards = [{**change_card(), "kind": "launch"}, {**digest_card(), "source_release": "cursor-2025-02-01-v1",
                                                   "date": "2025-02-01", "card_id": "cursor-2025-02-01-dddddd"}]
    body = "## What's changed\n" + "\n".join(f"- Candidate change line {n}" for n in range(9))
    release = {**release_record(title="v1.2", source_summary=""), "body": body, "cards": cards}

    post = frontmatter.loads(render_release_markdown(release, theme_labels=THEME_LABELS, pending_lines=2))
    regions = extract_machine_regions(post.content)

    assert regions["summary"].endswith("Tracked 2 cards from 9 candidate lines; 2 lines pending review.")
    assert "Agent shell]] · Agent Mode · Launch" in regions["cards"]
    assert "3 Agent Mode changes in v2.1.300]] · Agent Mode · Digest" in regions["cards"]
    single = frontmatter.loads(render_release_markdown(
        {**release, "cards": cards[:1]}, theme_labels=THEME_LABELS, pending_lines=1))
    assert extract_machine_regions(single.content)["summary"].endswith(
        "Tracked 1 card from 9 candidate lines; 1 line pending review.")


def test_write_run_counts_pending_lines_per_release(tmp_path: Path):
    vault = tmp_path / "vault"
    release = {**release_record(), "body": "- Agent can run shell commands.\n- New quasar renderer here."}
    pending = {**change_card(), "card_id": "cursor-2025-02-01-cccccc", "theme": "__candidate__",
               "theme_suggestion": "quasar", "title": "Quasar", "slug": "quasar",
               "evidence": [{"source_release": "https://example.com", "quote": "New quasar renderer here."}]}
    write_run_inputs(vault, "pending", [change_card()], [release])
    paths = PipelinePaths("pending", root=vault)
    write_json(paths.valid_cards, {"change_cards": [change_card()], "pending_theme_review": [pending]})

    assert write_run("pending", root=vault) == []
    page = frontmatter.load(vault / "Releases/Cursor/cursor-2025-02-01-v1.md")
    assert extract_machine_regions(page.content)["summary"].endswith(
        "Tracked 1 card from 2 candidate lines; 1 line pending review.")


def test_merge_history_resolves_pending_lines_absorbed_into_new_cards():
    old_pending = {**change_card(), "card_id": "cursor-2025-02-01-cccccc", "theme": "__candidate__",
                   "evidence": [{"source_release": "https://example.com", "quote": "Second paragraph."}]}
    unrelated = {**old_pending, "card_id": "cursor-2025-02-01-eeeeee",
                 "evidence": [{"source_release": "https://example.com", "quote": "Elsewhere."}]}
    card = {**change_card(), "evidence": [
        {"source_release": "https://example.com", "quote": "First paragraph."},
        {"source_release": "https://example.com", "quote": "Second paragraph!"}]}

    _, cards, queue = merge_history(([], [], [old_pending, unrelated]), [], [card], [], {"cursor"})

    assert [c["card_id"] for c in cards] == [card["card_id"]]
    assert [c["card_id"] for c in queue] == [unrelated["card_id"]]


def test_reconcile_replaces_queue_entries_of_reextracted_releases_only():
    stale = {**change_card(), "card_id": "cursor-2025-02-01-cccccc", "theme": "__candidate__",
             "evidence": [{"source_release": "https://example.com", "quote": "Improvements (6)↓↑"}]}
    elsewhere = {**stale, "card_id": "cursor-2025-01-01-eeeeee", "source_release": "cursor-2025-01-01-v0"}
    collected = {**release_record(), "body": "- Agent can run shell commands."}

    _, _, queue = merge_history(([], [], [stale, elsewhere]), [collected], [change_card()], [], {"cursor"})
    assert [c["card_id"] for c in queue] == [elsewhere["card_id"]]
    # Without reconciliation an unmatched entry stays queued.
    _, _, queue = merge_history(([], [], [stale]), [collected], [change_card()], [], set())
    assert [c["card_id"] for c in queue] == [stale["card_id"]]


def test_merge_history_matches_lines_without_list_markers():
    old = {**change_card(), "card_id": "chatgpt-2025-03-18-aaaaaa", "theme": "__candidate__",
           "evidence": [{"source_release": "https://example.com", "quote": "3⁠. Improved quote display."}]}
    card = {**change_card(), "evidence": [{"source_release": "https://example.com",
                                           "quote": "Improved quote display."}]}

    _, _, queue = merge_history(([], [], [old]), [], [card], [], set())
    assert queue == []


def test_reactivated_superseded_legacy_card_takes_the_new_template(tmp_path: Path):
    # A pre-W1 superseded page has neither record nor title, so its old H1 cannot be
    # matched; it was never refreshed, so it is generated text, not a human edit.
    target = tmp_path / "change.md"
    legacy = frontmatter.loads(legacy_change_markdown(change_card()).replace(
        "# Agent shell\n", "# Agent can run shell commands.\n"))
    for key in ("record", "title"):
        legacy.metadata.pop(key)
    legacy["superseded"] = True
    legacy["machine_hash"] = machine_hash(
        {k: v for k, v in legacy.metadata.items() if k != "machine_hash"},
        extract_machine_regions(legacy.content))
    target.write_text(frontmatter.dumps(legacy), encoding="utf-8")
    rendered = render_change_markdown(change_card(), {"evolves_from": []}, {})
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, [], pending) is True

    post = frontmatter.load(target)
    assert pending == []
    assert post.content == frontmatter.loads(rendered).content
    assert "superseded" not in post.metadata


# --- W2 PR 2: holding theme "uncategorized" ("Other changes") --------------------------

OTHER_LABELS = {**THEME_LABELS, "uncategorized": "Other changes"}
OTHER_LINES = ["Added new quasar renderer for geometric palettes",
               "Changed the zephyr gauge to round half values up"]
V300_URL = "https://github.com/anthropics/claude-code/releases/tag/v2.1.300"


def other_digest_card() -> dict[str, object]:
    return {**digest_card(), "card_id": "claude-code-2026-10-14-000000", "theme": "uncategorized",
            "title": "2 other changes in v2.1.300", "slug": "2-other-changes-in-v2-1-300",
            "evidence": [{"source_release": V300_URL, "quote": quote} for quote in OTHER_LINES]}


def test_other_changes_card_has_a_plain_label_and_only_release_context():
    card, sibling = other_digest_card(), digest_card()
    neighbour = {**related_card("cursor-2026-10-01-eeeeee", "Cursor", "2026-10-01", "Cursor quasar",
                                "uncategorized")}
    targets = {card["card_id"]: "Changes/Claude Code/other", sibling["card_id"]: "Changes/Claude Code/agent"}
    post = frontmatter.loads(render_change_markdown(
        card, {"evolves_from": []}, {}, targets, release_target="Releases/Claude Code/v2-1-300",
        release_title="v2.1.300", siblings=[card, sibling], earlier=neighbour,
        theme_labels=OTHER_LABELS))
    regions = extract_machine_regions(post.content)

    assert regions["header"].splitlines()[2] == (
        f"**Claude Code** · 2026-10-14 · Other changes · Digest · [Official source]({V300_URL}) · "
        "from [[Releases/Claude Code/v2-1-300|v2.1.300]]")
    assert "Themes/" not in post.content
    assert regions["context"] == (
        "## Also in this release\n\n"
        "- [[Changes/Claude Code/agent|3 Agent Mode changes in v2.1.300]] · Agent Mode")
    assert regions["nearby"] == "" and regions["relations"] == ""
    assert "diffusion" not in post.metadata and "related_changes" not in post.metadata
    assert post["description"] == (
        "Claude Code · 2026-10-14 · Other changes: 2 changes in v2.1.300 — "
        "Added new quasar renderer for geometric palettes")
    # Seen from a themed card of the release, Other changes come last.
    themed = {**digest_card(), "card_id": "claude-code-2026-10-14-ffffff", "title": "Agent tabs"}
    context = extract_machine_regions(frontmatter.loads(render_change_markdown(
        sibling, {}, {}, siblings=[card, sibling, themed], theme_labels=OTHER_LABELS)).content)["context"]
    assert [line.rsplit(" · ", 1)[1] for line in context.splitlines()[2:]] == [
        "Agent Mode", "Other changes"]


def test_release_page_lists_other_changes_last_and_outside_the_theme_count():
    from _scripts.history import historical_source_summary
    agent, other = digest_card(), other_digest_card()
    body = "## What's changed\n" + "\n".join(f"- Candidate change line {n}" for n in range(9))
    release = {**release_record(release_id="claude-code-2026-10-14-v2-1-300", product="claude-code",
                                product_name="Claude Code", date="2026-10-14", title="v2.1.300",
                                source_summary="", source_url=V300_URL),
               "body": body, "cards": [other, agent]}

    post = frontmatter.loads(render_release_markdown(release, theme_labels=OTHER_LABELS, pending_lines=1))
    regions = extract_machine_regions(post.content)

    assert regions["summary"] == (
        "2 tracked changes across 1 theme: Agent Mode; 1 in Other changes.\n\n"
        "Tracked 2 cards from 9 candidate lines; 1 line pending review.")
    assert regions["cards"].splitlines() == [
        "- [[2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · "
        "Agent Mode · Digest",
        "- [[2026-10-14-2-other-changes-in-v2-1-300|2 other changes in v2.1.300]] · "
        "Other changes · Digest",
    ]
    assert post["description"] == (
        "Claude Code release v2.1.300 on 2026-10-14: 2 tracked changes across Agent Mode, Other changes")
    only_other = extract_machine_regions(frontmatter.loads(render_release_markdown(
        {**release, "cards": [other]}, theme_labels=OTHER_LABELS)).content)["summary"]
    assert only_other == "1 tracked change, all in Other changes.\n\nTracked 1 card from 9 candidate lines."
    # Rebuilding a legacy Release page never mistakes the generated line for a source summary.
    assert historical_source_summary(only_other) == ""


def test_home_index_product_and_about_leave_other_changes_out_of_themes():
    from _scripts.analyze_a import analyze_products
    cards, analysis_a, analysis_b, releases = home_inputs()
    other = [home_card("claude-code", "Claude Code", "2026-10-20", "uncategorized", "bbbbb9"),
             home_card("cursor", "Cursor", "2026-10-09", "uncategorized", "c00099"),
             home_card("cursor", "Cursor", "2026-10-08", "uncategorized", "c00098")]
    labels = {**HOME_LABELS, "uncategorized": "Other changes"}
    vocabulary = {**HOME_VOCABULARY, "uncategorized": {"display_name": "Other changes",
                                                        "category": "other", "status": "holding"}}

    def home(card_set):
        return extract_machine_regions(frontmatter.loads(render_index_markdown(
            card_set, analysis_a, analysis_b, {"alerts": []}, theme_labels=labels,
            releases_by_product=releases, vocabulary=vocabulary)).content)

    before, after = home(cards), home(cards + other)
    # Same window (a newer Other changes card does not move it), entries and "3 more".
    assert after["recent"] == before["recent"]
    assert "Other changes" not in after["recent"]
    assert after["themes"] == before["themes"] and "uncategorized" not in after["themes"]
    assert "18 tracked changes · 5 themes" in after["header"]

    info = analyze_products(cards + other)["products"]["cursor"]
    product = render_product_markdown("cursor", info, [c for c in cards + other if c["product"] == "cursor"],
                                      theme_labels=labels)
    themes = extract_machine_regions(frontmatter.loads(product).content)["themes"].splitlines()
    assert themes[0].startswith("- [[Themes/agent-mode|Agent Mode]] · ")
    assert themes[-1] == "- Other changes · 2 cards"  # plain text, listed last
    assert "> - 2026-10-09 · Other changes: [[2026-10-09-uncategorized-c00099|Cursor c00099]]" in product

    about = extract_machine_regions(frontmatter.loads(render_about_markdown(
        cards + other, analysis_a["products"], releases, {"alerts": []})).content)
    assert about["status"].startswith("3 products · 6 archived releases · 18 tracked changes · 5 themes.")
    assert '"Other changes" digest of their release' in about["method"]
    assert "prose without a theme waits in a review queue" in about["method"]
    assert "- **Other changes**: " in about["glossary"]


def test_write_run_gives_other_changes_no_theme_page_and_no_neighbours(tmp_path: Path):
    config = tmp_path / "config"
    (config / "_scripts").mkdir(parents=True)
    for name in ("themes.yaml", "sources.yaml"):
        (config / "_scripts" / name).write_text((ROOT / "_scripts" / name).read_text())
    vault = tmp_path / "vault"
    first = {**release_record(), "body": "- Agent can run shell commands.\n- Quasar one here.\n- Quasar two here."}
    second = release_record(release_id="cursor-2025-03-01-v2", date="2025-03-01", title="Later release")
    agent = change_card()
    other = {**change_card(), "card_id": "cursor-2025-02-01-000000", "theme": "uncategorized",
             "kind": "digest", "title": "2 other changes in Cursor Projects",
             "slug": "2-other-changes-in-cursor-projects", "extractor_version": "fallback-v5",
             "evidence": [{"source_release": "https://example.com", "quote": quote}
                          for quote in ("Quasar one here.", "Quasar two here.")]}
    later = {**other, "card_id": "cursor-2025-03-01-111111", "date": "2025-03-01", "kind": "change",
             "source_release": "cursor-2025-03-01-v2", "title": "Quasar three", "slug": "quasar-three",
             "evidence": [{"source_release": "https://example.com", "quote": "Quasar three here."}]}
    write_run_inputs(vault, "other", [agent, other, later], [first, second])
    stale = vault / "Themes/uncategorized.md"
    stale.parent.mkdir(parents=True)
    stale.write_text(render_theme_markdown("uncategorized", [other]), encoding="utf-8")
    stale_text = stale.read_text(encoding="utf-8")

    assert write_run("other", root=vault, config_root=config, reconcile=True) == []

    assert sorted(path.name for path in (vault / "Themes").glob("*.md")) == [
        "agent-mode.md", "uncategorized.md"]
    assert stale.read_text(encoding="utf-8") == stale_text  # never refreshed or created
    page = frontmatter.load(vault / "Changes/Cursor/2025-02-01-2-other-changes-in-cursor-projects.md")
    regions = extract_machine_regions(page.content)
    assert " · Other changes · Digest · " in regions["header"]
    assert regions["nearby"] == "" and regions["relations"] == ""
    assert regions["context"] == (
        "## Also in this release\n\n- [[Changes/Cursor/2025-02-01-agent-shell|Agent shell]] · Agent Mode")
    release = frontmatter.load(vault / "Releases/Cursor/cursor-2025-02-01-v1.md")
    assert extract_machine_regions(release.content)["cards"].splitlines()[-1].endswith(
        "· Other changes · Digest")
    product = (vault / "Products/Cursor.md").read_text(encoding="utf-8")
    assert "> - 2025-03-01 · Other changes: [[Changes/Cursor/2025-03-01-quasar-three|Quasar three]]" in product
    index = extract_machine_regions(frontmatter.load(vault / "index.md").content)
    assert "Other changes" not in index["recent"] and "uncategorized" not in index["themes"]


def test_no_theme_page_is_written_for_other_changes(tmp_path: Path):
    other = {**change_card(), "theme": "uncategorized"}
    write_run_inputs(tmp_path, "other", [other], [release_record()])

    assert write_run("other", root=tmp_path) == []
    assert not (tmp_path / "Themes/uncategorized.md").exists()
    assert list((tmp_path / "Themes").glob("*.md")) == []


def test_merge_history_retires_pending_lines_published_as_other_changes():
    old_pending = [
        {**change_card(), "card_id": f"cursor-2025-02-01-{suffix * 6}", "theme": "__candidate__",
         "theme_suggestion": "quasar", "evidence": [{"source_release": "https://example.com",
                                                     "quote": f"- {quote}"}]}
        for suffix, quote in zip("ce", OTHER_LINES)
    ]
    elsewhere = {**old_pending[0], "card_id": "cursor-2025-01-01-ffffff", "source_release": "cursor-2025-01-01-v0"}
    other = {**change_card(), "card_id": "cursor-2025-02-01-000000", "theme": "uncategorized", "kind": "digest",
             "evidence": [{"source_release": "https://example.com", "quote": quote} for quote in OTHER_LINES]}

    # An incremental batch: only the "lines joined a card of the same release" rule applies.
    _, cards, queue = merge_history(([], [], [*old_pending, elsewhere]), [], [other], [], set())

    assert [card["card_id"] for card in cards] == [other["card_id"]]
    assert [card["card_id"] for card in queue] == [elsewhere["card_id"]]


# --- W2 PR 3: theme pages, monthly archive, cadence panel --------------------------------

from _scripts.writer import (  # noqa: E402
    AUTO_MOMENTS_CAPTION,
    KEY_MOMENTS_PER_PRODUCT,
    KEY_MOMENTS_TOTAL,
    auto_key_moments,
    granularity_note,
    render_archive_markdown,
    render_archive_month_markdown,
    render_cadence,
)

VERBOSITY = {"ChatGPT": 1.71, "Claude Code": 6.91, "Cursor": 4.04, "Aider": 9.0}
SCOPE_CALLOUT = (
    "> [!info]- How to read this timeline\n"
    "> Scope: tracked-products-only. Entries show same-theme chronology; they do not establish "
    "equivalent capabilities, adoption, or causation.")


def moment(product_name, date, suffix, kind="change", impact="incremental", title=None,
           release=None, theme="agent-mode", quote=None):
    product = product_name.lower().replace(" ", "-")
    title = title or f"{product_name} {suffix}"
    return {**change_card(), "card_id": f"{product}-{date}-{suffix}", "product": product,
            "product_name": product_name, "date": date, "theme": theme, "kind": kind,
            "impact": impact, "title": title, "slug": f"{product}-{suffix}",
            "source_release": release or f"{product}-{date}-r",
            "evidence": [{"source_release": "https://example.com", "quote": quote or title}]}


def theme_regions(cards, **kwargs):
    post = frontmatter.loads(render_theme_markdown(
        "agent-mode", cards, theme_labels=THEME_LABELS, verbosity=VERBOSITY, **kwargs))
    return post, extract_machine_regions(post.content)


def test_theme_page_header_sections_and_scope_callout():
    cards = [moment("Cursor", "2025-03-01", "c00001", kind="launch"),
             moment("Claude Code", "2026-10-14", "b00001"),
             moment("ChatGPT", "2026-07-09", "a00001", kind="launch")]
    post, regions = theme_regions(cards)

    assert list(regions) == ["header", "narrative", "moments", "scope", "timeline"]
    assert [line for line in post.content.splitlines() if line.startswith("## ")] == [
        "## Research summary", "## Key moments", "## Timeline"]
    # Granularity: most granular product first; Aider has no card in the theme.
    assert regions["header"] == (
        "# Agent Mode\n\n3 tracked changes across ChatGPT, Claude Code and Cursor · "
        "2025-03-01 → 2026-10-14 · Claude Code averages 6.9 cards per release, Cursor 4.0, "
        "ChatGPT 1.7")
    assert regions["scope"] == SCOPE_CALLOUT
    assert "Active changes" not in post.content and "Cross-Product Timeline" not in post.content
    assert post["description"] == "Cross-product timeline of Agent Mode changes in ChatGPT, Claude Code and Cursor."
    empty = extract_machine_regions(frontmatter.loads(render_theme_markdown("agent-mode", [])).content)
    assert empty["header"] == "# Agent Mode\n\nNo tracked changes yet."
    assert empty["timeline"] == "No changes yet."
    assert granularity_note(["Cursor"], {}) == ""


def test_theme_timeline_groups_by_year_and_month_with_counts():
    cards = [
        moment("Cursor", "2026-10-06", "c00001", kind="launch"),
        moment("Claude Code", "2026-10-14", "b00001", kind="digest", title="3 Agent Mode changes in v2.1.300"),
        moment("Claude Code", "2026-10-06", "b00002", kind="fix"),
        moment("Cursor", "2026-09-30", "c00002", kind="expansion"),
        moment("ChatGPT", "2026-09-29", "a00001", kind="pricing"),
        moment("Cursor", "2025-12-01", "c00003", kind="policy"),
    ]
    _, regions = theme_regions(cards, card_targets={card["card_id"]: f"Changes/x/{card['card_id']}"
                                                    for card in cards})

    assert regions["timeline"] == "\n".join([
        "### 2026 · 5 entries (ChatGPT 1 · Claude Code 2 · Cursor 2)",
        "",
        "#### 2026-10",
        "",
        "- 2026-10-14 · **Claude Code** · [[Changes/x/claude-code-2026-10-14-b00001|3 Agent Mode changes in v2.1.300]] · Digest",
        "- 2026-10-06 · **Claude Code** · [[Changes/x/claude-code-2026-10-06-b00002|Claude Code b00002]]",
        "- 2026-10-06 · **Cursor** · [[Changes/x/cursor-2026-10-06-c00001|Cursor c00001]] · Launch",
        "",
        "#### 2026-09",
        "",
        "- 2026-09-30 · **Cursor** · [[Changes/x/cursor-2026-09-30-c00002|Cursor c00002]]",
        "- 2026-09-29 · **ChatGPT** · [[Changes/x/chatgpt-2026-09-29-a00001|ChatGPT a00001]] · Pricing",
        "",
        "### 2025 · 1 entry (Cursor 1)",
        "",
        "#### 2025-12",
        "",
        "- 2025-12-01 · **Cursor** · [[Changes/x/cursor-2025-12-01-c00003|Cursor c00003]] · Policy",
    ])


def test_key_moments_are_launches_and_announcements_one_per_release():
    from _scripts.writer import moment_tier
    cards = [
        # Claude Code: one release with a launch and a high-signal line keeps the launch.
        moment("Claude Code", "2026-10-14", "b00001", kind="launch", release="cc-300"),
        moment("Claude Code", "2026-10-14", "b00002", title="Added /advisor to plan work", release="cc-300"),
        # Standalone announcements recognised from the quote and from the title.
        moment("Claude Code", "2026-09-01", "b00003", title="Agent hooks",
               quote="Introducing agent hooks for every tool call"),
        moment("Claude Code", "2026-08-01", "b00004", title="Background agents are now on by default"),
        # Machine impact does not qualify; digests and fixes never do.
        moment("Claude Code", "2026-07-01", "b00005", impact="paradigm-shift"),
        moment("Claude Code", "2026-06-01", "b00006", kind="digest", title="Introducing 3 changes"),
        moment("Claude Code", "2026-05-01", "b00007", kind="fix", title="Introducing a fix"),
        moment("Claude Code", "2026-04-01", "b00008"),
        moment("ChatGPT", "2026-07-09", "a00001", kind="launch"),
    ]
    targets = {card["card_id"]: f"Changes/x/{card['card_id']}" for card in cards}
    _, regions = theme_regions(cards, card_targets=targets)

    assert [moment_tier(card) for card in cards] == [0, 1, 1, 1, None, None, None, None, 0]
    assert moment_tier(moment("Cursor", "2026-01-01", "c00001", kind="launch", theme="uncategorized")) is None
    assert [card["card_id"][-6:] for card in auto_key_moments(cards)] == [
        "b00001", "b00003", "b00004", "a00001"]
    assert regions["moments"] == "\n".join([
        AUTO_MOMENTS_CAPTION,
        "",
        "| Quarter | ChatGPT | Claude Code |",
        "| --- | --- | --- |",
        "| 2026 Q4 | · | 2026-10-14 [[Changes/x/claude-code-2026-10-14-b00001\\|Claude Code b00001]] |",
        "| 2026 Q3 | 2026-07-09 [[Changes/x/chatgpt-2026-07-09-a00001\\|ChatGPT a00001]] | "
        "2026-09-01 [[Changes/x/claude-code-2026-09-01-b00003\\|Agent hooks]]<br>"
        "2026-08-01 [[Changes/x/claude-code-2026-08-01-b00004\\|Background agents are now on by default]] |",
    ])
    only_digests = [moment("Cursor", "2026-01-01", "c00001", kind="digest"),
                    moment("Cursor", "2026-02-01", "c00002", impact="significant")]
    assert theme_regions(only_digests)[1]["moments"] == f"No key moments selected yet. {AUTO_MOMENTS_CAPTION}"


def test_key_moments_take_one_per_quarter_first_then_fill_newest_best():
    # Ten 2026 launches, a 2025 launch (Background Agent) and a 2024 announcement.
    cards = [moment("Cursor", f"2026-{month:02d}-{day:02d}", f"c{month:02d}{day:02d}", kind="launch")
             for month, day in ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 20), (6, 5), (7, 5), (8, 5), (9, 5))]
    cards += [moment("Cursor", "2026-09-20", "c0920", title="Agents can now run tests",
                     quote="You can now run tests from an agent"),
              moment("Cursor", "2025-05-15", "c0515", kind="launch", title="Background Agent"),
              moment("Cursor", "2024-11-01", "c1101", title="Introducing Composer")]

    picked = [card["card_id"][-5:] for card in auto_key_moments(cards)]

    # Quarter picks: 2026 Q3 takes the launch over a newer announcement; 2025 Q2 and
    # 2024 Q4 are represented. The other 7 slots go to the newest remaining launches.
    assert picked == ["c0905", "c0805", "c0705", "c0605", "c0520", "c0505", "c0405", "c0305",
                      "c0205", "c0105", "c0515", "c1101"]
    assert "c0920" not in picked
    # With more than 12 quarters, the 12 newest quarters are kept.
    spread = [moment("Cursor", f"{2023 + index // 4}-{(index % 4) * 3 + 1:02d}-01", f"q{index:04d}",
                     kind="launch") for index in range(14)]
    assert sorted(card["card_id"][-5:] for card in auto_key_moments(spread)) == [
        f"q{index:04d}" for index in range(2, 14)]


def test_key_moments_trim_to_30_from_the_product_with_the_most_moments():
    def quarterly(name, day, first_year, first_month, count):
        cards = []
        for index in range(count):
            month = first_month + index * 3
            year, month = first_year + (month - 1) // 12, (month - 1) % 12 + 1
            cards.append(moment(name, f"{year}-{month:02d}-{day:02d}", f"{name[:2].lower()}{index:04d}",
                                kind="launch"))
        return cards

    cards = (quarterly("ChatGPT", 1, 2023, 1, 12) + quarterly("Claude Code", 2, 2023, 4, 12)
             + quarterly("Cursor", 3, 2024, 1, 8))
    selected = auto_key_moments(cards)

    assert KEY_MOMENTS_PER_PRODUCT == 12 and KEY_MOMENTS_TOTAL == 30
    counts = Counter(card["product_name"] for card in selected)
    # 32 moments: ChatGPT (holding the oldest, 2023-01-01) is trimmed first, then Claude Code.
    assert counts == {"ChatGPT": 11, "Claude Code": 11, "Cursor": 8}
    dropped = {card["date"] for card in cards} - {card["date"] for card in selected}
    assert dropped == {"2023-01-01", "2023-04-02"}


def test_editorial_key_moments_take_precedence_and_unknown_ids_fall_back():
    cards = [moment("Cursor", "2025-05-15", "c00001"), moment("Cursor", "2026-10-06", "c00002", kind="launch"),
             moment("ChatGPT", "2026-07-09", "a00001")]
    targets = {card["card_id"]: f"Changes/x/{card['card_id']}" for card in cards}

    _, curated = theme_regions(cards, card_targets=targets,
                               key_moments=["cursor-2025-05-15-c00001", "chatgpt-2026-07-09-a00001"])
    assert curated["moments"] == "\n".join([
        "| Quarter | ChatGPT | Cursor |",
        "| --- | --- | --- |",
        "| 2026 Q3 | 2026-07-09 [[Changes/x/chatgpt-2026-07-09-a00001\\|ChatGPT a00001]] | · |",
        "| 2025 Q2 | · | 2025-05-15 [[Changes/x/cursor-2025-05-15-c00001\\|Cursor c00001]] |",
    ])
    _, fallback = theme_regions(cards, card_targets=targets, key_moments=["cursor-2020-01-01-ffffff"])
    assert fallback["moments"].startswith(AUTO_MOMENTS_CAPTION)
    assert "cursor-2026-10-06-c00002" in fallback["moments"]


def test_editorial_key_moments_validation_reports_unknown_and_repeated_ids():
    from _scripts.editorial import KEY_MOMENT_DUPLICATE, KEY_MOMENT_UNKNOWN, key_moments
    cards = [moment("Cursor", "2025-05-15", "c00001"), moment("Cursor", "2025-06-04", "c00002"),
             moment("ChatGPT", "2026-01-01", "a00001", theme="memory")]
    editorial = {"key_moments": {
        "agent-mode": ["cursor-2025-06-04-c00002", "chatgpt-2026-01-01-a00001", "missing",
                       "cursor-2025-06-04-c00002"],
        "memory": ["cursor-2025-05-15-c00001"],
    }}

    curated, warnings = key_moments(editorial, cards)

    assert curated == {"agent-mode": ["cursor-2025-06-04-c00002"]}
    assert warnings == [
        {"theme": "agent-mode", "card_id": "chatgpt-2026-01-01-a00001", "reason": KEY_MOMENT_UNKNOWN},
        {"theme": "agent-mode", "card_id": "missing", "reason": KEY_MOMENT_UNKNOWN},
        {"theme": "agent-mode", "card_id": "cursor-2025-06-04-c00002", "reason": KEY_MOMENT_DUPLICATE},
        {"theme": "memory", "card_id": "cursor-2025-05-15-c00001", "reason": KEY_MOMENT_UNKNOWN},
    ]
    assert key_moments({}, cards) == ({}, [])
    assert key_moments({"key_moments": {"agent-mode": "cursor-2025-05-15-c00001"}}, cards)[0] == {}


def w1_theme_markdown(theme: str, card, notes: str = "") -> str:
    """A theme page as the W1 writer produced it (header region, Change Cards region)."""
    regions = {
        "header": "# Agent Mode",
        "timeline": "Scope: tracked-products-only.\n\n### 2025\n\n- 2025-02-01 · Cursor: [[x|Agent shell]]",
        "cards": "Active changes: 1. Use the dated links above to inspect each card.",
        "narrative": "Explore the dated evidence below.",
    }
    fields = {"tags": ["theme", "moc"], "title": "Agent Mode", "description": "Old description.",
              "status": "official", "publication": "active", "theme": theme,
              "products_involved": [card["product_name"]]}
    fields["machine_hash"] = machine_hash(fields, regions)
    body = (f"{machine_region('header', regions['header'])}\n\n"
            f"## Research summary\n{machine_region('narrative', regions['narrative'])}\n\n"
            f"## Cross-Product Timeline\n{machine_region('timeline', regions['timeline'])}\n\n"
            f"## Change Cards\n{machine_region('cards', regions['cards'])}\n" + notes)
    return render_frontmatter(fields, body)


def test_theme_skeleton_migrates_once_and_keeps_human_text(tmp_path: Path):
    card = change_card()
    rendered = render_theme_markdown("agent-mode", [card], theme_labels=THEME_LABELS, verbosity=VERBOSITY)
    target = tmp_path / "agent-mode.md"
    target.write_text(w1_theme_markdown("agent-mode", card), encoding="utf-8")
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, [], pending) is True
    assert pending == []
    assert frontmatter.load(target).content == frontmatter.loads(rendered).content
    migrated = target.read_bytes()
    write_markdown_file(target, rendered, [], pending)
    assert target.read_bytes() == migrated and pending == []

    # Notes after the regions survive later renders of the new skeleton.
    target.write_text(target.read_text(encoding="utf-8") + "\nCurator note on agent mode.\n",
                      encoding="utf-8")
    later = render_theme_markdown("agent-mode", [card, moment("Cursor", "2026-01-01", "c00009")],
                                  theme_labels=THEME_LABELS, verbosity=VERBOSITY)
    write_markdown_file(target, later, [], pending)
    text = target.read_text(encoding="utf-8")
    assert pending == [] and "Curator note on agent mode." in text and "2 tracked changes in Cursor" in text

    # A W1 page with human text keeps its structure and is reported for manual migration.
    legacy = tmp_path / "legacy.md"
    legacy.write_text(w1_theme_markdown("agent-mode", card, notes="\nKeep this note.\n"), encoding="utf-8")
    write_markdown_file(legacy, rendered, [], pending)
    post = frontmatter.load(legacy)
    assert pending == [{"file": str(legacy), "reason": MIGRATION_PENDING_REASON}]
    assert "Keep this note." in post.content
    assert extract_machine_regions(post.content)["timeline"] == extract_machine_regions(
        frontmatter.loads(rendered).content)["timeline"]


def archive_cards():
    cards = [
        moment("ChatGPT", "2026-10-07", "a00001", kind="launch", theme="model-support"),
        moment("Claude Code", "2026-10-14", "b00001", kind="digest", theme="uncategorized",
               title="5 other changes in v2.1.300"),
        moment("Claude Code", "2026-10-14", "b00002", kind="digest", title="3 Agent Mode changes in v2.1.300"),
        moment("Claude Code", "2026-10-02", "b00003"),
    ]
    return cards, {card["card_id"]: f"Changes/x/{card['card_id']}" for card in cards}


def test_archive_month_page_lists_cards_per_product_newest_first():
    cards, targets = archive_cards()
    post = frontmatter.loads(render_archive_month_markdown(
        "2026-10", cards, targets, OTHER_LABELS, previous="2026-09"))
    regions = extract_machine_regions(post.content)

    assert post["title"] == "October 2026" and post["tags"] == ["archive"]
    assert post["publication"] == "active"
    assert (post["date"], post["created"], post["modified"]) == ("2026-10-14", "2026-10-02", "2026-10-14")
    assert post["description"] == (
        "4 tracked changes announced in October 2026: ChatGPT 1 and Claude Code 3.")
    assert regions["header"] == (
        "# October 2026\n\n4 tracked changes · ChatGPT 1 · Claude Code 3\n\n"
        "← [[Archive/2026-09|September 2026]] · [[Archive/index|All months]]")
    # On one date the "Other changes" card follows the themed ones.
    assert regions["changes"] == "\n".join([
        "### ChatGPT",
        "",
        "- 2026-10-07 · Model Support · [[Changes/x/chatgpt-2026-10-07-a00001|ChatGPT a00001]] · Launch",
        "",
        "### Claude Code",
        "",
        "- 2026-10-14 · Agent Mode · [[Changes/x/claude-code-2026-10-14-b00002|3 Agent Mode changes in v2.1.300]] · Digest",
        "- 2026-10-14 · Other changes · [[Changes/x/claude-code-2026-10-14-b00001|5 other changes in v2.1.300]] · Digest",
        "- 2026-10-02 · Agent Mode · [[Changes/x/claude-code-2026-10-02-b00003|Claude Code b00003]]",
    ])


def test_archive_root_page_lists_months_newest_first_with_product_counts():
    cards, _ = archive_cards()
    cards += [moment("Cursor", "2026-09-30", "c00001"), moment("Cursor", "2025-12-01", "c00002"),
              moment("ChatGPT", "2025-12-24", "a00002")]
    post = frontmatter.loads(render_archive_markdown(cards))
    regions = extract_machine_regions(post.content)

    assert post["title"] == "Archive" and post["tags"] == ["archive"] and post["date"] == "2026-10-14"
    # The folder page prints the title: no H1 in the page.
    assert regions["header"] == (
        "Tracked changes by month of announcement, newest first: 7 tracked changes "
        "in 3 months, December 2025 → October 2026.")
    assert regions["months"] == "\n".join([
        "### 2026",
        "",
        "- [[Archive/2026-10|October 2026]] · 4 changes (ChatGPT 1 · Claude Code 3)",
        "- [[Archive/2026-09|September 2026]] · 1 change (Cursor 1)",
        "",
        "### 2025",
        "",
        "- [[Archive/2025-12|December 2025]] · 2 changes (ChatGPT 1 · Cursor 1)",
    ])
    empty = extract_machine_regions(frontmatter.loads(render_archive_markdown([])).content)
    assert empty == {"header": "No changes archived yet.", "months": "No months archived yet."}


def test_write_run_regenerates_archive_and_removes_months_without_cards(tmp_path: Path):
    february = change_card()
    march = {**change_card(), "card_id": "cursor-2025-03-01-cccccc", "date": "2025-03-01",
             "source_release": "cursor-2025-03-01-v2", "title": "Agent tabs", "slug": "agent-tabs"}
    releases = [release_record(), release_record(release_id="cursor-2025-03-01-v2", date="2025-03-01")]
    write_run_inputs(tmp_path, "first", [february, march], releases)
    assert write_run("first", root=tmp_path) == []
    archive = tmp_path / "Archive"
    assert sorted(path.name for path in archive.glob("*.md")) == ["2025-02.md", "2025-03.md", "index.md"]
    assert "[[Archive/2025-03|March 2025]] →" in (archive / "2025-02.md").read_text(encoding="utf-8")
    assert "[[Archive/2025-03|March 2025]] · 1 change (Cursor 1)" in (archive / "index.md").read_text(
        encoding="utf-8")
    # A human page in Archive/ and an emptied month with human notes are kept.
    (archive / "reading-list.md").write_text("# Reading list\n", encoding="utf-8")
    noted = archive / "2024-12.md"
    noted.write_text(render_archive_month_markdown(
        "2024-12", [{**february, "date": "2024-12-01"}]) + "\nKeep this month.\n", encoding="utf-8")

    # The March card is retired (reconcile): its month page goes.
    write_run_inputs(tmp_path, "second", [february], releases)
    assert write_run("second", root=tmp_path, reconcile=True) == []

    assert sorted(path.name for path in archive.glob("*.md")) == [
        "2024-12.md", "2025-02.md", "index.md", "reading-list.md"]
    assert "March 2025" not in (archive / "2025-02.md").read_text(encoding="utf-8")
    assert "[[Archive/2025-03" not in (archive / "index.md").read_text(encoding="utf-8")
    from _scripts.common import read_json
    from _scripts.writer import ARCHIVE_KEPT_REASON
    assert read_json(PipelinePaths("second", tmp_path).run_dir / "writer-migration-pending.json") == [
        {"file": "Archive/2024-12.md", "reason": ARCHIVE_KEPT_REASON}]
    # Rendering again changes nothing.
    snapshot = {path: path.read_bytes() for path in archive.glob("*.md")}
    write_run_inputs(tmp_path, "third", [february], releases)
    assert write_run("third", root=tmp_path) == []
    assert {path: path.read_bytes() for path in archive.glob("*.md")} == snapshot


CADENCE = {
    "as_of": "2026-10-14", "last_release_date": "2026-10-13", "days_since_last_release": 1,
    "releases_90d": 74, "baseline_monthly_releases": 18.46, "status": "normal",
    "monthly_counts": [{"month": f"2025-{month:02d}", "count": count, "archived": True}
                       for month, count in ((11, 12), (12, 0))]
    + [{"month": f"2026-{month:02d}", "count": count}
       for month, count in zip(range(1, 11), (16, 24, 1, 20, 19, 18, 22, 25, 26, 9))],
}


def test_cadence_panel_shows_gap_window_status_and_monthly_bars():
    text = render_cadence(CADENCE)
    lines = text.split("\n")

    assert lines[0] == ("Last release 2026-10-13 (1 day before the archive date) · 74 releases in the "
                        "last 90 days · cadence: normal")
    assert lines[2] == "Monthly releases, last 12 months (baseline 18.5 per month):"
    assert lines[4:7] == ["- 2025-11 ▇▇▇▇▇▇▇▇▇ 12", "- 2025-12 · 0", "- 2026-01 ▇▇▇▇▇▇▇▇▇▇▇▇ 16"]
    assert lines[7] == "- 2026-02 " + "▇" * 18 + " 24"
    assert lines[8] == "- 2026-03 ▇ 1"  # at least one bar for a month with releases
    assert lines[13] == "- 2026-08 " + "▇" * 19 + " 25"
    assert lines[14] == "- 2026-09 " + "▇" * 20 + " 26"  # the busiest month fills the bar
    assert len(lines) == 16
    same_day = render_cadence({**CADENCE, "days_since_last_release": 0, "status": "not-tracked"})
    assert same_day.startswith("Last release 2026-10-13 (the archive date) · ")
    assert "cadence: not tracked" in same_day
    # Months before the first archived release are a coverage gap, not silence.
    gap = {**CADENCE, "monthly_counts": [{"month": "2025-10", "count": 0, "archived": False},
                                         *CADENCE["monthly_counts"][1:]]}
    assert render_cadence(gap).split("\n")[4] == "- 2025-10 · not archived"
    assert render_cadence(None) == "Release cadence has not been measured yet."
    assert render_cadence({**CADENCE, "last_release_date": None}) == "No releases archived yet."


def existing_product_markdown(notes: str = "") -> str:
    """A product page in the pre-W2 layout the live pages have (P7 cadence inserted
    after the narrative, empty Editor Notes)."""
    regions = {"narrative": "Phase narrative.", "cadence": "Old cadence.", "coverage": "3 releases.",
               "summary": "Cursor: 3.", "eras": "No eras.", "releases": "- r", "changes": "- c"}
    fields = {"tags": ["product"], "title": "Cursor", "product": "cursor", "product_name": "Cursor"}
    fields["machine_hash"] = machine_hash(fields, regions)
    body = ("# Cursor\n\n"
            f"## Research summary\n{machine_region('narrative', regions['narrative'])}\n\n"
            f"## Release cadence\n{machine_region('cadence', regions['cadence'])}\n\n"
            f"## Source coverage\n{machine_region('coverage', regions['coverage'])}\n\n"
            f"## Summary\n{machine_region('summary', regions['summary'])}\n\n"
            f"## Eras\n{machine_region('eras', regions['eras'])}\n\n"
            f"## Release Archive\n{machine_region('releases', regions['releases'])}\n\n"
            f"## Change Timeline\n{machine_region('changes', regions['changes'])}\n\n"
            "## Editor Notes\n" + (f"\n{notes}\n" if notes else ""))
    return render_frontmatter(fields, body)


PRODUCT_HEADINGS = ["## Release cadence", "## Eras", "## Themes", "## Recent releases", "## Coverage"]
PRODUCT_REGIONS = ["header", "cadence", "narrative", "eras", "themes", "recent", "coverage",
                   "releases", "changes"]


def product_inputs():
    """Cursor with 12 releases (one card each except the last), positioning and one era."""
    releases = [release_record(release_id=f"cursor-2026-{month:02d}-01-r", date=f"2026-{month:02d}-01",
                               title=f"Release {month}") for month in range(1, 13)]
    themes = ["agent-mode"] * 6 + ["model-support"] * 3 + ["context-window", "uncategorized"]
    cards = [{**change_card(), "card_id": f"cursor-2026-{index + 1:02d}-01-c{index:05d}",
              "date": f"2026-{index + 1:02d}-01", "source_release": f"cursor-2026-{index + 1:02d}-01-r",
              "theme": theme, "title": f"Change {index}", "slug": f"change-{index}"}
             for index, theme in enumerate(themes)]
    info = {"product_name": "Cursor", "verbosity_baseline": 1.0, "top_themes": [],
            "positioning": "AI code editor; tracked from the official Cursor changelog.",
            "narrative_summary": "Cursor moves from chat to agents.",
            "narrative_limitations": "Dates are changelog dates.",
            "eras": [{"name": "Agents", "from": "2026-01-01", "to": None, "summary": "Agents arrive.",
                      "evidence": [{"release_id": r["release_id"], "title": r["title"], "date": r["date"],
                                    "url": r["source_url"]} for r in releases[:4]]}]}
    release_targets = {r["release_id"]: f"Releases/Cursor/{r['release_id']}" for r in releases}
    return info, cards, releases, release_targets


def test_product_page_renders_the_p6_skeleton():
    info, cards, releases, targets = product_inputs()
    page = frontmatter.loads(render_product_markdown(
        "cursor", info, cards, releases=releases, release_targets=targets,
        theme_labels={**HOME_LABELS, "uncategorized": "Other changes"}, cadence=CADENCE))
    assert page["description"] == "AI code editor; tracked from the official Cursor changelog."
    assert page["product"] == "cursor" and page["tags"] == ["product"]
    assert [line for line in page.content.splitlines() if line.startswith("## ")] == PRODUCT_HEADINGS
    regions = extract_machine_regions(page.content)
    assert list(regions) == PRODUCT_REGIONS
    assert regions["header"] == (
        "# Cursor\n\nAI code editor; tracked from the official Cursor changelog. · 12 releases · "
        "2026-01-01 → 2026-12-01 · [[About|coverage details]]")
    assert regions["narrative"] == "Cursor moves from chat to agents."
    eras = regions["eras"].split("\n")
    assert eras[0] == "### Agents (2026-01-01 → present)"
    assert eras[2:5] == ["Agents arrive.", "", "Representative releases:"]
    assert eras[6:9] == [f"- 2026-0{m}-01: [Release {m}](https://cursor.com/changelog/projects) · "
                         f"[[Releases/Cursor/cursor-2026-0{m}-01-r|Archived release]]" for m in (1, 2, 3)]
    assert "Release 4" not in regions["eras"]  # at most three representative releases
    assert eras[-1] == "**Scope:** Dates are changelog dates."


def test_product_themes_bars_scale_to_the_top_theme_and_list_other_changes_last():
    info, cards, releases, targets = product_inputs()
    many = cards + [{**cards[0], "card_id": f"cursor-2026-01-01-x{n:05d}", "theme": f"theme-{n:02d}"}
                    for n in range(9)]
    themes = extract_machine_regions(frontmatter.loads(render_product_markdown(
        "cursor", info, many, releases=releases, release_targets=targets,
        theme_labels={"agent-mode": "Agent Mode", "uncategorized": "Other changes"})).content)["themes"]
    lines = themes.split("\n")
    assert lines[0] == "- [[Themes/agent-mode|Agent Mode]] · 6 cards · " + "█" * 12
    assert lines[1] == "- [[Themes/model-support|Model Support]] · 3 cards · " + "█" * 6
    assert lines[2] == "- [[Themes/context-window|Context Window]] · 1 card · " + "██"
    assert len(lines) == 9  # top eight themes, then Other changes
    assert lines[-1] == "- Other changes · 1 card"
    assert "Themes/uncategorized" not in themes


def test_product_recent_releases_are_the_last_ten_newest_first_with_card_counts():
    info, cards, releases, targets = product_inputs()
    recent = extract_machine_regions(frontmatter.loads(render_product_markdown(
        "cursor", info, cards, releases=releases, release_targets=targets)).content)["recent"]
    lines = recent.split("\n")
    assert len(lines) == 10
    assert lines[0] == "- 2026-12-01 · [[Releases/Cursor/cursor-2026-12-01-r|Release 12]] · 0 cards"
    assert lines[1] == "- 2026-11-01 · [[Releases/Cursor/cursor-2026-11-01-r|Release 11]] · 1 card"
    assert lines[-1].startswith("- 2026-03-01 · ")


def test_product_archive_and_changes_are_collapsed_callouts_with_every_line_prefixed():
    info, cards, releases, targets = product_inputs()
    regions = extract_machine_regions(frontmatter.loads(render_product_markdown(
        "cursor", info, cards + [{**cards[0], "card_id": "cursor-2025-12-01-old000", "date": "2025-12-01"}],
        {cards[0]["card_id"]: "Changes/Cursor/x"}, releases=releases, release_targets=targets)).content)
    archive = regions["releases"].split("\n")
    assert archive[0] == "> [!info]- Release archive (12 releases)"
    assert archive[1] == "> - 2026-12-01: [[Releases/Cursor/cursor-2026-12-01-r|Release 12]]"
    assert len(archive) == 13
    changes = regions["changes"].split("\n")
    assert changes[0] == "> [!info]- All tracked changes (12 cards)"
    assert changes[1:3] == ["> **2026** · 11 cards", ">"]
    assert changes[3] == "> - 2026-11-01 · Uncategorized: [[2026-11-01-change-10|Change 10]]"
    assert "> **2025** · 1 card" in changes
    assert "> - 2026-01-01 · Agent Mode: [[Changes/Cursor/x|Change 0]]" in changes
    for region in (archive, changes):
        assert all(line == ">" or line.startswith("> ") for line in region)


def test_legacy_product_page_migrates_to_the_new_skeleton_idempotently(tmp_path: Path):
    target = tmp_path / "Cursor.md"
    target.write_text(existing_product_markdown(), encoding="utf-8")
    assert legacy_residue(frontmatter.load(target).content, "product") == ""
    info, cards, releases, targets = product_inputs()
    rendered = render_product_markdown("cursor", info, cards, releases=releases,
                                       release_targets=targets, cadence=CADENCE)
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, conflicts, pending) is True

    page = frontmatter.load(target)
    assert page.content == frontmatter.loads(rendered).content
    assert [line for line in page.content.splitlines() if line.startswith("## ")] == PRODUCT_HEADINGS
    assert page["description"] == info["positioning"]
    assert conflicts == [] and pending == []
    once = target.read_bytes()
    write_markdown_file(target, rendered, conflicts, pending)
    assert target.read_bytes() == once and pending == []


def test_legacy_product_page_with_human_text_is_kept_and_reported(tmp_path: Path):
    target = tmp_path / "Cursor.md"
    target.write_text(existing_product_markdown("Human product notes."), encoding="utf-8")
    info, cards, releases, targets = product_inputs()
    rendered = render_product_markdown("cursor", info, cards, releases=releases,
                                       release_targets=targets, cadence=CADENCE)
    conflicts: list[dict[str, str]] = []
    pending: list[dict[str, str]] = []

    assert write_markdown_file(target, rendered, conflicts, pending) is True

    content = frontmatter.load(target).content
    assert content.rstrip().endswith("## Editor Notes\n\nHuman product notes.")
    assert "## Summary" in content and "## Themes" not in content  # structure kept
    regions = extract_machine_regions(content)
    assert regions["cadence"].startswith("Last release 2026-10-13")  # present regions refreshed
    assert regions["releases"].startswith("> [!info]- Release archive (12 releases)")
    assert conflicts == [] and pending == [{"file": str(target), "reason": MIGRATION_PENDING_REASON}]
    once = target.read_bytes()
    write_markdown_file(target, rendered, conflicts, [])
    assert target.read_bytes() == once


def test_home_links_the_archive_and_shows_cadence_per_product():
    cadence = {"chatgpt": {"status": "quiet"}, "claude-code": {"status": "normal"},
               "cursor": {"status": "not-tracked"}}
    regions = extract_machine_regions(frontmatter.loads(render_home({"alerts": [], "cadence": cadence})).content)

    assert regions["recent"].endswith("\n\nAll months: [[Archive/index|Archive]]")
    assert regions["products"].splitlines() == [
        "- [[Products/ChatGPT|ChatGPT]] · 3 releases · 2025-01-01 → 2026-10-01 · "
        "2 releases in the last 90 days · cadence: quiet",
        "- [[Products/Claude Code|Claude Code]] · 1 release · 2026-10-14 → 2026-10-14 · "
        "1 release in the last 90 days · cadence: normal",
        "- [[Products/Cursor|Cursor]] · 2 releases · 2026-08-01 → 2026-10-13 · "
        "2 releases in the last 90 days · cadence: not tracked",
    ]
    empty = render_index_markdown([], {"products": {}}, {"themes": {}}, {"alerts": []})
    assert extract_machine_regions(frontmatter.loads(empty).content)["recent"] == (
        "No changes archived yet.\n\nAll months: [[Archive/index|Archive]]")


def test_about_says_cadence_is_measured_to_the_archive_date():
    about = extract_machine_regions(frontmatter.loads(render_about()).content)
    assert "- Cadence is measured to the newest archived release date, not the clock." in about["method"]
    assert "- **Cadence**: " in about["glossary"] and "- **Key moments**: " in about["glossary"]
