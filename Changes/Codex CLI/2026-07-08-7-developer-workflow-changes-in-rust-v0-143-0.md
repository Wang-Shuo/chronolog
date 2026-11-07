---
card_id: codex-cli-2026-07-08-d89fa7
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Developer Workflow: 7 changes in 0.143.0 —
  Preserved trailing realtime transcript text and terminal rollout events during shutdown…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2857
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1132663bf69d81ebb23817080d47f465977da521f5a578ed1afa70e2d621438
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-d89fa7
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 7 Developer Workflow changes'
  evidence:
  - quote: 'Preserved trailing realtime transcript text and terminal rollout events
      during shutdown. (#29918, #30144)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29720 ci: fail jobs that dirty the worktree @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30144 [codex] fix terminal rollout event durability @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30143 Let Codex consult user-level code-review-* skills. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30851 docs: add tag to fenced code block @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31066 chore: remove unused git-cliff configuration @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31267 chore(approvals) consolidate guardian calls for shell tools @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-developer-workflow-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-07-removed-the-startup-claude-command-missing-or-broken-warnings-they-now-appear-in|Removed
  the startup "claude command missing or broken" warnings]]'
- '[[Changes/GitHub Copilot CLI/2026-07-07-7-developer-workflow-changes-in-v1-0-69|7
  Developer Workflow changes in v1.0.69]]'
- '[[Changes/OpenCode/2026-07-07-desktop-make-terminal-shortcuts-take-priority-when-the-terminal-is-focused|Desktop
  Make terminal shortcuts take priority when the terminal is focused]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preserved trailing realtime transcript text and terminal rollout events during shutdown. (#29918, #30144)

> #29720 ci: fail jobs that dirty the worktree @anp-oai

> #30144 [codex] fix terminal rollout event durability @wiltzius-openai

> #30143 Let Codex consult user-level code-review-* skills. @anp-oai

> #30851 docs: add tag to fenced code block @bolinfest

> #31066 chore: remove unused git-cliff configuration @bolinfest

> #31267 chore(approvals) consolidate guardian calls for shell tools @dylan-hurd-oai

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
- [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Context Window
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-07 · OpenCode · [[Changes/OpenCode/2026-07-07-desktop-make-terminal-shortcuts-take-priority-when-the-terminal-is-focused|Desktop Make terminal shortcuts take priority when the terminal is focused]]
- Later: 2026-07-09 · Codex CLI · [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-d89fa7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-d89fa7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->