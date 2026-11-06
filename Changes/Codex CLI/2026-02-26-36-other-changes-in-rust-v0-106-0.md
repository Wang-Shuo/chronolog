---
card_id: codex-cli-2026-02-26-fdef36
date: '2026-02-26'
description: 'Codex CLI · 2026-02-26 · Other changes: 36 changes in 0.106.0 — Expanded
  the app-server v2 thread API with experimental thread-scoped realtime…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a5de881ea7299064be5e541acfc53cfa7fc2a1bbb35d687b3a6d964da8f5c32
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-26-fdef36
  comparison: ''
  date: '2026-02-26'
  description: 'Codex CLI — 0.106.0: 36 other changes'
  evidence:
  - quote: 'Expanded the app-server v2 thread API with experimental thread-scoped
      realtime endpoints/notifications and a `thread/unsubscribe` flow to unload live
      threads without archiving them (#12715, #10954)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: 'Promoted `js_repl` to `/experimental`, added startup compatibility checks
      with user-visible warnings, and lowered the validated minimum Node version to
      `22.22.0` (#12712, #12824, #12857)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: Added structured OTEL audit logging for embedded `codex-network-proxy`
      policy decisions and blocks (#12046)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: Removed the `steer` feature flag and standardized on the always-on steer
      path in the TUI composer (#12026)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12046 feat(network-proxy): add embedded OTEL policy audit logging @mcgrew-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12712 Promote js_repl to experimental with Node requirement @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12715 Add app-server v2 thread realtime API @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12791 Handle websocket timeout @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12802 Propagate session ID when compacting @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12732 feat(app-server): add ThreadItem::DynamicToolCall @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12807 Add simple realtime text logs @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12805 Update Codex docs success link @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12809 fix: harden zsh fork tests and keep subcommand approvals deterministic
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12808 make 5.3-codex visible in cli for api users @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#10954 feat(app-server): thread/unsubscribe API @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12806 only use preambles for realtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12830 Revert "only use preambles for realtime" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12831 only use preambles for realtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12735 Enable request_user_input in Default mode @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12814 feat: scope execve session approvals by approved skill metadata
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12026 Remove steer feature flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12811 Revert "Add skill approval event/response (#12633)" @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12824 Disable js_repl when Node is incompatible at startup @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12848 Try fixing windows pipeline @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12856 Attempt 2 to fix release @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12744 Skip system skills for extra roots @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12857 Reduce js_repl Node version requirement to 22.22.0 @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12865 Fix release build take @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12705 Hide local file link destinations in TUI markdown @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12823 Enforce user input length cap @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12885 nit: captial @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12870 tui: restore visible line numbers for hidden file links @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12901 chore: better awaiter description @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12905 chore: clean DB runtime @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12871 split-debuginfo @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12887 fix: do not apply turn cwd to metadata @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 36-other-changes-in-rust-v0-106-0
  source_release: codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db
  source_type: github_releases
  theme: uncategorized
  title: 36 other changes in rust-v0.106.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db]]'
source_type: github_releases
theme: uncategorized
title: 36 other changes in rust-v0.106.0
type: change
---

<!-- chronolog:begin region="header" -->
# 36 other changes in rust-v0.106.0

**Codex CLI** · 2026-02-26 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.106.0) · from [[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|0.106.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded the app-server v2 thread API with experimental thread-scoped realtime endpoints/notifications and a `thread/unsubscribe` flow to unload live threads without archiving them (#12715, #10954)

> Promoted `js_repl` to `/experimental`, added startup compatibility checks with user-visible warnings, and lowered the validated minimum Node version to `22.22.0` (#12712, #12824, #12857)

> Added structured OTEL audit logging for embedded `codex-network-proxy` policy decisions and blocks (#12046)

> Removed the `steer` feature flag and standardized on the always-on steer path in the TUI composer (#12026)

> #12046 feat(network-proxy): add embedded OTEL policy audit logging @mcgrew-oai

> #12712 Promote js_repl to experimental with Node requirement @fjord-oai

> #12715 Add app-server v2 thread realtime API @aibrahim-oai

> #12791 Handle websocket timeout @pakrym-oai

> #12802 Propagate session ID when compacting @rasmusrygaard

> #12732 feat(app-server): add ThreadItem::DynamicToolCall @owenlin0

> #12807 Add simple realtime text logs @aibrahim-oai

> #12805 Update Codex docs success link @etraut-openai

> #12809 fix: harden zsh fork tests and keep subcommand approvals deterministic @bolinfest

> #12808 make 5.3-codex visible in cli for api users @sayan-oai

> #10954 feat(app-server): thread/unsubscribe API @owenlin0

> #12806 only use preambles for realtime @aibrahim-oai

> #12830 Revert "only use preambles for realtime" @aibrahim-oai

> #12831 only use preambles for realtime @aibrahim-oai

> #12735 Enable request_user_input in Default mode @charley-oai

> #12814 feat: scope execve session approvals by approved skill metadata @bolinfest

> #12026 Remove steer feature flag @aibrahim-oai

> #12811 Revert "Add skill approval event/response (#12633)" @celia-oai

> #12824 Disable js_repl when Node is incompatible at startup @fjord-oai

> #12848 Try fixing windows pipeline @pakrym-oai

> #12856 Attempt 2 to fix release @pakrym-oai

> #12744 Skip system skills for extra roots @xl-openai

> #12857 Reduce js_repl Node version requirement to 22.22.0 @fjord-oai

> #12865 Fix release build take @pakrym-oai

> #12705 Hide local file link destinations in TUI markdown @pash-openai

> #12823 Enforce user input length cap @etraut-openai

> #12885 nit: captial @jif-oai

> #12870 tui: restore visible line numbers for hidden file links @pash-openai

> #12901 chore: better awaiter description @jif-oai

> #12905 chore: clean DB runtime @jif-oai

> #12871 split-debuginfo @pakrym-oai

> #12887 fix: do not apply turn cwd to metadata @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.106.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-26-2-account-and-access-changes-in-rust-v0-106-0|2 Account and Access changes in rust-v0.106.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-26-5-agent-mode-changes-in-rust-v0-106-0|5 Agent Mode changes in rust-v0.106.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-26-2-collaboration-changes-in-rust-v0-106-0|2 Collaboration changes in rust-v0.106.0]] · Collaboration
- [[Changes/Codex CLI/2026-02-26-improved-tui-local-file-link-rendering-to-hide-absolute-paths-while-preserving-v|Improved TUI local file-link rendering to hide absolute paths while preserving…]] · Interface Experience
- [[Changes/Codex CLI/2026-02-26-12417-core-bundle-settings-diff-updates-into-one-dev-user-envelope-charley-oai|♯12417 core: bundle settings diff updates into one dev/user envelope @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-02-26-4-model-support-changes-in-rust-v0-106-0|4 Model Support changes in rust-v0.106.0]] · Model Support
- [[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3 Memory and Personalization changes in rust-v0.106.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-26-2-mobile-and-desktop-changes-in-rust-v0-106-0|2 Mobile and Desktop changes in rust-v0.106.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-26-12758-feat-include-available-decisions-in-command-approval-requests-bolinfest|♯12758 feat: include available decisions in command approval requests @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-26-2-reliability-and-performance-changes-in-rust-v0-106-0|2 Reliability and Performance changes in rust-v0.106.0]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-26-fdef36&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-26-36-other-changes-in-rust-v0-106-0.md%0ACard%20ID%3A%20codex-cli-2026-02-26-fdef36%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.106.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->