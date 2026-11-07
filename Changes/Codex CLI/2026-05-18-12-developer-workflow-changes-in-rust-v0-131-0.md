---
card_id: codex-cli-2026-05-18-5d5470
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Developer Workflow: 12 changes in 0.131.0 —
  Added `codex doctor` for support-ready diagnostics across runtime, auth, terminal…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2806
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 181ed4b57f5d334d4d3768011924eaa0e249bbe3fe460dbb2f7a1aed09b0ee81
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-5d5470
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 12 Developer Workflow changes'
  evidence:
  - quote: Added `codex doctor` for support-ready diagnostics across runtime, auth,
      terminal, network, config, and local state. (#22336)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21628 Use `CARGO_NET_GIT_FETCH_WITH_CLI` in `rust-ci-full` for more reliable
      git fetches @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21738 extension: move git attribution into an extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20305 fix(exec-policy) use is_known_safe_command less @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#18748 [codex-analytics] emit terminal review events @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22159 Add Windows hook command overrides @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21946 fix(tui): handle hidden app git directives @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21206 feat(tui): add ambient terminal pets @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22246 [codex] Remove unused legacy shell tools @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22535 Remove resurrected `/collab` slash command @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22652 [codex] Ignore fsmonitor config in Git metadata reads @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22717 chore(config) rm windows_wsl_setup_acknowledged @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-developer-workflow-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: developer-workflow
  title: 12 Developer Workflow changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-16-terminal-newly-pinned-sessions-now-stay-at-the-end-of-the-pinned-list-instead-of|Terminal
  Newly pinned sessions now stay at the end of the pinned list instead…]]'
- '[[Changes/Windsurf/2026-05-16-2-developer-workflow-changes-in-v2-3-9|2 Developer
  Workflow changes in v2.3.9]]'
- '[[Changes/OpenCode/2026-05-17-core-fixed-custom-lsp-servers-not-sending-refresh-events-after-they-initialize|Core
  Fixed custom LSP servers not sending refresh events after they initialize]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: developer-workflow
title: 12 Developer Workflow changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Developer Workflow changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `codex doctor` for support-ready diagnostics across runtime, auth, terminal, network, config, and local state. (#22336)

> #21628 Use `CARGO_NET_GIT_FETCH_WITH_CLI` in `rust-ci-full` for more reliable git fetches @zanie-oai

> #21738 extension: move git attribution into an extension @jif-oai

> #20305 fix(exec-policy) use is_known_safe_command less @dylan-hurd-oai

> #18748 [codex-analytics] emit terminal review events @rhan-oai

> #22159 Add Windows hook command overrides @abhinav-oai

> #21946 fix(tui): handle hidden app git directives @fcoury-oai

> #21206 feat(tui): add ambient terminal pets @fcoury-oai

> #22246 [codex] Remove unused legacy shell tools @pakrym-oai

> #22535 Remove resurrected `/collab` slash command @etraut-openai

> #22652 [codex] Ignore fsmonitor config in Git metadata reads @bookholt-oai

> #22717 chore(config) rm windows_wsl_setup_acknowledged @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-17 · OpenCode · [[Changes/OpenCode/2026-05-17-core-fixed-custom-lsp-servers-not-sending-refresh-events-after-they-initialize|Core Fixed custom LSP servers not sending refresh events after they initialize]]
- Later: 2026-05-18 · OpenCode · [[Changes/OpenCode/2026-05-18-5-developer-workflow-changes-in-v1-15-5|5 Developer Workflow changes in v1.15.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-5d5470&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-5d5470%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->