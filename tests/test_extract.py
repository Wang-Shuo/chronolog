import shutil
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

import pytest

from _scripts.common import PipelinePaths, card_id_for, read_json, slugify, write_json
from _scripts.extract import (
    card_title,
    classify_theme,
    extract_cards_from_release,
    extract_run,
    load_review_decisions,
    load_theme_vocabulary,
    rank_theme_matches,
    semantic_preclassification_override,
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
        release_with_body("- Agent sharing controls improve review"),
        themes,
    )

    assert cards[0]["theme"] == "agent-mode"
    assert cards[0]["theme_resolution"] == "manual-semantic-rule-v1"
    assert [match["theme"] for match in cards[0]["theme_matches"][:2]] == [
        "agent-mode",
        "collaboration",
    ]


def test_plan_and_platform_names_only_decide_a_theme_when_nothing_else_matches():
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    def theme_of(text: str) -> str:
        return classify_theme(text, themes)["theme"]

    # "team" names a plan or an agent team, not collaboration; "iOS" and "Enterprise"
    # say where a change reaches. Each yields to what the line is about.
    assert theme_of("Agent team controls improve review permissions") == "agent-mode"
    assert theme_of("Voice conversations are now on iOS and Android") == "voice"
    assert theme_of("Custom instructions now hold more text for Enterprise users") == "memory"
    # With no other theme in the line, the platform or plan still decides.
    assert theme_of("ChatGPT for Android is now available") == "mobile-desktop"
    assert theme_of("Enterprise workspaces get a new dashboard") == "enterprise-admin"


def test_dollar_amounts_in_code_are_not_prices():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    shell = "Fixed false Bash permission prompts for `awk '{print $1}' file`"
    assert semantic_preclassification_override(shell, themes) == "safety-privacy"
    assert semantic_preclassification_override("Pro now costs $200/month", themes) == "pricing-model"
    assert semantic_preclassification_override("Standard: $0.50/M input tokens", themes) == "pricing-model"
    # Credits phrases still match through code spans such as a command name.
    assert semantic_preclassification_override(
        "Added `/usage-credits` so members see credits against their usage", themes) == "pricing-model"


def test_developer_tool_memory_means_ram_unless_it_names_product_memory():
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    def override(text: str, product: str) -> str | None:
        return semantic_preclassification_override(text, themes, product)

    ram = "Improved the embedded grep: pathological patterns fail fast instead of exhausting memory"
    assert override(ram, "claude-code") == "reliability-performance"
    assert override("Increased default memory for TypeScript language server.", "cursor") == (
        "reliability-performance")
    for product_memory in ("Added an ISO timestamp to memory file frontmatter",
                           "Project configs & auto memory now shared across git worktrees",
                           "Improved `/memory`: arrow keys flip settings such as Auto-memory",
                           "Agents have access to a memory tool that lets them learn from past runs"):
        assert override(product_memory, "claude-code") is None
    # ChatGPT's memory is the product feature.
    assert override("Memory now covers chats in projects for Plus users", "chatgpt") is None


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
    assert card["extractor_version"] == "fallback-v5"
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


# W2 card definition: cards follow the structure of the release body.

def structured_release(body: str, *, product="cursor", source_type="cursor_changelog",
                       title="Agent update", version="1.0"):
    names = {"cursor": "Cursor", "chatgpt": "ChatGPT", "claude-code": "Claude Code"}
    return {
        "product": product,
        "product_name": names[product],
        "release_id": f"{product}-2026-06-01-{slugify(title)}-0a1b2c3d",
        "source_type": source_type,
        "date": "2026-06-01",
        "version": version,
        "title": title,
        "body": body,
        "source_url": f"https://example.com/{product}/changelog",
    }


def w2_cards(body: str, **kwargs):
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    return extract_cards_from_release(structured_release(body, **kwargs), themes)


def quotes(card):
    return [item["quote"] for item in card["evidence"]]


