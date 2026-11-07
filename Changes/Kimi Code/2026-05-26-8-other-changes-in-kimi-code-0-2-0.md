---
card_id: kimi-code-2026-05-26-75ef91
date: '2026-05-26'
description: 'Kimi Code · 2026-05-26 · Other changes: 8 changes in Kimi Code 0.2.0
  (2026-05-26) — Add `Ctrl-J` as an additional shortcut for inserting new lines in
  the TUI…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 77301c18480ee0e75bbbbcc5527d70812fb46fd63c31a68673b0c2f57ba26a5f
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-05-26-75ef91
  comparison: ''
  date: '2026-05-26'
  description: 'Kimi Code — Kimi Code 0.2.0 (2026-05-26): 8 other changes'
  evidence:
  - quote: Add `Ctrl-J` as an additional shortcut for inserting new lines in the TUI
      prompt.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add wire record migration handling during session replay.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Migrate user skills from `~/.kimi/skills/` to `~/.kimi-code/skills/` during
      the first-launch migration; existing target skills are kept.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Correct the `X-Msh-Platform` header value to `kimi_code_cli`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Avoid CPU spikes from large streamed tool arguments and coalesce high-frequency
      streaming UI updates.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Warn tmux users when extended key settings may prevent modified Enter shortcuts
      from working.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Flatten tool call data by inlining tool names and arguments at the top
      level, and limit legacy record migration so it only rewrites matching tool call
      payloads.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Move wire metadata handling into the record layer and keep persistence
      backends limited to storage operations.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 8-other-changes-in-kimi-code-0-2-0
  source_release: kimi-code-2026-05-26-0-2-0-3e226658
  source_type: kimi_code_changelog
  theme: uncategorized
  title: 8 other changes in Kimi Code 0.2.0
  type: change
source_release: '[[Releases/Kimi Code/kimi-code-2026-05-26-0-2-0-3e226658|kimi-code-2026-05-26-0-2-0-3e226658]]'
source_type: kimi_code_changelog
theme: uncategorized
title: 8 other changes in Kimi Code 0.2.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in Kimi Code 0.2.0

**Kimi Code** · 2026-05-26 · Other changes · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-05-26-0-2-0-3e226658|Kimi Code 0.2.0 (2026-05-26)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `Ctrl-J` as an additional shortcut for inserting new lines in the TUI prompt.

> Add wire record migration handling during session replay.

> Migrate user skills from `~/.kimi/skills/` to `~/.kimi-code/skills/` during the first-launch migration; existing target skills are kept.

> Correct the `X-Msh-Platform` header value to `kimi_code_cli`.

> Avoid CPU spikes from large streamed tool arguments and coalesce high-frequency streaming UI updates.

> Warn tmux users when extended key settings may prevent modified Enter shortcuts from working.

> Flatten tool call data by inlining tool names and arguments at the top level, and limit legacy record migration so it only rewrites matching tool call payloads.

> Move wire metadata handling into the record layer and keep persistence backends limited to storage operations.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-05-26-persist-model-selections-from-the-terminal-ui-to-the-default-configuration-and-h|Persist model selections from the terminal UI to the default configuration…]] · Developer Workflow
- [[Changes/Kimi Code/2026-05-26-2-context-window-changes-in-kimi-code-0-2-0|2 Context Window changes in Kimi Code 0.2.0]] · Context Window
- [[Changes/Kimi Code/2026-05-26-3-model-support-changes-in-kimi-code-0-2-0|3 Model Support changes in Kimi Code 0.2.0]] · Model Support
- [[Changes/Kimi Code/2026-05-26-4-account-and-access-changes-in-kimi-code-0-2-0|4 Account and Access changes in Kimi Code 0.2.0]] · Account and Access
- [[Changes/Kimi Code/2026-05-26-2-projects-and-workspaces-changes-in-kimi-code-0-2-0|2 Projects and Workspaces changes in Kimi Code 0.2.0]] · Projects and Workspaces
- [[Changes/Kimi Code/2026-05-26-hide-the-empty-current-session-from-the-sessions-picker-while-keeping-other-empt|Hide the empty current session from the sessions picker while keeping other empty…]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-05-26-75ef91&body=Card%3A%20Changes%2FKimi%20Code%2F2026-05-26-8-other-changes-in-kimi-code-0-2-0.md%0ACard%20ID%3A%20kimi-code-2026-05-26-75ef91%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->