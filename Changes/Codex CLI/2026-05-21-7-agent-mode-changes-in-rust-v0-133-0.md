---
card_id: codex-cli-2026-05-21-1e5a35
date: '2026-05-21'
description: 'Codex CLI · 2026-05-21 · Agent Mode: 7 changes in 0.133.0 — Extensions
  can observe more lifecycle events, including subagent start/stop, tool execution,
  turn…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 845b8bff21565f344d468d0c34aa5a589d013514ab30b1168c7eb36685fcf47e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-21-1e5a35
  comparison: ''
  date: '2026-05-21'
  description: 'Codex CLI — 0.133.0: 7 Agent Mode changes'
  evidence:
  - quote: 'Extensions can observe more lifecycle events, including subagent start/stop,
      tool execution, turn metadata, and async approval/turn processing. (#22782,
      #22873, #23309, #23688, #23690, #23692)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: 'Made AGENTS instruction loading more reliable, including local global
      reads and warnings for invalid UTF-8 instead of silent drops. (#23343, #23232)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23343 codex: route global AGENTS reads through LOCAL_FS @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23144 Defer v1 multi-agent tools behind tool search @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23475 chore: namespace v1 sub-agent tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23576 test: fix multi-agent service tier assertion @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23232 Warn on invalid UTF-8 in AGENTS.md files @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-agent-mode-changes-in-rust-v0-133-0
  source_release: codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in rust-v0.133.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-20-loop-skill|/loop skill]]'
- '[[Changes/GitHub Copilot CLI/2026-05-20-remote-command-can-now-be-used-while-the-agent-is-working|/remote
  command can now be used while the agent is working]]'
- '[[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto
  mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in rust-v0.133.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in rust-v0.133.0

**Codex CLI** · 2026-05-21 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.133.0) · from [[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Extensions can observe more lifecycle events, including subagent start/stop, tool execution, turn metadata, and async approval/turn processing. (#22782, #22873, #23309, #23688, #23690, #23692)

> Made AGENTS instruction loading more reliable, including local global reads and warnings for invalid UTF-8 instead of silent drops. (#23343, #23232)

> #23343 codex: route global AGENTS reads through LOCAL_FS @starr-openai

> #23144 Defer v1 multi-agent tools behind tool search @jif-oai

> #23475 chore: namespace v1 sub-agent tools @jif-oai

> #23576 test: fix multi-agent service tier assertion @bolinfest

> #23232 Warn on invalid UTF-8 in AGENTS.md files @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.133.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context Window changes in rust-v0.133.0]] · Context Window
- [[Changes/Codex CLI/2026-05-21-3-developer-workflow-changes-in-rust-v0-133-0|3 Developer Workflow changes in rust-v0.133.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-21-23578-fix-app-server-speed-up-shutdown-fcoury-oai|♯23578 fix(app-server): speed up shutdown @fcoury-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-21-79-other-changes-in-rust-v0-133-0|79 other changes in rust-v0.133.0]] · Other changes
- [[Changes/Codex CLI/2026-05-21-goals-are-now-enabled-by-default-backed-by-dedicated-storage-and-track-progress|Goals are now enabled by default, backed by dedicated storage, and track progress…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-21 · Claude Code · [[Changes/Claude Code/2026-05-21-auto-mode-no-longer-suppresses-askuserquestion-when-the-user-or-a-skill-explicit|Auto mode no longer suppresses AskUserQuestion when the user or a skill explicitly…]]
- Later: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-2-agent-mode-changes-in-v0-43-0|2 Agent Mode changes in v0.43.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-21-1e5a35&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-21-7-agent-mode-changes-in-rust-v0-133-0.md%0ACard%20ID%3A%20codex-cli-2026-05-21-1e5a35%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.133.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->