@pytest.mark.parametrize(("body", "product", "source_type"), [
    ("#Background Agent\nAgent can now run tests in the background.\n"
     "Each agent works on its own branch and reports back when done.",
     "cursor", "cursor_changelog"),
    ("### Background Agent\nAgent can now run tests in the background.\n"
     "- Each agent works on its own branch and reports back when done.",
     "chatgpt", "chatgpt_changelog"),
])
def test_feature_section_becomes_one_card_titled_by_its_heading(body, product, source_type):
    cards = w2_cards(body, product=product, source_type=source_type)

    assert len(cards) == 1
    card = cards[0]
    assert card["title"] == "Background Agent"
    assert card["kind"] == "launch"
    assert card["theme"] == "agent-mode"
    assert quotes(card) == [
        "Agent can now run tests in the background.",
        "Each agent works on its own branch and reports back when done.",
    ]
    assert {item["source_release"] for item in card["evidence"]} == {
        f"https://example.com/{product}/changelog"}
    assert validate_card(card, set(load_theme_vocabulary("_scripts/themes.yaml"))) == []


def test_feature_section_without_text_quotes_its_heading():
    cards = w2_cards("Agent can now run shell commands in a sandbox.\n#Background Agent\n#Bug Fixes\n"
                     "- Terminal now supports code review workflows")

    feature = next(card for card in cards if card["title"] == "Background Agent")
    assert quotes(feature) == ["Background Agent"]


def test_scope_heading_bullets_become_cards_with_scope():
    body = ("### iOS\n- Agent can now run shell commands on your phone\n"
            "- Voice dictation stays available after you add attachments\n"
            "### Web, iOS, and Android\n- Memory now remembers your preferred units")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog",
                     title="ChatGPT app updates")

    assert [(card["scope"], card["theme"]) for card in cards] == [
        ("iOS", "agent-mode"), ("iOS", "voice"), ("Web, iOS, and Android", "memory")]
    assert all(len(card["evidence"]) == 1 for card in cards)


@pytest.mark.parametrize(("heading", "kind"), [
    ("Web", "scope"), ("iOS and Android", "scope"), ("Web, iOS, and Android", "scope"),
    ("macOS and Windows", "scope"), ("Plus", "scope"), ("Linux desktop", "scope"),
    ("What's changed", "generic"), ("Improvements", "generic"), ("Bug fixes:", "generic"),
    ("Patches", "generic"), ("Availability", "generic"), ("Other improvements", "generic"),
    ("Background Agent", "feature"), ("Docs", "feature"), ("Teams", "feature"),
])
def test_heading_kinds(heading, kind):
    from _scripts.extract import heading_kind
    assert heading_kind(heading) == kind


def test_preamble_paragraphs_with_one_theme_form_one_card():
    body = ("Agent mode can now plan larger tasks before editing.\n"
            "The agent shows each step and asks before running commands.\n"
            "Pricing now uses a metered plan for every team.")
    cards = w2_cards(body, title="v2.3")

    assert [(card["theme"], len(card["evidence"])) for card in cards] == [
        ("agent-mode", 2), ("pricing-model", 1)]
    assert cards[0]["title"] == "Agent mode can now plan larger tasks before editing"
    assert cards[0]["card_id"] == card_id_for(
        "cursor", "2026-06-01", "\n".join(quotes(cards[0])),
        source_release=structured_release(body, title="v2.3")["release_id"])


@pytest.mark.parametrize(("title", "expected"), [
    ("A new Pro plan with Astra Ultrafast", "A new Pro plan with Astra Ultrafast"),
    ("Introducing GPT-6 with Intelligent UI", "Introducing GPT-6 with Intelligent UI"),
    ("v2.1.300", "Agent mode can now plan larger tasks before editing"),
    ("Bug fixes", "Agent mode can now plan larger tasks before editing"),
])
def test_single_card_release_takes_an_informative_release_title(title, expected):
    body = ("Agent mode can now plan larger tasks before editing.\n"
            "The agent shows each step and asks before running commands.")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog", title=title)

    assert len(cards) == 1
    assert cards[0]["title"] == expected


