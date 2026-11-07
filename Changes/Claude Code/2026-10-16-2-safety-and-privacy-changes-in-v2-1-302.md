---
card_id: claude-code-2026-10-16-4cc9fe
date: '2026-10-16'
description: 'Claude Code · 2026-10-16 · Safety and Privacy: 2 changes in v2.1.302
  — Fixed `/design consent` and `/design revoke` suggesting `/design-login` when they
  fail…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2271
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8fdbcc51a50ca673a129b52f2bb97f699f37e360072fe6eb546e18138a939cf
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-16-4cc9fe
  comparison: ''
  date: '2026-10-16'
  description: 'Claude Code — v2.1.302: 2 Safety and Privacy changes'
  evidence:
  - quote: Fixed `/design consent` and `/design revoke` suggesting `/design-login`
      when they fail in a cloud session, where it isn't available; the message now
      points to claude.ai/design/settings
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  - quote: Changed `claude -p` and Agent SDK sessions with no permission mode to start
      in `default` mode on third-party providers, with telemetry off or on a fresh
      install; `--permission-mode auto` keeps auto
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-302
  source_release: claude-code-2026-10-16-v2-1-302-github-415177347-763faf43
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.302
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety
  and Privacy changes in v2.1.301]]'
- '[[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18
  Safety and Privacy changes in rust-v0.163.0]]'
- '[[Changes/Google Antigravity/2026-10-15-the-review-permissions-dialog-now-wraps-long-commands-and-paths-so-you-can-read|The
  Review permissions dialog now wraps long commands and paths, so you can read…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-16-v2-1-302-github-415177347-763faf43|claude-code-2026-10-16-v2-1-302-github-415177347-763faf43]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.302
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.302

**Claude Code** · 2026-10-16 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.302) · from [[Releases/Claude Code/claude-code-2026-10-16-v2-1-302-github-415177347-763faf43|v2.1.302]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `/design consent` and `/design revoke` suggesting `/design-login` when they fail in a cloud session, where it isn't available; the message now points to claude.ai/design/settings

> Changed `claude -p` and Agent SDK sessions with no permission mode to start in `default` mode on third-party providers, with telemetry off or on a fresh install; `--permission-mode auto` keeps auto

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.302
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-16-6-agent-mode-changes-in-v2-1-302|6 Agent Mode changes in v2.1.302]] · Agent Mode
- [[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved the message when a background session reopened from another folder has no…]] · Model Support
- [[Changes/Claude Code/2026-10-16-2-context-window-changes-in-v2-1-302|2 Context Window changes in v2.1.302]] · Context Window
- [[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3 Apps and Integrations changes in v2.1.302]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-16-added-a-notice-to-design-sync-and-design-login-that-standalone-claude-design-cla|Added a notice to /design-sync and /design-login that standalone Claude Design…]] · Account and Access
- [[Changes/Claude Code/2026-10-16-6-other-changes-in-v2-1-302|6 other changes in v2.1.302]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-15 · Google Antigravity · [[Changes/Google Antigravity/2026-10-15-the-review-permissions-dialog-now-wraps-long-commands-and-paths-so-you-can-read|The Review permissions dialog now wraps long commands and paths, so you can read…]]
- Later: 2026-10-16 · Cline · [[Changes/Cline/2026-10-16-cline-cloud-sessions-rolling-out-gradually-run-a-task-in-a-hosted-sandbox-on-a-g|Cline Cloud sessions, rolling out gradually]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-16-4cc9fe&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-16-2-safety-and-privacy-changes-in-v2-1-302.md%0ACard%20ID%3A%20claude-code-2026-10-16-4cc9fe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.302%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->