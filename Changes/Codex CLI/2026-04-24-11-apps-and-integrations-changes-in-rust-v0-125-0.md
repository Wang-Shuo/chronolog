---
card_id: codex-cli-2026-04-24-e7d4f3
date: '2026-04-24'
description: 'Codex CLI · 2026-04-24 · Apps and Integrations: 11 changes in 0.125.0
  — App-server integrations now support Unix socket transport, pagination-friendly…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 96ddd8a39ffb3f72cfe42a90ac458d5d6345c8288dcb8fd26c7a87379cf9f719
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-24-e7d4f3
  comparison: ''
  date: '2026-04-24'
  description: 'Codex CLI — 0.125.0: 11 Apps and Integrations changes'
  evidence:
  - quote: 'App-server integrations now support Unix socket transport, pagination-friendly
      resume/fork, sticky environments, and remote thread config/store plumbing. (#18255,
      #18892, #18897, #18908, #19008, #19014)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'App-server plugin management can install remote plugins and upgrade configured
      marketplaces. (#18917, #19074)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'Config/schema handling now rejects conflicting MultiAgentV2 thread limits,
      resolves relative agent-role config paths, hides unsupported MCP bearer-token
      fields, and rejects invalid `js_repl` image MIME types. (#19129, #19261, #19294,
      #19292)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'Plugin marketplace add/remove/startup-sync internals moved out of `codex-core`,
      and curated plugin cache versions now use short SHAs. (#19099, #19095)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'Stabilized flaky approval-popup and plugin MCP tool-discovery tests. (#19178,
      #19191)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18710 [codex] Fix plugin marketplace help usage @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19191 Stabilize plugin MCP tools test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19194 Mark hooks schema fixtures as generated @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19095 feat: Use short SHA versions for curated plugin cache entries @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18917 [codex] Support remote plugin install writes @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19294 Hide unsupported MCP bearer_token from config schema @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-125-0
  source_release: codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.125.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-04-23-4-apps-and-integrations-changes-in-v0-39-0|4 Apps
  and Integrations changes in v0.39.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-23-3-apps-and-integrations-changes-in-v1-0-35|3
  Apps and Integrations changes in v1.0.35]]'
- '[[Changes/Ollama/2026-04-23-openclaw-integration-now-bundles-ollama-s-web-search-plugin-in-openclaw|OpenClaw
  integration now bundles Ollama''s web search plugin in OpenClaw]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.125.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.125.0

**Codex CLI** · 2026-04-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.125.0) · from [[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server integrations now support Unix socket transport, pagination-friendly resume/fork, sticky environments, and remote thread config/store plumbing. (#18255, #18892, #18897, #18908, #19008, #19014)

> App-server plugin management can install remote plugins and upgrade configured marketplaces. (#18917, #19074)

> Config/schema handling now rejects conflicting MultiAgentV2 thread limits, resolves relative agent-role config paths, hides unsupported MCP bearer-token fields, and rejects invalid `js_repl` image MIME types. (#19129, #19261, #19294, #19292)

> Plugin marketplace add/remove/startup-sync internals moved out of `codex-core`, and curated plugin cache versions now use short SHAs. (#19099, #19095)

> Stabilized flaky approval-popup and plugin MCP tool-discovery tests. (#19178, #19191)

> #18710 [codex] Fix plugin marketplace help usage @xli-oai

> #19191 Stabilize plugin MCP tools test @etraut-openai

> #19194 Mark hooks schema fixtures as generated @abhinav-oai

> #19095 feat: Use short SHA versions for curated plugin cache entries @xl-openai

> #18917 [codex] Support remote plugin install writes @xli-oai

> #19294 Hide unsupported MCP bearer_token from config schema @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.125.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Context Window
- [[Changes/Codex CLI/2026-04-24-19167-ci-add-macos-keychain-entitlements-euroelessar|♯19167 ci: add macOS keychain entitlements @euroelessar]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-24-windows-bazel-ci-now-uses-a-stable-path-and-shared-query-startup-path-for-better|Windows Bazel CI now uses a stable PATH and shared query startup path for better…]] · Collaboration
- [[Changes/Codex CLI/2026-04-24-2-developer-workflow-changes-in-rust-v0-125-0|2 Developer Workflow changes in rust-v0.125.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-24-5-model-support-changes-in-rust-v0-125-0|5 Model Support changes in rust-v0.125.0]] · Model Support
- [[Changes/Codex CLI/2026-04-24-32-other-changes-in-rust-v0-125-0|32 other changes in rust-v0.125.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-23 · Ollama · [[Changes/Ollama/2026-04-23-openclaw-integration-now-bundles-ollama-s-web-search-plugin-in-openclaw|OpenClaw integration now bundles Ollama's web search plugin in OpenClaw]]
- Later: 2026-04-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-24-remote-command-shows-current-status-and-supports-remote-on-and-remote-off-to-tog|/remote command shows current status and supports /remote on and /remote off…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-24-e7d4f3&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0.md%0ACard%20ID%3A%20codex-cli-2026-04-24-e7d4f3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.125.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->