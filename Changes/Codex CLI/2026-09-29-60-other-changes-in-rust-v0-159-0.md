---
card_id: codex-cli-2026-09-29-8c29eb
date: '2026-09-29'
description: 'Codex CLI · 2026-09-29 · Other changes: 60 changes in 0.159.0 — New
  sessions get a compact welcome screen and consistent headers, with occasional tips
  during…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d39f5905707811fa7ed2bb5e987915581816b85025a4e170878741712b2b46b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-29-8c29eb
  comparison: ''
  date: '2026-09-29'
  description: 'Codex CLI — 0.159.0: 60 other changes'
  evidence:
  - quote: 'New sessions get a compact welcome screen and consistent headers, with
      occasional tips during and after turns. (#48513, #48562, #48352)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: 'The warnings viewer dismisses reviewed warnings when closed; press `k`
      to keep one for later. (#48205, #48206)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: You can scroll the transcript while deciding whether to implement a plan.
      (#48805)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: App-server clients can paginate thread history from a specific item. (#48151)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: 'Blank sessions retain drafts when switching tasks, and threads can be
      archived and listed before their first turn. (#48628, #48828, #48199)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: 'Approved commands retain explicit filesystem denials, and `.aws` directories
      are protected by default under writable roots. (#48155, #48176)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: Removed automatic follow-up prompt suggestions and the `tui.prompt_suggestions`
      setting. (#48621)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48135 Add opt-in code-mode yielding on new user input @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48151 Add item anchors to `thread/items/list` pagination @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48155 Preserve filesystem denials when preparing approved commands @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48157 Allow Windows daemon launches with residual job membership @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48168 Generate unique exec-server process IDs for every request @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48197 Optimize `blake3` in Bazel fastbuilds @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48198 Honor execution environment proxy requirements @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48199 Keep archived threads with empty previews visible in listings @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48205 Dismiss viewed TUI warnings when closing the viewer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48206 Add a keep-and-next action to the warnings viewer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48207 Preserve queued output for observers during code-mode termination
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48213 Isolate executable fixture copies in CLI tests on Linux @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48222 Preserve late result metadata for truncated code-mode calls @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48229 Extract Responses failure parsing into a dedicated module @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48272 Prevent Windows daemon launches from retaining launcher stdio @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48344 Preserve tool metadata for OpenAI provider endpoint overrides @peilin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48350 Display reconnect commands on a separate line @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48353 Stabilize skill catalogs across executor availability changes @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48469 Default to copying transcript selections in more terminals @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48483 Prevent console windows for piped Windows child processes @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48489 Fix Mermaid shape, relationship, and state description parsing
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48491 Fall back to embedded mode under restrictive Windows launchers
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48508 Preserve WebSocket continuations when steering a turn @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48513 Refresh the TUI welcome screen for new sessions @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48547 Fade blossom replays back to the idle state @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48549 Preserve Markdown tables and whitespace when copying TUI responses
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48560 Keep working tips stable during transcript interaction @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48562 Use a consistent borderless session header in the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48568 Allow exec-server to proxy permitted private IPs upstream @open-matt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48574 Preserve deferred tool namespace names before descriptions @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48575 Allow provisioned executors more time to come online @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48611 Centralize persistent mode enablement checks @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48621 Remove follow-up prompt suggestions from the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48623 Preserve empty Markdown list markers in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48626 Stop showing previous-session summaries when switching TUI sessions
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48628 Preserve blank TUI sessions when switching tasks @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48686 Remove WebSocket headers and tool payloads from info logs @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48725 Retain confirmed Code Mode messages for Guardian reviews @ankushg'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48727 Centralize executable fixture creation to avoid Linux ETXTBSY races
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48754 Render `/status` without borders and wrap long values @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48772 Fix Unix socket connections through long symlink paths @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48775 Match pinned transcript headers to the original prompt style @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48776 Remove the `current` badge from TUI task rows @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48796 Add opt-in structured errors for Guardian circuit-breaker interruptions
      @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48805 Allow transcript wheel scrolling while a modal is open @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48812 Add history-aware prewarming for idle threads @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48814 Preserve punctuation and semicolons in Mermaid labels @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48827 Show a hand pointer over transcript links in Ghostty and Kitty
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48828 Allow archiving threads before their first turn @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48830 Show a short, neutral TUI interruption notice @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48895 Expand native Mermaid flowchart syntax support @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48973 Isolate realtime auth fallback test from startup prewarm @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  - quote: '#48982 Prevent message-board notifications from reopening final answers
      @eknight-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.159.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 60-other-changes-in-rust-v0-159-0
  source_release: codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516
  source_type: github_releases
  theme: uncategorized
  title: 60 other changes in rust-v0.159.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516|codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516]]'
source_type: github_releases
theme: uncategorized
title: 60 other changes in rust-v0.159.0
type: change
---

<!-- chronolog:begin region="header" -->
# 60 other changes in rust-v0.159.0

**Codex CLI** · 2026-09-29 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.159.0) · from [[Releases/Codex CLI/codex-cli-2026-09-29-rust-v0-159-0-github-398926954-1ffcd516|0.159.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New sessions get a compact welcome screen and consistent headers, with occasional tips during and after turns. (#48513, #48562, #48352)

> The warnings viewer dismisses reviewed warnings when closed; press `k` to keep one for later. (#48205, #48206)

> You can scroll the transcript while deciding whether to implement a plan. (#48805)

> App-server clients can paginate thread history from a specific item. (#48151)

> Blank sessions retain drafts when switching tasks, and threads can be archived and listed before their first turn. (#48628, #48828, #48199)

> Approved commands retain explicit filesystem denials, and `.aws` directories are protected by default under writable roots. (#48155, #48176)

> Removed automatic follow-up prompt suggestions and the `tui.prompt_suggestions` setting. (#48621)

> #48135 Add opt-in code-mode yielding on new user input @pakrym-oai

> #48151 Add item anchors to `thread/items/list` pagination @btraut-openai

> #48155 Preserve filesystem denials when preparing approved commands @viyatb-oai

> #48157 Allow Windows daemon launches with residual job membership @etraut-openai

> #48168 Generate unique exec-server process IDs for every request @sdcoffey

> #48197 Optimize `blake3` in Bazel fastbuilds @jif-oai

> #48198 Honor execution environment proxy requirements @seanh-oai

> #48199 Keep archived threads with empty previews visible in listings @acrognale-oai

> #48205 Dismiss viewed TUI warnings when closing the viewer @fcoury-oai

> #48206 Add a keep-and-next action to the warnings viewer @fcoury-oai

> #48207 Preserve queued output for observers during code-mode termination @pakrym-oai

> #48213 Isolate executable fixture copies in CLI tests on Linux @jif-oai

> #48222 Preserve late result metadata for truncated code-mode calls @ningyi-oai

> #48229 Extract Responses failure parsing into a dedicated module @anp-oai

> #48272 Prevent Windows daemon launches from retaining launcher stdio @zm-oai

> #48344 Preserve tool metadata for OpenAI provider endpoint overrides @peilin-openai

> #48350 Display reconnect commands on a separate line @etraut-openai

> #48353 Stabilize skill catalogs across executor availability changes @vkg-oai

> #48469 Default to copying transcript selections in more terminals @fcoury-oai

> #48483 Prevent console windows for piped Windows child processes @fcoury-oai

> #48489 Fix Mermaid shape, relationship, and state description parsing @etraut-openai

> #48491 Fall back to embedded mode under restrictive Windows launchers @fcoury-oai

> #48508 Preserve WebSocket continuations when steering a turn @pakrym-oai

> #48513 Refresh the TUI welcome screen for new sessions @fcoury-oai

> #48547 Fade blossom replays back to the idle state @fcoury-oai

> #48549 Preserve Markdown tables and whitespace when copying TUI responses @fcoury-oai

> #48560 Keep working tips stable during transcript interaction @fcoury-oai

> #48562 Use a consistent borderless session header in the TUI @fcoury-oai

> #48568 Allow exec-server to proxy permitted private IPs upstream @open-matt

> #48574 Preserve deferred tool namespace names before descriptions @adaley-openai

> #48575 Allow provisioned executors more time to come online @richardopenai

> #48611 Centralize persistent mode enablement checks @alishobeiri-oai

> #48621 Remove follow-up prompt suggestions from the TUI @etraut-openai

> #48623 Preserve empty Markdown list markers in the TUI @etraut-openai

> #48626 Stop showing previous-session summaries when switching TUI sessions @etraut-openai

> #48628 Preserve blank TUI sessions when switching tasks @etraut-openai

> #48686 Remove WebSocket headers and tool payloads from info logs @chess-oai

> #48725 Retain confirmed Code Mode messages for Guardian reviews @ankushg

> #48727 Centralize executable fixture creation to avoid Linux ETXTBSY races @jif-oai

> #48754 Render `/status` without borders and wrap long values @fcoury-oai

> #48772 Fix Unix socket connections through long symlink paths @etraut-openai

> #48775 Match pinned transcript headers to the original prompt style @etraut-openai

> #48776 Remove the `current` badge from TUI task rows @etraut-openai

> #48796 Add opt-in structured errors for Guardian circuit-breaker interruptions @won-openai

> #48805 Allow transcript wheel scrolling while a modal is open @fcoury-oai

> #48812 Add history-aware prewarming for idle threads @vkg-oai

> #48814 Preserve punctuation and semicolons in Mermaid labels @etraut-openai

> #48827 Show a hand pointer over transcript links in Ghostty and Kitty @bc-openai

> #48828 Allow archiving threads before their first turn @bc-openai

> #48830 Show a short, neutral TUI interruption notice @fcoury-oai

> #48895 Expand native Mermaid flowchart syntax support @etraut-openai

> #48973 Isolate realtime auth fallback test from startup prewarm @jif-oai

> #48982 Prevent message-board notifications from reopening final answers @eknight-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.159.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-29-3-model-support-changes-in-rust-v0-159-0|3 Model Support changes in rust-v0.159.0]] · Model Support
- [[Changes/Codex CLI/2026-09-29-3-account-and-access-changes-in-rust-v0-159-0|3 Account and Access changes in rust-v0.159.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-29-48824-keep-voice-rtp-timestamps-aligned-to-20-ms-packets-bc-openai|♯48824 Keep voice RTP timestamps aligned to 20 ms packets @bc-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-29-4-interface-experience-changes-in-rust-v0-159-0|4 Interface Experience changes in rust-v0.159.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-29-3-safety-and-privacy-changes-in-rust-v0-159-0|3 Safety and Privacy changes in rust-v0.159.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-29-4-mobile-and-desktop-changes-in-rust-v0-159-0|4 Mobile and Desktop changes in rust-v0.159.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-29-3-editor-experience-changes-in-rust-v0-159-0|3 Editor Experience changes in rust-v0.159.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-29-8-apps-and-integrations-changes-in-rust-v0-159-0|8 Apps and Integrations changes in rust-v0.159.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-29-5-developer-workflow-changes-in-rust-v0-159-0|5 Developer Workflow changes in rust-v0.159.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-29-2-collaboration-changes-in-rust-v0-159-0|2 Collaboration changes in rust-v0.159.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-29-4-context-window-changes-in-rust-v0-159-0|4 Context Window changes in rust-v0.159.0]] · Context Window
- [[Changes/Codex CLI/2026-09-29-48190-bound-agent-message-board-sse-frames-before-parsing-jif-oai|♯48190 Bound agent message board SSE frames before parsing @jif-oai]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-29-8c29eb&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-29-60-other-changes-in-rust-v0-159-0.md%0ACard%20ID%3A%20codex-cli-2026-09-29-8c29eb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.159.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->