---
card_id: codex-cli-2026-05-07-b37945
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Accessibility and Localization: TUI startup
  and accessibility were tightened by bounding terminal probes, clearing the first
  inline…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|ChatGPT
    now supports a limited selection of languages in the interface]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 969
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: accessibility-localization
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 169672d951bc44c068648aa10af4b387b63059b57ab2787924b94e6d44afaf4b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-b37945
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: TUI startup and accessibility were tightened
    by bounding terminal probes, clearing the first inline viewport render, and honoring
    `animations = false` for live rows. (#20654, #21450, #20564)'
  evidence:
  - quote: 'TUI startup and accessibility were tightened by bounding terminal probes,
      clearing the first inline viewport render, and honoring `animations = false`
      for live rows. (#20654, #21450, #20564)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: accessibility-localization
  theme_matches:
  - matched_terms:
    - accessibility
    score: 50
    theme: accessibility-localization
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: TUI startup and accessibility were tightened by bounding terminal probes,
    clearing…
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-19-improve-quick-help-accessibility-screen-reader-friendly-tab-labels-reordered-lay|Improve
  quick help accessibility]]'
- '[[Changes/GitHub Copilot CLI/2026-03-09-table-disables-borders-in-screen-reader-mode-to-prevent-announcing-decorative-ch|Table
  disables borders in screen reader mode to prevent announcing decorative characters]]'
- '[[Changes/GitHub Copilot CLI/2026-03-17-improve-color-contrast-across-cli-themes-for-better-readability-and-accessibilit|Improve
  color contrast across CLI themes for better readability and accessibility]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: accessibility-localization
title: TUI startup and accessibility were tightened by bounding terminal probes, clearing…
type: change
---

<!-- chronolog:begin region="header" -->
# TUI startup and accessibility were tightened by bounding terminal probes, clearing…

**Codex CLI** · 2026-05-07 · [[Themes/accessibility-localization|Accessibility and Localization]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> TUI startup and accessibility were tightened by bounding terminal probes, clearing the first inline viewport render, and honoring `animations = false` for live rows. (#20654, #21450, #20564)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.129.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0|39 Apps and Integrations changes in rust-v0.129.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-07-3-mobile-and-desktop-changes-in-rust-v0-129-0|3 Mobile and Desktop changes in rust-v0.129.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-07-3-collaboration-changes-in-rust-v0-129-0|3 Collaboration changes in rust-v0.129.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065 feat(tui): redesign session picker @fcoury-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Model Support
- [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Accessibility and Localization

- Earlier: 2026-03-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-17-improve-color-contrast-across-cli-themes-for-better-readability-and-accessibilit|Improve color contrast across CLI themes for better readability and accessibility]]
- Later: 2026-06-12 · Claude Code · [[Changes/Claude Code/2026-06-12-session-titles-are-now-generated-in-the-language-of-your-conversation-set-the-la|Session titles are now generated in the language of your conversation…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-09-11 · ChatGPT · [[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|ChatGPT now supports a limited selection of languages in the interface]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-b37945&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin.md%0ACard%20ID%3A%20codex-cli-2026-05-07-b37945%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->