---
card_id: claude-code-2026-09-10-b61703
date: '2026-09-10'
description: 'Claude Code · 2026-09-10 · Safety and Privacy: 8 changes in v2.1.268
  — Fixed deny and ask permission rules on symlinked directories (`/etc`, `/tmp`,
  `/var` on…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1243
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b0856180bef8d2cda4186bd167cb3dba5a718a96fb60cd27d433c840689dba43
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-10-b61703
  comparison: ''
  date: '2026-09-10'
  description: 'Claude Code — v2.1.268: 8 Safety and Privacy changes'
  evidence:
  - quote: Fixed deny and ask permission rules on symlinked directories (`/etc`, `/tmp`,
      `/var` on macOS; `/bin` on Linux) not applying when a path was given by its
      real location, and Bash commands ignoring deny rules written on a symlinked
      path spelling
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Fixed a case where a Read or Edit deny rule did not apply when an `env
      -C`, `eval` or similar command the permission checker cannot analyze was on
      the same line
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Fixed long-context 429s on Fable models showing the usage-credits consent
      prompt instead of the 1M-context message on Pro and Team plans
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Improved the terminal permission prompt for artifacts: it now leads with
      the ask''s question'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: Changed the artifact data-edit permission prompt in the terminal to a card
      that shows the document count and who can open the artifact
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[VSCode] Added Left and Right arrow keys to change where an always-allow
      permission rule is saved, for keyboard and screen reader users'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[VSCode] Changed some artifact permission prompts to omit the "don''t
      ask again" choice, matching the terminal'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[Claude Tag] Improved how Claude explains a blocked action: it now says
      whether a permission check, its own decision to confirm first, or missing access
      stopped it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-safety-and-privacy-changes-in-v2-1-268
  source_release: claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in v2.1.268
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety
  and Privacy changes in v2.1.261]]'
- '[[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety
  and Privacy changes in v2.1.265]]'
- '[[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety
  and Privacy changes in v2.1.267]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in v2.1.268
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in v2.1.268

**Claude Code** · 2026-09-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) · from [[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|v2.1.268]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed deny and ask permission rules on symlinked directories (`/etc`, `/tmp`, `/var` on macOS; `/bin` on Linux) not applying when a path was given by its real location, and Bash commands ignoring deny rules written on a symlinked path spelling

> Fixed a case where a Read or Edit deny rule did not apply when an `env -C`, `eval` or similar command the permission checker cannot analyze was on the same line

> Fixed long-context 429s on Fable models showing the usage-credits consent prompt instead of the 1M-context message on Pro and Team plans

> Improved the terminal permission prompt for artifacts: it now leads with the ask's question

> Changed the artifact data-edit permission prompt in the terminal to a card that shows the document count and who can open the artifact

> [VSCode] Added Left and Right arrow keys to change where an always-allow permission rule is saved, for keyboard and screen reader users

> [VSCode] Changed some artifact permission prompts to omit the "don't ask again" choice, matching the terminal

> [Claude Tag] Improved how Claude explains a blocked action: it now says whether a permission check, its own decision to confirm first, or missing access stopped it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account and Access changes in v2.1.268]] · Account and Access
- [[Changes/Claude Code/2026-09-10-2-interface-experience-changes-in-v2-1-268|2 Interface Experience changes in v2.1.268]] · Interface Experience
- [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]] · Pricing Model
- [[Changes/Claude Code/2026-09-10-added-browser-tab-icons-for-published-artifacts-chosen-by-claude-to-match-each-p|Added browser-tab icons for published artifacts, chosen by Claude to match each page]] · Editor Experience
- [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-10-2-reliability-and-performance-changes-in-v2-1-268|2 Reliability and Performance changes in v2.1.268]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code Review Added a note under the still-open findings list in follow-up reviews]] · Developer Workflow
- [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]] · Agent Mode
- [[Changes/Claude Code/2026-09-10-vscode-added-a-claude-code-focus-last-message-command-that-moves-keyboard-focus|VSCode Added a "Claude Code]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-10-7-apps-and-integrations-changes-in-v2-1-268|7 Apps and Integrations changes in v2.1.268]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]]
- Later: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-10-b61703&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-10-8-safety-and-privacy-changes-in-v2-1-268.md%0ACard%20ID%3A%20claude-code-2026-09-10-b61703%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.268%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->