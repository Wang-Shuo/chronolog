---
card_id: codex-cli-2026-09-22-7c4828
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Mobile and Desktop: 11 changes in 0.156.0 —
  #44613 Enable user verification for local Codex Desktop sessions @riley-oai'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2872
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0941b485c12afea95cc6a1daa7bd1ed87f78ab22149d8a9b0e65c2e340e3f326
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-7c4828
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 11 Mobile and Desktop changes'
  evidence:
  - quote: '#44613 Enable user verification for local Codex Desktop sessions @riley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45345 Publish opt-in provisioned macOS packages with Rust releases @riley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45982 Use native DNS resolution for the network proxy on macOS @jdkula-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46032 Require forced macOS preferences for managed configuration @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46486 Make TUI async question replies compatible with desktop @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46495 Preserve the provisioned macOS CLI''s code-signing identity @riley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46500 Block mutating fcntls in restricted macOS Seatbelt policies @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46521 Use macOS member fallback in shared process-group termination helpers
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46571 Preserve macOS Seatbelt exclusions in scratch directories @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46583 Deny XPC service lookups in macOS Seatbelt profiles @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46661 Avoid fork when spawning macOS filesystem helpers @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-mobile-and-desktop-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: mobile-desktop
  title: 11 Mobile and Desktop changes in rust-v0.156.0
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|\U0001F4F1
  Apple device replies. An assistant reply no longer comes up blank in a home…]]"
- '[[Changes/AnythingLLM/2026-09-22-x-removed-the-borders-around-the-main-content-area-for-a-cleaner-desktop-layout|x
  Removed the borders around the main content area for a cleaner desktop layout]]'
- '[[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules
  are found and shown consistently]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: mobile-desktop
title: 11 Mobile and Desktop changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Mobile and Desktop changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #44613 Enable user verification for local Codex Desktop sessions @riley-oai

> #45345 Publish opt-in provisioned macOS packages with Rust releases @riley-oai

> #45982 Use native DNS resolution for the network proxy on macOS @jdkula-openai

> #46032 Require forced macOS preferences for managed configuration @joeflorencio-openai

> #46486 Make TUI async question replies compatible with desktop @etraut-openai

> #46495 Preserve the provisioned macOS CLI's code-signing identity @riley-oai

> #46500 Block mutating fcntls in restricted macOS Seatbelt policies @nornagon-openai

> #46521 Use macOS member fallback in shared process-group termination helpers @jif-oai

> #46571 Preserve macOS Seatbelt exclusions in scratch directories @nornagon-openai

> #46583 Deny XPC service lookups in macOS Seatbelt profiles @nornagon-openai

> #46661 Avoid fork when spawning macOS filesystem helpers @charliemarsh-oai

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
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-22 · Cline · [[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules are found and shown consistently]]
- Later: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-7c4828&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-7c4828%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->