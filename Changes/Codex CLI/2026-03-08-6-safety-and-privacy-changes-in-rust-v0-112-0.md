---
card_id: codex-cli-2026-03-08-5a0b3a
date: '2026-03-08'
description: 'Codex CLI · 2026-03-08 · Safety and Privacy: 6 changes in 0.112.0 —
  Merged executable permission profiles into per-turn sandbox policy for zsh-fork
  skill…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2049
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 79821e23c9433dcbdca9f2e9b19c65667fada8c20884334f149c58e24e4f7083
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
- '[[Changes/Notion/2026-03-05-the-new-can-create-pages-database-permission-lets-users-create-new-pages-in-a-da|The
  new “can create pages” database permission lets users create new pages…]]'
- '[[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed
  false-positive permission prompts for compound bash commands containing…]]'
- '[[Changes/OpenCode/2026-03-07-core-enable-auto-accept-keybind-regardless-of-permission-config|Core
  Enable auto-accept keybind regardless of permission config]]'
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

- Earlier: 2026-03-07 · OpenCode · [[Changes/OpenCode/2026-03-07-core-enable-auto-accept-keybind-regardless-of-permission-config|Core Enable auto-accept keybind regardless of permission config]]
- Later: 2026-03-08 · Open WebUI · [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-08-5a0b3a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-08-6-safety-and-privacy-changes-in-rust-v0-112-0.md%0ACard%20ID%3A%20codex-cli-2026-03-08-5a0b3a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.112.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->