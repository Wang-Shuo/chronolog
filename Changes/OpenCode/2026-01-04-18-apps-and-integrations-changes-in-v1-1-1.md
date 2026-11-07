---
card_id: opencode-2026-01-04-7c45c1
date: '2026-01-04'
description: 'OpenCode · 2026-01-04 · Apps and Integrations: 18 changes in v1.1.1
  — Breaking Changes for SDK Users Updated : { id, type, pattern, sessionID, messageID…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1018
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 314b405431addb55ed4a2a2358b9686dd0e43191f0b8983aa124fccc201fc91e
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-01-04-7c45c1
  comparison: ''
  date: '2026-01-04'
  description: 'OpenCode — v1.1.1: 18 Apps and Integrations changes'
  evidence:
  - quote: 'Breaking Changes for SDK Users Updated : { id, type, pattern, sessionID,
      messageID, callID, message, metadata, time }'
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: 'Breaking Changes for SDK Users Replied : { sessionID, permissionID, response
      }'
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: 'Breaking Changes for SDK Users Replied : { sessionID, requestID, reply
      }'
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users pattern is now patterns (array of strings)
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users message field removed
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users response renamed to reply
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users permissionID renamed to requestID
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users New always field contains patterns that
      would be approved for future requests if user selects "always"
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Other Changes Mode and plugin globs no longer search subdirectories (simplified
      to top-level only)
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Ensure @opencode-ai/plugin exists only on first run
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add MCP resources support
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Prevent duplicate plugin function initialization
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add timeout to MCP client connection calls
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add per-project MCP config overrides
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Improve plugin loading to handle builtin plugin failures gracefully
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add Kotlin LSP integration
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Fix Cloudflare AI Gateway SDK chat undefined error
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Terminal Make MCP status icon muted when no MCP servers are enabled
    source_release: https://opencode.ai/changelog/v1.1.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 18-apps-and-integrations-changes-in-v1-1-1
  source_release: opencode-2026-01-04-v1-1-1-588acaae
  source_type: opencode_changelog
  theme: apps-integrations
  title: 18 Apps and Integrations changes in v1.1.1
  type: change
related_changes:
- '[[Changes/OpenCode/2025-12-31-default-to-ai-sdk-openai-compatible-when-no-npm-package-is-provided|Default
  to ai-sdk/openai-compatible when no npm package is provided]]'
- '[[Changes/OpenCode/2025-12-31-core-display-mcp-tag-for-prompts-in-autocomplete-but-not-in-prompt|Core
  Display MCP tag for prompts in autocomplete but not in prompt]]'
- '[[Changes/GitHub Copilot CLI/2026-01-02-mcp-server-type-help-text-displays-correct-options|MCP
  server type help text displays correct options]]'
source_release: '[[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|opencode-2026-01-04-v1-1-1-588acaae]]'
source_type: opencode_changelog
theme: apps-integrations
title: 18 Apps and Integrations changes in v1.1.1
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Apps and Integrations changes in v1.1.1

**OpenCode** · 2026-01-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://opencode.ai/changelog/v1.1.1) · from [[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|v1.1.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Breaking Changes for SDK Users Updated : { id, type, pattern, sessionID, messageID, callID, message, metadata, time }

> Breaking Changes for SDK Users Replied : { sessionID, permissionID, response }

> Breaking Changes for SDK Users Replied : { sessionID, requestID, reply }

> Breaking Changes for SDK Users pattern is now patterns (array of strings)

> Breaking Changes for SDK Users message field removed

> Breaking Changes for SDK Users response renamed to reply

> Breaking Changes for SDK Users permissionID renamed to requestID

> Breaking Changes for SDK Users New always field contains patterns that would be approved for future requests if user selects "always"

> Other Changes Mode and plugin globs no longer search subdirectories (simplified to top-level only)

> Core Ensure @opencode-ai/plugin exists only on first run

> Core Add MCP resources support

> Core Prevent duplicate plugin function initialization

> Core Add timeout to MCP client connection calls

> Core Add per-project MCP config overrides

> Core Improve plugin loading to handle builtin plugin failures gracefully

> Core Add Kotlin LSP integration

> Core Fix Cloudflare AI Gateway SDK chat undefined error

> Terminal Make MCP status icon muted when no MCP servers are enabled

Source: https://opencode.ai/changelog/v1.1.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-01-04-13-safety-and-privacy-changes-in-v1-1-1|13 Safety and Privacy changes in v1.1.1]] · Safety and Privacy
- [[Changes/OpenCode/2026-01-04-3-model-support-changes-in-v1-1-1|3 Model Support changes in v1.1.1]] · Model Support
- [[Changes/OpenCode/2026-01-04-19-developer-workflow-changes-in-v1-1-1|19 Developer Workflow changes in v1.1.1]] · Developer Workflow
- [[Changes/OpenCode/2026-01-04-core-handle-notfounderror-for-non-shared-sessions-in-sync|Core Handle NotFoundError for non-shared sessions in sync]] · Collaboration
- [[Changes/OpenCode/2026-01-04-13-mobile-and-desktop-changes-in-v1-1-1|13 Mobile and Desktop changes in v1.1.1]] · Mobile and Desktop
- [[Changes/OpenCode/2026-01-04-core-add-tui-session-selection-api-endpoint-for-navigation|Core Add TUI session selection API endpoint for navigation]] · Interface Experience
- [[Changes/OpenCode/2026-01-04-4-agent-mode-changes-in-v1-1-1|4 Agent Mode changes in v1.1.1]] · Agent Mode
- [[Changes/OpenCode/2026-01-04-2-editor-experience-changes-in-v1-1-1|2 Editor Experience changes in v1.1.1]] · Editor Experience
- [[Changes/OpenCode/2026-01-04-2-context-window-changes-in-v1-1-1|2 Context Window changes in v1.1.1]] · Context Window
- [[Changes/OpenCode/2026-01-04-3-reliability-and-performance-changes-in-v1-1-1|3 Reliability and Performance changes in v1.1.1]] · Reliability and Performance
- [[Changes/OpenCode/2026-01-04-17-other-changes-in-v1-1-1|17 other changes in v1.1.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-02 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-02-mcp-server-type-help-text-displays-correct-options|MCP server type help text displays correct options]]
- Later: 2026-01-05 · ElevenLabs · [[Changes/ElevenLabs/2026-01-05-sdk-releases|SDK Releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-01-04-7c45c1&body=Card%3A%20Changes%2FOpenCode%2F2026-01-04-18-apps-and-integrations-changes-in-v1-1-1.md%0ACard%20ID%3A%20opencode-2026-01-04-7c45c1%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.1.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->