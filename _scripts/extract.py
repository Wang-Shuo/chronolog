from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from _scripts.common import PipelinePaths, card_id_for, read_json, read_yaml, slugify, write_json


IMPACT_WORDS = {
    "paradigm-shift": ["agent", "autonomous", "pricing", "200k", "major"],
    "significant": ["support", "new", "expanded", "integration", "model"],
}
AMBIGUITY_MARGIN = 25
GENERIC_HEADING_RE = re.compile(
    r"^(?:#+\s*)?(?:new features?|features?|improvements?|bug fixes?|fixes?|"
    r"other changes?|breaking changes?|what[’']?s (?:new|changed)|coming soon|changelog|"
    r"release notes?|patches?(?: \(\d+\))?(?:↓↑)?|chores?|how it works|"
    r"how to use it|key details|known limitations?|plan differences|"
    r"this build includes|cursor start includes)[:.!]?$",
    re.I,
)
VERSION_ONLY_RE = re.compile(r"^v?\d+(?:\.\d+){0,3}(?:[- ]?\w+)?$", re.I)
INSTRUCTION_PREFIXES = (
    "click on ",
    "for details",
    "go to ",
    "let us know",
    "navigate to ",
    "please give ",
    "please keep ",
    "please let ",
    "please report ",
    "select ",
    "settings ->",
    "this is very experimental",
    "toggle ",
    "to add ",
    "to enable ",
    "to get started ",
    "to share ",
    "to use ",
    "try using ",
    "try it out ",
    "download the ",
    "web only ",
    "we hope ",
    "learn more",
    "read more",
    "see:",
)
BUGFIX_PREFIX_RE = re.compile(
    r"^(?:hotfix(?:es)?|tiny (?:bug )?fix|small fixes?|minor .{0,30}fixes?|"
    r"bugfix|bug fixes|fixed|fix(?:es)?|resolved|reverted|patch(?:es)?|"
    r"v?\d+(?:\.\d+)+:\s*(?:fixed|fix(?:es)?)|"
    r"includes? (?:a |some )?fix|also fixes|this update fixes|"
    r"update \([^)]*\):? fixes|more diff fixes|some .{0,30}fixes?|"
    r"just includes bug fixes|other fixes|various bugs|miscellaneous fixes|"
    r"internal fixes)\b",
    re.I,
)
BUGFIX_TEXT_RE = re.compile(
    r"(?:\b(?:bug|issue|problem) (?:is |was )?(?:now )?fixed\b|"
    r"\b(?:has|have) been (?:fixed|restored)\b|\bworks? again\b|"
    r"\bbugs? .{0,40}\bsquashed\b|\bsupport has been restored\b)",
    re.I,
)
SECURITY_FIX_RE = re.compile(
    r"\b(?:security (?:issue|vulnerability)|vulnerability|cve-\d{4}-\d+|"
    r"permission|workspace trust|consent)\b",
    re.I,
)
LOW_SIGNAL_RE = re.compile(
    r"^(?:other (?:bits of )?polish|other small changes|small things|"
    r"a few other quality-of-life updates|updated some css|"
    r"internal infrastructure improvements(?: \(no user-facing changes\))?|"
    r"bug fixes and reliability improvements|cursor \d+(?:\.\d+)? is now available|"
    r"stability(?: improvements| \(\d+\)↓↑)|category: .+|"
    r"access to advanced data analysis|requires a remote mcp server)[.!]?$",
    re.I,
)
AVAILABILITY_PREFIXES = (
    "availability:",
    "at launch, this experience is available",
    "available on all chatgpt plans",
    "rollout begins today",
    "this feature is available today",
    "this feature is not yet available",
    "this was previously made available",
    "note this feature is currently limited",
)
BARE_LOCALE_RE = re.compile(r"^[A-Za-z][A-Za-z ]+ \([a-z]{2}(?:-[A-Za-z]{2,4})?\)$")
BOILERPLATE_PREFIXES = (
    "we're excited",
    "we’re excited",
    "we've made several updates",
    "we’ve made several updates",
    "here's what's new",
    "here’s what’s new",
)

