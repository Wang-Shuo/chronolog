---
card_id: codex-cli-2026-10-07-20e6ba
date: '2026-10-07'
description: 'Codex CLI · 2026-10-07 · Search and Browsing: 3 changes in 0.161.0 —
  Explicit launch permissions survive terminal reconnects and new sessions, while
  implicit…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1294
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ad7e00fb7e2469c65008170a7cebf7eddac6bee062dda2da9d4353c808e729e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-07-20e6ba
  comparison: ''
  date: '2026-10-07'
  description: 'Codex CLI — 0.161.0: 3 Search and Browsing changes'
  evidence:
  - quote: 'Explicit launch permissions survive terminal reconnects and new sessions,
      while implicit client settings no longer overwrite server or saved-thread web-search
      settings. (#49809, #49799)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49799 Preserve server web-search settings in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49946 Prevent stale file search results from being labeled with a new
      query @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-search-and-browsing-changes-in-rust-v0-161-0
  source_release: codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in rust-v0.161.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-01-improved-sdk-sessions-so-a-message-sent-with-priority-now-no-longer-cancels-a-ru|Improved
  SDK sessions so a message sent with priority "now" no longer cancels…]]'
- '[[Changes/Codex CLI/2026-10-01-browse-older-tasks-in-the-agent-command-center-with-a-keyboard-accessible-show-m|Browse
  older tasks in the agent command center with a keyboard-accessible…]]'
- '[[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed
  the interactive session''s WebSearch budget to refill over time (100 calls/hour]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in rust-v0.161.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in rust-v0.161.0

**Codex CLI** · 2026-10-07 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.161.0) · from [[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|0.161.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Explicit launch permissions survive terminal reconnects and new sessions, while implicit client settings no longer overwrite server or saved-thread web-search settings. (#49809, #49799)

> #49799 Preserve server web-search settings in the TUI @etraut-openai

> #49946 Prevent stale file search results from being labeled with a new query @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.161.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-07-10-developer-workflow-changes-in-rust-v0-161-0|10 Developer Workflow changes in rust-v0.161.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0|9 Safety and Privacy changes in rust-v0.161.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-07-5-apps-and-integrations-changes-in-rust-v0-161-0|5 Apps and Integrations changes in rust-v0.161.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-07-49856-support-daybreak-selection-in-codex-exec-etraut-openai|♯49856 Support Daybreak selection in codex exec @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]] · Model Support
- [[Changes/Codex CLI/2026-10-07-49876-remove-personality-plumbing-from-the-tui-etraut-openai|♯49876 Remove personality plumbing from the TUI @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-07-49473-use-the-rmcp-sdk-for-enterprise-managed-token-exchanges-nicksteele-oai|♯49473 Use the rmcp SDK for enterprise-managed token exchanges @nicksteele-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-10-07-10-account-and-access-changes-in-rust-v0-161-0|10 Account and Access changes in rust-v0.161.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-07-4-voice-and-audio-changes-in-rust-v0-161-0|4 Voice and Audio changes in rust-v0.161.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-07-9-context-window-changes-in-rust-v0-161-0|9 Context Window changes in rust-v0.161.0]] · Context Window
- [[Changes/Codex CLI/2026-10-07-2-collaboration-changes-in-rust-v0-161-0|2 Collaboration changes in rust-v0.161.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-07-93-other-changes-in-rust-v0-161-0|93 other changes in rust-v0.161.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed the interactive session's WebSearch budget to refill over time (100 calls/hour]]
- Later: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-07-20e6ba&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0.md%0ACard%20ID%3A%20codex-cli-2026-10-07-20e6ba%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.161.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->