# ChronoLog MVP Implementation Plan

> **Historical reference (status reviewed 2026-10-13):** This plan records the original Phase 1 implementation work, which now has code and generated artifacts. Its checkboxes and embedded examples are retained as history, not as a current status tracker or operating manual. The M1 reliability milestone has passed [acceptance](../../acceptance/m1-2026-10-13.md); the three-source MVP has also passed [M2 content acceptance](../../acceptance/m2-2026-10-13.md), including the user's human review. Use the [current development and acceptance plan](../../development-plan-2026-10-13.md) for follow-up work; run pipeline examples only in a disposable repository copy.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Phase 1 ChronoLog MVP: a local Obsidian Vault plus Python pipeline that collects tier-1 changelog data, creates validated Change Cards, analyzes product/theme evolution, renders Markdown, and builds with Quartz.

**Architecture:** The repository root is the Obsidian Vault. Python scripts under `_scripts/` own data collection, extraction, validation, analysis, silence detection, and deterministic Markdown rendering. JSON files in `_pipeline/` are rebuildable intermediates; durable product content is Markdown in `Products/`, `Releases/`, `Changes/`, `Themes/`, `Alerts/`, and `index.md`.

**Tech Stack:** Python 3.11+, pytest, PyYAML, httpx, feedparser, python-frontmatter, Node.js 20+, Quartz v4.

---

## File Structure

- Create `_scripts/__init__.py`: makes `_scripts` importable in tests.
- Create `_scripts/common.py`: shared dataclasses, JSON/YAML IO, slugging, hashing, date parsing, frontmatter helpers, machine region helpers.
- Create `_scripts/collect.py`: fixture, GitHub Releases, and RSS collection into `_pipeline/<run-id>/01-collected/releases.json`.
- Create `_scripts/extract.py`: deterministic fallback extraction, theme normalization, stable `card_id`.
- Create `_scripts/validate.py`: round-1 JSON schema validation and DLQ isolation.
- Create `_scripts/analyze_a.py`: per-product eras, `evolves_from`, and `verbosity_baseline`.
- Create `_scripts/analyze_b.py`: per-theme related changes and tracked-products-only diffusion.
- Create `_scripts/silence_monitor.py`: pure Python silence detection.
- Create `_scripts/writer.py`: Markdown rendering with machine region ownership and `machine_hash`.
- Create `_scripts/run_pipeline.py`: local Phase 1 orchestrator.
- Create `_scripts/sources.yaml`: 5-8 tier-1 source declarations plus fixture metadata.
- Create `_scripts/themes.yaml`: official theme vocabulary and aliases.
- Create `tests/fixtures/releases.json`: deterministic offline release fixture.
- Create `tests/test_common.py`, `tests/test_extract.py`, `tests/test_validate.py`, `tests/test_analyze.py`, `tests/test_silence_monitor.py`, `tests/test_writer.py`, `tests/test_pipeline.py`.
- Create `pyproject.toml`: Python dependencies and pytest config.
- Create `package.json`, `quartz.config.ts`, `quartz.layout.ts`: minimal Quartz setup.
- Create `.gitignore`: excludes `_pipeline/`, `node_modules/`, Quartz build output, caches, and `.DS_Store`.
- Create `README.md`: setup, fixture pipeline, live collection, and Quartz preview commands.

## Task 1: Project Scaffold And Fixture Data

**Files:**
- Create: `pyproject.toml`
- Create: `.gitignore`
- Create: `_scripts/__init__.py`
- Create: `_scripts/sources.yaml`
- Create: `_scripts/themes.yaml`
- Create: `tests/fixtures/releases.json`
- Create: `tests/test_project_scaffold.py`

- [ ] **Step 1: Write the failing scaffold test**

```python
from pathlib import Path
import json
import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_project_configs_and_fixture_are_present():
    sources = yaml.safe_load((ROOT / "_scripts" / "sources.yaml").read_text())
    themes = yaml.safe_load((ROOT / "_scripts" / "themes.yaml").read_text())
    fixture = json.loads((ROOT / "tests" / "fixtures" / "releases.json").read_text())

    assert len(sources["products"]) >= 5
    assert {product["feed_type"] for product in sources["products"]} <= {
        "github_releases",
        "blog_rss",
    }
    assert {"agent-mode", "context-window", "pricing-model"} <= {
        theme["slug"] for theme in themes["themes"]
    }
    assert len(fixture["releases"]) >= 10
    assert fixture["releases"][0]["product"]
```

- [ ] **Step 2: Run the scaffold test to verify it fails**

Run: `python -m pytest tests/test_project_scaffold.py -v`

Expected: FAIL because `_scripts/sources.yaml`, `_scripts/themes.yaml`, and fixture data do not exist.

- [ ] **Step 3: Create scaffold files**

Use `apply_patch` to add:

```toml
# pyproject.toml
[project]
name = "chronolog"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "feedparser>=6.0.11",
  "httpx>=0.27.0",
  "python-frontmatter>=1.1.0",
  "PyYAML>=6.0.1",
]

[project.optional-dependencies]
dev = ["pytest>=8.2.0"]

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

```gitignore
# .gitignore
.DS_Store
__pycache__/
.pytest_cache/
.venv/
node_modules/
public/
.quartz-cache/
_pipeline/
```

```python
# _scripts/__init__.py
"""ChronoLog pipeline scripts."""
```

```yaml
# _scripts/themes.yaml
themes:
  - slug: agent-mode
    display_name: Agent Mode
    aliases: [agent, agents, agentic, autonomous-agent, shell-command]
    category: paradigm
    status: official
  - slug: context-window
    display_name: Context Window
    aliases: [context, long-context, context-length, context-expansion, tokens]
    category: capability
    status: official
  - slug: pricing-model
    display_name: Pricing Model
    aliases: [pricing, billing, subscription, usage-based, plan]
    category: business
    status: official
  - slug: model-support
    display_name: Model Support
    aliases: [model, models, claude, gpt, gemini, llm]
    category: capability
    status: official
  - slug: editor-experience
    display_name: Editor Experience
    aliases: [editor, autocomplete, completion, ide, tab]
    category: workflow
    status: official
  - slug: collaboration
    display_name: Collaboration
    aliases: [team, teams, collaboration, sharing, multiplayer]
    category: workflow
    status: official
