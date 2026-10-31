---
card_id: claude-code-2026-04-28-ae7d39
date: '2026-04-28'
description: 'Claude Code · 2026-04-28 · Developer Workflow: 4 changes in v2.1.121
  — `/terminal-setup` now enables iTerm2''s "Applications in terminal may access clipboard"…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1137
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ae471e995685dbf4538167751c456bc714cc35520ddf44c16a38770b34605238
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-28-ae7d39
  comparison: ''
  date: '2026-04-28'
  description: 'Claude Code — v2.1.121: 4 Developer Workflow changes'
  evidence:
  - quote: '`/terminal-setup` now enables iTerm2''s "Applications in terminal may
      access clipboard" setting so `/copy` works, including from tmux'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: The terminal tab session title is now generated in your configured `language`
      setting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: LSP diagnostic summaries now expand on click/ctrl+o and show the expand
      hint
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  - quote: Reduced peak file descriptor usage during `find` in the Bash tool on large
      directory trees
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-developer-workflow-changes-in-v2-1-121
  source_release: claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v2.1.121
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-4-developer-workflow-changes-in-v2-1-119|4 Developer
  Workflow changes in v2.1.119]]'
- '[[Changes/Claude Code/2026-04-23-wsl-on-windows-can-now-inherit-windows-side-managed-settings-via-the-wslinherits|WSL
  on Windows can now inherit Windows-side managed settings…]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|OpenTelemetry:
  added claude_code.at_mention log event for @-mention resolution]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v2.1.121
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v2.1.121

**Claude Code** · 2026-04-28 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.121) · from [[Releases/Claude Code/claude-code-2026-04-28-v2-1-121-github-314262096-ff31d5ce|v2.1.121]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/terminal-setup` now enables iTerm2's "Applications in terminal may access clipboard" setting so `/copy` works, including from tmux

> The terminal tab session title is now generated in your configured `language` setting

> LSP diagnostic summaries now expand on click/ctrl+o and show the expand hint

> Reduced peak file descriptor usage during `find` in the Bash tool on large directory trees

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.121
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-28-faster-startup-after-upgrading-removed-the-recent-activity-panel-from-the-releas|Faster startup after upgrading]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-28-2-agent-mode-changes-in-v2-1-121|2 Agent Mode changes in v2.1.121]] · Agent Mode
- [[Changes/Claude Code/2026-04-28-opentelemetry-added-stop-reason-gen-ai-response-finish-reasons-and-user-system-p|OpenTelemetry: added stop_reason, gen_ai.response.finish_reasons…]] · Model Support
- [[Changes/Claude Code/2026-04-28-vscode-voice-dictation-now-respects-the-accessibility-voice-speechlanguage-setti|VSCode Voice dictation now respects the accessibility.voice.speechLanguage…]] · Voice and Audio
- [[Changes/Claude Code/2026-04-28-4-interface-experience-changes-in-v2-1-121|4 Interface Experience changes in v2.1.121]] · Interface Experience
- [[Changes/Claude Code/2026-04-28-6-apps-and-integrations-changes-in-v2-1-121|6 Apps and Integrations changes in v2.1.121]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-28-vscode-context-now-opens-a-native-token-usage-dialog|VSCode /context now opens a native token usage dialog]] · Context Window
- [[Changes/Claude Code/2026-04-28-vertex-ai-support-x-509-certificate-based-workload-identity-federation-mtls-adc|Vertex AI: support X.509 certificate-based Workload Identity Federation (mTLS ADC)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|OpenTelemetry: added claude_code.at_mention log event for @-mention resolution]]
- Later: 2026-04-29 · Cursor · [[Changes/Cursor/2026-04-29-added-first-class-run-streaming-with-sse-events-reconnect-support-via-last-event|Added first-class run streaming with SSE events, reconnect support…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-28-ae7d39&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-28-4-developer-workflow-changes-in-v2-1-121.md%0ACard%20ID%3A%20claude-code-2026-04-28-ae7d39%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.121%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->