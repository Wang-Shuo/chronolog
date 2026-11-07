---
card_id: github-copilot-cli-2026-09-16-744104
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Safety and Privacy: 17 changes in
  1.0.85 — Add /sandbox Network host allow/deny rules without replacing your configured…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2241
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 30a49d236ba9895ff1d2a4a8ead811b3e442ad67a73b5c9ee48f7ce8a65e7a53
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-744104
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 17 Safety and Privacy changes'
  evidence:
  - quote: Add /sandbox Network host allow/deny rules without replacing your configured
      upstream proxy
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Managed sandbox sessions can now be disabled for the rest of the session
      from an approved bypass prompt.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: copilot --help describes the --no-\* options again, and --no-auto-update
      says it runs the version bundled in the binary. --no-auto-login and --no-sandbox
      stay supported but remain hidden from help, as they were before the clap port
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Windows sandbox denials of loopback and local network access prompt to
      re-run the command outside the sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Approved sandbox retries are labeled sandbox relaxed while network policy
      stays enforced, or sandbox bypassed when fully unsandboxed; failed bypasses
      explain that host permissions still apply
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: An enterprise-managed sandbox policy delivered by MDM or a managed settings
      file no longer discards sandbox.allowBypass, so bypass prompts and /sandbox
      disable work as the policy intends
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: The managed sandbox startup notice no longer says sandboxing can't be turned
      off when your organization's policy allows a session opt-out; it names /sandbox
      disable instead
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: A failed command whose EPERM or EACCES diagnostic names a sandbox-blocked
      path now offers to run outside the sandbox, even when the command line never
      named that path
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: A write blocked by a read-only sandbox path, and a Node or Go network failure
      blocked by the sandbox, are now recognized as sandbox denials instead of surfacing
      as raw errors
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Show when sandboxing is only enabled for the current session in /sandbox
      status and settings.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: The `allowManagedHooksOnly` policy now also blocks extension-registered
      `preToolUse`, `postToolUse` and `postToolUseFailure` callbacks, which previously
      bypassed the managed-only lockdown that every other hook event already applied
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: A PowerShell write the sandbox blocks offers to run the command outside
      the sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: /sandbox disable turns the sandbox off for the current session when your
      organization's policy allows bypass
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Show /sandbox filesystem paths as absolute paths; typing ~/path still expands
      to your home directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Move the /sandbox Filesystem paths into their own list, opened from a Paths
      row
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Improve /sandbox guidance and show /sandbox policy in command help
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: On supported Windows sandbox policies, interactive shell commands now record
      blocked accesses. One approved escalation retries with file and process restrictions
      recording instead of blocking while network policy remains active, then falls
      back to the disclosed full bypass only if still blocked
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 17-safety-and-privacy-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in v1.0.85
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-09-14-add-the-kimi-code-permission-mode-reminder-environment-variable-set-it-to-0-to-s|Add
  the KIMI_CODE_PERMISSION_MODE_REMINDER environment variable]]'
- '[[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety
  and Privacy changes in v2.1.273]]'
- '[[Changes/Gemini CLI/2026-09-15-2-safety-and-privacy-changes-in-v0-60-0|2 Safety
  and Privacy changes in v0.60.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add /sandbox Network host allow/deny rules without replacing your configured upstream proxy

> Managed sandbox sessions can now be disabled for the rest of the session from an approved bypass prompt.

> copilot --help describes the --no-\* options again, and --no-auto-update says it runs the version bundled in the binary. --no-auto-login and --no-sandbox stay supported but remain hidden from help, as they were before the clap port

> Windows sandbox denials of loopback and local network access prompt to re-run the command outside the sandbox

> Approved sandbox retries are labeled sandbox relaxed while network policy stays enforced, or sandbox bypassed when fully unsandboxed; failed bypasses explain that host permissions still apply

> An enterprise-managed sandbox policy delivered by MDM or a managed settings file no longer discards sandbox.allowBypass, so bypass prompts and /sandbox disable work as the policy intends

> The managed sandbox startup notice no longer says sandboxing can't be turned off when your organization's policy allows a session opt-out; it names /sandbox disable instead

> A failed command whose EPERM or EACCES diagnostic names a sandbox-blocked path now offers to run outside the sandbox, even when the command line never named that path

> A write blocked by a read-only sandbox path, and a Node or Go network failure blocked by the sandbox, are now recognized as sandbox denials instead of surfacing as raw errors

> Show when sandboxing is only enabled for the current session in /sandbox status and settings.

> The `allowManagedHooksOnly` policy now also blocks extension-registered `preToolUse`, `postToolUse` and `postToolUseFailure` callbacks, which previously bypassed the managed-only lockdown that every other hook event already applied

> A PowerShell write the sandbox blocks offers to run the command outside the sandbox

> /sandbox disable turns the sandbox off for the current session when your organization's policy allows bypass

> Show /sandbox filesystem paths as absolute paths; typing ~/path still expands to your home directory

> Move the /sandbox Filesystem paths into their own list, opened from a Paths row

> Improve /sandbox guidance and show /sandbox policy in command help

> On supported Windows sandbox policies, interactive shell commands now record blocked accesses. One approved escalation retries with file and process restrictions recording instead of blocking while network policy remains active, then falls back to the disclosed full bypass only if still blocked

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed up startup when resuming an existing local session by its exact UUID with --resume]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-15 · Gemini CLI · [[Changes/Gemini CLI/2026-09-15-2-safety-and-privacy-changes-in-v0-60-0|2 Safety and Privacy changes in v0.60.0]]
- Later: 2026-09-16 · OpenHands · [[Changes/OpenHands/2026-09-16-test-cover-telemetry-consent-banner-by-aivong-openhands-in-https-github-com-open|test: cover telemetry consent banner]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-744104&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-17-safety-and-privacy-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-744104%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->