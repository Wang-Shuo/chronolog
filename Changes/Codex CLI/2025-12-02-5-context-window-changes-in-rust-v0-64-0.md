---
card_id: codex-cli-2025-12-02-44acfc
date: '2025-12-02'
description: 'Codex CLI · 2025-12-02 · Context Window: 5 changes in 0.64.0 — Threads
  and turns now include git info, current working directory, CLI version, source metadata…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2267
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ae9d5e7cc48673767ef1e83b82e2e2f060d1950acf2b95c260a2f10d198573a9
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-02-44acfc
  comparison: ''
  date: '2025-12-02'
  description: 'Codex CLI — 0.64.0: 5 Context Window changes'
  evidence:
  - quote: Threads and turns now include git info, current working directory, CLI
      version, source metadata, and propagate thread and turn IDs on every item and
      error. They emit new notifications for diffs, plan updates, token-usage changes,
      and compaction events. File-change items provide output deltas, and ImageView
      items render images inline.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Observability increases as command items expose process IDs and threads
      and turns emit token-usage and compaction events. Feedback metadata captures
      source information.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Compaction accounts for encrypted reasoning, handles token budgets accurately,
      and emits reliable token-usage and compaction events.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Account for encrypted reasoning for auto compaction by @aibrahim-oai in
      #7113'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat: add compaction event by @jif-oai in #7289'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-context-window-changes-in-rust-v0-64-0
  source_release: codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in rust-v0.64.0
  type: change
related_changes:
- '[[Changes/Lovable/2025-11-26-chat-suggestions|Chat suggestions]]'
- '[[Changes/Cline/2025-11-27-feat-context-add-context-window-error-detection-for-vercel-ai-gateway-by-shaper|feat(context):
  add context window error detection for vercel ai gateway]]'
- '[[Changes/Cline/2025-12-02-2-context-window-changes-in-v3-39-0|2 Context Window
  changes in v3.39.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in rust-v0.64.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in rust-v0.64.0

**Codex CLI** · 2025-12-02 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.64.0) · from [[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|0.64.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Threads and turns now include git info, current working directory, CLI version, source metadata, and propagate thread and turn IDs on every item and error. They emit new notifications for diffs, plan updates, token-usage changes, and compaction events. File-change items provide output deltas, and ImageView items render images inline.

> Observability increases as command items expose process IDs and threads and turns emit token-usage and compaction events. Feedback metadata captures source information.

> Compaction accounts for encrypted reasoning, handles token budgets accurately, and emits reliable token-usage and compaction events.

> Account for encrypted reasoning for auto compaction by @aibrahim-oai in #7113

> feat: add compaction event by @jif-oai in #7289

Source: https://github.com/openai/codex/releases/tag/rust-v0.64.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Model Support
- [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]] · Account and Access
- [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Agent Mode
- [[Changes/Codex CLI/2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0|4 Developer Workflow changes in rust-v0.64.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-02-execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session|Execution gains an experimental “exp” model, unified exec pruning to limit session…]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-02-3-editor-experience-changes-in-rust-v0-64-0|3 Editor Experience changes in rust-v0.64.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]] · Interface Experience
- [[Changes/Codex CLI/2025-12-02-46-other-changes-in-rust-v0-64-0|46 other changes in rust-v0.64.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2025-12-02 · Cline · [[Changes/Cline/2025-12-02-2-context-window-changes-in-v3-39-0|2 Context Window changes in v3.39.0]]
- Later: 2025-12-02 · Open WebUI · [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-02-44acfc&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-02-5-context-window-changes-in-rust-v0-64-0.md%0ACard%20ID%3A%20codex-cli-2025-12-02-44acfc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.64.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->