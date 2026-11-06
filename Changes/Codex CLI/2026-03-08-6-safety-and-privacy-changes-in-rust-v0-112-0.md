---
card_id: codex-cli-2026-03-08-5a0b3a
date: '2026-03-08'
description: 'Codex CLI · 2026-03-08 · Safety and Privacy: 6 changes in 0.112.0 —
  Merged executable permission profiles into per-turn sandbox policy for zsh-fork
  skill…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c6e463973b5e0aff4846d2d97c7f74f0fd168c05c2d88569c99e92e44c6a008
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-08-5a0b3a
  comparison: ''
  date: '2026-03-08'
  description: 'Codex CLI — 0.112.0: 6 Safety and Privacy changes'
  evidence:
  - quote: Merged executable permission profiles into per-turn sandbox policy for
      zsh-fork skill execution, allowing safer, additive privilege handling for tool
      runs. (#13496)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: Ensured Linux bubblewrap sandbox runs always unshare the user namespace
      to keep isolation consistent even for root-owned invocations. (#13624)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: Improved macOS sandbox network and unix-socket handling in Seatbelt, improving
      reliability for constrained subprocess environments. (#12702)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13496 feat: merge skill permission profiles into the turn sandbox for
      zsh-fork execs @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13624 fix(linux-sandbox): always unshare bwrap userns @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  - quote: '#13499 core/protocol: add structured macOS additional permissions and
      merge them into sandbox execution @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.112.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-safety-and-privacy-changes-in-rust-v0-112-0
  source_release: codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in rust-v0.112.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4
  Safety and Privacy changes in rust-v0.110.0]]'
- '[[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When
  invoked, the agent spins up a cloud sandbox and follows your instructions using…]]'
- '[[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed
  false-positive permission prompts for compound bash commands containing…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5|codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in rust-v0.112.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in rust-v0.112.0

**Codex CLI** · 2026-03-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.112.0) · from [[Releases/Codex CLI/codex-cli-2026-03-08-rust-v0-112-0-github-294459110-d90013b5|0.112.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Merged executable permission profiles into per-turn sandbox policy for zsh-fork skill execution, allowing safer, additive privilege handling for tool runs. (#13496)

> Ensured Linux bubblewrap sandbox runs always unshare the user namespace to keep isolation consistent even for root-owned invocations. (#13624)

> Improved macOS sandbox network and unix-socket handling in Seatbelt, improving reliability for constrained subprocess environments. (#12702)

> #13496 feat: merge skill permission profiles into the turn sandbox for zsh-fork execs @celia-oai

> #13624 fix(linux-sandbox): always unshare bwrap userns @viyatb-oai

> #13499 core/protocol: add structured macOS additional permissions and merge them into sandbox execution @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.112.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update models.json @aibrahim-oai]] · Model Support
- [[Changes/Codex CLI/2026-03-08-12702-improve-macos-seatbelt-network-and-unix-socket-handling-viyatb-oai|♯12702 Improve macOS Seatbelt network and unix socket handling @viyatb-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-08-added-a-new-model-selection-surface-update-so-the-latest-model-catalog-changes-a|Added a new model-selection surface update so the latest model catalog changes…]] · Interface Experience
- [[Changes/Codex CLI/2026-03-08-2-apps-and-integrations-changes-in-rust-v0-112-0|2 Apps and Integrations changes in rust-v0.112.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-08-11-other-changes-in-rust-v0-112-0|11 other changes in rust-v0.112.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-07 · Claude Code · [[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed false-positive permission prompts for compound bash commands containing…]]
- Later: 2026-03-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools now fully undoes /allow-all and re-triggers the autopilot…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-08-5a0b3a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-08-6-safety-and-privacy-changes-in-rust-v0-112-0.md%0ACard%20ID%3A%20codex-cli-2026-03-08-5a0b3a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.112.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->