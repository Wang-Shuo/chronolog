import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

import pytest

from _scripts.common import PipelinePaths, card_id_for, read_json, slugify, write_json
from _scripts.extract import (
    card_title,
    extract_cards_from_release,
    extract_run,
    load_review_decisions,
    load_theme_vocabulary,
    rank_theme_matches,
)
from _scripts.validate import validate_card


def release_with_body(body: str) -> dict[str, str]:
    return {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-05-01",
        "version": "v1.2",
        "title": "Extractor fixture",
        "body": body,
        "source_url": "https://example.com",
    }


def test_extractor_normalizes_theme_alias_and_stable_card_id():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-03-15",
        "version": "v1.0",
        "title": "Agent and context update",
        "body": "- Agent can run shell commands\n- Context window expanded to 200K tokens",
        "source_url": "https://example.com",
    }

    cards = extract_cards_from_release(release, themes)

    assert {card["theme"] for card in cards} >= {"agent-mode", "context-window"}
    assert cards[0]["card_id"] == extract_cards_from_release(release, themes)[0]["card_id"]
    assert cards[0]["evidence"][0]["quote"]


def test_extractor_marks_candidate_theme_when_no_alias_matches():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = {
        "product": "cursor",
        "product_name": "Cursor",
        "date": "2026-04-01",
        "version": "v1.1",
        "title": "Novel renderer",
        "body": "- New quasar renderer for reviewing geometric palettes",
        "source_url": "https://example.com",
    }

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "__candidate__"
    assert cards[0]["theme_suggestion"] == "quasar-renderer"


def test_extractor_does_not_match_theme_or_impact_inside_words():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body("- Stable planning remodel renewed workflow cleanup")

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "__candidate__"
    assert cards[0]["theme_suggestion"] == "stable-planning-remodel"
    assert cards[0]["impact"] == "incremental"
    assert "ai_generated" not in cards[0]
    assert "confidence" not in cards[0]


def test_extractor_matches_hyphenated_alias_written_with_space():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body("- Usage based metering controls are available")

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "pricing-model"


def test_extractor_skips_markdown_headings_and_strips_numbered_bullets():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "# Release Notes\n"
        "## Breaking Changes\n"
        "1. Added model support for Claude\n"
    )

    cards = extract_cards_from_release(release, themes)

    assert [card["title"] for card in cards] == ["Added model support for Claude"]
    assert cards[0]["theme"] == "model-support"


def test_extractor_dedupes_repeated_evidence_but_keeps_multiple_cards_per_theme():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "\n".join(
            [
                "- Agent can run task one",
                "- Agent can run task one!",
                "- Agent can run task two",
                "- Agent can run task three",
                "- Context window expanded to 200K tokens",
                "- Pricing now uses a metered plan",
            ]
        )
    )

    cards = extract_cards_from_release(release, themes)

    assert [card["theme"] for card in cards] == [
        "agent-mode",
        "agent-mode",
        "agent-mode",
        "context-window",
        "pricing-model",
    ]
    assert len({card["card_id"] for card in cards}) == 5


def test_theme_ranking_prefers_canonical_match_over_generic_alias():
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    matches = rank_theme_matches(
        "Collaboration workflow lets reviewers approve agent actions",
        themes,
    )
    cards = extract_cards_from_release(
        release_with_body("- Collaboration workflow lets reviewers approve agent actions"),
        themes,
    )

    assert matches[0]["theme"] == "collaboration"
    assert matches[1]["theme"] == "agent-mode"
    assert cards[0]["theme"] == "collaboration"
    assert cards[0]["theme_matches"][0]["matched_terms"] == ["collaboration"]


def test_extractor_resolves_known_ambiguous_theme_with_semantic_rule():
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    cards = extract_cards_from_release(
        release_with_body("- Agent team controls improve review permissions"),
        themes,
    )

    assert cards[0]["theme"] == "collaboration"
    assert cards[0]["theme_resolution"] == "manual-semantic-rule-v1"
    assert [match["theme"] for match in cards[0]["theme_matches"][:2]] == [
        "agent-mode",
        "collaboration",
    ]


