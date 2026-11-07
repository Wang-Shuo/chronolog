---
card_id: codex-cli-2026-07-21-723716
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Model Support: 22 changes in 0.145.0 — Added
  experimental Amazon Bedrock login, custom endpoint and authentication support, and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1289
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1cbadd173cd1c37bc43beebe6525ebba977686a07b68448e13efa95e411b7e4a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-723716
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 22 Model Support changes'
  evidence:
  - quote: 'Added experimental Amazon Bedrock login, custom endpoint and authentication
      support, and GPT-5.6 Sol as the default Bedrock model. (#31327, #33170, #33175,
      #32288, #33695)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: 'Updated the bundled OpenAI Docs skill with current GPT-5.6 model resolution,
      prompting, and migration guidance across macOS, Linux, and Windows. (#31842,
      #33121)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: Migrated bundled GPT-5.4 selections and internal uses to the corresponding
      GPT-5.6 Terra and Luna variants. (#33173)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31652 fix(tui): hide empty reasoning summaries @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31842 Update bundled OpenAI Docs skill for GPT-5.6 @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32206 Always send reasoning parameters in Responses requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32288 Make GPT-5.6 Sol the default Bedrock model @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32290 Respect model support for reasoning summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32316 Stop falling back to older model availability announcements @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32875 Use model catalog policies for Guardian auto review @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32881 Broaden remote compaction model fallback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32911 Allow injecting the models manager into `ThreadManager` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33121 Refine GPT-5.6 prompting and migration guidance @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33173 Migrate GPT-5.4 uses to GPT-5.6 variants @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33177 Support model catalog templates for Guardian policy prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33631 Honor configured model defaults for spawned agents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33656 Validate reasoning effort after applying spawn roles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33961 Refresh bundled model metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34047 Avoid resending the model for reasoning shortcuts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34365 Animate Max and Ultra reasoning effort changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34387 Refresh bundled model metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34429 Move shared skill models into `codex-skills` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 22-model-support-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: model-support
  title: 22 Model Support changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-18-3-model-support-changes-in-rust-v0-144-6|3 Model
  Support changes in rust-v0.144.6]]'
- '[[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve
  pasted prompt content when changing models through Ctrl+X /model]]'
- '[[Changes/OpenCode/2026-07-20-3-model-support-changes-in-v1-18-4|3 Model Support
  changes in v1.18.4]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: model-support
title: 22 Model Support changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 22 Model Support changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added experimental Amazon Bedrock login, custom endpoint and authentication support, and GPT-5.6 Sol as the default Bedrock model. (#31327, #33170, #33175, #32288, #33695)

> Updated the bundled OpenAI Docs skill with current GPT-5.6 model resolution, prompting, and migration guidance across macOS, Linux, and Windows. (#31842, #33121)

> Migrated bundled GPT-5.4 selections and internal uses to the corresponding GPT-5.6 Terra and Luna variants. (#33173)

> #31652 fix(tui): hide empty reasoning summaries @fcoury-oai

> #31842 Update bundled OpenAI Docs skill for GPT-5.6 @kkahadze-oai

> #32206 Always send reasoning parameters in Responses requests @copyberry

> #32288 Make GPT-5.6 Sol the default Bedrock model @copyberry

> #32290 Respect model support for reasoning summaries @copyberry

> #32316 Stop falling back to older model availability announcements @copyberry

> #32875 Use model catalog policies for Guardian auto review @copyberry

> #32881 Broaden remote compaction model fallback @copyberry

> #32911 Allow injecting the models manager into `ThreadManager` @copyberry

> #33121 Refine GPT-5.6 prompting and migration guidance @copyberry

> #33173 Migrate GPT-5.4 uses to GPT-5.6 variants @copyberry

> #33177 Support model catalog templates for Guardian policy prompts @copyberry

> #33631 Honor configured model defaults for spawned agents @copyberry

> #33656 Validate reasoning effort after applying spawn roles @copyberry

> #33961 Refresh bundled model metadata @copyberry

> #34047 Avoid resending the model for reasoning shortcuts @copyberry

> #34365 Animate Max and Ultra reasoning effort changes @copyberry

> #34387 Refresh bundled model metadata @copyberry

> #34429 Move shared skill models into `codex-skills` @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-20 · OpenCode · [[Changes/OpenCode/2026-07-20-3-model-support-changes-in-v1-18-4|3 Model Support changes in v1.18.4]]
- Later: 2026-07-21 · Gemini · [[Changes/Gemini/2026-07-21-3-6-flash-an-upgraded-model-for-your-daily-life|3.6 Flash: An upgraded model for your daily life]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-723716&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-22-model-support-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-723716%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->