---
card_id: codex-cli-2026-09-22-ec4899
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Safety and Privacy: 50 changes in 0.156.0 —
  Close sandbox isolation gaps involving inbound Windows connections, privileged Linux/macOS…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1255
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3b62e150037320e295ad43ae7f7ab87ca4d527f8c529bd40e26315a74514e353
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-ec4899
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 50 Safety and Privacy changes'
  evidence:
  - quote: 'Close sandbox isolation gaps involving inbound Windows connections, privileged
      Linux/macOS sockets, and writes through read-only macOS file handles. (#44639,
      #45984, #46500)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44617 Invalidate cached Guardian approvals for unscored permission widening
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44639 Block non-loopback inbound traffic for the Windows offline sandbox
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44658 Keep Windows sandbox private desktops alive across helper exits
      @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44676 Resolve permission profiles with explicit execution-host path context
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44694 Include the Windows sandbox service in release artifacts @johnl-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44755 Check folder consent before creating or resuming TUI tasks @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44872 Add managed network policy support to the Windows MXC sandbox @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44939 Respect execution hosts in Windows sandbox setup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44945 Route TUI Windows sandbox setup through the app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45169 Extract Windows sandbox setup and installation storage into the
      library @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45176 Wire the Windows MXC sandbox into command execution @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45178 Split Windows sandbox cleanup into preparation and completion phases
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45182 Validate Windows sandbox token groups before copying SIDs @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45224 Register Windows desktop uninstall ownership before sandbox setup
      @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45312 Extract Windows sandbox configuration preparation into a helper
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45455 Refactor Windows sandbox setup and service helpers @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45520 Add dependencies to the Windows sandbox service @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45533 Harden and share Windows sandbox identity helpers @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45534 Honor explicit Unix socket grants in the Linux managed sandbox
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45542 Add service-managed package registration for Windows sandbox accounts
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45550 Add opt-in registered package execution to the Windows sandbox
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45559 Resume Windows sandbox registration refresh after service restarts
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45730 Separate executor sandbox selection from Windows sandbox levels
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45737 Separate Windows sandbox implementations from legacy setup modes
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45757 Wire Windows sandbox selection into managed proxy routing @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45799 Complete Windows sandbox uninstall cleanup @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45813 Track Windows sandbox policy and per-thread executor hosts in the
      TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45821 Use app-server state for TUI Windows sandbox decisions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45830 Use app-server configuration for Windows sandbox state in the TUI
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45852 Preserve executor path conventions in permission summaries @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45863 Preserve executor path URIs in permission profile workspace roots
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45981 Preserve session config when switching thread permission profiles
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46008 Route built-in permission selections through the app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46013 Route permission shortcuts through the shared selection flow @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46038 Test Windows sandbox bin DACL modification permissions @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46043 Repair expired Windows sandbox account passwords during setup @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46112 Preserve filesystem sandbox policy context when the cwd disappears
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46122 Route filesystem reads and writes by their own sandbox permissions
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46126 Record daemon startup and update telemetry with consent handling
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46237 Improve Windows sandbox error details and registry cleanup @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46239 Prefer the provisioning service for automatic Windows sandbox setup
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46241 Repair Windows sandbox access to existing runtime children @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46271 Enable MXC selection through Windows sandbox configuration @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46322 Set the Windows sandbox type in the pending environment test @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46333 Handle disabled Windows sandbox accounts during cleanup @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46334 Share platform identity across path, network, and sandbox configuration
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46507 Run Windows sandbox tests exclusively when local @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46535 Allow unrelated namespace mounts in Linux sandbox socket checks
      @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46981 Canonicalize the workspace trust key in the doctor config test
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 50-safety-and-privacy-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: safety-privacy
  title: 50 Safety and Privacy changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-21-use-your-connected-tools-from-lovable-in-telegram|Use
  your connected tools from Lovable in Telegram]]'
- '[[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety
  and Privacy changes in v0.11.4]]'
- '[[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety
  and Privacy changes in v2.1.280]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: safety-privacy
