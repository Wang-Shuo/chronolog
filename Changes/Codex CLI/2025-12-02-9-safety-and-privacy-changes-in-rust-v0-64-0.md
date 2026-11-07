---
card_id: codex-cli-2025-12-02-b2b77f
date: '2025-12-02'
description: 'Codex CLI · 2025-12-02 · Safety and Privacy: 9 changes in 0.64.0 — Safety
  defaults improve via consolidated world-writable scanning and workspace-write…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 961
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 37b602df8a9fa31d5277966cc1aec7680503b3a5b8f1ff3b82baed35972163ae
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-02-b2b77f
  comparison: ''
  date: '2025-12-02'
  description: 'Codex CLI — 0.64.0: 9 Safety and Privacy changes'
  evidence:
  - quote: Safety defaults improve via consolidated world-writable scanning and workspace-write
      enforcement of read-only .git directories. Sandbox assessment and approval flows
      align with trust policies.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: MCP and shell tooling add shell-tool MCP login support, explicit capability
      declaration, sandbox awareness, publication to npm, and MCP elicitations. The
      rmcp client is upgraded to 0.10.0 for modern notifications.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Sandbox assessment regression is fixed, policy-approved commands are honored,
      dangerous-command checks are tightened on Windows, and workspace-write enforces
      .git read-only.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Review rollout filtering is disabled so history shows, approval presets
      respect workspace-write, /approvals trust detection is corrected, and sandbox
      command assessment edge cases are fixed.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Windows sandbox treats <workspace_root>/.git as read-only, and risky browser
      launches are flagged before execution.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Security and CI add cargo-audit and cargo-deny. GitHub Actions are updated
      to checkout v6 and upload-artifact v5. macOS 13 builds are dropped. A flaky
      Ubuntu variant is skipped. The next_minor_version script now resets the patch
      number correctly.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'refactor: inline sandbox type lookup in process_exec_tool_call by @bolinfest
      in #7122'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'bypass sandbox for policy approved commands by @zhao-oai in #7110'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Windows Sandbox: treat <workspace_root>/.git as read-only in workspace-write
      mode by @iceweasel-oai in #7142'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-64-0
  source_release: codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.64.0
  type: change
related_changes:
- '[[Changes/Lovable/2025-11-26-improved-share-invite-experience|Improved share &
  invite experience]]'
- '[[Changes/Lovable/2025-11-26-private-projects-for-everyone|Private projects for
  everyone]]'
- '[[Changes/Cline/2025-11-27-maint-npm-audit-fix-for-glob-package-vulnerability-by-canvrno-in-https-github-co|maint:
  npm audit fix for glob package vulnerability]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.64.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.64.0

**Codex CLI** · 2025-12-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.64.0) · from [[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|0.64.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Safety defaults improve via consolidated world-writable scanning and workspace-write enforcement of read-only .git directories. Sandbox assessment and approval flows align with trust policies.

> MCP and shell tooling add shell-tool MCP login support, explicit capability declaration, sandbox awareness, publication to npm, and MCP elicitations. The rmcp client is upgraded to 0.10.0 for modern notifications.

> Sandbox assessment regression is fixed, policy-approved commands are honored, dangerous-command checks are tightened on Windows, and workspace-write enforces .git read-only.

> Review rollout filtering is disabled so history shows, approval presets respect workspace-write, /approvals trust detection is corrected, and sandbox command assessment edge cases are fixed.

> Windows sandbox treats \<workspace_root>/.git as read-only, and risky browser launches are flagged before execution.

> Security and CI add cargo-audit and cargo-deny. GitHub Actions are updated to checkout v6 and upload-artifact v5. macOS 13 builds are dropped. A flaky Ubuntu variant is skipped. The next_minor_version script now resets the patch number correctly.

> refactor: inline sandbox type lookup in process_exec_tool_call by @bolinfest in #7122

> bypass sandbox for policy approved commands by @zhao-oai in #7110

> Windows Sandbox: treat \<workspace_root>/.git as read-only in workspace-write mode by @iceweasel-oai in #7142

Source: https://github.com/openai/codex/releases/tag/rust-v0.64.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Model Support
- [[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context Window changes in rust-v0.64.0]] · Context Window
- [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]] · Account and Access
- [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Agent Mode
- [[Changes/Codex CLI/2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0|4 Developer Workflow changes in rust-v0.64.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-02-execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session|Execution gains an experimental “exp” model, unified exec pruning to limit session…]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-02-3-editor-experience-changes-in-rust-v0-64-0|3 Editor Experience changes in rust-v0.64.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]] · Interface Experience
- [[Changes/Codex CLI/2025-12-02-46-other-changes-in-rust-v0-64-0|46 other changes in rust-v0.64.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-11-27 · Cline · [[Changes/Cline/2025-11-27-maint-npm-audit-fix-for-glob-package-vulnerability-by-canvrno-in-https-github-co|maint: npm audit fix for glob package vulnerability]]
- Later: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-improve-code-coverage-for-cli-src-ui-privacy-package-by-megha1188-in-https-githu|Improve code coverage for cli/src/ui/privacy package]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-02-b2b77f&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0.md%0ACard%20ID%3A%20codex-cli-2025-12-02-b2b77f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.64.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->