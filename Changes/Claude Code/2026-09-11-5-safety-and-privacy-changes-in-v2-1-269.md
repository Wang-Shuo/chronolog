---
card_id: claude-code-2026-09-11-ebeab3
date: '2026-09-11'
description: 'Claude Code · 2026-09-11 · Safety and Privacy: 5 changes in v2.1.269
  — Fixed a deny or ask permission rule starting with `!` applying beyond the settings…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 02881242becce424a7f8924600cb0c39127e88e8ec2cafd0a684978cd90fc8f3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-11-ebeab3
  comparison: ''
  date: '2026-09-11'
  description: 'Claude Code — v2.1.269: 5 Safety and Privacy changes'
  evidence:
  - quote: Fixed a deny or ask permission rule starting with `!` applying beyond the
      settings source that wrote it; such a rule now applies only within its own source,
      and a bare `!` negation is ignored
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: Fixed plugin `headersHelper` consent prompts showing a URL path that could
      be misread as a different host
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: Fixed missing cursor in the permission-rule, auto-mode-rule, add-directory,
      session-rename and feedback-review text fields when the terminal's native cursor
      is enabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: '[VSCode] Added a Permission rules dialog that lists permission rules and
      adds or removes them in user, project, and local settings; startup-option, session-only,
      and managed rules stay read-only'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  - quote: '[VSCode] Improved screen reader and keyboard accessibility in the slash-command
      menu, @-mention menu, output-style picker, Send/Stop button, permission and
      question cards, and onboarding checklist'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-269
  source_release: claude-code-2026-09-11-v2-1-269-github-387243742-288e9189
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.269
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety
  and Privacy changes in v2.1.265]]'
- '[[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety
  and Privacy changes in v2.1.267]]'
- '[[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety
  and Privacy changes in v2.1.268]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|claude-code-2026-09-11-v2-1-269-github-387243742-288e9189]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.269
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.269

**Claude Code** · 2026-09-11 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) · from [[Releases/Claude Code/claude-code-2026-09-11-v2-1-269-github-387243742-288e9189|v2.1.269]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a deny or ask permission rule starting with `!` applying beyond the settings source that wrote it; such a rule now applies only within its own source, and a bare `!` negation is ignored

> Fixed plugin `headersHelper` consent prompts showing a URL path that could be misread as a different host

> Fixed missing cursor in the permission-rule, auto-mode-rule, add-directory, session-rename and feedback-review text fields when the terminal's native cursor is enabled

> [VSCode] Added a Permission rules dialog that lists permission rules and adds or removes them in user, project, and local settings; startup-option, session-only, and managed rules stay read-only

> [VSCode] Improved screen reader and keyboard accessibility in the slash-command menu, @-mention menu, output-style picker, Send/Stop button, permission and question cards, and onboarding checklist

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.269
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-11-vscode-improved-documents-and-messages-written-for-someone-other-than-the-user-c|VSCode Improved documents and messages written for someone other than the user]] · Files and Data
- [[Changes/Claude Code/2026-09-11-5-apps-and-integrations-changes-in-v2-1-269|5 Apps and Integrations changes in v2.1.269]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-11-added-output-style-name-to-list-and-switch-output-styles-including-over-remote-c|Added /output-style name to list and switch output styles, including over Remote…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-11-changed-skills-synced-from-claude-ai-in-cloud-sessions-to-be-named-anthropic-ski|Changed skills synced from claude.ai in cloud sessions to be named…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi|Added OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-11-3-interface-experience-changes-in-v2-1-269|3 Interface Experience changes in v2.1.269]] · Interface Experience
- [[Changes/Claude Code/2026-09-11-improved-responsiveness-in-long-sessions-transcript-updates-no-longer-re-process|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-11-3-editor-experience-changes-in-v2-1-269|3 Editor Experience changes in v2.1.269]] · Editor Experience
- [[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]] · Model Support
- [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]]
- Later: 2026-09-12 · Claude Code · [[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed read-only git commands in Bash unexpectedly asking for permission after…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-11-ebeab3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-11-5-safety-and-privacy-changes-in-v2-1-269.md%0ACard%20ID%3A%20claude-code-2026-09-11-ebeab3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.269%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->