def test_lead_in_list_stays_with_its_paragraph_unless_it_has_another_theme():
    body = ("Agent mode can now plan larger tasks. The agent can now:\n"
            "- Run several agent tasks at once\n"
            "- Ask before it overwrites quasar renderer settings\n"
            "- Use the new pricing plan for metered teams")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog", title="Agent update")

    assert [len(card["evidence"]) for card in cards] == [3, 1]
    assert cards[1]["theme"] == "pricing-model"


LIST_BODY = "\n".join([
    "## What's changed",
    "- Added agent checkpoints so an agent run can be rewound",
    "- Improved agent startup in large repositories",
    "- Changed the agent status line to show the active subagent",
    "- Added `/rewind` command to restore an earlier agent step",
    "- Auto mode is now on by default for every agent session",
    "- Improved model picker to group models by provider",
    "- Added new quasar renderer for geometric palettes",
    "- Fixed a crash when opening an empty panel",
    "- Improved context window usage report in long sessions",
    "- Improved compaction to keep the latest context window summary",
])


def test_list_mode_builds_digests_standalone_announcements_and_other_changes():
    cards = w2_cards(LIST_BODY, product="claude-code", source_type="github_releases",
                     title="v2.1.300", version="v2.1.300")
    by_kind = {}
    for card in cards:
        by_kind.setdefault(card["kind"], []).append(card)

    digests = {card["theme"]: card for card in by_kind["digest"]}
    assert digests["agent-mode"]["title"] == "3 Agent Mode changes in v2.1.300"
    assert quotes(digests["agent-mode"]) == [
        "Added agent checkpoints so an agent run can be rewound",
        "Improved agent startup in large repositories",
        "Changed the agent status line to show the active subagent",
    ]
    assert digests["context-window"]["title"].startswith("2 ")
    standalone = {card["title"] for card in cards if len(card["evidence"]) == 1}
    assert "Added `/rewind` command to restore an earlier agent step" in standalone
    assert "Auto mode is now on by default for every agent session" in standalone
    # A single line of a theme is an ordinary card, not a digest of one.
    model = next(card for card in cards if card["theme"] == "model-support")
    assert model["kind"] != "digest" and len(model["evidence"]) == 1
    # The one line without a theme is an ordinary card of the holding theme, not queued.
    assert not [card for card in cards if card["theme"] == "__candidate__"]
    other = [card for card in cards if card["theme"] == "uncategorized"]
    assert [(quotes(card), card["kind"]) for card in other] == [
        (["Added new quasar renderer for geometric palettes"], "change")]
    assert other[0]["title"] == "Added new quasar renderer for geometric palettes"
    assert not any("Fixed a crash" in quote for card in cards for quote in quotes(card))
    themes = set(load_theme_vocabulary("_scripts/themes.yaml"))
    assert all(validate_card(card, themes) == [] for card in cards)
    digest = digests["agent-mode"]
    assert digest["card_id"] == card_id_for(
        "claude-code", "2026-06-01", "\n".join(quotes(digest)), source_release=digest["source_release"])


@pytest.mark.parametrize("body", [
    "#New Features\n" + "\n".join(f"Agent can now run task number {n} in parallel" for n in range(40)),
    "\n".join(f"- Agent can now run task number {n} in parallel" for n in range(40)),
])
def test_no_cap_long_lists_keep_every_classified_line_in_digests(body):
    cards = w2_cards(body)

    assert len(cards) == 1
    assert cards[0]["kind"] == "digest"
    assert len(cards[0]["evidence"]) == 40
    assert cards[0]["title"] == "40 Agent Mode changes in Agent update"


def test_short_preamble_lists_keep_one_card_per_bullet():
    body = "\n".join(f"- Agent can now run task number {n} in parallel" for n in range(8))
    cards = w2_cards(body)

    assert len(cards) == 8 and all(len(card["evidence"]) == 1 for card in cards)


