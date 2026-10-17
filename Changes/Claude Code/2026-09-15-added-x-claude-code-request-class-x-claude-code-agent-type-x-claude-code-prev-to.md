---
card_id: claude-code-2026-09-15-d69af3
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Context Window: Added `x-claude-code-request-class`,
  `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 534e84d3637e575b50b30144d2886f899001275bfa7aa0feb3a4407fdb68b58d
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-09-15-d69af3
  comparison: ''
  confidence: low
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: Added `x-claude-code-request-class`, `x-claude-code-agent-type`,
    `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted`
    request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`'
  evidence:
  - quote: Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`,
      `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers
      for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - llm
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Added `x-claude-code-request-class`, `x-claude-code-agent-type`…
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-10-you-shouldn-t-have-to-onboard-an-agent-every-time-you-start-a-task-each-project|Shared
  context]]'
- '[[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies-51d06c|Cursor
  launches Projects]]'
- '[[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved
  the spinner status during long thinking]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: context-window
title: Added x-claude-code-request-class, x-claude-code-agent-type…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `x-claude-code-request-class`, `x-claude-code-agent-type`…

**Claude Code** · 2026-09-15 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
- [[Changes/Claude Code/2026-09-15-8-other-changes-in-v2-1-273|8 other changes in v2.1.273]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]]
- Later: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-d69af3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to.md%0ACard%20ID%3A%20claude-code-2026-09-15-d69af3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->