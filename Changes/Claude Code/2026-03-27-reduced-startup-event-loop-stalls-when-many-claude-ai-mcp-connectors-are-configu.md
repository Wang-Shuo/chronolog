---
card_id: claude-code-2026-03-27-dcb91e
date: '2026-03-27'
description: 'Claude Code · 2026-03-27 · Apps and Integrations: Reduced startup event-loop
  stalls when many claude.ai MCP connectors are configured (macOS keychain cache…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You
    can join the waitlist to try plugins here]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1100
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 437355e0092f140347774a431fcafc1e10805fb8e27ec64139dbbbe9f192ec01
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-27-dcb91e
  comparison: ''
  date: '2026-03-27'
  description: 'Claude Code — v2.1.86: Reduced startup event-loop stalls when many
    claude.ai MCP connectors are configured (macOS keychain cache extended from 5s
    to 30s)'
  evidence:
  - quote: Reduced startup event-loop stalls when many claude.ai MCP connectors are
      configured (macOS keychain cache extended from 5s to 30s)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu
  source_release: claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859
  source_type: github_releases
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - connectors
    - mcp
    score: 100
    theme: apps-integrations
  - matched_terms:
    - macos
    score: 50
    theme: mobile-desktop
  title: Reduced startup event-loop stalls when many claude.ai MCP connectors are
    configured…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-claude-code-mcp-server-name-and-claude-code-mcp-server-url-environment-var|Added
  CLAUDE_CODE_MCP_SERVER_NAME and CLAUDE_CODE_MCP_SERVER_URL environment…]]'
- '[[Changes/Claude Code/2026-03-26-deep-link-queries-claude-cli-open-q-now-support-up-to-5-000-characters-with-a-sc|Deep
  link queries (claude-cli://open?q=…) now support up to 5,000 characters…]]'
- '[[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|ChatGPT
  rolls out updated Box, Notion, Linear, and Dropbox apps]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
source_type: github_releases
theme: apps-integrations
title: Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…
type: change
---

<!-- chronolog:begin region="header" -->
# Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…

**Claude Code** · 2026-03-27 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.86) · from [[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|v2.1.86]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Reduced startup event-loop stalls when many claude.ai MCP connectors are configured (macOS keychain cache extended from 5s to 30s)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|Reduced token overhead when mentioning files with @]] · Context Window
- [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|Added .jj and .sl to VCS directory exclusion lists so Grep and file autocomplete…]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-27 · ChatGPT · [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|ChatGPT rolls out updated Box, Notion, Linear, and Dropbox apps]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|Added MCP_CONNECTION_NONBLOCKING=true for -p mode to skip the MCP connection…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-you-can-join-the-waitlist-to-try-plugins-here|You can join the waitlist to try plugins here]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-27-dcb91e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu.md%0ACard%20ID%3A%20claude-code-2026-03-27-dcb91e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.86%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->