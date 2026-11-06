---
card_id: open-webui-2026-04-24-e6a0c5
date: '2026-04-24'
description: "Open WebUI · 2026-04-24 · Other changes: 13 changes in v0.9.2 — \U0001F525
  **Firecrawl v2 API.** Firecrawl web loading now uses the v2 API directly with proper
  retry…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 56524ed959eaed964d24b5c5577ff0090233c953a6b3eff7f1a66b421ed561d1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-24-e6a0c5
  comparison: ''
  date: '2026-04-24'
  description: 'Open WebUI — v0.9.2: 13 other changes'
  evidence:
  - quote: "\U0001F525 **Firecrawl v2 API.** Firecrawl web loading now uses the v2
      API directly with proper retry logic, exponential backoff on rate limits, and
      configurable timeout handling, improving reliability for both cloud and self-hosted
      Firecrawl setups. [#23934](https://github.com/open-webui/open-webui/pull/23934)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F4DA **Source overflow indicator.** The Sources button now shows
      a +N badge when more than three sources are available, so hidden sources are
      clearly indicated in chat responses. [#23918](https://github.com/open-webui/open-webui/pull/23918)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F4CA **Telemetry gauge reliability.** OpenTelemetry user gauge callbacks
      now use synchronous database queries directly, eliminating cross-thread async
      bridging issues that could cause silent failures in metric collection."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F310 **Translation updates.** Translations for Finnish, Korean,
      Portuguese (Brazil), and Dutch were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F5C4️ **Async database driver migration.** The async database backend
      now uses psycopg (v3) instead of asyncpg, eliminating brittle SSL parameter
      translation and supporting native libpq connection strings including `sslmode`,
      `options`, and `target_session_attrs` without any stripping or conversion."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F433 **Docker ARM64 reliability.** Docker images built for arm64
      via QEMU cross-compilation no longer produce 0-byte corrupted Python dependencies.
      `UV_LINK_MODE=copy` is now set in the Dockerfile to force reliable file installation."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F6E0️ **Throttle request handling.** Request handling no longer
      fails when user activity status updates are throttled with a non-zero interval.
      [#23979](https://github.com/open-webui/open-webui/pull/23979)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F507 **Fetch URL null content guard.** The `fetch_url` built-in
      tool now safely handles `None` content returned by web loaders instead of crashing
      with a `TypeError`."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F4E1 **Cancelled response stream cleanup.** Cancelled chat generation
      now explicitly closes the upstream response body iterator, preventing orphaned
      async generators from spinning in anyio internals."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F4FB **Redis notification compatibility.** Redis pub/sub now handles
      missing or incompatible `client_name` support more gracefully, preventing connection
      errors with certain Redis configurations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: ⚙️ **psycopg v3 async driver.** The async database driver has been migrated
      from `asyncpg` to `psycopg` (v3). This is a transparent change for most deployments,
      but custom connection strings with `asyncpg`-specific parameters may need adjustment.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F511 **Brotli dependency update.** Brotli has been updated to address
      CVE-2025-6176."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  - quote: "\U0001F5A5️ **Windows startup script.** The Windows startup batch script
      has been updated for improved compatibility."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-other-changes-in-v0-9-2
  source_release: open-webui-2026-04-24-v0-9-2-github-313142735-f0842502
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in v0.9.2
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|open-webui-2026-04-24-v0-9-2-github-313142735-f0842502]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in v0.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in v0.9.2

**Open WebUI** · 2026-04-24 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.2) · from [[Releases/Open WebUI/open-webui-2026-04-24-v0-9-2-github-313142735-f0842502|v0.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔥 **Firecrawl v2 API.** Firecrawl web loading now uses the v2 API directly with proper retry logic, exponential backoff on rate limits, and configurable timeout handling, improving reliability for both cloud and self-hosted Firecrawl setups. [#23934](https://github.com/open-webui/open-webui/pull/23934)

> 📚 **Source overflow indicator.** The Sources button now shows a +N badge when more than three sources are available, so hidden sources are clearly indicated in chat responses. [#23918](https://github.com/open-webui/open-webui/pull/23918)

> 📊 **Telemetry gauge reliability.** OpenTelemetry user gauge callbacks now use synchronous database queries directly, eliminating cross-thread async bridging issues that could cause silent failures in metric collection.

> 🌐 **Translation updates.** Translations for Finnish, Korean, Portuguese (Brazil), and Dutch were enhanced and expanded.

> 🗄️ **Async database driver migration.** The async database backend now uses psycopg (v3) instead of asyncpg, eliminating brittle SSL parameter translation and supporting native libpq connection strings including `sslmode`, `options`, and `target_session_attrs` without any stripping or conversion.

> 🐳 **Docker ARM64 reliability.** Docker images built for arm64 via QEMU cross-compilation no longer produce 0-byte corrupted Python dependencies. `UV_LINK_MODE=copy` is now set in the Dockerfile to force reliable file installation.

> 🛠️ **Throttle request handling.** Request handling no longer fails when user activity status updates are throttled with a non-zero interval. [#23979](https://github.com/open-webui/open-webui/pull/23979)

> 🔇 **Fetch URL null content guard.** The `fetch_url` built-in tool now safely handles `None` content returned by web loaders instead of crashing with a `TypeError`.

> 📡 **Cancelled response stream cleanup.** Cancelled chat generation now explicitly closes the upstream response body iterator, preventing orphaned async generators from spinning in anyio internals.

> 📻 **Redis notification compatibility.** Redis pub/sub now handles missing or incompatible `client_name` support more gracefully, preventing connection errors with certain Redis configurations.

> ⚙️ **psycopg v3 async driver.** The async database driver has been migrated from `asyncpg` to `psycopg` (v3). This is a transparent change for most deployments, but custom connection strings with `asyncpg`-specific parameters may need adjustment.

> 🔑 **Brotli dependency update.** Brotli has been updated to address CVE-2025-6176.

> 🖥️ **Windows startup script.** The Windows startup batch script has been updated for improved compatibility.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-24-2-memory-and-personalization-changes-in-v0-9-2|2 Memory and Personalization changes in v0.9.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-24-4-model-support-changes-in-v0-9-2|4 Model Support changes in v0.9.2]] · Model Support
- [[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|🧩 Automation model detection. The create_automation tool now correctly detects…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-24-3-reliability-and-performance-changes-in-v0-9-2|3 Reliability and Performance changes in v0.9.2]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-24-3-context-window-changes-in-v0-9-2|3 Context Window changes in v0.9.2]] · Context Window
- [[Changes/Open WebUI/2026-04-24-2-apps-and-integrations-changes-in-v0-9-2|2 Apps and Integrations changes in v0.9.2]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-24-2-editor-experience-changes-in-v0-9-2|2 Editor Experience changes in v0.9.2]] · Editor Experience
- [[Changes/Open WebUI/2026-04-24-3-account-and-access-changes-in-v0-9-2|3 Account and Access changes in v0.9.2]] · Account and Access
- [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-24-e6a0c5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-24-13-other-changes-in-v0-9-2.md%0ACard%20ID%3A%20open-webui-2026-04-24-e6a0c5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->