---
card_id: codex-cli-2026-07-08-886acc
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Context Window: 12 changes in 0.143.0 — #29249
  [codex] migrate environment context to model world state @pakrym-oai'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2485
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 197c3bdd7cc5f270de512e277c2e103cbd4edce33a8cf3f54a343e1446979571
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-886acc
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 12 Context Window changes'
  evidence:
  - quote: '#29249 [codex] migrate environment context to model world state @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29494 core: wrap token budget window context @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29527 core: use turn-owned world state for inline compaction @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29519 core: persist initial context window metadata @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29664 refactor: extract context window token status @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29665 fix: scope context remaining to body window @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29739 Update new_context_window instructions @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29743 core: reset context for token budget compaction @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29762 [codex] Reuse compacted history replacement for new context windows
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29815 [codex] Remove auto-compaction opt-out @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29936 core: add configurable <context_window_guidance> message @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31252 [tui] Truncate hook context in conversation history @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-context-window-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: context-window
  title: 12 Context Window changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-07-warn-when-static-context-uses-most-of-the-prompt-budget-and-block-requests-when|Warn
  when static context uses most of the prompt budget and block requests…]]'
- '[[Changes/OpenCode/2026-07-07-core-better-classify-z-ai-context-window-overflow-errors-so-oversized-requests-s|Core
  Better classify Z.ai context-window overflow errors so oversized requests…]]'
- '[[Changes/Claude Code/2026-07-08-improved-auto-mode-to-ask-before-running-rm-rf-on-a-variable-it-can-t-resolve-fr|Improved
  auto mode to ask before running rm -rf on a variable it can''t resolve…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: context-window
title: 12 Context Window changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Context Window changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #29249 [codex] migrate environment context to model world state @pakrym-oai

> #29494 core: wrap token budget window context @bolinfest

> #29527 core: use turn-owned world state for inline compaction @sayan-oai

> #29519 core: persist initial context window metadata @bolinfest

> #29664 refactor: extract context window token status @bolinfest

> #29665 fix: scope context remaining to body window @bolinfest

> #29739 Update new_context_window instructions @andmis

> #29743 core: reset context for token budget compaction @bolinfest

> #29762 [codex] Reuse compacted history replacement for new context windows @pakrym-oai

> #29815 [codex] Remove auto-compaction opt-out @rhan-oai

> #29936 core: add configurable \<context_window_guidance> message @bolinfest

> #31252 [tui] Truncate hook context in conversation history @abhinav-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5 Account and Access changes in rust-v0.143.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model Support changes in rust-v0.143.0]] · Model Support
- [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-07-08 · Claude Code · [[Changes/Claude Code/2026-07-08-improved-auto-mode-to-ask-before-running-rm-rf-on-a-variable-it-can-t-resolve-fr|Improved auto mode to ask before running rm -rf on a variable it can't resolve…]]
- Later: 2026-07-09 · Codex CLI · [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-886acc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-12-context-window-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-886acc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->