def test_extractor_skips_generic_headings_instructions_and_unclassified_bugfixes():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "# New Features\n"
        "- Learn more in our documentation\n"
        "- Fixed a crash when opening an empty panel\n"
        "- Terminal now supports code review workflows\n"
    )

    cards = extract_cards_from_release(release, themes)

    assert [card["theme"] for card in cards] == ["developer-workflow"]


def test_extractor_applies_explicit_semantic_review_dispositions():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = {
        **release_with_body("- Novel reviewed capability\n- Low-signal maintenance detail"),
        "release_id": "cursor-2026-05-01-reviewed-fixture-a1b2c3d4",
        "source_type": "cursor_changelog",
    }
    unreviewed = extract_cards_from_release(release, themes)
    decisions = {
        unreviewed[0]["card_id"]: "projects-workspaces",
        unreviewed[1]["card_id"]: "skip",
    }

    cards = extract_cards_from_release(release, themes, decisions)

    assert len(cards) == 1
    assert cards[0]["theme"] == "projects-workspaces"
    assert cards[0]["theme_resolution"] == "manual-backfill-review-v1"


def test_extractor_distinguishes_resource_memory_from_product_memory():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    cards = extract_cards_from_release(
        release_with_body("- Reduced memory usage in long-running sessions"),
        themes,
    )

    assert cards[0]["theme"] == "reliability-performance"
    assert cards[0]["theme_resolution"] == "manual-semantic-rule-v2"


def test_extractor_does_not_leave_whitespace_when_truncating_titles():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    line = "Agent workflow " + ("x" * 64) + " remainder " + ("y" * 20)

    cards = extract_cards_from_release(release_with_body(f"- {line}"), themes)
    title = cards[0]["title"]

    assert len(title) <= 90
    assert title == title.strip()
    assert title.endswith("…")
    head = title[:-1]
    assert head == head.rstrip()
    assert line.startswith(head)
    assert line[len(head)] == " "  # cut on a word boundary, never mid-word
    assert title == "Agent workflow " + "x" * 64 + "…"  # "remainder" would cross 84


