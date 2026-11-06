---
card_id: codex-cli-2026-02-17-a591e2
date: '2026-02-17'
description: 'Codex CLI · 2026-02-17 · Other changes: 59 changes in 0.102.0 — Expanded
  app-server fuzzy file search with explicit session-complete signaling so clients
  can…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7a2440d557d8bf3ca4eba9ece93d91ddd8956a897dc24a2053903ed94b04cb8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-17-a591e2
  comparison: ''
  date: '2026-02-17'
  description: 'Codex CLI — 0.102.0: 59 other changes'
  evidence:
  - quote: 'Expanded app-server fuzzy file search with explicit session-complete signaling
      so clients can stop loading indicators reliably. (#10268, #11773)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: Updated contributor guidance to require snapshot coverage for user-visible
      TUI changes. (#10669)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: 'Improved developer log tooling with new `just log --search` and `just
      log --compact` modes. (#11995, #11994)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: 'Updated vendored `rg` and tightened Bazel/Cargo lockfile sync checks to
      reduce dependency drift. (#12007, #11790)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#10268 app-server: add fuzzy search sessions for streaming file search
      @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11227 feat(app-server): experimental flag to persist extended history
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#10672 Add js_repl host helpers and exec end events @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11631 chore(core) Deprecate approval_policy: on-failure @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11633 feat: introduce Permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#10669 docs: require insta snapshot coverage for UI changes @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11645 fix: skip review_start_with_detached_delivery_returns_new_thread_id
      o… @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11622 Remove absolute path in rollout_summary @wendyjiao-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11638 fix(app-server): surface more helpful errors for json-rpc @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11656 Persist complete TurnContextItem state via canonical conversion
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11275 Added a test to verify that feature flags that are enabled by default
      are stable @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11651 Add cwd as an optional field to thread/list @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11660 chore(approvals) More approvals scenarios @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11703 fix(ci) lock rust toolchain at 1.93.0 to unblock @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11662 feat(network-proxy): structured policy signaling and attempt correlation
      to core @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11722 Lower missing rollout log level @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11712 chore: streamline phase 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11736 feat: increase windows workers stack @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11739 feat: add slug in name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11745 chore: move explorer to spark @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11755 app-server-test-client websocket client and thread tools @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11695 Updated app bug report template @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11686 Report syntax errors in rules file @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11763 Update read_path prompt @zuxin-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11772 chore: mini @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11666 Add js_repl kernel crash diagnostics @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11687 support app usage analytics @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11769 Improve GitHub issue deduplication reliability by introducing a
      stage… @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11770 fix(nix): use correct version from Cargo.toml in flake build @rupurt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11677 turn metadata: per-turn non-blocking @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11692 rmcp-client: fix auth crash @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#10590 tui: preserve remote image attachments across resume/backtrack
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11782 turn metadata followups @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11773 [app-server] add fuzzyFileSearch/sessionCompleted @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11756 codex-rs: fix thread resume rejoin semantics @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11799 fix(protocol): make local image test Bazel-friendly @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11796 Fix js_repl view_image test runtime panic @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11800 Fix js_repl in-flight tool-call waiter race @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11790 bazel: enforce MODULE.bazel.lock sync with Cargo.lock @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11674 feat(tui): render structured network approval prompts in approval
      overlay @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11550 feat(tui) Permissions update history item @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11534 Add process_uuid to sqlite logs @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11690 fix: show user warning when using default fallback metadata @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11780 chore(tui): reduce noisy key logging @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11893 bazel: fix snapshot parity for tests/*.rs rust_test targets @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11926 docs: mention Codex app in README intro @vb-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11866 chore(core) rm Feature::RequestRule @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11951 fix(core) exec_policy parsing fixes @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11932 fix: js_repl reset hang by clearing exec tool calls without waiting
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11922 fix: race in js repl @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11908 Exit early when session initialization fails @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11995 feat: add `--search` to `just log` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11994 feat: add `--compact` mode to `just log` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#12007 Update vendored rg to the latest stable version (15.1) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11801 Add remote skill scope/product_surface/enabled params and cleanup
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 59-other-changes-in-rust-v0-102-0
  source_release: codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0
  source_type: github_releases
  theme: uncategorized
  title: 59 other changes in rust-v0.102.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0]]'
source_type: github_releases
theme: uncategorized
title: 59 other changes in rust-v0.102.0
type: change
---

<!-- chronolog:begin region="header" -->
# 59 other changes in rust-v0.102.0

**Codex CLI** · 2026-02-17 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.102.0) · from [[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|0.102.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded app-server fuzzy file search with explicit session-complete signaling so clients can stop loading indicators reliably. (#10268, #11773)

> Updated contributor guidance to require snapshot coverage for user-visible TUI changes. (#10669)

> Improved developer log tooling with new `just log --search` and `just log --compact` modes. (#11995, #11994)

> Updated vendored `rg` and tightened Bazel/Cargo lockfile sync checks to reduce dependency drift. (#12007, #11790)

> #10268 app-server: add fuzzy search sessions for streaming file search @nornagon-openai

> #11227 feat(app-server): experimental flag to persist extended history @owenlin0

> #10672 Add js_repl host helpers and exec end events @fjord-oai

> #11631 chore(core) Deprecate approval_policy: on-failure @dylan-hurd-oai

> #11633 feat: introduce Permissions @bolinfest

> #10669 docs: require insta snapshot coverage for UI changes @joshka-oai

> #11645 fix: skip review_start_with_detached_delivery_returns_new_thread_id o… @owenlin0

> #11622 Remove absolute path in rollout_summary @wendyjiao-openai

> #11638 fix(app-server): surface more helpful errors for json-rpc @owenlin0

> #11656 Persist complete TurnContextItem state via canonical conversion @charley-oai

> #11275 Added a test to verify that feature flags that are enabled by default are stable @etraut-openai

> #11651 Add cwd as an optional field to thread/list @acrognale-oai

> #11660 chore(approvals) More approvals scenarios @dylan-hurd-oai

> #11703 fix(ci) lock rust toolchain at 1.93.0 to unblock @dylan-hurd-oai

> #11662 feat(network-proxy): structured policy signaling and attempt correlation to core @viyatb-oai

> #11722 Lower missing rollout log level @jif-oai

> #11712 chore: streamline phase 2 @jif-oai

> #11736 feat: increase windows workers stack @jif-oai

> #11739 feat: add slug in name @jif-oai

> #11745 chore: move explorer to spark @jif-oai

> #11755 app-server-test-client websocket client and thread tools @maxj-oai

> #11695 Updated app bug report template @etraut-openai

> #11686 Report syntax errors in rules file @etraut-openai

> #11763 Update read_path prompt @zuxin-oai

> #11772 chore: mini @jif-oai

> #11666 Add js_repl kernel crash diagnostics @fjord-oai

> #11687 support app usage analytics @alexsong-oai

> #11769 Improve GitHub issue deduplication reliability by introducing a stage… @etraut-openai

> #11770 fix(nix): use correct version from Cargo.toml in flake build @rupurt

> #11677 turn metadata: per-turn non-blocking @pash-openai

> #11692 rmcp-client: fix auth crash @maxj-oai

> #10590 tui: preserve remote image attachments across resume/backtrack @charley-oai

> #11782 turn metadata followups @pash-openai

> #11773 [app-server] add fuzzyFileSearch/sessionCompleted @nornagon-openai

> #11756 codex-rs: fix thread resume rejoin semantics @maxj-oai

> #11799 fix(protocol): make local image test Bazel-friendly @joshka-oai

> #11796 Fix js_repl view_image test runtime panic @fjord-oai

> #11800 Fix js_repl in-flight tool-call waiter race @fjord-oai

> #11790 bazel: enforce MODULE.bazel.lock sync with Cargo.lock @joshka-oai

> #11674 feat(tui): render structured network approval prompts in approval overlay @viyatb-oai

> #11550 feat(tui) Permissions update history item @dylan-hurd-oai

> #11534 Add process_uuid to sqlite logs @charley-oai

> #11690 fix: show user warning when using default fallback metadata @sayan-oai

> #11780 chore(tui): reduce noisy key logging @apanasenko-oai

> #11893 bazel: fix snapshot parity for tests/*.rs rust_test targets @apanasenko-oai

> #11926 docs: mention Codex app in README intro @vb-openai

> #11866 chore(core) rm Feature::RequestRule @dylan-hurd-oai

> #11951 fix(core) exec_policy parsing fixes @dylan-hurd-oai

> #11932 fix: js_repl reset hang by clearing exec tool calls without waiting @jif-oai

> #11922 fix: race in js repl @jif-oai

> #11908 Exit early when session initialization fails @jif-oai

> #11995 feat: add `--search` to `just log` @jif-oai

> #11994 feat: add `--compact` mode to `just log` @jif-oai

> #12007 Update vendored rg to the latest stable version (15.1) @etraut-openai

> #11801 Add remote skill scope/product_surface/enabled params and cleanup @xl-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.102.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-17-3-developer-workflow-changes-in-rust-v0-102-0|3 Developer Workflow changes in rust-v0.102.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-17-11-model-support-changes-in-rust-v0-102-0|11 Model Support changes in rust-v0.102.0]] · Model Support
- [[Changes/Codex CLI/2026-02-17-15-apps-and-integrations-changes-in-rust-v0-102-0|15 Apps and Integrations changes in rust-v0.102.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-17-2-mobile-and-desktop-changes-in-rust-v0-102-0|2 Mobile and Desktop changes in rust-v0.102.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-17-9-safety-and-privacy-changes-in-rust-v0-102-0|9 Safety and Privacy changes in rust-v0.102.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-17-11860-fixed-screen-reader-regression-in-cli-etraut-openai|♯11860 Fixed screen reader regression in CLI @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-02-17-11224-chore-clarify-web-search-deprecation-notices-and-consolidate-tests-sayan-o|♯11224 chore: clarify web_search deprecation notices and consolidate tests @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-17-4-context-window-changes-in-rust-v0-102-0|4 Context Window changes in rust-v0.102.0]] · Context Window
- [[Changes/Codex CLI/2026-02-17-4-memory-and-personalization-changes-in-rust-v0-102-0|4 Memory and Personalization changes in rust-v0.102.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-17-3-interface-experience-changes-in-rust-v0-102-0|3 Interface Experience changes in rust-v0.102.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-17-7-agent-mode-changes-in-rust-v0-102-0|7 Agent Mode changes in rust-v0.102.0]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-17-a591e2&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-17-59-other-changes-in-rust-v0-102-0.md%0ACard%20ID%3A%20codex-cli-2026-02-17-a591e2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.102.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->