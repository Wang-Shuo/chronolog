---
card_id: cursor-2026-06-04-1bdce3
date: '2026-06-04'
description: 'Cursor · 2026-06-04 · Automation and Scheduling: Reliable wait() on
  local runs: Local runs no longer resolve wait() before the terminal result is written…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 884
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 9f413c576bb8b164fc9bee5d0be8ff52990f35dd9f5938d4ffb3c510a8db5298
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
- '[[Changes/GitHub Copilot CLI/2026-05-28-schedule-manager-hint-bar-text-no-longer-wraps-over-dialog-borders-when-entries|Schedule
  manager hint bar text no longer wraps over dialog borders when entries are added]]'
- "[[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|\U0001F518
  Bulk enable or disable automations. Automations can now be enabled or disabled…]]"
- '[[Changes/GitHub Copilot CLI/2026-06-02-experimental-schedule-prompts-with-every-and-after|/experimental
  schedule prompts with /every and /after]]'
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

- Earlier: 2026-06-02 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-02-experimental-schedule-prompts-with-every-and-after|/experimental schedule prompts with /every and /after]]
- Later: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-workflows-now-opens-immediately-even-while-a-turn-is-in-progress|/workflows now opens immediately even while a turn is in progress]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-06-04-1bdce3&body=Card%3A%20Changes%2FCursor%2F2026-06-04-reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina.md%0ACard%20ID%3A%20cursor-2026-06-04-1bdce3%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fsdk-updates-jun-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->