---
card_id: kimi-code-2026-06-29-467011
date: '2026-06-29'
description: 'Kimi Code · 2026-06-29 · Other changes: 8 changes in Kimi Code 0.20.2
  (2026-06-29) — Add an optional `exclude_empty` parameter to the session list API
  to omit…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aa76285dcdc6ca2a1f4b1c73691af7ae4f8ce2b97d287266d9b6e35256accb4c
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-06-29-467011
  comparison: ''
  date: '2026-06-29'
  description: 'Kimi Code — Kimi Code 0.20.2 (2026-06-29): 8 other changes'
  evidence:
  - quote: Add an optional `exclude_empty` parameter to the session list API to omit
      sessions that have no messages.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Keep unsent composer attachments scoped to their session in the web UI,
      so switching sessions no longer leaks them into another session's next message.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: In the bundled web UI, a new session is now created only when the first
      message is sent, so `+ New` without a workspace opens the composer instead of
      making an empty session.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Restore each session's scroll position when switching back to it in the
      web UI.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Keep the open side panel when switching between sessions in the web UI.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Hide unused "New Session" entries from the web session list by default.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Replace the web composer attach button's plus icon with an image icon.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add provider type and protocol attributes to turn and API error telemetry.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 8-other-changes-in-kimi-code-0-20-2
  source_release: kimi-code-2026-06-29-0-20-2-a1391f13
  source_type: kimi_code_changelog
  theme: uncategorized
  title: 8 other changes in Kimi Code 0.20.2
  type: change
source_release: '[[Releases/Kimi Code/kimi-code-2026-06-29-0-20-2-a1391f13|kimi-code-2026-06-29-0-20-2-a1391f13]]'
source_type: kimi_code_changelog
theme: uncategorized
title: 8 other changes in Kimi Code 0.20.2
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in Kimi Code 0.20.2

**Kimi Code** · 2026-06-29 · Other changes · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-06-29-0-20-2-a1391f13|Kimi Code 0.20.2 (2026-06-29)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add an optional `exclude_empty` parameter to the session list API to omit sessions that have no messages.

> Keep unsent composer attachments scoped to their session in the web UI, so switching sessions no longer leaks them into another session's next message.

> In the bundled web UI, a new session is now created only when the first message is sent, so `+ New` without a workspace opens the composer instead of making an empty session.

> Restore each session's scroll position when switching back to it in the web UI.

> Keep the open side panel when switching between sessions in the web UI.

> Hide unused "New Session" entries from the web session list by default.

> Replace the web composer attach button's plus icon with an image icon.

> Add provider type and protocol attributes to turn and API error telemetry.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-06-29-add-a-completion-sound-and-question-notifications-to-the-web-ui-with-separate-se|Add a completion sound and question notifications to the web UI, with separate…]] · Editor Experience
- [[Changes/Kimi Code/2026-06-29-upgrade-web-markdown-renderer-dependencies-katex-markstream-vue-shiki-for-bug-fi|Upgrade web markdown renderer dependencies (katex, markstream-vue, shiki) for bug…]] · Reliability and Performance
- [[Changes/Kimi Code/2026-06-29-route-kimi-code-models-on-the-anthropic-compatible-protocol-through-the-beta-mes|Route Kimi Code models on the Anthropic-compatible protocol through the beta Messages API]] · Model Support
- [[Changes/Kimi Code/2026-06-29-remove-the-sessions-slash-command-from-the-web-ui-the-sidebar-already-covers-ses|Remove the /sessions slash command from the web UI]] · Search and Browsing
- [[Changes/Kimi Code/2026-06-29-in-the-bundled-web-ui-new-and-clear-are-now-aliases-that-open-the-session-onboar|In the bundled web UI, /new and /clear are now aliases that open the session…]] · Mobile and Desktop
- [[Changes/Kimi Code/2026-06-29-2-context-window-changes-in-kimi-code-0-20-2|2 Context Window changes in Kimi Code 0.20.2]] · Context Window
- [[Changes/Kimi Code/2026-06-29-2-interface-experience-changes-in-kimi-code-0-20-2|2 Interface Experience changes in Kimi Code 0.20.2]] · Interface Experience
- [[Changes/Kimi Code/2026-06-29-add-kimi-code-custom-headers-for-custom-outbound-llm-request-headers-and-send-th|Add KIMI_CODE_CUSTOM_HEADERS for custom outbound LLM request headers, and send…]] · Agent Mode
- [[Changes/Kimi Code/2026-06-29-scope-the-web-composer-s-up-down-input-history-to-the-current-session-instead-of|Scope the web composer's up/down input history to the current session instead…]] · Collaboration
- [[Changes/Kimi Code/2026-06-29-support-the-anthropic-compatible-protocol-for-kimi-code-including-video-input|Support the Anthropic-compatible protocol for Kimi Code, including video input]] · Multimodal Input
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-06-29-467011&body=Card%3A%20Changes%2FKimi%20Code%2F2026-06-29-8-other-changes-in-kimi-code-0-20-2.md%0ACard%20ID%3A%20kimi-code-2026-06-29-467011%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->