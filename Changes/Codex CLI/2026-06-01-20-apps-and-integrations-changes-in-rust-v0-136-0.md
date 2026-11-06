---
card_id: codex-cli-2026-06-01-260622
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Apps and Integrations: 20 changes in 0.136.0
  — App-server integrations can resume a thread with its initial turns page, see richer
  MCP…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3090d0da1a6f564dc1513638e8aa9fb29ed877c0434cf537dd1862fbf3801c2a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-260622
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 20 Apps and Integrations changes'
  evidence:
  - quote: 'App-server integrations can resume a thread with its initial turns page,
      see richer MCP server status, and launch stdio mode with `codex app-server --stdio`.
      (#23534, #24698, #24940)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Python SDK beta docs and package metadata now present the standard `pip
      install openai-codex` path, refreshed quickstarts, API reference, FAQ, and examples.
      (#24836, #24866, #24868, #24870)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: Python SDK examples and docs now use the public `CodexConfig` name for
      configuring `Codex` / `AsyncCodex`. (#24800)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: Built-in tool schema descriptions now clarify defaults, optional fields,
      bounds, and enums across shell, Code Mode, MCP, image, goal, plan, multi-agent,
      and related tools. (#24794)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'App-server and exec-server docs now cover API-key remote registration,
      `--stdio`, runtime extra skill roots, and remote-control server-token behavior.
      (#24666, #24940, #24977, #24141)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Python SDK releases can now be staged and published independently from
      runtime releases using `python-v*` tags while preserving the reviewed runtime
      dependency pin. (#24828, #24872)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: Updated MCP dependencies to `rmcp` 1.7.0 and refreshed compatibility code.
      (#24763)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24800 [codex] Rename Python SDK AppServerConfig to CodexConfig @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24828 [codex] Add independent beta release for the Python SDK @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24836 [codex] Prepare Python SDK beta documentation and package metadata
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24866 [codex] Simplify Python SDK install guidance @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24868 [codex] Remove Python SDK language classifiers @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24870 [codex] Remove Python SDK beta warning note @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24872 [codex] Stage Python SDK beta versions from release tags @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24698 Expose MCP server info as part of server status @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25013 feat: Add focused diagnostics for MCP HTTP send failures @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24964 [codex] Wait for MCP readiness in core integration tests @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24996 Filter plugin install suggestions by installed apps @nm-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25172 [codex] Update remote connector suggestions @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25381 [codex] Avoid forced directory refresh during plugin install auth
      checks @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-apps-and-integrations-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: apps-integrations
  title: 20 Apps and Integrations changes in rust-v0.136.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-28-10-apps-and-integrations-changes-in-v1-0-55|10
  Apps and Integrations changes in v1.0.55]]'
- '[[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4
  Apps and Integrations changes in v2.1.157]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-apps-and-integrations-changes-in-v1-0-56|2
  Apps and Integrations changes in v1.0.56]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: apps-integrations
title: 20 Apps and Integrations changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Apps and Integrations changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server integrations can resume a thread with its initial turns page, see richer MCP server status, and launch stdio mode with `codex app-server --stdio`. (#23534, #24698, #24940)

> Python SDK beta docs and package metadata now present the standard `pip install openai-codex` path, refreshed quickstarts, API reference, FAQ, and examples. (#24836, #24866, #24868, #24870)

> Python SDK examples and docs now use the public `CodexConfig` name for configuring `Codex` / `AsyncCodex`. (#24800)

> Built-in tool schema descriptions now clarify defaults, optional fields, bounds, and enums across shell, Code Mode, MCP, image, goal, plan, multi-agent, and related tools. (#24794)

> App-server and exec-server docs now cover API-key remote registration, `--stdio`, runtime extra skill roots, and remote-control server-token behavior. (#24666, #24940, #24977, #24141)

> Python SDK releases can now be staged and published independently from runtime releases using `python-v*` tags while preserving the reviewed runtime dependency pin. (#24828, #24872)

> Updated MCP dependencies to `rmcp` 1.7.0 and refreshed compatibility code. (#24763)

> #24800 [codex] Rename Python SDK AppServerConfig to CodexConfig @aibrahim-oai

> #24828 [codex] Add independent beta release for the Python SDK @aibrahim-oai

> #24836 [codex] Prepare Python SDK beta documentation and package metadata @aibrahim-oai

> #24866 [codex] Simplify Python SDK install guidance @aibrahim-oai

> #24868 [codex] Remove Python SDK language classifiers @aibrahim-oai

> #24870 [codex] Remove Python SDK beta warning note @aibrahim-oai

> #24872 [codex] Stage Python SDK beta versions from release tags @aibrahim-oai

> #24698 Expose MCP server info as part of server status @gpeal

> #25013 feat: Add focused diagnostics for MCP HTTP send failures @xl-openai

> #24964 [codex] Wait for MCP readiness in core integration tests @anp-oai

> #24996 Filter plugin install suggestions by installed apps @nm-openai

> #25172 [codex] Update remote connector suggestions @ericning-o

> #25381 [codex] Avoid forced directory refresh during plugin install auth checks @xl-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11 Developer Workflow changes in rust-v0.136.0]] · Developer Workflow
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
## Nearby in Apps and Integrations

- Earlier: 2026-05-29 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-29-2-apps-and-integrations-changes-in-v1-0-56|2 Apps and Integrations changes in v1.0.56]]
- Later: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5 Apps and Integrations changes in v1.0.57]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-260622&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-260622%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->