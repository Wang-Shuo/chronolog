---
card_id: codex-cli-2026-01-07-8d72e6
date: '2026-01-07'
description: 'Codex CLI · 2026-01-07 · Other changes: 25 changes in 0.79.0 — Show
  time/version-targeted announcement tips in the TUI, driven by a TOML file in the
  repo…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ecc123fe6e26dc535ccd444146089cd5ffa9bcd9360b97b1c68e36d37e36e603
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-07-8d72e6
  comparison: ''
  date: '2026-01-07'
  description: 'Codex CLI — 0.79.0: 25 other changes'
  evidence:
  - quote: Show time/version-targeted announcement tips in the TUI, driven by a TOML
      file in the repo (#8752)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Add an `[analytics] enabled=...` config section to control analytics behavior
      (#8350)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Make `apply_patch` parsing tolerant of whitespace-padded `*** Begin Patch`
      / `*** End Patch` markers (#8746)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Prevent `CODEX_MANAGED_CONFIG_PATH` from overriding managed config in production,
      closing a policy bypass (#8762)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Ensure app-server conversations respect the config passed in by the client
      (#8765)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Refactor skills discovery to use the config layer stack so all configured
      skill folders are considered (#8497)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Auto-populate GitHub release notes at release creation time (#8799)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Add more `apply_patch` test scenarios to harden coverage (#8230)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: Tweak unified exec event emission to only send “begin” when a PTY is present
      (#8780)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8497 Use ConfigLayerStack for skills discovery. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8440 Allow global exec flags after `resume` and fix CI codex build/timeout
      @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8230 chore(apply-patch) additional scenarios @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8746 fix: accept whitespace-padded patch markers @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8771 fix: render cwd-relative paths in tui @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8770 fix: fix readiness subscribe token wrap-around @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8780 chore: emit unified exec begin only when PTY exist @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8762 fix: stop honoring CODEX_MANAGED_CONFIG_PATH environment variable
      in production @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8735 feat: add head-tail buffer for `unified_exec` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8752 feat: forced tool tips @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8786 chore: clear background terminals on interrupt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8350 feat: add analytics config setting @JaviSoto'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8777 Clear copy pill background and add snapshot test @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8454 feat(app-server): thread/rollback API @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8765 [app-server] fix config loading for conversations @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  - quote: '#8799 fix: populate the release notes when the release is created @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.79.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 25-other-changes-in-rust-v0-79-0
  source_release: codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364
  source_type: github_releases
  theme: uncategorized
  title: 25 other changes in rust-v0.79.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364|codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364]]'
source_type: github_releases
theme: uncategorized
title: 25 other changes in rust-v0.79.0
type: change
---

<!-- chronolog:begin region="header" -->
# 25 other changes in rust-v0.79.0

**Codex CLI** · 2026-01-07 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.79.0) · from [[Releases/Codex CLI/codex-cli-2026-01-07-rust-v0-79-0-github-274682036-5d03e364|0.79.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Show time/version-targeted announcement tips in the TUI, driven by a TOML file in the repo (#8752)

> Add an `[analytics] enabled=...` config section to control analytics behavior (#8350)

> Make `apply_patch` parsing tolerant of whitespace-padded `*** Begin Patch` / `*** End Patch` markers (#8746)

> Prevent `CODEX_MANAGED_CONFIG_PATH` from overriding managed config in production, closing a policy bypass (#8762)

> Ensure app-server conversations respect the config passed in by the client (#8765)

> Refactor skills discovery to use the config layer stack so all configured skill folders are considered (#8497)

> Auto-populate GitHub release notes at release creation time (#8799)

> Add more `apply_patch` test scenarios to harden coverage (#8230)

> Tweak unified exec event emission to only send “begin” when a PTY is present (#8780)

> #8497 Use ConfigLayerStack for skills discovery. @xl-openai

> #8440 Allow global exec flags after `resume` and fix CI codex build/timeout @fjord-oai

> #8230 chore(apply-patch) additional scenarios @dylan-hurd-oai

> #8746 fix: accept whitespace-padded patch markers @tibo-openai

> #8771 fix: render cwd-relative paths in tui @joshka-oai

> #8770 fix: fix readiness subscribe token wrap-around @tibo-openai

> #8780 chore: emit unified exec begin only when PTY exist @jif-oai

> #8762 fix: stop honoring CODEX_MANAGED_CONFIG_PATH environment variable in production @bolinfest

> #8735 feat: add head-tail buffer for `unified_exec` @jif-oai

> #8752 feat: forced tool tips @jif-oai

> #8786 chore: clear background terminals on interrupt @jif-oai

> #8350 feat: add analytics config setting @JaviSoto

> #8777 Clear copy pill background and add snapshot test @joshka-oai

> #8454 feat(app-server): thread/rollback API @owenlin0

> #8765 [app-server] fix config loading for conversations @celia-oai

> #8799 fix: populate the release notes when the release is created @bolinfest

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
- [[Changes/Codex CLI/2026-01-07-4-search-and-browsing-changes-in-rust-v0-79-0|4 Search and Browsing changes in rust-v0.79.0]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-07-8d72e6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-07-25-other-changes-in-rust-v0-79-0.md%0ACard%20ID%3A%20codex-cli-2026-01-07-8d72e6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.79.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->