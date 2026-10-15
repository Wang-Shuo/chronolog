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
    assert "**Other** · [[Themes/mobile-desktop|Mobile and Desktop]] (1)" in index
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
        "Acquisition times, sampling rules, review status and glossary: [[About|About the data]].",
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
    assert "At most five cards are kept per release" in regions["method"]
    assert "Tracked N of M candidate lines" in regions["method"]
    assert regions["status"].startswith(
        "3 products · 6 archived releases · 15 tracked changes · 5 themes. "
        "Pending theme review: 1,234. Silence alerts: 0.")
    for term in ("Change Card", "Release", "Theme", "Era", "Tracked products only", "Candidate line"):
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
        "Acquisition details, sampling rules and known gaps: [[About]].")
