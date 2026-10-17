---
card_id: claude-code-2026-08-20-30b452
date: '2026-08-20'
description: 'Claude Code · 2026-08-20 · Other changes: 3 changes in v2.1.238 — Added
  `claude self-hosted-runner --defer-shutdown-max-min <minutes>`: on SIGTERM, keep…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9de94a1ee20013e11626110242def89b8c1645d0afc0286bd4d02f04caac0b74
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-20-30b452
  comparison: ''
  date: '2026-08-20'
  description: 'Claude Code — v2.1.238: 3 other changes'
  evidence:
  - quote: 'Added `claude self-hosted-runner --defer-shutdown-max-min <minutes>`:
      on SIGTERM, keep serving attached sessions, park what is left after that many
      minutes, then exit'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: 'Cross-session messaging: sending to a session on this machine that refuses
      inbound messages (e.g. `crossSessionInbound: "refuse"`) now reports "refused"
      to the sender instead of a silent success'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: 'Cross-session messaging: a session whose inbox drops your messages (rate
      limit or full queue) now tells your session, instead of the messages vanishing
      silently'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-other-changes-in-v2-1-238
  source_release: claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2
  source_type: github_releases
  theme: uncategorized
  title: 3 other changes in v2.1.238
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2]]'
source_type: github_releases
theme: uncategorized
title: 3 other changes in v2.1.238
type: change
---

<!-- chronolog:begin region="header" -->
# 3 other changes in v2.1.238

**Claude Code** · 2026-08-20 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) · from [[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|v2.1.238]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude self-hosted-runner --defer-shutdown-max-min <minutes>`: on SIGTERM, keep serving attached sessions, park what is left after that many minutes, then exit

> Cross-session messaging: sending to a session on this machine that refuses inbound messages (e.g. `crossSessionInbound: "refuse"`) now reports "refused" to the sender instead of a silent success

> Cross-session messaging: a session whose inbox drops your messages (rate limit or full queue) now tells your session, instead of the messages vanishing silently

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-20-updated-the-bundled-claude-api-skill-for-the-managed-agents-aug-19-release-web-s|Updated the bundled claude-api skill for the Managed Agents Aug 19 release]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6 Apps and Integrations changes in v2.1.238]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer Workflow changes in v2.1.238]] · Developer Workflow
- [[Changes/Claude Code/2026-08-20-improved-startup-bare-claude-starts-sooner-on-macos|Improved startup: bare claude starts sooner on macOS]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-20-improved-startup-responsiveness-the-automatic-update-check-now-runs-about-10-sec|Improved startup responsiveness]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-20-changed-ctrl-l-and-cmd-k-in-fullscreen-to-always-just-repaint-the-double-press-c|Changed Ctrl+L and Cmd+K in fullscreen to always just repaint]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-20-30b452&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-20-3-other-changes-in-v2-1-238.md%0ACard%20ID%3A%20claude-code-2026-08-20-30b452%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.238%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->