TITLE_CASES = [
    # Reviewed examples from the W1 title plan.
    (
        "Claude Code",
        "Added a `dir` prop on a mod's `Text` for right-to-left text: on Windows and in VS "
        "Code's terminal its rows read in that direction and sit flush right",
        "Added a `dir` prop on a mod's `Text` for right-to-left text",
    ),
    (
        "Cursor",
        "A Project runs on its own computer in the cloud, so closing your laptop doesn't stop "
        "it. When something needs testing on your machine, the coordinator spins up a local "
        "agent to run it there.",
        "A Project runs on its own computer in the cloud, so closing your laptop doesn't stop it",
    ),
    (
        "ChatGPT",
        "Among Pro plans, Ultrafast is available only with Pro 500. Buying credits on Pro 100 "
        "or Pro 200 does not unlock it.",
        "Among Pro plans, Ultrafast is available only with Pro 500",
    ),
    (
        "Cursor",
        "Today we're launching Projects in Cursor. Projects lets you take on larger bodies of "
        "work, such as a feature, a migration, or a full app.",
        "Cursor launches Projects",
    ),
    (
        "ChatGPT",
        "We’re excited to announce that ChatGPT Go, our low cost subscription plan, is now "
        "available in Brazil, Mexico and Chile for local pricing.",
        "ChatGPT Go, our low cost subscription plan, is now available in Brazil, Mexico…",
    ),
    (
        "Claude Code",
        "You can now see a breakdown of your agent's context usage.",
        "See a breakdown of your agent's context usage",
    ),
    (
        "Cursor",
        "Fast (default): $3.00/M input, $15.00/M output tokens",
        "Fast (default): $3.00/M input, $15.00/M output tokens",
    ),
    (
        "Cursor",
        "Welcome to the first nightly release! It comes with agents, which we aren't "
        "releasing yet.",
        "Welcome to the first nightly release!",
    ),
    (
        "Claude Code",
        "claude agents rows now show done/total before the detail when work is fanned out "
        "across many sessions",
        "claude agents rows now show done/total before the detail when work is fanned out…",
    ),
    (
        "Claude Code",
        "Improved send now (ctrl+enter) in a subagent's view: it now moves the subagent's run "
        "to the foreground",
        "Improved send now (ctrl+enter) in a subagent's view",
    ),
    (
        "Claude Code",
        "Fixed /remote-control sessions showing the wrong permission mode in the mobile app, "
        "e.g. when reattaching after a restart of the daemon process",
        "Fixed /remote-control sessions showing the wrong permission mode in the mobile app…",
    ),
    (
        "ChatGPT",
        "Pro ($100/month): Built for longer, high-intensity Codex sessions. It includes "
        "unlimited usage.",
        "Pro ($100/month): Built for longer, high-intensity Codex sessions",
    ),
    (
        "Claude Code",
        "Added `$.ui.view({ agentId })` for mods: shows an agent's transcript in the main view "
        "when you ask, and `$.ui.view({})` goes back",
        "Added `$.ui.view({ agentId })` for mods",
    ),
    (
        "ChatGPT",
        "We’re introducing dots: always-on agents in ChatGPT that can take on ongoing work for "
        "you across your apps.",
        "ChatGPT introduces dots",
    ),
    (
        "Cursor",
        "This release introduces builds: ready-to-use copies of your development environment "
        "that agents start from.",
        "Cursor introduces builds",
    ),
    (
        "Cursor",
        "Standard: $0.50/M input, $2.50/M output tokens",
        "Standard: $0.50/M input, $2.50/M output tokens",
    ),
    # Terminal punctuation: one trailing "." is stripped, "?" and "!" are kept.
    ("Cursor", "Agent can now run tests in the background.", "Agent can now run tests in the background"),
    ("ChatGPT", "Want faster answers? Try the new model in the picker.", "Want faster answers?"),
    # Abbreviations, versions and domains are not sentence ends.
    (
        "Claude Code",
        "Added support for pasting images, e.g. PNG and JPEG screenshots",
        "Added support for pasting images, e.g. PNG and JPEG screenshots",
    ),
    (
        "Claude Code",
        "Compare responses side by side, i.e. Opus vs. Sonnet. Results are saved per session.",
        "Compare responses side by side, i.e. Opus vs. Sonnet",
    ),
    (
        "Claude Code",
        "Updated the bundled ripgrep to v14.1.1. Search is now faster on large repos",
        "Updated the bundled ripgrep to v14.1.1",
    ),
    (
        "Cursor",
        "Cursor's long-running agent is now available at cursor.com/agents for Ultra plans",
        "Cursor's long-running agent is now available at cursor.com/agents for Ultra plans",
    ),
    # Truncation never splits a code span and never ends on a dangling token.
    (
        "Claude Code",
        "Added `claude doctor --verbose` output and `claude mcp list --include-disabled-servers` "
        "for debugging broken MCP setups",
        "Added `claude doctor --verbose` output…",
    ),
    (
        "Claude Code",
        "Added the turn's completion time to the end-of-turn duration line, e.g. "
        "`✻ Sautéed for 23s · done 6:05 PM`",
        "Added the turn's completion time to the end-of-turn duration line…",
    ),
    (
        "Cursor",
        "Agents " + "coordinate " * 15 + "work",
        "Agents coordinate coordinate coordinate coordinate coordinate coordinate coordinate…",
    ),
    # Vendor voice with straight and curly apostrophes.
    ("Cursor", "We’re rolling out Bugbot to all teams.", "Cursor rolls out Bugbot to all teams"),
    ("Cursor", "We've improved codebase context!", "Cursor improves codebase context!"),
    ("Cursor", "We’ve also added a file picker to Composer.", "Cursor adds a file picker to Composer"),
    ("ChatGPT", "Today, we’re introducing GPT-6 Astra.", "ChatGPT introduces GPT-6 Astra"),
    (
        "Cursor",
        "We're thrilled to introduce Composer, our new agent model.",
        "Cursor introduces Composer, our new agent model",
    ),
    (
        "ChatGPT",
        "Good news! We’re expanding availability of the ChatGPT app for iOS to more countries.",
        "ChatGPT expands availability of the ChatGPT app for iOS to more countries",
    ),
    (
        "Cursor",
        "This release brings Bugbot for code review, a first look at memories, one-click MCP "
        "setup, Jupyter support, and more.",
        "Cursor brings Bugbot for code review, a first look at memories, one-click MCP setup…",
    ),
    # Openings without an explicit rule keep the vendor's wording.
    (
        "ChatGPT",
        "We’re retiring the Voice experience in the ChatGPT macOS app on January 15, 2026.",
        "We’re retiring the Voice experience in the ChatGPT macOS app on January 15, 2026",
    ),
    (
        "Cursor",
        "We've shipped a batch of new functionality across the TypeScript and Python SDKs.",
        "We've shipped a batch of new functionality across the TypeScript and Python SDKs",
    ),
    (
        "Cursor",
        "We’ve heard your feedback and are rolling out a unified pricing model.",
        "We’ve heard your feedback and are rolling out a unified pricing model",
    ),
    (
        "ChatGPT",
        "Today we started rolling out two updates to voice mode in ChatGPT:",
        "Today we started rolling out two updates to voice mode in ChatGPT",
    ),
    # A coordinated gerund blocks the rewrite ("introduces ... and updating").
    (
        "ChatGPT",
        "We’re introducing a new $100/month Pro plan and updating how Codex usage works "
        "across Plus and Pro.",
        "We’re introducing a new $100/month Pro plan and updating how Codex usage works…",
    ),
    # A redundant " in {product}" is dropped once the product is the subject: at the end,
    # or before punctuation or a lowercase word, never before a name or a possessive.
    ("Cursor", "We're rolling out Bugbot in Cursor.", "Cursor rolls out Bugbot"),
    ("ChatGPT", "We’re launching group chats in ChatGPT!", "ChatGPT launches group chats!"),
    (
        "ChatGPT",
        "We’re rolling out a new speech-to-text model for dictation in ChatGPT across all "
        "plans. This is a behind-the-scenes update.",
        "ChatGPT rolls out a new speech-to-text model for dictation across all plans",
    ),
    (
        "Cursor",
        "We've added a toggle in Cursor Settings for agent sounds.",
        "Cursor adds a toggle in Cursor Settings for agent sounds",
    ),
    (
        "ChatGPT",
        "We’re rolling out a refreshed sidebar in ChatGPT’s desktop app.",
        "ChatGPT rolls out a refreshed sidebar in ChatGPT’s desktop app",
    ),
    ("Cursor", "Projects are now available in Cursor.", "Projects are now available in Cursor"),
    (
        "Cursor",
        "You can now share canvases in Cursor with your teammates.",
        "Share canvases in Cursor with your teammates",
    ),
    # Any terminator followed by a space and a non-lowercase character ends a sentence.
    (
        "Cursor",
        "Run Bugbot and Security Review with /review before pushing code. /review prompts "
        "you to choose which checks to run.",
        "Run Bugbot and Security Review with /review before pushing code",
    ),
    (
        "Cursor",
        "We've added a new feedback button at the top right of the app. - We really do",
        "Cursor adds a new feedback button at the top right of the app",
    ),
    (
        "Cursor",
        "Mention the agent in any thread. @Cursor replies with a plan before it starts.",
        "Mention the agent in any thread",
    ),
    # A first sentence under 20 characters is joined with the next when both fit.
    (
        "ChatGPT",
        "Faster sharing. Sharing chats is now easier and faster, with a quicker-loading share "
        "menu.",
        "Faster sharing. Sharing chats is now easier and faster, with a quicker-loading share menu",
    ),
    (
        "Cursor",
        "Bugfixes! Fixed the crash when opening large files.",
        "Bugfixes! Fixed the crash when opening large files",
    ),
    (
        "Cursor",
        'Bugfixes! Fixed the "ejected from slow mode" UI, added auto-switching logic for the '
        "model type when switching on API, improved the speed of the linter.",
        "Bugfixes!",
    ),
    # Colon heads need at least 3 tokens and 16 characters.
    (
        "Claude Code",
        "Added `/goal` command: set a completion condition and Claude keeps working across "
        "turns until it's met. Works in interactive, `-p`, and Remote Control",
        "Added `/goal` command",
    ),
    (
        "Claude Code",
        "Improved auto-updater: retries transient network failures, reports specific error "
        "categories and OS error codes on failure, and shows the current version",
        "Improved auto-updater: retries transient network failures, reports specific error…",
    ),
    # Truncation drops trailing stopwords and never leaves a bracket or quote open.
    (
        "Claude Code",
        "Improved startup time for sessions that load a large number of plugins from the "
        "marketplace and the local plugin cache directory",
        "Improved startup time for sessions that load a large number of plugins…",
    ),
    (
        "Claude Code",
        "Added projected context cost to the status line and `/context` (per-turn and "
        "per-invocation token estimates for each loaded skill)",
        "Added projected context cost to the status line and `/context`…",
    ),
    (
        "Claude Code",
        "Thinking spinner now shows progress inline (“still thinking”, “thinking more”, "
        "“almost done”) with elapsed time",
        "Thinking spinner now shows progress inline…",
    ),
    (
        "Claude Code",
        'Fixed plugin scripts failing with "Permission denied while reading the plugin cache '
        'directory on network mounted volumes" errors',
        "Fixed plugin scripts failing…",
    ),
    # Sentences the source ran together split at "lowercase/) . Uppercase".
    (
        "ChatGPT",
        "We’re excited to bring GPT-4, our latest model, to our ChatGPT Plus subscribers.GPT-4 "
        "has enhanced capabilities in:",
        "ChatGPT brings GPT-4, our latest model, to our ChatGPT Plus subscribers",
    ),
    (
        "ChatGPT",
        "Available on web, mobile (iOS & Android), and desktop (macOS & Windows).Note that "
        "some features roll out gradually.",
        "Available on web, mobile (iOS & Android), and desktop (macOS & Windows)",
    ),
    (
        "ChatGPT",
        "Personal Memory must be enabled to utilize this feature.Settings -> Personalization "
        "-> Memory",
        "Personal Memory must be enabled to utilize this feature",
    ),
    (
        "Claude Code",
        "Run `config.Load()` before start.Then the agent reads the merged settings",
        "Run `config.Load()` before start",
    ),
    # ...but not short identifiers, dotted chains, domains, versions or inline code.
    (
        "Claude Code",
        "Use os.Getenv to read variables in the sandbox",
        "Use os.Getenv to read variables in the sandbox",
    ),
    ("Claude Code", "Call fs.Stat before reading the file", "Call fs.Stat before reading the file"),
    ("Cursor", "apiKey: process.env.CURSOR_API_KEY!,", "apiKey: process.env.CURSOR_API_KEY!,"),
    (
        "Cursor",
        "Read the docs at cursor.com/docs.Then try it",
        "Read the docs at cursor.com/docs.Then try it",
    ),
    ("Claude Code", "Updated to v2.1.300.Next release soon", "Updated to v2.1.300.Next release soon"),
    (
        "Claude Code",
        "Added `foo.Bar` to the mod API so mods can read the active session",
        "Added `foo.Bar` to the mod API so mods can read the active session",
    ),
    # Zero-width characters hid an ordered-list marker from split_release_lines.
    (
        "ChatGPT",
        "2\u2060. Text selection improvements: you can now select text across horizontal "
        "rulers. 3\u2060. Performance improvements.",
        "Text selection improvements: you can now select text across horizontal rulers",
    ),
]