# These rules encode the manual review decisions from the three-product backfill.
# They are applied only when the controlled vocabulary has no clear winner.
SEMANTIC_THEME_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "safety-privacy",
        (
            "permission",
            "sandbox",
            "privacy",
            "security",
            "trusted contact",
            "parental control",
            "data protection",
        ),
    ),
    (
        "account-access",
        ("login", "sign in", "authentication", "oauth", "account control"),
    ),
    (
        "pricing-model",
        (
            "price",
            "pricing",
            "billing",
            "cost",
            "subscription",
            "credits",
            "purchase chatgpt plus",
            "bills monthly",
            "$20/month",
            "$200/month",
        ),
    ),
    (
        "automation-scheduling",
        (
            "automation",
            "automations",
            "automated prompt",
            "scheduled task",
            "recurring prompt",
            "cron",
            "scheduler",
            "schedule",
            "/loop",
            "/proactive",
        ),
    ),
    (
        "projects-workspaces",
        (
            "start a new project",
            "project directly from a chat",
            "project context",
            "projects bring your chats",
            "project workspace",
            "conversation branch",
            "branch conversations",
            "composer history",
            "session history",
            "forking sessions",
            "resume sessions",
            "session resume",
        ),
    ),
    (
        "accessibility-localization",
        (
            "accessibility",
            "screen reader",
            "language pack",
            "languages in the interface",
            "japanese ime",
            "full width zenkaku",
            "internationalization",
            "localized",
        ),
    ),
    (
        "learning-tools",
        ("study mode", "learning experience", "socratic style", "guide understanding"),
    ),
    (
        "image-generation",
        ("dall e", "image generation", "generate images", "image library"),
    ),
    (
        "voice",
        ("voice", "dictation", "transcription", "speech to text", "audio"),
    ),
    (
        "multimodal",
        ("multimodal", "image input", "visual input", "screen share", "video"),
    ),
    (
        "memory",
        ("memory", "memories", "personalization", "custom instruction", "personality"),
    ),
    (
        "search-browsing",
        ("web search", "browse", "browsing", "deep research", "search result"),
    ),
    (
        "apps-integrations",
        (
            "plugin",
            "connector",
            "integration",
            "app directory",
            "mcp",
            "extension marketplace",
            "extensions",
            "azure openai",
            "jira",
            "slack",
            "github app",
            "sdk",
            "hook event",
            "hooks",
            "browser controls",
            "remote control",
        ),
    ),
    (
        "enterprise-admin",
        ("enterprise", "administrator", "admin control", "workspace control"),
    ),
    (
        "mobile-desktop",
        (
            "mobile",
            "desktop",
            "ios",
            "android",
            "macos",
            "windows app",
            "windows desktop",
            "windows support",
            "on windows",
            "for windows",
            "ipad",
            "iphone",
        ),
    ),
    (
        "context-window",
        ("context", "token limit", "context window", "compaction", "prompt cache"),
    ),
    (
        "file-data",
        (
            "file upload",
            "uploaded files",
            "file library",
            "file type support",
            "data analysis",
            "code interpreter",
            "spreadsheet",
            "document",
            "pdf",
            "canvas",
            "interactive chart",
        ),
    ),
    (
        "interface-experience",
        (
            "user interface",
            "sidebar",
            "navigation",
            "keyboard shortcut",
            "keybinding",
            "picker",
            "prompt bar",
            "rendering",
            "autocomplete",
            "completion",
            "stop generating",
            "hotkey",
            "chat history",
            "select and copy",
            "scrollbar",
            "chat styling",
            "tooltip",
            "keyboard ergonomics",
            "activity bar",
            "onboarding",
            "full screen",
            "fullscreen",
            "status indicator",
            "prompt footer",
            "progress indicator",
            "spinner",
            "message composer",
            "focus mode",
            "selection",
            "copy shortcut",
            "conversation search",
            "interaction improvements",
        ),
    ),
    (
        "editor-experience",
        (
            "editor",
            "edit",
            "edits",
            "diff",
            "cmd k",
            "cmd-k",
            "copilot++",
            "cursor prediction",
            "apply chat suggestion",
            "apply chat suggestions",
            "lint error",
            "codebase",
            "multi file",
            "multi-file",
            "word wrap",
            "ghost text",
            "intellisense",
        ),
    ),
    (
        "developer-workflow",
        (
            "terminal",
            "language server",
            "lsp",
            "pull request",
            "code review",
            "code intelligence",
            "shell",
            "bash",
            "command",
            "diff",
            "task management",
            "git",
            "github pr",
            "worktree",
            "dev container",
            "remote ssh",
            "wsl",
            "linter",
            "debug mode",
            "/debug",
            "code block",
            "codeblocks",
            "pull requests",
            "pr review",
            "commit",
        ),
    ),
    (
        "reliability-performance",
        (
            "performance",
            "latency",
            "faster",
            "speed",
            "responsiveness",
            "stability",
            "more robust",
            "significantly more stable",
            "stalled api stream",
            "progress heartbeat",
        ),
    ),
    (
        "collaboration",
        ("collaboration", "collaborator", "team", "share", "shared"),
    ),
    (
        "agent-mode",
        (
            "agent",
            "autonomous",
            "background session",
            "background script",
            "agent workflow",
            "subagent",
            "auto mode",
            "auto review",
            "auto-review",
            "interpreter mode",
            "task tool",
            "taskcreate",
            "taskupdate",
            "cloud environment",
            "in-cloud",
            "monitor tool",
            "work for longer",
        ),
    ),
    (
        "model-support",
        (
            "model",
            "reasoning",
            "instruction following",
            "intelligence",
            "gpt 4",
            "gpt 5",
            "claude 3",
            "claude opus",
            "claude sonnet",
            "sonnet",
            "opus",
            "gemini",
            "o1",
            "o3",
            "o4",
        ),
    ),
)


