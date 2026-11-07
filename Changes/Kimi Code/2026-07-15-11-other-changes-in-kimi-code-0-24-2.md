---
card_id: kimi-code-2026-07-15-c3b8ee
date: '2026-07-15'
description: 'Kimi Code · 2026-07-15 · Other changes: 11 changes in Kimi Code 0.24.2
  (2026-07-15) — Add a builtin `/check-kimi-code-docs` skill that automatically answers…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a67d68c5b6325daba2b287e65275240127acf1e9686d12c56a161b22ccf3f467
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-15-c3b8ee
  comparison: ''
  date: '2026-07-15'
  description: 'Kimi Code — Kimi Code 0.24.2 (2026-07-15): 11 other changes'
  evidence:
  - quote: Add a builtin `/check-kimi-code-docs` skill that automatically answers
      Kimi Code product questions with official-docs sources.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Align `kimi -p` behavior across engines: `print_background_mode` and `print_max_turns`
      now apply, and `/goal` runs stay alive until the goal finishes.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Workspaces now stay in sync: new sessions register automatically, missing
      workspaces are restored at startup, and removed ones stay removed.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: '`kimi web` now logs failed requests and key operations so daemon issues
      are easier to diagnose.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Minimized plan review and question cards now use an upward chevron
      for expand.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Show server error details when actions like stopping or archiving
      a session fail.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Keep loaded sessions visible when the session list fails to reload.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Restore the AgentSwarm member list after a page refresh.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'web: Show each message''s actual send time after reloading a session.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Correct the guidance shown when a goal cannot be paused or resumed.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Rename the dynamic tool loading capability from `select_tools` to `dynamically_loaded_tools`;
      behavior is unchanged.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 11-other-changes-in-kimi-code-0-24-2
  source_release: kimi-code-2026-07-15-0-24-2-2faa0103
  source_type: kimi_code_changelog
  theme: uncategorized
  title: 11 other changes in Kimi Code 0.24.2
  type: change
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-15-0-24-2-2faa0103|kimi-code-2026-07-15-0-24-2-2faa0103]]'
source_type: kimi_code_changelog
theme: uncategorized
title: 11 other changes in Kimi Code 0.24.2
type: change
---

<!-- chronolog:begin region="header" -->
# 11 other changes in Kimi Code 0.24.2

**Kimi Code** · 2026-07-15 · Other changes · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-15-0-24-2-2faa0103|Kimi Code 0.24.2 (2026-07-15)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add a builtin `/check-kimi-code-docs` skill that automatically answers Kimi Code product questions with official-docs sources.

> Align `kimi -p` behavior across engines: `print_background_mode` and `print_max_turns` now apply, and `/goal` runs stay alive until the goal finishes.

> Workspaces now stay in sync: new sessions register automatically, missing workspaces are restored at startup, and removed ones stay removed.

> `kimi web` now logs failed requests and key operations so daemon issues are easier to diagnose.

> web: Minimized plan review and question cards now use an upward chevron for expand.

> web: Show server error details when actions like stopping or archiving a session fail.

> web: Keep loaded sessions visible when the session list fails to reload.

> web: Restore the AgentSwarm member list after a page refresh.

> web: Show each message's actual send time after reloading a session.

> Correct the guidance shown when a goal cannot be paused or resumed.

> Rename the dynamic tool loading capability from `select_tools` to `dynamically_loaded_tools`; behavior is unchanged.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-15-kimi-p-now-stays-alive-by-default-while-background-tasks-are-pending-with-no-eff|kimi -p now stays alive by default while background tasks are pending, with no…]] · Interface Experience
- [[Changes/Kimi Code/2026-07-15-3-agent-mode-changes-in-kimi-code-0-24-2|3 Agent Mode changes in Kimi Code 0.24.2]] · Agent Mode
- [[Changes/Kimi Code/2026-07-15-the-per-step-llm-retry-limit-is-raised-from-3-to-10-attempts-so-transient-provid|The per-step LLM retry limit is raised from 3 to 10 attempts, so transient provider…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-15-c3b8ee&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-15-11-other-changes-in-kimi-code-0-24-2.md%0ACard%20ID%3A%20kimi-code-2026-07-15-c3b8ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->