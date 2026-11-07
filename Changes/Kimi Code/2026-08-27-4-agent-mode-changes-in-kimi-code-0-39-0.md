---
card_id: kimi-code-2026-08-27-41edff
date: '2026-08-27'
description: 'Kimi Code · 2026-08-27 · Agent Mode: 4 changes in Kimi Code 0.39.0 (2026-08-27)
  — Add experimental tower mode for multi-agent orchestration; set…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8be3ce40e2232e54f980059de8c6c68be153bb0ee10519465349340cf4a16db3
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-08-27-41edff
  comparison: ''
  date: '2026-08-27'
  description: 'Kimi Code — Kimi Code 0.39.0 (2026-08-27): 4 Agent Mode changes'
  evidence:
  - quote: Add experimental tower mode for multi-agent orchestration; set `KIMI_CODE_EXPERIMENTAL_TOWER=1`,
      then run `/tower on` and `/tower ` to start.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add an optional `fork` parameter to subagent and swarm tools that starts
      the subagent with a snapshot of the calling agent's conversation history; set
      `KIMI_CODE_EXPERIMENTAL_SUBAGENT_FORK=1` or `subagent_fork = true` under `[experimental]`
      in config.toml to enable it.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Allow moving a running foreground Bash command or subagent to the
      background via the "Move to background" button on the running card.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add a dedicated `[swarm] timeout_ms` config option (or the `KIMI_CODE_SWARM_TIMEOUT_MS`
      env var) for AgentSwarm subagent timeouts, which no longer follow `[subagent]
      timeout_ms`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 4-agent-mode-changes-in-kimi-code-0-39-0
  source_release: kimi-code-2026-08-27-0-39-0-fcb1a786
  source_type: kimi_code_changelog
  theme: agent-mode
  title: 4 Agent Mode changes in Kimi Code 0.39.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud
  Agents no longer require a connected GitHub or other third-party SCM provider…]]'
- '[[Changes/Cursor/2026-08-27-cursor-now-port-forwards-your-cloud-agent-s-live-environment-straight-to-your-br|A
  live preview, right in the browser]]'
- '[[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent
  Mode changes in v1.0.81]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-08-27-0-39-0-fcb1a786|kimi-code-2026-08-27-0-39-0-fcb1a786]]'
source_type: kimi_code_changelog
theme: agent-mode
title: 4 Agent Mode changes in Kimi Code 0.39.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in Kimi Code 0.39.0

**Kimi Code** · 2026-08-27 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-08-27-0-39-0-fcb1a786|Kimi Code 0.39.0 (2026-08-27)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add experimental tower mode for multi-agent orchestration; set `KIMI_CODE_EXPERIMENTAL_TOWER=1`, then run `/tower on` and `/tower ` to start.

> Add an optional `fork` parameter to subagent and swarm tools that starts the subagent with a snapshot of the calling agent's conversation history; set `KIMI_CODE_EXPERIMENTAL_SUBAGENT_FORK=1` or `subagent_fork = true` under `[experimental]` in config.toml to enable it.

> web: Allow moving a running foreground Bash command or subagent to the background via the "Move to background" button on the running card.

> Add a dedicated `[swarm] timeout_ms` config option (or the `KIMI_CODE_SWARM_TIMEOUT_MS` env var) for AgentSwarm subagent timeouts, which no longer follow `[subagent] timeout_ms`.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-08-27-web-add-a-flat-by-workspace-tab-to-the-mobile-session-list|web: Add a flat/by-workspace tab to the mobile session list]] · Editor Experience
- [[Changes/Kimi Code/2026-08-27-web-revamp-the-right-sidebar-as-a-multi-tab-panel|web: Revamp the right sidebar as a multi-tab panel]] · Interface Experience
- [[Changes/Kimi Code/2026-08-27-web-improve-mobile-ui-styling|web: Improve mobile UI styling]] · Mobile and Desktop
- [[Changes/Kimi Code/2026-08-27-web-improve-composer-interaction-including-the-presentation-of-file-folder-and-m|web: Improve composer interaction, including the presentation of file, folder…]] · Presentation Creation
- [[Changes/Kimi Code/2026-08-27-2-apps-and-integrations-changes-in-kimi-code-0-39-0|2 Apps and Integrations changes in Kimi Code 0.39.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-27 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]]
- Later: 2026-08-27 · OpenHands · [[Changes/OpenHands/2026-08-27-4-agent-mode-changes-in-v1-16-0|4 Agent Mode changes in v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-08-27-41edff&body=Card%3A%20Changes%2FKimi%20Code%2F2026-08-27-4-agent-mode-changes-in-kimi-code-0-39-0.md%0ACard%20ID%3A%20kimi-code-2026-08-27-41edff%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->