def normalize_match_text(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", text).strip()


def contains_phrase(normalized_text: str, normalized_phrase: str) -> bool:
    if not normalized_phrase:
        return False
    return f" {normalized_phrase} " in f" {normalized_text} "


def load_theme_vocabulary(path: str | Path) -> dict[str, dict[str, Any]]:
    data = read_yaml(Path(path))
    vocab = {}
    for theme in data["themes"]:
        canonical_terms = {
            normalize_match_text(theme["slug"]),
            normalize_match_text(theme["display_name"]),
        }
        alias_terms = {
            normalize_match_text(term) for term in theme.get("aliases", [])
        } - canonical_terms
        vocab[theme["slug"]] = {
            **theme,
            "canonical_terms": canonical_terms,
            "alias_terms": alias_terms,
            "terms": canonical_terms | alias_terms,
        }
    return vocab


def load_review_decisions(
    path: str | Path,
    themes: dict[str, dict[str, Any]],
) -> dict[str, str]:
    review_path = Path(path)
    if not review_path.exists():
        return {}
    payload = read_yaml(review_path) or {}
    decisions = {
        str(card_id): str(disposition)
        for card_id, disposition in (payload.get("decisions") or {}).items()
    }
    invalid = sorted(
        {
            disposition
            for disposition in decisions.values()
            if disposition != "skip" and disposition not in themes
        }
    )
    if invalid:
        raise ValueError(f"unknown themes in semantic review: {', '.join(invalid)}")
    return decisions


def split_release_lines(body: str) -> list[str]:
    lines = []
    fence = None
    for raw in body.splitlines():
        stripped = raw.strip()
        marker = re.match(r"^(`{3,}|~{3,})", stripped)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        if stripped.startswith("#"):
            continue
        line = re.sub(r"^(?:[-*]\s+|\d+[.)]\s+)", "", stripped).strip()
        # HTML changelog text may flatten <pre> blocks without Markdown fences.
        # These TypeScript statements are examples, not release announcements.
        if re.match(r"^(?:(?:const|let|var)\s+\w+\s*=|import\s+[{*]|import\s+\w+\s+from\s|for\s+await\s*\(|console\.log\s*\()", line):
            continue
        if len(line) >= 12:
            lines.append(line)
    return lines


def rank_theme_matches(
    text: str,
    themes: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    normalized = normalize_match_text(text)
    matches = []
    for slug, theme in themes.items():
        canonical = sorted(
            term
            for term in theme.get("canonical_terms", set())
            if contains_phrase(normalized, term)
        )
        aliases = sorted(
            term
            for term in theme.get("alias_terms", theme.get("terms", set()))
            if term not in canonical and contains_phrase(normalized, term)
        )
        matched_terms = canonical + aliases
        if not matched_terms:
            continue
        score = sum(100 + 10 * len(term.split()) for term in canonical)
        score += sum(40 + 10 * len(term.split()) for term in aliases)
        matches.append(
            {
                "theme": slug,
                "score": score,
                "matched_terms": matched_terms,
            }
        )
    return sorted(matches, key=lambda match: (-match["score"], match["theme"]))


def candidate_suggestion(text: str) -> str:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9]+", text.lower())[:3]
    if words and words[0] in {"new"}:
        words = words[1:]
    return slugify(" ".join(words) or "unclassified")


def classify_theme(text: str, themes: dict[str, dict[str, Any]]) -> dict[str, Any]:
    matches = rank_theme_matches(text, themes)
    if not matches:
        return {
            "theme": "__candidate__",
            "theme_suggestion": candidate_suggestion(text),
            "theme_review_reason": "no_match",
            "theme_matches": [],
        }

    top = matches[0]
    if len(matches) > 1 and top["score"] - matches[1]["score"] < AMBIGUITY_MARGIN:
        return {
            "theme": "__candidate__",
            "theme_suggestion": f"{top['theme']}-or-{matches[1]['theme']}",
            "theme_review_reason": "ambiguous_match",
            "theme_matches": matches,
        }

    result = {"theme": top["theme"]}
    if len(matches) > 1:
        result["theme_matches"] = matches
    return result


def choose_theme(text: str, themes: dict[str, dict[str, Any]]) -> tuple[str, str | None]:
    classification = classify_theme(text, themes)
    return classification["theme"], classification.get("theme_suggestion")


def choose_impact(text: str) -> str:
    normalized = normalize_match_text(text)
    for impact, words in IMPACT_WORDS.items():
        if any(contains_phrase(normalized, normalize_match_text(word)) for word in words):
            return impact
    return "incremental"


def semantic_theme_hint(
    text: str,
    themes: dict[str, dict[str, Any]],
) -> str | None:
    normalized = normalize_match_text(text)
    for theme, phrases in SEMANTIC_THEME_RULES:
        if theme not in themes:
            continue
        if any(contains_phrase(normalized, normalize_match_text(phrase)) for phrase in phrases):
            return theme
    return None


def semantic_preclassification_override(
    text: str,
    themes: dict[str, dict[str, Any]],
) -> str | None:
    normalized = normalize_match_text(text)
    specific = (
        ('agent-mode', r'^ChatGPT Work is an agent|^We[’\']re introducing dots'),
        ('collaboration', r'share with specific people|share across your workspace|library sharing|assign viewer or editor'),
        ('model-support', r'^(?:Added|Introducing) (?:Claude )?(?:Opus|Sonnet|Haiku|Fable|GPT[- ])'),
        ('pricing-model', r'\$\d|(?:request|token)[ -]based pricing|\bcredits?\b.*\b(?:usage|top.up|allowance)\b'),
        ('safety-privacy', r'lockdown mode|credentials? from subprocess|(?:permission|classifier) rules'),
        ('developer-workflow', r'login shell'),
        ('interface-experience', r'recent (?:chats|conversations)|new chat ux|new settings|theme picker|focus view'),
        ('context-window', r'auto.compact|autocompactwindow'),
    )
    for theme, pattern in specific:
        if theme in themes and re.search(pattern, text, re.I):
            return theme
    technical_memory_phrases = (
        "memory allocation",
        "memory issue",
        "memory leak",
        "memory overhead",
        "memory pressure",
        "memory usage",
        "out of memory",
    )
    if "reliability-performance" in themes and any(
        contains_phrase(normalized, phrase) for phrase in technical_memory_phrases
    ):
        return "reliability-performance"
    if "safety-privacy" in themes and re.search(
        r"\b(?:permission|privacy|sandbox|security (?:control|issue|review|vulnerability)|"
        r"vulnerability|workspace trust|consent)\b",
        text,
        re.I,
    ):
        return "safety-privacy"
    if "context-window" in themes and re.search(
        r"\b(?:codebase context|context window|entire repo|long context|"
        r"search through files)\b",
        text,
        re.I,
    ):
        return "context-window"
    if "model-support" in themes and re.search(
        r"\b(?:gpt[- ]?4(?:o|\.\d+)?|gpt[- ]?[56](?:\.\d+)?|o[134](?:-pro|-mini)?|"
        r"sonnet|opus|gemini)\b",
        text,
        re.I,
    ):
        return "model-support"
    if "apps-integrations" in themes and re.search(r"\bgpt store\b", text, re.I):
        return "apps-integrations"
    if "file-data" in themes and re.search(
        r"\b(?:financial|health|medical) context\b",
        text,
        re.I,
    ):
        return "file-data"
    return None


def should_skip_line(line: str, classification: dict[str, Any]) -> bool:
    normalized = normalize_match_text(line)
    visible = line.strip().lstrip("#").strip()
    if GENERIC_HEADING_RE.fullmatch(visible) or VERSION_ONLY_RE.fullmatch(visible):
        return True
    if LOW_SIGNAL_RE.fullmatch(visible) or BARE_LOCALE_RE.fullmatch(visible):
        return True
    if any(normalized.startswith(normalize_match_text(prefix)) for prefix in AVAILABILITY_PREFIXES):
        return True
    if (
        re.match(r"^(?:available (?:only |on |to |for )|rolling out)", visible, re.I)
        and len(normalized.split()) <= 35
    ):
        return True
    if any(
        normalized.startswith(normalize_match_text(prefix))
        for prefix in INSTRUCTION_PREFIXES
    ):
        return True
    if (
        (BUGFIX_PREFIX_RE.match(visible) or BUGFIX_TEXT_RE.search(visible))
        and not SECURITY_FIX_RE.search(visible)
    ):
        return True
    if classification.get("theme_review_reason") == "no_match" and any(
        normalized.startswith(normalize_match_text(prefix))
        for prefix in BOILERPLATE_PREFIXES
    ):
        return True
    return False


def extract_cards_from_release(
    release: dict[str, Any],
    themes: dict[str, dict[str, Any]],
    review_decisions: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    lines = split_release_lines(release.get("body", ""))
    if not lines and release.get("source_type") not in {None, "fixture"}:
        return []
    lines = lines or [release["title"]]
    cards = []
    seen_card_ids: set[str] = set()
    source_release = release.get("release_id") or (
        f"{release['product']}-{release['date']}-"
        f"{slugify(release.get('version') or release['title'])}"
    )
    release_scoped_identity = (
        source_release
        if release.get("release_id") and release.get("source_type") != "fixture"
        else None
    )
    for line in lines:
        card_id = card_id_for(
            release["product"],
            release["date"],
            line,
            source_release=release_scoped_identity,
        )
        review_decision = (review_decisions or {}).get(card_id)
        if review_decision == "skip":
            continue
        classification = classify_theme(line, themes)
        if review_decision:
            classification = {
                "theme": review_decision,
                "theme_resolution": "manual-backfill-review-v1",
                "theme_matches": classification.get("theme_matches", []),
            }
        else:
            override = semantic_preclassification_override(line, themes)
            if override:
                classification = {
                    "theme": override,
                    "theme_resolution": "manual-semantic-rule-v2",
                    "theme_matches": classification.get("theme_matches", []),
                }
        if not review_decision and should_skip_line(line, classification):
            continue
        if not review_decision and classification["theme"] == "__candidate__":
            hint = semantic_theme_hint(line, themes)
            if hint:
                classification = {
                    "theme": hint,
                    "theme_resolution": "manual-semantic-rule-v1",
                    "theme_matches": classification.get("theme_matches", []),
                }
        if card_id in seen_card_ids:
            continue
        seen_card_ids.add(card_id)
        impact = choose_impact(line)
        card = {
            "type": "change",
            "card_id": card_id,
            "product": release["product"],
            "product_name": release["product_name"],
            "source_release": source_release,
            "date": release["date"],
            "title": line[:80].rstrip(),
            "slug": slugify(line)[:80].strip("-"),
            "theme": classification["theme"],
            "impact": impact,
            "description": f"{release['product_name']} — {release['title']}: {line}",
            "comparison": "",
            "evidence": [{"source_release": release.get("source_url", ""), "quote": line}],
            "extractor_version": "fallback-v3" if release_scoped_identity else "fallback-v1",
            "source_type": release.get("source_type", "unknown"),
        }
        card.update({key: value for key, value in classification.items() if key != "theme"})
        if impact in {"significant", "paradigm-shift"}:
            card["ai_generated"] = True
            card["confidence"] = "low"
        cards.append(card)
        if len(cards) >= 5:
            break
    return cards


def extract_run(run_id: str, root: Path = ROOT) -> list[dict[str, Any]]:
    paths = PipelinePaths(run_id, root=root)
    themes = load_theme_vocabulary(root / "_scripts/themes.yaml")
    review_decisions = load_review_decisions(
        root / "_scripts/backfill_review.yaml",
        themes,
    )
    review_decisions.update(load_review_decisions(root / "_scripts/m2_review.yaml", themes))
    releases = read_json(paths.collected)["releases"]
    cards = [
        card
        for release in releases
        for card in extract_cards_from_release(release, themes, review_decisions)
    ]
    write_json(paths.extracted, {"run_id": run_id, "change_cards": cards})
    candidates = [
        {
            key: card[key]
            for key in [
                "card_id",
                "product",
                "product_name",
                "date",
                "title",
                "theme_suggestion",
                "theme_review_reason",
                "theme_matches",
                "evidence",
            ]
            if key in card
        }
        for card in cards
        if card["theme"] == "__candidate__"
    ]
    write_json(paths.theme_candidates, {"run_id": run_id, "candidates": candidates})
    return cards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    extract_run(args.run_id)


if __name__ == "__main__":
    main()
