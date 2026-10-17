---
card_id: cursor-2026-06-04-36bb12
date: '2026-06-04'
description: 'Cursor · 2026-06-04 · Agent Mode: By default, a local SDK agent runs
  tool calls without asking for approval, since there''s no human in the loop in a
  headless…'
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
machine_hash: fdbf581ce96b81cf4dd4308959216407e634d12ff2a0989b03aa5e21334e254f
product: cursor
product_name: Cursor
record:
  ai_generated: true
  card_id: cursor-2026-06-04-36bb12
  comparison: ''
  confidence: low
  date: '2026-06-04'
  description: 'Cursor — Custom stores, custom tools, and auto-review for the Cursor
    SDK: By default, a local SDK agent runs tool calls without asking for approval,
    since there''s no human in the loop in a headless run. Set local.autoReview to
    route those calls through auto-review instead. A classifier decides which calls
    run automatically and which to hold back, rather than bypassing review entirely.'
  evidence:
  - quote: By default, a local SDK agent runs tool calls without asking for approval,
      since there's no human in the loop in a headless run. Set local.autoReview to
      route those calls through auto-review instead. A classifier decides which calls
      run automatically and which to hold back, rather than bypassing review entirely.
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: You steer that classifier with natural-language instructions in permissions.json.
      The autoRun.allow_instructions field describes call shapes to lean toward allowing,
      and autoRun.block_instructions describes the ones to hold for review. For example,
      you can allow read-only inspections of build artifacts while always pausing
      on destructive operations like deletes.
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: '"Read-only inspections of build artifacts under ./dist are fine."'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: '"Always pause delete operations so I get a chance to review them."'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: cursor
  product_name: Cursor
  slug: auto-review
  source_release: cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856
  source_type: cursor_changelog
  theme: agent-mode
  title: Auto-review
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode
  changes in v2.1.163]]'
- '[[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added
  the ability for agents to embed buttons in canvases that will run a specific…]]'
- '[[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
source_type: cursor_changelog
theme: agent-mode
title: Auto-review
type: change
---

<!-- chronolog:begin region="header" -->
# Auto-review

**Cursor** · 2026-06-04 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://cursor.com/changelog/sdk-updates-jun-2026) · from [[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|Custom stores, custom tools, and auto-review for the Cursor SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> By default, a local SDK agent runs tool calls without asking for approval, since there's no human in the loop in a headless run. Set local.autoReview to route those calls through auto-review instead. A classifier decides which calls run automatically and which to hold back, rather than bypassing review entirely.
>
> You steer that classifier with natural-language instructions in permissions.json. The autoRun.allow_instructions field describes call shapes to lean toward allowing, and autoRun.block_instructions describes the ones to hold for review. For example, you can allow read-only inspections of build artifacts while always pausing on destructive operations like deletes.
>
> "Read-only inspections of build artifacts under ./dist are fine."
>
> "Always pause delete operations so I get a chance to review them."
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Safety and Privacy
- [[Changes/Cursor/2026-06-04-bundled-ripgrep-local-shell-runs-use-the-bundled-platform-rg-binary-without-modi|Bundled ripgrep: Local shell runs use the bundled platform rg binary without…]] · Mobile and Desktop
- [[Changes/Cursor/2026-06-04-reliability-performance-and-platform-improvements|Reliability, performance, and platform improvements]] · Reliability and Performance
- [[Changes/Cursor/2026-06-04-reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina|Reliable wait() on local runs]] · Automation and Scheduling
- [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Agent Mode
- [[Changes/Cursor/2026-06-04-run-correlation-every-send-now-carries-a-platform-generated-requestid-exposed-on|Run correlation: Every send() now carries a platform-generated requestId, exposed…]] · Memory and Personalization
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
- Later: 2026-06-05 · Cursor · [[Changes/Cursor/2026-06-05-ask-the-agent-to-make-one-match-the-other-remove-repeated-content-or-adjust-a-gr|Multi-select elements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-06-04-36bb12&body=Card%3A%20Changes%2FCursor%2F2026-06-04-auto-review.md%0ACard%20ID%3A%20cursor-2026-06-04-36bb12%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fsdk-updates-jun-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->