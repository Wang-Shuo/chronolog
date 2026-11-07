---
card_id: codex-cli-2026-09-09-1a2db7
date: '2026-09-09'
description: 'Codex CLI · 2026-09-09 · Model Support: 21 changes in 0.154.0 — Remote
  resume and fork operations preserve saved permissions; fresh sessions and forks
  respect…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1339
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13cf40e9e8e0f999bac708d35047b448bc106a8f40616dd32ba4febf31907016
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-09-1a2db7
  comparison: ''
  date: '2026-09-09'
  description: 'Codex CLI — 0.154.0: 21 Model Support changes'
  evidence:
  - quote: 'Remote resume and fork operations preserve saved permissions; fresh sessions
      and forks respect server model defaults unless explicitly overridden. (#43330,
      #43177, #43355)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: Updated the bundled OpenAI Docs skill with GPT-6-Astra migration, compatibility,
      and prompting guidance. (#42931)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42328 Support durable reasoning configuration updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42422 Honor model requirements in Guardian computer-use scoring @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42607 Add GPT-6-Astra to the bundled model catalog @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42619 Add GPT-6-Astra to Amazon Bedrock catalogs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42638 Update GPT-6-Astra Fast tier speed description @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42639 Warn when saved model defaults are overridden @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42657 Use a generic fallback model name in status tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42744 Honor model-provided Guardian review policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42824 Refine user input guidance for GPT-6 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42836 Make GPT-6-Astra user input guidance conditional @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42879 List GPT-6-Astra in the model picker @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42931 Update OpenAI Docs skill guidance for GPT-6 Astra @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43083 Supply Bazel-managed CMake and Ninja for the bundled Opus build
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43100 Add bounded incoming Opus RTP handling to the voice host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43110 Record reasoning effort changes in conversation history behind
      a flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43177 Use server model defaults for fresh TUI startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43355 Let the app server resolve implicit model settings for CLI forks
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43359 Show the server''s model provider ID in TUI status @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43456 Wait for thread idle before rollback in model-switching tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 21-model-support-changes-in-rust-v0-154-0
  source_release: codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1
  source_type: github_releases
  theme: model-support
  title: 21 Model Support changes in rust-v0.154.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support
  changes in v2026.9.3]]'
- '[[Changes/ChatGPT/2026-09-09-chatgpt-voice-can-now-use-gpt-5-6-or-gpt-6-astra-when-it-needs-to-search-or-reas-848954|ChatGPT
  Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason…]]'
- '[[Changes/Claude Code/2026-09-09-added-maxeffortlevel-setting-top-level-or-per-model-under-modelsettings-caps-the|Added
  maxEffortLevel setting (top-level or per model under modelSettings)]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1]]'
source_type: github_releases
theme: model-support
title: 21 Model Support changes in rust-v0.154.0
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Model Support changes in rust-v0.154.0

**Codex CLI** · 2026-09-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.154.0) · from [[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote resume and fork operations preserve saved permissions; fresh sessions and forks respect server model defaults unless explicitly overridden. (#43330, #43177, #43355)

> Updated the bundled OpenAI Docs skill with GPT-6-Astra migration, compatibility, and prompting guidance. (#42931)

> #42328 Support durable reasoning configuration updates @copyberry

> #42422 Honor model requirements in Guardian computer-use scoring @copyberry

> #42607 Add GPT-6-Astra to the bundled model catalog @copyberry

> #42619 Add GPT-6-Astra to Amazon Bedrock catalogs @copyberry

> #42638 Update GPT-6-Astra Fast tier speed description @copyberry

> #42639 Warn when saved model defaults are overridden @copyberry

> #42657 Use a generic fallback model name in status tests @copyberry

> #42744 Honor model-provided Guardian review policies @copyberry

> #42824 Refine user input guidance for GPT-6 @copyberry

> #42836 Make GPT-6-Astra user input guidance conditional @copyberry

> #42879 List GPT-6-Astra in the model picker @copyberry

> #42931 Update OpenAI Docs skill guidance for GPT-6 Astra @copyberry

> #43083 Supply Bazel-managed CMake and Ninja for the bundled Opus build @copyberry

> #43100 Add bounded incoming Opus RTP handling to the voice host @copyberry

> #43110 Record reasoning effort changes in conversation history behind a flag @copyberry

> #43177 Use server model defaults for fresh TUI startup @copyberry

> #43355 Let the app server resolve implicit model settings for CLI forks @copyberry

> #43359 Show the server's model provider ID in TUI status @copyberry

> #43456 Wait for thread idle before rollback in model-switching tests @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.154.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5 Account and Access changes in rust-v0.154.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-09-19-apps-and-integrations-changes-in-rust-v0-154-0|19 Apps and Integrations changes in rust-v0.154.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-09-4-interface-experience-changes-in-rust-v0-154-0|4 Interface Experience changes in rust-v0.154.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-09-17-context-window-changes-in-rust-v0-154-0|17 Context Window changes in rust-v0.154.0]] · Context Window
- [[Changes/Codex CLI/2026-09-09-6-mobile-and-desktop-changes-in-rust-v0-154-0|6 Mobile and Desktop changes in rust-v0.154.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] · Model Support
- [[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice and Audio changes in rust-v0.154.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-09-experimental-worktree-support-lets-you-create-isolated-checkouts-for-new-or-fork|Experimental worktree support lets you create isolated checkouts for new or forked…]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-09-42746-handle-pending-network-reviews-after-process-completion-copyberry|♯42746 Handle pending network reviews after process completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-09-42306-stabilize-the-detached-exec-server-session-resume-test-copyberry|♯42306 Stabilize the detached exec-server session resume test @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration changes in rust-v0.154.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-09-7-developer-workflow-changes-in-rust-v0-154-0|7 Developer Workflow changes in rust-v0.154.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-09-119-other-changes-in-rust-v0-154-0|119 other changes in rust-v0.154.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-added-maxeffortlevel-setting-top-level-or-per-model-under-modelsettings-caps-the|Added maxEffortLevel setting (top-level or per model under modelSettings)]]
- Later: 2026-09-09 · Google Antigravity · [[Changes/Google Antigravity/2026-09-09-2-model-support-changes-in-hub-v2-13-0-introducing-new-documents|2 Model Support changes in HUB v2.13.0 — Introducing new Documents…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-09-1a2db7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-09-21-model-support-changes-in-rust-v0-154-0.md%0ACard%20ID%3A%20codex-cli-2026-09-09-1a2db7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.154.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->