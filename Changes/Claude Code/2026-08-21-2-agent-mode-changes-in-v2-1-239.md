---
card_id: claude-code-2026-08-21-3c529e
date: '2026-08-21'
description: 'Claude Code · 2026-08-21 · Agent Mode: 2 changes in v2.1.239 — `ListAgents`
  now tells a session its own name (the one peers use to message it), and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1142
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 556f1819aa3c2e92b48dbcf7877cde336b0203b4576d2fe4d1080e6778404fc3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-21-3c529e
  comparison: ''
  date: '2026-08-21'
  description: 'Claude Code — v2.1.239: 2 Agent Mode changes'
  evidence:
  - quote: '`ListAgents` now tells a session its own name (the one peers use to message
      it), and `SendMessage` to your own name says so instead of "no agent named …"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
  - quote: '`ListAgents` and `/list-agents` now list your live teammates (previously
      only subagents and other sessions appeared, so a reachable teammate looked absent)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-239
  source_release: claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.239
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-19-steering-improvements|Steering improvements]]'
- '[[Changes/Cursor/2026-08-19-subagents-on-their-own-machines|Subagents on their
  own machines]]'
- '[[Changes/Cursor/2026-08-19-goal|/goal]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918|claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.239
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.239

**Claude Code** · 2026-08-21 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) · from [[Releases/Claude Code/claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918|v2.1.239]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `ListAgents` now tells a session its own name (the one peers use to message it), and `SendMessage` to your own name says so instead of "no agent named …"

> `ListAgents` and `/list-agents` now list your live teammates (previously only subagents and other sessions appeared, so a reachable teammate looked absent)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-21-3-interface-experience-changes-in-v2-1-239|3 Interface Experience changes in v2.1.239]] · Interface Experience
- [[Changes/Claude Code/2026-08-21-2-developer-workflow-changes-in-v2-1-239|2 Developer Workflow changes in v2.1.239]] · Developer Workflow
- [[Changes/Claude Code/2026-08-21-persistent-retry-mode-claude-code-retry-watchdog-now-fails-immediately-on-organi|Persistent retry mode (CLAUDE_CODE_RETRY_WATCHDOG) now fails immediately…]] · Pricing Model
- [[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2 Apps and Integrations changes in v2.1.239]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-21-claude-in-chrome-clear-now-closes-the-session-s-chrome-tab-group-and-empty-group|Claude in Chrome]] · Editor Experience
- [[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved the reminder shown after compaction so a skill's original arguments are not…]] · Context Window
- [[Changes/Claude Code/2026-08-21-remote-sessions-images-uploaded-from-mobile-now-include-their-saved-file-path-so|Remote sessions: images uploaded from mobile now include their saved file path…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-21-windows-cross-session-messaging-is-now-available-so-claude-code-sessions-across|Windows: cross-session messaging is now available, so Claude Code sessions across…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-21-alpine-musl-builds-native-image-paste-clipboard-and-audio-capture-add-ons-now-lo|Alpine/musl builds: native image paste, clipboard, and audio-capture add-ons now…]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-19 · Cursor · [[Changes/Cursor/2026-08-19-goal|/goal]]
- Later: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-21-3c529e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-21-2-agent-mode-changes-in-v2-1-239.md%0ACard%20ID%3A%20claude-code-2026-08-21-3c529e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.239%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->