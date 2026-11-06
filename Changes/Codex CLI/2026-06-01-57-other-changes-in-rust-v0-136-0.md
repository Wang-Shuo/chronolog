---
card_id: codex-cli-2026-06-01-79e0eb
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Other changes: 57 changes in 0.136.0 — TUI
  markdown now keeps web links clickable with OSC 8 metadata, and cramped tables switch
  to…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6a32a485f5a5d0d7c1e9a7352a30bf04a9b6e3a57a740711afd069318a4ea218
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-79e0eb
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 57 other changes'
  evidence:
  - quote: 'TUI markdown now keeps web links clickable with OSC 8 metadata, and cramped
      tables switch to readable key/value records without losing link targets. (#24472,
      #24636, #24825)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Sessions can now be archived from the TUI with `/archive` or from the
      CLI with `codex archive` / `codex unarchive`; archived sessions are protected
      from resume/fork until restored. (#25027, #25021)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Resumed TUI sessions seed prompt history from the session transcript,
      multiline hook output renders as separate rows, and Vim normal-mode editing
      behaves correctly. (#24298, #24965, #25022)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Bedrock auth now falls back to `AWS_REGION` / `AWS_DEFAULT_REGION`, and
      unsupported Bedrock GPT service tiers are no longer advertised or sent. (#25171,
      #25318)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: The bundled OpenAI Docs skill was updated with current Codex manual routing
      and a cached manual fetch helper. (#24914)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Trimmed CI/build maintenance by moving Bazel Windows jobs to Codex runners,
      removing the libubsan workaround, and reverting the startup benchmark that broke
      musl builders. (#24952, #24782, #24937)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24472 feat(tui): add OSC 8 web links to rich content @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24636 feat(tui): render cramped markdown tables as key-value records
      [2 of 2] @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24666 Allow API-key auth for remote exec-server registration @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24763 Update rmcp to 1.7.0 @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24819 [codex] Remove redundant SQLite dynamic tool storage @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24830 Treat refresh_token_reused 400s as relogin-required @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24891 Stabilize Guardian client cache key handling @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24895 Thread Guardian cache key through session @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24902 [codex] Fix Guardian argument comment lint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24897 Add Guardian review metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24915 Add thread start contributor facts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24916 Add turn error lifecycle contributor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24865 [codex] Store pending response items directly @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24914 [codex] Update OpenAI Docs skill @vb-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24651 Add app-server startup benchmark crate @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24925 Gate goal tools by thread eligibility @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24782 Remove libubsan CI workaround @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24813 extension-api: add TurnItemEmitter to tool calls @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23534 feat(app-server): include turns page on thread resume @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24936 Fix extension turn item emitter test event ordering @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24700 [codex] Support ui visibility meta for tools @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24937 Revert "Add app-server startup benchmark crate" @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24952 Move Bazel Windows jobs onto codex-runners @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24940 Add `codex app-server --stdio` alias @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24949 [codex] Handle PowerShell UTF-8 setup failures @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23768 runtime: prepend zsh fork bin dir to PATH @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24947 fix(exec-server): reject websocket requests with Origin headers
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24653 [codex] Add user input client ids @alexi-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24962 Tighten hook output event schemas @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24970 fix(config): use deny for Unix socket permissions @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24977 Add runtime extra skill roots API @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24298 Seed prompt history from resumed messages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23943 fix: preserve deny-read sandboxing for safe commands @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24716 Fix fs/watch debounce batching @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24924 Use inject_if_running for active goal steering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25075 fix: main @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24794 [codex] Improve built-in tool schema docs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25095 Handle goal usage limits from turn errors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25106 Remove stale rollout TODO tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24965 Render multiline hook output in TUI @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25017 Align TUI permissions labels with app @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25035 Use session wording in `/rename` confirmation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25116 [exec-server] Kill dropped filesystem helpers @erichoracek'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24180 code-mode: introduce durable session interface @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25134 ci: use issue triage environment for issue workflows @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25118 exec-server: preserve fs helper CoreFoundation env @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25022 [codex] Fix Vim normal mode editing @jinghanx88'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25161 Recommend Bazel VSCode extension. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25171 fix: Bedrock API key region fallback @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24541 feat(config) experimental_request_user_input toggle @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#25021 Add thread archive CLI commands @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 57-other-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: uncategorized
  title: 57 other changes in rust-v0.136.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: uncategorized
title: 57 other changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 57 other changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> TUI markdown now keeps web links clickable with OSC 8 metadata, and cramped tables switch to readable key/value records without losing link targets. (#24472, #24636, #24825)

> Sessions can now be archived from the TUI with `/archive` or from the CLI with `codex archive` / `codex unarchive`; archived sessions are protected from resume/fork until restored. (#25027, #25021)

> Resumed TUI sessions seed prompt history from the session transcript, multiline hook output renders as separate rows, and Vim normal-mode editing behaves correctly. (#24298, #24965, #25022)

> Bedrock auth now falls back to `AWS_REGION` / `AWS_DEFAULT_REGION`, and unsupported Bedrock GPT service tiers are no longer advertised or sent. (#25171, #25318)

> The bundled OpenAI Docs skill was updated with current Codex manual routing and a cached manual fetch helper. (#24914)

> Trimmed CI/build maintenance by moving Bazel Windows jobs to Codex runners, removing the libubsan workaround, and reverting the startup benchmark that broke musl builders. (#24952, #24782, #24937)

> #24472 feat(tui): add OSC 8 web links to rich content @fcoury-oai

> #24636 feat(tui): render cramped markdown tables as key-value records [2 of 2] @fcoury-oai

> #24666 Allow API-key auth for remote exec-server registration @sdcoffey

> #24763 Update rmcp to 1.7.0 @anp-oai

> #24819 [codex] Remove redundant SQLite dynamic tool storage @sayan-oai

> #24830 Treat refresh_token_reused 400s as relogin-required @alexsong-oai

> #24891 Stabilize Guardian client cache key handling @jif-oai

> #24895 Thread Guardian cache key through session @jif-oai

> #24902 [codex] Fix Guardian argument comment lint @jif-oai

> #24897 Add Guardian review metrics @jif-oai

> #24915 Add thread start contributor facts @jif-oai

> #24916 Add turn error lifecycle contributor @jif-oai

> #24865 [codex] Store pending response items directly @pakrym-oai

> #24914 [codex] Update OpenAI Docs skill @vb-openai

> #24651 Add app-server startup benchmark crate @anp-oai

> #24925 Gate goal tools by thread eligibility @jif-oai

> #24782 Remove libubsan CI workaround @anp-oai

> #24813 extension-api: add TurnItemEmitter to tool calls @sayan-oai

> #23534 feat(app-server): include turns page on thread resume @btraut-openai

> #24936 Fix extension turn item emitter test event ordering @bolinfest

> #24700 [codex] Support ui visibility meta for tools @gpeal

> #24937 Revert "Add app-server startup benchmark crate" @anp-oai

> #24952 Move Bazel Windows jobs onto codex-runners @anp-oai

> #24940 Add `codex app-server --stdio` alias @anp-oai

> #24949 [codex] Handle PowerShell UTF-8 setup failures @iceweasel-oai

> #23768 runtime: prepend zsh fork bin dir to PATH @bolinfest

> #24947 fix(exec-server): reject websocket requests with Origin headers @viyatb-oai

> #24653 [codex] Add user input client ids @alexi-openai

> #24962 Tighten hook output event schemas @abhinav-oai

> #24970 fix(config): use deny for Unix socket permissions @viyatb-oai

> #24977 Add runtime extra skill roots API @xl-openai

> #24298 Seed prompt history from resumed messages @etraut-openai

> #23943 fix: preserve deny-read sandboxing for safe commands @bolinfest

> #24716 Fix fs/watch debounce batching @etraut-openai

> #24924 Use inject_if_running for active goal steering @jif-oai

> #25075 fix: main @jif-oai

> #24794 [codex] Improve built-in tool schema docs @jif-oai

> #25095 Handle goal usage limits from turn errors @jif-oai

> #25106 Remove stale rollout TODO tests @jif-oai

> #24965 Render multiline hook output in TUI @abhinav-oai

> #25017 Align TUI permissions labels with app @etraut-openai

> #25035 Use session wording in `/rename` confirmation @etraut-openai

> #25116 [exec-server] Kill dropped filesystem helpers @erichoracek

> #24180 code-mode: introduce durable session interface @cconger

> #25134 ci: use issue triage environment for issue workflows @etraut-openai

> #25118 exec-server: preserve fs helper CoreFoundation env @starr-openai

> #25022 [codex] Fix Vim normal mode editing @jinghanx88

> #25161 Recommend Bazel VSCode extension. @anp-oai

> #25171 fix: Bedrock API key region fallback @celia-oai

> #24541 feat(config) experimental_request_user_input toggle @dylan-hurd-oai

> #25021 Add thread archive CLI commands @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11 Developer Workflow changes in rust-v0.136.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model Support changes in rust-v0.136.0]] · Model Support
- [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]] · Context Window
- [[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3 Search and Browsing changes in rust-v0.136.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-01-2-interface-experience-changes-in-rust-v0-136-0|2 Interface Experience changes in rust-v0.136.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image Generation changes in rust-v0.136.0]] · Image Generation
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-79e0eb&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-57-other-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-79e0eb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->