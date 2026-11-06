---
card_id: codex-cli-2026-09-22-16a747
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Interface Experience: 32 changes in 0.156.0
  — Choose an optional fullscreen UI with `/tui` for your next launch, including transcript…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1352
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9e52654996e7cffc1fe9d470adee19378f2438f49fa0711fe37f3bd8834c5057
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-16a747
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 32 Interface Experience changes'
  evidence:
  - quote: 'Choose an optional fullscreen UI with `/tui` for your next launch, including
      transcript search, mouse selection, and right-click copying. (#46732, #46734,
      #46883, #46895)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: 'Preserve streamed answers and plans when turns fail, are interrupted,
      or receive subagent completion events. (#45549, #46867)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45770 Improve analytics chart readability and navigation @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45772 Expose experimental analytics plan history and improve navigation
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45854 Add `/daemon` menu for local background server updates @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46266 Expand Unicode math rendering with accents, symbols, and delimiters
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46310 Defer environment selection changes until the next turn @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46516 Handle completion timing in the multi-agent resume test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46552 Move child completion routing into the agent controller @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46557 Fix active-turn environment selection lookup @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46680 Improve TUI contrast, keyboard hints, and picker layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46691 Standardize TUI picker presentation and fix wrapping boundaries
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46692 Unify TUI picker styling and improve compact layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46695 Unify TUI prompts with shared picker styling and layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46697 Unify TUI picker styling and improve compact session layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46709 Add compact activity rendering and preserve transcript source text
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46720 Cache transcript layouts across measurement and rendering @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46721 Anchor transcript scrolling to entries and bound viewport rendering
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46722 Cancel pending transcript Home jumps on subsequent navigation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46732 Add selection and copying to the transcript viewer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46752 Add an animated Codex logo to fresh conversations and onboarding
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46837 Improve agent command center rows and page navigation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46840 Simplify agent command center hints and back navigation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46849 Move fullscreen transcript control to TUI configuration @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46857 Extract shared text selection helpers for the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46858 Add mouse selection and editing to the fullscreen composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46859 Limit the welcome logo animation to onboarding @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46863 Stabilize usage dashboard navigation and add keyboard help @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46866 Enable mouse navigation in the TUI usage view @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46879 Count TUI launches by fullscreen transcript configuration @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46931 Use shared, keymap-aware tips in the fullscreen composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46938 Add independent TUI rendering toggles for Mermaid, math, and tables
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 32-interface-experience-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: interface-experience
  title: 32 Interface Experience changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key
  selection in the question dialog works for choices 10 and beyond]]'
- '[[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface
  Experience changes in v0.11.4]]'
- '[[Changes/Claude Code/2026-09-22-5-interface-experience-changes-in-v2-1-280|5 Interface
  Experience changes in v2.1.280]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: interface-experience
title: 32 Interface Experience changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 32 Interface Experience changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Choose an optional fullscreen UI with `/tui` for your next launch, including transcript search, mouse selection, and right-click copying. (#46732, #46734, #46883, #46895)

> Preserve streamed answers and plans when turns fail, are interrupted, or receive subagent completion events. (#45549, #46867)

> #45770 Improve analytics chart readability and navigation @fcoury-oai

> #45772 Expose experimental analytics plan history and improve navigation @fcoury-oai

> #45854 Add `/daemon` menu for local background server updates @etraut-openai

> #46266 Expand Unicode math rendering with accents, symbols, and delimiters @etraut-openai

> #46310 Defer environment selection changes until the next turn @sayan-oai

> #46516 Handle completion timing in the multi-agent resume test @jif-oai

> #46552 Move child completion routing into the agent controller @jif-oai

> #46557 Fix active-turn environment selection lookup @sayan-oai

> #46680 Improve TUI contrast, keyboard hints, and picker layouts @etraut-openai

> #46691 Standardize TUI picker presentation and fix wrapping boundaries @etraut-openai

> #46692 Unify TUI picker styling and improve compact layouts @etraut-openai

> #46695 Unify TUI prompts with shared picker styling and layouts @etraut-openai

> #46697 Unify TUI picker styling and improve compact session layouts @etraut-openai

> #46709 Add compact activity rendering and preserve transcript source text @etraut-openai

> #46720 Cache transcript layouts across measurement and rendering @etraut-openai

> #46721 Anchor transcript scrolling to entries and bound viewport rendering @etraut-openai

> #46722 Cancel pending transcript Home jumps on subsequent navigation @etraut-openai

> #46732 Add selection and copying to the transcript viewer @etraut-openai

> #46752 Add an animated Codex logo to fresh conversations and onboarding @etraut-openai

> #46837 Improve agent command center rows and page navigation @etraut-openai

> #46840 Simplify agent command center hints and back navigation @etraut-openai

> #46849 Move fullscreen transcript control to TUI configuration @etraut-openai

> #46857 Extract shared text selection helpers for the TUI @etraut-openai

> #46858 Add mouse selection and editing to the fullscreen composer @etraut-openai

> #46859 Limit the welcome logo animation to onboarding @etraut-openai

> #46863 Stabilize usage dashboard navigation and add keyboard help @etraut-openai

> #46866 Enable mouse navigation in the TUI usage view @etraut-openai

> #46879 Count TUI launches by fullscreen transcript configuration @etraut-openai

> #46931 Use shared, keymap-aware tips in the fullscreen composer @etraut-openai

> #46938 Add independent TUI rendering toggles for Mermaid, math, and tables @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
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
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-5-interface-experience-changes-in-v2-1-280|5 Interface Experience changes in v2.1.280]]
- Later: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-4-interface-experience-changes-in-v2-1-281|4 Interface Experience changes in v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-16a747&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-32-interface-experience-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-16a747%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->