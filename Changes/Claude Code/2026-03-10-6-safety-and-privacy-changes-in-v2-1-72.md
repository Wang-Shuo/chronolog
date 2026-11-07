---
card_id: claude-code-2026-03-10-8bc3c1
date: '2026-03-10'
description: 'Claude Code · 2026-03-10 · Safety and Privacy: 6 changes in v2.1.72
  — Added `lsof`, `pgrep`, `tput`, `ss`, `fd`, and `fdfind` to the bash auto-approval…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1059
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ea1c121c9fb6dc12fda9df7714b833148b8ebee266f405e989a0819f21694d21
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-10-8bc3c1
  comparison: ''
  date: '2026-03-10'
  description: 'Claude Code — v2.1.72: 6 Safety and Privacy changes'
  evidence:
  - quote: Added `lsof`, `pgrep`, `tput`, `ss`, `fd`, and `fdfind` to the bash auto-approval
      allowlist, reducing permission prompts for common read-only operations
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: Reduced false-positive bash permission prompts — tree-sitter parsing now
      handles `find -exec`, variable assignments, command substitutions, and many
      other patterns that previously triggered unnecessary prompts. Also fixed tree-sitter
      not loading in npm-installed versions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: Fixed digit keys selecting menu options instead of typing in plan mode
      permission prompt's text input
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: 'Fixed sandbox permission issues: certain file write operations incorrectly
      allowed without prompting, and output redirections to allowlisted directories
      (like `/tmp/claude/`) prompting unnecessarily'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: Fixed "Always Allow" saving permission rules that never match again
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  - quote: 'Fixed several permission rule matching issues: wildcard rules not matching
      commands with heredocs, embedded newlines, or no arguments; `sandbox.excludedCommands`
      failing with env var prefixes; "always allow" suggesting overly broad prefixes
      for nested CLI tools; and deny rules not applying to all command forms'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-72
  source_release: claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.72
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|\U0001F5A5️
  Open Terminal permission fix. Open Terminal is now visible without requiring…]]"
- '[[Changes/ElevenLabs/2026-03-09-packages|Packages]]'
- '[[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools
  now fully undoes /allow-all and re-triggers the autopilot…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48|claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.72
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.72

**Claude Code** · 2026-03-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.72) · from [[Releases/Claude Code/claude-code-2026-03-10-v2-1-72-github-294951528-18ee0f48|v2.1.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `lsof`, `pgrep`, `tput`, `ss`, `fd`, and `fdfind` to the bash auto-approval allowlist, reducing permission prompts for common read-only operations

> Reduced false-positive bash permission prompts — tree-sitter parsing now handles `find -exec`, variable assignments, command substitutions, and many other patterns that previously triggered unnecessary prompts. Also fixed tree-sitter not loading in npm-installed versions

> Fixed digit keys selecting menu options instead of typing in plan mode permission prompt's text input

> Fixed sandbox permission issues: certain file write operations incorrectly allowed without prompting, and output redirections to allowlisted directories (like `/tmp/claude/`) prompting unnecessarily

> Fixed "Always Allow" saving permission rules that never match again

> Fixed several permission rule matching issues: wildcard rules not matching commands with heredocs, embedded newlines, or no arguments; `sandbox.excludedCommands` failing with env var prefixes; "always allow" suggesting overly broad prefixes for nested CLI tools; and deny rules not applying to all command forms

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-10-improved-bash-command-parsing-by-switching-to-a-native-module-faster-initializat|Improved bash command parsing by switching to a native module]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes in v2.1.72]] · Agent Mode
- [[Changes/Claude Code/2026-03-10-3-developer-workflow-changes-in-v2-1-72|3 Developer Workflow changes in v2.1.72]] · Developer Workflow
- [[Changes/Claude Code/2026-03-10-added-claude-code-disable-cron-environment-variable-to-immediately-stop-schedule|Added CLAUDE_CODE_DISABLE_CRON environment variable to immediately stop scheduled…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-10-added-w-key-in-copy-to-write-the-focused-selection-directly-to-a-file-bypassing|Added w key in /copy to write the focused selection directly to a file…]] · Interface Experience
- [[Changes/Claude Code/2026-03-10-improved-voice-input-transcription-accuracy-for-repo-names-and-common-dev-terms|Improved voice input transcription accuracy for repo names and common dev terms…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-10-vscode-added-vscode-anthropic-claude-code-open-uri-handler-to-open-a-new-claude|VSCode: Added vscode://anthropic.claude-code/open URI handler to open a new Claude…]] · Editor Experience
- [[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps and Integrations changes in v2.1.72]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-10-7-other-changes-in-v2-1-72|7 other changes in v2.1.72]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools now fully undoes /allow-all and re-triggers the autopilot…]]
- Later: 2026-03-10 · Codex CLI · [[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10 Safety and Privacy changes in rust-v0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-10-8bc3c1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-10-6-safety-and-privacy-changes-in-v2-1-72.md%0ACard%20ID%3A%20claude-code-2026-03-10-8bc3c1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->