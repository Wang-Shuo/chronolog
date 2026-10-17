---
card_id: claude-code-2026-09-15-9f3cc0
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Account and Access: 4 changes in v2.1.273
  — Improved `/autofix-pr`: when `gh pr view` fails it now shows gh''s own error (sign-in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 16b650cb5665e63bf43bbd87b6195bad6ef6f125ffa87db7a345855d2fd1b034
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-15-9f3cc0
  comparison: ''
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: 4 Account and Access changes'
  evidence:
  - quote: 'Improved `/autofix-pr`: when `gh pr view` fails it now shows gh''s own
      error (sign-in, SAML, rate limit) instead of a generic exit-code line'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: 'Improved the error when a cloud session can''t be created because your
      Claude login expired or was revoked: it now tells you to run `/login`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Improved the error shown when an MCP server's sign-in expires mid-session
      to say how to re-authenticate (`/mcp`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Changed sign-in with a Claude account to also request access to your claude.ai
      plugins
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-account-and-access-changes-in-v2-1-273
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v2.1.273
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-08-2-account-and-access-changes-in-v2-1-265|2 Account
  and Access changes in v2.1.265]]'
- '[[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account
  and Access changes in v2.1.268]]'
- '[[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed
  Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v2.1.273
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v2.1.273

**Claude Code** · 2026-09-15 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/autofix-pr`: when `gh pr view` fails it now shows gh's own error (sign-in, SAML, rate limit) instead of a generic exit-code line

> Improved the error when a cloud session can't be created because your Claude login expired or was revoked: it now tells you to run `/login`

> Improved the error shown when an MCP server's sign-in expires mid-session to say how to re-authenticate (`/mcp`)

> Changed sign-in with a Claude account to also request access to your claude.ai plugins

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Context Window
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved Claude apps gateway sign-in rate limit errors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-9f3cc0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-4-account-and-access-changes-in-v2-1-273.md%0ACard%20ID%3A%20claude-code-2026-09-15-9f3cc0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->