```

```yaml
# _scripts/sources.yaml
products:
  - name: cursor
    display_name: Cursor
    feed_type: github_releases
    repo: getcursor/cursor
    backfill: full
    themes: [agent-mode, context-window, model-support, editor-experience]
    track_silence: true
    silence_window: month
    silence_periods: 2
    silence_baseline_factor: 0.5
    language: en
  - name: aider
    display_name: Aider
    feed_type: github_releases
    repo: Aider-AI/aider
    backfill: full
    themes: [agent-mode, model-support, editor-experience]
    track_silence: true
    silence_window: month
    silence_periods: 2
    silence_baseline_factor: 0.5
    language: en
  - name: continue
    display_name: Continue
    feed_type: github_releases
    repo: continuedev/continue
    backfill: full
    themes: [model-support, editor-experience, context-window]
    track_silence: true
    silence_window: month
    silence_periods: 2
    silence_baseline_factor: 0.5
    language: en
  - name: tabby
    display_name: Tabby
    feed_type: github_releases
    repo: TabbyML/tabby
    backfill: full
    themes: [editor-experience, model-support]
    track_silence: true
    silence_window: month
    silence_periods: 2
    silence_baseline_factor: 0.5
    language: en
  - name: openhands
    display_name: OpenHands
    feed_type: github_releases
    repo: All-Hands-AI/OpenHands
    backfill: full
    themes: [agent-mode, model-support]
    track_silence: true
    silence_window: month
    silence_periods: 2
    silence_baseline_factor: 0.5
    language: en
```

Create `tests/fixtures/releases.json`:

```json
{
  "releases": [
    {
      "product": "cursor",
      "product_name": "Cursor",
      "date": "2024-01-12",
      "version": "v0.20",
      "title": "Editor autocomplete update",
      "body": "- Editor autocomplete now responds faster in large files\n- New model support for Claude workflows",
      "source_url": "https://example.com/cursor/v0.20",
      "source_type": "fixture"
    },
    {
      "product": "cursor",
      "product_name": "Cursor",
      "date": "2025-03-15",
      "version": "v0.38",
      "title": "Agent and context update",
      "body": "- Agent can run shell commands after approval\n- Context window expanded to 200K tokens",
      "source_url": "https://example.com/cursor/v0.38",
      "source_type": "fixture"
    },
    {
      "product": "aider",
      "product_name": "Aider",
      "date": "2024-02-10",
      "version": "v0.22",
      "title": "Model support expansion",
      "body": "- Added model support for Claude and GPT coding workflows\n- Editor integration improves autocomplete handoff",
      "source_url": "https://example.com/aider/v0.22",
      "source_type": "fixture"
    },
    {
      "product": "aider",
      "product_name": "Aider",
      "date": "2025-01-20",
      "version": "v0.72",
      "title": "Agent repository workflow",
      "body": "- Agent workflow can inspect repository files before edits\n- Pricing documentation explains usage-based API costs",
      "source_url": "https://example.com/aider/v0.72",
      "source_type": "fixture"
    },
    {
      "product": "continue",
      "product_name": "Continue",
      "date": "2024-05-01",
      "version": "v0.9",
      "title": "IDE context improvements",
      "body": "- Context providers now index workspace symbols\n- Model support adds configurable local LLM options",
      "source_url": "https://example.com/continue/v0.9",
      "source_type": "fixture"
    },
    {
      "product": "continue",
      "product_name": "Continue",
      "date": "2025-08-08",
      "version": "v1.2",
      "title": "Team collaboration",
      "body": "- Team collaboration settings can share assistant rules\n- Context window handling improved for monorepos",
      "source_url": "https://example.com/continue/v1.2",
      "source_type": "fixture"
    },
    {
      "product": "tabby",
      "product_name": "Tabby",
      "date": "2024-03-18",
      "version": "v0.8",
      "title": "Editor completion release",
      "body": "- Editor completion latency reduced for self-hosted teams\n- Model support adds new code-specialized model presets",
      "source_url": "https://example.com/tabby/v0.8",
      "source_type": "fixture"
    },
    {
      "product": "tabby",
      "product_name": "Tabby",
      "date": "2025-10-02",
      "version": "v1.1",
      "title": "Usage and team controls",
      "body": "- Pricing page adds usage-based deployment guidance\n- Collaboration controls add team-level model policies",
      "source_url": "https://example.com/tabby/v1.1",
      "source_type": "fixture"
    },
    {
      "product": "openhands",
      "product_name": "OpenHands",
      "date": "2024-06-21",
      "version": "v0.7",
      "title": "Autonomous agent runtime",
      "body": "- Agent runtime can execute shell commands in a sandbox\n- Model support adds configurable provider routing",
      "source_url": "https://example.com/openhands/v0.7",
      "source_type": "fixture"
    },
    {
      "product": "openhands",
      "product_name": "OpenHands",
      "date": "2026-01-10",
      "version": "v1.0",
      "title": "Context and collaboration release",
      "body": "- Context window handling improves long-running repository tasks\n- Collaboration workflow lets reviewers approve agent actions",
      "source_url": "https://example.com/openhands/v1.0",
      "source_type": "fixture"
    }
  ]
}
```

- [ ] **Step 4: Run the scaffold test to verify it passes**

Run: `python -m pytest tests/test_project_scaffold.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml .gitignore _scripts/__init__.py _scripts/sources.yaml _scripts/themes.yaml tests/fixtures/releases.json tests/test_project_scaffold.py
git commit -m "chore: scaffold ChronoLog MVP project"
```

## Task 2: Common Helpers

**Files:**
- Create: `_scripts/common.py`
- Create: `tests/test_common.py`

- [ ] **Step 1: Write failing common helper tests**

```python
from datetime import date
from pathlib import Path

from _scripts.common import (
    card_id_for,
    machine_hash,
    read_json,
    slugify,
    write_json,
)


def test_slugify_normalizes_text_for_paths():
    assert slugify("Cursor Agent Mode!") == "cursor-agent-mode"
    assert slugify("  GPT-4.1 / Claude  ") == "gpt-4-1-claude"


def test_card_id_is_stable_from_quote():
    first = card_id_for("Cursor", "2026-03-15", "Context window expanded to 200K tokens.")
    second = card_id_for("cursor", "2026-03-15", " context window expanded to 200k tokens ")
    assert first == second
    assert first.startswith("cursor-2026-03-15-")
    assert len(first.rsplit("-", 1)[-1]) == 6


def test_write_json_creates_parent_directories(tmp_path: Path):
    target = tmp_path / "nested" / "file.json"
    write_json(target, {"run_id": "demo", "day": date(2026, 6, 26).isoformat()})
    assert read_json(target)["run_id"] == "demo"


def test_machine_hash_excludes_machine_hash_field():
    fields = {"title": "Cursor", "machine_hash": "old"}
    regions = {"summary": "Hello"}
    assert machine_hash(fields, regions) == machine_hash({"title": "Cursor"}, regions)
```

- [ ] **Step 2: Run common helper tests to verify they fail**

Run: `python -m pytest tests/test_common.py -v`

Expected: FAIL with `ModuleNotFoundError` or missing helper names.

- [ ] **Step 3: Implement common helpers**

Create `_scripts/common.py` with:

```python
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def short_hash(value: str, length: int = 6) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()[:length]


