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
# A surface tag, short label or patch version before a fix ("[VSCode] Fixed ...",
# "Windows: Fixed ...", "1.7.13: Bug fixes").
FIX_LABEL_PREFIX_RE = re.compile(
    r"^(?:(?:\[[^\]]{1,40}\]\s*)+(?:[A-Z][\w .-]{0,30}:\s+)?|[A-Z][\w .-]{0,30}:\s+|"
    r"v?\d+(?:\.\d+)+(?:\s*[-–]\s*v?\d+(?:\.\d+)+)?\s*[:\-–]\s+)"
    r"(?=(?:fixed|fix(?:es)?|resolved|reverted|bug ?fix(?:es)?)\b)",
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
    """Themes by slug with their match terms. A holding theme has no terms: it is
    assigned by card structure, never matched by words."""
    data = read_yaml(Path(path))
    vocab = {}
    for theme in data["themes"]:
        if theme.get("status") == "holding":
            vocab[theme["slug"]] = {
                **theme, "canonical_terms": set(), "alias_terms": set(), "terms": set()
            }
            continue
        canonical_terms = {
            normalize_match_text(theme["slug"]),
            normalize_match_text(theme["display_name"]),
        }
        context_terms = {
            normalize_match_text(term) for term in theme.get("context_aliases", [])
        } - canonical_terms
        alias_terms = {
            normalize_match_text(term) for term in theme.get("aliases", [])
        } - canonical_terms
        vocab[theme["slug"]] = {
            **theme,
            "canonical_terms": canonical_terms,
            "alias_terms": alias_terms | context_terms,
            "context_terms": context_terms,
            "terms": canonical_terms | alias_terms | context_terms,
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
    # Decisions name official themes only; a holding theme is never a review outcome.
    invalid = sorted(
        {
            disposition
            for disposition in decisions.values()
            if disposition != "skip"
            and (disposition not in themes or themes[disposition].get("status") == "holding")
        }
    )
    if invalid:
        raise ValueError(f"unknown themes in semantic review: {', '.join(invalid)}")
    return decisions


# HTML changelog text may flatten <pre> blocks without Markdown fences.
# These TypeScript statements are examples, not release announcements.
CODE_SAMPLE_RE = re.compile(
    r"^(?:(?:const|let|var)\s+\w+\s*=|import\s+[{*]|import\s+\w+\s+from\s|"
    r"for\s+await\s*\(|console\.log\s*\()"
)
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")
MIN_LINE_CHARS = 12


def _unfenced_lines(body: str):
    """Stripped body lines outside fenced code blocks."""
    fence = None
    for raw in body.splitlines():
        stripped = raw.strip()
        marker = FENCE_RE.match(stripped)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield stripped


def split_release_lines(body: str) -> list[str]:
    """Candidate lines of a release body: the denominator shown on Release pages."""
    lines = []
    for stripped in _unfenced_lines(body):
        if stripped.startswith("#"):
            continue
        line = re.sub(r"^(?:[-*]\s+|\d+[.)]\s+)", "", stripped).strip()
        if CODE_SAMPLE_RE.match(line):
            continue
        if len(line) >= MIN_LINE_CHARS:
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
    # A theme matched only by plan, platform or audience names (context_aliases) yields
    # to any theme matched by what the line is about.
    context_only = {
        match["theme"] for match in matches
        if set(match["matched_terms"]) <= themes[match["theme"]].get("context_terms", set())
    }
    if len(context_only) < len(matches):
        matches = [match for match in matches if match["theme"] not in context_only]
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


# Resource memory (RAM) rather than the product's memory feature: a line about memory
# that also names a resource measure, unless it is about memories or memory files.
RESOURCE_MEMORY_RE = re.compile(
    r"\b(?:footprint|usage|consumption|leaks?|pressure|heap|wasm|preload(?:s|ed|ing)?|"
    r"\d+(?:\.\d+)?\s?[KMG]B|into memory|"
    r"(?:read|reading|load|loading) (?:the )?(?:entire|large|whole) files?)\b",
    re.I,
)
PRODUCT_MEMORY_RE = re.compile(
    r"\bmemories\b|\bremember\w*|\brecall\w*|\bpersonali[sz]\w*|\bMEMORY\.md\b|\bCLAUDE\.md\b|"
    r"\bauto[- ]?memory\b|\bautoMemory\w*|/memory\b|`memory`|"
    r"\b(?:saved|persistent) memory\b|\bmemory (?:files?|index|stores?|dialog|directory|tool)\b",
    re.I,
)
# A dollar amount, not shell or awk text such as $1 or $(pwd); matched outside code spans.
MONEY_RE = r"(?<![\w$])\$\d+(?:[.,]\d+)*[kKmMbB]?(?![\w}'\"])"
INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
# (theme, pattern, whether inline code is ignored); the first match wins.
SPECIFIC_OVERRIDES = (
    ('agent-mode', r'^ChatGPT Work is an agent|^We[’\']re introducing dots', False),
    ('collaboration', r'share with specific people|share across your workspace|library sharing|assign viewer or editor', False),
    ('model-support', r'^(?:Added|Introducing) (?:Claude )?(?:Opus|Sonnet|Haiku|Fable|GPT[- ])', False),
    ('pricing-model', MONEY_RE, True),
    ('pricing-model', r'(?:request|token)[ -]based pricing|\bcredits?\b.*\b(?:usage|top.up|allowance)\b', False),
    ('safety-privacy', r'lockdown mode|credentials? from subprocess|(?:permission|classifier) rules', False),
    ('developer-workflow', r'login shell', False),
    ('interface-experience', r'recent (?:chats|conversations)|new chat ux|new settings|theme picker|focus view', False),
    ('context-window', r'auto.compact|autocompactwindow', False),
)


def is_resource_memory(text: str) -> bool:
    return bool(
        re.search(r"\bmemory\b", text, re.I)
        and RESOURCE_MEMORY_RE.search(text)
        and not PRODUCT_MEMORY_RE.search(text)
    )


def semantic_preclassification_override(
    text: str,
    themes: dict[str, dict[str, Any]],
    product: str | None = None,
) -> str | None:
    normalized = normalize_match_text(text)
    code_free = INLINE_CODE_RE.sub(" ", text)
    for theme, pattern, ignore_code in SPECIFIC_OVERRIDES:
        if theme in themes and re.search(pattern, code_free if ignore_code else text, re.I):
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
    resource_sense = product in themes.get("memory", {}).get("resource_sense_products", ())
    if "reliability-performance" in themes and (
        any(contains_phrase(normalized, phrase) for phrase in technical_memory_phrases)
        or is_resource_memory(text)
        or (resource_sense and re.search(r"\bmemory\b", text, re.I)
            and not PRODUCT_MEMORY_RE.search(text))
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
        re.match(r"^(?:available (?:only |on |to |for |in )|rolling out)", visible, re.I)
        and len(normalized.split()) <= 35
    ):
        return True
    if any(
        normalized.startswith(normalize_match_text(prefix))
        for prefix in INSTRUCTION_PREFIXES
    ):
        return True
    if (
        (
            BUGFIX_PREFIX_RE.match(visible)
            or BUGFIX_PREFIX_RE.match(FIX_LABEL_PREFIX_RE.sub("", visible, count=1))
            or BUGFIX_TEXT_RE.search(visible)
        )
        and not SECURITY_FIX_RE.search(visible)
    ):
        return True
    if classification.get("theme_review_reason") == "no_match" and any(
        normalized.startswith(normalize_match_text(prefix))
        for prefix in BOILERPLATE_PREFIXES
    ):
        return True
    return False


TITLE_MAX_CHARS = 90
TITLE_TRUNCATE_AT = 84
TITLE_SHORT_SENTENCE_CHARS = 20
TITLE_SEGMENT_MIN_TOKENS = 3
TITLE_SEGMENT_MIN_CHARS = 16
TITLE_SEGMENT_SEPARATORS = ((": ",), (" — ", " – ", "; "))
TITLE_TRAILING_STOPWORDS = frozenset(
    "a an the to of in on for and or with by from at as is are was were that this its "
    "your their when while so which into via be it".split()
)
_WE_ARE = "(?:today,? )?we(?:[’']re| are)"
_WE_HAVE = "(?:today,? )?we(?:[’']ve| have)"
# Vendor first-person openings with an explicit rewrite into product-as-subject or
# imperative voice. Each rule: (pattern anchored at the start, replacement,
# capitalize the remainder). "{P}" is the product name and "{0}" the captured verb
# in third person singular. Openings without a rule keep the vendor's wording.
VENDOR_VOICE_RULES: tuple[tuple[re.Pattern[str], str, bool], ...] = tuple(
    (re.compile(pattern, re.I), replacement, capitalize)
    for pattern, replacement, capitalize in (
        (rf"^{_WE_ARE} introducing ", "{P} introduces ", False),
        (rf"^{_WE_ARE} launching ", "{P} launches ", False),
        (rf"^{_WE_ARE} rolling out ", "{P} rolls out ", False),
        (rf"^{_WE_ARE} expanding ", "{P} expands ", False),
        (rf"^(?:{_WE_ARE} adding|{_WE_HAVE} (?:also )?added) ", "{P} adds ", False),
        (
            r"^(?:today,? )?we[’']ve (?:also )?(improved|updated|fixed|made|expanded|changed) ",
            "{P} {0} ",
            False,
        ),
        (rf"^{_WE_ARE} (?:now )?(?:excited|happy|thrilled) to (?:announce|share) that ", "", True),
        (
            rf"^{_WE_ARE} (?:now )?(?:excited|happy|thrilled) to "
            r"(introduce|launch|announce|bring|expand) ",
            "{P} {0} ",
            False,
        ),
        (r"^this release (introduces|brings|adds|includes|makes) ", "{P} {0} ", False),
        (r"^you can now ", "", True),
    )
)
GOOD_NEWS_RE = re.compile(r"^good news! ", re.I)
# "We're introducing a plan and updating how ..." would become "{P} introduces a plan
# and updating ...", so a coordinated gerund in the first sentence blocks rewrites.
COORDINATED_GERUND_RE = re.compile(r" and (?:also )?\w+ing\b")
THIRD_PERSON_VERBS = {
    "improved": "improves",
    "updated": "updates",
    "fixed": "fixes",
    "made": "makes",
    "expanded": "expands",
    "changed": "changes",
    "introduce": "introduces",
    "launch": "launches",
    "announce": "announces",
    "bring": "brings",
    "expand": "expands",
}
# A sentence ends at ".", "!" or "?" followed by whitespace and anything but a
# lowercase ASCII letter, or at the end of the text. A "." glued to the next
# character (v2.1.300, $0.50/M, cursor.com) is not a sentence end, except for
# sentences the source ran together ("subscribers.GPT-4", "Windows).Note"): a "." after a
# lowercase letter or ")" and before an uppercase letter, outside inline code, whose
# preceding token has at least 3 letters and no dot of its own ("os.Getenv",
# "fs.Stat" and "process.env.CURSOR_API_KEY" stay intact).
SENTENCE_END_RE = re.compile(r"[.!?](?=\s+[^a-z\s]|\s*$)")
GLUED_SENTENCE_END_RE = re.compile(r"(?<=[a-z)])\.(?=[A-Z])")
GLUED_SENTENCE_MIN_LETTERS = 3
TITLE_ABBREVIATION_RE = re.compile(
    r"(?<![\w.])(?:(?i:e\.g|i\.e|etc|vs|approx|incl)|Mr|Dr|No)$"
)
# Zero-width/format characters and a leading ordered-list marker that
# split_release_lines could not strip because of them ("2<U+2060>. Text ...").
INVISIBLE_CHARS_RE = re.compile("[\u200b-\u200d\u2060\ufeff]")
LIST_MARKER_RE = re.compile(r"^\d{1,3}[.)] ")


def _capitalize_first(text: str) -> str:
    if text[:1].isascii() and text[:1].islower():
        return text[0].upper() + text[1:]
    return text


def _rewrite_vendor_voice(text: str, product_name: str) -> tuple[str, bool]:
    """Return the rewritten text and whether the product became the subject."""
    for pattern, replacement, capitalize in VENDOR_VOICE_RULES:
        match = pattern.match(text)
        if not match:
            continue
        verb = match.group(1).lower() if match.groups() else ""
        prefix = replacement.format(THIRD_PERSON_VERBS.get(verb, verb), P=product_name)
        remainder = text[match.end():]
        return prefix + (_capitalize_first(remainder) if capitalize else remainder), bool(prefix)
    return text, False


def _is_glued_sentence_end(text: str, dot: int) -> bool:
    token = text[:dot].rsplit(" ", 1)[-1]
    return (
        text.count("`", 0, dot) % 2 == 0
        and "." not in token
        and sum(char.isalpha() for char in token) >= GLUED_SENTENCE_MIN_LETTERS
    )


def _sentence_ends(text: str):
    terminators = {match.start() for match in SENTENCE_END_RE.finditer(text)}
    terminators.update(
        match.start()
        for match in GLUED_SENTENCE_END_RE.finditer(text)
        if _is_glued_sentence_end(text, match.start())
    )
    for position in sorted(terminators):
        # Punctuation inside inline code ("`<!-- ... -->`") never ends a sentence.
        if text.count("`", 0, position) % 2:
            continue
        if not TITLE_ABBREVIATION_RE.search(text[:position]):
            yield position + 1


def _first_sentence(text: str) -> str:
    return text[: next(_sentence_ends(text), len(text))]


def _drop_product_mentions(text: str, product_name: str) -> str:
    """Drop " in {P}" when the product is already the subject of the title."""
    if not product_name:
        return text
    return re.sub(rf" in {re.escape(product_name)}(?=$|[.,;:!?)]|\s[a-z—–])", "", text)


def _strip_terminator(text: str) -> str:
    return text[:-1].rstrip() if text.endswith((".", ":")) else text


def _balanced_backticks(text: str) -> bool:
    return text.count("`") % 2 == 0


def _unmatched_opener(text: str) -> int:
    """Index of the first "(" or curly/straight double quote left open, or -1."""
    stack: list[int] = []
    curly: list[int] = []
    straight: list[int] = []
    for index, char in enumerate(text):
        if char == "(":
            stack.append(index)
        elif char == ")" and stack:
            stack.pop()
        elif char == "“":
            curly.append(index)
        elif char == "”" and curly:
            curly.pop()
        elif char == '"':
            if straight:
                straight.pop()
            else:
                straight.append(index)
    open_positions = stack[:1] + curly[:1] + straight[:1]
    return min(open_positions) if open_positions else -1


def _truncate_title(text: str) -> str:
    cut = text.rfind(" ", 0, TITLE_TRUNCATE_AT + 1)
    head = text[:cut] if cut > 0 else text[:TITLE_TRUNCATE_AT]
    stopword_passes = 0
    while True:
        head = head.rstrip(" ,;:—–-")
        opener = _unmatched_opener(head)
        if not _balanced_backticks(head):
            candidate = head[: head.rfind("`")]
        elif opener >= 0:
            candidate = head[:opener]
        elif head[-1:] and not (head[-1].isalnum() or head[-1] in ")`'") and " " in head:
            # Drop a dangling last token ("e.g.", "&", "/", "->") instead of ending on it.
            candidate = head[: head.rfind(" ")]
        elif (
            stopword_passes < 2
            and " " in head
            and head.rsplit(" ", 1)[1].lower() in TITLE_TRAILING_STOPWORDS
        ):
            stopword_passes += 1
            candidate = head[: head.rfind(" ")]
        else:
            break
        if not any(char.isalnum() for char in candidate):
            break
        head = candidate
    return head + "…"


def card_title(line: str, product_name: str) -> str:
    """Return a deterministic, readable Change Card title for one changelog line.

    Card identity (card_id, slug, file path) is derived from the raw line elsewhere;
    the title is presentation only.
    """
    text = re.sub(r"\s+", " ", INVISIBLE_CHARS_RE.sub("", line)).strip()
    text = LIST_MARKER_RE.sub("", text)
    good_news = GOOD_NEWS_RE.match(text)
    if good_news:
        text = text[good_news.end():]
    product_subject = False
    if not COORDINATED_GERUND_RE.search(_first_sentence(text)):
        text, product_subject = _rewrite_vendor_voice(text, product_name)

    ends = list(_sentence_ends(text))[:2]
    sentence = _strip_terminator(text[: ends[0]] if ends else text)
    if len(sentence) < TITLE_SHORT_SENTENCE_CHARS and len(ends) > 1:
        joined = _strip_terminator(text[: ends[1]])
        if len(joined) <= TITLE_MAX_CHARS:
            sentence = joined
    if product_subject:
        sentence = _drop_product_mentions(sentence, product_name)
    title = sentence if len(sentence) <= TITLE_MAX_CHARS else ""
    for separators in TITLE_SEGMENT_SEPARATORS if not title else ():
        positions = [sentence.find(sep) for sep in separators if sep in sentence]
        segment = sentence[: min(positions)].rstrip() if positions else ""
        if (
            len(segment.split()) >= TITLE_SEGMENT_MIN_TOKENS
            and TITLE_SEGMENT_MIN_CHARS <= len(segment) <= TITLE_MAX_CHARS
            and _balanced_backticks(segment)
        ):
            title = segment
            break
    title = _strip_terminator(title or _truncate_title(sentence)).strip()
    return title[:TITLE_MAX_CHARS].rstrip()


# ---------------------------------------------------------------------------
# Card definition (W2 P3): a card is one announced change that can be understood on
# its own. Cards follow the structure of the release body instead of one line each:
#
# - a body is parsed into heading, paragraph and bullet blocks;
# - a feature heading and its text become one card;
# - bullets under a scope heading (Web, iOS, Plus, ...) and up to eight preamble
#   bullets become one card each, as before; bullets that complete a paragraph ending
#   with a colon stay in that paragraph's card unless they have a theme of their own;
# - consecutive preamble paragraphs about one theme become one card;
# - list mode (generic headings, long preamble lists, GitHub releases) keeps each
#   line classified on its own, publishes high-signal lines as standalone cards and
#   folds the rest into one digest card per theme per release; lines without a
#   confident theme take the holding theme and fold into an "Other changes" digest.
#
# Review decisions keyed by a line's identity apply to that line wherever it lands;
# a decision keyed by a card's identity applies to the whole card.
#
# Heading levels are treated alike: every heading closes the previous section. Each
# collected body uses a single heading level (Cursor "#", Claude Code "##", ChatGPT
# "###" or "####"), so nested sections do not occur in the archive.

HEADING_LINE_RE = re.compile(r"^(#{1,6})\s*(\S.*)$")
# Cursor flattens collapsible groups ("Improvements (29)↓↑", "Patches↓↑") into a line.
COLLAPSIBLE_GROUP_RE = re.compile(r"^(?P<label>\S.*?)(?:\s*\(\d+\))?\s*↓↑$")
BULLET_MARKER_RE = re.compile(r"^(?:[-*•]\s+|\d{1,3}[.)]\s+)")
# Cursor drops list markup; a short label before a colon still marks a list item
# ("Apply button: ...", "0.47.2: ...").
# A sentence opening ("We're introducing dots: ...") is not a label.
LABELLED_ITEM_RE = re.compile(
    r"^(?!(?i:we|you|i|our|it|this|these|there|here|today)\b)"
    r"[A-Z0-9\"“`@/][^:.!?]{0,40}:\s+\S"
)
LABELLED_ITEM_MAX_WORDS = 5
# Version-prefixed patch notes ("0.47.1: ...", "2.0.1-2.0.28: ...", "0.48.1 - ...").
VERSION_ITEM_RE = re.compile(r"^v?\d+(?:\.\d+)+(?:\s*[-–]\s*v?\d+(?:\.\d+)+)?\s*[:\-–]\s*\S")
PATCH_GROUP_RE = re.compile(r"^patch(?:es)?$", re.I)
# Flattened code lines that end inside an object or argument list ('model: { id: "x" },').
CODE_FRAGMENT_RE = re.compile(r"[,{\[(]$")
# Emoji remnants such as a lone U+FE0F before a Cursor heading.
HEADING_DECORATION_RE = re.compile(r"^[^\w/“\"'`(]+")
# Headings that group unrelated items or describe rollout rather than name a change.
SECTION_GENERIC_RE = re.compile(
    r"^(?:availability\b.*|other (?:improvements|updates|changes)\b.*|"
    r"additional improvements\b.*|(?:.* )?quality[- ]of[- ]life improvements|"
    r"stability improvements|regressions|get(?:ting)? started|what[’']?s next|"
    r"why we[’']re making this change|please give us feedback\W*|what it reports)[:.!]?$",
    re.I,
)
_SCOPE_LABEL = (
    r"(?:(?:linux|windows|macos|mac) desktop|desktop apps?|mobile apps?|web|ios|ipados|"
    r"android|desktop|mobile|macos|mac|windows|linux|ipad|iphone|chromeos|"
    r"free|go|plus|pro|team|business|enterprise|edu|education|healthcare)"
)
# Platform and plan labels: "iOS", "Web, iOS, and Android", "macOS and Windows".
SCOPE_HEADING_RE = re.compile(
    rf"^(?:chatgpt )?{_SCOPE_LABEL}"
    rf"(?:(?:\s*,\s*(?:and\s+|&\s+)?|\s+(?:and|&)\s+|\s*/\s*){_SCOPE_LABEL})*"
    r"(?: (?:users?|apps?|plans?))?:?$",
    re.I,
)
PREAMBLE_BULLET_LIMIT = 8
AVAILABILITY_PARAGRAPH_RE = re.compile(r"^(?:available|rolling out|now available)\b", re.I)
ROLLOUT_SUBJECT_RE = re.compile(r"^[A-Z][^.:]{0,60} (?:is|are) (?:now )?(?:rolling out|available)\b")
# B+ pilot: list lines that announce something on their own and stay standalone cards.
HIGH_SIGNAL_RE = re.compile(
    r"^(?:introducing |added `?/[a-z][a-z0-9-]*`? |new: |you can now |"
    r"[^.]{0,100}?\bnow (?:on|enabled|runs?) by default\b|"
    r"[^.]{0,100}?\bis now (?:generally available|GA)\b)",
    re.I,
)
HIGH_SIGNAL_AVAILABLE_RE = re.compile(r"^[^.]{0,100}?\bnow available\b", re.I)
HIGH_SIGNAL_AVAILABLE_MIN_CHARS = 60
VERSIONED_TITLE_RE = re.compile(r"^v?\d+(?:\.\d+)+(?:[- ]?\w+)?(?:\s*\([^)]*\))?$", re.I)
TITLE_DATE_SUFFIX_RE = re.compile(r"\s*\(\d{4}-\d{2}-\d{2}\)$")
# Cursor changelog URLs name versioned releases "0-48-x" or "1-1".
CURSOR_VERSION_SLUG_RE = re.compile(r"^\d+(?:-\d+)*(?:-x)?$")
DIGEST_LABEL_MAX_CHARS = 40
# Holding theme (themes.yaml ``status: holding``): list lines without a confident theme
# are published in one "Other changes" digest per release instead of the review queue.
# Holding cards appear on Release and product pages, never on theme pages or the home page.
UNCATEGORIZED_THEME = "uncategorized"
HOLDING_THEMES = frozenset({UNCATEGORIZED_THEME})

KIND_LABELS = {
    "launch": "Launch",
    "expansion": "Expansion",
    "pricing": "Pricing",
    "policy": "Policy",
    "fix": "Fix",
    "digest": "Digest",
    "change": "Change",
}
KINDS = frozenset(KIND_LABELS)
KIND_FIX_RE = re.compile(r"^(?:fixed\b|fix:)", re.I)
# Feature headings that name an improvement or a fix rather than a new capability.
KIND_CHANGE_HEADING_RE = re.compile(
    r"^(?:improved|improvements?|improving|better|faster|updated|updates?)\b", re.I
)
KIND_FIX_HEADING_RE = re.compile(r"^(?:fixed|fix(?:es)?)\b", re.I)
KIND_POLICY_RE = re.compile(
    r"\b(?:deprecat\w*|retir(?:e|es|ed|ing|ement)|sunset\w*|end[- ]of[- ]life|"
    r"no longer (?:be )?(?:available|supported|offered)|"
    r"(?:rate|usage|message|request|weekly|daily|hourly|monthly)(?: \w+)? (?:limits?|caps?)|"
    r"quotas?|parental controls?|age (?:prediction|verification|assurance|requirements?)|"
    r"teens?)\b",
    re.I,
)
KIND_EXPANSION_START_RE = re.compile(
    r"^(?:available\b|rolling out\b|now available in\b|"
    r"(?:good news! )?(?:(?:today,? )?we(?:[’']re| are) )?(?:now )?expanding\b)",
    re.I,
)
_KIND_REGIONS = (
    r"(?:\d+ (?:additional |more |new )?(?:countries|markets|regions)|"
    r"(?:additional|more|new) (?:countries|markets|regions)|countries and regions|"
    r"india|brazil|indonesia|japan|korea|europe|the eu|the eea|the uk|united kingdom|"
    r"canada|mexico|latin america|africa|southeast asia|australia|philippines|vietnam|"
    r"thailand|malaysia|singapore|turkey|pakistan|bangladesh|nigeria|egypt)"
)
_KIND_SURFACES = (
    r"(?:ios|android|web|desktop|macos|mac|windows|linux|mobile|ipad|iphone|bedrock|"
    r"vertex(?: ai)?|foundry|jetbrains|slack|"
    r"(?:free|go|plus|pro|team|business|enterprise|edu|max) "
    r"(?:users?|plans?|subscribers?|customers?|workspaces?))"
)
# "now available" scoped to new places, platforms or plans, without a new capability.
KIND_SCOPED_AVAILABILITY_RE = re.compile(
    rf"\bnow (?:available|rolling out)\b[^.]{{0,60}}?\b(?:in|on|to|for|across)\b"
    rf"[^.]{{0,60}}?\b(?:{_KIND_REGIONS}|{_KIND_SURFACES})\b|"
    rf"\b(?:launch(?:es|ed|ing)?|available|rolling out)\b[^.]{{0,100}}?"
    rf"\b(?:in|to|across) (?:{_KIND_REGIONS})\b",
    re.I,
)
KIND_LAUNCH_RE = re.compile(
    r"^(?:introducing|announcing|meet)\b|"
    r"^(?:today,? )?we(?:[’']re| are) (?:now )?(?:launching|introducing|announcing|releasing)\b|"
    r"^this release (?:introduces|brings|adds)\b|"
    r"^(?:today,? )?we(?:[’']re| are) (?:excited|happy|thrilled) to "
    r"(?:announce|introduce|launch|bring)\b|"
    r"\b(?:is|are) now (?:generally )?available\b|^now available\b",
    re.I,
)


def clean_block_text(text: str) -> str:
    """Collapse whitespace and drop zero-width characters, as ``card_title`` does."""
    return re.sub(r"\s+", " ", INVISIBLE_CHARS_RE.sub("", text)).strip()


def parse_release_blocks(body: str) -> list[dict[str, Any]]:
    """Ordered ``heading``, ``paragraph`` and ``bullet`` blocks of a release body.

    Fenced code, flattened code samples and lines shorter than a candidate line are
    dropped. Headings match ``^#{1,6}\\s*\\S`` (Cursor writes ``#Heading``); Cursor's
    collapsible group lines ("Improvements (29)↓↑") are headings too.
    """
    blocks: list[dict[str, Any]] = []
    for stripped in _unfenced_lines(body):
        line = clean_block_text(stripped)
        if not line:
            continue
        heading = HEADING_LINE_RE.match(line)
        if heading:
            text = HEADING_DECORATION_RE.sub("", heading.group(2)).strip()
            if text:
                blocks.append({"type": "heading", "level": len(heading.group(1)), "text": text})
            continue
        group = COLLAPSIBLE_GROUP_RE.match(line)
        if group:
            blocks.append(
                {"type": "heading", "level": 0, "text": group.group("label"), "collapsible": True}
            )
            continue
        marker = BULLET_MARKER_RE.match(line)
        text = line[marker.end():].strip() if marker else line
        if CODE_SAMPLE_RE.match(text) or CODE_FRAGMENT_RE.search(text) or len(text) < MIN_LINE_CHARS:
            continue
        blocks.append({"type": "bullet" if marker or is_labelled_item(text) else "paragraph",
                       "text": text})
    return blocks


def is_labelled_item(text: str) -> bool:
    """A list item whose markup was lost: a short label and a colon, or a version."""
    match = LABELLED_ITEM_RE.match(text)
    label = text[: text.find(":")] if match else ""
    return bool(match and len(label.split()) <= LABELLED_ITEM_MAX_WORDS) or bool(
        VERSION_ITEM_RE.match(text)
    )


def heading_kind(text: str) -> str:
    """``generic``, ``scope`` (platform or plan label) or ``feature``."""
    visible = text.strip()
    if (
        GENERIC_HEADING_RE.fullmatch(visible)
        or SECTION_GENERIC_RE.fullmatch(visible)
        or VERSION_ONLY_RE.fullmatch(visible)
        or LOW_SIGNAL_RE.fullmatch(visible)
        or BUGFIX_PREFIX_RE.match(visible)
    ):
        return "generic"
    if SCOPE_HEADING_RE.fullmatch(visible):
        return "scope"
    return "feature"


def release_sections(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """A preamble plus one section per heading, each holding its blocks.

    A collapsible "Patches" group holds only version-prefixed lines; the first other
    line closes it and the text continues the last section that was not a group.
    """
    sections = [{"kind": "preamble", "heading": "", "blocks": []}]
    anchor = current = sections[0]
    for block in blocks:
        if block["type"] == "heading":
            collapsible = bool(block.get("collapsible"))
            current = {
                "kind": "generic" if collapsible else heading_kind(block["text"]),
                "heading": block["text"],
                "blocks": [],
                "patches": collapsible and bool(PATCH_GROUP_RE.match(block["text"])),
            }
            sections.append(current)
            if not collapsible:
                anchor = current
            continue
        if current.get("patches") and current["blocks"] and not VERSION_ITEM_RE.match(block["text"]):
            current = anchor
        current["blocks"].append(block)
    return sections


def is_availability_paragraph(text: str) -> bool:
    """A rollout or availability note: "Available ...", "Rolling out ...", "Now available
    ...", or "<Subject> is/are (now) rolling out/available ..."; not a lead-in."""
    return not text.rstrip().endswith(":") and bool(
        AVAILABILITY_PARAGRAPH_RE.match(text) or ROLLOUT_SUBJECT_RE.match(text)
    )


def is_high_signal(text: str) -> bool:
    """B+ pilot rule: a list line that is a standalone announcement."""
    return bool(
        HIGH_SIGNAL_RE.match(text)
        or (
            len(text) >= HIGH_SIGNAL_AVAILABLE_MIN_CHARS
            and HIGH_SIGNAL_AVAILABLE_RE.match(text)
        )
    )


def card_kind(texts: list[str], theme: str, *, feature: bool = False) -> str:
    """Kind of a non-digest card from its lead text (heading and first paragraph).

    Precedence: fix, policy, expansion, launch wording, pricing theme, feature section.
    A feature section is a fix or a change when its heading opens with a fix word
    ("Fixed …") or an improvement word ("Improved …", "Faster …", "Updates to …").
    """
    if feature and texts and texts[0]:
        heading = texts[0].strip()
        if KIND_FIX_HEADING_RE.match(heading):
            return "fix"
        if KIND_CHANGE_HEADING_RE.match(heading):
            return "change"
    leads = [_first_sentence(text) for text in texts if text]
    if not feature and leads and KIND_FIX_RE.match(FIX_LABEL_PREFIX_RE.sub("", leads[0], count=1)):
        return "fix"
    if any(KIND_POLICY_RE.search(lead) for lead in leads):
        return "policy"
    if any(
        KIND_EXPANSION_START_RE.match(lead) or KIND_SCOPED_AVAILABILITY_RE.search(lead)
        for lead in leads
    ):
        return "expansion"
    if any(KIND_LAUNCH_RE.search(lead) for lead in leads):
        return "launch"
    if theme == "pricing-model":
        return "pricing"
    return "launch" if feature else "change"


def informative_release_title(title: str) -> bool:
    """A release title that names the change: not generic, a version or a fix label."""
    visible = title.strip()
    return bool(visible) and not (
        GENERIC_HEADING_RE.fullmatch(visible)
        or VERSION_ONLY_RE.fullmatch(visible)
        or VERSIONED_TITLE_RE.fullmatch(visible)
        or LOW_SIGNAL_RE.fullmatch(visible)
        or BUGFIX_PREFIX_RE.match(visible)
    )


def release_label(release: dict[str, Any]) -> str:
    """Short release name: the version of a GitHub release, else the title."""
    if release.get("source_type") == "github_releases" and release.get("version"):
        return str(release["version"]).strip()
    return TITLE_DATE_SUFFIX_RE.sub("", str(release.get("title") or "")).strip()


def digest_release_label(release: dict[str, Any]) -> str:
    """Release name in digest titles: a GitHub version, a Cursor version taken from the
    changelog URL ("0-48-x" -> "0.48.x"), else the title cut at 40 characters."""
    if release.get("source_type") == "github_releases" and release.get("version"):
        return str(release["version"]).strip()
    if release.get("source_type") == "cursor_changelog":
        slug = str(release.get("source_url") or "").rstrip("/").rsplit("/", 1)[-1]
        if CURSOR_VERSION_SLUG_RE.match(slug):
            return slug.replace("-", ".")
    return _shorten_label(release_label(release), DIGEST_LABEL_MAX_CHARS)


def _shorten_label(label: str, budget: int) -> str:
    """Cut ``label`` on a word boundary so that it and "…" fit in ``budget``."""
    if len(label) <= budget:
        return label
    head = label[: max(budget - 1, 1)]
    if label[len(head)] != " " and " " in head:
        head = head[: head.rfind(" ")]
    while " " in head and head.rsplit(" ", 1)[1].lower() in TITLE_TRAILING_STOPWORDS:
        head = head[: head.rfind(" ")]
    return head.rstrip(" ,;:—–-&/") + "…"


def digest_title(count: int, theme_display: str, label: str) -> str:
    prefix = f"{count} {theme_display} changes in "
    return prefix + _shorten_label(label, TITLE_MAX_CHARS - len(prefix))


def theme_display_name(theme: str, themes: dict[str, dict[str, Any]]) -> str:
    return str(themes.get(theme, {}).get("display_name") or theme.replace("-", " ").title())


def line_classification(
    text: str,
    themes: dict[str, dict[str, Any]],
    review_decision: str | None = None,
    product: str | None = None,
) -> dict[str, Any] | None:
    """Theme of one line: review decision, semantic override, skip rules, hint.

    Returns None when the skip rules reject the line.
    """
    classification = classify_theme(text, themes)
    if review_decision:
        return {
            "theme": review_decision,
            "theme_resolution": "manual-backfill-review-v1",
            "theme_matches": classification.get("theme_matches", []),
        }
    override = semantic_preclassification_override(text, themes, product)
    if override:
        classification = {
            "theme": override,
            "theme_resolution": "manual-semantic-rule-v2",
            "theme_matches": classification.get("theme_matches", []),
        }
    if should_skip_line(text, classification):
        return None
    if classification["theme"] == "__candidate__":
        hint = semantic_theme_hint(text, themes)
        if hint:
            classification = {
                "theme": hint,
                "theme_resolution": "manual-semantic-rule-v1",
                "theme_matches": classification.get("theme_matches", []),
            }
    return classification


def feature_classification(
    heading: str,
    first_text: str,
    themes: dict[str, dict[str, Any]],
    product: str | None = None,
) -> dict[str, Any]:
    """Theme of a feature section: the heading alone when it matches, else heading + text."""
    override = semantic_preclassification_override(heading, themes, product)
    heading_only = classify_theme(heading, themes)
    if override:
        return {
            "theme": override,
            "theme_resolution": "manual-semantic-rule-v2",
            "theme_matches": heading_only.get("theme_matches", []),
        }
    if heading_only["theme"] != "__candidate__":
        return heading_only
    joined = f"{heading}. {first_text}" if first_text else heading
    classification = classify_theme(joined, themes)
    override = semantic_preclassification_override(joined, themes, product)
    if override:
        return {
            "theme": override,
            "theme_resolution": "manual-semantic-rule-v2",
            "theme_matches": classification.get("theme_matches", []),
        }
    if classification["theme"] == "__candidate__":
        hint = semantic_theme_hint(joined, themes)
        if hint:
            return {
                "theme": hint,
                "theme_resolution": "manual-semantic-rule-v1",
                "theme_matches": classification.get("theme_matches", []),
            }
    return classification


def matched_themes(classification: dict[str, Any]) -> set[str]:
    return {classification["theme"]} | {
        match["theme"] for match in classification.get("theme_matches", [])
    }


def same_theme_run(lead: dict[str, Any], follower: dict[str, Any]) -> bool:
    """Whether a following line continues a run: it has no theme of its own, or one
    side's theme is among the other's theme matches."""
    return (
        follower["theme"] == "__candidate__"
        or lead["theme"] in matched_themes(follower)
        or follower["theme"] in matched_themes(lead)
    )


class _ReleaseCards:
    """Cards of one release, built section by section in body order."""

    def __init__(
        self,
        release: dict[str, Any],
        themes: dict[str, dict[str, Any]],
        review_decisions: dict[str, str],
    ) -> None:
        self.release = release
        self.themes = themes
        self.decisions = review_decisions
        self.source_release = release.get("release_id") or (
            f"{release['product']}-{release['date']}-"
            f"{slugify(release.get('version') or release['title'])}"
        )
        self.scoped = (
            self.source_release
            if release.get("release_id") and release.get("source_type") != "fixture"
            else None
        )
        self.used: set[str] = set()
        self.drafts: list[dict[str, Any]] = []
        self.list_items: list[dict[str, Any]] = []
        self.position = 0

    def identity(self, quotes: list[str]) -> str:
        return card_id_for(
            self.release["product"],
            self.release["date"],
            "\n".join(quotes),
            source_release=self.scoped,
        )

    def item(self, block: dict[str, Any]) -> dict[str, Any] | None:
        """One classified line; None when skipped, reviewed as skip or repeated."""
        self.position += 1
        text = block["text"]
        line_id = self.identity([text])
        if line_id in self.used:
            return None
        decision = self.decisions.get(line_id)
        if decision == "skip":
            return None
        classification = line_classification(text, self.themes, decision, self.release.get("product"))
        if classification is None:
            return None
        self.used.add(line_id)
        return {
            "text": text,
            "type": block["type"],
            "classification": classification,
            "order": self.position,
        }

    def add(self, origin: str, items: list[dict[str, Any]], classification: dict[str, Any], **extra):
        self.drafts.append(
            {"origin": origin, "items": items, "classification": classification,
             "order": items[0]["order"] if items else self.position, **extra}
        )

    def single(self, item: dict[str, Any], origin: str, scope: str = "") -> None:
        self.add(origin, [item], item["classification"], scope=scope)

    def feature_section(self, section: dict[str, Any]) -> None:
        self.position += 1
        order = self.position
        items = [item for block in section["blocks"] if (item := self.item(block))]
        heading = section["heading"]
        first = items[0]["text"] if items else ""
        classification = feature_classification(heading, first, self.themes, self.release.get("product"))
        if not items:
            heading_id = self.identity([heading])
            if heading_id in self.used or self.decisions.get(heading_id) == "skip":
                return
            self.used.add(heading_id)
            items = [{"text": heading, "type": "heading", "classification": classification,
                      "order": order}]
        self.drafts.append(
            {"origin": "feature", "items": items, "classification": classification,
             "order": order, "heading": heading}
        )

    def paragraph_runs(self, items: list[dict[str, Any]]) -> None:
        """Group consecutive paragraphs about one theme into runs.

        A paragraph continues the run when the run's theme is among the paragraph's
        theme matches (or the other way round), so one stray keyword does not split a
        description. Unclassified paragraphs have no theme of their own and stay with
        their neighbours; a run of unclassified paragraphs waits for theme review.
        """
        runs: list[dict[str, Any]] = []
        for item in items:
            classification = item["classification"]
            current = runs[-1] if runs else None
            if current and (
                current["classification"]["theme"] == "__candidate__"
                or same_theme_run(current["classification"], classification)
            ):
                if current["classification"]["theme"] == "__candidate__":
                    current["classification"] = classification
                current["items"].append(item)
            else:
                runs.append({"classification": classification, "items": [item]})
        for run in runs:
            self.add("paragraphs", run["items"], run["classification"])

    def preamble(self, section: dict[str, Any]) -> None:
        """Preamble paragraphs form theme runs; bullets become cards or list items.

        Bullets right after a paragraph that ends with a colon ("GPT-4 has enhanced
        capabilities in:") complete that paragraph and stay in its card when they have no
        theme of their own or the paragraph's theme; a bullet with another theme (or a
        reviewed theme) still becomes its own card.

        An availability or rollout paragraph ("Dots are rolling out gradually to ...")
        is added as evidence to the previous card with a theme, so it stays published;
        without such a card it is handled like any other paragraph.
        """
        blocks = section["blocks"]
        lead_in: set[int] = set()
        for index, block in enumerate(blocks):
            if block["type"] == "paragraph" and block["text"].endswith(":"):
                follower = index + 1
                while follower < len(blocks) and blocks[follower]["type"] == "bullet":
                    lead_in.add(follower)
                    follower += 1
        bullets = sum(
            block["type"] == "bullet" and index not in lead_in
            for index, block in enumerate(blocks)
        )
        list_bullets = bullets > PREAMBLE_BULLET_LIMIT
        paragraphs: list[dict[str, Any]] = []
        lead: dict[str, Any] | None = None
        owner: dict[str, Any] | None = None  # item of the last card with a theme
        for index, block in enumerate(blocks):
            attach = index in lead_in and lead is not None
            if block["type"] != "paragraph" and not attach:
                self.paragraph_runs(paragraphs)
                paragraphs = []
            item = self.item(block)
            if block["type"] == "paragraph":
                lead = item if item is not None and block["text"].endswith(":") else None
            elif not attach:
                lead = None
            if item is None:
                continue
            if (
                block["type"] == "paragraph"
                and owner is not None
                and is_availability_paragraph(item["text"])
                and item["classification"].get("theme_resolution") != "manual-backfill-review-v1"
            ):
                owner.setdefault("attached", []).append(item)
            elif attach and item["classification"]["theme"] in {
                "__candidate__", lead["classification"]["theme"]
            }:
                lead.setdefault("attached", []).append(item)
            else:
                if block["type"] == "paragraph":
                    paragraphs.append(item)
                elif list_bullets and not attach:
                    self.list_items.append(item)
                else:
                    self.single(item, "bullet")
                if item["classification"]["theme"] != "__candidate__":
                    owner = item
        self.paragraph_runs(paragraphs)

    def list_mode(self) -> None:
        """High-signal lines stay standalone; the other lines of one theme form a digest.

        A line without a confident theme takes the holding theme when the vocabulary
        declares it, so list items never wait in the review queue: they join the
        release's "Other changes" digest (or stay standalone like any other line).
        """
        holding = UNCATEGORIZED_THEME in self.themes
        by_theme: dict[str, list[dict[str, Any]]] = {}
        for item in self.list_items:
            if holding and item["classification"]["theme"] == "__candidate__":
                item["classification"] = {**item["classification"], "theme": UNCATEGORIZED_THEME}
            theme = item["classification"]["theme"]
            if theme == "__candidate__" or is_high_signal(item["text"]):
                self.single(item, "list")
            else:
                by_theme.setdefault(theme, []).append(item)
        for theme, items in by_theme.items():
            if len(items) == 1:
                self.single(items[0], "list")
            else:
                self.add("digest", items, {"theme": theme})

    def build(self, sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
        flat_list = self.release.get("source_type") == "github_releases"
        for section in sections:
            if flat_list or section["kind"] == "generic":
                self.list_items.extend(
                    item for block in section["blocks"] if (item := self.item(block))
                )
            elif section["kind"] == "feature":
                self.feature_section(section)
            elif section["kind"] == "scope":
                for block in section["blocks"]:
                    if item := self.item(block):
                        self.single(item, "scope", scope=section["heading"])
            else:
                self.preamble(section)
        self.list_mode()
        cards = []
        seen: set[str] = set()
        for draft in sorted(self.drafts, key=lambda draft: draft["order"]):
            card = self.card(draft)
            if card is not None and card["card_id"] not in seen:
                seen.add(card["card_id"])
                cards.append(card)
        title = release_label(self.release)
        if (
            len(cards) == 1
            and cards[0].pop("_origin") == "paragraphs"
            and informative_release_title(title)
        ):
            card = cards[0]
            card["title"] = card_title(title, self.release["product_name"])
            card["kind"] = card_kind([title, card["evidence"][0]["quote"]], card["theme"])
        for card in cards:
            card.pop("_origin", None)
        return cards

    def card(self, draft: dict[str, Any]) -> dict[str, Any] | None:
        release = self.release
        product_name = release["product_name"]
        # Lines attached to an item (lead-in bullets, availability notes) follow it; they
        # may be attached after the draft was created, so they are read only here.
        quotes = [
            part["text"]
            for item in draft["items"]
            for part in (item, *item.get("attached", ()))
        ]
        card_id = self.identity(quotes)
        classification = dict(draft["classification"])
        decision = self.decisions.get(card_id)
        if decision == "skip":
            return None
        if decision and classification.get("theme_resolution") != "manual-backfill-review-v1":
            classification = {
                "theme": decision,
                "theme_resolution": "manual-backfill-review-v1",
                "theme_matches": classification.get("theme_matches", []),
            }
        theme = classification["theme"]
        origin = draft["origin"]
        primary = quotes[0]
        if origin == "digest":
            # "12 Agent Mode changes in v2.1.300"; a holding digest reads "12 other changes".
            display = "other" if theme in HOLDING_THEMES else theme_display_name(theme, self.themes)
            title = digest_title(len(quotes), display, digest_release_label(release))
            slug_source = title
            kind = "digest"
            impact = "incremental"
            description = f"{product_name} — {release['title']}: {len(quotes)} {display} changes"
        elif origin == "feature":
            heading = draft["heading"]
            body_text = primary if draft["items"][0]["type"] != "heading" else ""
            title = card_title(heading, product_name)
            slug_source = heading
            kind = card_kind([heading, body_text], theme, feature=True)
            impact = choose_impact(f"{heading}. {body_text}" if body_text else heading)
            description = f"{product_name} — {release['title']}: {primary}"
        else:
            title = card_title(primary, product_name)
            slug_source = primary
            kind = card_kind([primary], theme)
            impact = choose_impact(primary)
            description = f"{product_name} — {release['title']}: {primary}"
        card = {
            "type": "change",
            "card_id": card_id,
            "product": release["product"],
            "product_name": product_name,
            "source_release": self.source_release,
            "date": release["date"],
            "title": title,
            "slug": slugify(slug_source)[:80].strip("-"),
            "theme": theme,
            "kind": kind,
            "impact": impact,
            "description": description,
            "comparison": "",
            "evidence": [
                {"source_release": release.get("source_url", ""), "quote": quote}
                for quote in quotes
            ],
            "extractor_version": "fallback-v5" if self.scoped else "fallback-v1",
            "source_type": release.get("source_type", "unknown"),
            "_origin": origin,
        }
        if draft.get("scope"):
            card["scope"] = draft["scope"]
        card.update({key: value for key, value in classification.items() if key != "theme"})
        if impact in {"significant", "paradigm-shift"}:
            card["ai_generated"] = True
            card["confidence"] = "low"
        return card


def extract_cards_from_release(
    release: dict[str, Any],
    themes: dict[str, dict[str, Any]],
    review_decisions: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Change Cards of one release under the W2 card definition (see above)."""
    body = str(release.get("body") or "")
    builder = _ReleaseCards(release, themes, review_decisions or {})
    if split_release_lines(body):
        sections = release_sections(parse_release_blocks(body))
    elif release.get("source_type") in {None, "fixture"}:
        sections = [{"kind": "preamble", "heading": "",
                     "blocks": [{"type": "paragraph", "text": str(release["title"])}]}]
    else:
        return []
    return builder.build(sections)


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
