---
card_id: claude-code-2026-09-14-55a66f
date: '2026-09-14'
description: 'Claude Code · 2026-09-14 · Apps and Integrations: 5 changes in v2.1.271
  — Added `--accept-command <sha256>` to `claude plugin install` and `claude plugin…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1271
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e5ece67e506693fba5fd5096467c705a8775c22dd1009b083c0a631ee1eba5ae
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-14-55a66f
  comparison: ''
  date: '2026-09-14'
  description: 'Claude Code — v2.1.271: 5 Apps and Integrations changes'
  evidence:
  - quote: Added `--accept-command <sha256>` to `claude plugin install` and `claude
      plugin update` to accept exactly the command a previous `--json` run displayed,
      instead of `-y`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Improved Remote Control to leave fewer empty sessions on claude.ai when
      setup fails on a flaky network
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved `claude mcp serve`: a running tool call now sends a progress
      update every 30 seconds, so clients show it is still running and idle timeouts
      don''t abort a long command that prints nothing'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved Foundry and Claude Platform on AWS sessions: an `alwaysLoad`
      MCP server that finishes connecting mid-conversation is usable on the next turn
      without a tool-search round trip'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: '[VSCode] Improved the Hooks dialog: a save refused because of the settings
      file itself now opens a popup with an "Open settings file" button and the reason
      behind "Copy error"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-271
  source_release: claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.271
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added
  /output-style name to list and switch output styles, including over Remote…]]'
- '[[Changes/ChatGPT/2026-09-14-for-new-health-plugin-connections-chatgpt-will-now-default-to-each-user-s-global|For
  new Health plugin connections, ChatGPT will now default to each user’s global…]]'
- '[[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You
  can change your Health permissions anytime in Settings → Plugins → Health]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.271
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.271

**Claude Code** · 2026-09-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.271) · from [[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|v2.1.271]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--accept-command <sha256>` to `claude plugin install` and `claude plugin update` to accept exactly the command a previous `--json` run displayed, instead of `-y`

> Improved Remote Control to leave fewer empty sessions on claude.ai when setup fails on a flaky network

> Improved `claude mcp serve`: a running tool call now sends a progress update every 30 seconds, so clients show it is still running and idle timeouts don't abort a long command that prints nothing

> Improved Foundry and Claude Platform on AWS sessions: an `alwaysLoad` MCP server that finishes connecting mid-conversation is usable on the next turn without a tool-search round trip

> [VSCode] Improved the Hooks dialog: a save refused because of the settings file itself now opens a popup with an "Open settings file" button and the reason behind "Copy error"

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]] · Account and Access
- [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]] · Pricing Model
- [[Changes/Claude Code/2026-09-14-2-files-and-data-changes-in-v2-1-271|2 Files and Data changes in v2.1.271]] · Files and Data
- [[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor Experience changes in v2.1.271]] · Editor Experience
- [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]] · Context Window
- [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Agent Mode
- [[Changes/Claude Code/2026-09-14-improved-terminal-rendering-performance-large-diffs-and-long-transcripts-render|Improved terminal rendering performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-14-2-mobile-and-desktop-changes-in-v2-1-271|2 Mobile and Desktop changes in v2.1.271]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-14-3-interface-experience-changes-in-v2-1-271|3 Interface Experience changes in v2.1.271]] · Interface Experience
- [[Changes/Claude Code/2026-09-14-improved-startup-time-slightly-by-skipping-a-redundant-validation-of-built-in-mo|Improved startup time slightly by skipping a redundant validation of built-in model…]] · Model Support
- [[Changes/Claude Code/2026-09-14-9-other-changes-in-v2-1-271|9 other changes in v2.1.271]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-14 · ChatGPT · [[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You can change your Health permissions anytime in Settings → Plugins → Health]]
- Later: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-14-55a66f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-14-5-apps-and-integrations-changes-in-v2-1-271.md%0ACard%20ID%3A%20claude-code-2026-09-14-55a66f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.271%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->