@pytest.mark.parametrize(("product_name", "line", "expected"), TITLE_CASES)
def test_card_title(product_name: str, line: str, expected: str):
    title = card_title(line, product_name)

    assert title == expected
    assert len(title) <= 90
    assert title == title.strip()
    assert title.count("`") % 2 == 0
    if title.endswith("…"):
        assert len(title) <= 85
        assert title.count("(") == title.count(")")
        assert title.count('"') % 2 == 0


@pytest.mark.parametrize("line", [
    "word " * 60,
    "Supercalifragilistic" * 10,
    "Added `" + "a" * 120 + "` flag",
    "We are introducing " + "x" * 200,
])
def test_card_title_hard_caps_pathological_lines(line: str):
    title = card_title(line, "Claude Code")

    assert 0 < len(title) <= 90
    assert title == title.strip()
    assert title.count("`") % 2 == 0


def test_card_title_does_not_change_card_identity():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    line = (
        "We're introducing agent checkpoints so you can rewind an agent run to any earlier "
        "step. This makes long tasks safer."
    )
    release = {**release_with_body(f"- {line}"), "release_id": "cursor-2026-05-01-v1-2",
               "source_type": "cursor_changelog"}

    card = extract_cards_from_release(release, themes)[0]

    assert card["title"] == (
        "Cursor introduces agent checkpoints so you can rewind an agent run to any earlier step"
    )
    assert card["slug"] == slugify(line)[:80].strip("-")
    assert card["card_id"] == card_id_for(
        "cursor", "2026-05-01", line, source_release="cursor-2026-05-01-v1-2"
    )
    assert card["evidence"][0]["quote"] == line
    assert card["extractor_version"] == "fallback-v4"
    assert validate_card(card, set(themes)) == []


