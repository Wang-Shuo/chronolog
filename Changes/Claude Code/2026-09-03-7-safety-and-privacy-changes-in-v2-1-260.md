---
card_id: claude-code-2026-09-03-de9b1b
date: '2026-09-03'
description: 'Claude Code · 2026-09-03 · Safety and Privacy: 7 changes in v2.1.260
  — Fixed `Edit`/`Write`/`Read` permission rules whose path contains parentheses being…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2228
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fe26367a735037772b22f4b80d7da7f4766e83638e41ba82061681df032ad955
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-03-de9b1b
  comparison: ''
  date: '2026-09-03'
  description: 'Claude Code — v2.1.260: 7 Safety and Privacy changes'
  evidence:
  - quote: Fixed `Edit`/`Write`/`Read` permission rules whose path contains parentheses
      being dropped as invalid or ignored by the Bash sandbox, which left "read-only"
      folders writable
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Fixed one file permission rule with an uncompilable pattern (e.g. an unclosed
      `[`) making every file edit fail with `Invalid regular expression`; such a deny
      rule now guards the literal path it spells
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Fixed Bash permission checks auto-approving zsh commands that hide a command
      substitution in a REPORTTIME, REPORTMEMORY or DIRSTACKSIZE assignment; these
      now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: 'Glob/Grep: Fixed the search path being probed on disk before the permission
      check; a missing path is now reported after permission is decided, as Read does'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed permission rules with text after the closing parenthesis (e.g.
      `Bash(ls) x`), which never matched anything, to be reported as invalid settings
      instead of being silently ignored
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: Changed server-managed settings so a managed CLAUDE.md (`claudeMd`) no
      longer triggers the security approval dialog; hooks, shell-command, sandbox,
      and unsafe `env` settings still require approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  - quote: 'Changed commands typed at the `!` bash-mode prompt to run outside the
      sandbox even when strict sandbox mode (`sandbox.allowUnsandboxedCommands: false`)
      is on, like typing into your own terminal'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-safety-and-privacy-changes-in-v2-1-260
  source_release: claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v2.1.260
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety
  and Privacy changes in v2.1.259]]'
- '[[Changes/Google Antigravity/2026-09-02-permission-prompts-again-describe-the-specific-action-being-requested-instead-of|Permission
  prompts again describe the specific action being requested instead…]]'
- '[[Changes/Kimi Code/2026-09-02-2-safety-and-privacy-changes-in-kimi-code-0-40-0|2
  Safety and Privacy changes in Kimi Code 0.40.0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v2.1.260
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v2.1.260

**Claude Code** · 2026-09-03 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) · from [[Releases/Claude Code/claude-code-2026-09-03-v2-1-260-github-382367470-ac2ba1fc|v2.1.260]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `Edit`/`Write`/`Read` permission rules whose path contains parentheses being dropped as invalid or ignored by the Bash sandbox, which left "read-only" folders writable

> Fixed one file permission rule with an uncompilable pattern (e.g. an unclosed `[`) making every file edit fail with `Invalid regular expression`; such a deny rule now guards the literal path it spells

> Fixed Bash permission checks auto-approving zsh commands that hide a command substitution in a REPORTTIME, REPORTMEMORY or DIRSTACKSIZE assignment; these now prompt for approval

> Glob/Grep: Fixed the search path being probed on disk before the permission check; a missing path is now reported after permission is decided, as Read does

> Changed permission rules with text after the closing parenthesis (e.g. `Bash(ls) x`), which never matched anything, to be reported as invalid settings instead of being silently ignored

> Changed server-managed settings so a managed CLAUDE.md (`claudeMd`) no longer triggers the security approval dialog; hooks, shell-command, sandbox, and unsafe `env` settings still require approval

> Changed commands typed at the `!` bash-mode prompt to run outside the sandbox even when strict sandbox mode (`sandbox.allowUnsandboxedCommands: false`) is on, like typing into your own terminal

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-03-2-model-support-changes-in-v2-1-260|2 Model Support changes in v2.1.260]] · Model Support
- [[Changes/Claude Code/2026-09-03-improved-the-settings-error-for-rules-such-as-edit-c-dir-name-where-is-read-as-a|Improved the settings error for rules such as Edit(C:\dir\(name)\), where…]] · Editor Experience
- [[Changes/Claude Code/2026-09-03-improved-deleting-a-background-session-whose-worktree-has-unpushed-commits-the-m|Improved deleting a background session whose worktree has unpushed commits]] · Developer Workflow
- [[Changes/Claude Code/2026-09-03-4-interface-experience-changes-in-v2-1-260|4 Interface Experience changes in v2.1.260]] · Interface Experience
- [[Changes/Claude Code/2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260|3 Mobile and Desktop changes in v2.1.260]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode changes in v2.1.260]] · Agent Mode
- [[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context Window changes in v2.1.260]] · Context Window
- [[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4 Apps and Integrations changes in v2.1.260]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added /reload-plugins to headless sessions, so it appears in the Claude Code…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-03-3-other-changes-in-v2-1-260|3 other changes in v2.1.260]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-02 · Kimi Code · [[Changes/Kimi Code/2026-09-02-2-safety-and-privacy-changes-in-kimi-code-0-40-0|2 Safety and Privacy changes in Kimi Code 0.40.0]]
- Later: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-03-de9b1b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-03-7-safety-and-privacy-changes-in-v2-1-260.md%0ACard%20ID%3A%20claude-code-2026-09-03-de9b1b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.260%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->