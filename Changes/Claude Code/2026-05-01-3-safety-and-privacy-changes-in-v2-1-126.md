---
card_id: claude-code-2026-05-01-34f11e
date: '2026-05-01'
description: 'Claude Code · 2026-05-01 · Safety and Privacy: 3 changes in v2.1.126
  — `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`,
  `.git/`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1111
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0be1717d9671a98408889f97eca65254a967dcd13dd902342eea213e7e6d5fb3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-01-34f11e
  comparison: ''
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: 3 Safety and Privacy changes'
  evidence:
  - quote: '`--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`,
      `.git/`, `.vscode/`, shell config files, and other previously-protected paths
      (catastrophic removal commands still prompt as a safety net)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  - quote: 'Auto mode: the spinner now turns red when a permission check stalls, instead
      of looking like the tool is running'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  - quote: '**Security:** Fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly`
      being ignored when a higher-priority managed-settings source lacked a `sandbox`
      block'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-126
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.126
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor
  Security Review is now in beta on Teams and Enterprise plans]]'
- '[[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|Security
  Reviewer]]'
- '[[Changes/Cursor/2026-04-30-vulnerability-scanner-b19b70|Vulnerability Scanner]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.126
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.126

**Claude Code** · 2026-05-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) · from [[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)

> Auto mode: the spinner now turns red when a permission check stalls, instead of looking like the tool is running

> **Security:** Fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` being ignored when a higher-priority managed-settings source lacked a `sandbox` block

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-01-2-model-support-changes-in-v2-1-126|2 Model Support changes in v2.1.126]] · Model Support
- [[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated OpenTelemetry event now fires for user-typed slash…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-05-01-3-developer-workflow-changes-in-v2-1-126|3 Developer Workflow changes in v2.1.126]] · Developer Workflow
- [[Changes/Claude Code/2026-05-01-added-claude-project-purge-path-to-delete-all-claude-code-state-for-a-project-tr|- Added claude project purge path to delete all Claude Code state for a project…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-01-powershell-tool-bare-e-g-git-diff-file-is-no-longer-mis-flagged-as-the-stop-pars|PowerShell tool: bare -- (e.g. git diff -- file) is no longer mis-flagged…]] · Editor Experience
- [[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude auth login now accepts the OAuth code pasted into the terminal…]] · Account and Access
- [[Changes/Claude Code/2026-05-01-2-other-changes-in-v2-1-126|2 other changes in v2.1.126]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-30 · Cursor · [[Changes/Cursor/2026-04-30-vulnerability-scanner-b19b70|Vulnerability Scanner]]
- Later: 2026-05-01 · Cursor · [[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|Default Off: users can discover and opt in]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-01-34f11e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-01-3-safety-and-privacy-changes-in-v2-1-126.md%0ACard%20ID%3A%20claude-code-2026-05-01-34f11e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.126%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->