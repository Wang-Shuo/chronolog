---
card_id: dify-2026-09-10-7b4dc7
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Collaboration: 3 changes in v1.17.1 - Bug Fixes
  and Improvements — The workflow canvas required a mouse to reposition anything.
  Nodes…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6cb7d9cf622690769e390c73be0623c6f6225c1db1dcee93d7b000b6da9d4aee
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-7b4dc7
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 3 Collaboration changes'
  evidence:
  - quote: The workflow canvas required a mouse to reposition anything. Nodes, multi-node
      selections, comment markers, and draft comments can now be moved with the arrow
      keys — hold Shift for larger steps — including Note, Iteration, and Loop nodes.
      Continuous movement is committed on key release or blur, so it produces one
      undo entry rather than one per keypress, and read-only mode, container boundaries,
      and collaboration updates are all still respected. (#41967)
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Large workflow graphs broke the collaboration socket.** `sync_request`
      payloads exceeded Engine.IO''s 1 MiB default, so the frame was rejected and
      the editor reconnect-looped. The ceiling is now configurable through `WEBSOCKET_MAX_HTTP_BUFFER_SIZE`,
      default 10 MiB. (#41347)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `WEBSOCKET_MAX_HTTP_BUFFER_SIZE` | `10485760` | Socket.IO frame ceiling
      for the collaboration WebSocket. Raise it if very large workflow graphs still
      fail to sync. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-collaboration-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: collaboration
  title: 3 Collaboration changes in 1.17.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-09-shared-folders-and-ownership|Shared folders and ownership]]'
- '[[Changes/ChatGPT/2026-09-09-library-sharing-lets-you-share-files-and-folders-in-chatgpt-choose-who-can-acces|Library
  sharing lets you share files and folders in ChatGPT, choose who can access…]]'
- '[[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration
  changes in rust-v0.154.0]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: collaboration
title: 3 Collaboration changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Collaboration changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The workflow canvas required a mouse to reposition anything. Nodes, multi-node selections, comment markers, and draft comments can now be moved with the arrow keys — hold Shift for larger steps — including Note, Iteration, and Loop nodes. Continuous movement is committed on key release or blur, so it produces one undo entry rather than one per keypress, and read-only mode, container boundaries, and collaboration updates are all still respected. (#41967)

> **Large workflow graphs broke the collaboration socket.** `sync_request` payloads exceeded Engine.IO's 1 MiB default, so the frame was rejected and the editor reconnect-looped. The ceiling is now configurable through `WEBSOCKET_MAX_HTTP_BUFFER_SIZE`, default 10 MiB. (#41347)

> | `WEBSOCKET_MAX_HTTP_BUFFER_SIZE` | `10485760` | Socket.IO frame ceiling for the collaboration WebSocket. Raise it if very large workflow graphs still fail to sync. |

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration changes in rust-v0.154.0]]
- Later: 2026-09-10 · v0 · [[Changes/v0/2026-09-10-new-chats-created-in-a-team-workspace-are-now-visible-to-the-team-by-default-mak|Team chats are easier to discover and collaborate on]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-7b4dc7&body=Card%3A%20Changes%2FDify%2F2026-09-10-3-collaboration-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-7b4dc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->