def test_cursor_patch_group_ends_at_the_first_unversioned_line():
    from _scripts.extract import parse_release_blocks, release_sections
    body = ("Patches (2)↓↑\n0.47.1: Improved performance for large files\n"
            "0.47.2: Agent tab accepts single-line selections\n"
            "This release focuses on agent stability for long sessions.\n"
            "#Agent tabs\nAgents now open in tabs.")
    sections = release_sections(parse_release_blocks(body))

    assert [(section["kind"], len(section["blocks"])) for section in sections] == [
        ("preamble", 1), ("generic", 2), ("feature", 1)]


def test_digest_title_stays_within_the_title_limit():
    title = "Reliability, Keyboard Shortcuts, Early access opt-in and a very long list of extras"
    body = "#New Features\n" + "\n".join(f"Agent can now run task number {n}" for n in range(3))
    card = w2_cards(body, title=title)[0]

    assert card["title"].startswith("3 Agent Mode changes in Reliability")
    assert len(card["title"]) <= 90 and card["title"].endswith("…")


@pytest.mark.parametrize(("texts", "theme", "feature", "kind"), [
    (["Introducing GPT-6 with Intelligent UI"], "model-support", False, "launch"),
    (["We're launching ChatGPT Go, a new low-cost subscription plan."], "pricing-model", False, "launch"),
    (["We're launching ChatGPT Go, our low cost subscription plan, in Brazil."], "pricing-model", False,
     "expansion"),
    (["ChatGPT Go is now available in 16 additional countries."], "pricing-model", False, "expansion"),
    (["Codex is now available in the ChatGPT app for iOS."], "mobile-desktop", False, "expansion"),
    (["Rolling out to Plus users on the web."], "mobile-desktop", False, "expansion"),
    (["Fast mode is now available for Opus 4.6."], "model-support", False, "launch"),
    (["Usage-based pricing now applies to every team."], "pricing-model", False, "pricing"),
    (["GPT-4.5 will be retired from the model picker next month."], "model-support", False, "policy"),
    (["We're doubling the message limits for Plus users."], "model-support", False, "policy"),
    (["Parental controls are now available to all families."], "safety-privacy", False, "policy"),
    (["Fixed a permission bypass in sandboxed commands"], "safety-privacy", False, "fix"),
    (["[VSCode] Fixed a permission prompt shown twice"], "safety-privacy", False, "fix"),
    (["Agent can run shell commands"], "agent-mode", False, "change"),
    (["Background Agent", "Agent can now run tests in the background."], "agent-mode", True, "launch"),
    (["Simpler, unified pricing", "Every plan now includes usage."], "pricing-model", True, "pricing"),
])
def test_kind_assignment(texts, theme, feature, kind):
    from _scripts.extract import card_kind
    assert card_kind(texts, theme, feature=feature) == kind


def test_identity_joins_every_evidence_quote_and_single_lines_keep_their_ids():
    body = "#Background Agent\nAgent can now run tests in the background.\nAgents report back when done."
    release = structured_release(body)
    card = w2_cards(body)[0]
    single = w2_cards("- Agent can now run tests in the background.")[0]

    assert card["card_id"] == card_id_for(
        "cursor", "2026-06-01",
        "Agent can now run tests in the background.\nAgents report back when done.",
        source_release=release["release_id"])
    assert single["card_id"] == card_id_for(
        "cursor", "2026-06-01", "Agent can now run tests in the background.",
        source_release=release["release_id"])
    assert card["extractor_version"] == single["extractor_version"] == "fallback-v5"


def test_tagged_bug_fix_lines_are_skipped_like_plain_fixes():
    cards = w2_cards("- [VSCode] Fixed the agent panel flickering\n- Windows: Fixed agent startup\n"
                     "- 0.48.7 - Fixes an issue where agent chats were deleted\n"
                     "- Agent can run shell commands")

    assert [quotes(card) for card in cards] == [["Agent can run shell commands"]]


def test_flattened_code_lines_are_not_evidence():
    body = ("#Cursor SDK\nAgents are now available from TypeScript.\n"
            "model: { id: \"composer-2.5\" },\nlocal: { cwd: process.cwd() },\n"
            "const agent = await Agent.create({")
    assert quotes(w2_cards(body)[0]) == ["Agents are now available from TypeScript."]


