---
card_id: open-webui-2026-08-25-c20f18
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Memory and Personalization: 8 changes in v0.11.1
  — \U0001F4F6 **Streaming rebuilt from the ground up.** A reply now streams as small
  pieces of…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13b28aa3862b2494257b30375ca762762c9c4fdb739dc491f5b76cf1cf4599c9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-c20f18
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 8 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F4F6 **Streaming rebuilt from the ground up.** A reply now streams
      as small pieces of new text instead of resending the whole message so far with
      every update, so the data sent over a reply grows with its length rather than
      with its length squared, which on a server with many people chatting at once
      means far less processor time spent encoding, passing, and decoding those updates,
      far less load and memory on the shared cache that carries them between instances,
      and far less work in your browser, which no longer takes in the whole reply
      again and redraws the parts of it that have not changed on every update, cutting
      the data sent and the server work spent appending to a message by up to 1000x
      on a very long reply, and a reply still in progress is now kept aside on the
      server, so reopening the conversation after a refresh picks it up where it is
      rather than showing a blank message, on deployments backed by Redis. [Commit](https://github.com/open-webui/open-webui/commit/a1579a01ff43cacb357269707d36267ad35e01d6),
      [Commit](https://github.com/open-webui/open-webui/commit/c755ef60c6bd47ea25306bd898d9a6d1bd8e871d),
      [Commit](https://github.com/open-webui/open-webui/commit/d02b6a21fc02fb073782e25356968cfee3c45c36),
      [Commit](https://github.com/open-webui/open-webui/commit/3e186abdd91edee9e97e43c9b345714643a84cf5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F975 **Constant load on an idle instance.** An instance sitting
      idle no longer works through every chat you have once a second looking for timers
      that are due, which on a large history kept about a quarter of a processor core
      busy doing nothing and could exhaust memory until the application was killed.
      [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622),
      [#27745](https://github.com/open-webui/open-webui/issues/27745)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9FA **Leaner stored document metadata.** Bulky extraction details
      such as page layouts, tables and detected languages are no longer kept alongside
      a document in the vector store, and a new \"RAG_METADATA_MAX_VALUE_CHARS\" setting
      drops any remaining oversized value, falling back to the configured upload size
      limit so a document that expands enormously while being read cannot exhaust
      a server's memory. [Commit](https://github.com/open-webui/open-webui/commit/278e97589e71d119b887d5bca9d6ae32912d1dff),
      [Commit](https://github.com/open-webui/open-webui/commit/e3a7a64d82ab2dd06c681ce85027367ccc8234d4),
      [#29025](https://github.com/open-webui/open-webui/pull/29025)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4A3 **Documents that unpack far beyond their size.** A Word, Excel,
      PowerPoint, OpenDocument or EPUB file that expands to far more than it stores
      is now rejected before it is read, where one could previously be used to exhaust
      a server's memory. [Commit](https://github.com/open-webui/open-webui/commit/2a0274a0a039dbe0a1ad4d24003b085aae7b896b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F333 **Folders disappearing when moved into themselves.** Moving
      a folder inside one of its own subfolders is now refused, where it was accepted
      and made that folder and everything in it vanish from the sidebar with no way
      to bring it back, while leaving the server walking the loop endlessly and querying
      the database as it went, which could exhaust a worker and its memory; any folder
      already in that state is returned to the top level. [#28748](https://github.com/open-webui/open-webui/pull/28748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4A7 **Attaching a very large file from a link.** A file fetched
      from a link is now written to disk as it arrives and stops at the configured
      size limit, where the whole thing was held in memory first with no limit applied,
      so a large enough file could exhaust the server; a download that fails partway
      no longer leaves the partial file behind. [#28945](https://github.com/open-webui/open-webui/pull/28945)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5EF️ **Losing the conversation with memory on.** With the memory
      tool enabled, the model can see the earlier messages in your conversation again,
      instead of answering the second message as though the first had never been sent.
      [#28400](https://github.com/open-webui/open-webui/issues/28400)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9E0 **Faster follow-ups with memory enabled.** The memories handed
      to the model now appear in a stable order from one message to the next, so servers
      that reuse their work between turns no longer reprocess the whole conversation
      each time you reply. [#28292](https://github.com/open-webui/open-webui/issues/28292),
      [Commit](https://github.com/open-webui/open-webui/commit/ff74bfa6a117c6f03097034c74c2f9bdfb824203),
      [Commit](https://github.com/open-webui/open-webui/commit/d22bb6703f244e6769ac9b0f2e41d784ad6cf535)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-memory-and-personalization-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: memory
  title: 8 Memory and Personalization changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2
  Memory and Personalization changes in rust-v0.149.0]]'
- '[[Changes/Midjourney/2026-08-21-settings|Settings]]'
- '[[Changes/Claude/2026-08-25-memory-in-claude-cowork-editable-topics-and-a-sensitive-topics-setting|Memory
  in Claude Cowork, editable topics, and a sensitive topics setting]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: memory
title: 8 Memory and Personalization changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Memory and Personalization changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📶 **Streaming rebuilt from the ground up.** A reply now streams as small pieces of new text instead of resending the whole message so far with every update, so the data sent over a reply grows with its length rather than with its length squared, which on a server with many people chatting at once means far less processor time spent encoding, passing, and decoding those updates, far less load and memory on the shared cache that carries them between instances, and far less work in your browser, which no longer takes in the whole reply again and redraws the parts of it that have not changed on every update, cutting the data sent and the server work spent appending to a message by up to 1000x on a very long reply, and a reply still in progress is now kept aside on the server, so reopening the conversation after a refresh picks it up where it is rather than showing a blank message, on deployments backed by Redis. [Commit](https://github.com/open-webui/open-webui/commit/a1579a01ff43cacb357269707d36267ad35e01d6), [Commit](https://github.com/open-webui/open-webui/commit/c755ef60c6bd47ea25306bd898d9a6d1bd8e871d), [Commit](https://github.com/open-webui/open-webui/commit/d02b6a21fc02fb073782e25356968cfee3c45c36), [Commit](https://github.com/open-webui/open-webui/commit/3e186abdd91edee9e97e43c9b345714643a84cf5)

> 🥵 **Constant load on an idle instance.** An instance sitting idle no longer works through every chat you have once a second looking for timers that are due, which on a large history kept about a quarter of a processor core busy doing nothing and could exhaust memory until the application was killed. [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622), [#27745](https://github.com/open-webui/open-webui/issues/27745)

> 🧺 **Leaner stored document metadata.** Bulky extraction details such as page layouts, tables and detected languages are no longer kept alongside a document in the vector store, and a new "RAG_METADATA_MAX_VALUE_CHARS" setting drops any remaining oversized value, falling back to the configured upload size limit so a document that expands enormously while being read cannot exhaust a server's memory. [Commit](https://github.com/open-webui/open-webui/commit/278e97589e71d119b887d5bca9d6ae32912d1dff), [Commit](https://github.com/open-webui/open-webui/commit/e3a7a64d82ab2dd06c681ce85027367ccc8234d4), [#29025](https://github.com/open-webui/open-webui/pull/29025)

> 💣 **Documents that unpack far beyond their size.** A Word, Excel, PowerPoint, OpenDocument or EPUB file that expands to far more than it stores is now rejected before it is read, where one could previously be used to exhaust a server's memory. [Commit](https://github.com/open-webui/open-webui/commit/2a0274a0a039dbe0a1ad4d24003b085aae7b896b)

> 🌳 **Folders disappearing when moved into themselves.** Moving a folder inside one of its own subfolders is now refused, where it was accepted and made that folder and everything in it vanish from the sidebar with no way to bring it back, while leaving the server walking the loop endlessly and querying the database as it went, which could exhaust a worker and its memory; any folder already in that state is returned to the top level. [#28748](https://github.com/open-webui/open-webui/pull/28748)

> 💧 **Attaching a very large file from a link.** A file fetched from a link is now written to disk as it arrives and stops at the configured size limit, where the whole thing was held in memory first with no limit applied, so a large enough file could exhaust the server; a download that fails partway no longer leaves the partial file behind. [#28945](https://github.com/open-webui/open-webui/pull/28945)

> 🗯️ **Losing the conversation with memory on.** With the memory tool enabled, the model can see the earlier messages in your conversation again, instead of answering the second message as though the first had never been sent. [#28400](https://github.com/open-webui/open-webui/issues/28400)

> 🧠 **Faster follow-ups with memory enabled.** The memories handed to the model now appear in a stable order from one message to the next, so servers that reuse their work between turns no longer reprocess the whole conversation each time you reply. [#28292](https://github.com/open-webui/open-webui/issues/28292), [Commit](https://github.com/open-webui/open-webui/commit/ff74bfa6a117c6f03097034c74c2f9bdfb824203), [Commit](https://github.com/open-webui/open-webui/commit/d22bb6703f244e6769ac9b0f2e41d784ad6cf535)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-08-25 · Claude · [[Changes/Claude/2026-08-25-memory-in-claude-cowork-editable-topics-and-a-sensitive-topics-setting|Memory in Claude Cowork, editable topics, and a sensitive topics setting]]
- Later: 2026-08-26 · Codex CLI · [[Changes/Codex CLI/2026-08-26-3-memory-and-personalization-changes-in-rust-v0-150-0|3 Memory and Personalization changes in rust-v0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-c20f18&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-8-memory-and-personalization-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-c20f18%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->