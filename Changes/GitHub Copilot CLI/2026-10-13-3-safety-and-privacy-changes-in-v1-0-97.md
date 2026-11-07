---
card_id: github-copilot-cli-2026-10-13-66aff7
date: '2026-10-13'
description: 'GitHub Copilot CLI · 2026-10-13 · Safety and Privacy: 3 changes in 1.0.97
  — Autopilot denies a preToolUse hook''s "ask" decision instead of stopping on a…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ed3e6d17479ac54d3a75d3147e9e285987b835ae06394ffea2f442c46faa4161
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-13-66aff7
  comparison: ''
  date: '2026-10-13'
  description: 'GitHub Copilot CLI — 1.0.97: 3 Safety and Privacy changes'
  evidence:
  - quote: Autopilot denies a preToolUse hook's "ask" decision instead of stopping
      on a permission dialog nobody is watching
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: In /config, managed permission rules are read-only and hidden unless set
      by your organization.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  - quote: Unavailable permission recovery attempts are now tracked per request, so
      unrelated calls no longer consume each other's retry budget.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-safety-and-privacy-changes-in-v1-0-97
  source_release: github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v1.0.97
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin
  approval waits]]'
- '[[Changes/OpenHands/2026-10-12-fix-telemetry-retry-automation-consent-sync-by-enyst-in-https-github-com-openhan|fix(telemetry):
  retry automation consent sync]]'
- '[[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security-99509e|Origin
  now integrates with over 20 apps for deployments, CI, code review, security…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v1.0.97
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v1.0.97

**GitHub Copilot CLI** · 2026-10-13 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.97) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|1.0.97]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Autopilot denies a preToolUse hook's "ask" decision instead of stopping on a permission dialog nobody is watching

> In /config, managed permission rules are read-only and hidden unless set by your organization.

> Unavailable permission recovery attempts are now tracked per request, so unrelated calls no longer consume each other's retry budget.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.97
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-13-background-shell-wait-status-no-longer-animates-when-no-foreground-work-is-runni|Background-shell wait status no longer animates when no foreground work is running]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-13-show-billed-ai-credits-in-usage-for-token-billed-sessions-including-after-resume|Show billed AI Credits in /usage for token-billed sessions, including after resume]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-10-13-emergency-memory-relief-in-long-sessions-can-now-bypass-its-cooldown-before-v8-a|Emergency memory relief in long sessions can now bypass its cooldown before V8…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-10-13-synchronous-task-json-output-now-includes-failed-child-error-and-lifecycle-event|Synchronous /task JSON output now includes failed child error and lifecycle events…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent Mode changes in v1.0.97]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-10-13-4-apps-and-integrations-changes-in-v1-0-97|4 Apps and Integrations changes in v1.0.97]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-13-power-bi-and-bluebird-mcp-servers-accept-their-published-resource-scopes-during|Power BI and Bluebird MCP servers accept their published resource scopes during sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-10-13-8-other-changes-in-v1-0-97|8 other changes in v1.0.97]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-13 · Cursor · [[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security-99509e|Origin now integrates with over 20 apps for deployments, CI, code review, security…]]
- Later: 2026-10-13 · HeyGen · [[Changes/HeyGen/2026-10-13-admin-billing-and-security|Admin, billing and security]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-13-66aff7&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-13-3-safety-and-privacy-changes-in-v1-0-97.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-13-66aff7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.97%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->