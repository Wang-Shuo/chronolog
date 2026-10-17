---
card_id: claude-code-2026-05-01-339b7d
date: '2026-05-01'
description: 'Claude Code · 2026-05-01 · Developer Workflow: 3 changes in v2.1.126
  — Windows: when the PowerShell tool is enabled, Claude now treats PowerShell as
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1140
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 602c5cd8a57d7a8d8cd94388f0e507a48bde13a2302d7b71d6f6732fee65e9ba
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-01-339b7d
  comparison: ''
  date: '2026-05-01'
  description: 'Claude Code — v2.1.126: 3 Developer Workflow changes'
  evidence:
  - quote: 'Windows: when the PowerShell tool is enabled, Claude now treats PowerShell
      as the primary shell instead of defaulting to Bash'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  - quote: Bounded total size of file-modified reminders when a linter touches many
      files at once
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  - quote: 'Windows: clipboard writes no longer expose copied content in process command-line
      arguments visible to EDR/SIEM telemetry; also fixes >22KB selections not reaching
      the clipboard'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-126
  source_release: claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.126
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|OpenTelemetry:
  added claude_code.at_mention log event for @-mention resolution]]'
- '[[Changes/Claude Code/2026-04-28-4-developer-workflow-changes-in-v2-1-121|4 Developer
  Workflow changes in v2.1.121]]'
- '[[Changes/Cursor/2026-04-29-added-first-class-run-streaming-with-sse-events-reconnect-support-via-last-event|Added
  first-class run streaming with SSE events, reconnect support…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.126
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.126

**Claude Code** · 2026-05-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) · from [[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|v2.1.126]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows: when the PowerShell tool is enabled, Claude now treats PowerShell as the primary shell instead of defaulting to Bash

> Bounded total size of file-modified reminders when a linter touches many files at once

> Windows: clipboard writes no longer expose copied content in process command-line arguments visible to EDR/SIEM telemetry; also fixes >22KB selections not reaching the clipboard

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-01-2-model-support-changes-in-v2-1-126|2 Model Support changes in v2.1.126]] · Model Support
- [[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated OpenTelemetry event now fires for user-typed slash…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-05-01-3-safety-and-privacy-changes-in-v2-1-126|3 Safety and Privacy changes in v2.1.126]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-01-added-claude-project-purge-path-to-delete-all-claude-code-state-for-a-project-tr|- Added claude project purge path to delete all Claude Code state for a project…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-01-powershell-tool-bare-e-g-git-diff-file-is-no-longer-mis-flagged-as-the-stop-pars|PowerShell tool: bare -- (e.g. git diff -- file) is no longer mis-flagged…]] · Editor Experience
- [[Changes/Claude Code/2026-05-01-claude-auth-login-now-accepts-the-oauth-code-pasted-into-the-terminal-when-the-b|claude auth login now accepts the OAuth code pasted into the terminal…]] · Account and Access
- [[Changes/Claude Code/2026-05-01-2-other-changes-in-v2-1-126|2 other changes in v2.1.126]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-29 · Cursor · [[Changes/Cursor/2026-04-29-added-first-class-run-streaming-with-sse-events-reconnect-support-via-last-event|Added first-class run streaming with SSE events, reconnect support…]]
- Later: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-2-developer-workflow-changes-in-v2-1-129|2 Developer Workflow changes in v2.1.129]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-01-339b7d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-01-3-developer-workflow-changes-in-v2-1-126.md%0ACard%20ID%3A%20claude-code-2026-05-01-339b7d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.126%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->