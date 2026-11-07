---
card_id: kimi-code-2026-07-12-1babc9
date: '2026-07-12'
description: 'Kimi Code · 2026-07-12 · Agent Mode: 2 changes in Kimi Code 0.23.6 (2026-07-12)
  — Add a `subagent.timeout_ms` config option (or the `KIMI_SUBAGENT_TIMEOUT_MS`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1102
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7c7bf00ca2ecfbca75a389f3606ea3b8197f232ffd414e425c02ec912ae776d1
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-12-1babc9
  comparison: ''
  date: '2026-07-12'
  description: 'Kimi Code — Kimi Code 0.23.6 (2026-07-12): 2 Agent Mode changes'
  evidence:
  - quote: Add a `subagent.timeout_ms` config option (or the `KIMI_SUBAGENT_TIMEOUT_MS`
      env var) to control how long a single subagent may run before timing out; the
      default is raised from 30 minutes to 2 hours.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Add a print-mode background policy: set `[background].print_background_mode
      = "steer"` to keep `kimi -p` alive across background-task completions, so the
      main agent can be steered into follow-up turns.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 2-agent-mode-changes-in-kimi-code-0-23-6
  source_release: kimi-code-2026-07-12-0-23-6-0f24ae91
  source_type: kimi_code_changelog
  theme: agent-mode
  title: 2 Agent Mode changes in Kimi Code 0.23.6
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode
  changes in v2.1.207]]'
- '[[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto
  mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]]'
- '[[Changes/Ollama/2026-07-11-2-agent-mode-changes-in-v0-32-0|2 Agent Mode changes
  in v0.32.0]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-12-0-23-6-0f24ae91|kimi-code-2026-07-12-0-23-6-0f24ae91]]'
source_type: kimi_code_changelog
theme: agent-mode
title: 2 Agent Mode changes in Kimi Code 0.23.6
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in Kimi Code 0.23.6

**Kimi Code** · 2026-07-12 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-12-0-23-6-0f24ae91|Kimi Code 0.23.6 (2026-07-12)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add a `subagent.timeout_ms` config option (or the `KIMI_SUBAGENT_TIMEOUT_MS` env var) to control how long a single subagent may run before timing out; the default is raised from 30 minutes to 2 hours.

> Add a print-mode background policy: set `[background].print_background_mode = "steer"` to keep `kimi -p` alive across background-task completions, so the main agent can be steered into follow-up turns.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-12-update-the-webbridge-install-page-link-opened-from-the-plugins-panel|Update the WebBridge install page link opened from the /plugins panel]] · Apps and Integrations
- [[Changes/Kimi Code/2026-07-12-web-add-workspaces-by-typing-an-absolute-path-directly-in-the-workspace-picker-s|web: Add workspaces by typing an absolute path directly in the workspace picker's…]] · Interface Experience
- [[Changes/Kimi Code/2026-07-12-keep-kimi-p-runs-alive-after-a-turn-ends-while-a-goal-is-still-active-or-a-cron|Keep kimi -p runs alive after a turn ends while a goal is still active or a cron…]] · Automation and Scheduling
- [[Changes/Kimi Code/2026-07-12-web-keep-the-server-access-token-for-up-to-7-days-across-tab-close-and-browser-r|web: Keep the server access token for up to 7 days across tab close and browser…]] · Editor Experience
- [[Changes/Kimi Code/2026-07-12-3-model-support-changes-in-kimi-code-0-23-6|3 Model Support changes in Kimi Code 0.23.6]] · Model Support
- [[Changes/Kimi Code/2026-07-12-2-other-changes-in-kimi-code-0-23-6|2 other changes in Kimi Code 0.23.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-11 · Ollama · [[Changes/Ollama/2026-07-11-2-agent-mode-changes-in-v0-32-0|2 Agent Mode changes in v0.32.0]]
- Later: 2026-07-13 · Codex CLI · [[Changes/Codex CLI/2026-07-13-2-agent-mode-changes-in-rust-v0-144-2|2 Agent Mode changes in rust-v0.144.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-12-1babc9&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-12-2-agent-mode-changes-in-kimi-code-0-23-6.md%0ACard%20ID%3A%20kimi-code-2026-07-12-1babc9%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->