def test_card_title_ignores_sentence_punctuation_inside_inline_code():
    line = "Changed HTML comments (`<!-- ... -->`) to stay hidden. Comments remain visible"
    assert card_title(line, "Claude Code") == "Changed HTML comments (`<!-- ... -->`) to stay hidden"


def test_line_review_decision_applies_to_a_single_line_feature_card():
    body = "#Design Mode in canvases\nDesign Mode is now available in canvases."
    release = structured_release(body)
    line_id = card_id_for("cursor", "2026-06-01", "Design Mode is now available in canvases.",
                          source_release=release["release_id"])
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    card = extract_cards_from_release(release, themes, {line_id: "file-data"})[0]

    assert card["card_id"] == line_id
    assert card["theme"] == "file-data"
    assert card["theme_resolution"] == "manual-backfill-review-v1"


# W2 round 2: availability notes, resource memory and digest release labels.

def test_available_in_fragment_is_skipped():
    body = ("See how clothes could look on you.\n"
            "- Save your finds: Save any product to Favorites in your ChatGPT Library.\n"
            "Available in ChatGPT on mobile and web.")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog", title="New ways to shop")

    assert not any("Available in ChatGPT" in quote for card in cards for quote in quotes(card))


@pytest.mark.parametrize("note", [
    "Dots are rolling out gradually to eligible Pro and Business Premium users aged 18 and older.",
    "Now available to every Plus and Pro user who opts in from the agent settings page today.",
    "Start bills monthly with auto-renewal and is available from July 28, 2026.",
])
def test_availability_paragraph_joins_the_previous_card(note):
    body = ("We're introducing dots: always-on agents in ChatGPT that keep working between "
            "conversations.\n" + note + "\nPricing now uses a metered plan for every team.")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog", title="Meet your dot")

    assert [quotes(card)[1:] for card in cards if card["theme"] == "agent-mode"] == [[note]]
    agent = next(card for card in cards if card["theme"] == "agent-mode")
    assert agent["kind"] == "launch" and len(cards) == 2


def test_availability_paragraph_skips_pending_cards_and_first_paragraphs_stay():
    first = w2_cards("Agents are now available to every team on the Business plan in the agent panel.",
                     product="chatgpt", source_type="chatgpt_changelog", title="Agents for teams")
    assert len(first) == 1 and len(first[0]["evidence"]) == 1

    body = ("Three new agent plugins help students work with their course materials.\n"
            "- Quasar renderer: geometric palettes for flashcards\n"
            "The plugins are available through Edu deployments chosen by each school.")
    cards = w2_cards(body, product="chatgpt", source_type="chatgpt_changelog", title="Edu plugins")
    agent = next(card for card in cards if card["theme"] == "agent-mode")
    assert quotes(agent)[-1].startswith("The plugins are available")
    assert [len(card["evidence"]) for card in cards if card["theme"] == "__candidate__"] == [1]


def test_feature_sections_keep_trailing_availability_text():
    card = w2_cards("#Background Agent\nAgent can now run tests in the background.\n"
                    "Background Agent is rolling out to all users starting today.")[0]
    assert len(card["evidence"]) == 2


def test_sentence_openings_are_not_list_labels():
    from _scripts.extract import is_labelled_item
    assert is_labelled_item("Apply button: We've added some polish to the apply flow.")
    assert not is_labelled_item("We’re introducing dots: always-on agents in ChatGPT.")


@pytest.mark.parametrize(("line", "theme"), [
    ("Improved LSP tool rendering and memory context building to no longer read entire files",
     "reliability-performance"),
    ("Improved session upload and memory sync to avoid reading large files into memory before "
     "size/binary checks", "reliability-performance"),
    ("Reduced baseline memory by ~16MB by deferring Yoga WASM preloading", "reliability-performance"),
    ("Reduced memory footprint for SDK and CCR sessions using stream-json output",
     "reliability-performance"),
    ("Memory now remembers your preferred units", "memory"),
    ("Reduced the memory footprint of MEMORY.md files loaded at startup", "memory"),
])
def test_resource_memory_lines_route_to_reliability(line, theme):
    from _scripts.extract import line_classification
    classification = line_classification(line, load_theme_vocabulary("_scripts/themes.yaml"))
    assert classification["theme"] == theme


