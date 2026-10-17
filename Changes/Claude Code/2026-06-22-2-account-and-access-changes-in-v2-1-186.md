---
card_id: claude-code-2026-06-22-f69227
date: '2026-06-22'
description: 'Claude Code · 2026-06-22 · Account and Access: 2 changes in v2.1.186
  — Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate
  MCP…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 956ba24240efb9a4d7750199139b77d66320f0c179016823c79c8fac541c39ee
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-22-f69227
  comparison: ''
  date: '2026-06-22'
  description: 'Claude Code — v2.1.186: 2 Account and Access changes'
  evidence:
  - quote: Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate
      MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser`
      stdin redirect support for completing over SSH
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
  - quote: Added "Claude Platform on AWS - refresh credentials" option to `/login`
      when `awsAuthRefresh` is configured
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-account-and-access-changes-in-v2-1-186
  source_release: claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v2.1.186
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|Added
  a prompt before writing to shell startup files…]]'
- '[[Changes/Claude Code/2026-06-08-improved-the-error-message-shown-when-your-organization-has-disabled-api-key-aut|Improved
  the error message shown when your organization has disabled API key…]]'
- '[[Changes/Claude Code/2026-06-17-improved-the-mcp-oauth-browser-page-to-match-claude-code-s-visual-style-and-auto|Improved
  the MCP OAuth browser page to match Claude Code''s visual style…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b|claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v2.1.186
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v2.1.186

**Claude Code** · 2026-06-22 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.186) · from [[Releases/Claude Code/claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b|v2.1.186]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing over SSH

> Added "Claude Platform on AWS - refresh credentials" option to `/login` when `awsAuthRefresh` is configured

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-22-2-apps-and-integrations-changes-in-v2-1-186|2 Apps and Integrations changes in v2.1.186]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-22-improved-memory-the-agent-is-now-reminded-to-compact-its-memory-md-index-when-ne|Improved memory: the agent is now reminded to compact its MEMORY.md index…]] · Memory and Personalization
- [[Changes/Claude Code/2026-06-22-changed-review-pr-to-use-the-same-review-engine-as-code-review-medium|Changed /review pr to use the same review engine as /code-review medium]] · Developer Workflow
- [[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety and Privacy changes in v2.1.186]] · Safety and Privacy
- [[Changes/Claude Code/2026-06-22-bash-commands-now-trigger-claude-to-respond-to-the-output-automatically-set-resp|! bash commands now trigger Claude to respond to the output automatically]] · Context Window
- [[Changes/Claude Code/2026-06-22-2-agent-mode-changes-in-v2-1-186|2 Agent Mode changes in v2.1.186]] · Agent Mode
- [[Changes/Claude Code/2026-06-22-3-other-changes-in-v2-1-186|3 other changes in v2.1.186]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-06-17 · Claude Code · [[Changes/Claude Code/2026-06-17-improved-the-mcp-oauth-browser-page-to-match-claude-code-s-visual-style-and-auto|Improved the MCP OAuth browser page to match Claude Code's visual style…]]
- Later: 2026-06-24 · Claude Code · [[Changes/Claude Code/2026-06-24-improved-mcp-oauth-discovery-and-token-requests-now-retry-once-after-transient-n|Improved MCP OAuth]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-22-f69227&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-22-2-account-and-access-changes-in-v2-1-186.md%0ACard%20ID%3A%20claude-code-2026-06-22-f69227%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.186%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->