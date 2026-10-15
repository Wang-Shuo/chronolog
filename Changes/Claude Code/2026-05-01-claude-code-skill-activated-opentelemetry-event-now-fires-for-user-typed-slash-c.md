---
card_id: claude-code-2026-05-01-2a9a10
date: '2026-05-01'
description: 'Claude Code · 2026-05-01 · Automation and Scheduling: `claude_code.skill_activated`
  OpenTelemetry event now fires for user-typed slash commands and carries a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2025-12-17-tasks-let-you-set-up-automated-prompts-that-chatgpt-can-run-for-you-you-can-now|Tasks
    let you set up automated prompts that ChatGPT can run for you]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 135
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: significant
machine_hash: fef64aa28658b36f7e4c035e2f799b526a7c3f61440faf203a8f86bfb0d8ed55
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-05-01-2a9a10
  comparison: ''
  confidence: low
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: `claude_code.skill_activated` OpenTelemetry
    event now fires for user-typed slash commands and carries a new `invocation_trigger`
    attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)'
  evidence:
  - quote: '`claude_code.skill_activated` OpenTelemetry event now fires for user-typed
      slash commands and carries a new `invocation_trigger` attribute (`"user-slash"`,
      `"claude-proactive"`, or `"nested-skill"`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v4
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: automation-scheduling
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: '`claude_code.skill_activated` OpenTelemetry event now fires for user-typed
    slash…'
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-11-most-plugins-contain-mcps-that-cloud-agents-can-use-when-kicked-off-manually-or|Most
  plugins contain MCPs that cloud agents can use when kicked off manually…]]'
- '[[Changes/Claude Code/2026-03-26-added-timestamp-markers-in-transcripts-when-scheduled-tasks-loop-croncreate-fire|Added
  timestamp markers in transcripts when scheduled tasks (/loop, CronCreate) fire]]'
- '[[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|/proactive
  is now an alias for /loop]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: automation-scheduling
title: claude_code.skill_activated OpenTelemetry event now fires for user-typed slash…
type: change
---

<!-- chronolog:begin region="header" -->
# `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash…

**Claude Code** · 2026-05-01 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) · from [[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash commands and carries a new `invocation_trigger` attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-01-added-claude-project-purge-path-to-delete-all-claude-code-state-for-a-project-tr|- Added claude project purge path to delete all Claude Code state for a project…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-01-dangerously-skip-permissions-now-bypasses-prompts-for-writes-to-claude-git-vscod|--dangerously-skip-permissions now bypasses prompts for writes to .claude/…]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude auth login now accepts the OAuth code pasted into the terminal…]] · Account and Access
- [[Changes/Claude Code/2026-05-01-the-model-picker-now-lists-models-from-your-gateway-s-v1-models-endpoint-when-an|The /model picker now lists models from your gateway's /v1/models endpoint…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-04-13 · Claude Code · [[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|/proactive is now an alias for /loop]]
- Later: 2026-05-20 · Cursor · [[Changes/Cursor/2026-05-20-for-the-next-7-days-all-agent-runs-for-newly-created-automations-are-50-off|For the next 7 days, all agent runs for newly created automations are 50% off]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2025-12-17 · ChatGPT · [[Changes/ChatGPT/2025-12-17-tasks-let-you-set-up-automated-prompts-that-chatgpt-can-run-for-you-you-can-now|Tasks let you set up automated prompts that ChatGPT can run for you]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-01-2a9a10&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c.md%0ACard%20ID%3A%20claude-code-2026-05-01-2a9a10%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.126%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->