@pytest.mark.parametrize(("release", "label"), [
    ({"source_type": "cursor_changelog", "source_url": "https://cursor.com/changelog/0-48-x",
      "title": "Chat tabs, Custom modes & Faster indexing"}, "0.48.x"),
    ({"source_type": "cursor_changelog", "source_url": "https://cursor.com/changelog/1-1",
      "title": "Background Agents in Slack"}, "1.1"),
    ({"source_type": "cursor_changelog", "source_url": "https://cursor.com/changelog/projects",
      "title": "Cursor Projects"}, "Cursor Projects"),
    ({"source_type": "chatgpt_changelog", "source_url": "https://help.openai.com/x",
      "title": "Share files and folders from your Library"}, "Share files and folders…"),
    ({"source_type": "github_releases", "source_url": "https://github.com/x/releases/tag/v2.1.300",
      "title": "v2.1.300", "version": "v2.1.300"}, "v2.1.300"),
])
def test_digest_release_label(release, label):
    from _scripts.extract import digest_release_label
    assert digest_release_label(release) == label
    assert len(label) <= 40


def test_cursor_digest_title_uses_the_version_from_the_changelog_url():
    body = "#New Features\n" + "\n".join(f"Agent can now run task number {n}" for n in range(3))
    release = {**structured_release(body, title="Chat tabs, Custom modes & Faster indexing"),
               "source_url": "https://cursor.com/changelog/0-48-x"}
    card = extract_cards_from_release(release, load_theme_vocabulary("_scripts/themes.yaml"))[0]
    assert card["title"] == "3 Agent Mode changes in 0.48.x"


# W2 PR 2: holding theme ("Other changes") for list lines without a theme; kind headings.

OTHER_LINES = [
    "Added new quasar renderer for geometric palettes",
    "Changed the zephyr gauge to round half values up",
    "Improved nebula glyph spacing in narrow panes",
]
OTHER_LIST = "## What's changed\n" + "\n".join(f"- {line}" for line in OTHER_LINES)


def other_release(body: str = OTHER_LIST):
    return structured_release(body, product="claude-code", source_type="github_releases",
                              title="v2.1.300", version="v2.1.300")


def test_list_lines_without_a_theme_form_one_other_changes_digest_per_release():
    body = (OTHER_LIST + "\n- Introducing quasar palettes for every gauge"
            "\n- Agent can now run shell commands after approval")
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    cards = extract_cards_from_release(other_release(body), themes)

    assert not [card for card in cards if card["theme"] == "__candidate__"]
    other = [card for card in cards if card["theme"] == "uncategorized"]
    digest = next(card for card in other if card["kind"] == "digest")
    assert digest["title"] == "3 other changes in v2.1.300"
    assert quotes(digest) == OTHER_LINES
    assert digest["description"] == "Claude Code — v2.1.300: 3 other changes"
    assert digest["card_id"] == card_id_for(
        "claude-code", "2026-06-01", "\n".join(OTHER_LINES), source_release=digest["source_release"])
    # A high-signal line without a theme stays a standalone card of the holding theme.
    standalone = [card for card in other if card["kind"] != "digest"]
    assert [(quotes(card), card["kind"]) for card in standalone] == [
        (["Introducing quasar palettes for every gauge"], "launch")]
    assert {card["theme"] for card in cards} == {"uncategorized", "agent-mode"}
    assert all(validate_card(card, set(themes)) == [] for card in cards)


def test_holding_theme_is_assigned_by_structure_never_by_words():
    from _scripts.extract import line_classification
    themes = load_theme_vocabulary("_scripts/themes.yaml")

    assert themes["uncategorized"]["display_name"] == "Other changes"
    assert themes["uncategorized"]["terms"] == set()
    line = "Other changes to the uncategorized quasar list"
    assert line_classification(line, themes)["theme"] == "__candidate__"
    # Without a holding theme in the vocabulary, list lines wait for review as before.
    official = {slug: theme for slug, theme in themes.items() if theme["status"] == "official"}
    cards = extract_cards_from_release(other_release(), official)
    assert [card["theme"] for card in cards] == ["__candidate__"] * 3


