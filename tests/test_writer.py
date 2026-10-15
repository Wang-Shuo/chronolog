from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import frontmatter
import pytest

from _scripts.common import PipelinePaths, load_site, machine_hash, write_json
from _scripts.history import merge_history
from _scripts.writer import (
    MIGRATION_PENDING_REASON,
    change_card_paths,
    ensure_vault_dirs,
    extract_machine_regions,
    legacy_residue,
    machine_region,
    main,
    reconcile_missing_change_cards,
    relation_link,
    render_change_markdown,
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
        "Tracked 3 of 7 candidate lines.")
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
        "Agents now run in the cloud.\n\nTracked 0 changes.")
    assert "candidate_line_count" not in post["record"]
    for generic in ("What's changed", "#New Features", "Release notes", "v1.2"):
        summary = extract_machine_regions(frontmatter.loads(render_release_markdown(
            release_record(title="v1.2", source_summary=generic))).content)["summary"]
        assert summary == "No change cards extracted.\n\nTracked 0 changes."


def test_candidate_line_count_survives_history_reconstruction():
    collected = {**release_record(), "body": "- First candidate line here\n- Second candidate line here"}

    releases, _, _ = merge_history(([], [], []), [collected], [], [], set())
    assert releases == [{**release_record(), "candidate_line_count": 2}]

    # Incremental runs rebuild releases from the frontmatter record, without a body.
    record = frontmatter.loads(render_release_markdown({**collected, "cards": []}))["record"]
    assert record["candidate_line_count"] == 2
    summary = extract_machine_regions(frontmatter.loads(
        render_release_markdown({**record, "cards": []})).content)["summary"]
    assert summary.endswith("Tracked 0 of 2 candidate lines.")


def test_theme_display_names_label_theme_index_and_product_pages():
    card = {**change_card(), "theme": "mobile-desktop"}
    labels = {"mobile-desktop": "Mobile and Desktop", "agent-mode": "Agent Mode"}
    editorial = "**Research question: what changed on _desktop_?**\n\nSecond paragraph."

    theme = frontmatter.loads(render_theme_markdown("mobile-desktop", [card], editorial=editorial,
                                                    theme_labels=labels))
    assert theme["title"] == "Mobile and Desktop"
    assert extract_machine_regions(theme.content)["header"] == "# Mobile and Desktop"
    assert theme["description"] == "Research question: what changed on desktop?"
    plain = frontmatter.loads(render_theme_markdown("mobile-desktop", [card], theme_labels=labels))
    assert plain["description"] == "Cross-product timeline of Mobile and Desktop changes in Cursor."
    # Without a vocabulary entry the slug is title-cased.
    assert frontmatter.loads(render_theme_markdown("file-data", []))["title"] == "File Data"

    index = render_index_markdown([card], {"products": {}}, {"themes": {"agent-mode": {}, "mobile-desktop": {}}},
                                  {}, theme_labels=labels)
    assert "- [[Themes/mobile-desktop|Mobile and Desktop]]" in index
    assert "- [[Themes/agent-mode|Agent Mode]] — From assisted edits to delegated work" in index

    info = {"product_name": "Cursor", "verbosity_baseline": 1, "eras": [],
            "top_themes": ["mobile-desktop", "agent-mode"]}
    product = render_product_markdown("cursor", info, [card], {card["card_id"]: "Changes/Cursor/x"},
                                      theme_labels=labels)
    assert "Most represented themes: Mobile and Desktop, Agent Mode." in product
    assert "- 2025-02-01 · Mobile and Desktop: [[Changes/Cursor/x|Agent shell]]" in product


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
    assert extract_machine_regions(page.content)["summary"].endswith("Tracked 2 of 2 candidate lines.")
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
