---
card_id: codex-cli-2026-06-18-9166cf
date: '2026-06-18'
description: 'Codex CLI · 2026-06-18 · Apps and Integrations: 17 changes in 0.141.0
  — Hook trust bypass now persists through `codex exec` thread start and resume, while…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4eafde56ce10e890189ec12020d40757d3b8e729848b00f1ed7534a074c2ad9f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-18-9166cf
  comparison: ''
  date: '2026-06-18'
  description: 'Codex CLI — 0.141.0: 17 Apps and Integrations changes'
  evidence:
  - quote: 'Hook trust bypass now persists through `codex exec` thread start and resume,
      while blocking `PostToolUse` hooks correctly reject code-mode tool calls. (#26434,
      #28365)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: 'Plugin capabilities now route consistently by authentication mode, deduplicate
      conflicting App/MCP declarations, and preserve remote marketplace ordering.
      (#27461, #27602, #27607, #27902, #27958, #28395)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27607 [codex] Dedupe plugin MCPs by app declaration name @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27884 Add selected-plugin precedence and attribution to the MCP catalog
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27870 Discover stdio MCP servers from selected executor plugins @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27602 [codex] Preserve plugin apps in connector listings @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27461 [codex] Skip plugin MCP OAuth for matching app routes @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27893 Activate selected executor plugin MCPs in app-server @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#26702 TUI Plugin Sharing 2 - add remote plugin section plumbing @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28234 [mcp] Increase default tool timeout to 300 seconds @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28203 [codex] Add created-by-me remote plugin marketplace @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28365 Respect blocking PostToolUse hooks in code mode @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27813 [codex] Reuse Apps policy evaluation across MCP tool exposure @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28395 [codex] Preserve remote plugin directory order @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27902 [codex] Centralize plugin auth capability filtering @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#27958 [codex] Make plugin details capability aware @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28441 [codex] Use expect in integration tests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-apps-and-integrations-changes-in-rust-v0-141-0
  source_release: codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75
  source_type: github_releases
  theme: apps-integrations
  title: 17 Apps and Integrations changes in rust-v0.141.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-17-build-in-lovable-from-claude|Build in Lovable from
  Claude]]'
- '[[Changes/Lovable/2026-06-17-app-connector-lightspeed|App connector: Lightspeed]]'
- '[[Changes/OpenCode/2026-06-17-4-apps-and-integrations-changes-in-v1-17-8|4 Apps
  and Integrations changes in v1.17.8]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75]]'
source_type: github_releases
theme: apps-integrations
title: 17 Apps and Integrations changes in rust-v0.141.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Apps and Integrations changes in rust-v0.141.0

**Codex CLI** · 2026-06-18 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.141.0) · from [[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|0.141.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hook trust bypass now persists through `codex exec` thread start and resume, while blocking `PostToolUse` hooks correctly reject code-mode tool calls. (#26434, #28365)

> Plugin capabilities now route consistently by authentication mode, deduplicate conflicting App/MCP declarations, and preserve remote marketplace ordering. (#27461, #27602, #27607, #27902, #27958, #28395)

> #27607 [codex] Dedupe plugin MCPs by app declaration name @felixxia-oai

> #27884 Add selected-plugin precedence and attribution to the MCP catalog @jif-oai

> #27870 Discover stdio MCP servers from selected executor plugins @jif-oai

> #27602 [codex] Preserve plugin apps in connector listings @felixxia-oai

> #27461 [codex] Skip plugin MCP OAuth for matching app routes @felixxia-oai

> #27893 Activate selected executor plugin MCPs in app-server @jif-oai

> #26702 TUI Plugin Sharing 2 - add remote plugin section plumbing @canvrno-oai

> #28234 [mcp] Increase default tool timeout to 300 seconds @adaley-openai

> #28203 [codex] Add created-by-me remote plugin marketplace @ericning-o

> #28365 Respect blocking PostToolUse hooks in code mode @abhinav-oai

> #27813 [codex] Reuse Apps policy evaluation across MCP tool exposure @mzeng-openai

> #28395 [codex] Preserve remote plugin directory order @jameswt-oai

> #27902 [codex] Centralize plugin auth capability filtering @felixxia-oai

> #27958 [codex] Make plugin details capability aware @felixxia-oai

> #28441 [codex] Use expect in integration tests @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.141.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-18-5-agent-mode-changes-in-rust-v0-141-0|5 Agent Mode changes in rust-v0.141.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-18-7-developer-workflow-changes-in-rust-v0-141-0|7 Developer Workflow changes in rust-v0.141.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-18-tls-connections-now-support-p-521-certificate-signatures-commonly-used-by-enterp|TLS connections now support P-521 certificate signatures commonly used by enterprise…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-18-28257-support-staging-oauth-client-id-overrides-apanasenko-oai|♯28257 Support staging OAuth client ID overrides @apanasenko-oai]] · Account and Access
- [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Context Window
- [[Changes/Codex CLI/2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0|3 Memory and Personalization changes in rust-v0.141.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-06-18-42-other-changes-in-rust-v0-141-0|42 other changes in rust-v0.141.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-17 · OpenCode · [[Changes/OpenCode/2026-06-17-4-apps-and-integrations-changes-in-v1-17-8|4 Apps and Integrations changes in v1.17.8]]
- Later: 2026-06-18 · Lovable · [[Changes/Lovable/2026-06-18-inspect-your-app-s-ai-activity|Inspect your app's AI activity]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-18-9166cf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0.md%0ACard%20ID%3A%20codex-cli-2026-06-18-9166cf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.141.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->