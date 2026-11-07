---
card_id: codex-cli-2026-05-26-6e9456
date: '2026-05-26'
description: 'Codex CLI · 2026-05-26 · Apps and Integrations: 11 changes in 0.134.0
  — Made connector tool schemas more reliable by preserving local `$ref`/`$defs` structures…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2720
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eaebea3b7311cf5ee9eec2e84f165bf61f00e2316e340157d86edd68ebe58988
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-26-6e9456
  comparison: ''
  date: '2026-05-26'
  description: 'Codex CLI — 0.134.0: 11 Apps and Integrations changes'
  evidence:
  - quote: 'Made connector tool schemas more reliable by preserving local `$ref`/`$defs`
      structures and compacting oversized schemas before exposure. (#23357, #23904)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Let read-only MCP tools run concurrently when they advertise `readOnlyHint`.
      (#23750)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: 'Improved remote reliability by reconnecting stale exec-server websocket
      clients, retrying remote control immediately after auth recovery, and retrying
      remote compaction v2 streams. (#23867, #23775, #23951)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Allowed plugin skills to reuse shared plugin-level icon assets. (#23776)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: 'Added image re-encoding benchmarks and connector-style JSON schema policy
      fixtures. (#23935, #24152)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23583 Route MCP servers through explicit environments @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#22552 Remove plugin hooks feature flag @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23775 fix(remote-control): retry after auth recovery @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23776 fix: Allow plugin skills to share plugin-level icon assets @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23750 Allow parallel MCP tool calls when annotated readOnly @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23890 mcp: surface profile migration guidance under --profile @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-apps-and-integrations-changes-in-rust-v0-134-0
  source_release: codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in rust-v0.134.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-05-25-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-05-25-sdk-releases|SDK Releases]]'
- '[[Changes/Lovable/2026-05-25-custom-mcp-servers-available-on-all-plans|Custom MCP
  servers available on all plans]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in rust-v0.134.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in rust-v0.134.0

**Codex CLI** · 2026-05-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.134.0) · from [[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Made connector tool schemas more reliable by preserving local `$ref`/`$defs` structures and compacting oversized schemas before exposure. (#23357, #23904)

> Let read-only MCP tools run concurrently when they advertise `readOnlyHint`. (#23750)

> Improved remote reliability by reconnecting stale exec-server websocket clients, retrying remote control immediately after auth recovery, and retrying remote compaction v2 streams. (#23867, #23775, #23951)

> Allowed plugin skills to reuse shared plugin-level icon assets. (#23776)

> Added image re-encoding benchmarks and connector-style JSON schema policy fixtures. (#23935, #24152)

> #23583 Route MCP servers through explicit environments @starr-openai

> #22552 Remove plugin hooks feature flag @abhinav-oai

> #23775 fix(remote-control): retry after auth recovery @apanasenko-oai

> #23776 fix: Allow plugin skills to share plugin-level icon assets @xl-openai

> #23750 Allow parallel MCP tool calls when annotated readOnly @anp-oai

> #23890 mcp: surface profile migration guidance under --profile @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.134.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-26-3-agent-mode-changes-in-rust-v0-134-0|3 Agent Mode changes in rust-v0.134.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915 3 of 4 tui: route feature and memory toggles through app server @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-26-23736-add-new-enterprise-requirement-gate-adams-oai|♯23736 Add new enterprise requirement gate @adams-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-05-26-5-context-window-changes-in-rust-v0-134-0|5 Context Window changes in rust-v0.134.0]] · Context Window
- [[Changes/Codex CLI/2026-05-26-2-account-and-access-changes-in-rust-v0-134-0|2 Account and Access changes in rust-v0.134.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0|7 Safety and Privacy changes in rust-v0.134.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-26-2-mobile-and-desktop-changes-in-rust-v0-134-0|2 Mobile and Desktop changes in rust-v0.134.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-26-47-other-changes-in-rust-v0-134-0|47 other changes in rust-v0.134.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-25 · Lovable · [[Changes/Lovable/2026-05-25-custom-mcp-servers-available-on-all-plans|Custom MCP servers available on all plans]]
- Later: 2026-05-27 · Claude Code · [[Changes/Claude Code/2026-05-27-4-apps-and-integrations-changes-in-v2-1-152|4 Apps and Integrations changes in v2.1.152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-26-6e9456&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0.md%0ACard%20ID%3A%20codex-cli-2026-05-26-6e9456%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.134.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->