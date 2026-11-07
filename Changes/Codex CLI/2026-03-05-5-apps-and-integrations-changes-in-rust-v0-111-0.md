---
card_id: codex-cli-2026-03-05-be9549
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Apps and Integrations: 5 changes in 0.111.0
  — Codex now tells the model which plugins are enabled at session start, improving…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2638
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 731d41a91bce6f33e30cdee20de9bd1ddb4e9485936689aee418ff94057471c4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-be9549
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.111.0: 5 Apps and Integrations changes'
  evidence:
  - quote: Codex now tells the model which plugins are enabled at session start, improving
      discovery of installed MCPs, apps, and skills. (#13433)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.111.0
  - quote: App-server v2 now exposes MCP elicitation as a structured request/response
      flow instead of raw events, which simplifies client integrations. (#13425)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.111.0
  - quote: '#13433 feat: track plugins mcps/apps and add plugin info to user_instructions
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.111.0
  - quote: '#13533 [apps] Fix the issue where apps is not enabled after codex resume.
      @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.111.0
  - quote: '#13425 feat(app-server): support mcp elicitations in v2 api @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.111.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-apps-and-integrations-changes-in-rust-v0-111-0
  source_release: codex-cli-2026-03-05-rust-v0-111-0-github-293639875-9259bb82
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in rust-v0.111.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added
  /reload-plugins command to activate pending plugin changes without restarting]]'
- '[[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps
  and Integrations changes in v2.1.69]]'
- '[[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7
  Apps and Integrations changes in rust-v0.110.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-111-0-github-293639875-9259bb82|codex-cli-2026-03-05-rust-v0-111-0-github-293639875-9259bb82]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in rust-v0.111.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in rust-v0.111.0

**Codex CLI** · 2026-03-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.111.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-111-0-github-293639875-9259bb82|0.111.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Codex now tells the model which plugins are enabled at session start, improving discovery of installed MCPs, apps, and skills. (#13433)

> App-server v2 now exposes MCP elicitation as a structured request/response flow instead of raw events, which simplifies client integrations. (#13425)

> #13433 feat: track plugins mcps/apps and add plugin info to user_instructions @sayan-oai

> #13533 [apps] Fix the issue where apps is not enabled after codex resume. @mzeng-openai

> #13425 feat(app-server): support mcp elicitations in v2 api @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.111.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-2-voice-and-audio-changes-in-rust-v0-111-0|2 Voice and Audio changes in rust-v0.111.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-05-resuming-a-thread-now-preserves-its-stored-git-context-and-keeps-apps-enabled-av|Resuming a thread now preserves its stored git context and keeps apps enabled…]] · Context Window
- [[Changes/Codex CLI/2026-03-05-expanded-image-workflow-support-for-clients-including-client-side-handling-of-im|Expanded image workflow support for clients, including client-side handling…]] · Image Generation
- [[Changes/Codex CLI/2026-03-05-added-sample-skill-documentation-for-artifact-workflows-including-slide-deck-and|Added sample skill documentation for artifact workflows, including slide deck…]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13538-chore-add-web-search-tool-type-for-image-support-sayan-oai|♯13538 chore: add web_search_tool_type for image support @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-05-13446-tui-show-speed-in-session-header-pash-openai|♯13446 tui Show speed in session header @pash-openai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-03-05-13504-preserve-persisted-thread-git-info-in-resume-joeytrasatti-openai|♯13504 Preserve persisted thread git info in resume @joeytrasatti-openai]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-fast-mode-is-now-enabled-by-default-and-the-tui-header-shows-whether-the-session|Fast mode is now enabled by default, and the TUI header shows whether the session…]] · Other changes
- [[Changes/Codex CLI/2026-03-05-15-other-changes-in-rust-v0-111-0|15 other changes in rust-v0.111.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]]
- Later: 2026-03-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-05-11-apps-and-integrations-changes-in-v0-0-422|11 Apps and Integrations changes in v0.0.422]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-be9549&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-5-apps-and-integrations-changes-in-rust-v0-111-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-be9549%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.111.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->