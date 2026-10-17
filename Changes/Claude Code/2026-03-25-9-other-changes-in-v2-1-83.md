---
card_id: claude-code-2026-03-25-a325b7
date: '2026-03-25'
description: 'Claude Code · 2026-03-25 · Other changes: 9 changes in v2.1.83 — Added
  transcript search — press `/` in transcript mode (`Ctrl+O`) to search, `n`/`N` to
  step…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bf73682be049cade07ddfb13146ebcfc02fedd4819e109688d9899391e137371
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-25-a325b7
  comparison: ''
  date: '2026-03-25'
  description: 'Claude Code — v2.1.83: 9 other changes'
  evidence:
  - quote: Added transcript search — press `/` in transcript mode (`Ctrl+O`) to search,
      `n`/`N` to step through matches
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: 'Pasted images now insert an `[Image #N]` chip at the cursor so you can
      reference them positionally in your prompt'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: '`chat:killAgents` and `chat:fastMode` are now rebindable via `~/.claude/keybindings.json`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Improved `WebFetch` to identify as `Claude-User` so site operators can
      recognize and allowlist Claude Code traffic via `robots.txt`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Reduced scrollback resets in long sessions from once per turn to once per
      ~50 messages
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Increased non-streaming fallback token cap (21k → 64k) and timeout (120s
      → 300s local) so fallback requests are less likely to be truncated
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: '`/status` now works while Claude is responding, instead of being queued
      until the turn finishes'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: 'Linux: respect `XDG_DATA_HOME` when registering the `claude-cli://` protocol
      handler'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Deprecated `TaskOutput` tool in favor of using `Read` on the background
      task's output file path
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-83
  source_release: claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.83
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.83
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.83

**Claude Code** · 2026-03-25 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) · from [[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|v2.1.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added transcript search — press `/` in transcript mode (`Ctrl+O`) to search, `n`/`N` to step through matches

> Pasted images now insert an `[Image #N]` chip at the cursor so you can reference them positionally in your prompt

> `chat:killAgents` and `chat:fastMode` are now rebindable via `~/.claude/keybindings.json`

> Improved `WebFetch` to identify as `Claude-User` so site operators can recognize and allowlist Claude Code traffic via `robots.txt`

> Reduced scrollback resets in long sessions from once per turn to once per ~50 messages

> Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s local) so fallback requests are less likely to be truncated

> `/status` now works while Claude is responding, instead of being queued until the turn finishes

> Linux: respect `XDG_DATA_HOME` when registering the `claude-cli://` protocol handler

> Deprecated `TaskOutput` tool in favor of using `Read` on the background task's output file path

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]] · Agent Mode
- [[Changes/Claude Code/2026-03-25-2-interface-experience-changes-in-v2-1-83|2 Interface Experience changes in v2.1.83]] · Interface Experience
- [[Changes/Claude Code/2026-03-25-3-editor-experience-changes-in-v2-1-83|3 Editor Experience changes in v2.1.83]] · Editor Experience
- [[Changes/Claude Code/2026-03-25-3-reliability-and-performance-changes-in-v2-1-83|3 Reliability and Performance changes in v2.1.83]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps and Integrations changes in v2.1.83]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-25-added-managed-settings-d-drop-in-directory-alongside-managed-settings-json-letti|Added managed-settings.d/ drop-in directory alongside managed-settings.json…]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-25-a325b7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-25-9-other-changes-in-v2-1-83.md%0ACard%20ID%3A%20claude-code-2026-03-25-a325b7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->