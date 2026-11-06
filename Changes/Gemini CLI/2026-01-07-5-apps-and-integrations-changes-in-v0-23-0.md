---
card_id: gemini-cli-2026-01-07-eefb68
date: '2026-01-07'
description: 'Gemini CLI · 2026-01-07 · Apps and Integrations: 5 changes in Release
  v0.23.0 — Use official ACP SDK and support HTTP/SSE based MCP servers by @SteffenDE
  in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1021
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e62a36f417fc316eb250b1da5b67d7bd6b7f287e2b3a3a7f2fef8df458a769b9
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-07-eefb68
  comparison: ''
  date: '2026-01-07'
  description: 'Gemini CLI — Release v0.23.0: 5 Apps and Integrations changes'
  evidence:
  - quote: Use official ACP SDK and support HTTP/SSE based MCP servers by @SteffenDE
      in https://github.com/google-gemini/gemini-cli/pull/13856
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
  - quote: '(docs): Add reference section to hooks documentation by @abhipatel12 in
      https://github.com/google-gemini/gemini-cli/pull/15159'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
  - quote: 'feat(hooks): add support for friendly names and descriptions by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/15174'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
  - quote: 'feat(hooks): reduce log verbosity and improve error reporting in UI by
      @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15297'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
  - quote: 'feat(telemetry): add clearcut logging for hooks by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15405'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 5-apps-and-integrations-changes-in-v0-23-0
  source_release: gemini-cli-2026-01-07-v0-23-0-github-274690353-5e923999
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v0.23.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-01-05-sdk-releases|SDK Releases]]'
- '[[Changes/Cline/2026-01-06-exclude-binary-files-without-extensions-from-diffs|Exclude
  binary files without extensions from diffs]]'
- '[[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694
  MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-07-v0-23-0-github-274690353-5e923999|gemini-cli-2026-01-07-v0-23-0-github-274690353-5e923999]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v0.23.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v0.23.0

**Gemini CLI** · 2026-01-07 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-07-v0-23-0-github-274690353-5e923999|Release v0.23.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Use official ACP SDK and support HTTP/SSE based MCP servers by @SteffenDE in https://github.com/google-gemini/gemini-cli/pull/13856

> (docs): Add reference section to hooks documentation by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15159

> feat(hooks): add support for friendly names and descriptions by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15174

> feat(hooks): reduce log verbosity and improve error reporting in UI by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15297

> feat(telemetry): add clearcut logging for hooks by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15405

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.23.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-07-add-core-tool-that-adds-all-context-from-the-core-package-by-jacob314-in-https-g|Add core tool that adds all context from the core package]] · Context Window
- [[Changes/Gemini CLI/2026-01-07-3-agent-mode-changes-in-v0-23-0|3 Agent Mode changes in v0.23.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-01-07-4-developer-workflow-changes-in-v0-23-0|4 Developer Workflow changes in v0.23.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-07-chore-core-remove-legacy-fallback-flags-and-migrate-loop-detection-by-adamfweidm|chore(core): remove legacy fallback flags and migrate loop detection]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-01-07-3-model-support-changes-in-v0-23-0|3 Model Support changes in v0.23.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-07-feat-core-implement-jit-context-memory-loading-and-ui-sync-by-sandytao520-in-htt|feat(core): Implement JIT context memory loading and UI sync]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-01-07-validate-oauth-resource-parameter-matches-mcp-server-url-by-galz10-in-https-gith|Validate OAuth resource parameter matches MCP server URL]] · Account and Access
- [[Changes/Gemini CLI/2026-01-07-26-other-changes-in-v0-23-0|26 other changes in v0.23.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-06 · Codex CLI · [[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694 MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]]
- Later: 2026-01-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-07-shutdown-mcp-servers-after-subagent-execution-completes|Shutdown MCP servers after subagent execution completes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-07-eefb68&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-07-5-apps-and-integrations-changes-in-v0-23-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-07-eefb68%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.23.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->