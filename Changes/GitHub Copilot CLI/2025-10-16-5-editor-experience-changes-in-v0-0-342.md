---
card_id: github-copilot-cli-2025-10-16-d99c89
date: '2025-10-16'
description: 'GitHub Copilot CLI · 2025-10-16 · Editor Experience: 5 changes in 0.0.342
  — New sessions are stored in `~/.copilot/session-state`'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2531
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7e665ad8729817913d1568b8b2ec3beb0b5e18ee9c3292f35446d7ddcefd5773
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2025-10-16-d99c89
  comparison: ''
  date: '2025-10-16'
  description: 'GitHub Copilot CLI — 0.0.342: 5 Editor Experience changes'
  evidence:
  - quote: New sessions are stored in `~/.copilot/session-state`
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.342
  - quote: Legacy sessions are stored in `~/.copilot/history-session-state` -- these
      will be migrated to the new format & location as you resume them from `copilot
      --resume`
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.342
  - quote: 'Improved debug log collection convenience by adding a persistent `log_level`
      option in `~/.copilot/config`. Possible values: `["none", "error", "warning",
      "info", "debug", "all", "default"]`'
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.342
  - quote: Added `gradlew` to the list of commands whose subcommands can be whitelisted
      (fixes https://github.com/github/copilot-cli/issues/217#issuecomment-3393844685)
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.342
  - quote: Run `npm install -g @github/copilot@latest` to update!
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.342
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-editor-experience-changes-in-v0-0-342
  source_release: github-copilot-cli-2025-10-16-v0-0-342-github-254861396-9c0ec25f
  source_type: github_releases
  theme: editor-experience
  title: 5 Editor Experience changes in v0.0.342
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-13-2-editor-experience-changes-in-v0-0-340|2
  Editor Experience changes in v0.0.340]]'
- '[[Changes/Gemini CLI/2025-10-15-4-editor-experience-changes-in-v0-9-0|4 Editor
  Experience changes in v0.9.0]]'
- '[[Changes/GitHub Copilot CLI/2025-10-15-run-npm-install-g-github-copilot-latest-to-update|Run
  npm install -g @github/copilot@latest to update!]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-16-v0-0-342-github-254861396-9c0ec25f|github-copilot-cli-2025-10-16-v0-0-342-github-254861396-9c0ec25f]]'
source_type: github_releases
theme: editor-experience
title: 5 Editor Experience changes in v0.0.342
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Editor Experience changes in v0.0.342

**GitHub Copilot CLI** · 2025-10-16 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v0.0.342) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-16-v0-0-342-github-254861396-9c0ec25f|0.0.342]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New sessions are stored in `~/.copilot/session-state`

> Legacy sessions are stored in `~/.copilot/history-session-state` -- these will be migrated to the new format & location as you resume them from `copilot --resume`

> Improved debug log collection convenience by adding a persistent `log_level` option in `~/.copilot/config`. Possible values: `["none", "error", "warning", "info", "debug", "all", "default"]`

> Added `gradlew` to the list of commands whose subcommands can be whitelisted (fixes https://github.com/github/copilot-cli/issues/217#issuecomment-3393844685)

> Run `npm install -g @github/copilot@latest` to update!

Source: https://github.com/github/copilot-cli/releases/tag/v0.0.342
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2025-10-16-enabled-non-interactive-ghe-logins-by-respecting-the-gh-host-environment-variabl|Enabled non-interactive GHE logins by respecting the GH_HOST environment variable…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2025-10-16-added-debug-logging-when-calls-to-model-result-in-copilot-api-errors-this-should|Added debug logging when calls to /model result in Copilot API errors]] · Model Support
- [[Changes/GitHub Copilot CLI/2025-10-16-enabled-the-kitty-protocol-by-default-multi-line-input-is-now-supported-via-shif|Enabled the Kitty protocol by default]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2025-10-16-3-other-changes-in-v0-0-342|3 other changes in v0.0.342]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2025-10-15 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-15-run-npm-install-g-github-copilot-latest-to-update|Run npm install -g @github/copilot@latest to update!]]
- Later: 2025-10-17 · Codex CLI · [[Changes/Codex CLI/2025-10-17-diff-mode-wraps-long-lines-4891|/diff mode wraps long lines (♯4891)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2025-10-16-d99c89&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2025-10-16-5-editor-experience-changes-in-v0-0-342.md%0ACard%20ID%3A%20github-copilot-cli-2025-10-16-d99c89%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv0.0.342%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->