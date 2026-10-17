---
card_id: claude-code-2026-08-17-7da5bd
date: '2026-08-17'
description: 'Claude Code · 2026-08-17 · Safety and Privacy: 8 changes in v2.1.234
  — Security: remote file reads, session restore, CLAUDE.md includes, workflow scripts
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d7c8cd97b03ddd51d470d0292a27f14d8abc43bcc6e713d28c1aa2cc8402ca0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-17-7da5bd
  comparison: ''
  date: '2026-08-17'
  description: 'Claude Code — v2.1.234: 8 Safety and Privacy changes'
  evidence:
  - quote: 'Security: remote file reads, session restore, CLAUDE.md includes, workflow
      scripts and file uploads now reject Windows NT-namespace (`\??\`) paths, hardening
      the remaining pre-approval file accesses against the NTLM credential-leak vector'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: Fixed session-scoped permission answers (including denies) being dropped
      when answering background subagent tool permission prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: Fixed accepting the "Try the new fullscreen renderer?" prompt restarting
      the session without its permission mode (e.g. `--dangerously-skip-permissions`),
      tool allow/deny rules, model or effort flags
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: Fixed a case where an IDE diff tab closing during a permission re-prompt
      could answer the new prompt with the previous input
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: 'Fixed: permission previews now relay only to channel servers admitted
      by the inbound trust gate, and a server''s explicit permission-capability opt-out
      is honored'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: 'Fixed: credential masking on relayed permission previews can no longer
      hide commands, paths, or destinations from the approver; oversized private-key
      blocks now redact under full-strength redaction'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: 'Fixed: provider API tokens that mask on permission previews now mask even
      when directly followed by shell delimiters'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  - quote: Remote Control sessions started from Claude Code Desktop or VS Code now
      keep phones and claude.ai/code updated on the session's permission mode (and
      claude.ai/code on the model) as they change
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-safety-and-privacy-changes-in-v2-1-234
  source_release: claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in v2.1.234
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved
  sandbox: IPv6 literals in network domain lists are now bracketed…]]'
- '[[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety
  and Privacy changes in v2.1.232]]'
- '[[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety
  and Privacy changes in v2.1.233]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673|claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in v2.1.234
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in v2.1.234

**Claude Code** · 2026-08-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.234) · from [[Releases/Claude Code/claude-code-2026-08-17-v2-1-234-github-371864218-2ca32673|v2.1.234]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Security: remote file reads, session restore, CLAUDE.md includes, workflow scripts and file uploads now reject Windows NT-namespace (`\??\`) paths, hardening the remaining pre-approval file accesses against the NTLM credential-leak vector

> Fixed session-scoped permission answers (including denies) being dropped when answering background subagent tool permission prompts

> Fixed accepting the "Try the new fullscreen renderer?" prompt restarting the session without its permission mode (e.g. `--dangerously-skip-permissions`), tool allow/deny rules, model or effort flags

> Fixed a case where an IDE diff tab closing during a permission re-prompt could answer the new prompt with the previous input

> Fixed: permission previews now relay only to channel servers admitted by the inbound trust gate, and a server's explicit permission-capability opt-out is honored

> Fixed: credential masking on relayed permission previews can no longer hide commands, paths, or destinations from the approver; oversized private-key blocks now redact under full-strength redaction

> Fixed: provider API tokens that mask on permission previews now mask even when directly followed by shell delimiters

> Remote Control sessions started from Claude Code Desktop or VS Code now keep phones and claude.ai/code updated on the session's permission mode (and claude.ai/code on the model) as they change

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.234
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support changes in v2.1.234]] · Model Support
- [[Changes/Claude Code/2026-08-17-2-apps-and-integrations-changes-in-v2-1-234|2 Apps and Integrations changes in v2.1.234]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-17-2-context-window-changes-in-v2-1-234|2 Context Window changes in v2.1.234]] · Context Window
- [[Changes/Claude Code/2026-08-17-3-interface-experience-changes-in-v2-1-234|3 Interface Experience changes in v2.1.234]] · Interface Experience
- [[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed the redundant "Allowed by auto mode classifier" line that auto mode showed…]] · Agent Mode
- [[Changes/Claude Code/2026-08-17-removed-the-default-teammate-model-setting-from-config-agent-team-teammates-now|Removed the "Default teammate model" setting from /config]] · Collaboration
- [[Changes/Claude Code/2026-08-17-2-account-and-access-changes-in-v2-1-234|2 Account and Access changes in v2.1.234]] · Account and Access
- [[Changes/Claude Code/2026-08-17-12-other-changes-in-v2-1-234|12 other changes in v2.1.234]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-14 · Claude Code · [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]]
- Later: 2026-08-18 · Claude Code · [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-17-7da5bd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-17-8-safety-and-privacy-changes-in-v2-1-234.md%0ACard%20ID%3A%20claude-code-2026-08-17-7da5bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.234%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->