---
card_id: codex-cli-2026-01-27-01b5a1
date: '2026-01-27'
description: 'Codex CLI · 2026-01-27 · Search and Browsing: 5 changes in 0.92.0 —
  Added filtering on the thread list in the app server to make large thread sets easier
  to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 54e83d32905b75de99ae40f2eeb2fe5ab1e0a4f9d3b188ff32ae36011f03e80a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-27-01b5a1
  comparison: ''
  date: '2026-01-27'
  description: 'Codex CLI — 0.92.0: 5 Search and Browsing changes'
  evidence:
  - quote: Added filtering on the thread list in the app server to make large thread
      sets easier to browse. (#9897)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: Cached `web_search` is now the default client behavior. (#9974)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: The `web_search` tool now handles and displays all action types, and shows
      in-progress activity instead of appearing stuck. (#9960)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9960 fix: handle all web_search actions and in progress invocations @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9974 make cached web_search client-side default @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-search-and-browsing-changes-in-rust-v0-92-0
  source_release: codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c
  source_type: github_releases
  theme: search-browsing
  title: 5 Search and Browsing changes in rust-v0.92.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search
  and Browsing changes in v0.7.0]]'
- '[[Changes/Codex CLI/2026-01-16-2-search-and-browsing-changes-in-rust-v0-86-0|2
  Search and Browsing changes in rust-v0.86.0]]'
- '[[Changes/Cursor/2026-01-16-added-webfetch-websearch-tools-approval-options-for-granular-controls-over-web-s|Added
  WebFetch, WebSearch tools, & approval options for granular controls over web…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c|codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c]]'
source_type: github_releases
theme: search-browsing
title: 5 Search and Browsing changes in rust-v0.92.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Search and Browsing changes in rust-v0.92.0

**Codex CLI** · 2026-01-27 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.92.0) · from [[Releases/Codex CLI/codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c|0.92.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added filtering on the thread list in the app server to make large thread sets easier to browse. (#9897)

> Cached `web_search` is now the default client behavior. (#9974)

> The `web_search` tool now handles and displays all action types, and shows in-progress activity instead of appearing stuck. (#9960)

> #9960 fix: handle all web_search actions and in progress invocations @sayan-oai

> #9974 make cached web_search client-side default @sayan-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.92.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-27-9818-feat-rebase-multi-agent-tui-on-config-snapshot-jif-oai|♯9818 feat: rebase multi-agent tui on config_snapshot @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-27-refreshed-protocol-mcp-docs-to-reflect-thread-unarchive-and-the-updated-request|Refreshed protocol/MCP docs to reflect thread/unarchive and the updated…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-27-3-interface-experience-changes-in-rust-v0-92-0|3 Interface Experience changes in rust-v0.92.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-27-2-developer-workflow-changes-in-rust-v0-92-0|2 Developer Workflow changes in rust-v0.92.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-27-2-safety-and-privacy-changes-in-rust-v0-92-0|2 Safety and Privacy changes in rust-v0.92.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-27-2-account-and-access-changes-in-rust-v0-92-0|2 Account and Access changes in rust-v0.92.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-27-2-collaboration-changes-in-rust-v0-92-0|2 Collaboration changes in rust-v0.92.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-27-9718-feat-tui-personality-dylan-hurd-oai|♯9718 feat(tui) /personality @dylan-hurd-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-27-2-model-support-changes-in-rust-v0-92-0|2 Model Support changes in rust-v0.92.0]] · Model Support
- [[Changes/Codex CLI/2026-01-27-48-other-changes-in-rust-v0-92-0|48 other changes in rust-v0.92.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-01-16 · Cursor · [[Changes/Cursor/2026-01-16-added-webfetch-websearch-tools-approval-options-for-granular-controls-over-web-s|Added WebFetch, WebSearch tools, & approval options for granular controls over web…]]
- Later: 2026-01-28 · Gemini · [[Changes/Gemini/2026-01-28-meet-your-new-ai-browsing-assistant-gemini-in-chrome|Meet your new AI browsing assistant: Gemini in Chrome]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-27-01b5a1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-27-5-search-and-browsing-changes-in-rust-v0-92-0.md%0ACard%20ID%3A%20codex-cli-2026-01-27-01b5a1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.92.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->