---
card_id: claude-code-2026-10-21-ff3242
date: '2026-10-21'
description: 'Claude Code · 2026-10-21 · Safety and Privacy: Added the `claude_code.safety_event`
  OpenTelemetry event for each tool call a permission rule, auto mode, a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1284
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: d9012d41076171b6beaf5de364fdf399c7f0682da84bdbe300ebcf6784af25f9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-21-ff3242
  comparison: ''
  date: '2026-10-21'
  description: 'Claude Code — v2.1.307: Added the `claude_code.safety_event` OpenTelemetry
    event for each tool call a permission rule, auto mode, a safety check, a hook
    or the sandbox stopped, prompted or sent back'
  evidence:
  - quote: Added the `claude_code.safety_event` OpenTelemetry event for each tool
      call a permission rule, auto mode, a safety check, a hook or the sandbox stopped,
      prompted or sent back
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.307
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm
  source_release: claude-code-2026-10-21-v2-1-307-github-420041378-ab2f5a8d
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - auto mode
    score: 60
    theme: agent-mode
  - matched_terms:
    - safety
    score: 50
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v2
  title: Added the `claude_code.safety_event` OpenTelemetry event for each tool call…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety
  and Privacy changes in v2.1.302]]'
- '[[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added
  decider: "person" to a mod''s tool.check answer: only the permission dialog…]]'
- '[[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety
  and Privacy changes in v2.1.305]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-21-v2-1-307-github-420041378-ab2f5a8d|claude-code-2026-10-21-v2-1-307-github-420041378-ab2f5a8d]]'
source_type: github_releases
theme: safety-privacy
title: Added the claude_code.safety_event OpenTelemetry event for each tool call…
type: change
---

<!-- chronolog:begin region="header" -->
# Added the `claude_code.safety_event` OpenTelemetry event for each tool call…

**Claude Code** · 2026-10-21 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.307) · from [[Releases/Claude Code/claude-code-2026-10-21-v2-1-307-github-420041378-ab2f5a8d|v2.1.307]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added the `claude_code.safety_event` OpenTelemetry event for each tool call a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.307
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-21-2-developer-workflow-changes-in-v2-1-307|2 Developer Workflow changes in v2.1.307]] · Developer Workflow
- [[Changes/Claude Code/2026-10-21-3-apps-and-integrations-changes-in-v2-1-307|3 Apps and Integrations changes in v2.1.307]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-21-2-voice-and-audio-changes-in-v2-1-307|2 Voice and Audio changes in v2.1.307]] · Voice and Audio
- [[Changes/Claude Code/2026-10-21-2-account-and-access-changes-in-v2-1-307|2 Account and Access changes in v2.1.307]] · Account and Access
- [[Changes/Claude Code/2026-10-21-changed-the-axscreenreader-setting-and-claude-ax-screen-reader-in-a-settings-env|Changed the axScreenReader setting and CLAUDE_AX_SCREEN_READER in a settings…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-21-improved-fork-subagents-launched-together-each-is-now-told-which-launch-is-its-o|Improved fork subagents launched together]] · Agent Mode
- [[Changes/Claude Code/2026-10-21-added-claude-api-api-version-to-move-claude-api-code-to-api-version-2026-10-21|Added /claude-api api-version to move Claude API code to API version 2026-10-21]] · Other changes
- [[Changes/Claude Code/2026-10-21-4-other-changes-in-v2-1-307|4 other changes in v2.1.307]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-20 · Claude Code · [[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety and Privacy changes in v2.1.305]]
- Later: 2026-10-22 · Claude Code · [[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety and Privacy changes in v2.1.309]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-21-ff3242&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm.md%0ACard%20ID%3A%20claude-code-2026-10-21-ff3242%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.307%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->