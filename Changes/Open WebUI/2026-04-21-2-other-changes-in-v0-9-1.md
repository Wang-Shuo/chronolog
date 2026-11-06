---
card_id: open-webui-2026-04-21-871b19
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Other changes: 2 changes in v0.9.1 — \U0001F41B
  **Missing `aiosqlite` dependency.** Fixed a startup crash (`ModuleNotFoundError:
  No module…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a5d899904a4b4a1d0de0de814a3e2d41a09f62df33b8bf6ed836f430d36490d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-871b19
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.1: 2 other changes'
  evidence:
  - quote: "\U0001F41B **Missing `aiosqlite` dependency.** Fixed a startup crash (`ModuleNotFoundError:
      No module named 'aiosqlite'`) when installing Open WebUI via `pip` or `uv` by
      adding the missing `aiosqlite` package to `pyproject.toml`. The dependency was
      listed in `requirements.txt` but not in the published package metadata, so it
      was not installed automatically. [#23916](https://github.com/open-webui/open-webui/issues/23916)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.1
  - quote: "\U0001F41B **Missing `asyncpg` dependency.** Added the missing `asyncpg`
      package to `pyproject.toml` to prevent the same startup crash for PostgreSQL
      users. Like `aiosqlite`, it was present in `requirements.txt` but absent from
      the published package dependencies."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-other-changes-in-v0-9-1
  source_release: open-webui-2026-04-21-v0-9-1-github-311660265-e316987f
  source_type: github_releases
  theme: uncategorized
  title: 2 other changes in v0.9.1
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-1-github-311660265-e316987f|open-webui-2026-04-21-v0-9-1-github-311660265-e316987f]]'
source_type: github_releases
theme: uncategorized
title: 2 other changes in v0.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 other changes in v0.9.1

**Open WebUI** · 2026-04-21 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.1) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-1-github-311660265-e316987f|v0.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🐛 **Missing `aiosqlite` dependency.** Fixed a startup crash (`ModuleNotFoundError: No module named 'aiosqlite'`) when installing Open WebUI via `pip` or `uv` by adding the missing `aiosqlite` package to `pyproject.toml`. The dependency was listed in `requirements.txt` but not in the published package metadata, so it was not installed automatically. [#23916](https://github.com/open-webui/open-webui/issues/23916)

> 🐛 **Missing `asyncpg` dependency.** Added the missing `asyncpg` package to `pyproject.toml` to prevent the same startup crash for PostgreSQL users. Like `aiosqlite`, it was present in `requirements.txt` but absent from the published package dependencies.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-871b19&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-2-other-changes-in-v0-9-1.md%0ACard%20ID%3A%20open-webui-2026-04-21-871b19%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->