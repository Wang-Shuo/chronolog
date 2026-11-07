---
card_id: codex-cli-2026-02-17-8c0efd
date: '2026-02-17'
description: 'Codex CLI · 2026-02-17 · Safety and Privacy: 9 changes in 0.102.0 —
  Added a more unified permissions flow, including clearer permissions history in
  the TUI and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2030
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 917c3c6420ce0560d623872f43055063d7587edc6757feb61836d45cf5063698
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-17-8c0efd
  comparison: ''
  date: '2026-02-17'
  description: 'Codex CLI — 0.102.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Added a more unified permissions flow, including clearer permissions history
      in the TUI and a slash command to grant sandbox read access when directories
      are blocked. (#11633, #11512, #11550, #11639)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11512 add a slash command to grant sandbox read access to inaccessible
      directories @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11639 [feat] add seatbelt permission files @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11667 sandbox NUX metrics update @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11658 feat(skills): add permission profiles from openai.yaml metadata
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11767 fix(core): add linux bubblewrap sandbox tag @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11948 add(feedback): over-refusal / safety check @fouad-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11964 add(core): safety check downgrade warning @fouad-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11970 Protect workspace .agents directory in Windows sandbox @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-102-0
  source_release: codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.102.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-13-2-safety-and-privacy-changes-in-v2-1-41|2 Safety
  and Privacy changes in v2.1.41]]'
- "[[Changes/Open WebUI/2026-02-14-public-sharing-security-fix-fixed-a-security-issue-where-users-with-write-access|\U0001F6E1️
  Public sharing security fix. Fixed a security issue where users with write…]]"
- '[[Changes/Claude Code/2026-02-17-vscode-improved-permission-destination-choice-project-user-session-to-persist-ac|VSCode
  Improved permission destination choice (project/user/session) to persist…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.102.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.102.0

**Codex CLI** · 2026-02-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.102.0) · from [[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|0.102.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a more unified permissions flow, including clearer permissions history in the TUI and a slash command to grant sandbox read access when directories are blocked. (#11633, #11512, #11550, #11639)

> #11512 add a slash command to grant sandbox read access to inaccessible directories @iceweasel-oai

> #11639 [feat] add seatbelt permission files @celia-oai

> #11667 sandbox NUX metrics update @iceweasel-oai

> #11658 feat(skills): add permission profiles from openai.yaml metadata @celia-oai

> #11767 fix(core): add linux bubblewrap sandbox tag @viyatb-oai

> #11948 add(feedback): over-refusal / safety check @fouad-openai

> #11964 add(core): safety check downgrade warning @fouad-openai

> #11970 Protect workspace .agents directory in Windows sandbox @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.102.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-17-3-developer-workflow-changes-in-rust-v0-102-0|3 Developer Workflow changes in rust-v0.102.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-17-11-model-support-changes-in-rust-v0-102-0|11 Model Support changes in rust-v0.102.0]] · Model Support
- [[Changes/Codex CLI/2026-02-17-15-apps-and-integrations-changes-in-rust-v0-102-0|15 Apps and Integrations changes in rust-v0.102.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-17-2-mobile-and-desktop-changes-in-rust-v0-102-0|2 Mobile and Desktop changes in rust-v0.102.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-17-11860-fixed-screen-reader-regression-in-cli-etraut-openai|♯11860 Fixed screen reader regression in CLI @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-02-17-11224-chore-clarify-web-search-deprecation-notices-and-consolidate-tests-sayan-o|♯11224 chore: clarify web_search deprecation notices and consolidate tests @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-17-4-context-window-changes-in-rust-v0-102-0|4 Context Window changes in rust-v0.102.0]] · Context Window
- [[Changes/Codex CLI/2026-02-17-4-memory-and-personalization-changes-in-rust-v0-102-0|4 Memory and Personalization changes in rust-v0.102.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-17-3-interface-experience-changes-in-rust-v0-102-0|3 Interface Experience changes in rust-v0.102.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-17-7-agent-mode-changes-in-rust-v0-102-0|7 Agent Mode changes in rust-v0.102.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-17-59-other-changes-in-rust-v0-102-0|59 other changes in rust-v0.102.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-17 · Claude Code · [[Changes/Claude Code/2026-02-17-vscode-improved-permission-destination-choice-project-user-session-to-persist-ac|VSCode Improved permission destination choice (project/user/session) to persist…]]
- Later: 2026-02-17 · Cursor · [[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access controls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-17-8c0efd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-17-9-safety-and-privacy-changes-in-rust-v0-102-0.md%0ACard%20ID%3A%20codex-cli-2026-02-17-8c0efd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.102.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->