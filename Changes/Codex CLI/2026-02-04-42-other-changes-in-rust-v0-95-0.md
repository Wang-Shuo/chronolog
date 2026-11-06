---
card_id: codex-cli-2026-02-04-c3ac7a
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Other changes: 42 changes in 0.95.0 — Improved
  401 error diagnostics by including server message/body details plus `cf-ray` and…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5b5ac7c79d047cdfc0fada54ec61dd930cb5e937058882cd759f86a96272cef4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-c3ac7a
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.95.0: 42 other changes'
  evidence:
  - quote: Improved 401 error diagnostics by including server message/body details
      plus `cf-ray` and `requestId`. (#10508)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: 'Refreshed issue templates and labeler prompts to better separate CLI/app
      bug reporting and feature requests. (#10411, #10453, #10548, #10552)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10381 chore: collab experimental @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10231 feat: experimental flags @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10383 fix: thread listing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10386 fix: Rfc3339 casting @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10269 Nicer highlighting of slash commands, /plan accepts prompt args
      and pasted images @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10394 chore: ignore synthetic messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10398 feat: drop sqlx logging @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10281 Select experimental features with space @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10402 feat: add `--experimental` to `generate-ts` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10411 Updated labeler workflow prompt to include "app" label @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10399 emit a separate metric when the user cancels UAT during elevated
      setup @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10377 chore(tui) /personalities tip @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10252 [feat] persist thread_dynamic_tools in db @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10064 TUI: Render request_user_input results in history and simplify
      interrupt handling @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10452 Hide short worked-for label in final separator @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10454 app tool tip @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10455 chore: add phase to message responseitem @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10453 Updated bug and feature templates @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10465 Restore status after preamble @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10142 feat(secrets): add codex-secrets crate @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10157 chore: nuke chat/completions API @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10498 feat: drop wire_api from clients @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10501 feat: clean codex-api part 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10508 Add more detail to 401 error @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10521 Avoid redundant transactional check before inserting dynamic tools
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10408 fix WebSearchAction type clash between v1 and v2 @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10532 feat: `find_thread_path_by_id_str_in_subdir` from DB @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10536 Revert "Load untrusted rules" @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10412 fix(app-server): fix TS annotations for optional fields on requests
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10416 fix(app-server): fix approval events in review mode @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10545 Improve Default mode prompt (less confusion with Plan mode) @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10189 implement per-workspace capability SIDs for workspace specific
      ACLs @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10548 Updated bug templates and added a new one for app @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10531 [codex] Default values from requirements if unset @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10552 Fixed icon for CLI bug template @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10039 chore(arg0): advisory-lock janitor for codex tmp paths @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10448 feat: add APIs to list and download public remote skills @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10519 Handle exec shutdown on Interrupt (fixes immortal `codex exec`
      with websockets) @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10556 Feat: add upgrade to app server modelList @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10461 feat(tui): pace catch-up stream chunking with hysteresis @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 42-other-changes-in-rust-v0-95-0
  source_release: codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b
  source_type: github_releases
  theme: uncategorized
  title: 42 other changes in rust-v0.95.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b]]'
source_type: github_releases
theme: uncategorized
title: 42 other changes in rust-v0.95.0
type: change
---

<!-- chronolog:begin region="header" -->
# 42 other changes in rust-v0.95.0

**Codex CLI** · 2026-02-04 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.95.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved 401 error diagnostics by including server message/body details plus `cf-ray` and `requestId`. (#10508)

> Refreshed issue templates and labeler prompts to better separate CLI/app bug reporting and feature requests. (#10411, #10453, #10548, #10552)

> #10381 chore: collab experimental @jif-oai

> #10231 feat: experimental flags @jif-oai

> #10383 fix: thread listing @jif-oai

> #10386 fix: Rfc3339 casting @jif-oai

> #10269 Nicer highlighting of slash commands, /plan accepts prompt args and pasted images @charley-oai

> #10394 chore: ignore synthetic messages @jif-oai

> #10398 feat: drop sqlx logging @jif-oai

> #10281 Select experimental features with space @pakrym-oai

> #10402 feat: add `--experimental` to `generate-ts` @jif-oai

> #10411 Updated labeler workflow prompt to include "app" label @etraut-openai

> #10399 emit a separate metric when the user cancels UAT during elevated setup @iceweasel-oai

> #10377 chore(tui) /personalities tip @dylan-hurd-oai

> #10252 [feat] persist thread_dynamic_tools in db @celia-oai

> #10064 TUI: Render request_user_input results in history and simplify interrupt handling @charley-oai

> #10452 Hide short worked-for label in final separator @aibrahim-oai

> #10454 app tool tip @aibrahim-oai

> #10455 chore: add phase to message responseitem @sayan-oai

> #10453 Updated bug and feature templates @etraut-openai

> #10465 Restore status after preamble @pakrym-oai

> #10142 feat(secrets): add codex-secrets crate @viyatb-oai

> #10157 chore: nuke chat/completions API @jif-oai

> #10498 feat: drop wire_api from clients @jif-oai

> #10501 feat: clean codex-api part 1 @jif-oai

> #10508 Add more detail to 401 error @gt-oai

> #10521 Avoid redundant transactional check before inserting dynamic tools @jif-oai

> #10408 fix WebSearchAction type clash between v1 and v2 @sayan-oai

> #10532 feat: `find_thread_path_by_id_str_in_subdir` from DB @jif-oai

> #10536 Revert "Load untrusted rules" @viyatb-oai

> #10412 fix(app-server): fix TS annotations for optional fields on requests @owenlin0

> #10416 fix(app-server): fix approval events in review mode @owenlin0

> #10545 Improve Default mode prompt (less confusion with Plan mode) @charley-oai

> #10189 implement per-workspace capability SIDs for workspace specific ACLs @iceweasel-oai

> #10548 Updated bug templates and added a new one for app @etraut-openai

> #10531 [codex] Default values from requirements if unset @gt-oai

> #10552 Fixed icon for CLI bug template @etraut-openai

> #10039 chore(arg0): advisory-lock janitor for codex tmp paths @viyatb-oai

> #10448 feat: add APIs to list and download public remote skills @xl-openai

> #10519 Handle exec shutdown on Interrupt (fixes immortal `codex exec` with websockets) @rasmusrygaard

> #10556 Feat: add upgrade to app server modelList @shijie-oai

> #10461 feat(tui): pace catch-up stream chunking with hysteresis @joshka-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.95.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0|10 Developer Workflow changes in rust-v0.95.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-04-10340-session-picker-shows-thread-name-if-set-pap-openai|♯10340 Session picker shows thread_name if set @pap-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Context Window
- [[Changes/Codex CLI/2026-02-04-10404-cleanup-collaboration-mode-variants-charley-oai|♯10404 Cleanup collaboration mode variants @charley-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-04-2-mobile-and-desktop-changes-in-rust-v0-95-0|2 Mobile and Desktop changes in rust-v0.95.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Model Support
- [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5 Apps and Integrations changes in rust-v0.95.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2 Search and Browsing changes in rust-v0.95.0]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-c3ac7a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-42-other-changes-in-rust-v0-95-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-c3ac7a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.95.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->