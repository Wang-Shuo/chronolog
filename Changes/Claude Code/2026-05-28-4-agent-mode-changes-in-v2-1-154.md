---
card_id: claude-code-2026-05-28-792c73
date: '2026-05-28'
description: 'Claude Code · 2026-05-28 · Agent Mode: 4 changes in v2.1.154 — `claude
  agents`: type `! <command>` to run a shell command as a background session you can…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0a6b52e095f01867859118d7369e26ec82860b659ed0f7e57deeb16c22702d67
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-28-792c73
  comparison: ''
  date: '2026-05-28'
  description: 'Claude Code — v2.1.154: 4 Agent Mode changes'
  evidence:
  - quote: '`claude agents`: type `! <command>` to run a shell command as a background
      session you can attach to and detach from. Also available as `claude --bg --exec
      ''<command>''`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: '`claude agents`: `/logout` now signs you out instead of being sent to
      a background session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: '`←←` to open the agents view now works on Bedrock, Vertex, Foundry, and
      with telemetry disabled'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: Improved the auto-mode classifier's detection of data exfiltration, particularly
      bulk transfers of repository contents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-154
  source_release: claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.154
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-20-loop-skill|/loop skill]]'
- '[[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto
  mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]]'
- '[[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode
  changes in v2.1.152]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.154
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.154

**Claude Code** · 2026-05-28 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) · from [[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|v2.1.154]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `claude agents`: type `! <command>` to run a shell command as a background session you can attach to and detach from. Also available as `claude --bg --exec '<command>'`

> `claude agents`: `/logout` now signs you out instead of being sent to a background session

> `←←` to open the agents view now works on Bedrock, Vertex, Foundry, and with telemetry disabled

> Improved the auto-mode classifier's detection of data exfiltration, particularly bulk transfers of repository contents

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-28-remote-control-autocomplete-now-shows-disconnect-remote-control-when-remote-cont|/remote-control autocomplete now shows "Disconnect Remote Control" when Remote…]] · Editor Experience
- [[Changes/Claude Code/2026-05-28-vscode-auto-mode-no-longer-requires-the-bypass-permissions-setting-to-appear-in|VSCode Auto mode no longer requires the bypass-permissions setting to appear…]] · Interface Experience
- [[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4 Apps and Integrations changes in v2.1.154]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-28-5-model-support-changes-in-v2-1-154|5 Model Support changes in v2.1.154]] · Model Support
- [[Changes/Claude Code/2026-05-28-simplify-now-runs-a-cleanup-only-review-reuse-simplification-efficiency-altitude|/simplify now runs a cleanup-only review…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Agent Mode
- [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|Claude now reserves the multiple-choice question prompt for decisions it genuinely…]] · Context Window
- [[Changes/Claude Code/2026-05-28-renamed-the-effort-slider-labels-from-speed-intelligence-to-faster-smarter-for-c|Renamed the /effort slider labels…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-27 · Claude Code · [[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode changes in v2.1.152]]
- Later: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-3-agent-mode-changes-in-v2-1-153|3 Agent Mode changes in v2.1.153]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-28-792c73&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-28-4-agent-mode-changes-in-v2-1-154.md%0ACard%20ID%3A%20claude-code-2026-05-28-792c73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.154%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->