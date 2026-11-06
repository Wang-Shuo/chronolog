---
card_id: github-copilot-cli-2026-05-20-c1b860
date: '2026-05-20'
description: 'GitHub Copilot CLI · 2026-05-20 · Apps and Integrations: 4 changes in
  1.0.51 — /remote commands now respect organization remote control and view from
  cloud…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c7b5e25489ce9903793941ebc12d9e8133e8159b0ae78ae8280ef5947e54a814
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-20-c1b860
  comparison: ''
  date: '2026-05-20'
  description: 'GitHub Copilot CLI — 1.0.51: 4 Apps and Integrations changes'
  evidence:
  - quote: /remote commands now respect organization remote control and view from
      cloud policy and show a clear error when disabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.51
  - quote: MCP tool loading at startup is faster for users with many HTTP-based MCP
      servers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.51
  - quote: Add preMcpToolCall hook for hook providers to control outgoing MCP request
      metadata
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.51
  - quote: postToolUse hooks can now inject additionalContext into successful tool
      results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.51
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-apps-and-integrations-changes-in-v1-0-51
  source_release: github-copilot-cli-2026-05-20-v1-0-51-github-326293635-21098fc1
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v1.0.51
  type: change
related_changes:
- '[[Changes/Gemini/2026-05-19-gemini-can-connect-to-more-apps-starting-with-opentable-canva-and-instacart|Gemini
  can connect to more apps, starting with OpenTable, Canva, and Instacart]]'
- '[[Changes/GitHub Copilot CLI/2026-05-19-9-apps-and-integrations-changes-in-v1-0-49|9
  Apps and Integrations changes in v1.0.49]]'
- '[[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9
  Apps and Integrations changes in rust-v0.132.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-20-v1-0-51-github-326293635-21098fc1|github-copilot-cli-2026-05-20-v1-0-51-github-326293635-21098fc1]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v1.0.51
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v1.0.51

**GitHub Copilot CLI** · 2026-05-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.51) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-20-v1-0-51-github-326293635-21098fc1|1.0.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> /remote commands now respect organization remote control and view from cloud policy and show a clear error when disabled

> MCP tool loading at startup is faster for users with many HTTP-based MCP servers

> Add preMcpToolCall hook for hook providers to control outgoing MCP request metadata

> postToolUse hooks can now inject additionalContext into successful tool results

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.51
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-20-github-mcp-web-search-tool-is-available-immediately-without-requiring-tool-searc|GitHub MCP web search tool is available immediately without requiring tool search]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-05-20-4-developer-workflow-changes-in-v1-0-51|4 Developer Workflow changes in v1.0.51]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-20-customizable-status-line-in-the-terminal-footer-displays-session-info-such-as-mo|Customizable status line in the terminal footer displays session info such as model…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-20-shell-tool-calls-succeed-even-when-the-model-omits-the-description-parameter|Shell tool calls succeed even when the model omits the description parameter]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-20-remote-command-can-now-be-used-while-the-agent-is-working|/remote command can now be used while the agent is working]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-20-2-editor-experience-changes-in-v1-0-51|2 Editor Experience changes in v1.0.51]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-20-memory-show-displays-documentation-links-for-learning-about-and-managing-copilot|/memory show displays documentation links for learning about and managing Copilot Memory]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-05-20-2-account-and-access-changes-in-v1-0-51|2 Account and Access changes in v1.0.51]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-20-2-pricing-model-changes-in-v1-0-51|2 Pricing Model changes in v1.0.51]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add /security-review slash command to review code changes for security…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-20-6-other-changes-in-v1-0-51|6 other changes in v1.0.51]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-20 · Codex CLI · [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]]
- Later: 2026-05-21 · Codex CLI · [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-20-c1b860&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-20-4-apps-and-integrations-changes-in-v1-0-51.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-20-c1b860%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.51%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->