title: 50 Safety and Privacy changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 50 Safety and Privacy changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Close sandbox isolation gaps involving inbound Windows connections, privileged Linux/macOS sockets, and writes through read-only macOS file handles. (#44639, #45984, #46500)

> #44617 Invalidate cached Guardian approvals for unscored permission widening @jif-oai

> #44639 Block non-loopback inbound traffic for the Windows offline sandbox @viyatb-oai

> #44658 Keep Windows sandbox private desktops alive across helper exits @chess-oai

> #44676 Resolve permission profiles with explicit execution-host path context @seanh-oai

> #44694 Include the Windows sandbox service in release artifacts @johnl-oai

> #44755 Check folder consent before creating or resuming TUI tasks @etraut-openai

> #44872 Add managed network policy support to the Windows MXC sandbox @iceweasel-oai

> #44939 Respect execution hosts in Windows sandbox setup @etraut-openai

> #44945 Route TUI Windows sandbox setup through the app server @etraut-openai

> #45169 Extract Windows sandbox setup and installation storage into the library @zm-oai

> #45176 Wire the Windows MXC sandbox into command execution @iceweasel-oai

> #45178 Split Windows sandbox cleanup into preparation and completion phases @zm-oai

> #45182 Validate Windows sandbox token groups before copying SIDs @zm-oai

> #45224 Register Windows desktop uninstall ownership before sandbox setup @chess-oai

> #45312 Extract Windows sandbox configuration preparation into a helper @seanh-oai

> #45455 Refactor Windows sandbox setup and service helpers @zm-oai

> #45520 Add dependencies to the Windows sandbox service @zm-oai

> #45533 Harden and share Windows sandbox identity helpers @zm-oai

> #45534 Honor explicit Unix socket grants in the Linux managed sandbox @viyatb-oai

> #45542 Add service-managed package registration for Windows sandbox accounts @zm-oai

> #45550 Add opt-in registered package execution to the Windows sandbox @zm-oai

> #45559 Resume Windows sandbox registration refresh after service restarts @zm-oai

> #45730 Separate executor sandbox selection from Windows sandbox levels @iceweasel-oai

> #45737 Separate Windows sandbox implementations from legacy setup modes @iceweasel-oai

> #45757 Wire Windows sandbox selection into managed proxy routing @iceweasel-oai

> #45799 Complete Windows sandbox uninstall cleanup @chess-oai

> #45813 Track Windows sandbox policy and per-thread executor hosts in the TUI @etraut-openai

> #45821 Use app-server state for TUI Windows sandbox decisions @etraut-openai

> #45830 Use app-server configuration for Windows sandbox state in the TUI @etraut-openai

> #45852 Preserve executor path conventions in permission summaries @seanh-oai

> #45863 Preserve executor path URIs in permission profile workspace roots @seanh-oai

> #45981 Preserve session config when switching thread permission profiles @etraut-openai

> #46008 Route built-in permission selections through the app server @etraut-openai

> #46013 Route permission shortcuts through the shared selection flow @etraut-openai

> #46038 Test Windows sandbox bin DACL modification permissions @zm-oai

> #46043 Repair expired Windows sandbox account passwords during setup @zm-oai

> #46112 Preserve filesystem sandbox policy context when the cwd disappears @anp-oai

> #46122 Route filesystem reads and writes by their own sandbox permissions @anp-oai

> #46126 Record daemon startup and update telemetry with consent handling @etraut-openai

> #46237 Improve Windows sandbox error details and registry cleanup @chess-oai

> #46239 Prefer the provisioning service for automatic Windows sandbox setup @zm-oai

> #46241 Repair Windows sandbox access to existing runtime children @chess-oai

> #46271 Enable MXC selection through Windows sandbox configuration @iceweasel-oai

> #46322 Set the Windows sandbox type in the pending environment test @sayan-oai

> #46333 Handle disabled Windows sandbox accounts during cleanup @chess-oai

> #46334 Share platform identity across path, network, and sandbox configuration @seanh-oai

> #46507 Run Windows sandbox tests exclusively when local @jif-oai

> #46535 Allow unrelated namespace mounts in Linux sandbox socket checks @pash-openai

> #46981 Canonicalize the workspace trust key in the doctor config test @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]]
- Later: 2026-09-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-ec4899&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-ec4899%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->