def card_id_for(product: str, release_date: str, quote: str) -> str:
    return f"{slugify(product)}-{release_date}-{short_hash(quote)}"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_date(value: str) -> date:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def machine_hash(machine_fields: dict[str, Any], regions: dict[str, str]) -> str:
    fields = {key: value for key, value in machine_fields.items() if key != "machine_hash"}
    payload = {"fields": fields, "regions": regions}
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class PipelinePaths:
    run_id: str
    root: Path = ROOT

    @property
    def run_dir(self) -> Path:
        return self.root / "_pipeline" / self.run_id

    @property
    def collected(self) -> Path:
        return self.run_dir / "01-collected" / "releases.json"

    @property
    def extracted(self) -> Path:
        return self.run_dir / "02-extracted" / "change_cards.json"

    @property
    def valid_cards(self) -> Path:
        return self.run_dir / "02-extracted" / "valid_change_cards.json"

    @property
    def analyze_a(self) -> Path:
        return self.run_dir / "03a-analyzed-per" / "analysis.json"

    @property
    def analyze_b(self) -> Path:
        return self.run_dir / "03b-analyzed-cross" / "analysis.json"

    @property
    def silence(self) -> Path:
        return self.run_dir / "03c-silence" / "alerts.json"

    @property
    def dlq(self) -> Path:
        return self.root / "_pipeline" / "dlq" / f"{self.run_id}-failed.json"
```

- [ ] **Step 4: Run common helper tests to verify they pass**

Run: `python -m pytest tests/test_common.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/common.py tests/test_common.py
git commit -m "feat: add ChronoLog common helpers"
```

## Task 3: Collector

**Files:**
- Create: `_scripts/collect.py`
- Create: `tests/test_collect.py`

- [ ] **Step 1: Write failing collector tests**

```python
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
```

- [ ] **Step 2: Run collector tests to verify they fail**

Run: `python -m pytest tests/test_collect.py -v`

Expected: FAIL because `_scripts.collect` does not exist.

- [ ] **Step 3: Implement collector**

Create `_scripts/collect.py` with functions `load_sources`, `collect_fixture`, `fetch_github_releases`, `fetch_rss_releases`, `collect_live`, and a CLI accepting `--fixture`, `--backfill`, `--run-id`, and `--limit`.

Core implementation:

```python
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import feedparser
import httpx

from _scripts.common import PipelinePaths, parse_date, read_json, read_yaml, write_json


def load_sources(path: Path) -> list[dict[str, Any]]:
    data = read_yaml(path)
    return [product for product in data["products"] if product.get("enabled", True)]


def collect_fixture(fixture_path: Path, output_path: Path) -> dict[str, Any]:
    data = read_json(fixture_path)
    releases = sorted(data["releases"], key=lambda item: (item["product"], item["date"]))
    payload = {"source": "fixture", "releases": releases}
    write_json(output_path, payload)
    return payload