def test_prose_feature_sections_and_short_lists_without_a_theme_still_wait_for_review():
    body = ("New quasar renderer for geometric palettes.\n"
            "#Zephyr gauges\nGauges now round half values up.")
    prose = w2_cards(body, title="Quasar update")
    assert [(card["theme"], quotes(card)) for card in prose] == [
        ("__candidate__", ["New quasar renderer for geometric palettes."]),
        ("__candidate__", ["Gauges now round half values up."]),
    ]
    short_list = w2_cards("- Quasar renderer draws geometric palettes\n"
                          "- Zephyr gauges round half values up",
                          product="chatgpt", source_type="chatgpt_changelog", title="Quasar update")
    assert [card["theme"] for card in short_list] == ["__candidate__"] * 2


def test_review_decisions_cannot_name_the_holding_theme(tmp_path: Path):
    review = tmp_path / "review.yaml"
    review.write_text("decisions:\n  card-1: uncategorized\n", encoding="utf-8")

    with pytest.raises(ValueError, match="unknown themes in semantic review: uncategorized"):
        load_review_decisions(review, load_theme_vocabulary("_scripts/themes.yaml"))


def test_card_decision_moves_an_other_changes_digest_into_an_official_theme():
    themes = load_theme_vocabulary("_scripts/themes.yaml")
    digest = extract_cards_from_release(other_release(), themes)[0]

    moved = extract_cards_from_release(other_release(), themes,
                                       {digest["card_id"]: "interface-experience"})[0]

    assert moved["card_id"] == digest["card_id"]
    assert moved["theme"] == "interface-experience"
    assert moved["title"] == "3 Interface Experience changes in v2.1.300"


@pytest.mark.parametrize(("heading", "kind"), [
    ("Improved Code Review", "change"),
    ("Improvement to long sessions", "change"),
    ("Improvements for agent planning", "change"),
    ("Improving tab completions", "change"),
    ("Better context for agents", "change"),
    ("Faster indexing", "change"),
    ("Updated model picker", "change"),
    ("Update to Bugbot", "change"),
    ("Updates to the agent panel", "change"),
    ("Fixed agent restarts", "fix"),
    ("Fix for terminal hangs", "fix"),
    ("Fixes in the agent panel", "fix"),
    ("Background Agent", "launch"),
    ("Betterment of plans", "launch"),
    ("Upgraded terminal", "launch"),
])
def test_feature_heading_names_an_improvement_or_a_fix(heading, kind):
    from _scripts.extract import card_kind
    assert card_kind([heading, "Agents now plan before they edit."], "agent-mode", feature=True) == kind


def test_improvement_heading_outranks_launch_wording_of_its_section():
    from _scripts.extract import card_kind
    assert card_kind(["Improved Code Review", "Code review is now available to every team."],
                     "developer-workflow", feature=True) == "change"
    assert card_kind(["Code Review", "Code review is now available to every team."],
                     "developer-workflow", feature=True) == "launch"
    card = w2_cards("#Faster indexing\nIndexing large repositories now takes half the time.")[0]
    assert (card["title"], card["kind"]) == ("Faster indexing", "change")


def test_patch_version_bug_fix_lines_are_skipped_rather_than_published_as_other_changes():
    # Cursor patch groups list "1.7.13: Bug fixes"; with no theme they would otherwise
    # land in the release's Other changes digest.
    body = ("Patches (4)↓↑\n1.7.13: Bug fixes\n2.0.1-2.0.28: Bug fixes\n"
            "1.7.21: Screenshot fixes\n1.7.14: Plan mode improvements and interactive todos")
    cards = w2_cards(body)

    assert [quotes(card) for card in cards] == [
        ["1.7.21: Screenshot fixes", "1.7.14: Plan mode improvements and interactive todos"]]
    assert cards[0]["theme"] == "uncategorized"
