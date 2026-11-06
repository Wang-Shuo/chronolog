---
card_id: codex-cli-2026-02-04-088ac5
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Developer Workflow: 10 changes in 0.95.0 —
  `/plan` now accepts inline prompt arguments and pasted images, and slash-command…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1054
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c4c179e0cc6d0951917643eb0aeab088e0f3107108f083d350c2e96a460fcfd1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-088ac5
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.95.0: 10 Developer Workflow changes'
  evidence:
  - quote: '`/plan` now accepts inline prompt arguments and pasted images, and slash-command
      editing/highlighting in the TUI is more polished. (#10269)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: Shell-related tools can now run in parallel, improving multi-command execution
      throughput. (#10505)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: Shell executions now receive `CODEX_THREAD_ID`, so scripts and skills can
      detect the active thread/session. (#10096)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: Expanded TUI chat composer docs to cover slash-command arguments and attachment
      handling in plan/review flows. (#10269)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10382 nit: shell snapshot retention to 3 days @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10258 fix: unsafe auto-approval of git commands @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10145 make codex better at git @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10505 Enable parallel shell tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10096 Inject CODEX_THREAD_ID into the terminal environment @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10367 chore: add `codex debug app-server` tooling @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-developer-workflow-changes-in-rust-v0-95-0
  source_release: codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b
  source_type: github_releases
  theme: developer-workflow
  title: 10 Developer Workflow changes in rust-v0.95.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-03-2-developer-workflow-changes-in-v2-1-30|2 Developer
  Workflow changes in v2.1.30]]'
- '[[Changes/Claude Code/2026-02-03-added-debug-for-claude-to-help-troubleshoot-the-current-session|Added
  /debug for Claude to help troubleshoot the current session]]'
- '[[Changes/Claude Code/2026-02-04-reduced-layout-jitter-in-the-terminal-when-the-spinner-appears-and-disappears-du|Reduced
  layout jitter in the terminal when the spinner appears and disappears during…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b]]'
source_type: github_releases
theme: developer-workflow
title: 10 Developer Workflow changes in rust-v0.95.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Developer Workflow changes in rust-v0.95.0

**Codex CLI** · 2026-02-04 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.95.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/plan` now accepts inline prompt arguments and pasted images, and slash-command editing/highlighting in the TUI is more polished. (#10269)

> Shell-related tools can now run in parallel, improving multi-command execution throughput. (#10505)

> Shell executions now receive `CODEX_THREAD_ID`, so scripts and skills can detect the active thread/session. (#10096)

> Expanded TUI chat composer docs to cover slash-command arguments and attachment handling in plan/review flows. (#10269)

> #10382 nit: shell snapshot retention to 3 days @jif-oai

> #10258 fix: unsafe auto-approval of git commands @viyatb-oai

> #10145 make codex better at git @pash-openai

> #10505 Enable parallel shell tools @jif-oai

> #10096 Inject CODEX_THREAD_ID into the terminal environment @maxj-oai

> #10367 chore: add `codex debug app-server` tooling @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.95.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-10340-session-picker-shows-thread-name-if-set-pap-openai|♯10340 Session picker shows thread_name if set @pap-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Context Window
- [[Changes/Codex CLI/2026-02-04-10404-cleanup-collaboration-mode-variants-charley-oai|♯10404 Cleanup collaboration mode variants @charley-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-04-2-mobile-and-desktop-changes-in-rust-v0-95-0|2 Mobile and Desktop changes in rust-v0.95.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Model Support
- [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5 Apps and Integrations changes in rust-v0.95.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2 Search and Browsing changes in rust-v0.95.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-04-42-other-changes-in-rust-v0-95-0|42 other changes in rust-v0.95.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-04 · Claude Code · [[Changes/Claude Code/2026-02-04-reduced-layout-jitter-in-the-terminal-when-the-spinner-appears-and-disappears-du|Reduced layout jitter in the terminal when the spinner appears and disappears during…]]
- Later: 2026-02-04 · Codex CLI · [[Changes/Codex CLI/2026-02-04-constrained-requirement-values-now-include-source-provenance-enabling-source-awa|Constrained requirement values now include source provenance, enabling source-aware…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-088ac5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-088ac5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.95.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->