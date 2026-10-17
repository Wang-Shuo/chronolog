---
card_id: cursor-2026-06-04-bfc264
date: '2026-06-04'
description: 'Cursor · 2026-06-04 · Agent Mode: 5 changes in Custom stores, custom
  tools, and auto-review for the Cursor SDK — Safe checkpoints on dispose: Disposing
  a local…'
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
impact: incremental
kind: digest
machine_hash: e73e31660f57aef61b9f1c7a642b8ae8a350cb5449bb1684f6e5b1dc4a061bbf
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-06-04-bfc264
  comparison: ''
  date: '2026-06-04'
  description: 'Cursor — Custom stores, custom tools, and auto-review for the Cursor
    SDK: 5 Agent Mode changes'
  evidence:
  - quote: 'Safe checkpoints on dispose: Disposing a local agent no longer removes
      checkpoint data when a root reference is missing but checkpoint blobs still
      exist. The agent directory is only cleared when there''s genuinely nothing left
      to keep.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: 'Cloud streaming over HTTP/1.1: Cloud agent sessions now stream correctly
      on HTTP/1.1 transports used by some proxies, older Node fetch stacks, and certain
      CI images. HTTP/2 behavior is unchanged.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: 'Lighter import: Importing @cursor/sdk no longer eagerly loads the full
      local agent stack. Cloud-only and type-only consumers skip the local runtime
      cost until the first local call, with no API change. The first local call pays
      a one-time import, then stays cached.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: 'Workspace-scoped list_runs: Client, AsyncClient, and Agent.list_runs take
      an optional cwd, and the bridge falls back to its launch workspace. This fixes
      spurious "agent not found" results when the bridge runs as a subprocess.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  - quote: 'Clearer not-found errors: Looking up an agent that isn''t in the resolved
      workspace returns a clear not-found error instead of an opaque internal error.'
    source_release: https://cursor.com/changelog/sdk-updates-jun-2026
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cursor
  product_name: Cursor
  slug: 5-agent-mode-changes-in-custom-stores-custom-tools
  source_release: cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856
  source_type: cursor_changelog
  theme: agent-mode
  title: 5 Agent Mode changes in Custom stores, custom tools…
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]]'
- '[[Changes/Cursor/2026-06-04-auto-review|Auto-review]]'
- '[[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
source_type: cursor_changelog
theme: agent-mode
title: 5 Agent Mode changes in Custom stores, custom tools…
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in Custom stores, custom tools…

**Cursor** · 2026-06-04 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://cursor.com/changelog/sdk-updates-jun-2026) · from [[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|Custom stores, custom tools, and auto-review for the Cursor SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Safe checkpoints on dispose: Disposing a local agent no longer removes checkpoint data when a root reference is missing but checkpoint blobs still exist. The agent directory is only cleared when there's genuinely nothing left to keep.

> Cloud streaming over HTTP/1.1: Cloud agent sessions now stream correctly on HTTP/1.1 transports used by some proxies, older Node fetch stacks, and certain CI images. HTTP/2 behavior is unchanged.

> Lighter import: Importing @cursor/sdk no longer eagerly loads the full local agent stack. Cloud-only and type-only consumers skip the local runtime cost until the first local call, with no API change. The first local call pays a one-time import, then stays cached.

> Workspace-scoped list_runs: Client, AsyncClient, and Agent.list_runs take an optional cwd, and the bridge falls back to its launch workspace. This fixes spurious "agent not found" results when the bridge runs as a subprocess.

> Clearer not-found errors: Looking up an agent that isn't in the resolved workspace returns a clear not-found error instead of an opaque internal error.

Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Safety and Privacy
- [[Changes/Cursor/2026-06-04-bundled-ripgrep-local-shell-runs-use-the-bundled-platform-rg-binary-without-modi|Bundled ripgrep: Local shell runs use the bundled platform rg binary without…]] · Mobile and Desktop
- [[Changes/Cursor/2026-06-04-reliability-performance-and-platform-improvements|Reliability, performance, and platform improvements]] · Reliability and Performance
- [[Changes/Cursor/2026-06-04-reliable-wait-on-local-runs-local-runs-no-longer-resolve-wait-before-the-termina|Reliable wait() on local runs]] · Automation and Scheduling
- [[Changes/Cursor/2026-06-04-jsonl-and-custom-stores|JSONL and custom stores]] · Agent Mode
- [[Changes/Cursor/2026-06-04-auto-review|Auto-review]] · Agent Mode
- [[Changes/Cursor/2026-06-04-run-correlation-every-send-now-carries-a-platform-generated-requestid-exposed-on|Run correlation: Every send() now carries a platform-generated requestId, exposed…]] · Memory and Personalization
- [[Changes/Cursor/2026-06-04-nested-subagents|Nested subagents]] · Agent Mode
- [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]] · Apps and Integrations
- [[Changes/Cursor/2026-06-04-2-apps-and-integrations-changes-in-custom-stores-custom-tools|2 Apps and Integrations changes in Custom stores, custom tools…]] · Apps and Integrations
- [[Changes/Cursor/2026-06-04-0-1-6-release-and-analytics-cursor-sdk-0-1-6-documents-the-buildkite-release-pat|0.1.6 release and analytics]] · Files and Data
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-06-04-bfc264&body=Card%3A%20Changes%2FCursor%2F2026-06-04-5-agent-mode-changes-in-custom-stores-custom-tools.md%0ACard%20ID%3A%20cursor-2026-06-04-bfc264%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fsdk-updates-jun-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->