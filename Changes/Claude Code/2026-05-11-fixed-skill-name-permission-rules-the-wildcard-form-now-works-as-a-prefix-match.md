---
card_id: claude-code-2026-05-11-034be7
date: '2026-05-11'
description: 'Claude Code · 2026-05-11 · Safety and Privacy: Fixed `Skill(name *)`
  permission rules — the wildcard form now works as a prefix match, matching `Bash(ls
  *)`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1121
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: e2ec766845ffcf261c8e58e9beb693a841db58b9e87bfb1de6daeb1c0f966f69
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-11-034be7
  comparison: ''
  date: '2026-05-11'
  description: 'Claude Code — v2.1.139: Fixed `Skill(name *)` permission rules — the
    wildcard form now works as a prefix match, matching `Bash(ls *)` behavior'
  evidence:
  - quote: Fixed `Skill(name *)` permission rules — the wildcard form now works as
      a prefix match, matching `Bash(ls *)` behavior
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  extractor_version: fallback-v5
  impact: incremental
  kind: fix
  product: claude-code
  product_name: Claude Code
  slug: fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match
  source_release: claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed `Skill(name *)` permission rules
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|Trusted
  contact in ChatGPT]]'
- '[[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added
  sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]]'
- '[[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety
  and Privacy changes in v2.1.136]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d]]'
source_type: github_releases
theme: safety-privacy
title: Fixed Skill(name ) permission rules
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed `Skill(name *)` permission rules

**Claude Code** · 2026-05-11 · [[Themes/safety-privacy|Safety and Privacy]] · Fix · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) · from [[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|v2.1.139]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed `Skill(name *)` permission rules — the wildcard form now works as a prefix match, matching `Bash(ls *)` behavior
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-11-added-hook-args-string-field-exec-form-that-spawns-the-command-directly-without|Added hook args: string field (exec form) that spawns the command directly…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]] · Context Window
- [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-11-8-apps-and-integrations-changes-in-v2-1-139|8 Apps and Integrations changes in v2.1.139]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-11-compaction-prompt-now-asks-the-model-to-preserve-sensitive-user-instructions|Compaction prompt now asks the model to preserve sensitive user instructions]] · Model Support
- [[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]] · Editor Experience
- [[Changes/Claude Code/2026-05-11-added-scroll-speed-command-to-tune-mouse-wheel-scroll-speed-with-a-live-preview|Added /scroll-speed command to tune mouse wheel scroll speed with a live preview]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode changes in v2.1.139]] · Agent Mode
- [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-08 · Claude Code · [[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety and Privacy changes in v2.1.136]]
- Later: 2026-05-13 · Claude Code · [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-11-034be7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match.md%0ACard%20ID%3A%20claude-code-2026-05-11-034be7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.139%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->