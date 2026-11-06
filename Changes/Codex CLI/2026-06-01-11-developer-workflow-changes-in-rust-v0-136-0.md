---
card_id: codex-cli-2026-06-01-229172
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Developer Workflow: 11 changes in 0.136.0 —
  Sandboxed commands clean up more reliably after interruptions or denied Windows
  network…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d40be3a44c9be8a139c41439ebbee42e6203354225c5695d8507ac02251f9b6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-229172
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 11 Developer Workflow changes'
  evidence:
  - quote: 'Sandboxed commands clean up more reliably after interruptions or denied
      Windows network attempts, and `deny` read rules stay enforced for safe-command
      and approval-bypass paths. (#22729, #19880, #23943)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Removed the stale app-server debug-client pieces and cleaned up the workspace
      after deletion. (#25063, #25064, #25065, #25066, #25067, #25068, #25069, #25070,
      #25075)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25063 Drop the stale debug-client manifest @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25064 Remove the generated debug-client README @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25065 Delete debug-client app-server process plumbing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25066 Retire debug-client interactive command parsing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25067 Remove the debug-client CLI entrypoint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25068 Delete debug-client JSONL output helper @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25069 Remove debug-client server event reader @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25070 Drop debug-client prompt state tracking @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25027 Add `/archive` slash command @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-developer-workflow-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in rust-v0.136.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-28-3-developer-workflow-changes-in-v1-0-55|3
  Developer Workflow changes in v1.0.55]]'
- '[[Changes/Claude Code/2026-05-29-3-developer-workflow-changes-in-v2-1-157|3 Developer
  Workflow changes in v2.1.157]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-4-developer-workflow-changes-in-v1-0-56|4
  Developer Workflow changes in v1.0.56]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandboxed commands clean up more reliably after interruptions or denied Windows network attempts, and `deny` read rules stay enforced for safe-command and approval-bypass paths. (#22729, #19880, #23943)

> Removed the stale app-server debug-client pieces and cleaned up the workspace after deletion. (#25063, #25064, #25065, #25066, #25067, #25068, #25069, #25070, #25075)

> #25063 Drop the stale debug-client manifest @jif-oai

> #25064 Remove the generated debug-client README @jif-oai

> #25065 Delete debug-client app-server process plumbing @jif-oai

> #25066 Retire debug-client interactive command parsing @jif-oai

> #25067 Remove the debug-client CLI entrypoint @jif-oai

> #25068 Delete debug-client JSONL output helper @jif-oai

> #25069 Remove debug-client server event reader @jif-oai

> #25070 Drop debug-client prompt state tracking @jif-oai

> #25027 Add `/archive` slash command @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model Support changes in rust-v0.136.0]] · Model Support
- [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]] · Context Window
- [[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3 Search and Browsing changes in rust-v0.136.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-01-2-interface-experience-changes-in-rust-v0-136-0|2 Interface Experience changes in rust-v0.136.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image Generation changes in rust-v0.136.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-01-57-other-changes-in-rust-v0-136-0|57 other changes in rust-v0.136.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-29 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-29-4-developer-workflow-changes-in-v1-0-56|4 Developer Workflow changes in v1.0.56]]
- Later: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp show, /lsp test, and /lsp reload correctly discover project LSP config…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-229172&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-229172%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->