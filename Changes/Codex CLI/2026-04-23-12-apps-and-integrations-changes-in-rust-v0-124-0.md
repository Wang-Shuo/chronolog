---
card_id: codex-cli-2026-04-23-61a43a
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Apps and Integrations: 12 changes in 0.124.0
  — Remote plugin marketplaces can now be listed and read directly, with more reliable…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2687
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 33efd96a708f54148adc09c5cbec8d7db23f9f853ca8e1dee96869e11f1023c6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-61a43a
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.124.0: 12 Apps and Integrations changes'
  evidence:
  - quote: 'Remote plugin marketplaces can now be listed and read directly, with more
      reliable detail lookups and larger result pages. (#18452, #19079)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: 'Hooks are now stable, can be configured inline in `config.toml` and managed
      `requirements.toml`, and can observe MCP tools as well as `apply_patch` and
      long-running Bash sessions. (#18893, #18385, #18391, #18888, #19012)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18391 fix(core): emit hooks for apply_patch edits @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18916 test(core): move prompt debug coverage to integration suite @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18452 feat: Support remote plugin list/read. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18888 hooks: emit Bash PostToolUse when exec_command completes via write_stdin
      @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19031 Fix relative stdio MCP cwd fallback @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18893 codex: support hooks in config.toml and requirements.toml @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19012 Mark codex_hooks stable @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19079 Use remote plugin IDs for detail reads and enlarge list pages @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18385 Support MCP tools in hooks @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19113 Fix auto-review config compatibility across protocol and SDK @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-apps-and-integrations-changes-in-rust-v0-124-0
  source_release: codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in rust-v0.124.0
  type: change
related_changes:
- '[[Changes/Cline/2026-04-22-wire-up-remote-globalskills-from-enterprise-remote-config-with-full-ui-toggle-su|Wire
  up remote globalSkills from enterprise remote config with full UI, toggle…]]'
- '[[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3
  Apps and Integrations changes in v2.1.119]]'
- '[[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5
  Apps and Integrations changes in v2.1.118]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in rust-v0.124.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in rust-v0.124.0

**Codex CLI** · 2026-04-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.124.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote plugin marketplaces can now be listed and read directly, with more reliable detail lookups and larger result pages. (#18452, #19079)

> Hooks are now stable, can be configured inline in `config.toml` and managed `requirements.toml`, and can observe MCP tools as well as `apply_patch` and long-running Bash sessions. (#18893, #18385, #18391, #18888, #19012)

> #18391 fix(core): emit hooks for apply_patch edits @fcoury-oai

> #18916 test(core): move prompt debug coverage to integration suite @bolinfest

> #18452 feat: Support remote plugin list/read. @xl-openai

> #18888 hooks: emit Bash PostToolUse when exec_command completes via write_stdin @eternal-openai

> #19031 Fix relative stdio MCP cwd fallback @mzeng-openai

> #18893 codex: support hooks in config.toml and requirements.toml @eternal-openai

> #19012 Mark codex_hooks stable @abhinav-oai

> #19079 Use remote plugin IDs for detail reads and enlarge list pages @xl-openai

> #18385 Support MCP tools in hooks @abhinav-oai

> #19113 Fix auto-review config compatibility across protocol and SDK @won-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.124.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Context Window
- [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-124-0|45 other changes in rust-v0.124.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5 Apps and Integrations changes in v2.1.118]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-61a43a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-61a43a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.124.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->