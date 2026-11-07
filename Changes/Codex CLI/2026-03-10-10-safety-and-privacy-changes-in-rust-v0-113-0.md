---
card_id: codex-cli-2026-03-10-325a24
date: '2026-03-10'
description: 'Codex CLI · 2026-03-10 · Safety and Privacy: 10 changes in 0.113.0 —
  Added the new permission-profile config language and split filesystem/network sandbox…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2051
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cc25cfadabff4b1995d5ced0efa7fa40ebfa1969c1b60b620ecb7ae73329528f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-10-325a24
  comparison: ''
  date: '2026-03-10'
  description: 'Codex CLI — 0.113.0: 10 Safety and Privacy changes'
  evidence:
  - quote: 'Added the new permission-profile config language and split filesystem/network
      sandbox policy plumbing for more precise policy control. (#13434, #13439, #13440,
      #13448, #13449, #13453)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13677 chore: remove unused legacy macOS permission types @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13669 copy current exe to CODEX_HOME/.sandbox-bin for apply_patch @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13703 Clarify sandbox permission override helper semantics @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13434 config: add initial support for the new permission profile config
      language in config.toml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13439 sandboxing: plumb split sandbox policies through runtime @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13445 safety: honor filesystem policy carveouts in apply_patch @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13448 seatbelt: honor split filesystem sandbox policies @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13449 linux-sandbox: plumb split sandbox policies through helper @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13453 linux-sandbox: honor split filesystem policies in bwrap @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-safety-and-privacy-changes-in-rust-v0-113-0
  source_release: codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in rust-v0.113.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-03-09-packages|Packages]]'
- '[[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools
  now fully undoes /allow-all and re-triggers the autopilot…]]'
- '[[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety
  and Privacy changes in v2.1.72]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in rust-v0.113.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in rust-v0.113.0

**Codex CLI** · 2026-03-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.113.0) · from [[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the new permission-profile config language and split filesystem/network sandbox policy plumbing for more precise policy control. (#13434, #13439, #13440, #13448, #13449, #13453)

> #13677 chore: remove unused legacy macOS permission types @celia-oai

> #13669 copy current exe to CODEX_HOME/.sandbox-bin for apply_patch @iceweasel-oai

> #13703 Clarify sandbox permission override helper semantics @charley-oai

> #13434 config: add initial support for the new permission profile config language in config.toml @bolinfest

> #13439 sandboxing: plumb split sandbox policies through runtime @bolinfest

> #13445 safety: honor filesystem policy carveouts in apply_patch @bolinfest

> #13448 seatbelt: honor split filesystem sandbox policies @bolinfest

> #13449 linux-sandbox: plumb split sandbox policies through helper @bolinfest

> #13453 linux-sandbox: honor split filesystem policies in bwrap @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.113.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-10-2-automation-and-scheduling-changes-in-rust-v0-113-0|2 Automation and Scheduling changes in rust-v0.113.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-10-13734-feat-prune-old-memories-in-db-jif-oai|♯13734 feat: prune old memories in DB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-10-4-interface-experience-changes-in-rust-v0-113-0|4 Interface Experience changes in rust-v0.113.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-10-8-developer-workflow-changes-in-rust-v0-113-0|8 Developer Workflow changes in rust-v0.113.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-10-14117-feat-otel-centralize-otel-metric-names-and-shared-tag-builders-owenlin0|♯14117 feat(otel): Centralize OTEL metric names and shared tag builders @owenlin0]] · Collaboration
- [[Changes/Codex CLI/2026-03-10-image-generation-now-saves-output-files-into-the-current-working-directory-13607|Image generation now saves output files into the current working directory]] · Image Generation
- [[Changes/Codex CLI/2026-03-10-14123-pass-on-save-info-to-model-ui-tweaks-won-openai|♯14123 pass on save info to model + ui tweaks @won-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-10-2-search-and-browsing-changes-in-rust-v0-113-0|2 Search and Browsing changes in rust-v0.113.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-10-2-account-and-access-changes-in-rust-v0-113-0|2 Account and Access changes in rust-v0.113.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-10-4-context-window-changes-in-rust-v0-113-0|4 Context Window changes in rust-v0.113.0]] · Context Window
- [[Changes/Codex CLI/2026-03-10-70-other-changes-in-rust-v0-113-0|70 other changes in rust-v0.113.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-10 · Claude Code · [[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety and Privacy changes in v2.1.72]]
- Later: 2026-03-11 · Claude Code · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-10-325a24&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0.md%0ACard%20ID%3A%20codex-cli-2026-03-10-325a24%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.113.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->