def fetch_github_releases(product: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    url = f"https://api.github.com/repos/{product['repo']}/releases"
    response = httpx.get(url, timeout=30.0, headers={"Accept": "application/vnd.github+json"})
    response.raise_for_status()
    releases = []
    for item in response.json()[:limit]:
        published = item.get("published_at") or item.get("created_at")
        releases.append({
            "product": product["name"],
            "product_name": product["display_name"],
            "date": parse_date(published).isoformat(),
            "version": item.get("tag_name") or item.get("name") or "release",
            "title": item.get("name") or item.get("tag_name") or "Release",
            "body": item.get("body") or "",
            "source_url": item.get("html_url") or url,
            "source_type": "github_releases",
        })
    return releases


def fetch_rss_releases(product: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    feed = feedparser.parse(product["url"])
    releases = []
    for entry in feed.entries[:limit]:
        date_value = getattr(entry, "published", None) or getattr(entry, "updated", None)
        releases.append({
            "product": product["name"],
            "product_name": product["display_name"],
            "date": parse_date(date_value).isoformat(),
            "version": getattr(entry, "id", getattr(entry, "title", "release")),
            "title": getattr(entry, "title", "Release"),
            "body": getattr(entry, "summary", ""),
            "source_url": getattr(entry, "link", product["url"]),
            "source_type": "blog_rss",
        })
    return releases


def collect_live(sources_path: Path, output_path: Path, limit: int) -> dict[str, Any]:
    releases: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for product in load_sources(sources_path):
        try:
            if product["feed_type"] == "github_releases":
                releases.extend(fetch_github_releases(product, limit))
            elif product["feed_type"] == "blog_rss":
                releases.extend(fetch_rss_releases(product, limit))
        except Exception as exc:
            errors.append({"product": product["name"], "error": str(exc)})
    payload = {"source": "live", "releases": sorted(releases, key=lambda item: item["date"]), "errors": errors}
    write_json(output_path, payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--backfill", nargs="?", const="all")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    paths = PipelinePaths(args.run_id)
    if args.fixture:
        collect_fixture(Path("tests/fixtures/releases.json"), paths.collected)
    else:
        collect_live(Path("_scripts/sources.yaml"), paths.collected, args.limit)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run collector tests to verify they pass**

Run: `python -m pytest tests/test_collect.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/collect.py tests/test_collect.py
git commit -m "feat: collect tier one changelog sources"
```

## Task 4: Extractor

**Files:**
- Create: `_scripts/extract.py`
- Create: `tests/test_extract.py`

- [ ] **Step 1: Write failing extractor tests**

```python
from _scripts.extract import extract_cards_from_release, load_theme_vocabulary


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
        "title": "Mobile companion",
        "body": "- New mobile companion app for reviewing conversations",
        "source_url": "https://example.com",
    }

    cards = extract_cards_from_release(release, themes)

    assert cards[0]["theme"] == "__candidate__"
    assert cards[0]["theme_suggestion"] == "mobile-companion"
```

- [ ] **Step 2: Run extractor tests to verify they fail**

Run: `python -m pytest tests/test_extract.py -v`

Expected: FAIL because `_scripts.extract` does not exist.

- [ ] **Step 3: Implement deterministic extractor**

Create `_scripts/extract.py` with:

```python
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from _scripts.common import PipelinePaths, card_id_for, read_json, read_yaml, slugify, write_json


IMPACT_WORDS = {
    "paradigm-shift": ["agent", "autonomous", "pricing", "200k", "major"],
    "significant": ["support", "new", "expanded", "integration", "model"],
}


def load_theme_vocabulary(path: str | Path) -> dict[str, dict[str, Any]]:
    data = read_yaml(Path(path))
    vocab = {}
    for theme in data["themes"]:
        terms = {theme["slug"], theme["display_name"].lower(), *theme.get("aliases", [])}
        vocab[theme["slug"]] = {**theme, "terms": {term.lower() for term in terms}}
    return vocab


def split_release_lines(body: str) -> list[str]:
    lines = []
    for raw in body.splitlines():
        line = re.sub(r"^[-*#\s]+", "", raw).strip()
        if len(line) >= 12:
            lines.append(line)
    return lines


def choose_theme(text: str, themes: dict[str, dict[str, Any]]) -> tuple[str, str | None]:
    lowered = text.lower()
    for slug, theme in themes.items():
        if any(term in lowered for term in theme["terms"]):
            return slug, None
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9]+", text.lower())[:3]
    return "__candidate__", slugify(" ".join(words) or "unclassified")


def choose_impact(text: str) -> str:
    lowered = text.lower()
    for impact, words in IMPACT_WORDS.items():
        if any(word in lowered for word in words):
            return impact
    return "incremental"


def extract_cards_from_release(release: dict[str, Any], themes: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    lines = split_release_lines(release.get("body", "")) or [release["title"]]
    cards = []
    seen_themes: set[str] = set()
    for line in lines[:5]:
        theme, suggestion = choose_theme(line, themes)
        identity_theme = suggestion if theme == "__candidate__" else theme
        if identity_theme in seen_themes:
            continue
        seen_themes.add(identity_theme)
        impact = choose_impact(line)
        card = {
            "type": "change",
            "card_id": card_id_for(release["product"], release["date"], line),
            "product": release["product"],
            "product_name": release["product_name"],
            "source_release": f"{release['product']}-{release['date']}-{slugify(release.get('version') or release['title'])}",
            "date": release["date"],
            "title": line[:80],
            "slug": slugify(line)[:80].strip("-"),
            "theme": theme,
            "impact": impact,
            "description": line,
            "comparison": "",
            "evidence": [{"source_release": release.get("source_url", ""), "quote": line}],
            "extractor_version": "fallback-v1",
        }
        if suggestion:
            card["theme_suggestion"] = suggestion
        if impact in {"significant", "paradigm-shift"}:
            card["ai_generated"] = True
            card["confidence"] = "low"
        cards.append(card)
    return cards


def extract_run(run_id: str) -> list[dict[str, Any]]:
    paths = PipelinePaths(run_id)
    themes = load_theme_vocabulary(Path("_scripts/themes.yaml"))
    releases = read_json(paths.collected)["releases"]
    cards = [card for release in releases for card in extract_cards_from_release(release, themes)]
    write_json(paths.extracted, {"run_id": run_id, "change_cards": cards})
    return cards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    extract_run(args.run_id)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run extractor tests to verify they pass**

Run: `python -m pytest tests/test_extract.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/extract.py tests/test_extract.py
git commit -m "feat: extract deterministic change cards"
```

## Task 5: Validator And DLQ

**Files:**
- Create: `_scripts/validate.py`
- Create: `tests/test_validate.py`

- [ ] **Step 1: Write failing validator tests**

```python
from pathlib import Path

from _scripts.common import write_json
from _scripts.validate import validate_cards_file


def test_validate_cards_file_splits_valid_and_invalid_records(tmp_path: Path):
    source = tmp_path / "cards.json"
    valid_output = tmp_path / "valid.json"
    dlq_output = tmp_path / "dlq.json"
    write_json(source, {
        "change_cards": [
            {
                "type": "change",
                "card_id": "cursor-2026-03-15-a1b2c3",
                "product": "cursor",
                "product_name": "Cursor",
                "source_release": "cursor-2026-03-15-v1",
                "date": "2026-03-15",
                "title": "Agent mode",
                "slug": "agent-mode",
                "theme": "agent-mode",
                "impact": "significant",
                "description": "Agent mode can run commands.",
                "comparison": "",
                "evidence": [{"source_release": "https://example.com", "quote": "Agent mode can run commands."}],
                "extractor_version": "fallback-v1",
                "ai_generated": True,
                "confidence": "low",
            },
            {"type": "change", "theme": "made-up", "impact": "huge"},
        ]
    })

    result = validate_cards_file(source, valid_output, dlq_output, "_scripts/themes.yaml")

    assert result["passed"] == 1
    assert result["failed"] == 1
    assert valid_output.exists()
    assert dlq_output.exists()
```

- [ ] **Step 2: Run validator tests to verify they fail**

Run: `python -m pytest tests/test_validate.py -v`

Expected: FAIL because `_scripts.validate` does not exist.

- [ ] **Step 3: Implement validator and DLQ writer**

Create `_scripts/validate.py` with:

```python
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from _scripts.common import PipelinePaths, read_json, read_yaml, write_json


REQUIRED_FIELDS = {
    "type", "card_id", "product", "product_name", "source_release", "date", "title",
    "slug", "theme", "impact", "description", "evidence", "extractor_version",
}
IMPACTS = {"incremental", "significant", "paradigm-shift"}
CARD_ID_RE = re.compile(r"^[a-z0-9-]+-\d{4}-\d{2}-\d{2}-[a-f0-9]{6}$")


def official_themes(themes_path: str | Path) -> set[str]:
    data = read_yaml(Path(themes_path))
    return {theme["slug"] for theme in data["themes"] if theme.get("status") == "official"}


def validate_card(card: dict[str, Any], themes: set[str]) -> list[str]:
    errors = []
    missing = sorted(REQUIRED_FIELDS - set(card))
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if card.get("type") != "change":
        errors.append("type must be change")
    if not CARD_ID_RE.match(str(card.get("card_id", ""))):
        errors.append("card_id is not deterministic format")
    if card.get("theme") not in themes:
        if card.get("theme") != "__candidate__" or not card.get("theme_suggestion"):
            errors.append("theme must be official or candidate with suggestion")
    if card.get("impact") not in IMPACTS:
        errors.append("impact is invalid")
    evidence = card.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence is required")
    elif not evidence[0].get("source_release") or not evidence[0].get("quote"):
        errors.append("evidence requires source_release and quote")
    if not str(card.get("description", "")).strip():
        errors.append("description is required")
    if card.get("impact") in {"significant", "paradigm-shift"}:
        if card.get("ai_generated") is not True or card.get("confidence") not in {"low", "medium", "high"}:
            errors.append("high impact cards require ai_generated and confidence")
    return errors


def validate_cards_file(source: Path, valid_output: Path, dlq_output: Path, themes_path: str | Path) -> dict[str, int]:
    payload = read_json(source)
    themes = official_themes(themes_path)
    valid = []
    failed = []
    for card in payload.get("change_cards", []):
        errors = validate_card(card, themes)
        if errors:
            failed.append({"record": card, "errors": errors})
        else:
            valid.append(card)
    write_json(valid_output, {"change_cards": valid})
    if failed:
        write_json(dlq_output, {"failed": failed})
    return {"passed": len(valid), "failed": len(failed)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--round", default="1")
    args = parser.parse_args()
    if args.round != "1":
        return
    paths = PipelinePaths(args.run_id)
    validate_cards_file(paths.extracted, paths.valid_cards, paths.dlq, "_scripts/themes.yaml")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run validator tests to verify they pass**

Run: `python -m pytest tests/test_validate.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/validate.py tests/test_validate.py
git commit -m "feat: validate change cards and isolate dlq"
```

## Task 6: Analyzer-A

**Files:**
- Create: `_scripts/analyze_a.py`
- Create: `tests/test_analyze.py`

- [ ] **Step 1: Write failing Analyzer-A tests**

```python
from _scripts.analyze_a import analyze_products


def test_analyze_products_creates_eras_and_evolves_from():
    cards = [
        {"card_id": "cursor-2025-01-01-aaaaaa", "product": "cursor", "product_name": "Cursor", "date": "2025-01-01", "theme": "editor-experience", "source_release": "r1"},
        {"card_id": "cursor-2025-06-01-bbbbbb", "product": "cursor", "product_name": "Cursor", "date": "2025-06-01", "theme": "editor-experience", "source_release": "r2"},
        {"card_id": "cursor-2026-01-01-cccccc", "product": "cursor", "product_name": "Cursor", "date": "2026-01-01", "theme": "agent-mode", "source_release": "r3"},
    ]

    result = analyze_products(cards)

    cursor = result["products"]["cursor"]
    assert cursor["verbosity_baseline"] == 1.0
    assert len(cursor["eras"]) >= 2
    assert result["evolves_from"]["cursor-2025-06-01-bbbbbb"] == ["cursor-2025-01-01-aaaaaa"]
```

- [ ] **Step 2: Run Analyzer-A tests to verify they fail**

Run: `python -m pytest tests/test_analyze.py::test_analyze_products_creates_eras_and_evolves_from -v`

Expected: FAIL because `_scripts.analyze_a` does not exist.

- [ ] **Step 3: Implement Analyzer-A**

Create `_scripts/analyze_a.py` with:

```python
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from typing import Any

from _scripts.common import PipelinePaths, read_json, write_json


def analyze_products(cards: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        grouped[card["product"]].append(card)

    products = {}
    evolves_from = {}
    for product, product_cards in grouped.items():
        ordered = sorted(product_cards, key=lambda card: (card["date"], card["card_id"]))
        releases = {card["source_release"] for card in ordered}
        theme_counts = Counter(card["theme"] for card in ordered)
        baseline = round(len(ordered) / max(len(releases), 1), 2)

        midpoint = max(len(ordered) // 2, 1)
        era_groups = [ordered[:midpoint], ordered[midpoint:]] if len(ordered) >= 3 else [ordered]
        eras = []
        for index, era_cards in enumerate(era_groups, start=1):
            dominant = Counter(card["theme"] for card in era_cards).most_common(1)[0][0]
            eras.append({
                "name": f"{dominant.replace('-', ' ').title()} Era",
                "from": era_cards[0]["date"],
                "to": era_cards[-1]["date"] if index < len(era_groups) else None,
                "summary": f"{product} focused on {dominant} across {len(era_cards)} tracked changes.",
                "dominant_theme": dominant,
                "data_sparse": len(ordered) < 3,
            })

        previous_by_theme: dict[str, str] = {}
        for card in ordered:
            previous = previous_by_theme.get(card["theme"])
            if previous:
                evolves_from[card["card_id"]] = [previous]
            previous_by_theme[card["theme"]] = card["card_id"]

        products[product] = {
            "product_name": ordered[0]["product_name"],
            "verbosity_baseline": baseline,
            "top_themes": [theme for theme, _ in theme_counts.most_common()],
            "eras": eras,
        }

    return {"products": products, "evolves_from": evolves_from}


def analyze_run(run_id: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    cards = read_json(paths.valid_cards)["change_cards"]
    result = analyze_products(cards)
    write_json(paths.analyze_a, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    analyze_run(args.run_id)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run Analyzer-A tests to verify they pass**

Run: `python -m pytest tests/test_analyze.py::test_analyze_products_creates_eras_and_evolves_from -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/analyze_a.py tests/test_analyze.py
git commit -m "feat: analyze product evolution eras"
```

## Task 7: Analyzer-B

**Files:**
- Create: `_scripts/analyze_b.py`
- Modify: `tests/test_analyze.py`

- [ ] **Step 1: Write failing Analyzer-B test**

```python
from _scripts.analyze_b import analyze_themes


def test_analyze_themes_creates_related_changes_and_diffusion():
    cards = [
        {"card_id": "aider-2025-01-01-aaaaaa", "product": "aider", "product_name": "Aider", "date": "2025-01-01", "theme": "agent-mode"},
        {"card_id": "cursor-2025-02-01-bbbbbb", "product": "cursor", "product_name": "Cursor", "date": "2025-02-01", "theme": "agent-mode"},
        {"card_id": "tabby-2025-03-01-cccccc", "product": "tabby", "product_name": "Tabby", "date": "2025-03-01", "theme": "editor-experience"},
    ]

    result = analyze_themes(cards)

    cursor = result["cards"]["cursor-2025-02-01-bbbbbb"]
    assert cursor["related_changes"] == ["aider-2025-01-01-aaaaaa"]
    assert cursor["diffusion"]["scope"] == "tracked-products-only"
    assert cursor["diffusion"]["role"] == "follower"
    assert cursor["diffusion"]["lag_days"] == 31
```

- [ ] **Step 2: Run Analyzer-B test to verify it fails**

Run: `python -m pytest tests/test_analyze.py::test_analyze_themes_creates_related_changes_and_diffusion -v`

Expected: FAIL because `_scripts.analyze_b` does not exist.

- [ ] **Step 3: Implement Analyzer-B**

Create `_scripts/analyze_b.py` with:

```python
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
from typing import Any

from _scripts.common import PipelinePaths, read_json, write_json


def date_value(value: str) -> date:
    return date.fromisoformat(value)


def analyze_themes(cards: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    tracked_products = {card["product"] for card in cards}
    for card in cards:
        grouped[card["theme"]].append(card)

    patches = {}
    themes = {}
    for theme, theme_cards in grouped.items():
        ordered = sorted(theme_cards, key=lambda card: (card["date"], card["card_id"]))
        first = ordered[0]
        first_date = date_value(first["date"])
        themes[theme] = {
            "cards": [card["card_id"] for card in ordered],
            "products": sorted({card["product"] for card in ordered}),
        }
        for index, card in enumerate(ordered):
            previous = [other["card_id"] for other in ordered[max(0, index - 3):index]]
            role = "originator" if card["card_id"] == first["card_id"] else "follower"
            if card["product"] == first["product"] and role != "originator":
                role = "variant"
            patches[card["card_id"]] = {
                "related_changes": previous,
                "diffusion": {
                    "theme": theme,
                    "scope": "tracked-products-only",
                    "role": role,
                    "first_in_tracked": first["card_id"],
                    "lag_days": (date_value(card["date"]) - first_date).days,
                    "tracked_products_count": len(tracked_products),
                },
            }
    return {"themes": themes, "cards": patches}


def analyze_run(run_id: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    cards = read_json(paths.valid_cards)["change_cards"]
    result = analyze_themes(cards)
    write_json(paths.analyze_b, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    args = parser.parse_args()
    analyze_run(args.run_id)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run Analyzer-B test to verify it passes**

Run: `python -m pytest tests/test_analyze.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/analyze_b.py tests/test_analyze.py
git commit -m "feat: analyze theme diffusion"
```

## Task 8: Silence Monitor

**Files:**
- Create: `_scripts/silence_monitor.py`
- Create: `tests/test_silence_monitor.py`

- [ ] **Step 1: Write failing silence monitor tests**

```python
from _scripts.silence_monitor import detect_silence


def test_silence_monitor_marks_sparse_history_pending():
    releases = [{"product": "cursor", "date": "2026-06-01"}]
    source = {"name": "cursor", "display_name": "Cursor", "track_silence": True, "silence_periods": 2}

    result = detect_silence(releases, [source], today="2026-06-26")

    assert result["alerts"] == []
    assert result["pending"][0]["product"] == "cursor"


def test_silence_monitor_alerts_for_configured_silence():
    releases = [
        {"product": "cursor", "date": "2025-01-01"},
        {"product": "cursor", "date": "2025-02-01"},
        {"product": "cursor", "date": "2025-03-01"},
        {"product": "cursor", "date": "2025-04-01"},
    ]
    source = {
        "name": "cursor",
        "display_name": "Cursor",
        "track_silence": True,
        "silence_window": "month",
        "silence_periods": 2,
        "silence_baseline_factor": 0.5,
    }

    result = detect_silence(releases, [source], today="2026-06-26")

    assert result["alerts"][0]["type"] == "silence"
    assert result["alerts"][0]["product"] == "cursor"
```

- [ ] **Step 2: Run silence monitor tests to verify they fail**

Run: `python -m pytest tests/test_silence_monitor.py -v`

Expected: FAIL because `_scripts.silence_monitor` does not exist.

- [ ] **Step 3: Implement silence monitor**

Create `_scripts/silence_monitor.py` with:

```python
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
from typing import Any

from _scripts.collect import load_sources
from _scripts.common import PipelinePaths, read_json, write_json


def month_index(value: date) -> int:
    return value.year * 12 + value.month


def detect_silence(releases: list[dict[str, Any]], sources: list[dict[str, Any]], today: str) -> dict[str, Any]:
    today_date = date.fromisoformat(today)
    by_product: dict[str, list[date]] = defaultdict(list)
    for release in releases:
        by_product[release["product"]].append(date.fromisoformat(release["date"]))

    alerts = []
    pending = []
    current_month = month_index(today_date)
    for source in sources:
        if not source.get("track_silence", False):
            continue
        product = source["name"]
        dates = sorted(by_product.get(product, []))
        if len(dates) < 4:
            pending.append({"product": product, "silence_tracking": "pending", "reason": "insufficient history"})
            continue
        active_months = {month_index(day) for day in dates}
        first_month = month_index(dates[0])
        months_observed = max(current_month - first_month, 1)
        baseline = len(active_months) / months_observed
        periods = int(source.get("silence_periods", 2))
        recent_count = sum(1 for offset in range(periods) if current_month - offset in active_months)
        threshold = baseline * float(source.get("silence_baseline_factor", 0.5))
        if recent_count < threshold and all(current_month - offset not in active_months for offset in range(periods)):
            alerts.append({
                "type": "silence",
                "product": product,
                "product_name": source.get("display_name", product),
                "date": today,
                "silence_periods": periods,
                "baseline_monthly_releases": round(baseline, 2),
                "recent_releases": recent_count,
                "message": f"{source.get('display_name', product)} has no releases in the last {periods} month windows.",
            })
    return {"alerts": alerts, "pending": pending}


def monitor_run(run_id: str, today: str) -> dict[str, Any]:
    paths = PipelinePaths(run_id)
    releases = read_json(paths.collected)["releases"]
    sources = load_sources(paths.root / "_scripts" / "sources.yaml")
    result = detect_silence(releases, sources, today)
    write_json(paths.silence, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--today", default=date.today().isoformat())
    args = parser.parse_args()
    monitor_run(args.run_id, args.today)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run silence monitor tests to verify they pass**

Run: `python -m pytest tests/test_silence_monitor.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/silence_monitor.py tests/test_silence_monitor.py
git commit -m "feat: detect product release silence"
```

## Task 9: Writer Ownership And Markdown Rendering

**Files:**
- Create: `_scripts/writer.py`
- Create: `tests/test_writer.py`

- [ ] **Step 1: Write failing writer tests**

```python
from pathlib import Path

from _scripts.writer import render_theme_markdown, replace_machine_region


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


def test_render_theme_markdown_contains_mermaid_timeline(tmp_path: Path):
    cards = [
        {"card_id": "aider-2025-01-01-aaaaaa", "product": "aider", "product_name": "Aider", "date": "2025-01-01", "title": "Agent mode", "theme": "agent-mode", "slug": "agent-mode"},
        {"card_id": "cursor-2025-02-01-bbbbbb", "product": "cursor", "product_name": "Cursor", "date": "2025-02-01", "title": "Agent shell", "theme": "agent-mode", "slug": "agent-shell"},
    ]

    markdown = render_theme_markdown("agent-mode", cards)

    assert "```mermaid" in markdown
    assert "timeline" in markdown
    assert "Aider" in markdown
    assert "Cursor" in markdown
```

- [ ] **Step 2: Run writer tests to verify they fail**

Run: `python -m pytest tests/test_writer.py -v`

Expected: FAIL because `_scripts.writer` does not exist.

- [ ] **Step 3: Implement writer**

Create `_scripts/writer.py` with these exported functions:

```python
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import frontmatter

from _scripts.common import PipelinePaths, machine_hash, read_json, slugify, write_text


REGION_RE = re.compile(r"<!-- chronolog:begin region=\"(?P<name>[^\"]+)\" -->.*?<!-- chronolog:end -->", re.S)


def machine_region(region: str, content: str) -> str:
    return f"<!-- chronolog:begin region=\"{region}\" -->\n{content.rstrip()}\n<!-- chronolog:end -->"


def replace_machine_region(existing: str, region: str, content: str) -> str:
    rendered = machine_region(region, content)
    pattern = re.compile(rf"<!-- chronolog:begin region=\"{re.escape(region)}\" -->.*?<!-- chronolog:end -->", re.S)
    if pattern.search(existing):
        return pattern.sub(rendered, existing)
    return existing.rstrip() + "\n\n" + rendered + "\n"


def render_frontmatter(metadata: dict[str, Any], body: str) -> str:
    post = frontmatter.Post(body, **metadata)
    return frontmatter.dumps(post)


def card_link(card: dict[str, Any]) -> str:
    return f"[[{card['date']}-{card['slug']}]]"


def render_theme_markdown(theme: str, cards: list[dict[str, Any]]) -> str:
    ordered = sorted(cards, key=lambda card: (card["date"], card["product_name"]))
    timeline = ["```mermaid", "timeline", f"    title {theme}"]
    for card in ordered:
        timeline.append(f"    {card['date']} : {card['product_name']} : {card['title']}")
    timeline.append("```")
    links = "\n".join(f"- {card['date']} {card['product_name']}: {card_link(card)}" for card in ordered)
    body = f"# Theme: {theme}\n\n## Cross-Product Timeline\n{machine_region('timeline', chr(10).join(timeline))}\n\n## Change Cards\n{machine_region('cards', links)}\n"
    fields = {
        "tags": ["theme", "moc"],
        "status": "official",
        "products_involved": sorted({card["product_name"] for card in ordered}),
    }
    fields["machine_hash"] = machine_hash(fields, {"timeline": "\n".join(timeline), "cards": links})
    return render_frontmatter(fields, body)


def render_change_markdown(card: dict[str, Any], patch_a: dict[str, Any], patch_b: dict[str, Any]) -> str:
    metadata = {key: card[key] for key in ["type", "card_id", "product", "source_release", "date", "theme", "impact", "extractor_version"]}
    metadata.update(patch_a)
    metadata.update(patch_b)
    evidence = "\n".join(f"> {item['quote']}\n> Source: {item['source_release']}" for item in card["evidence"])
    body_regions = {
        "description": card["description"],
        "evidence": evidence,
        "evolution": "\n".join(f"- {item}" for item in patch_a.get("evolves_from", [])) or "No prior tracked change.",
        "diffusion": str(patch_b.get("diffusion", {"scope": "tracked-products-only"})),
    }
    metadata["machine_hash"] = machine_hash(metadata, body_regions)
    body = f"# {card['title']}\n\n" + "\n\n".join(machine_region(name, content) for name, content in body_regions.items()) + "\n\n## Editor Notes\n"
    return render_frontmatter(metadata, body)
```

Also implement `write_run(run_id)` in the same file:

```python
def write_run(run_id: str) -> None:
    paths = PipelinePaths(run_id)
    cards = read_json(paths.valid_cards)["change_cards"]
    analysis_a = read_json(paths.analyze_a)
    analysis_b = read_json(paths.analyze_b)
    silence = read_json(paths.silence) if paths.silence.exists() else {"alerts": []}

    cards_by_id = {card["card_id"]: card for card in cards}
    cards_by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    cards_by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    releases_by_product: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)

    for card in cards:
        patch_a = {"evolves_from": analysis_a.get("evolves_from", {}).get(card["card_id"], [])}
        patch_b = analysis_b.get("cards", {}).get(card["card_id"], {})
        cards_by_product[card["product"]].append(card)
        cards_by_theme[card["theme"]].append(card)
        target = paths.root / "Changes" / card["product_name"] / f"{card['date']}-{card['slug']}.md"
        write_text(target, render_change_markdown(card, patch_a, patch_b))
        releases_by_product[card["product_name"]][card["source_release"]] = {
            "date": card["date"],
            "title": card["source_release"],
            "cards": releases_by_product[card["product_name"]].get(card["source_release"], {}).get("cards", []) + [card],
        }

    for product, product_info in analysis_a["products"].items():
        product_cards = sorted(cards_by_product[product], key=lambda item: item["date"])
        target = paths.root / "Products" / f"{product_info['product_name']}.md"
        write_text(target, render_product_markdown(product, product_info, product_cards))

    for product_name, releases in releases_by_product.items():
        for release in releases.values():
            target = paths.root / "Releases" / product_name / f"{release['date']}-{slugify(release['title'])}.md"
            write_text(target, render_release_markdown(product_name, release))

    for theme, theme_cards in cards_by_theme.items():
        target = paths.root / "Themes" / f"{theme}.md"
        write_text(target, render_theme_markdown(theme, theme_cards))

    for alert in silence.get("alerts", []):
        target = paths.root / "Alerts" / f"{alert['date']}-{alert['product']}-silence.md"
        write_text(target, render_alert_markdown(alert))

    write_text(paths.root / "index.md", render_index_markdown(cards, analysis_a, analysis_b, silence))
```

The same implementation pass must add `render_product_markdown`, `render_release_markdown`, `render_alert_markdown`, and `render_index_markdown` as small functions in `_scripts/writer.py`. Each function should use `machine_region` for generated sections and `render_frontmatter` for YAML frontmatter.

- [ ] **Step 4: Run writer tests to verify they pass**

Run: `python -m pytest tests/test_writer.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/writer.py tests/test_writer.py
git commit -m "feat: render vault markdown with ownership regions"
```

## Task 10: Pipeline Orchestrator And End-To-End Fixture

**Files:**
- Create: `_scripts/run_pipeline.py`
- Create: `tests/test_pipeline.py`
- Modify: `_scripts/writer.py`

- [ ] **Step 1: Write failing end-to-end pipeline test**

```python
from pathlib import Path
import subprocess
import sys


def test_fixture_pipeline_generates_vault_content():
    subprocess.run(
        [sys.executable, "_scripts/run_pipeline.py", "--fixture", "--run-id", "test-demo", "--today", "2026-06-26"],
        check=True,
    )

    assert Path("Products").exists()
    assert Path("Changes").exists()
    assert Path("Releases").exists()
    assert Path("Themes").exists()
    assert Path("index.md").exists()
    assert any(Path("Themes").glob("*.md"))
    assert "```mermaid" in next(Path("Themes").glob("*.md")).read_text()
```

- [ ] **Step 2: Run pipeline test to verify it fails**

Run: `python -m pytest tests/test_pipeline.py -v`

Expected: FAIL because `_scripts/run_pipeline.py` does not exist or writer output is incomplete.

- [ ] **Step 3: Implement orchestrator**

Create `_scripts/run_pipeline.py`:

```python
from __future__ import annotations

import argparse
import subprocess
import sys


def run_step(args: list[str]) -> None:
    subprocess.run([sys.executable, *args], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="demo")
    parser.add_argument("--fixture", action="store_true")
    parser.add_argument("--today", default="2026-06-26")
    args = parser.parse_args()

    collect_args = ["_scripts/collect.py", "--run-id", args.run_id]
    if args.fixture:
        collect_args.append("--fixture")
    run_step(collect_args)
    run_step(["_scripts/extract.py", "--run-id", args.run_id])
    run_step(["_scripts/validate.py", "--round", "1", "--run-id", args.run_id])
    run_step(["_scripts/analyze_a.py", "--run-id", args.run_id])
    run_step(["_scripts/analyze_b.py", "--run-id", args.run_id])
    run_step(["_scripts/silence_monitor.py", "--run-id", args.run_id, "--today", args.today])
    run_step(["_scripts/writer.py", "--run-id", args.run_id])


if __name__ == "__main__":
    main()
```

Verify `writer.write_run(run_id)` writes:

- `Products/{ProductName}.md`
- `Releases/{ProductName}/{date}-{version-or-title}.md`
- `Changes/{ProductName}/{date}-{slug}.md`
- `Themes/{theme}.md`
- `Alerts/{date}-{product}-silence.md`
- `index.md`

- [ ] **Step 4: Run pipeline test to verify it passes**

Run: `python -m pytest tests/test_pipeline.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _scripts/run_pipeline.py _scripts/writer.py tests/test_pipeline.py
git commit -m "feat: run fixture pipeline end to end"
```

## Task 11: Quartz Preview

**Files:**
- Create: `package.json`
- Create: `quartz.config.ts`
- Create: `quartz.layout.ts`
- Create: `README.md`

- [ ] **Step 1: Write failing package/config smoke test**

```python
from pathlib import Path
import json


def test_quartz_files_define_build_command():
    package = json.loads(Path("package.json").read_text())
    assert package["scripts"]["build"] == "quartz build"
    assert "quartz" in package["dependencies"]
    assert Path("quartz.config.ts").exists()
```

Save this in `tests/test_quartz_config.py`.

- [ ] **Step 2: Run Quartz config test to verify it fails**

Run: `python -m pytest tests/test_quartz_config.py -v`

Expected: FAIL because `package.json` and Quartz config files do not exist.

- [ ] **Step 3: Add minimal Quartz files and README**

Create `package.json`:

```json
{
  "name": "chronolog",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "build": "quartz build",
    "serve": "quartz build --serve"
  },
  "dependencies": {
    "@jackyzha0/quartz": "^4.5.1"
  },
  "devDependencies": {
    "typescript": "^5.5.0"
  }
}
```

Create `quartz.config.ts`:

```ts
import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "ChronoLog",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "localhost:8080",
    ignorePatterns: ["private", "templates", ".obsidian", "_pipeline", "docs/superpowers", "tests"],
    defaultDateType: "modified",
    theme: {
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f8f7f2",
          lightgray: "#dedbd2",
          gray: "#6c6a63",
          darkgray: "#34332f",
          dark: "#171714",
          secondary: "#9b6a19",
          tertiary: "#3f6f6b",
          highlight: "rgba(155, 106, 25, 0.15)",
          textHighlight: "#fff0bd",
        },
        darkMode: {
          light: "#171714",
          lightgray: "#34332f",
          gray: "#9d9a90",
          darkgray: "#dedbd2",
          dark: "#f8f7f2",
          secondary: "#d49a36",
          tertiary: "#74aaa4",
          highlight: "rgba(212, 154, 54, 0.2)",
          textHighlight: "#5a4314",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: false }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
```

Create `quartz.layout.ts`:

```ts
import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [],
}
```

Create `README.md` with:

```markdown
# ChronoLog

Run the local MVP fixture pipeline:

```bash
python -m pytest
python _scripts/run_pipeline.py --fixture --run-id demo --today 2026-06-26
```

Build the Quartz site:

```bash
npm install
npx quartz build
```

Preview locally:

```bash
npx quartz build --serve
```
```

- [ ] **Step 4: Run Quartz config test to verify it passes**

Run: `python -m pytest tests/test_quartz_config.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add package.json quartz.config.ts quartz.layout.ts README.md tests/test_quartz_config.py
git commit -m "feat: add Quartz preview configuration"
```

## Task 12: Final Verification And MVP Acceptance

**Files:**
- Modify: generated Vault files from fixture pipeline.
- Inspect: `Products/`, `Themes/`, `Changes/`, `Releases/`, `Alerts/`, `index.md`.

- [ ] **Step 1: Run full Python test suite**

Run: `python -m pytest`

Expected: PASS with every test file passing.

- [ ] **Step 2: Run fixture pipeline**

Run: `python _scripts/run_pipeline.py --fixture --run-id demo --today 2026-06-26`

Expected: exit code 0 and generated Markdown in `Products/`, `Changes/`, `Releases/`, `Themes/`, and `index.md`.

- [ ] **Step 3: Re-run validation against demo run**

Run: `python _scripts/validate.py --round 1 --run-id demo`

Expected: exit code 0; `_pipeline/demo/02-extracted/valid_change_cards.json` contains valid cards. If `_pipeline/dlq/demo-failed.json` exists, every failed record is a deliberate candidate or malformed fixture from a test-only path, not normal fixture output.

- [ ] **Step 4: Install Node dependencies**

Run: `npm install`

Expected: exit code 0 and a generated `package-lock.json`.

- [ ] **Step 5: Build Quartz**

Run: `npx quartz build`

Expected: exit code 0 and generated static output in `public/`.

- [ ] **Step 6: Inspect MVP content requirements**

Run:

```bash
find Products Changes Releases Themes Alerts -type f | sort
rg -n "```mermaid|timeline" Themes
rg -n "chronolog:begin region=\"eras\"|verbosity_baseline" Products
rg -n "chronolog:begin region=\"diffusion\"|tracked-products-only" Changes
```

Expected:

- Product pages exist and contain eras.
- Change cards exist under per-product directories.
- Release pages exist under per-product directories.
- Theme pages include Mermaid timeline blocks.
- Change pages include diffusion metadata with `tracked-products-only`.

- [ ] **Step 7: Commit final generated MVP artifacts**

```bash
git add README.md package-lock.json Products Changes Releases Themes Alerts index.md
git commit -m "chore: generate ChronoLog MVP fixture vault"
```

- [ ] **Step 8: Report verification evidence**

In the final response, include:

- `python -m pytest` result.
- `python _scripts/run_pipeline.py --fixture --run-id demo --today 2026-06-26` result.
- `python _scripts/validate.py --round 1 --run-id demo` result.
- `npm install` result.
- `npx quartz build` result.
- A concise list of generated top-level artifacts.

## Self-Review Checklist

- Spec coverage: Tasks 1-12 cover the approved design scope, including Vault structure, tier-1 source config, fixture backfill path, extraction, validation, Analyzer-A, Analyzer-B, silence monitor, Writer ownership, Mermaid Theme MOCs, Quartz preview, tests, and final acceptance commands.
- Scope control: Phase 2 and Phase 3 items stay outside the plan except where README names future commands.
- Type consistency: `card_id`, `theme`, `impact`, `evidence`, `verbosity_baseline`, `evolves_from`, `related_changes`, `diffusion`, `machine_hash`, and `run_id` names are consistent across tasks.
- Verification: Every production module has a failing-test step, implementation step, passing-test step, and commit step.
