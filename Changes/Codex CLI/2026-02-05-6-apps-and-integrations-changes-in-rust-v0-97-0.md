---
card_id: codex-cli-2026-02-05-89020e
date: '2026-02-05'
description: 'Codex CLI · 2026-02-05 · Apps and Integrations: 6 changes in 0.97.0
  — Added a session-scoped “Allow and remember” option for MCP/App tool approvals,
  so…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6f31c773ae90fa7f8640dff9f2755632b005a5d078dc268451a1c47464e6e7ca
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-05-89020e
  comparison: ''
  date: '2026-02-05'
  description: 'Codex CLI — 0.97.0: 6 Apps and Integrations changes'
  evidence:
  - quote: Added a session-scoped “Allow and remember” option for MCP/App tool approvals,
      so repeated calls to the same tool can be auto-approved during the session.
      (#10584)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Added support for mixed text and image content in dynamic tool outputs
      for app-server integrations. (#10567)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Added caching for MCP actions from apps to reduce repeated load latency
      for users with many installed apps. (#10662)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10584 Add option to approve and remember MCP/Apps tool usage @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10593 Fix jitter in TUI apps/connectors picker @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10662 [apps] Cache MCP actions from apps. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-apps-and-integrations-changes-in-rust-v0-97-0
  source_release: codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in rust-v0.97.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5
  Apps and Integrations changes in rust-v0.95.0]]'
- '[[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14
  Apps and Integrations changes in v0.27.0]]'
- '[[Changes/Claude Code/2026-02-05-skills-defined-in-claude-skills-within-additional-directories-add-dir-are-now-lo|Skills
  defined in .claude/skills/ within additional directories (--add-dir)…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in rust-v0.97.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in rust-v0.97.0

**Codex CLI** · 2026-02-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.97.0) · from [[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|0.97.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a session-scoped “Allow and remember” option for MCP/App tool approvals, so repeated calls to the same tool can be auto-approved during the session. (#10584)

> Added support for mixed text and image content in dynamic tool outputs for app-server integrations. (#10567)

> Added caching for MCP actions from apps to reduce repeated load latency for users with many installed apps. (#10662)

> #10584 Add option to approve and remember MCP/Apps tool usage @canvrno-oai

> #10593 Fix jitter in TUI apps/connectors picker @canvrno-oai

> #10662 [apps] Cache MCP actions from apps. @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.97.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-05-4-memory-and-personalization-changes-in-rust-v0-97-0|4 Memory and Personalization changes in rust-v0.97.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-05-2-model-support-changes-in-rust-v0-97-0|2 Model Support changes in rust-v0.97.0]] · Model Support
- [[Changes/Codex CLI/2026-02-05-2-developer-workflow-changes-in-rust-v0-97-0|2 Developer Workflow changes in rust-v0.97.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-05-10649-fix-test-shell-command-interruption-flake-gt-oai|♯10649 Fix test_shell_command_interruption flake @gt-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-02-05-2-safety-and-privacy-changes-in-rust-v0-97-0|2 Safety and Privacy changes in rust-v0.97.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-05-10667-chore-app-server-document-experimental-api-opt-in-owenlin0|♯10667 chore(app-server): document experimental API opt-in @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-02-05-2-interface-experience-changes-in-rust-v0-97-0|2 Interface Experience changes in rust-v0.97.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-05-18-other-changes-in-rust-v0-97-0|18 other changes in rust-v0.97.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-05 · Claude Code · [[Changes/Claude Code/2026-02-05-skills-defined-in-claude-skills-within-additional-directories-add-dir-are-now-lo|Skills defined in .claude/skills/ within additional directories (--add-dir)…]]
- Later: 2026-02-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-05-plugin-and-marketplace-names-support-uppercase-letters|Plugin and marketplace names support uppercase letters]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-05-89020e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-05-6-apps-and-integrations-changes-in-rust-v0-97-0.md%0ACard%20ID%3A%20codex-cli-2026-02-05-89020e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.97.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->