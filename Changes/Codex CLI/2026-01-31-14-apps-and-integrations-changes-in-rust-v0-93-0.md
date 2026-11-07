---
card_id: codex-cli-2026-01-31-c93021
date: '2026-01-31'
description: 'Codex CLI · 2026-01-31 · Apps and Integrations: 14 changes in 0.93.0
  — MCP tool image outputs render reliably even when image blocks aren’t first or
  are…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1045
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 254cf11d54691c50479948925be21b89aebb24bc78c0ad47742b48046b305a39
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-31-c93021
  comparison: ''
  date: '2026-01-31'
  description: 'Codex CLI — 0.93.0: 14 Apps and Integrations changes'
  evidence:
  - quote: MCP tool image outputs render reliably even when image blocks aren’t first
      or are partially malformed. (#9815)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10003 feat: make it possible to specify --config flags in the SDK @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9815 Fix: Render MCP image outputs regardless of ordering @Kbediako'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9982 [skills] Auto install MCP dependencies when running skils with dependency
      specs. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10092 Update shell-tool-mcp.yml @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10095 Update shell-tool-mcp.yml @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10101 fix(ci) fix shell-tool-mcp version v2 @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10111 fix(ci) more shell-tool-mcp issues @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10115 update the ci pnpm workflow for shell-tool-mcp to use corepack
      for pnpm versioning @mjr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9728 [connectors] Support connectors part 2 - slash command and tui @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10135 fix(ci) missing package.json for shell-mcp-tool @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10175 Add OpenAI docs MCP tooltip @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10182 fix: unify `npm publish` call across shell-tool-mcp.yml and rust-release.yml
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10200 MCP tool call approval (simplified version) @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-apps-and-integrations-changes-in-rust-v0-93-0
  source_release: codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in rust-v0.93.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-01-30-3-apps-and-integrations-changes-in-v0-0-400|3
  Apps and Integrations changes in v0.0.400]]'
- '[[Changes/OpenCode/2026-01-30-2-apps-and-integrations-changes-in-v1-1-47-2|2 Apps
  and Integrations changes in v1.1.47 + 2]]'
- '[[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart
  approvals are now enabled by default, with explicit approval prompts for MCP…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in rust-v0.93.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in rust-v0.93.0

**Codex CLI** · 2026-01-31 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.93.0) · from [[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|0.93.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tool image outputs render reliably even when image blocks aren’t first or are partially malformed. (#9815)

> #10003 feat: make it possible to specify --config flags in the SDK @bolinfest

> #9815 Fix: Render MCP image outputs regardless of ordering @Kbediako

> #9982 [skills] Auto install MCP dependencies when running skils with dependency specs. @mzeng-openai

> #10092 Update shell-tool-mcp.yml @dylan-hurd-oai

> #10095 Update shell-tool-mcp.yml @dylan-hurd-oai

> #10101 fix(ci) fix shell-tool-mcp version v2 @dylan-hurd-oai

> #10111 fix(ci) more shell-tool-mcp issues @dylan-hurd-oai

> #10115 update the ci pnpm workflow for shell-tool-mcp to use corepack for pnpm versioning @mjr-openai

> #9728 [connectors] Support connectors part 2 - slash command and tui @mzeng-openai

> #10135 fix(ci) missing package.json for shell-mcp-tool @dylan-hurd-oai

> #10175 Add OpenAI docs MCP tooltip @joshka-oai

> #10182 fix: unify `npm publish` call across shell-tool-mcp.yml and rust-release.yml @bolinfest

> #10200 MCP tool call approval (simplified version) @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.93.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context Window changes in rust-v0.93.0]] · Context Window
- [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-31-10191-chore-app-server-document-authmode-owenlin0|♯10191 chore(app-server): document AuthMode @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-01-31-10011-really-fix-pwd-for-windows-codex-zip-iceweasel-oai|♯10011 really fix pwd for windows codex zip @iceweasel-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654 Show OAuth error descriptions in callback responses @blevy-oai]] · Account and Access
- [[Changes/Codex CLI/2026-01-31-3-interface-experience-changes-in-rust-v0-93-0|3 Interface Experience changes in rust-v0.93.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-31-3-reliability-and-performance-changes-in-rust-v0-93-0|3 Reliability and Performance changes in rust-v0.93.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-31-6-developer-workflow-changes-in-rust-v0-93-0|6 Developer Workflow changes in rust-v0.93.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-31-10030-clarify-external-editor-env-var-message-joshka-oai|♯10030 Clarify external editor env var message @joshka-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-31-3-search-and-browsing-changes-in-rust-v0-93-0|3 Search and Browsing changes in rust-v0.93.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-97-other-changes-in-rust-v0-93-0|97 other changes in rust-v0.93.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-30 · OpenCode · [[Changes/OpenCode/2026-01-30-2-apps-and-integrations-changes-in-v1-1-47-2|2 Apps and Integrations changes in v1.1.47 + 2]]
- Later: 2026-01-31 · OpenCode · [[Changes/OpenCode/2026-01-31-core-bump-ai-sdk-packages|Core Bump AI SDK packages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-31-c93021&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0.md%0ACard%20ID%3A%20codex-cli-2026-01-31-c93021%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.93.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->