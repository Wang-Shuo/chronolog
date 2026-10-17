---
card_id: claude-code-2026-09-30-046419
date: '2026-09-30'
description: 'Claude Code · 2026-09-30 · Agent Mode: 6 changes in v2.1.286 — Improved
  send now (ctrl+enter) in a subagent''s view: it now moves the subagent''s running
  command…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1182
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 69521f3f26743e083454f7a70f3e27f5945781c5160b5db1c50f2ba5d6d773aa
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-30-046419
  comparison: ''
  date: '2026-09-30'
  description: 'Claude Code — v2.1.286: 6 Agent Mode changes'
  evidence:
  - quote: 'Improved send now (ctrl+enter) in a subagent''s view: it now moves the
      subagent''s running command to the background so your message is read right
      away'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Improved replies from background agents to your messages so they no longer
      open with a separate recap of what you said
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: 'Improved claude.ai artifact link reads: WebFetch now asks the same questions
      as the Artifact tool''s read (no artifact prompt while the session''s network
      access is on, one per artifact while it is off), and an auto-mode yes no longer
      counts where only you can answer'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed the send-now key (ctrl+enter) to move a skill's own shell command
      to the background instead of ending it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: Changed the `claude-api` skill's Managed Agents examples to create environments
      with limited networking
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  - quote: '[VSCode] Changed Stop and Escape to end only the current turn; background
      agents keep running and can be stopped one by one from the agent map'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-agent-mode-changes-in-v2-1-286
  source_release: claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7
  source_type: github_releases
  theme: agent-mode
  title: 6 Agent Mode changes in v2.1.286
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added
  a "Yes, but ask again next time" answer to auto mode''s prompt before a read…]]'
- '[[Changes/ChatGPT/2026-09-29-we-re-introducing-dots-always-on-agents-in-chatgpt-that-can-take-on-ongoing-work-24bef5|ChatGPT
  introduces dots]]'
- '[[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode
  changes in v2.1.285]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7|claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7]]'
source_type: github_releases
theme: agent-mode
title: 6 Agent Mode changes in v2.1.286
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Agent Mode changes in v2.1.286

**Claude Code** · 2026-09-30 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.286) · from [[Releases/Claude Code/claude-code-2026-09-30-v2-1-286-github-400266224-9fb31eb7|v2.1.286]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved send now (ctrl+enter) in a subagent's view: it now moves the subagent's running command to the background so your message is read right away

> Improved replies from background agents to your messages so they no longer open with a separate recap of what you said

> Improved claude.ai artifact link reads: WebFetch now asks the same questions as the Artifact tool's read (no artifact prompt while the session's network access is on, one per artifact while it is off), and an auto-mode yes no longer counts where only you can answer

> Changed the send-now key (ctrl+enter) to move a skill's own shell command to the background instead of ending it

> Changed the `claude-api` skill's Managed Agents examples to create environments with limited networking

> [VSCode] Changed Stop and Escape to end only the current turn; background agents keep running and can be stopped one by one from the agent map

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed how failed API requests are retried]] · Model Support
- [[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11 Apps and Integrations changes in v2.1.286]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-30-4-interface-experience-changes-in-v2-1-286|4 Interface Experience changes in v2.1.286]] · Interface Experience
- [[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer Workflow changes in v2.1.286]] · Developer Workflow
- [[Changes/Claude Code/2026-09-30-improved-the-external-editor-ctrl-g-editors-that-take-a-line-number-now-open-on|Improved the external editor (Ctrl+G)]] · Editor Experience
- [[Changes/Claude Code/2026-09-30-improved-the-model-fallback-notice-and-the-autocompact-thrashing-error-to-say-wh|Improved the model fallback notice and the autocompact-thrashing error to say…]] · Context Window
- [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-30-046419&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-30-6-agent-mode-changes-in-v2-1-286.md%0ACard%20ID%3A%20claude-code-2026-09-30-046419%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.286%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->