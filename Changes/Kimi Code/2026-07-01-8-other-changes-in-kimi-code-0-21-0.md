---
card_id: kimi-code-2026-07-01-347c47
date: '2026-07-01'
description: 'Kimi Code · 2026-07-01 · Other changes: 8 changes in Kimi Code 0.21.0
  (2026-07-01) — Stop a malformed message history from permanently bricking a session
  on…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 09da7e24f100c31b0babdd69f853099d24b0c16a1ca249d0d979dc12601ee167
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-01-347c47
  comparison: ''
  date: '2026-07-01'
  description: 'Kimi Code — Kimi Code 0.21.0 (2026-07-01): 8 other changes'
  evidence:
  - quote: Stop a malformed message history from permanently bricking a session on
      strict providers (Anthropic). The request is repaired before sending — orphaned
      tool calls are closed and empty/whitespace-only text blocks dropped — and if
      the provider still rejects its structure, it is resent once with a wire-compliant
      rebuild.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Force-exit headless runs (`kimi -p`) so a stray ref'd handle left over
      from the run can't keep a completed run alive until an external timeout, and
      bound prompt cleanup so a wedged shutdown step can't hang shutdown.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add a double-Esc shortcut to open the undo selector. Press Esc twice while
      idle to undo.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Always show the usage-data opt-out toggle in the web settings with a clearer
      label and description.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Keep only recent user prompts plus a single user-role summary; drop assistant
      and tool messages.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Repair tool_use/tool_result adjacency before sending, fixing a strict-provider
      HTTP 400 when a tool call and its result became non-adjacent.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Refactor the thinking effort system
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add a server-side key-value store API for persisting web UI preferences
      to the user's data directory.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 8-other-changes-in-kimi-code-0-21-0
  source_release: kimi-code-2026-07-01-0-21-0-c7d001d2
  source_type: kimi_code_changelog
  theme: uncategorized
  title: 8 other changes in Kimi Code 0.21.0
  type: change
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-01-0-21-0-c7d001d2|kimi-code-2026-07-01-0-21-0-c7d001d2]]'
source_type: kimi_code_changelog
theme: uncategorized
title: 8 other changes in Kimi Code 0.21.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in Kimi Code 0.21.0

**Kimi Code** · 2026-07-01 · Other changes · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-01-0-21-0-c7d001d2|Kimi Code 0.21.0 (2026-07-01)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Stop a malformed message history from permanently bricking a session on strict providers (Anthropic). The request is repaired before sending — orphaned tool calls are closed and empty/whitespace-only text blocks dropped — and if the provider still rejects its structure, it is resent once with a wire-compliant rebuild.

> Force-exit headless runs (`kimi -p`) so a stray ref'd handle left over from the run can't keep a completed run alive until an external timeout, and bound prompt cleanup so a wedged shutdown step can't hang shutdown.

> Add a double-Esc shortcut to open the undo selector. Press Esc twice while idle to undo.

> Always show the usage-data opt-out toggle in the web settings with a clearer label and description.

> Keep only recent user prompts plus a single user-role summary; drop assistant and tool messages.

> Repair tool_use/tool_result adjacency before sending, fixing a strict-provider HTTP 400 when a tool call and its result became non-adjacent.

> Refactor the thinking effort system

> Add a server-side key-value store API for persisting web UI preferences to the user's data directory.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-01-merge-consecutive-user-turns-for-strict-providers-gemini-vertex-fixing-an-http-4|Merge consecutive user turns for strict providers (Gemini/Vertex), fixing an HTTP…]] · Model Support
- [[Changes/Kimi Code/2026-07-01-plugins-can-now-provide-slash-commands-via-a-commands-field-in-their-manifest-re|Plugins can now provide slash commands via a commands field in their manifest…]] · Apps and Integrations
- [[Changes/Kimi Code/2026-07-01-add-mermaid-diagram-rendering-to-the-web-chat-fenced-mermaid-blocks-in-assistant|Add Mermaid diagram rendering to the web chat]] · Interface Experience
- [[Changes/Kimi Code/2026-07-01-2-context-window-changes-in-kimi-code-0-21-0|2 Context Window changes in Kimi Code 0.21.0]] · Context Window
- [[Changes/Kimi Code/2026-07-01-show-file-path-completions-when-typing-in-shell-mode|Show file path completions when typing / in shell mode (!)]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-01-347c47&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-01-8-other-changes-in-kimi-code-0-21-0.md%0ACard%20ID%3A%20kimi-code-2026-07-01-347c47%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->