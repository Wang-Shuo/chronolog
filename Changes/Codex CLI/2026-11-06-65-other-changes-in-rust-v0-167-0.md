---
card_id: codex-cli-2026-11-06-a17d73
date: '2026-11-06'
description: 'Codex CLI · 2026-11-06 · Other changes: 65 changes in 0.167.0 — Preview
  local image attachments while composing on supported terminals, and open viewed
  local…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a3c450abf133bc3207419e1a62aabfb962447a2623692d31c041a8b0709e9286
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-11-06-a17d73
  comparison: ''
  date: '2026-11-06'
  description: 'Codex CLI — 0.167.0: 65 other changes'
  evidence:
  - quote: 'Preview local image attachments while composing on supported terminals,
      and open viewed local images from clickable transcript paths (#58261, #58446).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: Expand patch details directly in the transcript while an approval prompt
      is open (#58281).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: Deleting text that exposes a leading `!` keeps an ordinary draft in chat
      mode (#58412).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: 'Network approval prompts close when their requests end. Concurrent requests
      to the same endpoint prompt one at a time (#58350, #58351).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: 'DotSlash manifests now reference the Cargo packages shipped with the release
      (#58717, #58757).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57850 Wire bounded output collection into the code mode runtime @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57864 Allow upstream interruption when canceling Responses Lite turns
      @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57866 Retry transient environment startup failures on the next turn @pansul47-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57870 Enable server-side output truncation for Code Mode sessions @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#57876 Reuse the cached runtime keymap for default configuration @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58013 Fix argument comment lint tests after rust-clippy branch rename
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58025 Add trace-safe diagnostics for Noise relay request progress @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58028 Add direct Guardian review of recorded exec calls @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58034 Add an option to disable successful SSE delta logs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58040 Preserve native tool-call evidence through Guardian review @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58075 Use serving assessments for adaptive Guardian review @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58083 Use a dedicated binary for Bazel schema generation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58110 Ignore RUSTSEC-2026-0418 for the Windows-only libz-sys dependency
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58119 Add experimental Guardian review for injected thread commands @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58121 Centralize provider request preparation auth checks @sgarg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58122 Add an incremental exec tools feature flag @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58123 Add validated elastic section budget configuration for Guardian
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58125 Support negotiated server-side truncation in Code Mode clients
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58130 Support pasted search text in the skills toggle view @xma-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58157 Expose system proxy support as an experimental setting @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58159 Add a feature flag for code-mode host output truncation @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58171 Stabilize cancellation and tracing tests @aakash-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58182 Support managed network requirements under `permissions.network`
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58190 Allow providers to opt into Cyber access programs @jamy-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58195 Preserve remote read compatibility with older executors @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58196 Require Bazel release artifacts and publish DotSlash manifests
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58198 Centralize TOML config deserialization @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58221 Preserve realtime V3 transcripts in conversation history @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58237 Preserve unrelated side conversations when archiving or deleting
      threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58240 Enable TUI task tools for embedded app-server sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58241 Update `mio` from 1.2.0 to 1.2.4 @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58251 Reload remote executor credentials safely across token rotation
      @tgrue-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58260 Reuse `LocalImageAttachment` throughout the TUI composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58261 Add local image thumbnails to the TUI composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58270 Recognize Rex terminals and enable Kitty graphics for pets @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58281 Allow inline patch review during approval prompts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58324 Treat auth reload failures as transient during token refresh @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58343 Preserve fallback token refreshes when the keyring is unreadable
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58350 Resolve network approval prompts when their requests end @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58351 Serialize manual network approval prompts per endpoint @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58357 Extract pre-tool-use hook handling into a helper @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58380 Broadcast thread section changes to connected clients @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58381 Fix unsettled refresh detection after workspace switching @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58385 Test V8 inline typed array storage limits @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58399 Reduce jemalloc arena count for Linux musl builds @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58403 Run package updates outside the project on non-Windows platforms
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58406 Add host-inherited thread instructions and execution policies @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58410 Enable deferred tool world state by default @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58411 Expose non-consuming input activity waits to hosts @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58412 Keep exposed leading bangs literal in the chat composer @xma-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58436 Add interactive controls and refresh inline visualization styles
      @philipp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58446 Make viewed image paths clickable in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58456 Preserve incomplete response output in failed inference traces
      @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58457 Enable cross-backend session switching in the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58459 Tighten Bazel CI snapshot handling and OTLP test cleanup @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58713 Extract fresh session adoption from TUI session startup @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58716 Support OSC 52 clipboard forwarding through GNU screen @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58717 Make Bazel checks advisory and pause Bazel release artifacts @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58751 Release superseded assistant text from live paginated history @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58757 Remove Bazel outputs from DotSlash release configs @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 65-other-changes-in-rust-v0-167-0
  source_release: codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc
  source_type: github_releases
  theme: uncategorized
  title: 65 other changes in rust-v0.167.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc]]'
source_type: github_releases
theme: uncategorized
title: 65 other changes in rust-v0.167.0
type: change
---

<!-- chronolog:begin region="header" -->
# 65 other changes in rust-v0.167.0

**Codex CLI** · 2026-11-06 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.167.0) · from [[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preview local image attachments while composing on supported terminals, and open viewed local images from clickable transcript paths (#58261, #58446).

> Expand patch details directly in the transcript while an approval prompt is open (#58281).

> Deleting text that exposes a leading `!` keeps an ordinary draft in chat mode (#58412).

> Network approval prompts close when their requests end. Concurrent requests to the same endpoint prompt one at a time (#58350, #58351).

> DotSlash manifests now reference the Cargo packages shipped with the release (#58717, #58757).

> #57850 Wire bounded output collection into the code mode runtime @seanh-oai

> #57864 Allow upstream interruption when canceling Responses Lite turns @liame-oai

> #57866 Retry transient environment startup failures on the next turn @pansul47-oai

> #57870 Enable server-side output truncation for Code Mode sessions @seanh-oai

> #57876 Reuse the cached runtime keymap for default configuration @bc-openai

> #58013 Fix argument comment lint tests after rust-clippy branch rename @seanh-oai

> #58025 Add trace-safe diagnostics for Noise relay request progress @apanasenko-oai

> #58028 Add direct Guardian review of recorded exec calls @swastik-oai

> #58034 Add an option to disable successful SSE delta logs @jif-oai

> #58040 Preserve native tool-call evidence through Guardian review @ioanbudea-OAI

> #58075 Use serving assessments for adaptive Guardian review @jif-oai

> #58083 Use a dedicated binary for Bazel schema generation @jif-oai

> #58110 Ignore RUSTSEC-2026-0418 for the Windows-only libz-sys dependency @swastik-oai

> #58119 Add experimental Guardian review for injected thread commands @swastik-oai

> #58121 Centralize provider request preparation auth checks @sgarg-oai

> #58122 Add an incremental exec tools feature flag @akira-oai

> #58123 Add validated elastic section budget configuration for Guardian @ioanbudea-OAI

> #58125 Support negotiated server-side truncation in Code Mode clients @seanh-oai

> #58130 Support pasted search text in the skills toggle view @xma-oai

> #58157 Expose system proxy support as an experimental setting @abhinav-oai

> #58159 Add a feature flag for code-mode host output truncation @seanh-oai

> #58171 Stabilize cancellation and tracing tests @aakash-oai

> #58182 Support managed network requirements under `permissions.network` @viyatb-oai

> #58190 Allow providers to opt into Cyber access programs @jamy-OAI

> #58195 Preserve remote read compatibility with older executors @dkovalenko-oai

> #58196 Require Bazel release artifacts and publish DotSlash manifests @dkovalenko-oai

> #58198 Centralize TOML config deserialization @dkovalenko-oai

> #58221 Preserve realtime V3 transcripts in conversation history @guinness-oai

> #58237 Preserve unrelated side conversations when archiving or deleting threads @etraut-openai

> #58240 Enable TUI task tools for embedded app-server sessions @etraut-openai

> #58241 Update `mio` from 1.2.0 to 1.2.4 @euroelessar

> #58251 Reload remote executor credentials safely across token rotation @tgrue-openai

> #58260 Reuse `LocalImageAttachment` throughout the TUI composer @etraut-openai

> #58261 Add local image thumbnails to the TUI composer @etraut-openai

> #58270 Recognize Rex terminals and enable Kitty graphics for pets @etraut-openai

> #58281 Allow inline patch review during approval prompts @etraut-openai

> #58324 Treat auth reload failures as transient during token refresh @jif-oai

> #58343 Preserve fallback token refreshes when the keyring is unreadable @jif-oai

> #58350 Resolve network approval prompts when their requests end @charliemarsh-oai

> #58351 Serialize manual network approval prompts per endpoint @charliemarsh-oai

> #58357 Extract pre-tool-use hook handling into a helper @swastik-oai

> #58380 Broadcast thread section changes to connected clients @charliemarsh-oai

> #58381 Fix unsettled refresh detection after workspace switching @jif-oai

> #58385 Test V8 inline typed array storage limits @fcoury-oai

> #58399 Reduce jemalloc arena count for Linux musl builds @dkovalenko-oai

> #58403 Run package updates outside the project on non-Windows platforms @viyatb-oai

> #58406 Add host-inherited thread instructions and execution policies @rhan-oai

> #58410 Enable deferred tool world state by default @adaley-openai

> #58411 Expose non-consuming input activity waits to hosts @rhan-oai

> #58412 Keep exposed leading bangs literal in the chat composer @xma-oai

> #58436 Add interactive controls and refresh inline visualization styles @philipp-oai

> #58446 Make viewed image paths clickable in the TUI @etraut-openai

> #58456 Preserve incomplete response output in failed inference traces @cassirer-openai

> #58457 Enable cross-backend session switching in the TUI @bc-openai

> #58459 Tighten Bazel CI snapshot handling and OTLP test cleanup @imac-oai

> #58713 Extract fresh session adoption from TUI session startup @bc-openai

> #58716 Support OSC 52 clipboard forwarding through GNU screen @etraut-openai

> #58717 Make Bazel checks advisory and pause Bazel release artifacts @dkovalenko-oai

> #58751 Release superseded assistant text from live paginated history @btraut-openai

> #58757 Remove Bazel outputs from DotSlash release configs @fcoury-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.167.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-11-06-2-editor-experience-changes-in-rust-v0-167-0|2 Editor Experience changes in rust-v0.167.0]] · Editor Experience
- [[Changes/Codex CLI/2026-11-06-3-search-and-browsing-changes-in-rust-v0-167-0|3 Search and Browsing changes in rust-v0.167.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]] · Model Support
- [[Changes/Codex CLI/2026-11-06-8-context-window-changes-in-rust-v0-167-0|8 Context Window changes in rust-v0.167.0]] · Context Window
- [[Changes/Codex CLI/2026-11-06-6-developer-workflow-changes-in-rust-v0-167-0|6 Developer Workflow changes in rust-v0.167.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-11-06-4-voice-and-audio-changes-in-rust-v0-167-0|4 Voice and Audio changes in rust-v0.167.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2 Mobile and Desktop changes in rust-v0.167.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5 Account and Access changes in rust-v0.167.0]] · Account and Access
- [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Agent Mode
- [[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13 Interface Experience changes in rust-v0.167.0]] · Interface Experience
- [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0|12 Apps and Integrations changes in rust-v0.167.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-11-06-a17d73&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-11-06-65-other-changes-in-rust-v0-167-0.md%0ACard%20ID%3A%20codex-cli-2026-11-06-a17d73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.167.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->