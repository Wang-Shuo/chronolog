---
card_id: codex-cli-2026-04-30-ffa7bb
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Model Support: 10 changes in 0.128.0 — Added
  persisted `/goal` workflows with app-server APIs, model tools, runtime continuation,
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1207
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8134957dd7cc26fa857ab76121321c3ad57203281d95999d4f395ffe90a854dc
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-ffa7bb
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 10 Model Support changes'
  evidence:
  - quote: 'Added persisted `/goal` workflows with app-server APIs, model tools, runtime
      continuation, and TUI controls for create, pause, resume, and clear. (#18073,
      #18074, #18075, #18076, #18077, #20082)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Updated the bundled OpenAI Docs skill for GPT-5.5, `gpt-image-2`, and
      clearer upgrade guidance. (#19407, #19443, #19422)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19407 Update bundled OpenAI Docs skill for GPT-5.5 @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19416 Fix: use function apply_patch tool for Bedrock model @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19461 fix: Bedrock GPT-5.4 reasoning levels @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18075 Add goal model tools (3 / 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19287 Restore persisted model provider on thread resume @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19771 fix: filter dynamic deferred tools from model_visible_specs @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19442 feat: disable capabilities by model provider @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20109 feat: update Bedrock Mantle endpoint and GPT-5.4 model ID @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-model-support-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-28-2-model-support-changes-in-v1-14-29|2 Model Support
  changes in v1.14.29]]'
- '[[Changes/Dify/2026-04-29-27-model-support-changes-in-1-14-0|27 Model Support changes
  in 1.14.0]]'
- '[[Changes/OpenCode/2026-04-29-4-model-support-changes-in-v1-14-30|4 Model Support
  changes in v1.14.30]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added persisted `/goal` workflows with app-server APIs, model tools, runtime continuation, and TUI controls for create, pause, resume, and clear. (#18073, #18074, #18075, #18076, #18077, #20082)

> Updated the bundled OpenAI Docs skill for GPT-5.5, `gpt-image-2`, and clearer upgrade guidance. (#19407, #19443, #19422)

> #19407 Update bundled OpenAI Docs skill for GPT-5.5 @kkahadze-oai

> #19416 Fix: use function apply_patch tool for Bedrock model @celia-oai

> #19461 fix: Bedrock GPT-5.4 reasoning levels @celia-oai

> #18075 Add goal model tools (3 / 5) @etraut-openai

> #19287 Restore persisted model provider on thread resume @etraut-openai

> #19771 fix: filter dynamic deferred tools from model_visible_specs @sayan-oai

> #19442 feat: disable capabilities by model provider @celia-oai

> #20109 feat: update Bedrock Mantle endpoint and GPT-5.4 model ID @celia-oai

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
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-29 · OpenCode · [[Changes/OpenCode/2026-04-29-4-model-support-changes-in-v1-14-30|4 Model Support changes in v1.14.30]]
- Later: 2026-05-01 · Claude Code · [[Changes/Claude Code/2026-05-01-2-model-support-changes-in-v2-1-126|2 Model Support changes in v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-ffa7bb&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-10-model-support-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-ffa7bb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->