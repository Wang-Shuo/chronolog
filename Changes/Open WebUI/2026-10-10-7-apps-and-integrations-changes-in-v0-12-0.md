---
card_id: open-webui-2026-10-10-278657
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Apps and Integrations: 7 changes in v0.12.0
  — \U0001F5DC️ **Tool Search for large tool sets.** Administrators can now turn on
  Tool Search…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1297
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2a56c93d57d08a4e22bd8d0fdf7cdd9332d63773ce7cbe1876b6f70adacd2e7d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-278657
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 7 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F5DC️ **Tool Search for large tool sets.** Administrators can now
      turn on Tool Search, marked experimental, in Admin Settings > Interface, so
      tools with long definitions are left out of the request and only listed by name
      and a short description, and the model looks up the full definition with a `search_tools`
      tool when it needs one, which keeps the prompt small and the prompt cache intact
      when many tools or MCP servers are enabled; the Deferral Threshold sets the
      definition length in characters above which a tool is held back, Always Loaded
      Tools takes names or patterns such as github\\_\\* that are always sent, and
      Defer Built-in Tools decides whether built-in tools are held back too. It applies
      with native function calling and can be set with \"ENABLE_TOOL_SEARCH\", \"TOOL_SEARCH_DEFER_THRESHOLD\",
      \"TOOL_SEARCH_ALWAYS_LOADED\" and \"TOOL_SEARCH_DEFER_BUILTIN_TOOLS\". [Commit](https://github.com/open-webui/open-webui/commit/088830cf82f6ac430653079668fc2c66d830f164)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F39A️ **Separate switches for Tools, Functions and tool servers.**
      Administrators can now turn off workspace Tools, Functions or external tool
      servers on their own with \"ENABLE_TOOLS\", \"ENABLE_FUNCTIONS\" and \"ENABLE_TOOL_SERVERS\",
      so in-process plugins can be switched off while OpenAPI, MCP and Open Terminal
      servers keep working, or the other way round. [Commit](https://github.com/open-webui/open-webui/commit/f50f9e6252209760d0b96f090766e91fb826ecba),
      [#31509](https://github.com/open-webui/open-webui/issues/31509)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAAB **Unreachable MCP servers shown as a status.** When an MCP
      server attached to a chat cannot be reached, the reply now shows a \"Failed
      to connect to MCP server\" status line and carries on without that server's
      tools, instead of marking the reply with an error. [Commit](https://github.com/open-webui/open-webui/commit/6defd4a9479ad82d4736df6c382d38ba54650dd1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4F8 **MCP tool images reach the model.** An image returned by an
      MCP tool, such as a camera snapshot, is now handed to the model as well as shown
      in the tool call, so the model can answer about what it shows. [#30358](https://github.com/open-webui/open-webui/pull/30358),
      [#30327](https://github.com/open-webui/open-webui/issues/30327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⌛ **MCP tool call timeout.** MCP tool calls now stop after the time set
      in "AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER", or "AIOHTTP_CLIENT_TIMEOUT" when that
      is unset, and the model sees the timeout as a tool error, where a hung MCP server
      kept the chat waiting until the connection was closed. [#31641](https://github.com/open-webui/open-webui/pull/31641),
      [#31640](https://github.com/open-webui/open-webui/issues/31640)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✂️ **Long MCP tool names.** Chats with an MCP server whose ID plus tool
      name is longer than 64 characters no longer fail on providers that cap tool
      names at 64 characters, such as the OpenAI API and AWS Bedrock; those names
      are now shortened with a stable hash ending while the MCP server is still called
      with the original tool name. [#31822](https://github.com/open-webui/open-webui/pull/31822),
      [#31821](https://github.com/open-webui/open-webui/issues/31821)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E6 **Structured results from MCP tools.** When an MCP tool returns
      structured data alongside its text, the model now receives that data too, where
      only the text part reached it and tools that put their real result in the structured
      part looked empty. [Commit](https://github.com/open-webui/open-webui/commit/22102e4a24863808793ddb9f53b599e274347280),
      [#28926](https://github.com/open-webui/open-webui/issues/28926)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-apps-and-integrations-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3
  Apps and Integrations changes in v2.1.296]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-managed-plugin-setup-retries-hourly-or-after-policy-changes-instead-of-on-every|Managed
  plugin setup retries hourly or after policy changes instead of on every…]]'
- '[[Changes/Lovable/2026-10-09-generate-a-secret-that-another-app-also-needs|Generate
  a secret that another app also needs]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗜️ **Tool Search for large tool sets.** Administrators can now turn on Tool Search, marked experimental, in Admin Settings > Interface, so tools with long definitions are left out of the request and only listed by name and a short description, and the model looks up the full definition with a `search_tools` tool when it needs one, which keeps the prompt small and the prompt cache intact when many tools or MCP servers are enabled; the Deferral Threshold sets the definition length in characters above which a tool is held back, Always Loaded Tools takes names or patterns such as github\_\* that are always sent, and Defer Built-in Tools decides whether built-in tools are held back too. It applies with native function calling and can be set with "ENABLE_TOOL_SEARCH", "TOOL_SEARCH_DEFER_THRESHOLD", "TOOL_SEARCH_ALWAYS_LOADED" and "TOOL_SEARCH_DEFER_BUILTIN_TOOLS". [Commit](https://github.com/open-webui/open-webui/commit/088830cf82f6ac430653079668fc2c66d830f164)

> 🎚️ **Separate switches for Tools, Functions and tool servers.** Administrators can now turn off workspace Tools, Functions or external tool servers on their own with "ENABLE_TOOLS", "ENABLE_FUNCTIONS" and "ENABLE_TOOL_SERVERS", so in-process plugins can be switched off while OpenAPI, MCP and Open Terminal servers keep working, or the other way round. [Commit](https://github.com/open-webui/open-webui/commit/f50f9e6252209760d0b96f090766e91fb826ecba), [#31509](https://github.com/open-webui/open-webui/issues/31509)

> 🪫 **Unreachable MCP servers shown as a status.** When an MCP server attached to a chat cannot be reached, the reply now shows a "Failed to connect to MCP server" status line and carries on without that server's tools, instead of marking the reply with an error. [Commit](https://github.com/open-webui/open-webui/commit/6defd4a9479ad82d4736df6c382d38ba54650dd1)

> 📸 **MCP tool images reach the model.** An image returned by an MCP tool, such as a camera snapshot, is now handed to the model as well as shown in the tool call, so the model can answer about what it shows. [#30358](https://github.com/open-webui/open-webui/pull/30358), [#30327](https://github.com/open-webui/open-webui/issues/30327)

> ⌛ **MCP tool call timeout.** MCP tool calls now stop after the time set in "AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER", or "AIOHTTP_CLIENT_TIMEOUT" when that is unset, and the model sees the timeout as a tool error, where a hung MCP server kept the chat waiting until the connection was closed. [#31641](https://github.com/open-webui/open-webui/pull/31641), [#31640](https://github.com/open-webui/open-webui/issues/31640)

> ✂️ **Long MCP tool names.** Chats with an MCP server whose ID plus tool name is longer than 64 characters no longer fail on providers that cap tool names at 64 characters, such as the OpenAI API and AWS Bedrock; those names are now shortened with a stable hash ending while the MCP server is still called with the original tool name. [#31822](https://github.com/open-webui/open-webui/pull/31822), [#31821](https://github.com/open-webui/open-webui/issues/31821)

> 📦 **Structured results from MCP tools.** When an MCP tool returns structured data alongside its text, the model now receives that data too, where only the text part reached it and tools that put their real result in the structured part looked empty. [Commit](https://github.com/open-webui/open-webui/commit/22102e4a24863808793ddb9f53b599e274347280), [#28926](https://github.com/open-webui/open-webui/issues/28926)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-09 · Lovable · [[Changes/Lovable/2026-10-09-generate-a-secret-that-another-app-also-needs|Generate a secret that another app also needs]]
- Later: 2026-10-11 · Ollama · [[Changes/Ollama/2026-10-11-ollama-launch-claude-no-longer-shows-a-warning-about-claude-connectors-by-hoyyev|ollama launch claude no longer shows a warning about Claude connectors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-278657&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-7-apps-and-integrations-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-278657%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->