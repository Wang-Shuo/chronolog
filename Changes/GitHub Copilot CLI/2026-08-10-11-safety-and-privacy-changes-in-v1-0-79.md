---
card_id: github-copilot-cli-2026-08-10-8c9eb6
date: '2026-08-10'
description: 'GitHub Copilot CLI · 2026-08-10 · Safety and Privacy: 11 changes in
  1.0.79 — The /sandbox configuration dialog shows where sandbox settings are stored
  in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2204
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5ae89f74bdb9f7a640549b9e904bf932abc1e8f102e738b0c06a50acad64a098
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-10-8c9eb6
  comparison: ''
  date: '2026-08-10'
  description: 'GitHub Copilot CLI — 1.0.79: 11 Safety and Privacy changes'
  evidence:
  - quote: The /sandbox configuration dialog shows where sandbox settings are stored
      in settings.json
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Allow enterprise-managed sandbox policy to enforce a proxy URL while credentials
      remain user-controlled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: A tool directory inside your workspace that is on PATH (.venv/bin, node_modules/.bin,
      an in-repo GOPATH) no longer turns that part of the workspace read-only in the
      sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: 'The /sandbox configuration dialog groups the git, gh, and (on macOS) keychain
      settings under a new Auth tab, and the settings keys moved from `sandbox.gitAuth`/`sandbox.ghAuth`
      to `sandbox.auth.git`/`sandbox.auth.gh`. There is no migration: the old keys
      are ignored in settings files, and SDK requests that still send them are rejected
      as invalid rather than ignored'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: On macOS, a sandbox read-only path nested inside a writable one now stays
      read-only instead of inheriting the write permission from the wider path
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: A sandbox that cannot start an MCP server now fails in seconds instead
      of stalling the session, and sandbox startup failures for both MCP and language
      servers now say the sandbox was at fault and how to fix or opt out of it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Disabling an extension no longer breaks elicitation, canvases, or tool
      permission prompts for other extensions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: On Linux, searches and most shell commands blocked by the sandbox now offer
      to re-run outside it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: 'BREAKING: the sandbox setting `allowDevToolCaches` is renamed `allowDevToolAccess`,
      since it grants dev-tool config and registries too, not just caches. The old
      key is no longer read and is ignored silently, so an existing `false` opt-out
      reverts to the default (on). Rename it in settings.json and in any managed/MDM
      policy.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Add /sandbox policy to show effective sandbox paths, denials, and network
      access
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: /sandbox tags inactive settings as (disabled) and explains why they are
      locked, and documents dev tool caches in copilot help sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 11-safety-and-privacy-changes-in-v1-0-79
  source_release: github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in v1.0.79
  type: change
related_changes:
- '[[Changes/Replit/2026-08-07-security-scan-while-you-build|Security scan while you
  build]]'
- '[[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety
  and Privacy changes in v2.1.225]]'
- '[[Changes/Cline/2026-08-09-never-run-a-foreign-compiled-plugin-sandbox-bootstrap-for-a-source-host|Never
  run a foreign compiled plugin-sandbox bootstrap for a source host]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in v1.0.79
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in v1.0.79

**GitHub Copilot CLI** · 2026-08-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.79) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|1.0.79]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The /sandbox configuration dialog shows where sandbox settings are stored in settings.json

> Allow enterprise-managed sandbox policy to enforce a proxy URL while credentials remain user-controlled

> A tool directory inside your workspace that is on PATH (.venv/bin, node_modules/.bin, an in-repo GOPATH) no longer turns that part of the workspace read-only in the sandbox

> The /sandbox configuration dialog groups the git, gh, and (on macOS) keychain settings under a new Auth tab, and the settings keys moved from `sandbox.gitAuth`/`sandbox.ghAuth` to `sandbox.auth.git`/`sandbox.auth.gh`. There is no migration: the old keys are ignored in settings files, and SDK requests that still send them are rejected as invalid rather than ignored

> On macOS, a sandbox read-only path nested inside a writable one now stays read-only instead of inheriting the write permission from the wider path

> A sandbox that cannot start an MCP server now fails in seconds instead of stalling the session, and sandbox startup failures for both MCP and language servers now say the sandbox was at fault and how to fix or opt out of it

> Disabling an extension no longer breaks elicitation, canvases, or tool permission prompts for other extensions

> On Linux, searches and most shell commands blocked by the sandbox now offer to re-run outside it

> BREAKING: the sandbox setting `allowDevToolCaches` is renamed `allowDevToolAccess`, since it grants dev-tool config and registries too, not just caches. The old key is no longer read and is ignored silently, so an existing `false` opt-out reverts to the default (on). Rename it in settings.json and in any managed/MDM policy.

> Add /sandbox policy to show effective sandbox paths, denials, and network access

> /sandbox tags inactive settings as (disabled) and explains why they are locked, and documents dev tool caches in copilot help sandbox

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.79
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-10-a-failed-session-history-load-no-longer-leaves-the-timeline-permanently-empty-th|A failed session-history load no longer leaves the timeline permanently empty]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-08-10-2-interface-experience-changes-in-v1-0-79|2 Interface Experience changes in v1.0.79]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-improve-teleported-subagent-tasks-navigation-with-nested-tree-browsing-current-a|Improve teleported subagent /tasks navigation with nested tree browsing, current/all…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-08-10-2-editor-experience-changes-in-v1-0-79|2 Editor Experience changes in v1.0.79]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-2-mobile-and-desktop-changes-in-v1-0-79|2 Mobile and Desktop changes in v1.0.79]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-10-3-apps-and-integrations-changes-in-v1-0-79|3 Apps and Integrations changes in v1.0.79]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-10-compute-context-attribution-against-the-auto-resolved-model-so-token-totals-are|Compute /context attribution against the Auto-resolved model so token totals…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-10-3-model-support-changes-in-v1-0-79|3 Model Support changes in v1.0.79]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-10-login-links-are-clickable-during-web-and-device-code-sign-in|Login links are clickable during web and device-code sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-10-4-developer-workflow-changes-in-v1-0-79|4 Developer Workflow changes in v1.0.79]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-10-2-enterprise-and-administration-changes-in-v1-0-79|2 Enterprise and Administration changes in v1.0.79]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-10-11-other-changes-in-v1-0-79|11 other changes in v1.0.79]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-09 · Cline · [[Changes/Cline/2026-08-09-never-run-a-foreign-compiled-plugin-sandbox-bootstrap-for-a-source-host|Never run a foreign compiled plugin-sandbox bootstrap for a source host]]
- Later: 2026-08-10 · Lovable · [[Changes/Lovable/2026-08-10-security-scan-setting-removed-from-workspace-settings|Security scan setting removed from workspace settings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-10-8c9eb6&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-10-11-safety-and-privacy-changes-in-v1-0-79.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-10-8c9eb6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.79%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->