---
card_id: cursor-2026-06-04-1bdce3
date: '2026-06-04'
description: 'Cursor · 2026-06-04 · Automation and Scheduling: Reliable wait() on
  local runs: Local runs no longer resolve wait() before the terminal result is written…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2451
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ee3e31de607c151e113055612b4ae127b32e10620fc41a6892905d7b82340116
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-06-04-1bdce3
  comparison: ''
  date: '2026-06-04'
  description: 'Cursor — Custom stores, custom tools, and auto-review for the Cursor
    SDK: Reliable wait() on local runs: Local runs no longer resolve wait() before
    the terminal result is written. Hydration keeps refreshing until the run reaches
    a final state, so automation reads a complete result.'
  evidence:
  - quote: 'Reliable wait() on local runs: Local runs no longer resolve wait() before
      the terminal result is written. Hydration keeps refreshing until the run reaches
      a final state, so automation reads a complete result.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cursor
  product_name: Cursor
  slug: reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina
  source_release: cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856
  source_type: cursor_changelog
  theme: automation-scheduling
  theme_matches:
  - matched_terms:
    - automation
    score: 50
    theme: automation-scheduling
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: Reliable wait() on local runs
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-02-render-scheduled-reminders-distinctly-in-the-tui-expose-cron-fired-events-to-sdk|Render
  scheduled reminders distinctly in the TUI, expose cron fired events to SDK…]]'
- '[[Changes/Devin/2026-06-03-personal-automations|Personal Automations]]'
- '[[Changes/Devin/2026-06-03-v3-api-organization-members-and-automations|V3 API:
  Organization Members and Automations]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
source_type: cursor_changelog
theme: automation-scheduling
title: Reliable wait() on local runs
type: change
---

<!-- chronolog:begin region="header" -->
# Reliable wait() on local runs

**Cursor** · 2026-06-04 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://cursor.com/changelog/sdk-updates-jun-2026) · from [[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|Custom stores, custom tools, and auto-review for the Cursor SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Reliable wait() on local runs: Local runs no longer resolve wait() before the terminal result is written. Hydration keeps refreshing until the run reaches a final state, so automation reads a complete result.
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Safety and Privacy
- [[Changes/Cursor/2026-06-04-bundled-ripgrep-local-shell-runs-use-the-bundled-platform-rg-binary-without-modi|Bundled ripgrep: Local shell runs use the bundled platform rg binary without…]] · Mobile and Desktop
- [[Changes/Cursor/2026-06-04-reliability-performance-and-platform-improvements|Reliability, performance, and platform improvements]] · Reliability and Performance
- [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Agent Mode
- [[Changes/Cursor/2026-06-04-auto-review|Auto-review]] · Agent Mode
- [[Changes/Cursor/2026-06-04-run-correlation-every-send-now-carries-a-platform-generated-requestid-exposed-on|Run correlation: Every send() now carries a platform-generated requestId, exposed…]] · Reliability and Performance
- [[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]] · Agent Mode
- [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]] · Apps and Integrations
- [[Changes/Cursor/2026-06-04-2-apps-and-integrations-changes-in-custom-stores-custom-tools|2 Apps and Integrations changes in Custom stores, custom tools…]] · Apps and Integrations
- [[Changes/Cursor/2026-06-04-5-agent-mode-changes-in-custom-stores-custom-tools|5 Agent Mode changes in Custom stores, custom tools…]] · Agent Mode
- [[Changes/Cursor/2026-06-04-0-1-6-release-and-analytics-cursor-sdk-0-1-6-documents-the-buildkite-release-pat|0.1.6 release and analytics]] · Files and Data
- [[Changes/Cursor/2026-06-04-self-contained-typescript-types-published-d-ts-files-no-longer-reference-unpubli|Self-contained TypeScript types]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-06-03 · Devin · [[Changes/Devin/2026-06-03-v3-api-organization-members-and-automations|V3 API: Organization Members and Automations]]
- Later: 2026-06-05 · Devin · [[Changes/Devin/2026-06-05-scratchpad-moved-under-mcps-in-automations|Scratchpad Moved Under MCPs in Automations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-06-04-1bdce3&body=Card%3A%20Changes%2FCursor%2F2026-06-04-reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina.md%0ACard%20ID%3A%20cursor-2026-06-04-1bdce3%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fsdk-updates-jun-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->