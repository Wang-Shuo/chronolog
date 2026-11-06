# Product expansion — 2026-11-06

The working vault now tracks **10 products**, with **1,998 releases**, **7,829
Change Cards** and **25 themes**. This adds 1,180 official release records and
5,087 cards to the existing ChatGPT, Claude Code and Cursor archive. The changes
are local; no commit, pull request or deployment was made.

| Added product | Releases | Cards | Archived announcement dates | Official source |
| --- | ---: | ---: | --- | --- |
| Codex CLI | 179 | 1,386 | 2025-06-30 → 2026-11-06 | [openai/codex](https://github.com/openai/codex/releases) |
| Gemini CLI | 160 | 627 | 2025-06-28 → 2026-11-04 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli/releases) |
| GitHub Copilot CLI | 193 | 1,198 | 2025-09-26 → 2026-11-06 | [github/copilot-cli](https://github.com/github/copilot-cli/releases) |
| Windsurf | 121 | 240 | 2025-04-02 → 2026-10-30 | [Devin Desktop stable changelog](https://docs.devin.ai/desktop/changelog) |
| Cline | 297 | 771 | 2024-07-28 → 2026-10-26 | [cline/cline](https://github.com/cline/cline/releases) |
| Aider | 93 | 344 | 2023-06-07 → 2025-08-09 | [Aider-AI/aider](https://github.com/Aider-AI/aider/releases) |
| OpenHands | 137 | 521 | 2024-06-04 → 2026-11-05 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands/releases) |

## Scope and source handling

- `_scripts/sources.yaml` now controls collection and public product eligibility.
  The sidebar, search index, graph, RSS audit and timeline filter styles no longer
  assume three products or an eight-product maximum.
- New GitHub sources include stable versioned application releases. Prereleases,
  drafts, separately tagged SDK/CLI packages and temporary evidence uploads are
  excluded. Codex uses 20-item API pages because 100-item responses returned 504.
- Windsurf's official URL redirects to Devin Desktop. The collector reads its
  official Markdown export, preserving version/date pairs and HTML anchors while
  excluding download widgets. The current endpoint starts in April 2025.
- CLI archives represent those named CLIs. Endpoint traversal is not proof of
  lifetime coverage or coverage of a vendor's other product surfaces. Each product
  page and About state the source limitations and acquisition timestamp.
- The original three product archives retain their previous acquisition dates.
  Aider's old latest-release date is upstream inactivity, not a failed fetch.
- Eight legacy Aider/OpenHands cards and four release pages were matched against
  `tests/fixtures/releases.json`, verified against their machine hashes and marked
  superseded through the existing reconciliation/transaction helpers. Their files
  remain locally available. Continue and Tabby remain disabled.
- GitHub author/PR attribution no longer affects theme classification or standalone
  titles; quoted evidence and stable identities retain the original text. Contributor
  lists and “Full Changelog” links are not changes. Generic “New”/“Added” sections
  do not merge unrelated features into one card.
- A protocol-less `www.openai.com` link in an official Codex quote is rendered with
  HTTPS; inline code and the stored evidence remain unchanged.

## Verification

Final run: `product-expansion-2026-11-06-r2`, **candidate-applied**, 8,961 files
applied after all gates passed. The separate fixture retirement changed 12 files.

- **506 tests passed**, including pagination through excluded releases, source-format
  failure handling, coverage metadata, attribution classification, catalog-driven
  publication, more than eight product filters and protocol-less source links.
- Vault validation checked **11,273 Markdown files** and **174,692 links**, with no
  errors; release/card counts match the merged input.
- Quartz built successfully. The publication audit checked **9,959 HTML pages** and
  **336,149 links**, confirmed **9,914 active indexed pages**, excluded fixtures and
  superseded pages, and verified all **30 RSS items**.
- Chrome showed all ten products in the Explorer. Codex CLI navigation opened its
  179-release product page. Selecting the tenth timeline filter showed only Windsurf
  entries. At 1440px and 390px, document width matched viewport width; the wide
  comparison table scrolls inside its container. Browser console: zero errors or
  warnings. Screenshots and exact check scope are in the evidence directory.
- **49 new prose candidates** remain in `_review/` (111 total); they are excluded from
  the public site. New product eras have not been editorially reviewed, and existing
  theme research summaries explicitly retain their original three-product scope.

## Evidence and replay

[Evidence directory](product-expansion-evidence/sha256.json) contains the compressed
live collection, final quality report, test/build logs, publication and vault audits,
fixture retirement manifest and browser evidence, with SHA-256 hashes.

The collection was fetched live on 2026-11-06; generation used that saved input and
is correctly labeled `replay` in the operations report. It does not count toward
seven-day scheduled-run acceptance.

```bash
.venv/bin/python -m _scripts.operations --mode generate \
  --run-id product-expansion-replay-unique \
  --output _pipeline/product-expansion-replay-unique \
  --collection docs/acceptance/product-expansion-evidence/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog
```

This builds and checks an isolated candidate. The normal reviewed deployment
workflow still governs publication to the live site.
