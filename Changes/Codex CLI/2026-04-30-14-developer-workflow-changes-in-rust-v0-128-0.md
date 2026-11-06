---
card_id: codex-cli-2026-04-30-915497
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Developer Workflow: 14 changes in 0.128.0 —
  Added `codex update`, configurable TUI keymaps, plan-mode nudges, action-required
  terminal…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1139
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 23996cbf0512d6cb965609de2a80b907ed9de64f55982ef6552b180b616d07db
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-915497
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 14 Developer Workflow changes'
  evidence:
  - quote: 'Added `codex update`, configurable TUI keymaps, plan-mode nudges, action-required
      terminal titles, and active-turn `/statusline` and `/title` edits. (#19933,
      #18593, #19901, #18372, #19917)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Improved TUI reliability around terminal resize reflow, markdown list
      spacing, slash-command popup layout, keyboard cleanup, shell-mode escape, and
      working status updates. (#18575, #19706, #19511, #19625, #19986, #19939)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Hardened managed network behavior for deferred denials, proxy bypass defaults,
      resolved target checks, IPv6 host matching, and `git -C` approval handling.
      (#19184, #20002, #19999, #19995, #20085)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19511 Keep slash command popup columns stable while scrolling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18575 fix(tui): reflow scrollback on terminal resize @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19640 [codex] remove responses command @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19618 Persist shell mode commands in prompt history @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19491 Streamline account and command handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19874 [codex-backend] Prefer state git metadata in filtered thread lists
      @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18372 Show action required in terminal title @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19933 Add `codex update` command @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19986 fix(tui): let esc exit empty shell mode @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20085 fix: don''t auto approve git -C ... @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20228 [codex-backend] Prefer sqlite git info for rollout-path reads @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-developer-workflow-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: developer-workflow
  title: 14 Developer Workflow changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-29-added-first-class-run-streaming-with-sse-events-reconnect-support-via-last-event|Added
  first-class run streaming with SSE events, reconnect support…]]'
- '[[Changes/Dify/2026-04-29-2-developer-workflow-changes-in-1-14-0|2 Developer Workflow
  changes in 1.14.0]]'
- '[[Changes/Windsurf/2026-04-29-devin-for-terminal|Devin for Terminal]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: developer-workflow
title: 14 Developer Workflow changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Developer Workflow changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `codex update`, configurable TUI keymaps, plan-mode nudges, action-required terminal titles, and active-turn `/statusline` and `/title` edits. (#19933, #18593, #19901, #18372, #19917)

> Improved TUI reliability around terminal resize reflow, markdown list spacing, slash-command popup layout, keyboard cleanup, shell-mode escape, and working status updates. (#18575, #19706, #19511, #19625, #19986, #19939)

> Hardened managed network behavior for deferred denials, proxy bypass defaults, resolved target checks, IPv6 host matching, and `git -C` approval handling. (#19184, #20002, #19999, #19995, #20085)

> #19511 Keep slash command popup columns stable while scrolling @etraut-openai

> #18575 fix(tui): reflow scrollback on terminal resize @fcoury-oai

> #19640 [codex] remove responses command @tibo-openai

> #19618 Persist shell mode commands in prompt history @etraut-openai

> #19491 Streamline account and command handlers @pakrym-oai

> #19874 [codex-backend] Prefer state git metadata in filtered thread lists @joeytrasatti-openai

> #18372 Show action required in terminal title @canvrno-oai

> #19933 Add `codex update` command @etraut-openai

> #19986 fix(tui): let esc exit empty shell mode @fcoury-oai

> #20085 fix: don't auto approve git -C ... @owenlin0

> #20228 [codex-backend] Prefer sqlite git info for rollout-path reads @joeytrasatti-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-29 · Windsurf · [[Changes/Windsurf/2026-04-29-devin-for-terminal|Devin for Terminal]]
- Later: 2026-05-01 · Claude Code · [[Changes/Claude Code/2026-05-01-3-developer-workflow-changes-in-v2-1-126|3 Developer Workflow changes in v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-915497&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-915497%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->