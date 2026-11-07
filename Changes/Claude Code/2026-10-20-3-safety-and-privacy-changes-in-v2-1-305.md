---
card_id: claude-code-2026-10-20-7e4f88
date: '2026-10-20'
description: 'Claude Code · 2026-10-20 · Safety and Privacy: 3 changes in v2.1.305
  — Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create
  user…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2275
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d9187ec9f51a2303f8d8643a481c0be82ed0c622c9ef4d2e04e50d89a081e72c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-20-7e4f88
  comparison: ''
  date: '2026-10-20'
  description: 'Claude Code — v2.1.305: 3 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux
      can create user namespaces (Chromium, rootless podman); this lets them get around
      the sandbox's file protections
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: 'Fixed startup warnings printing as raw text above the logo: they now go
      to the debug log, and permission rules that restrict nothing show as warning
      rows under the banner'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: Improved MCP consent dialogs so an Enter meant for the prompt is less likely
      to be taken as Accept
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-305
  source_release: claude-code-2026-10-20-v2-1-305-github-418781864-90995baa
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.305
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added
  decider: "person" to a mod''s tool.check answer: only the permission dialog…]]'
- '[[Changes/GitHub Copilot CLI/2026-10-19-6-safety-and-privacy-changes-in-v1-0-100|6
  Safety and Privacy changes in v1.0.100]]'
- '[[Changes/OpenHands/2026-10-19-fix-theme-make-consent-backend-scope-readable-by-enyst-in-https-github-com-openh|fix(theme):
  make consent backend scope readable]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|claude-code-2026-10-20-v2-1-305-github-418781864-90995baa]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.305
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.305

**Claude Code** · 2026-10-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.305) · from [[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|v2.1.305]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create user namespaces (Chromium, rootless podman); this lets them get around the sandbox's file protections

> Fixed startup warnings printing as raw text above the logo: they now go to the debug log, and permission rules that restrict nothing show as warning rows under the banner

> Improved MCP consent dialogs so an Enter meant for the prompt is less likely to be taken as Accept

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-20-2-developer-workflow-changes-in-v2-1-305|2 Developer Workflow changes in v2.1.305]] · Developer Workflow
- [[Changes/Claude Code/2026-10-20-vscode-changed-the-message-shown-when-a-session-does-not-start-in-time-and-no-ho|VSCode Changed the message shown when a session does not start in time and no hook…]] · Account and Access
- [[Changes/Claude Code/2026-10-20-4-apps-and-integrations-changes-in-v2-1-305|4 Apps and Integrations changes in v2.1.305]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-20-claude-tag-added-public-slack-channels-claude-hasn-t-joined-to-the-claude-tag-ad|Claude Tag Added public Slack channels Claude hasn't joined to the Claude Tag…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-20-improved-a-mod-s-image-to-draw-its-picture-in-iterm2-3-5-and-later-with-fullscre|Improved a mod's Image to draw its picture in iTerm2 3.5 and later with fullscreen…]] · Interface Experience
- [[Changes/Claude Code/2026-10-20-vscode-added-a-running-start-up-hooks-spinner-status-with-a-screen-reader-announ|VSCode Added a "Running start-up hooks" spinner status, with a screen reader…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-20-4-other-changes-in-v2-1-305|4 other changes in v2.1.305]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-19 · OpenHands · [[Changes/OpenHands/2026-10-19-fix-theme-make-consent-backend-scope-readable-by-enyst-in-https-github-com-openh|fix(theme): make consent backend scope readable]]
- Later: 2026-10-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-20-permission-approval-prompts-explain-escalation-causes-and-show-a-request-specifi|Permission approval prompts explain escalation causes and show a request-specific…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-20-7e4f88&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-20-3-safety-and-privacy-changes-in-v2-1-305.md%0ACard%20ID%3A%20claude-code-2026-10-20-7e4f88%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.305%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->