def test_review_decisions_only_reference_official_themes(tmp_path: Path):
    review = tmp_path / "review.yaml"
    review.write_text("decisions:\n  card-1: not-a-theme\n", encoding="utf-8")
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    with pytest.raises(ValueError, match="unknown themes"):
        load_review_decisions(review, themes)


def test_extractor_adds_ai_fields_only_for_high_impact_cards():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    release = release_with_body(
        "- Stable workflow polishing for command history\n"
        "- Added new model support for Claude"
    )

    cards = extract_cards_from_release(release, themes)

    incremental_card = cards[0]
    significant_card = cards[1]
    assert incremental_card["impact"] == "incremental"
    assert "ai_generated" not in incremental_card
    assert "confidence" not in incremental_card
    assert significant_card["impact"] == "significant"
    assert significant_card["ai_generated"] is True
    assert significant_card["confidence"] == "low"


def test_extract_run_writes_extracted_change_cards():
    run_id = f"pytest-extract-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)

    try:
        write_json(
            paths.collected,
            {"releases": [release_with_body("- Agent can run shell commands")]},
        )

        cards = extract_run(run_id)

        output = read_json(paths.extracted)
        assert paths.extracted.exists()
        assert output == {"run_id": run_id, "change_cards": cards}
        assert output["change_cards"][0]["theme"] == "agent-mode"
        assert read_json(paths.theme_candidates) == {"run_id": run_id, "candidates": []}
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)


def test_extract_run_writes_candidate_review_queue():
    run_id = f"pytest-candidate-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)

    try:
        write_json(
            paths.collected,
            {"releases": [release_with_body("- New quasar renderer for geometric palettes")]},
        )

        cards = extract_run(run_id)
        candidates = read_json(paths.theme_candidates)["candidates"]

        assert cards[0]["theme"] == "__candidate__"
        assert candidates[0]["card_id"] == cards[0]["card_id"]
        assert candidates[0]["theme_review_reason"] == "no_match"
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)


def test_direct_cli_invocation_writes_extracted_change_cards():
    run_id = f"pytest-direct-extract-{uuid4().hex}"
    paths = PipelinePaths(run_id)
    shutil.rmtree(paths.run_dir, ignore_errors=True)

    try:
        write_json(
            paths.collected,
            {"releases": [release_with_body("- Context window expanded to 200K tokens")]},
        )

        result = subprocess.run(
            [sys.executable, "_scripts/extract.py", "--run-id", run_id],
            cwd=Path.cwd(),
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        output = read_json(paths.extracted)
        assert output["change_cards"][0]["theme"] == "context-window"
    finally:
        shutil.rmtree(paths.run_dir, ignore_errors=True)
