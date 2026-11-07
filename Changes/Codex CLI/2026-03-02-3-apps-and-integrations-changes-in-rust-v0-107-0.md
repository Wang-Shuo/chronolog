---
card_id: codex-cli-2026-03-02-275083
date: '2026-03-02'
description: 'Codex CLI · 2026-03-02 · Apps and Integrations: 3 changes in 0.107.0
  — `thread/start` no longer blocks unrelated app-server requests, reducing stalls
  during…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2635
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 616228eb5d57f93694ab81db75e4a75d6f4a2dbac466e5f64017c62573922828
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-02-275083
  comparison: ''
  date: '2026-03-02'
  description: 'Codex CLI — 0.107.0: 3 Apps and Integrations changes'
  evidence:
  - quote: '`thread/start` no longer blocks unrelated app-server requests, reducing
      stalls during slow startup paths such as MCP auth checks. (#13033)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12745 [apps] Improve app/list with force_fetch=true @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13067 [apps] Stablize app list updated event. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-apps-and-integrations-changes-in-rust-v0-107-0
  source_release: codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in rust-v0.107.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-27-plugin-and-marketplace-git-repos-update-correctly-after-force-pushes-and-tag-bas|Plugin
  and marketplace git repos update correctly after force-pushes and tag-based…]]'
- '[[Changes/GitHub Copilot CLI/2026-02-27-3-apps-and-integrations-changes-in-v0-0-419|3
  Apps and Integrations changes in v0.0.419]]'
- '[[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added
  ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in rust-v0.107.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in rust-v0.107.0

**Codex CLI** · 2026-03-02 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.107.0) · from [[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `thread/start` no longer blocks unrelated app-server requests, reducing stalls during slow startup paths such as MCP auth checks. (#13033)

> #12745 [apps] Improve app/list with force_fetch=true @mzeng-openai

> #13067 [apps] Stablize app list updated event. @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.107.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-02-2-multimodal-input-changes-in-rust-v0-107-0|2 Multimodal Input changes in rust-v0.107.0]] · Multimodal Input
- [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-3-account-and-access-changes-in-rust-v0-107-0|3 Account and Access changes in rust-v0.107.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Model Support
- [[Changes/Codex CLI/2026-03-02-3-editor-experience-changes-in-rust-v0-107-0|3 Editor Experience changes in rust-v0.107.0]] · Editor Experience
- [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-02-5-voice-and-audio-changes-in-rust-v0-107-0|5 Voice and Audio changes in rust-v0.107.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-02-24-other-changes-in-rust-v0-107-0|24 other changes in rust-v0.107.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]]
- Later: 2026-03-02 · ElevenLabs · [[Changes/ElevenLabs/2026-03-02-javascript-sdk|JavaScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-02-275083&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0.md%0ACard%20ID%3A%20codex-cli-2026-03-02-275083%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.107.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->