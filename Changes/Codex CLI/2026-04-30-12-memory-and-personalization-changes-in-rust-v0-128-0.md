---
card_id: codex-cli-2026-04-30-55b512
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Memory and Personalization: 12 changes in 0.128.0
  — #18982 feat: use git-backed workspace diffs for memory consolidation @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1015
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 75263f03b860699a2d95330abbb4b59006e80aa901435c32e268242e0a4b2f3b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-55b512
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 12 Memory and Personalization changes'
  evidence:
  - quote: '#18982 feat: use git-backed workspace diffs for memory consolidation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19809 Allow Phase 2 memory claims after retry exhaustion @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19818 chore: split memories part 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19860 feat: split memories part 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19967 Stabilize memory Phase 2 input ordering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19970 feat: trigger memories from user turns with cooldown @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19990 feat: skip memory startup when Codex rate limits are low @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19998 feat: house-keeping memories 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20000 feat: house-keeping memories 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20005 feat: house-keeping memories 3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20018 core tests: migrate model/personality turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20186 nit: drop old memories things @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-memory-and-personalization-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: memory
  title: 12 Memory and Personalization changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/Cline/2026-04-24-improve-cline-core-memory-diagnostics-used-by-the-extension-runtime|Improve
  cline-core memory diagnostics used by the extension runtime]]'
- '[[Changes/GitHub Copilot CLI/2026-04-24-custom-instruction-files-in-gitignored-directories-e-g-github-instructions-now-l|Custom
  instruction files in .gitignored directories (e.g., .github/instructions/)…]]'
- '[[Changes/Gemini CLI/2026-04-28-refactor-memory-replace-memorymanageragent-with-prompt-driven-memory-editing-acr|refactor(memory):
  replace MemoryManagerAgent with prompt-driven memory editing…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: memory
title: 12 Memory and Personalization changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Memory and Personalization changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #18982 feat: use git-backed workspace diffs for memory consolidation @jif-oai

> #19809 Allow Phase 2 memory claims after retry exhaustion @jif-oai

> #19818 chore: split memories part 1 @jif-oai

> #19860 feat: split memories part 2 @jif-oai

> #19967 Stabilize memory Phase 2 input ordering @jif-oai

> #19970 feat: trigger memories from user turns with cooldown @jif-oai

> #19990 feat: skip memory startup when Codex rate limits are low @jif-oai

> #19998 feat: house-keeping memories 1 @jif-oai

> #20000 feat: house-keeping memories 2 @jif-oai

> #20005 feat: house-keeping memories 3 @jif-oai

> #20018 core tests: migrate model/personality turns to profiles @bolinfest

> #20186 nit: drop old memories things @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-28 · Gemini CLI · [[Changes/Gemini CLI/2026-04-28-refactor-memory-replace-memorymanageragent-with-prompt-driven-memory-editing-acr|refactor(memory): replace MemoryManagerAgent with prompt-driven memory editing…]]
- Later: 2026-05-05 · ChatGPT · [[Changes/ChatGPT/2026-05-05-starting-today-we-re-rolling-out-memory-improvements-to-chatgpt-plus-and-pro-use|Memory sources and more personalized responses in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-55b512&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-55b512%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->