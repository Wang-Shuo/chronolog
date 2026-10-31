---
card_id: claude-code-2026-04-09-499a41
date: '2026-04-09'
description: 'Claude Code · 2026-04-09 · Safety and Privacy: 6 changes in v2.1.98
  — Added subprocess sandboxing with PID namespace isolation on Linux when…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5ce8826b95dde146cb37bc94cc519a3c7e564ec4d94ca02b3b7c1d28598db6d2
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-09-499a41
  comparison: ''
  date: '2026-04-09'
  description: 'Claude Code — v2.1.98: 6 Safety and Privacy changes'
  evidence:
  - quote: Added subprocess sandboxing with PID namespace isolation on Linux when
      `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env
      var to limit per-session script invocations
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Fixed a Bash tool permission bypass where a backslash-escaped flag could
      be auto-allowed as read-only and lead to arbitrary code execution
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Fixed compound Bash commands bypassing forced permission prompts for safety
      checks and explicit ask rules in auto and bypass-permissions modes
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Fixed `Bash(cmd:*)` and `Bash(git commit *)` wildcard permission rules
      failing to match commands with extra spaces or tabs
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Fixed permission rules with names matching JavaScript prototype properties
      (e.g. `toString`) causing `settings.json` to be silently ignored
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  - quote: Fixed agent team members not inheriting the leader's permission mode when
      using `--dangerously-skip-permissions`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-98
  source_release: claude-code-2026-04-09-v2-1-98-github-307232194-a0774436
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.98
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-04-linux-sandbox-now-ships-the-apply-seccomp-helper-in-both-npm-and-native-builds-r|Linux
  sandbox now ships the apply-seccomp helper in both npm and native builds…]]'
- '[[Changes/Claude Code/2026-04-07-vscode-added-a-warning-banner-when-settings-json-files-fail-to-parse-so-users-kn|VSCode
  Added a warning banner when settings.json files fail to parse, so users…]]'
- '[[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety
  and Privacy changes in v2.1.97]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|claude-code-2026-04-09-v2-1-98-github-307232194-a0774436]]'
source_type: github_releases
superseded: true
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.98
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.98

**Claude Code** · 2026-04-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.98) · from [[Releases/Claude Code/claude-code-2026-04-09-v2-1-98-github-307232194-a0774436|v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set, and `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations

> Fixed a Bash tool permission bypass where a backslash-escaped flag could be auto-allowed as read-only and lead to arbitrary code execution

> Fixed compound Bash commands bypassing forced permission prompts for safety checks and explicit ask rules in auto and bypass-permissions modes

> Fixed `Bash(cmd:*)` and `Bash(git commit *)` wildcard permission rules failing to match commands with extra spaces or tabs

> Fixed permission rules with names matching JavaScript prototype properties (e.g. `toString`) causing `settings.json` to be silently ignored

> Fixed agent team members not inheriting the leader's permission mode when using `--dangerously-skip-permissions`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.98
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-09-fixed-false-bash-permission-prompts-for-cut-d-paste-d-column-s-awk-print-1-file|Fixed false Bash permission prompts for cut -d /, paste -d /, column -s /…]] · Pricing Model
- [[Changes/Claude Code/2026-04-09-2-editor-experience-changes-in-v2-1-98|2 Editor Experience changes in v2.1.98]] · Editor Experience
- [[Changes/Claude Code/2026-04-09-fixed-a-memory-leak-where-remote-control-permission-handler-entries-were-retaine|Fixed a memory leak where Remote Control permission handler entries were retained…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-09-6-developer-workflow-changes-in-v2-1-98|6 Developer Workflow changes in v2.1.98]] · Developer Workflow
- [[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|Added interactive Google Vertex AI setup wizard accessible from the login screen…]] · Account and Access
- [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]] · Agent Mode
- [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]] · Context Window
- [[Changes/Claude Code/2026-04-09-3-other-changes-in-v2-1-98|3 other changes in v2.1.98]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-08 · Claude Code · [[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety and Privacy changes in v2.1.97]]
- Later: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-09-499a41&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-09-6-safety-and-privacy-changes-in-v2-1-98.md%0ACard%20ID%3A%20claude-code-2026-04-09-499a41%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.98%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->