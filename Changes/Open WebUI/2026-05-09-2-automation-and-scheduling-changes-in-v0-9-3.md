---
card_id: open-webui-2026-05-09-68ffd4
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Automation and Scheduling: 2 changes in v0.9.3
  — \U0001FA9F **Windows PostgreSQL startup compatibility.** Windows pip installs
  using…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2425
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dff61d3d83373f1242018cd1a08688c2e3cac5f2d99920518ce58df15c5c436a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-68ffd4
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 2 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001FA9F **Windows PostgreSQL startup compatibility.** Windows pip installs
      using PostgreSQL now start reliably with psycopg async by using a compatible
      event loop policy instead of the default Proactor loop. [Commit](https://github.com/open-webui/open-webui/commit/7eaecbad5a0913ed04ca3bc10c930bb051dd2bd9),
      [#24152](https://github.com/open-webui/open-webui/issues/24152)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F916 **Automation update tool reliability.** Updating existing automations
      in chat now works correctly instead of failing with a missing method error.
      [Commit](https://github.com/open-webui/open-webui/commit/f39f4a86aedc2769d8268670a020b1f3c16776dd),
      [#24405](https://github.com/open-webui/open-webui/issues/24405#issuecomment-4408011166)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-automation-and-scheduling-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: automation-scheduling
  title: 2 Automation and Scheduling changes in v0.9.3
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-04-24-automation-model-detection-the-create-automation-tool-now-correctly-detects-the|\U0001F9E9
  Automation model detection. The create_automation tool now correctly detects…]]"
- '[[Changes/Dify/2026-04-29-3-automation-and-scheduling-changes-in-1-14-0|3 Automation
  and Scheduling changes in 1.14.0]]'
- '[[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated
  OpenTelemetry event now fires for user-typed slash…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: automation-scheduling
title: 2 Automation and Scheduling changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Automation and Scheduling changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪟 **Windows PostgreSQL startup compatibility.** Windows pip installs using PostgreSQL now start reliably with psycopg async by using a compatible event loop policy instead of the default Proactor loop. [Commit](https://github.com/open-webui/open-webui/commit/7eaecbad5a0913ed04ca3bc10c930bb051dd2bd9), [#24152](https://github.com/open-webui/open-webui/issues/24152)

> 🤖 **Automation update tool reliability.** Updating existing automations in chat now works correctly instead of failing with a missing method error. [Commit](https://github.com/open-webui/open-webui/commit/f39f4a86aedc2769d8268670a020b1f3c16776dd), [#24405](https://github.com/open-webui/open-webui/issues/24405#issuecomment-4408011166)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-05-01 · Claude Code · [[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated OpenTelemetry event now fires for user-typed slash…]]
- Later: 2026-05-12 · Dify · [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-68ffd4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-68ffd4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->