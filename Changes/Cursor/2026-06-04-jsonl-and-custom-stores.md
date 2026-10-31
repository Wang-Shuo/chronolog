---
card_id: cursor-2026-06-04-324b8e
date: '2026-06-04'
description: 'Cursor · 2026-06-04 · Agent Mode: Both SDKs persist agent and run metadata
  so you can resume an agent after a process restart. Until now, that store was…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1064
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 2bb716bec623be206a4131d31c7b5f5adb485fb8b417203ffda889cea85e5faa
product: cursor
product_name: Cursor
record:
  ai_generated: true
  card_id: cursor-2026-06-04-324b8e
  comparison: ''
  confidence: low
  date: '2026-06-04'
  description: 'Cursor — Custom stores, custom tools, and auto-review for the Cursor
    SDK: Both SDKs persist agent and run metadata so you can resume an agent after
    a process restart. Until now, that store was SQLite. You can now opt into a JSONL
    store instead, which writes a plain, append-only file you can read, diff, and
    check into version control. Both SqliteLocalAgentStore and JsonlLocalAgentStore
    are exported directly.'
  evidence:
  - quote: Both SDKs persist agent and run metadata so you can resume an agent after
      a process restart. Until now, that store was SQLite. You can now opt into a
      JSONL store instead, which writes a plain, append-only file you can read, diff,
      and check into version control. Both SqliteLocalAgentStore and JsonlLocalAgentStore
      are exported directly.
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: If neither default fits your setup, implement the public LocalAgentStore
      interface and pass it through local.store. Build an in-memory store for ephemeral
      CI runs, or back persistence with Postgres when you want agent state to live
      next to the rest of your application data. The Python SDK exposes host, JSONL,
      and composed JSONL stores through the bridge.
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: cursor
  product_name: Cursor
  slug: jsonl-and-custom-stores
  source_release: cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856
  source_type: cursor_changelog
  theme: agent-mode
  title: JSONL and custom stores
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude
  agents rows now show done/total before the detail when work is fanned out]]'
- '[[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode
  changes in v2.1.163]]'
- '[[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added
  the ability for agents to embed buttons in canvases that will run a specific…]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
source_type: cursor_changelog
theme: agent-mode
title: JSONL and custom stores
type: change
---

<!-- chronolog:begin region="header" -->
# JSONL and custom stores

**Cursor** · 2026-06-04 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://cursor.com/changelog/sdk-updates-jun-2026) · from [[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|Custom stores, custom tools, and auto-review for the Cursor SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Both SDKs persist agent and run metadata so you can resume an agent after a process restart. Until now, that store was SQLite. You can now opt into a JSONL store instead, which writes a plain, append-only file you can read, diff, and check into version control. Both SqliteLocalAgentStore and JsonlLocalAgentStore are exported directly.
>
> If neither default fits your setup, implement the public LocalAgentStore interface and pass it through local.store. Build an in-memory store for ephemeral CI runs, or back persistence with Postgres when you want agent state to live next to the rest of your application data. The Python SDK exposes host, JSONL, and composed JSONL stores through the bridge.
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Safety and Privacy
- [[Changes/Cursor/2026-06-04-bundled-ripgrep-local-shell-runs-use-the-bundled-platform-rg-binary-without-modi|Bundled ripgrep: Local shell runs use the bundled platform rg binary without…]] · Mobile and Desktop
- [[Changes/Cursor/2026-06-04-reliability-performance-and-platform-improvements|Reliability, performance, and platform improvements]] · Reliability and Performance
- [[Changes/Cursor/2026-06-04-reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina|Reliable wait() on local runs]] · Automation and Scheduling
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
## Nearby in Agent Mode

- Earlier: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added the ability for agents to embed buttons in canvases that will run a specific…]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-with-canvases-agents-can-create-interactive-artifacts-like-dashboards-reports-an|With canvases, agents can create interactive artifacts like dashboards, reports…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-06-04-324b8e&body=Card%3A%20Changes%2FCursor%2F2026-06-04-jsonl-and-custom-stores.md%0ACard%20ID%3A%20cursor-2026-06-04-324b8e%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fsdk-updates-jun-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->