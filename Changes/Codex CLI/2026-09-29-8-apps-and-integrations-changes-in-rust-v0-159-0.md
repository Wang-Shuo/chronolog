---
card_id: codex-cli-2026-09-29-dfcf68
date: '2026-09-29'
description: 'Codex CLI · 2026-09-29 · Apps and Integrations: 8 changes in 0.159.0
  — Windows launches avoid stray console windows for MCP servers, code-mode hosts,
  and piped…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2846
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dc1e14529c0fb8e2bdadc570b6ac45616106289c0aeef2a0d05deac7f7e91464
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-29-dfcf68
  comparison: ''
  date: '2026-09-29'
  description: 'Codex CLI — 0.159.0: 8 Apps and Integrations changes'
  evidence:
  - quote: 'Windows launches avoid stray console windows for MCP servers, code-mode
      hosts, and piped commands; restrictive launchers can fall back to embedded mode.
      (#48138, #48238, #48483, #48491)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: Removed the bundled `plugin-creator` skill. (#48604)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48143 Preserve executor MCP credential boundaries across reconnects @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48238 Suppress console windows for local Windows MCP servers @malsamiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48604 Remove the bundled `plugin-creator` skill @martinauyeung-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48724 Prevent Linux ETXTBSY races in MCP stdio tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48764 Preserve MCP app resource URIs without defaulting display mode
      @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48783 Add single-server MCP status discovery with thread connection reuse
      @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-apps-and-integrations-changes-in-rust-v0-159-0
  source_release: codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in rust-v0.159.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-29-we-re-making-it-easier-to-bring-meeting-context-into-chatgpt-so-you-can-act-on-n|We’re
  making it easier to bring meeting context into ChatGPT so you can act on next…]]'
- '[[Changes/ChatGPT/2026-09-29-supported-plugins-can-use-mcp-events-to-start-an-automation-when-something-chang-d9add6|Start
  automations from connected-app events]]'
- '[[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14
  Apps and Integrations changes in v2.1.285]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516|codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in rust-v0.159.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in rust-v0.159.0

**Codex CLI** · 2026-09-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.159.0) · from [[Releases/Codex CLI/codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516|0.159.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows launches avoid stray console windows for MCP servers, code-mode hosts, and piped commands; restrictive launchers can fall back to embedded mode. (#48138, #48238, #48483, #48491)

> Removed the bundled `plugin-creator` skill. (#48604)

> #48143 Preserve executor MCP credential boundaries across reconnects @rreichel3-oai

> #48238 Suppress console windows for local Windows MCP servers @malsamiri-oai

> #48604 Remove the bundled `plugin-creator` skill @martinauyeung-oai

> #48724 Prevent Linux ETXTBSY races in MCP stdio tests @jif-oai

> #48764 Preserve MCP app resource URIs without defaulting display mode @victor-openai

> #48783 Add single-server MCP status discovery with thread connection reuse @victor-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.159.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-29-3-model-support-changes-in-rust-v0-159-0|3 Model Support changes in rust-v0.159.0]] · Model Support
- [[Changes/Codex CLI/2026-09-29-3-account-and-access-changes-in-rust-v0-159-0|3 Account and Access changes in rust-v0.159.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-29-48824-keep-voice-rtp-timestamps-aligned-to-20-ms-packets-bc-openai|♯48824 Keep voice RTP timestamps aligned to 20 ms packets @bc-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-29-4-interface-experience-changes-in-rust-v0-159-0|4 Interface Experience changes in rust-v0.159.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-29-3-safety-and-privacy-changes-in-rust-v0-159-0|3 Safety and Privacy changes in rust-v0.159.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-29-4-mobile-and-desktop-changes-in-rust-v0-159-0|4 Mobile and Desktop changes in rust-v0.159.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-29-3-editor-experience-changes-in-rust-v0-159-0|3 Editor Experience changes in rust-v0.159.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-29-5-developer-workflow-changes-in-rust-v0-159-0|5 Developer Workflow changes in rust-v0.159.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-29-2-collaboration-changes-in-rust-v0-159-0|2 Collaboration changes in rust-v0.159.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-29-4-context-window-changes-in-rust-v0-159-0|4 Context Window changes in rust-v0.159.0]] · Context Window
- [[Changes/Codex CLI/2026-09-29-48190-bound-agent-message-board-sse-frames-before-parsing-jif-oai|♯48190 Bound agent message board SSE frames before parsing @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-09-29-60-other-changes-in-rust-v0-159-0|60 other changes in rust-v0.159.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]]
- Later: 2026-09-29 · Gemini CLI · [[Changes/Gemini CLI/2026-09-29-2-apps-and-integrations-changes-in-v0-62-0|2 Apps and Integrations changes in v0.62.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-29-dfcf68&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-29-8-apps-and-integrations-changes-in-rust-v0-159-0.md%0ACard%20ID%3A%20codex-cli-2026-09-29-dfcf68%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.159.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->