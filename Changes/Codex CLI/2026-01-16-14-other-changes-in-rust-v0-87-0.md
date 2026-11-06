---
card_id: codex-cli-2026-01-16-01e32c
date: '2026-01-16'
description: 'Codex CLI · 2026-01-16 · Other changes: 14 changes in 0.87.0 — User
  message metadata (text elements and byte ranges) now round-trips through…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 64b2de2015f4226990197c34dee901abd04da4a684b66e1a8f6c4cd5411223be
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-16-01e32c
  comparison: ''
  date: '2026-01-16'
  description: 'Codex CLI — 0.87.0: 14 other changes'
  evidence:
  - quote: User message metadata (text elements and byte ranges) now round-trips through
      protocol/app-server/core so UI annotations can survive history rebuilds. (#9331)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: The TUI now surfaces approval requests from spawned/unsubscribed threads.
      (#9232)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: The TUI “Worked for” separator only appears after actual work has occurred.
      (#8958)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: Piped non-PTY commands no longer hang waiting on stdin. (#9369)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: Windows builds enable the PowerShell UTF-8 feature by default. (#9195)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9331 Add text element metadata to protocol, app server, and core @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9195 chore(windows) Enable Powershell UTF8 feature @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#8958 fix(tui): only show ''Worked for'' separator when actual work was
      performed @ThanhNguyxn'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9232 feat: propagate approval request of unsubscribed threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9357 feat: run user commands under user snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9294 feat: collab wait multiple IDs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9366 feat: CODEX_CI @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9367 prompt collab @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9369 chore: close pipe on non-pty processes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-other-changes-in-rust-v0-87-0
  source_release: codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8
  source_type: github_releases
  theme: uncategorized
  title: 14 other changes in rust-v0.87.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8|codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8]]'
source_type: github_releases
theme: uncategorized
title: 14 other changes in rust-v0.87.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 other changes in rust-v0.87.0

**Codex CLI** · 2026-01-16 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.87.0) · from [[Releases/Codex CLI/codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8|0.87.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> User message metadata (text elements and byte ranges) now round-trips through protocol/app-server/core so UI annotations can survive history rebuilds. (#9331)

> The TUI now surfaces approval requests from spawned/unsubscribed threads. (#9232)

> The TUI “Worked for” separator only appears after actual work has occurred. (#8958)

> Piped non-PTY commands no longer hang waiting on stdin. (#9369)

> Windows builds enable the PowerShell UTF-8 feature by default. (#9195)

> #9331 Add text element metadata to protocol, app server, and core @charley-oai

> #9195 chore(windows) Enable Powershell UTF8 feature @dylan-hurd-oai

> #8958 fix(tui): only show 'Worked for' separator when actual work was performed @ThanhNguyxn

> #9232 feat: propagate approval request of unsubscribed threads @jif-oai

> #9357 feat: run user commands under user snapshot @jif-oai

> #9294 feat: collab wait multiple IDs @jif-oai

> #9366 feat: CODEX_CI @jif-oai

> #9367 prompt collab @jif-oai

> #9369 chore: close pipe on non-pty processes @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.87.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-16-collaboration-wait-calls-can-block-on-multiple-ids-in-one-request-simplifying-mu|Collaboration wait calls can block on multiple IDs in one request, simplifying…]] · Collaboration
- [[Changes/Codex CLI/2026-01-16-3-apps-and-integrations-changes-in-rust-v0-87-0|3 Apps and Integrations changes in rust-v0.87.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-16-9336-rename-model-turn-to-sampling-request-aibrahim-oai|♯9336 rename model turn to sampling request @aibrahim-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-16-user-shell-commands-now-run-under-the-user-snapshot-so-aliases-and-shell-config|User shell commands now run under the user snapshot so aliases and shell config…]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-16-2-context-window-changes-in-rust-v0-87-0|2 Context Window changes in rust-v0.87.0]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-16-01e32c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-16-14-other-changes-in-rust-v0-87-0.md%0ACard%20ID%3A%20codex-cli-2026-01-16-01e32c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.87.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->