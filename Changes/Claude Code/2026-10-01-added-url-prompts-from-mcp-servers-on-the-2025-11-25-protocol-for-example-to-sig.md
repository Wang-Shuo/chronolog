---
card_id: claude-code-2026-10-01-dd8194
date: '2026-10-01'
description: 'Claude Code · 2026-10-01 · Account and Access: Added URL prompts from
  MCP servers on the 2025-11-25 protocol, for example to sign in. If a server no longer…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 7e4598c697c0523c415551a8ef21952d2c0ae44aacc08d3d193cce9045b92029
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-01-dd8194
  comparison: ''
  date: '2026-10-01'
  description: 'Claude Code — v2.1.287: Added URL prompts from MCP servers on the
    2025-11-25 protocol, for example to sign in. If a server no longer connects after
    this update, add "bareElicitationCapability": true to its MCP config entry'
  evidence:
  - quote: 'Added URL prompts from MCP servers on the 2025-11-25 protocol, for example
      to sign in. If a server no longer connects after this update, add "bareElicitationCapability":
      true to its MCP config entry'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig
  source_release: claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87
  source_type: github_releases
  theme: account-access
  theme_matches:
  - matched_terms:
    - sign in
    score: 60
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: Added URL prompts from MCP servers on the 2025-11-25 protocol, for example
    to sign in
  type: change
related_changes:
- '[[Changes/Cline/2026-09-30-if-a-new-task-fails-cline-sign-in-signing-in-and-submitting-a-revised-prompt-now|If
  a new task fails Cline sign-in, signing in and submitting a revised prompt now…]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-mcp-oauth-sign-in-to-servers-such-as-datadog-reuses-a-still-valid-cached-token|MCP
  OAuth sign-in to servers such as Datadog reuses a still-valid cached token]]'
- '[[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account
  and Access changes in v2026.9.7]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87]]'
source_type: github_releases
theme: account-access
title: Added URL prompts from MCP servers on the 2025-11-25 protocol, for example
  to sign in
type: change
---

<!-- chronolog:begin region="header" -->
# Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in

**Claude Code** · 2026-10-01 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) · from [[Releases/Claude Code/claude-code-2026-10-01-v2-1-287-github-401174143-9cfdbb87|v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in. If a server no longer connects after this update, add "bareElicitationCapability": true to its MCP config entry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-01-4-model-support-changes-in-v2-1-287|4 Model Support changes in v2.1.287]] · Model Support
- [[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-01-vscode-changed-the-claude-in-chrome-enabled-by-default-switch-to-also-connect-th|VSCode Changed the Claude in Chrome "Enabled by default" switch to also connect…]] · Editor Experience
- [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-01-3-developer-workflow-changes-in-v2-1-287|3 Developer Workflow changes in v2.1.287]] · Developer Workflow
- [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-01-changed-screen-reader-mode-to-write-new-or-changed-lines-without-first-pausing-w|Changed screen reader mode to write new or changed lines without first pausing…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-01-3-reliability-and-performance-changes-in-v2-1-287|3 Reliability and Performance changes in v2.1.287]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]] · Agent Mode
- [[Changes/Claude Code/2026-10-01-improved-memory-the-left-and-right-arrow-keys-now-flip-its-on-off-settings-such|Improved /memory: the left and right arrow keys now flip its on/off settings, such…]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved SDK sessions so a message sent with priority "now" no longer cancels…]] · Search and Browsing
- [[Changes/Claude Code/2026-10-01-4-other-changes-in-v2-1-287|4 other changes in v2.1.287]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-30 · OpenClaw · [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]]
- Later: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-2-account-and-access-changes-in-rust-v0-160-0|2 Account and Access changes in rust-v0.160.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-01-dd8194&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig.md%0ACard%20ID%3A%20claude-code-2026-10-01-dd8194%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.287%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->