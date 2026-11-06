---
card_id: codex-cli-2026-01-07-f60efc
date: '2026-01-07'
description: 'Codex CLI · 2026-01-07 · Search and Browsing: 4 changes in 0.79.0 —
  Add `web_search_cached` to enable cached-only Web Search results as a safer alternative
  to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1021
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b61d77ddfafd16b6684ffc557217a3a71c926f2f0b6b10cf6594760afcd8f84
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-07-f60efc
  comparison: ''
  date: '2026-01-07'
  description: 'Codex CLI — 0.79.0: 4 Search and Browsing changes'
  evidence:
  - quote: Add `web_search_cached` to enable cached-only Web Search results as a safer
      alternative to live requests (#8795)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: 'Reduce TUI UX glitches: suppress popups when browsing input history, fix
      copy “pill” rendering, and clear background terminals on interrupt (#8772, #8777,
      #8786)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8772 suppress popups while browsing input history @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8795 add web_search_cached flag @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-search-and-browsing-changes-in-rust-v0-79-0
  source_release: codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364
  source_type: github_releases
  theme: search-browsing
  title: 4 Search and Browsing changes in rust-v0.79.0
  type: change
related_changes:
- '[[Changes/Replit/2025-11-26-better-search-rankings-for-custom-domains|Better search
  rankings for Custom Domains]]'
- "[[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|\U0001F6E1️
  Web search domain filtering was corrected to properly block results when any…]]"
- '[[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search
  and Browsing changes in v0.6.42]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364|codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364]]'
source_type: github_releases
theme: search-browsing
title: 4 Search and Browsing changes in rust-v0.79.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in rust-v0.79.0

**Codex CLI** · 2026-01-07 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.79.0) · from [[Releases/Codex CLI/codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364|0.79.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `web_search_cached` to enable cached-only Web Search results as a safer alternative to live requests (#8795)

> Reduce TUI UX glitches: suppress popups when browsing input history, fix copy “pill” rendering, and clear background terminals on interrupt (#8772, #8777, #8786)

> #8772 suppress popups while browsing input history @xl-openai

> #8795 add web_search_cached flag @sayan-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.79.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-07-render-paths-relative-to-the-current-working-directory-before-checking-git-roots|Render paths relative to the current working directory before checking git roots…]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-07-4-agent-mode-changes-in-rust-v0-79-0|4 Agent Mode changes in rust-v0.79.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-07-allow-global-exec-flags-model-json-sandbox-toggles-etc-to-be-passed-after-codex|Allow global exec flags (model/json/sandbox toggles, etc.) to be passed after…]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-07-2-account-and-access-changes-in-rust-v0-79-0|2 Account and Access changes in rust-v0.79.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-07-3-model-support-changes-in-rust-v0-79-0|3 Model Support changes in rust-v0.79.0]] · Model Support
- [[Changes/Codex CLI/2026-01-07-add-app-server-thread-rollback-so-ide-clients-can-undo-the-last-n-turns-without|Add app-server thread/rollback so IDE clients can undo the last N turns without…]] · Editor Experience
- [[Changes/Codex CLI/2026-01-07-25-other-changes-in-rust-v0-79-0|25 other changes in rust-v0.79.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-12-21 · Open WebUI · [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]]
- Later: 2026-01-08 · v0 · [[Changes/v0/2026-01-08-improved-the-speed-and-token-use-of-the-web-search-tool|Improved the speed and token use of the Web Search tool]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-07-f60efc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-07-4-search-and-browsing-changes-in-rust-v0-79-0.md%0ACard%20ID%3A%20codex-cli-2026-01-07-f60efc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.79.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->