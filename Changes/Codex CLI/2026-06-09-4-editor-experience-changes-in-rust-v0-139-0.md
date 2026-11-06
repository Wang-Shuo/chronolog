---
card_id: codex-cli-2026-06-09-fc1589
date: '2026-06-09'
description: 'Codex CLI · 2026-06-09 · Editor Experience: 4 changes in 0.139.0 — `codex
  doctor` now includes editor and pager environment details in the local report while…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1183
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d8f76b976b4c31f13394c6858851eb0c492bc15b6b8f5a9261c397eefb781657
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-09-fc1589
  comparison: ''
  date: '2026-06-09'
  description: 'Codex CLI — 0.139.0: 4 Editor Experience changes'
  evidence:
  - quote: '`codex doctor` now includes editor and pager environment details in the
      local report while redacting raw values in JSON output. (#27081)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: Image edits now use the exact referenced image file paths instead of guessing
      from conversation history, so attached-image edits land on the intended input.
      (#26486)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26486 Route image edits through referenced file paths @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27081 feat(doctor): report editor and pager environment @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-editor-experience-changes-in-rust-v0-139-0
  source_release: codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in rust-v0.139.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-08-edit-messages-with-attachments-you-can-now-edit-messages-that-include-attachment|Edit
  messages with attachments]]'
- '[[Changes/Claude Code/2026-06-08-background-sessions-now-preserve-ide-chrome-bare-remote-control-and-other-flags|Background
  sessions now preserve --ide, --chrome, --bare, --remote-control…]]'
- '[[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor
  Experience changes in rust-v0.138.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in rust-v0.139.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in rust-v0.139.0

**Codex CLI** · 2026-06-09 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.139.0) · from [[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|0.139.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex doctor` now includes editor and pager environment details in the local report while redacting raw values in JSON output. (#27081)

> Image edits now use the exact referenced image file paths instead of guessing from conversation history, so attached-image edits land on the intended input. (#26486)

> #26486 Route image edits through referenced file paths @won-openai

> #27081 feat(doctor): report editor and pager environment @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.139.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-09-3-context-window-changes-in-rust-v0-139-0|3 Context Window changes in rust-v0.139.0]] · Context Window
- [[Changes/Codex CLI/2026-06-09-3-search-and-browsing-changes-in-rust-v0-139-0|3 Search and Browsing changes in rust-v0.139.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-09-plugin-marketplace-automation-is-more-informative-and-responsive-codex-plugin-ma|Plugin marketplace automation is more informative and responsive]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-09-26637-codex-speed-up-external-agent-session-imports-stefanstokic-oai|♯26637 codex Speed up external agent session imports @stefanstokic-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-09-8-apps-and-integrations-changes-in-rust-v0-139-0|8 Apps and Integrations changes in rust-v0.139.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-09-26821-codex-exclude-external-tool-output-from-memories-rka-oai|♯26821 codex Exclude external tool output from memories @rka-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-09-5-agent-mode-changes-in-rust-v0-139-0|5 Agent Mode changes in rust-v0.139.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release builds once again publish separate symbol archives with line tables…]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-09-5-safety-and-privacy-changes-in-rust-v0-139-0|5 Safety and Privacy changes in rust-v0.139.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-09-24-other-changes-in-rust-v0-139-0|24 other changes in rust-v0.139.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-08 · Codex CLI · [[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor Experience changes in rust-v0.138.0]]
- Later: 2026-06-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-09-4-editor-experience-changes-in-v1-0-61|4 Editor Experience changes in v1.0.61]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-09-fc1589&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-09-4-editor-experience-changes-in-rust-v0-139-0.md%0ACard%20ID%3A%20codex-cli-2026-06-09-fc1589%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.139.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->