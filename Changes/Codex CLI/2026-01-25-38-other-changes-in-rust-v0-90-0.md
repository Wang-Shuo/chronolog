---
card_id: codex-cli-2026-01-25-a74f17
date: '2026-01-25'
description: 'Codex CLI · 2026-01-25 · Other changes: 38 changes in 0.90.0 — WebSocket
  connections now support proxy configuration. (#9719)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 19b051195ec4767bd3374367f178fd82feb4a5535e870a98314c80a490f22df2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-25-a74f17
  comparison: ''
  date: '2026-01-25'
  description: 'Codex CLI — 0.90.0: 38 other changes'
  evidence:
  - quote: WebSocket connections now support proxy configuration. (#9719)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: 'Improved resume reliability by handling out-of-order events and prompting
      for the working directory when it differs. (#9512, #9731)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: Backspace no longer deletes a text element when the cursor is at the element’s
      left edge. (#9630)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: Config loading errors are clearer and more actionable across surfaces.
      (#9746)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: Updated GitHub Actions for Node 24 compatibility. (#9722)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9715 feat: fix formatting of `codex features list` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9716 Fix typo in experimental_prompt.md @iudizm'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9719 feat: support proxy for ws connection @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9712 TUI: prompt to implement plan and switch to Execute @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9713 use machine scope instead of user scope for dpapi. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9730 Hide mode cycle hint while a task is running @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9720 feat: add session source as otel metadata tag @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9565 Fix execpolicy parsing for multiline quoted args @jdsalasca'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9745 chore: use some raw strings to reduce quoting @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9753 nit: exclude PWD for rc sourcing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9690 feat: tui beta for collab @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9116 Persist text element ranges and attached images across history/resume
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9777 plan mode prompt change @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9722 Upgrade GitHub Actions for Node 24 compatibility @salmanmkc'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9611 Print warning if we skip config loading @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9787 Remove stale TODO comment from defs.bzl @jcoens-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9700 still load skills @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9791 Load untrusted rules @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9792 Chore: remove mode from header @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9802 Have a coding mode and only show coding and plan @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9746 Another round of improvements for config error messages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9812 Remove batman reference from experimental prompt @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9769 feat: add thread spawn source for collab tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9765 feat: ephemeral threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9819 fix: libcc link @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9820 fix: musl build @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9630 Prevent backspace from removing a text element when the cursor is
      at the element’s left edge @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9840 Revert "fix: musl build" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9778 Raise welcome animation breakpoint to 37 rows @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9731 Ask for cwd choice when resuming session from different cwd @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9841 Revert "fix: libcc link" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9834 Mark collab as beta @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  - quote: '#9847 Revert "Revert "fix: musl build"" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.90.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 38-other-changes-in-rust-v0-90-0
  source_release: codex-cli-2026-01-25-rust-v0-90-0-github-279750097-d3f5736c
  source_type: github_releases
  theme: uncategorized
  title: 38 other changes in rust-v0.90.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-25-rust-v0-90-0-github-279750097-d3f5736c|codex-cli-2026-01-25-rust-v0-90-0-github-279750097-d3f5736c]]'
source_type: github_releases
theme: uncategorized
title: 38 other changes in rust-v0.90.0
type: change
---

<!-- chronolog:begin region="header" -->
# 38 other changes in rust-v0.90.0

**Codex CLI** · 2026-01-25 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.90.0) · from [[Releases/Codex CLI/codex-cli-2026-01-25-rust-v0-90-0-github-279750097-d3f5736c|0.90.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> WebSocket connections now support proxy configuration. (#9719)

> Improved resume reliability by handling out-of-order events and prompting for the working directory when it differs. (#9512, #9731)

> Backspace no longer deletes a text element when the cursor is at the element’s left edge. (#9630)

> Config loading errors are clearer and more actionable across surfaces. (#9746)

> Updated GitHub Actions for Node 24 compatibility. (#9722)

> #9715 feat: fix formatting of `codex features list` @bolinfest

> #9716 Fix typo in experimental_prompt.md @iudizm

> #9719 feat: support proxy for ws connection @apanasenko-oai

> #9712 TUI: prompt to implement plan and switch to Execute @charley-oai

> #9713 use machine scope instead of user scope for dpapi. @iceweasel-oai

> #9730 Hide mode cycle hint while a task is running @charley-oai

> #9720 feat: add session source as otel metadata tag @alexsong-oai

> #9565 Fix execpolicy parsing for multiline quoted args @jdsalasca

> #9745 chore: use some raw strings to reduce quoting @bolinfest

> #9753 nit: exclude PWD for rc sourcing @jif-oai

> #9690 feat: tui beta for collab @jif-oai

> #9116 Persist text element ranges and attached images across history/resume @charley-oai

> #9777 plan mode prompt change @aibrahim-oai

> #9722 Upgrade GitHub Actions for Node 24 compatibility @salmanmkc

> #9611 Print warning if we skip config loading @gt-oai

> #9787 Remove stale TODO comment from defs.bzl @jcoens-openai

> #9700 still load skills @gt-oai

> #9791 Load untrusted rules @gt-oai

> #9792 Chore: remove mode from header @aibrahim-oai

> #9802 Have a coding mode and only show coding and plan @aibrahim-oai

> #9746 Another round of improvements for config error messages @etraut-openai

> #9812 Remove batman reference from experimental prompt @charley-oai

> #9769 feat: add thread spawn source for collab tools @jif-oai

> #9765 feat: ephemeral threads @jif-oai

> #9819 fix: libcc link @jif-oai

> #9820 fix: musl build @jif-oai

> #9630 Prevent backspace from removing a text element when the cursor is at the element’s left edge @charley-oai

> #9840 Revert "fix: musl build" @aibrahim-oai

> #9778 Raise welcome animation breakpoint to 37 rows @mzeng-openai

> #9731 Ask for cwd choice when resuming session from different cwd @charley-oai

> #9841 Revert "fix: libcc link" @aibrahim-oai

> #9834 Mark collab as beta @pakrym-oai

> #9847 Revert "Revert "fix: musl build"" @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.90.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-25-9512-fix-resume-picker-when-user-event-appears-after-head-jdsalasca|♯9512 Fix resume picker when user event appears after head @jdsalasca]] · Interface Experience
- [[Changes/Codex CLI/2026-01-25-4-safety-and-privacy-changes-in-rust-v0-90-0|4 Safety and Privacy changes in rust-v0.90.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-25-3-apps-and-integrations-changes-in-rust-v0-90-0|3 Apps and Integrations changes in rust-v0.90.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-25-5-collaboration-changes-in-rust-v0-90-0|5 Collaboration changes in rust-v0.90.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-25-5-model-support-changes-in-rust-v0-90-0|5 Model Support changes in rust-v0.90.0]] · Model Support
- [[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-90-0|2 Agent Mode changes in rust-v0.90.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-25-2-developer-workflow-changes-in-rust-v0-90-0|2 Developer Workflow changes in rust-v0.90.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-25-9674-feat-app-server-expose-personality-dylan-hurd-oai|♯9674 feat(app-server) Expose personality @dylan-hurd-oai]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-25-a74f17&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-25-38-other-changes-in-rust-v0-90-0.md%0ACard%20ID%3A%20codex-cli-2026-01-25-a74f17%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.90.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->