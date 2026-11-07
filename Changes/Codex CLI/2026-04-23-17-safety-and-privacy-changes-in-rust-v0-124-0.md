---
card_id: codex-cli-2026-04-23-485d49
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Safety and Privacy: 17 changes in 0.124.0 —
  Fixed permission-mode drift so `/permissions` changes survive side conversations
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2095
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 54565061e373669722de7f3898b3d1cb5bb7a08696207274dcae791d52ca8e99
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-485d49
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.124.0: 17 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed permission-mode drift so `/permissions` changes survive side conversations
      and updated Full Access state is correctly reflected in MCP approval handling.
      (#18924, #19033)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18867 sandboxing: materialize cwd-relative permission globs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18276 exec-server: carry filesystem sandbox profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18277 core: derive active permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18953 use long-lived sessions for codex sandbox windows @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18278 app-server: expose thread permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18279 app-server: accept permission profile overrides @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19033 Fix MCP permission policy sync @leoshimo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19016 exec-server: expose arg0 alias root to fs sandbox @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19046 exec-server: require explicit filesystem sandbox cwd @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18280 clients: send permission profiles to app-server @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18281 rollout: persist turn permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18282 protocol: report session permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19055 Add safety check notification and error handling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18283 app-server: accept command permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18924 TUI: preserve permission state after side conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19086 app-server: include filesystem entries in permission requests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-safety-and-privacy-changes-in-rust-v0-124-0
  source_release: codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in rust-v0.124.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-22-better-mlx-thread-safety-for-array-management|Better
  MLX thread safety for array management]]'
- '[[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed
  MCP step-up authorization silently refreshing instead of prompting…]]'
- '[[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety
  and Privacy changes in v2.1.119]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in rust-v0.124.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in rust-v0.124.0

**Codex CLI** · 2026-04-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.124.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed permission-mode drift so `/permissions` changes survive side conversations and updated Full Access state is correctly reflected in MCP approval handling. (#18924, #19033)

> #18867 sandboxing: materialize cwd-relative permission globs @bolinfest

> #18276 exec-server: carry filesystem sandbox profiles @bolinfest

> #18277 core: derive active permission profiles @bolinfest

> #18953 use long-lived sessions for codex sandbox windows @iceweasel-oai

> #18278 app-server: expose thread permission profiles @bolinfest

> #18279 app-server: accept permission profile overrides @bolinfest

> #19033 Fix MCP permission policy sync @leoshimo-oai

> #19016 exec-server: expose arg0 alias root to fs sandbox @bolinfest

> #19046 exec-server: require explicit filesystem sandbox cwd @bolinfest

> #18280 clients: send permission profiles to app-server @bolinfest

> #18281 rollout: persist turn permission profiles @bolinfest

> #18282 protocol: report session permission profiles @bolinfest

> #19055 Add safety check notification and error handling @etraut-openai

> #18283 app-server: accept command permission profiles @bolinfest

> #18924 TUI: preserve permission state after side conversations @etraut-openai

> #19086 app-server: include filesystem entries in permission requests @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.124.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Context Window
- [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-124-0|45 other changes in rust-v0.124.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety and Privacy changes in v2.1.119]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-485d49&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-485d49%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.124.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->