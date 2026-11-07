---
card_id: opencode-2026-10-27-5c0742
date: '2026-10-27'
description: 'OpenCode · 2026-10-27 · Memory and Personalization: 8 changes in v2.2.0
  — Core Reduce memory use when code search finds very large lines.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1195
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1461ec5d0c5112f18c29029273b19d967ef0b74e5197ffb011b5c37a8672d5b
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-27-5c0742
  comparison: ''
  date: '2026-10-27'
  description: 'OpenCode — v2.2.0: 8 Memory and Personalization changes'
  evidence:
  - quote: Core Reduce memory use when code search finds very large lines.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Move image resizing off the main process and release idle image memory.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Desktop Add opt-in memory logging and remote debugging for desktop debug
      builds.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Core Reduce memory retained by long-running tool calls and unchanged hooked
      model requests.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Terminal Release closed and background session transcripts to prevent memory
      growth.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: Desktop Reduce desktop memory use by releasing closed transcripts, discarded
      tool-result images, retained UI batches, and aborted timeline work.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: SDK Let SDK clients discard inline tool-result file payloads to reduce
      memory use.
    source_release: https://opencode.ai/changelog/v2.2.0
  - quote: SDK Release omitted tool-image payloads from memory instead of retaining
      their base64 data.
    source_release: https://opencode.ai/changelog/v2.2.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 8-memory-and-personalization-changes-in-v2-2-0
  source_release: opencode-2026-10-27-v2-2-0-f60b51f1
  source_type: opencode_changelog
  theme: memory
  title: 8 Memory and Personalization changes in v2.2.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-24-2-memory-and-personalization-changes-in-v2026-10-7|2
  Memory and Personalization changes in v2026.10.7]]'
- '[[Changes/Codex CLI/2026-10-27-5-memory-and-personalization-changes-in-rust-v0-165-0|5
  Memory and Personalization changes in rust-v0.165.0]]'
- '[[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4
  Memory and Personalization changes in v2026.10.8]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|opencode-2026-10-27-v2-2-0-f60b51f1]]'
source_type: opencode_changelog
theme: memory
title: 8 Memory and Personalization changes in v2.2.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Memory and Personalization changes in v2.2.0

**OpenCode** · 2026-10-27 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.0) · from [[Releases/OpenCode/opencode-2026-10-27-v2-2-0-f60b51f1|v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Reduce memory use when code search finds very large lines.

> Core Move image resizing off the main process and release idle image memory.

> Desktop Add opt-in memory logging and remote debugging for desktop debug builds.

> Core Reduce memory retained by long-running tool calls and unchanged hooked model requests.

> Terminal Release closed and background session transcripts to prevent memory growth.

> Desktop Reduce desktop memory use by releasing closed transcripts, discarded tool-result images, retained UI batches, and aborted timeline work.

> SDK Let SDK clients discard inline tool-result file payloads to reduce memory use.

> SDK Release omitted tool-image payloads from memory instead of retaining their base64 data.

Source: https://opencode.ai/changelog/v2.2.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-27-73-mobile-and-desktop-changes-in-v2-2-0|73 Mobile and Desktop changes in v2.2.0]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-13-model-support-changes-in-v2-2-0|13 Model Support changes in v2.2.0]] · Model Support
- [[Changes/OpenCode/2026-10-27-core-preserve-literal-0-and-arguments-text-in-custom-command-input|Core Preserve literal $0 and $ARGUMENTS text in custom command input]] · Pricing Model
- [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-2-search-and-browsing-changes-in-v2-2-0|2 Search and Browsing changes in v2.2.0]] · Search and Browsing
- [[Changes/OpenCode/2026-10-27-create-install-and-share-desktop-plugins-experimental|Create, install and share Desktop plugins (experimental)]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-10-interface-experience-changes-in-v2-2-0|10 Interface Experience changes in v2.2.0]] · Interface Experience
- [[Changes/OpenCode/2026-10-27-3-context-window-changes-in-v2-2-0|3 Context Window changes in v2.2.0]] · Context Window
- [[Changes/OpenCode/2026-10-27-restored-the-todo-tool-in-desktop-via-opt-in|Restored the Todo tool in desktop via opt-in]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-tui-plugins-require-opentui-0-7|TUI plugins require OpenTUI 0.7]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-14-apps-and-integrations-changes-in-v2-2-0|14 Apps and Integrations changes in v2.2.0]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-core-honor-shared-parallel-tool-call-and-service-tier-settings-for-groq|Core Honor shared parallel tool-call and service-tier settings for Groq]] · Collaboration
- [[Changes/OpenCode/2026-10-27-2-voice-and-audio-changes-in-v2-2-0|2 Voice and Audio changes in v2.2.0]] · Voice and Audio
- [[Changes/OpenCode/2026-10-27-refreshed-the-desktop-app-experience|Refreshed the desktop app experience]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-27-2-safety-and-privacy-changes-in-v2-2-0|2 Safety and Privacy changes in v2.2.0]] · Safety and Privacy
- [[Changes/OpenCode/2026-10-27-core-coordinate-oauth-credential-refreshes-across-locations-and-processes|Core Coordinate OAuth credential refreshes across locations and processes]] · Account and Access
- [[Changes/OpenCode/2026-10-27-5-editor-experience-changes-in-v2-2-0|5 Editor Experience changes in v2.2.0]] · Editor Experience
- [[Changes/OpenCode/2026-10-27-plugins-can-now-attach-and-update-keyed-session-instructions-with-ctx-session-in|Plugins can now attach and update keyed session instructions…]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add configurable prompt cache TTLs per provider/model]] · Model Support
- [[Changes/OpenCode/2026-10-27-2-agent-mode-changes-in-v2-2-0|2 Agent Mode changes in v2.2.0]] · Agent Mode
- [[Changes/OpenCode/2026-10-27-3-projects-and-workspaces-changes-in-v2-2-0|3 Projects and Workspaces changes in v2.2.0]] · Projects and Workspaces
- [[Changes/OpenCode/2026-10-27-opencode-ai-root-is-now-the-promise-api|opencode/ai root is now the Promise API]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-27-13-developer-workflow-changes-in-v2-2-0|13 Developer Workflow changes in v2.2.0]] · Developer Workflow
- [[Changes/OpenCode/2026-10-27-6-reliability-and-performance-changes-in-v2-2-0|6 Reliability and Performance changes in v2.2.0]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-27-31-other-changes-in-v2-2-0|31 other changes in v2.2.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-27 · OpenClaw · [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]]
- Later: 2026-10-29 · Codex CLI · [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-27-5c0742&body=Card%3A%20Changes%2FOpenCode%2F2026-10-27-8-memory-and-personalization-changes-in-v2-2-0.md%0ACard%20ID%3A%20opencode-2026-10-27-5c0742%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->