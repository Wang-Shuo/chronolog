---
card_id: claude-code-2026-08-19-27fec2
date: '2026-08-19'
description: 'Claude Code · 2026-08-19 · Model Support: Added `ANTHROPIC_DEFAULT_MODEL`
  environment variable: sets the model new sessions start on, while a `/model` pick…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1318
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: f89d786405888afa5a1f7bdde492ad51d3ec75c2f5e875256a130956a55f191a
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-19-27fec2
  comparison: ''
  confidence: low
  date: '2026-08-19'
  description: 'Claude Code — v2.1.236: Added `ANTHROPIC_DEFAULT_MODEL` environment
    variable: sets the model new sessions start on, while a `/model` pick still overrides
    it and persists across restarts (unlike `ANTHROPIC_MODEL`)'
  evidence:
  - quote: 'Added `ANTHROPIC_DEFAULT_MODEL` environment variable: sets the model new
      sessions start on, while a `/model` pick still overrides it and persists across
      restarts (unlike `ANTHROPIC_MODEL`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s
  source_release: claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79
  source_type: github_releases
  theme: model-support
  title: Added `ANTHROPIC_DEFAULT_MODEL` environment variable
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-11-changed-the-write-tool-so-newer-models-can-overwrite-an-existing-file-they-haven|Changed
  the Write tool so newer models can overwrite an existing file they haven''t…]]'
- '[[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support
  changes in v2.1.233]]'
- '[[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support
  changes in v2.1.234]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79]]'
source_type: github_releases
theme: model-support
title: Added ANTHROPIC_DEFAULT_MODEL environment variable
type: change
---

<!-- chronolog:begin region="header" -->
# Added `ANTHROPIC_DEFAULT_MODEL` environment variable

**Claude Code** · 2026-08-19 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.236) · from [[Releases/Claude Code/claude-code-2026-08-19-v2-1-236-github-373272539-bbbacf79|v2.1.236]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_DEFAULT_MODEL` environment variable: sets the model new sessions start on, while a `/model` pick still overrides it and persists across restarts (unlike `ANTHROPIC_MODEL`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.236
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-19-improved-startup-performance-the-session-counter-is-now-written-in-the-backgroun|Improved startup performance: the session counter is now written in the background]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-19-added-notify-when-idle-to-cross-session-sendmessage-ask-another-claude-code-sess|Added notify_when_idle to cross-session SendMessage]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer Workflow changes in v2.1.236]] · Developer Workflow
- [[Changes/Claude Code/2026-08-19-changed-the-model-picker-to-highlight-only-the-newest-model-s-name-so-the-highli|Changed the /model picker to highlight only the newest model's name…]] · Interface Experience
- [[Changes/Claude Code/2026-08-19-4-agent-mode-changes-in-v2-1-236|4 Agent Mode changes in v2.1.236]] · Agent Mode
- [[Changes/Claude Code/2026-08-19-sigterm-in-print-sdk-mode-no-longer-records-an-interrupted-turn-or-synthetic-too|SIGTERM in print/SDK mode no longer records an interrupted turn or synthetic tool…]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-19-usage-now-shows-the-usage-credits-spend-row-for-team-and-enterprise-members-and|/usage now shows the usage-credits spend row for Team and Enterprise members…]] · Pricing Model
- [[Changes/Claude Code/2026-08-19-3-other-changes-in-v2-1-236|3 other changes in v2.1.236]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-17 · Claude Code · [[Changes/Claude Code/2026-08-17-2-model-support-changes-in-v2-1-234|2 Model Support changes in v2.1.234]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-19-27fec2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-19-added-anthropic-default-model-environment-variable-sets-the-model-new-sessions-s.md%0ACard%20ID%3A%20claude-code-2026-08-19-27fec2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.236%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->