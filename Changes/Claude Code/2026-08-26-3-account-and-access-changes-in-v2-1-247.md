---
card_id: claude-code-2026-08-26-c699bd
date: '2026-08-26'
description: 'Claude Code · 2026-08-26 · Account and Access: 3 changes in v2.1.247
  — Changed analytics to stay off from startup, not only after login, when managed
  settings…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1245
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ceaafd5211464c510c23d6178852ffa6d802697f65c688ff4ac4f475c73c44f7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-26-c699bd
  comparison: ''
  date: '2026-08-26'
  description: 'Claude Code — v2.1.247: 3 Account and Access changes'
  evidence:
  - quote: Changed analytics to stay off from startup, not only after login, when
      managed settings force gateway login or a custom OAuth deployment is configured
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Changed Claude apps gateway sign-in requests to identify Claude Code (a
      `surface=claude_code` device-authorization parameter and a `claude-code/<version>`
      User-Agent)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  - quote: Changed organization sign-in enforcement to exit at start when the administrator's
      managed settings cannot be read, even if host-supplied or per-user Windows registry
      settings exist
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-account-and-access-changes-in-v2-1-247
  source_release: claude-code-2026-08-26-v2-1-247-github-377320078-fc507178
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v2.1.247
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-17-2-account-and-access-changes-in-v2-1-234|2 Account
  and Access changes in v2.1.234]]'
- '[[Changes/ChatGPT/2026-08-25-chatgpt-work-s-browser-on-web-and-mobile-can-also-help-you-get-tasks-done-on-som-99be54|ChatGPT
  Work can now complete tasks on signed-in websites]]'
- '[[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved
  attribution of usage telemetry to your organization for workload identity…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|claude-code-2026-08-26-v2-1-247-github-377320078-fc507178]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v2.1.247
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v2.1.247

**Claude Code** · 2026-08-26 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) · from [[Releases/Claude Code/claude-code-2026-08-26-v2-1-247-github-377320078-fc507178|v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed analytics to stay off from startup, not only after login, when managed settings force gateway login or a custom OAuth deployment is configured

> Changed Claude apps gateway sign-in requests to identify Claude Code (a `surface=claude_code` device-authorization parameter and a `claude-code/<version>` User-Agent)

> Changed organization sign-in enforcement to exit at start when the administrator's managed settings cannot be read, even if host-supplied or per-user Windows registry settings exist

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]] · Model Support
- [[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed terminal hyperlinks in rendered markdown]] · Developer Workflow
- [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-26-changed-the-prompt-footer-pr-badge-to-skip-its-github-re-check-on-terminal-refoc|Changed the prompt-footer PR badge to skip its GitHub re-check on terminal refocus…]] · Interface Experience
- [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved attribution of usage telemetry to your organization for workload identity…]]
- Later: 2026-08-28 · Claude Code · [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-26-c699bd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-26-3-account-and-access-changes-in-v2-1-247.md%0ACard%20ID%3A%20claude-code-2026-08-26-c699bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.247%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->