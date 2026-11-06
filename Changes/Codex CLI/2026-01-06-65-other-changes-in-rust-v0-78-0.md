---
card_id: codex-cli-2026-01-06-2cc418
date: '2026-01-06'
description: 'Codex CLI · 2026-01-06 · Other changes: 65 changes in 0.78.0 — Support
  project-aware config layering: load repo-local `.codex/config.toml`, honor configurable…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f97a52dbb78119cbc1eebeb30fddcd72a181d80be482fb358e00375890a61733
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-06-2cc418
  comparison: ''
  date: '2026-01-06'
  description: 'Codex CLI — 0.78.0: 65 other changes'
  evidence:
  - quote: 'Support project-aware config layering: load repo-local `.codex/config.toml`,
      honor configurable `project_root_markers`, and merge that with system config
      like `/etc/codex/config.toml`. (#8354, #8359, #8461)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: Start Windows PowerShell sessions in UTF-8 mode to reduce encoding-related
      prompt/output issues. (#7902)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: 'Exec policy rules can now include human-readable justifications, and policy
      loading follows the unified config-layer stack. (#8349, #8453, #8751)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: Make `/review` compute diffs from the session’s working directory so base-branch
      detection works correctly with runtime cwd overrides. (#8738)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: Handle the legacy Chat Completions streaming terminator cleanly to avoid
      spurious SSE parse errors. (#8708)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: Avoid a panic when parsing alpha/stable version strings. (#8406)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: 'Replace and de-duplicate user docs with links to the developer documentation
      site (including skills docs). (#8662, #8407)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: 'Clarify configuration documentation, including the `developer_instructions`
      option. (#8376, #8701)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: 'Update Rust dependencies across `codex-rs`. (#8414, #8596, #8597)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8407 Point skills docs to developer documentation site @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8406 fix: do not panic on alphas @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8423 test(tui2): re-enable ANSI for VT100 tests @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8424 chore: un-ship undo @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8376 docs: add `developer_instructions` config option and update descriptions
      @448523760'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8431 chore: drop undo from the docs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8412 chore(deps): bump test-log from 0.2.18 to 0.2.19 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8413 chore(deps): bump landlock from 0.4.2 to 0.4.4 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8414 chore(deps): bump clap from 4.5.47 to 4.5.53 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8416 chore(deps): bump openssl-sys from 0.9.109 to 0.9.111 in /codex-rs
      @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#7902 feat(windows) start powershell in utf-8 mode @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8349 Add ExecPolicyManager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8354 feat: support in-repo .codex/config.toml entries as sources of config
      info @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8359 feat: add support for project_root_markers in config.toml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8444 use a junction for the cwd while read ACLs are being applied @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8447 remove minimal client version @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8448 chore: add ConfigLayerStack as a field of Config @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8418 chore(tui): include tracing targets in file logs @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8456 chore: include User layer in ConfigLayerStack even if config.toml
      is empty @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8453 feat: load ExecPolicyManager from ConfigLayerStack @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8461 feat: honor /etc/codex/config.toml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8463 fix(tui2): fix screen corruption @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8293 [tui] add optional details to TUI status header @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8486 fix(codex-cli): improve ripgrep download diagnostics @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8493 fix: fix test that was writing temp file to cwd instead of TMPDIR
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8499 perf(tui): cap redraw scheduling to 60fps @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8498 fix: declare test path relative to `$CARGO_MANIFEST_DIR` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8307 [chore] add additional_details to StreamErrorEvent + wire through
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8522 fix: restrict windows-sys to Windows target @RunjiLiu'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8596 chore(deps): bump tracing-subscriber from 0.3.20 to 0.3.22 in /codex-rs
      @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8597 chore(deps): bump tokio from 1.47.1 to 1.48.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8598 chore(deps): bump regex-lite from 0.1.7 to 0.1.8 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8662 Replaced user documentation with links to developers docs site @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8681 perf(tui2): reduce unnecessary redraws @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8682 Fixed broken link in README @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8677 Account for last token count on resume @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8415 chore(deps): bump tracing-opentelemetry from 0.31.0 to 0.32.0 in
      /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8688 Attach more tags to feedback submissions @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8701 chore: update outdated docs @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8697 fix: brighten transcript copy affordance @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8629 ci: prevent workflows from running on forks @leezenn'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8695 fix(tui2): avoid scroll stickiness at cell boundaries @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8716 fix(tui2): render copy pill at viewport bottom @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8721 chore(deps): bump clap_complete from 4.5.57 to 4.5.64 in /codex-rs
      @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8723 chore(deps): bump tokio-stream from 0.1.17 to 0.1.18 in /codex-rs
      @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8724 chore(deps): bump derive_more from 2.0.1 to 2.1.1 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8725 chore(deps): bump insta from 1.44.3 to 1.46.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8556 fix: chat multiple tool calls @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8738 fix: /review to respect session cwd @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8708 fix(codex-api): handle Chat Completions DONE sentinel @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8377 feat: expose outputSchema to user_turn/turn_start app_server API
      @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8747 chore: GH pager @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8686 better idempotency for creating/updating firewall rules during setup.
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8459 chore: improve skills render section @gverma-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#7858 Use issuer URL in device auth prompt link @abrar71'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8751 feat: add justification arg to prefix_rule() in *.rules @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 65-other-changes-in-rust-v0-78-0
  source_release: codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a
  source_type: github_releases
  theme: uncategorized
  title: 65 other changes in rust-v0.78.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a]]'
source_type: github_releases
theme: uncategorized
title: 65 other changes in rust-v0.78.0
type: change
---

<!-- chronolog:begin region="header" -->
# 65 other changes in rust-v0.78.0

**Codex CLI** · 2026-01-06 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.78.0) · from [[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|0.78.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Support project-aware config layering: load repo-local `.codex/config.toml`, honor configurable `project_root_markers`, and merge that with system config like `/etc/codex/config.toml`. (#8354, #8359, #8461)

> Start Windows PowerShell sessions in UTF-8 mode to reduce encoding-related prompt/output issues. (#7902)

> Exec policy rules can now include human-readable justifications, and policy loading follows the unified config-layer stack. (#8349, #8453, #8751)

> Make `/review` compute diffs from the session’s working directory so base-branch detection works correctly with runtime cwd overrides. (#8738)

> Handle the legacy Chat Completions streaming terminator cleanly to avoid spurious SSE parse errors. (#8708)

> Avoid a panic when parsing alpha/stable version strings. (#8406)

> Replace and de-duplicate user docs with links to the developer documentation site (including skills docs). (#8662, #8407)

> Clarify configuration documentation, including the `developer_instructions` option. (#8376, #8701)

> Update Rust dependencies across `codex-rs`. (#8414, #8596, #8597)

> #8407 Point skills docs to developer documentation site @etraut-openai

> #8406 fix: do not panic on alphas @aibrahim-oai

> #8423 test(tui2): re-enable ANSI for VT100 tests @joshka-oai

> #8424 chore: un-ship undo @jif-oai

> #8376 docs: add `developer_instructions` config option and update descriptions @448523760

> #8431 chore: drop undo from the docs @jif-oai

> #8412 chore(deps): bump test-log from 0.2.18 to 0.2.19 in /codex-rs @dependabot

> #8413 chore(deps): bump landlock from 0.4.2 to 0.4.4 in /codex-rs @dependabot

> #8414 chore(deps): bump clap from 4.5.47 to 4.5.53 in /codex-rs @dependabot

> #8416 chore(deps): bump openssl-sys from 0.9.109 to 0.9.111 in /codex-rs @dependabot

> #7902 feat(windows) start powershell in utf-8 mode @dylan-hurd-oai

> #8349 Add ExecPolicyManager @pakrym-oai

> #8354 feat: support in-repo .codex/config.toml entries as sources of config info @bolinfest

> #8359 feat: add support for project_root_markers in config.toml @bolinfest

> #8444 use a junction for the cwd while read ACLs are being applied @iceweasel-oai

> #8447 remove minimal client version @aibrahim-oai

> #8448 chore: add ConfigLayerStack as a field of Config @bolinfest

> #8418 chore(tui): include tracing targets in file logs @joshka-oai

> #8456 chore: include User layer in ConfigLayerStack even if config.toml is empty @bolinfest

> #8453 feat: load ExecPolicyManager from ConfigLayerStack @bolinfest

> #8461 feat: honor /etc/codex/config.toml @bolinfest

> #8463 fix(tui2): fix screen corruption @joshka-oai

> #8293 [tui] add optional details to TUI status header @sayan-oai

> #8486 fix(codex-cli): improve ripgrep download diagnostics @joshka-oai

> #8493 fix: fix test that was writing temp file to cwd instead of TMPDIR @bolinfest

> #8499 perf(tui): cap redraw scheduling to 60fps @joshka-oai

> #8498 fix: declare test path relative to `$CARGO_MANIFEST_DIR` @bolinfest

> #8307 [chore] add additional_details to StreamErrorEvent + wire through @sayan-oai

> #8522 fix: restrict windows-sys to Windows target @RunjiLiu

> #8596 chore(deps): bump tracing-subscriber from 0.3.20 to 0.3.22 in /codex-rs @dependabot

> #8597 chore(deps): bump tokio from 1.47.1 to 1.48.0 in /codex-rs @dependabot

> #8598 chore(deps): bump regex-lite from 0.1.7 to 0.1.8 in /codex-rs @dependabot

> #8662 Replaced user documentation with links to developers docs site @etraut-openai

> #8681 perf(tui2): reduce unnecessary redraws @joshka-oai

> #8682 Fixed broken link in README @etraut-openai

> #8677 Account for last token count on resume @aibrahim-oai

> #8415 chore(deps): bump tracing-opentelemetry from 0.31.0 to 0.32.0 in /codex-rs @dependabot

> #8688 Attach more tags to feedback submissions @pakrym-oai

> #8701 chore: update outdated docs @tibo-openai

> #8697 fix: brighten transcript copy affordance @joshka-oai

> #8629 ci: prevent workflows from running on forks @leezenn

> #8695 fix(tui2): avoid scroll stickiness at cell boundaries @joshka-oai

> #8716 fix(tui2): render copy pill at viewport bottom @joshka-oai

> #8721 chore(deps): bump clap_complete from 4.5.57 to 4.5.64 in /codex-rs @dependabot

> #8723 chore(deps): bump tokio-stream from 0.1.17 to 0.1.18 in /codex-rs @dependabot

> #8724 chore(deps): bump derive_more from 2.0.1 to 2.1.1 in /codex-rs @dependabot

> #8725 chore(deps): bump insta from 1.44.3 to 1.46.0 in /codex-rs @dependabot

> #8556 fix: chat multiple tool calls @jif-oai

> #8738 fix: /review to respect session cwd @tibo-openai

> #8708 fix(codex-api): handle Chat Completions DONE sentinel @joshka-oai

> #8377 feat: expose outputSchema to user_turn/turn_start app_server API @apanasenko-oai

> #8747 chore: GH pager @jif-oai

> #8686 better idempotency for creating/updating firewall rules during setup. @iceweasel-oai

> #8459 chore: improve skills render section @gverma-openai

> #7858 Use issuer URL in device auth prompt link @abrar71

> #8751 feat: add justification arg to prefix_rule() in *.rules @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.78.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-06-3-safety-and-privacy-changes-in-rust-v0-78-0|3 Safety and Privacy changes in rust-v0.78.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-06-performance-tuning-for-tuis-cap-redraw-scheduling-and-reduce-unnecessary-rerende|Performance tuning for TUIs]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-06-8743-macos-load-config-requirements-from-mdm-gt-oai|♯8743 (MacOS) Load config requirements from MDM @gt-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-06-2-context-window-changes-in-rust-v0-78-0|2 Context Window changes in rust-v0.78.0]] · Context Window
- [[Changes/Codex CLI/2026-01-06-3-editor-experience-changes-in-rust-v0-78-0|3 Editor Experience changes in rust-v0.78.0]] · Editor Experience
- [[Changes/Codex CLI/2026-01-06-6-developer-workflow-changes-in-rust-v0-78-0|6 Developer Workflow changes in rust-v0.78.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-06-support-enterprise-managed-configuration-requirements-on-macos-via-an-mdm-provid|Support enterprise-managed configuration requirements on macOS via an MDM-provided…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-01-06-9-interface-experience-changes-in-rust-v0-78-0|9 Interface Experience changes in rust-v0.78.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-06-5-model-support-changes-in-rust-v0-78-0|5 Model Support changes in rust-v0.78.0]] · Model Support
- [[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694 MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-06-2cc418&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-06-65-other-changes-in-rust-v0-78-0.md%0ACard%20ID%3A%20codex-cli-2026-01-06-2cc418%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.78.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->