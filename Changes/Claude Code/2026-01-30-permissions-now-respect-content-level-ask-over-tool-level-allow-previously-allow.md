---
card_id: claude-code-2026-01-30-3cd8a3
date: '2026-01-30'
description: 'Claude Code · 2026-01-30 · Safety and Privacy: Permissions now respect
  content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2012
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 01c95d2f0c966175fb5adcd87d2e224754cc137727f90f892afc5ab2be1bebfa
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-01-30-3cd8a3
  comparison: ''
  date: '2026-01-30'
  description: 'Claude Code — v2.1.27: Permissions now respect content-level `ask`
    over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed
    all bash commands, but will now permission prompt for `rm`.'
  evidence:
  - quote: 'Permissions now respect content-level `ask` over tool-level `allow`. Previously
      `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now
      permission prompt for `rm`.'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.27
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow
  source_release: claude-code-2026-01-30-v2-1-27-github-281663155-d003937d
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Permissions now respect content-level `ask` over tool-level `allow`
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-01-28-3-safety-and-privacy-changes-in-v0-26-0|3 Safety
  and Privacy changes in v0.26.0]]'
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|Fixed
  per-user temp directory isolation to prevent permission conflicts on shared systems]]'
- '[[Changes/OpenCode/2026-01-29-core-allow-media-src-data-url-for-small-audio-files-in-content-security-policy|Core
  Allow media-src data: URL for small audio files in Content Security Policy]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-30-v2-1-27-github-281663155-d003937d|claude-code-2026-01-30-v2-1-27-github-281663155-d003937d]]'
source_type: github_releases
theme: safety-privacy
title: Permissions now respect content-level ask over tool-level allow
type: change
---

<!-- chronolog:begin region="header" -->
# Permissions now respect content-level `ask` over tool-level `allow`

**Claude Code** · 2026-01-30 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.27) · from [[Releases/Claude Code/claude-code-2026-01-30-v2-1-27-github-281663155-d003937d|v2.1.27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-01-30-2-developer-workflow-changes-in-v2-1-27|2 Developer Workflow changes in v2.1.27]] · Developer Workflow
- [[Changes/Claude Code/2026-01-30-added-from-pr-flag-to-resume-sessions-linked-to-a-specific-github-pr-number-or-u|Added --from-pr flag to resume sessions linked to a specific GitHub PR number or URL]] · Projects and Workspaces
- [[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|VSCode: Enabled Claude in Chrome integration]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-29 · OpenCode · [[Changes/OpenCode/2026-01-29-core-allow-media-src-data-url-for-small-audio-files-in-content-security-policy|Core Allow media-src data: URL for small audio files in Content Security Policy]]
- Later: 2026-01-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP server support permission flags: --yolo, --allow-all, etc. and permissions config]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-01-30-3cd8a3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow.md%0ACard%20ID%3A%20claude-code-2026-01-30-3cd8a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->