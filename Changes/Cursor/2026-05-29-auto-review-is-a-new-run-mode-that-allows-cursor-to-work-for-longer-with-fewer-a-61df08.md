---
card_id: cursor-2026-05-29-61df08
date: '2026-05-29'
description: 'Cursor · 2026-05-29 · Agent Mode: Auto-review is a new run mode that
  allows Cursor to work for longer with fewer approval prompts and safer execution.'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1058
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: a3ce4b72bb865a636bb55837226710fe0f11d9065d0a47573cfabd196d2a8179
product: cursor
product_name: Cursor
record:
  ai_generated: true
  card_id: cursor-2026-05-29-61df08
  comparison: ''
  confidence: low
  date: '2026-05-29'
  description: 'Cursor — Auto-review Run Mode: Auto-review is a new run mode that
    allows Cursor to work for longer with fewer approval prompts and safer execution.'
  evidence:
  - quote: Auto-review is a new run mode that allows Cursor to work for longer with
      fewer approval prompts and safer execution.
    source_release: https://cursor.com/changelog/auto-review
  - quote: Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls
      run immediately, and calls that can be sandboxed run in the sandbox. All other
      agent actions go to a classifier subagent that decides whether to allow the
      call, try a different approach, or ask for your approval.
    source_release: https://cursor.com/changelog/auto-review
  - quote: Configure your run mode in Settings > Cursor Settings > Agents > Approvals
      & Execution. You can also steer the classifier agent by giving it custom instructions.
    source_release: https://cursor.com/changelog/auto-review
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: cursor
  product_name: Cursor
  slug: auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a
  source_release: cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919
  source_type: cursor_changelog
  theme: agent-mode
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Auto-review Run Mode
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714
  fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-05-28-3-agent-mode-changes-in-v1-0-55|3 Agent
  Mode changes in v1.0.55]]'
- '[[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude
  agents: the agent field in settings.json is now honored for dispatched…]]'
source_release: '[[Releases/Cursor/cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919|cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919]]'
source_type: cursor_changelog
theme: agent-mode
title: Auto-review Run Mode
type: change
---

<!-- chronolog:begin region="header" -->
# Auto-review Run Mode

**Cursor** · 2026-05-29 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://cursor.com/changelog/auto-review) · from [[Releases/Cursor/cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919|Auto-review Run Mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Auto-review is a new run mode that allows Cursor to work for longer with fewer approval prompts and safer execution.
>
> Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls run immediately, and calls that can be sandboxed run in the sandbox. All other agent actions go to a classifier subagent that decides whether to allow the call, try a different approach, or ask for your approval.
>
> Configure your run mode in Settings > Cursor Settings > Agents > Approvals & Execution. You can also steer the classifier agent by giving it custom instructions.
>
> Source: https://cursor.com/changelog/auto-review
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-29 · Claude Code · [[Changes/Claude Code/2026-05-29-claude-agents-the-agent-field-in-settings-json-is-now-honored-for-dispatched-ses|claude agents: the agent field in settings.json is now honored for dispatched…]]
- Later: 2026-05-29 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-29-add-builtinagents-rubberduck-setting-to-enable-or-disable-the-rubber-duck-agent|Add builtInAgents.rubberDuck setting to enable or disable the rubber duck agent…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-05-29-61df08&body=Card%3A%20Changes%2FCursor%2F2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a-61df08.md%0ACard%20ID%3A%20cursor-2026-05-29-61df08%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fauto-review%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->